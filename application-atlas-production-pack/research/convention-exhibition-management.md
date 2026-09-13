# Research Notes — Convention / Exhibition Management

Research date: 2026-09-07
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what software the directory leaf "Convention / Exhibition Management" refers to in the real market: what the show-organizer's system contains, how it differs from the neighboring Event Management Platform / Venue Management System / Exhibitor Management leaves, and which structure is definitional versus common implementation.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: this is the organizer-side system for producing trade shows / expositions / conventions, and its distinguishing structure (vs generic event management) is the exhibition floor as sellable space inventory plus the exhibitor population that occupies it.
- Nearest neighbors suspected: Event Management Platform (generic event lifecycle), Venue Management System (venue-side spaces), Exhibitor Management (directory sibling — likely a slice), Event Registration Platform (slice), Event Ticketing Platform (admission revenue), Festival Management (lineup/stage-shaped large events).
- Unknowns: whether attendee registration is definitional; whether "convention" (conference-shaped) and "exhibition" (floor-shaped) are one Type or two; historical/regional shape of the Type.

## Research Questions

1. What objects exist inside a show organizer's system? (show/edition, exhibitor, booth/space, floor plan, contract/payment, attendee, session, lead, sponsorship)
2. How is floor space sold, assigned, and kept from being double-sold?
3. How do exhibitors interact with the system (portal, listings, deadlines, leads)?
4. How do attendees interact (directory, floor plan, planner, app, registration)?
5. Where does registration live — in this system or at an integration seam?
6. How do conventions (session-heavy) and exhibitions (floor-heavy) combine in one product?
7. What is the recurring-economy of a show (rebooking, retention, renewal)?
8. What are the boundaries vs Event Management Platform, Venue Management, Exhibitor Management, Festival Management?

## Representative Products

| Product | Why selected | Position in market |
|---|---|---|
| Map Your Show (MYS) | Exhibition-first specialist; documents floor-plan + booth-sales machinery in depth | The Type's structural center |
| Swapcard | Attendee-experience / data-first platform; exhibitor operations as marketplace-style layer | Broad-suite pole with strong exhibitor layer |
| Cvent | Market-leading suite; trade-show solutions page + full product catalog observed | Broad-suite pole / boundary anchor |
| Stova | Merged suite (Aventri/MeetingPlay lineage); Exhibitor Resource Center + trade-show event type | Broad-suite pole, association/enterprise tier |
| RainFocus | Enterprise conference platform (Adobe-class conventions) | Boundary anchor toward Event Management Platform |

## Sources

All fetched 2026-09-07 from official vendor surfaces:

