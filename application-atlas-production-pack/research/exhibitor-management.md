# Research Notes — Exhibitor Management

Research date: 2026-09-07
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what software the directory leaf "Exhibitor Management" (§26 Travel, Hospitality, Food Service & Events) refers to in the real market: what the system manages, who operates it (organizer vs exhibitor), what lifecycle and rules govern the exhibitor relationship, and — critically — how it holds its boundary against Convention / Exhibition Management (which owns the sellable floor), Event Lead Retrieval (exhibitor-side capture), Sponsor Management (parallel population slice), and Event Management Platform (generic lifecycle). This pass also discharges the joint-review flag left by the convention-exhibition-management pass ("probable parent-child/slice relationship — keep-both-with-containment vs fold").

## Initial Boundary (pre-research hypothesis)

- Hypothesis: this is the organizer-side system for managing the exhibitor relationship and participation logistics across the show cycle — exhibitor company records, onboarding, task/checklist coordination, document collection, communications, booth staff registration, and the exhibitor-facing self-service portal (Exhibitor Resource Center / Exhibitor Portal / Exhibitor Center).
- The floor-sale machinery (booth inventory, space commerce) belongs to Convention / Exhibition Management; Cvent sells Exhibitor Management as a standalone product without floor commerce, which supports a distinct core.
- Nearest neighbors: Convention / Exhibition Management (containment candidate), Event Management Platform (optional module pole), Event Lead Retrieval (different actor: exhibitor staff on the floor), Sponsor Management (parallel slice), Attendee Management (person population vs company population), Event Credential / Badge Management (badge machinery), Event Registration Platform (intake machinery).
- Unknowns at start: whether the exhibitor-facing portal is definitional or merely the dominant realization; whether payments/orders are core; whether booth association is core; how document collection works in practice; historical forms (paper exhibitor manual era); regional variants.

## Research Questions

1. Who operates the system — organizer, exhibitor, or both? What does each side control?
2. What is the core object? How is an exhibitor (company) different from an attendee (person) in the system?
3. What lifecycle does an exhibitor move through, and what states/deadlines matter?
4. How do tasks/checklists/deadlines work? Is the exhibitor manual a document or an interactive system?
5. How does document/content collection work (compliance documents, insurance, listings)?
6. What does the exhibitor portal let the exhibitor do itself?
7. How do booth association, staff registration, payments/orders, and lead/ROI visibility attach to the exhibitor record?
8. Where is the boundary vs Convention / Exhibition Management, Event Management Platform, Event Lead Retrieval, Sponsor Management?
9. What did the pre-digital form of this work look like (historical check)?

## Representative Products

| Product | Why selected | Position in market |
|---|---|---|
| Cvent Exhibitor Management | The market anchor — sold under this exact name as a standalone product; enterprise tier | Dedicated-product pole, organizer-console-led |
| Map Your Show (Exhibitor Resource Center) | Exhibition-first specialist; ERC documented in depth; its floor/booth-sales products are separate — vendor product split documents the seam | Exhibition-specialist module pole, exhibitor-hub-led |
| Whova (Exhibitor & Sponsor Management) | Mid-market all-in-one; richest reachable documentation of intake, document hub, and staff registration | Accessible platform-module pole, conference/SMB tier |
| Swapcard (Exhibitor Center) | AI-first platform; exhibitor value/ROI-centric framing | AI-first platform pole |
| Stova (Exhibitor Resource Center) | Suite module, association/enterprise tier (carried from convention pass fetch) | Broad-suite pole |
| vFairs (exhibitor portal) | Platform module with dedicated exhibitor portal and named team roles (carried from event-lead-retrieval pass) | Mid-market platform pole |

Six products, four fresh fetches this pass + two same-day observations carried from sibling passes' official-page fetches. Different philosophies (dedicated product / exhibition specialist / all-in-one / AI-first / enterprise suite) and different customer tiers (enterprise show organizers, associations, mid-market conferences, SMB expos).

## Sources

All fetched 2026-09-07 from official vendor surfaces:

- Cvent Exhibitor Management: https://www.cvent.com/en/event-marketing-management/exhibitor-management — Tier 2 product page, feature-detailed.
- Map Your Show Exhibitor Resource Center: https://www.mapyourshow.com/exhibitor-resource-center — Tier 2 product page, feature-detailed.
- Swapcard Exhibitor & Sponsor Tools: https://www.swapcard.com/features/exhibitor-sponsor-tools — Tier 2 + FAQ.
- Whova Exhibitor & Trade Show Management: https://whova.com/trade-show-app-lead-retrieval/ — Tier 2 product page + FAQ.
- Stova root page (Exhibitor Resource Center description): https://stova.io/ — Tier 2, fetched 2026-09-07 in the convention-exhibition-management pass (research/convention-exhibition-management.md).
- vFairs exhibitor portal / lead capture setup pages — Tier 2, fetched 2026-09-07 in the event-lead-retrieval pass (research/event-lead-retrieval.md).

Failed fetches this pass (abandoned per network rule, 2 attempts each): stova.io/exhibitor-management (404), stova.io/products/ (404), vfairs.com/exhibitor-management (404), vfairs.com/event-management-software (404), whova.com/exhibitor-center/ (redirect to homepage), cvent.com/en/products/exhibitor-management (404 — correct URL found on second guess).

Source-access limitations:
- No Tier-1 help-center / user-guide articles were fetched for any product; all evidence is from official product/marketing pages and FAQs. Operational specifics (exact states, permission ladders, numeric limits, default deadlines) are therefore NOT asserted anywhere.
- Stova and vFairs observations rest on their official root/setup pages fetched the same date by sibling passes; their exhibitor-management-specific product pages were unreachable this pass. Observations from those two are marked as carried evidence and never used as the sole support for a definitional claim.
- Vendor scale/engagement figures (MYS "1.7 Million Exhibitors", Whova "88% adoption / 17,593 leads / 62,971 vendor impressions") are vendor marketing claims — recorded as claims only, never used as structural evidence.

## Product Observations

### Cvent Exhibitor Management (evidence layer: A — official product page)

- Positioning: "Enhance exhibitor & sponsor logistics, engagement, and ROI with ease"; "Managing exhibitors is one of the most important and time-consuming parts of your job. Save time by streamlining exhibitor tasks and communications, eliminating the need for back-and-forth coordination." Retention framing: "Ensure they're getting value from your event – and that you're able to prove it – so that they keep coming back each year." (A)
- Feature blocks (A):
  - **Exhibitor Portal** — "a central location where admins can manage and see all things related to their events. Uploading company descriptions and keeping track of tasks has never been easier." Capabilities: "Create and assign tasks", "View task completion details", "Hands-off management of exhibitor profiles", "Self-serve registration for booth staff". The "admins" here are exhibitor-side admins managing their own participation.
  - **Booth management** — "an automated, centralized solution for managing show floors… updating floor plans, booth selections, and exhibitor coordination": "Increase transparency with detailed booth information", "Manage real-time booth associations efficiently", "Control booth selection visibility", "Streamline booth assignments". (Exhibitor↔booth association machinery; no floor-plan layout editing or space commerce on this page.)
  - **Booth staff registration & appointments** — self-serve booth staff registration; "Attendees can view exhibitor profiles and request meetings directly, while exhibitor admins can manage their booth staff's calendars in the Exhibitor Portal": "Control personal & team calendars", "View accepted appointments with contacts", "Share availability with attendees", "Set parameters for meeting times".
  - **Task management & reports** — create/assign tasks, view completion details (population-level visibility).
  - **Sponsored sessions & exhibitor packages** — exhibitor-facing commerce packages.
  - **Lead retrieval & reporting** — "Streamline the purchase of LeadCapture licenses or rental devices"; "Customize questions for each exhibitor"; "Export leads on-demand and view in real-time"; "Comprehensive reporting and visibility into event performance".
  - **Communications** — "Ensure your exhibitors are providing the information and content you need on time, and give them one central location to manage everything they need for the event they're exhibiting at": "Automate pre-and post-event emails", "Send reminders and access codes quickly", "Align exhibitor communications with your event's branding", "Create branded emails to match your event's theme".