- Map Your Show: root (https://www.mapyourshow.com/), Floor Builder (https://www.mapyourshow.com/trade-show-exposition-floor-builder), Booth Sales (https://www.mapyourshow.com/trade-show-booth-sales) — Tier 2 product pages, feature-detailed.
- Swapcard: root (https://www.swapcard.com/), Exhibitor & Sponsor Tools (https://www.swapcard.com/features/exhibitor-sponsor-tools) — Tier 2 + FAQ.
- Cvent: Event Marketing & Management (https://www.cvent.com/en/event-marketing-management), Trade Show Solutions (https://www.cvent.com/en/event-marketing-management/trade-show-solutions), Products catalog (https://www.cvent.com/en/products) — Tier 2.
- Stova: root (https://stova.io/) — Tier 2.
- RainFocus: root (https://www.rainfocus.com/) — Tier 2 (help center not fetched).

Failed fetches (abandoned per network rule, one attempt each): expocad.com (404 — legacy floor-plan tool for §24 check). Not attempted: Cvent support KB (Salesforce-gated), RainFocus help center, Whova/EventMobi (stop conditions reached).

Source-access limitations:
- No Tier-1 help-center / user-guide articles were fetched for any product; all evidence is from official product/marketing pages and FAQs. Operational specifics (exact states, limits, defaults) are therefore NOT asserted.
- Legacy exhibition tools (expoCAD) unreachable → the historical check rests on inference and on observed lineage references (e.g., an MYS customer testimonial describing a switch from a2z), not on direct observation of legacy products.
- Vendor scale claims (MYS "1.7M exhibitors served", Swapcard "4,000+ events / 92+ countries / 7M+ attendees / 120,000+ exhibitors", Cvent "8.3M events") are vendor marketing figures — recorded as claims only, not used as evidence for structure.

## Product Observations

### Map Your Show (evidence layer: A — official product pages, feature-detailed)

- Positioning: "the growth engine for trade shows"; audiences: trade show organizers, conference organizers, corporate event organizers.
- **Floor Builder** (floor-plan machinery, A):
  - Create/edit/update dynamic event layouts "from simple booth arrangements to complex, real-time floor plan changes"; drag-and-drop; create, combine, split, customize booths; no CAD required; snap-to alignment; coordinate-based fine-tuning.
  - "Max Fit" floor plan upload guides booth placement and numbering; system compares current layout to Max Fit; booth numbers auto-adjust (product-specific mechanism).
  - Audit report identifies booths with sizing/placement/numbering errors.
  - Booth types, statuses, custom booth properties "at scale"; Booth Highlight colors by type/attribute.
  - Booth lock (temporary or permanent) to prevent accidental changes or reserve space.
  - Multi-user concurrent access; real-time updates (incl. live on-site rebooking on the floor plan).
  - Audience-scoped views: attendee view (labels/icons for POIs — restrooms, meeting rooms, food courts) vs exhibitor view (columns, venue entrances, utility locations) for strategic space selection.
  - Print/export floor plans (print-ready, and DXF/PDF export to the general service contractor so the GSC can update CAD files — single-product observation).
  - Advanced viewing/sorting/filtering by exhibitor name, space requests, booth sales status.
- **Booth Sales / MYS Sales Pro** (A):
  - Exhibitors view available spaces by size, self-select a booth from the live floor plan, compare pricing, complete transactions.
  - Applications gather exhibitor/sponsor information; "Sell by Space" model: collect space selections, competitor/partner listings, preferences — organizer assigns (vs self-select model). Both models documented in one product.
  - Sponsorship sales with real-time availability; on-platform advertising (banner placements, product spotlights); package upgrades across directory / interactive floor plan / mobile app.
  - Payments: invoicing and credit-card processing on-platform ("over 15 payment processors integrated" — vendor claim).
  - Reporting: real-time booth-sales and sponsorship dashboards, custom reports, trends, progress.
  - Onsite rebooking: secure next-year commitments on-site; renewals workflow; onsite rebooking service.
  - Customer quote (testimonial): "pull sales reports, send invoices, copies of signed contracts, collection notices… at the push of a button"; separate quote: "switched from A2Z to Map Your Show" (a2z = legacy exhibition-management suite; lineage evidence).
- **Exhibitor Resource Center** (A): centralized exhibitor portal to manage listings, meet deadlines, maximize promotional opportunities.
- **Attendee-facing** (A): Exhibitor Directory (online directory with exhibitor listings + advertising); My Show Planner (search exhibitors, schedule sessions, save exhibitors, personalized agenda); Mobile App (session scheduling, on-site navigation, real-time updates); MYS Smart Scan (attendees scan badges, booths, products).
- **Exhibitor value loop** (A): Sales Accelerator — AI for exhibitors to identify leads, find contacts, draft follow-up.
- **Conference machinery** (A): Conference Management — call-for-proposals, session schedules, education content promotion; Session Seat Reservations.
- **Registration** (A): Registration Integration product — MYS integrates external registration systems rather than owning registration natively.
- **Integrations** (A): CRM, payment processors, association management software (AMS).
- **Analytics** (A): MYS Insights — AI analytics predicting event sales, identifying at-risk exhibitors, benchmarks.

### Swapcard (evidence layer: A)

- Positioning: "revenue-first event management platform"; supports trade shows, conferences, association events; in-person/hybrid/online.
- Registration (A): multi-audience flows with conditional logic; dynamic ticketing/pricing (tiers, member rates, promo codes); embedded registration; onsite check-in with QR, badge printing, access control.
- Program (A): web+mobile app; multi-track programs, "unlimited session hierarchies"; abstracts, child/sub-child sessions, speaker coordination; AI recommendations (Sherlock AI — product-specific).
- Exhibitor machinery (A): Exhibitor Center — lead capture (badge scan pulls full attendee profiles; meetings, profile visits, chat messages auto-added to lead lists), centralized lead dashboard with sort/collaborate/export, AI recommended leads (behavior-based, in-exhibitor-dashboard), exhibitors can receive AND initiate meeting requests, shared team calendar; exhibitor profile editing on desktop and mobile for booth staff.
- Hosted buyer programs (A): Smart Meetings — match exhibitors/buyers by preferences and availability, automated scheduling, meetings in participant schedules, attendance/performance data.
- Monetization (A): ad placements (homepage spotlights, sponsored session banners, in-app placements) with impressions/clicks reporting.
- Exhibitor ROI (A): booth traffic, leads, meeting conversions, ad engagement, content views; retention framing ("rebook with confidence").
- Analytics (A): registration/intent data, engagement/behavior analytics, exhibitor & sponsorship performance, revenue insights; native exports and integrations.
- No floor-plan builder or booth-space inventory observed on the fetched pages (recorded as absence-of-observation, not industry claim).

### Cvent (evidence layer: A)

- Broad platform for event marketing & management across the lifecycle: registration & marketing, venue sourcing, vendor marketplace, event diagramming, repeatable events, hotel room blocks (Passkey), approvals/budgeting, speaker management; event app, check-in & badging (OnArrival), attendee engagement (Attendee Hub), trade-show lead capture (iCapture), trade-show meetings (Jifflenow), virtual, webinars; reporting, integrations, surveys, lead retrieval, AI content repurposing (product names are L3; capabilities are the evidence).
- "Manage speakers, sponsors, and exhibitors in one place" (platform page, A).
- Trade Show Solutions page (A): framed around the exhibitor value loop — "lock in meetings before the show, capture and qualify every lead on-site, follow up before the show floor closes": lead capture (badge/QR/business card scan, validation/enrichment, routing to reps, follow-up triggers), meeting scheduling (request/approve/confirm pre-show, SME matching, check-in, no-show tracking, pipeline dashboards), CRM/marketing syncs, APIs/webhooks.
- Products catalog (A): dedicated **Exhibitor Management** product ("manage exhibitor logistics and deliver ROI; streamline exhibitor tasks and communications"), Abstract Management (call for papers), Speaker Resource Center, Cvent Appointments (networking/appointment scheduling incl. exhibitors), Cvent LeadCapture ("allow your exhibitors and sponsors to collect, qualify, and follow up with leads").
- Event Diagramming (A): collaborative venue diagramming for layouts/seating — venue-design object, distinct from sellable booth inventory (boundary-relevant).
- No booth-sales / floor-plan-inventory product visible in the fetched catalog (absence-of-observation; Cvent's a2z lineage not verifiable from fetched pages — recorded limitation).

### Stova (evidence layer: A)

- Broad suite: Plan (event management platform, registration, session & speaker management, Exhibitor Resource Center), Engage (networking & engagement, marketing, virtual/webinars, websites), Experience (onsite services, mobile, event lead capture, access control & session scanning), Measure (Event Intelligence Suite: dashboards, cross-event analytics, registration intelligence, revenue monitoring; lead retrieval; event cloning; surveys).
- Exhibitor Resource Center (A): self-service portal for event guidelines, floor plans, deadlines, content submission; exhibitor preparation and task tracking pre-event.
- Event types (A): trade shows, small/mid/large conferences, sales kickoffs, regional/global events, field marketing, investor relations, training; roles include "Tradeshow Planners"; customers include trade-show organizers (RX — organizer group).
- Onsite (A): check-in kiosks, badge printing, access control, session scanning, lead retrieval.
- Floor-plan booth-sales machinery not observed on fetched pages.

### RainFocus (evidence layer: A)

- Enterprise event platform "for B2B events"; event types: conferences, kickoffs, roadshows, field marketing, sales activations, webinars; industries incl. associations; customers incl. major technology companies and RSA Conference (logo wall — market context only).
- Modules (A): Registration, Call for Papers, Speaker Enablement, Sponsor Activation, Attendee Engagement, Meetings Management, On-Site Experience, Mobile App, Performance & Strategy, Sales Enablement, Marketing Data, Portfolio Orchestration; agentic AI (Nexus — product-specific).
- Sponsor Activation (A) = sponsor-facing module; no exhibitor-booth sales / floor-plan machinery observed → serves as the boundary anchor toward Event Management Platform even for very large conventions.

## Cross-product Comparison

| Structure / capability | MYS | Swapcard | Cvent | Stova | RainFocus | Evidence layer |
|---|---|---|---|---|---|---|
| Show/edition as managed event unit | ✓ | ✓ | ✓ | ✓ | ✓ (portfolio) | B |
| Exhibitor records/profiles (companies) | ✓ | ✓ | ✓ | ✓ | ✓ (sponsor activation) | B |
| Floor plan as sellable booth/space inventory (states, assignment) | ✓ (defining product) | not observed | not observed (venue diagramming is design-side) | portal displays floor plans | not observed | A (single product) |
| Booth/space sale + contract + payment machinery | ✓ (core product) | not observed (registration monetization instead) | not observed | not observed | not observed | A (single product) |
| Exhibitor self-service portal (listings, deadlines, tasks, content) | ✓ | ✓ (Exhibitor Center) | ✓ (Exhibitor Management product) | ✓ | ✓ (Speaker Enablement analog for sponsors) | B |
| Exhibitor directory + attendee-facing floor plan | ✓ | ✓ (profiles/lists) | ✓ (Attendee Hub) | ✓ (portal guidance) | ✓ | B |
| Attendee registration & badging/check-in | via integration (✓ seam) | ✓ native | ✓ native | ✓ native | ✓ native | B |
| Program/sessions/speakers/CFP | ✓ (conference mgmt) | ✓ (abstracts, hierarchies) | ✓ (abstract mgmt, speaker center) | ✓ (session & speaker mgmt) | ✓ (call for papers, speaker enablement) | B |
| Attendee show planner + mobile app | ✓ | ✓ | ✓ (Attendee Hub/app) | ✓ | ✓ | B |
| Lead capture / lead retrieval for exhibitors | ✓ (Smart Scan, Sales Accelerator) | ✓ (lead dashboard, AI leads) | ✓ (iCapture, LeadCapture) | ✓ (lead retrieval) | n/s | B |
| Buyer–seller meeting scheduling / hosted buyer | ✓ (planner+scans) | ✓ (Smart Meetings) | ✓ (Appointments, Jifflenow) | ✓ (meeting scheduling) | ✓ (Meetings Management) | B |
| Sponsorship / advertising sales | ✓ (Sales Pro, on-platform ads) | ✓ (ad placements) | ✓ (sponsors managed) | n/s | ✓ (Sponsor Activation) | B |
| Exhibitor ROI / performance reporting | ✓ (Insights, at-risk) | ✓ (booth traffic, ROI) | ✓ | ✓ (Intelligence Suite) | ✓ (Performance & Strategy) | B |
| On-site rebooking / retention loop | ✓ (onsite rebooking) | ✓ (retention framing) | n/s | n/s | n/s | A (single product, positioned as differentiator) |
| GSC / contractor floor-plan exchange | ✓ (DXF/PDF export) | n/s | n/s | n/s | n/s | A (single product) |
| Multi-show portfolio management | n/s | ✓ ("dozens across regions") | ✓ (Access Portal) | ✓ (portfolio view, event cloning) | ✓ (Portfolio Orchestration) | B |
| AI personalization / matchmaking | ✓ (MYS Connected) | ✓ (Sherlock AI) | ✓ (CventIQ) | ✓ (AI matchmaking) | ✓ (Nexus) | B (era-common) |

Reading: the exhibitor population layer + attendee experience layer are cross-product common (B). The sellable-floor machinery (booth inventory + booth commerce + rebooking) is documented in depth only at the exhibition-first specialist — but it is precisely what the specialist considers its product spine, what broad suites lack or delegate, and what the customer testimonial lineage (a2z → MYS) treats as the category's defining substance. The broad suites' trade-show pages frame value around the exhibitor loop (leads/meetings), not the floor sale — consistent with the hypothesis that the floor/exhibitor structure is the Type's differentiator while everything else is shared event-platform substance.

## Canonical Model (four-level abstraction)

### L0 — Defining Invariant

An operator-side system for producing an exhibition/convention, whose smallest stable structure is:

```text
Show (dated, venue-bound, produced occasion; typically recurring editions)
└── Exhibitor population (companies/organizations paying to participate; identifiable records)
    └── Exhibition floor as sellable space inventory
        (floor plan decomposed into individually identified booth/space units with availability states)
        └── Exhibitor-to-space allocation binding
            (space application/selection → assignment → contract/payment for the specific space)
```

Test: remove the floor + space-sale machinery → generic Event Management Platform. Remove the exhibitor population → venue booking/diagramming. Remove the show container → CRM. Remove the commercial allocation binding → a directory/publishing tool. Each removal collapses the Type into a different one.

Note on what is deliberately NOT in L0:
- **Attendee registration** — the exhibition-first specialist (MYS) provides registration only as an integration; historically and structurally the registration function can live outside this system. It is L1.
- **Sessions/program/speakers** — conventions carry them, pure exhibitions may not; L1.
- **Mobile app / lead capture / matchmaking** — modern but not definitional; L1/L2.
- §24 historical check: the check rests on inference (legacy tools unreachable). Observed lineage evidence (a2z → MYS switch; the specialist's floor-plan-first spine; broad suites bundling registration natively) supports a core of floor+exhibitor+allocation that predates and can survive without the attendee-facing digital layer. Assertion kept at C-level (canonical inference).

### L1 — Common Mature Structure (standard capabilities across the researched sample)

- Exhibitor application → contract → payment machinery for space and non-space items (B: MYS explicit; Cvent exhibitor logistics; Swapcard monetization)
- Exhibitor self-service portal: listings/profile editing, deadlines, task tracking, content submission (B: MYS ERC, Swapcard Exhibitor Center, Cvent Exhibitor Management, Stova ERC)
- Public exhibitor directory with categories/search + interactive attendee-facing floor plan (B)
- Attendee registration, check-in, badging — native in suites, integration seam in the specialist (B)
- Session/agenda/speaker machinery incl. call-for-proposals for convention formats (B: all five)
- Attendee show planner (save exhibitors, schedule sessions) + event mobile app (B)
- Exhibitor lead capture/lead retrieval: badge scanning → lead lists → qualification → export/CRM sync (B: four of five)
- Buyer–seller meeting scheduling incl. hosted-buyer programs (B)
- Sponsorship and advertising sales with real-time availability and package upsells (B)
- Exhibitor/performance analytics: leads, meetings, booth traffic, ROI, retention-risk (B)
- Booth allocation operations: holds/locks, status types, reassignment during the sales cycle (A: MYS; assumed common — moderate phrasing in final doc)
- AI personalization/recommendations and AI exhibitor tooling (B: all five — era-common)

### L2 — Variant / Optional Structure

- Show-type segments: B2B trade show vs consumer/public expo vs association annual meeting + exhibit hall vs hosted-buyer market vs conference-with-expo vs corporate events (B)
- Space-selling model: sell-by-space (application + organizer assignment, documented "Sell by Space") vs exhibitor self-select of specific booths vs renewal/priority-based allocation (A: MYS documents multiple; general market phrased moderately)
- Registration ownership: native (suites) vs integrated (specialist) (B)
- Virtual/hybrid exhibition layers, event cloning, multi-show portfolios (B: Swapcard, Stova, RainFocus; Cvent Essentials/Access Portal)
- On-site operations depth: kiosks, badge printing hardware, access control, session scanning (B: Cvent OnArrival, Stova, Swapcard)
- Housing/room-block management for conventions (A: Cvent Passkey; single-product observation in sample)
- GSC/contractor coordination formats (DXF/PDF export — A: MYS, single product)
- AMS/CRM integration posture (association-run shows) (B: MYS AMS integration, RainFocus associations industry)

### L3 — Vendor-specific (research notes only)

- MYS: Max Fit layout comparison, Booth Lock, Booth Highlight, Sales Pro/ERC/Smart Scan/Connected naming, "over 15 payment processors", "1.7M exhibitors served" claim, a2z-switch testimonial.
- Swapcard: Sherlock AI, Exhibitor Center naming, adoption-rate claims (70–80% vs 30–40%), "4,000+ events / 92+ countries / 7M+ attendees / 120,000+ exhibitors" claims.
- Cvent: iCapture, Jifflenow, OnArrival, Attendee Hub, Passkey, CventIQ names; "8.3M events" / "89% of Fortune 100" claims.
- Stova: Event Intelligence Suite, event cloning naming, RX customer mention.
- RainFocus: Nexus agentic AI, Portfolio Orchestration naming.

## Rejected Findings (considered and not promoted)

- "Registration is the core" — rejected: the purest Type representative treats registration as an integration; suites are broader systems where registration serves all event types.
- "Mobile app is the core" — rejected: era-common L1; shows ran for decades without them.
- "AI matchmaking is the core" — rejected: era-common across all five sampled products; appears as differentiator packaging, not structure.
- "Floor-plan drawing tool = this Type" — rejected: Cvent's Event Diagramming draws venue layouts/seating without sellable-booth semantics; the Type requires the inventory + commerce semantics, not the drawing surface alone.
- "This Type = Event Management Platform with a trade-show page" — rejected: the sampled suites lack the floor-sale spine; conflating the two would erase the observed market division of labor (specialist + suite integrations).

## Boundary Findings

1. **vs Event Management Platform** (sharpest seam). EMP's center: event lifecycle (registration → engagement → measurement) for any event type. This Type's center: the sellable floor + exhibitor commerce. Structural test both directions: remove booth/floor machinery from a convention system → EMP; add sellable-booth inventory to EMP → this Type. Sampled suites (Cvent, Stova, RainFocus) sit on the EMP side even when serving trade shows; MYS sits on this Type's side; Swapcard straddles (carries both structures partially). Products straddle; the leaves stand.
2. **vs Exhibitor Management** (directory sibling, unprocessed at research time). Exhibitor Management is the exhibitor-population slice (records, portal, logistics, communications) — Cvent even sells it as a standalone product. Convention/Exhibition Management is the show-level system that contains that slice plus the floor inventory and space commerce. Probable parent-child / slice relationship — flagged for joint review; do not merge silently.
3. **vs Venue Management System**: different operator (venue vs organizer) and different object (bookable venue spaces vs the show's booth inventory). Cvent's own split (hospitality platform vs event platform) documents the seam.
4. **vs Event Registration Platform**: registration machinery slice; in this Type it may be native or an integration seam (A evidence for the seam).
5. **vs Event Ticketing Platform**: monetizes admission (attendee pays); this Type monetizes participation (exhibitor pays for space/services). Both may coexist in one show's stack.
6. **vs Festival Management**: festivals organize stages/lineups/ticketing for audiences; exhibitions organize exhibitors/booths for a marketplace. Both large-scale produced events; different core objects.
7. **vs Event Lead Retrieval / Event Agenda Management / Attendee Management** (directory siblings): slices of the exhibitor value loop, the program layer, and the audience layer respectively — bundled here, sold separately there.
8. **vs Event Diagramming** (capability inside several suites): authoring venue diagrams vs managing sellable booth inventory — the commerce semantics are the discriminator.

## Uncertainties

- Legacy/regional exhibition software (expoCAD and similar) could not be accessed; the §24 historical check is therefore inferential (C-level) rather than directly observed.
- Cvent's a2z-lineage exhibition product could not be verified from fetched surfaces; Cvent is treated as a broad-suite boundary anchor based on observed pages only.
- Whether every mature exhibition system enforces hard no-double-selling of booths (assumed; only MYS's locks/assignments directly observed) — phrased moderately in the final doc.
- Help-center-level operational detail (exact state names, permission models, payment terms machinery) not observed for any product — final doc avoids precise defaults/limits.
- Regional practices (e.g., European Messe model) unverified — sample is US-market-heavy; final doc keeps segment variants generic.

## Final Synthesis

Convention / Exhibition Management is the show organizer's operating system for producing exhibitions and conventions. Its defining core is the coupling of four structures: the produced show, the exhibitor population, the exhibition floor decomposed into individually identified sellable space units on a floor plan, and the allocation binding that assigns specific space to specific exhibitors against contracts and payments. Around that core, mature products assemble a standard capability set in two directions: an exhibitor-facing commerce and service layer (applications, contracts, portal, directory listings, advertising/sponsorship sales, lead capture, ROI reporting, rebooking) and an attendee-facing experience layer (registration, directory, floor plan, planner, app, meetings, sessions). Broad event platforms share the attendee layer and much of the exhibitor layer across all event types; what marks this Type as distinct is the sellable-floor structure and the exhibition-specific operating loop (lay out the floor → sell the floor → onboard exhibitors → build the audience and program → drive the match → run the show → settle leads/ROI → rebook the floor for the next edition).