### Map Your Show — Exhibitor Resource Center (evidence layer: A — official product page)

- Positioning: "Make staying on top of listings, deadlines, and promotions simple"; "It's hard for trade show and event exhibitors to stay on top of show deadlines and critical promotional opportunities. The… Resource Center makes it simple for exhibitors to stay on top of their online listing, critical deadlines, and promotional opportunities." (A)
- **Exhibitor Portal**: "Create a landing page for your exhibitors to highlight all of the key information and dates. Encourage your exhibitors to set up their online profile, view and pay their balance, and see their leads from the event." (A)
- **Exhibitor Checklist**: "The Checklist operates as the central hub for your exhibitors. List and track action items for your exhibitors to complete." Task List: "Create categories of 'to-do' tasks, and connect a vendor to a specific task on the checklist" (service-vendor linkage — e.g., connecting a decorator/vendor to a task). Email Reminders: "Create reminder emails before checklist items are due so your exhibitors stay on track with show deadlines." (A)
- **Exhibitor Resources**: "your exhibitors can search and find all of the key event information and files. Link resource files to widgets and checklist items." (A)
- **Data Management**: "Exhibitors can add and update their brand information and changes are available immediately in My Show Planner and the Mobile App." (A — propagation of exhibitor edits to audience surfaces)
- **Lead Tracking**: "Allow exhibitors to see leads and stats within the exhibitor portal. Exhibitors can connect with attendees who add the exhibitor to My Show Planner." (A)
- **Payment Management**: "Add the MYS Booth Sales Product and integrate with a payment gateway to allow exhibitors to purchase booth space, upgrade packages, and other items. Let the exhibitor make payments at scheduled times leading up to the event." (A — payments available in the ERC, but space purchase is explicitly the separate Booth Sales product; installment/scheduled payments documented)
- **Single Sign On**: "single sign on integration with registration, housing and show services so exhibitors have all of their logins, all in one place. Exhibitors can create a personalized login for every member of the team." (A)
- **Sponsorship Sales**: "Add the Booth Sales product to give exhibitors the ability to purchase advertising and sponsorships directly in the ERC." (A)
- **Communications**: "Send notifications to exhibitors with critical information before, during, and after the event." (A)
- Organizer-side control: "The back-end management and functionality allows us to customize and tailor the experience to the special needs of the show and specific industry" (customer testimonial, A-as-claim). MYS ships ERC as a product separate from Floor Builder and Booth Sales (nav structure, A) — the vendor's own product split documents the exhibitor-ops vs floor-commerce seam.
- Custom Widgets: template widgets for fast setup; widget library; custom widgets. (A)

### Whova — Exhibitor & Trade Show Management (evidence layer: A — official product page + FAQ)

- Nav positioning: "Exhibitor & Sponsor Management — Boost exhibitor & sponsor ROI with digital profiles, lead retrieval, sponsor banners in 20+ places, outreach campaigns, gamification and logistics management." (A)
- **"Save Time by Streamlining and Centralizing Exhibitor Management"** block (A):
  - Intake through registration: "Effectively gather exhibitors and sponsors through registration — Enable exhibitor booth selection, sponsor tier, a-la-carte sponsorship with secure & fast payment collection."
  - Self-service profiles: "Empower exhibitors to build and customize their own booth profiles through the exhibitor portal."
  - **Document collection hub**: "Central hub to collect, track and manage important documents — Effortlessly gather compliance documents through a single dashboard with automatic reminders and real-time tracking."
  - Communication channel: "Facilitate communication between organizers and exhibitors through dedicated channel for important announcements and information."
  - Expo websites: "Generate customizable exhibitor and sponsor webpages with automatic updates."
- **Exhibition registration flows** (A): "booth reservation for exhibitors during registration — Allow exhibitors to pick their booth spaces while they register for their tickets"; "Facilitate booth staff registration with exhibitor access to edit information — Allow exhibitors to directly add booth staff information once they know who will attend"; bonus add-ons ("sponsorship opportunities or booth amenities"); payment flexibility ("credit/debit cards, check, wire and invoice payment methods"); "custom question forms to accommodate specific exhibitor tiers"; "Easily track orders and sales — Keep track of exhibitor ticket sales and orders for analysis and reporting".
- **Online booths** (A): customizable interactive booths, tiering ("Give top exhibitors the best booth visibility and more time in the Virtual Exhibitor Hall"), product videos, livestream showcases, brochures/photos, gallery layout.
- **Lead generation for exhibitors** (A): coupons/giveaways, QR scan + manual entry + virtual booth interactions, export to CRM, gamification ("Passport Contest and Leaderboard"), 1-1 messaging, virtual business cards, SmartProfiles.
- Retention framing: "Help your exhibitors generate more business so they come back to your trade show year after year." (A)
- FAQ self-definition of the surrounding category: "Trade show management software is a specialized digital platform that centralizes the planning and execution of exhibitions. It replaces fragmented spreadsheets by consolidating interactive floor plans, exhibitor registration, and financial tracking into one streamlined workflow." (A — useful as the market's own articulation of the pre-software state: spreadsheets)

### Swapcard — Exhibitor & Sponsor Tools (evidence layer: A — official page + FAQ)

- "Swapcard helps you provide exhibitors with management tools that go beyond contact info and deliver the context needed to close deals." (A)
- **Exhibitor Center** as the exhibitor-facing hub (A): leads "automatically centralized in the Exhibitor Center, with tools to qualify, tag, and export them"; AI recommended leads "appear directly inside each exhibitor's dashboard"; exhibitors "can both receive and initiate meeting requests… manage a shared team calendar"; "All exhibitor tools, including meeting schedules, lead dashboards, and profile editing, are available on both desktop and mobile, making it easy for booth staff to stay organized on the show floor."
- ROI framing (A): "exhibitor booth traffic, number of leads, meeting conversions, ad engagement, and content views… the evidence they need to assess performance and rebook with confidence."
- Hosted buyer: "Organizers can create structured matchmaking programs using Smart Meetings, where exhibitors and buyers are automatically matched based on preferences and availability." (A)
- FAQ articulation of the exhibitor's expectation: "Exhibitors and sponsors expect more than just digital exposure. They want qualified leads, brand visibility, streamlined scheduling, and clear performance metrics they can use to justify their investment." (A)

### Stova — Exhibitor Resource Center (evidence layer: A, carried from research/convention-exhibition-management.md — fetched 2026-09-07 from stova.io root)

- "Exhibitor Resource Center: self-service portal for event guidelines, floor plans, deadlines, content submission; exhibitor preparation and task tracking pre-event." (A, carried)
- Ships inside a broad suite (Plan pillar); trade-show organizer customers (RX). (A, carried)

### vFairs — exhibitor portal (evidence layer: A, carried from research/event-lead-retrieval.md — fetched 2026-09-07)

- Setup split: "Configure the lead capture app within the same vFairs backend as the rest of your event" (organizer side) + "Give exhibitors access to a dedicated portal to configure their booth and invite teammates for collaboration" (exhibitor side). (A, carried)
- Team roles inside the exhibitor: "booth managers, and booth reps" with varying access degrees. (A, carried)

## Cross-product Comparison

| Structure / capability | Cvent EM | MYS ERC | Whova | Swapcard | Stova | vFairs | Layer |
|---|---|---|---|---|---|---|---|
| Exhibitor as company-level record with its own people (contacts/admins/booth staff) | ✓ (booth staff admins) | ✓ (per-team logins) | ✓ (staff info editing) | ✓ (team calendar) | ✓ | ✓ (booth managers/reps) | B |
| Organizer console over the exhibitor population | ✓ (tasks, booth, comms, reports) | ✓ (back-end management) | ✓ (dashboards) | ✓ | ✓ | ✓ (backend config) | B |
| Exhibitor-facing self-service portal bound to own record | ✓ (Exhibitor Portal) | ✓ (ERC) | ✓ (exhibitor portal) | ✓ (Exhibitor Center) | ✓ (ERC) | ✓ (dedicated portal) | B |
| Task/checklist/deadline machinery | ✓ (create/assign, completion) | ✓ (checklist hub, reminders) | ✓ (documents w/ reminders + tracking) | n/e (fetched pages) | ✓ (task tracking) | ✓ (config templates) | B |
| Document/content collection | ✓ ("information and content… on time") | ✓ (resources linked to checklist) | ✓ (compliance documents hub) | n/e | ✓ (content submission) | ✓ (booth config) | B |
| Listing/profile editing propagating to audience surfaces | ✓ (profile mgmt) | ✓ (immediate in planner+app) | ✓ (webpages auto-update) | ✓ (profile editing) | n/e | ✓ (booth config) | B |
| Organizer↔exhibitor communications | ✓ (pre/post emails, reminders, access codes, branded) | ✓ (notifications before/during/after) | ✓ (announcement channel) | n/e | n/e | n/e | B |
| Self-serve booth staff registration | ✓ | ✓ (team logins, indirect) | ✓ | ✓ (booth staff on mobile, indirect) | n/e | ✓ (invite teammates) | B |
| Exhibitor↔booth association / assignment | ✓ (booth management block) | booth in other MYS products | ✓ (booth selection at registration) | n/e | ✓ (floor plans in portal) | ✓ (configure booth) | B |
| Orders/payments/balances | ✓ (LeadCapture purchase streamlining) | ✓ (balance, payment schedules — via Booth Sales) | ✓ (payment methods, order tracking, add-ons) | n/e | n/e | n/e | B (packaging varies) |
| Lead stats & ROI visibility in the exhibitor's surface | ✓ (LeadCapture reporting) | ✓ (lead tracking) | ✓ (export/ROI framing) | ✓ (dashboards) | n/e | ✓ (lead dashboard) | B |
| Buyer–seller appointments/meetings | ✓ (staff calendars) | n/e | ✓ (SmartProfiles/meetings) | ✓ (Smart Meetings) | n/e | n/e | B |
| Virtual/online booths + tiering | n/e | n/e | ✓ | ✓ (virtual interactions, ads) | n/e | ✓ (virtual booths) | B |
| Packages/sponsorship/advertising sales to exhibitors | ✓ (packages, sponsored sessions) | ✓ (via Booth Sales) | ✓ (tiers, a-la-carte) | ✓ (ad placements) | n/e | n/e | B |
| Integration spine (registration / housing / show services / SSO) | suite-native | ✓ (SSO explicit) | registration-native | platform-native | suite-native | platform-native | B |

Reading: (1) the two-sided portal structure is present in all six products and is the named centerpiece of four (Exhibitor Portal / ERC / Exhibitor Center / dedicated portal) — B-layer commonality; (2) tasks/checklists/deadlines + document/content collection + communications form one functional cluster (the obligation loop) evidenced across all six; (3) exhibitor-side profile/listing editing with propagation to audience surfaces is universal; (4) booth association appears everywhere but with very different machinery depth — from a full booth-management block (Cvent) to booth-selection-at-registration (Whova) to floor plans merely displayed in the portal (Stova) — while floor-plan layout editing and space commerce appear in none of the six sampled products' exhibitor-management surfaces (MYS ships them as separate products); (5) payments/orders and lead/ROI visibility are common but packaged differently (sometimes via separate commerce/lead products).

## Canonical Model (four-level abstraction)

### L0 — Defining Invariant

An organizer-side system for managing the participating companies' journey through a show, whose smallest stable structure is:

```text
The show's exhibitor program
└── Exhibitor record (the participating company — an organization-level managed unit
    carrying its own people, listing content, space reference, and entitlements)
    └── Participation obligations (organizer-defined tasks, deadlines, documents,
        and content required from each exhibitor)
        └── worked jointly to completion: organizer defines/verifies,
            exhibitor completes through its own self-service surface
            bound to the exhibitor's own record
```

Three structures. Removal tests:

- Remove the exhibitor company record (keep people) → Attendee Management / a contacts tool.
- Remove the obligation loop (keep records + listing) → an exhibitor directory / profile listing tool.
- Remove exhibitor-side completion (keep organizer-side tracking) → an organizer-internal tracker — a spreadsheet/CRM, not an exhibitor relationship system; the exhibitor stops being an actor in the system.

Note on what is deliberately NOT in L0:
- **The digital portal as a specific artifact** — the exhibitor-side completion structure predates the portal: the paper exhibitor manual + return-forms loop (organizer-defined deadlines and forms, exhibitor-side completion, organizer verification) satisfies all three structures non-digitally (§24 historical check passed at the structural level; see Uncertainties). The portal is the standard modern realization (L1) and the near-universal named centerpiece.
- **Booth/space inventory and space commerce** — the exhibitor record carries a space reference, but the floor plan as sellable inventory and the sale of space belong to Convention / Exhibition Management.
- **Lead capture on the floor** — belongs to Event Lead Retrieval; this Type holds the exhibitor-side visibility of results.
- **Payments** — common but packaged variously (native, registration-based, or via a separate commerce module).
- **Attendee registration, event app, agenda** — sibling layers consumed by or feeding the exhibitor program.

### L1 — Common Mature Structure (standard capabilities across the sample)

- **Intake into the exhibitor population**: application or exhibitor-registration forms with tiers, packages, add-ons, and often booth selection at intake (A: Whova explicit; B: packages/tiering across Cvent, MYS-via-Booth-Sales, Swapcard).
- **Listing/profile management**: exhibitors build and edit their own company profile/booth content; edits propagate to audience-facing surfaces (directory, planner, app, expo webpages) — A: MYS ("changes are available immediately"), Whova ("automatic updates"); B: four more.
- **Task/checklist machinery**: organizer-defined task categories and items with deadlines; completion tracked per exhibitor; automatic/email reminders before due dates; in one product, tasks linked to service vendors (A: MYS, Cvent; B: Whova documents documents-with-reminders, Stova task tracking).
- **Document & content collection hub**: required documents (compliance-class) and content (company descriptions, media) gathered through one dashboard with reminders and real-time tracking (A: Whova, Cvent, MYS; B: Stova).
- **Organizer↔exhibitor communications**: branded pre/post-event emails, deadline reminders, access codes, dedicated announcement channels (A: Cvent, MYS, Whova).
- **Booth staff registration**: self-serve by the exhibitor, with per-team access; staff feed badge/check-in machinery and appointment calendars (A: Cvent, Whova; B: vFairs teammates, MYS per-team logins).
- **Orders/payments/balances**: exhibitors view balances, pay on schedules, buy add-ons/packages; organizer tracks orders/sales (A: MYS, Whova; B: Cvent).
- **Lead & ROI visibility**: leads and stats surfaced in the exhibitor's own surface; export; performance reporting used for retention ("rebook with confidence" framing) (B: five of six).
- **Buyer–seller appointments**: attendee-requested or matched meetings managed against booth-staff calendars (B: Cvent, Swapcard, Whova).
- **Virtual/online booths and tiered visibility** (B: Whova, Swapcard, vFairs).
- **Integration spine**: registration, floor plan, housing/show services, directory/app, SSO for exhibitor teams (A: MYS SSO; B: platform-native elsewhere).

### L2 — Variant / Optional Structure

- **Packaging pole**: dedicated standalone product (Cvent) vs exhibition-specialist module (MYS ERC) vs all-in-one platform module (Whova, vFairs, Stova, Swapcard). The same vendor may sell floor machinery and exhibitor ops as separate products (MYS) — packaging documents the seam.
- **Console-first vs hub-first**: organizer-console-led (Cvent task/booth management) vs exhibitor-hub-led (MYS ERC as "the central hub").
- **Space-machinery depth**: booth reference only vs booth selection during registration vs a booth-management block (associations/assignments/selection visibility, Cvent) — full floor inventory + space sale remains the sibling Type.
- **Show-type scope**: B2B trade show, consumer/public expo, conference exhibit hall, association annual show (B: Whova serves expos/conferences/associations; MYS trade shows; Cvent trade shows + sponsors).
- **Virtual/hybrid exhibitor surfaces** depth (B).
- **Payment ownership**: native registration flows vs separate commerce module vs invoice-only (B).
- **Sponsor bundling**: market labels bundle "exhibitor & sponsor" (Cvent, Whova) — populations and obligation sets differ; sibling leaf expected to hold its own Type.

### L3 — Vendor-specific (research notes only)

- Cvent: LeadCapture license/rental purchase streamlining; "control booth selection visibility"; Appointments Premium; branded-email tooling; the "8.3M events" claim.
- MYS: ERC naming; checklist widgets; vendor-to-task linkage; SSO across registration/housing/show services; "1.7 Million Exhibitors" claim; the Group Show Director testimonial; Booth Sales/Max Fit/Sales Pro as separate products.
- Whova: Passport Contest/Leaderboard gamification; SmartProfiles; tiered Virtual Exhibitor Hall time; "20+ places" sponsor banners; 88% adoption / 17,593 leads / 62,971 impressions claims; payment-method list.
- Swapcard: Sherlock AI; Exhibitor Center naming; Smart Meetings hosted-buyer machinery; ad placements with impression/click reporting.
- Stova: ERC naming inside the Plan pillar; event cloning (suite context).
- vFairs: booth manager / booth rep role naming; configuration templates reusable across events.

## Rejected Findings (considered and not promoted)

- "Lead capture is the core" — rejected: floor capture is Event Lead Retrieval's defining act (different actor — exhibitor staff reading attendee credentials on the show floor). Here, leads appear as results/ROI visibility attached to the exhibitor record. The event-lead-retrieval pass itself drew the line ("Remove capture (keep booth logistics) → Exhibitor Management").
- "The floor plan / booth inventory is the core" — rejected: no sampled exhibitor-management surface edits floor layouts or sells space; MYS ships those as separate products; Cvent's booth block is exhibitor↔booth association, not inventory commerce. Floor machinery is Convention / Exhibition Management's defining core.
- "Payments are definitional" — rejected: machinery varies (registration-native, commerce module, invoice-only); free/community exhibitor programs are coherent without it.
- "Meeting scheduling is definitional" — rejected: attendee↔exhibitor matchmaking is a common module (sometimes its own product — Cvent Appointments), not the relationship core.
- "Sponsors are part of this Type" — rejected: market bundles the two populations in labels and product scope, but the sponsor is a distinct managed population (packages/visibility, not space obligations); a sibling leaf exists — keep-both expected at that pass.

## Boundary Findings

1. **vs Convention / Exhibition Management — joint-review flag DISCHARGED from this side; keep-both with containment ratified.** The convention/exhibition Type's defining core is the produced show + exhibitor population + the exhibition floor as sellable space inventory + the exhibitor-to-space allocation binding and space commerce. Exhibitor Management holds the exhibitor-relationship operations layer: company records, the obligation loop, and two-sided self-service — machinery that stands alone for conference-with-expo, consumer expo, and association contexts, and is sold standalone (Cvent ships it as its own product without floor commerce; MYS ships ERC as a separate product from Floor Builder/Booth Sales — vendor product splits document the seam). Removal tests both ways: remove floor inventory + space sale from a show OS → exhibitor management remains meaningful and marketable; remove the exhibitor ops (records/obligations/portal) from a show OS → floor/sales tooling with nobody onboarded or serviced. The relationship is containment (convention Type contains this slice), not alias — consistent with how the directory already treats Event Lead Retrieval, Attendee Management, and Event Agenda Management as slices of the event family.
2. **vs Event Management Platform** — EMP's center is the event lifecycle for any event type; its own pass recorded exhibitors/sponsors as *optional* modules. This Type's center is the exhibitor population's relationship. Broad suites straddle by bundling; both Types stand.
3. **vs Event Lead Retrieval** — different actor and object: lead retrieval = exhibitor *staff* capturing *attendee* credentials on the floor; exhibitor management = the *organizer* managing the *exhibitor company* across the cycle. Lead stats/ROI visibility here consumes what capture produces. Seam held from both sides.
4. **vs Attendee Management** — person population with attendance lifecycle vs company population with participation obligations. At conference scale both run in parallel; exhibitor staff typically enter the attendee layer for badge purposes while the company record stays here.
5. **vs Sponsor Management (sibling, unprocessed)** — parallel population slice. Direct evidence of bundling: Cvent's product page and Whova's nav label cover "exhibitor & sponsor" jointly. Populations and obligation sets differ (booth/logistics/documents vs packages/visibility/advertising). Flag for that pass: expect keep-both with the same containment pattern; joint review recommended.
6. **vs Event Credential / Badge Management** — badge production/issuance is its own machinery; booth staff rosters maintained here are a feeding source. vFairs/MYS per-team logins and Cvent self-serve staff registration document the handoff seam.
7. **vs sales CRM** — exhibitor records look CRM-like, but the obligations are event-participation-shaped (deadlines, documents, staff rosters, listing content) and the loop is show-cycle-bounded; Whova's own FAQ names the pre-software state as "fragmented spreadsheets." Sales CRM remains an adjacent consumer of exhibitor data, not this Type.

## Uncertainties

- Stova and vFairs evidence is carried from same-date sibling-pass fetches of their official pages; their dedicated exhibitor-management product pages were unreachable this pass (404 ×2 each — abandoned per network rule). Their observations were never used as sole support for a definitional claim.
- No Tier-1 help-center articles reached for any product → no precise state names, permission ladders, numeric limits, or default deadline schemes asserted anywhere; final doc phrases rules at conceptual level.
- Document-collection depth (approval workflows, insurance-certificate specifics) is directly evidenced only as "compliance documents… automatic reminders and real-time tracking" (Whova) and content-deadline enforcement (Cvent) — kept general in the final doc.
- Historical check is structural: the paper exhibitor-manual era (manual + forms + organizer tracking) satisfies the L0 structures by construction, but no legacy exhibitor-administration product documentation was directly fetched; assertion kept at C-level (canonical inference).
- Regional practice (e.g., European Messe catalog administration) unverified — sample is US-market-heavy; variants kept generic.
- Payment machinery placement (native vs commerce module vs registration-based) varies across the sample; no fee/plan claims made.

## Final Synthesis

Exhibitor Management is the organizer-side system for managing the companies that exhibit at a show across the whole participation cycle. Its defining core is a three-part structure: the exhibitor as a managed company record (distinct from attendee person records, carrying its own people, listing content, space reference, and entitlements); the participation obligation loop (organizer-defined tasks, deadlines, documents, and content per exhibitor, worked define→complete→verify with deadline reminders); and exhibitor-side completion through a self-service surface bound to the exhibitor's own record (the Exhibitor Portal / Exhibitor Resource Center / Exhibitor Center of mature products; the paper manual+form loop is the same structure pre-digitally). Around that core, mature products assemble a standard capability set: intake with tiers/packages and often booth selection, listing editing that propagates immediately to audience surfaces, checklist/document machinery with reminders, branded organizer↔exhibitor communications, self-serve booth staff registration, orders/balances, lead-and-ROI visibility feeding retention, appointments, and virtual booths. The Type's boundaries are as important as its core: it does not own the sellable floor (Convention / Exhibition Management), the show-floor capture act (Event Lead Retrieval), the badge artifact (Event Credential / Badge Management), or the sponsor population (Sponsor Management) — it is the relationship and logistics layer that those systems assume, feed, and consume. The convention-exhibition-management pass's joint-review flag is discharged with keep-both-with-containment.
