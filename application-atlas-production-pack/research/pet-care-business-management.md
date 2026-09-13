# Research Notes — Pet Care Business Management

Research date: 2026-09-09
Slug: pet-care-business-management
Directory location: §29 Home, Family, Personal & Local Services (siblings: Veterinary Practice Management, Pet Grooming Management, Pet Boarding Management, Pet Daycare Management, Pet Training Management, Dog Walking Platform, Pet Sitting Platform, Appointment-based Service Business Management, Salon Management System)

## Research Goal

Understand what "Pet Care Business Management" software actually is as an Application Type: who operates it, what core objects exist inside it, how a pet-care company's whole operation (multiple service lines — daycare, boarding, grooming, training, retail) is administered in one system, and where its boundary sits against the single-line pet-care sibling Types, against the structurally rhyming Salon Management System / Appointment-based Service Business Management, and against consumer-side pet-service marketplaces.

Prior-pass context carried into this pass:
- pet-boarding-management (processed 2026-09-09) recorded: "pet-care-business-management is the umbrella-scope leaf over the same product population (boarding+daycare+grooming+training+retail suites)".
- dog-walking-platform (processed 2026-09-07) recorded: "Pet Care Business Management | operator-side software for pet-care companies (client records, staff scheduling, routing, invoicing); not two-sided stranger matching".
- applications/pet-boarding-management.md Related-Types table: "Pet Care Business Management | umbrella sibling | the same product population viewed at whole-business scope".

## Initial Boundary

Working hypothesis before research:

1. Core use: operator-side administration of a pet-care business (front desk, scheduling, staff, billing) — not consumer-facing matching.
2. Primary users: front-desk staff, groomers/trainers/attendants, owner/manager.
3. Nearest neighbors: the single-line pet-care siblings (boarding / daycare / grooming / training management), Salon Management System, Appointment-based Service Business Management, Veterinary Practice Management, Dog Walking / Pet Sitting Platforms.
4. Likely seam: the whole-business, multi-service-line scope vs one service line's core.
5. Unknowns: is multi-line scope definitional or merely common? Is retail/POS part of the core? Is staff management definitional? Does a distinct Type exist here at all, or is the leaf an alias/umbrella that should be flagged?

## Research Questions

1. What are the core objects? (client, pet, booking types, staff, invoice, packages, retail items…)
2. How do multiple service lines coexist in one system — one booking model or several?
3. How does the client/pet account accumulate across lines (history, packages, credits, vaccines)?
4. How does billing consolidate across lines and retail?
5. How do staff/specialists participate (assignment, scheduling, payroll)?
6. What happens during service delivery (care tasks, report cards) and is it part of the core?
7. What self-service surfaces exist (online booking, portal) and are they definitional?
8. What rules matter (capacity, vaccination currency, approval, pricing rules)?
9. Where are the boundaries against single-line siblings, salon management, vet practice management, and consumer marketplaces?
10. Historical check: would desktop-era multi-line kennel software satisfy the definition?

## Representative Products

Selection principles applied: market representation, documentation completeness, different product philosophies, different customer tiers, different geographies.

1. **Gingr** — cloud multi-line suite (boarding, daycare, grooming, training, dog park), US, SMB→enterprise/multi-location. Deep Zendesk knowledge base (Tier-1).
2. **ProPet Software** — cloud modular suite (boarding, daycare, grooming, training, retail), Canada (Ottawa), founder-owned, SMB. Product site + module/feature pages (Tier-2).
3. **Revelation Pets** — deliberately simple cloud pet-care software (kennel, daycare, cattery, grooming), small-business positioning, US (same parent as Gingr). Features/FAQ pages (Tier-2).
4. **DaySmart Pet (123Pet)** — grooming-led pet business software serving grooming/daycare/boarding/mobile, solo→high-volume salons, US. Solution pages (Tier-2).
5. **MoeGo** — mobile-first platform, grooming + boarding + daycare live (training/retail/pet-sitting "coming soon"), solo→franchise/enterprise. Help Center (Intercom, Tier-1 structure).

Rejected/considered: PetExec (docs JS-unreachable, carried limitation from boarding pass), PetLinx (unreachable, carried), Kennel Connection (legacy desktop pole — used in the boarding pass via migration pages; not re-fetched this pass), BusyPaws (not fetched; sample already saturated per stop conditions).

## Sources

Fetched 2026-09-09:

- Gingr root: https://www.gingrapp.com/
- Gingr Help Center home: https://support.gingrapp.com/hc/en-us
- Gingr section — Owners and Animals: https://support.gingrapp.com/hc/en-us/sections/25504866326541-Owners-and-Animals
- Gingr section — Reservations, Appointments, and Group Classes: https://support.gingrapp.com/hc/en-us/sections/25504731245453-Reservations-Appointments-and-Group-Classes
- Gingr article — Reservations, Appointments, and Group Classes (Feature Overview): https://support.gingrapp.com/hc/en-us/articles/31239370360461
- Gingr article — During the Stay and Departure (Topic Outline): https://support.gingrapp.com/hc/en-us/articles/29641449718669
- Gingr section — Retail, Purchases, and Order Management: https://support.gingrapp.com/hc/en-us/sections/25447459799821-Retail-Purchases-and-Order-Management
- Gingr section — Staff & Specialist Account Management: https://support.gingrapp.com/hc/en-us/sections/25504429716877-Staff-Specialist-Account-Management
- Gingr section — Facility Management: https://support.gingrapp.com/hc/en-us/sections/25504838903565-Facility-Management
- Gingr section — Prices and Pricing Rules: https://support.gingrapp.com/hc/en-us/sections/25504803812877-Prices-and-Pricing-Rules
- ProPet root (via propetware.com): https://propetsoftware.com/ → https://www.propetware.com/
- Revelation Pets root: https://www.revelationpets.com/
- Revelation Pets features: https://www.revelationpets.com/features
- Revelation Pets FAQ: https://www.revelationpets.com/faq
- DaySmart Pet root: https://www.daysmart.com/pet/
- DaySmart Pet operations: https://www.daysmart.com/pet/solution/operations/
- DaySmart Pet scheduling: https://www.daysmart.com/pet/solution/scheduling-software/
- MoeGo root: https://www.moego.pet/
- MoeGo Help Center home: https://www.moego.pet/help/en
- MoeGo collection — Boarding & Daycare: https://www.moego.pet/help/en/collections/12675402-boarding-daycare
- MoeGo collection — Client & Pet: https://www.moego.pet/help/en/collections/12568164-client-pet

Source-access limitations:
- www.propetsoftware.com failed twice (transport error); reached the same vendor at propetware.com. Evidence for ProPet is Tier-2 (product/module/feature pages), not help-center depth.
- PetExec and PetLinx remain unreachable (carried from the pet-boarding pass). The legacy desktop pole is evidenced indirectly (boarding pass: current vendors' official migration pages document imports from the ceased-trading Windows-desktop KennelSuite generation).
- Revelation Pets and DaySmart Pet evidence is Tier-2 (marketing/feature pages); no authenticated product walkthroughs. Precise numeric limits, defaults, and state names are therefore NOT stated anywhere in this research or the final document.
- Gingr and MoeGo provided Tier-1 help-center structure (section/collection and article titles), which is strong evidence for object structure and workflow shape but not for exact field-level behavior.

## Product A — Gingr

### Key observations (Evidence layer A unless noted)

- Positioning: "The pet business software for boarding kennels, doggy daycare, grooming salons, dog training" + dog park + enterprise. "Boarding, daycare, grooming, training, and dog park software in one system." "One system for the whole operation." "Gingr runs the whole business, not just the calendar."
- Front-desk dashboard ("Today"): checked-in / expected / going-home counts, capacity (e.g. "12 / 20"), a schedule mixing Daycare, Boarding, Grooming, and Training entries per time slot, online bookings landing in a visit detail, PreCheck status ("vaccines OK"), report cards, messages, payments, staff schedule.
- Three distinct booking types (Feature Overview, Tier-1):
  - **Reservations** — "Times when owners check in and check out their pet" (boarding/daycare stays).
  - **Appointments** — "Services that a customer can book for a specific time with a specific specialist" (grooming).
  - **Group Classes** — "Series of training classes with pre-set dates."
  - Plus **Check-In** (quick check-in, from "Expected Today", from animal profile, check in a pet without a reservation) and **During the Stay and Departure** (Report Cards, Check Out, Additional Services).
- Owners and Animals: Owner Accounts + Animals as separate record types with detail pages; Employee Notes attached; search for owners or animals.
- Facility Management: Hours of Operation (recurring, specific-date, pick-up/drop-off windows), Locations (add additional locations), **Areas and Lodging** (create areas, create lodgings), **Capacity Limits** (location capacity, lodging capacity, capacity by date), **Run Cards** (set up, auto-print at check-in, show employee notes), Forms (form types — waivers/agreements), Tax Settings (location/reservation-type/service tax), Data Management, Go Live (import checklist), Sell-your-Business (ownership transfer).
- Staff & Specialist: Staff User Accounts (create/activate, employee sign-up, import), **Specialist Scheduling** (specialists = groomers/trainers with schedules), User Access and Permissions (location restriction), **Employee Management Add-On** (add-on packaging).
- Retail: POS items, sell from POS tab / cart / dashboard / reservation details, inventory (update, SKU labels, purchase history), gift certificates, promotions/coupons, **Packages** (sell, credits, checkout with package credit), package subscriptions, memberships (portal signup, renewal), store credit, complete sales, manage orders.
- Pricing: Pricing Rules incl. **Peak Date Charges**; Price Verification via generated estimates for reservations and appointments.
- Payments: integrated processing (Gingr Payments / CardConnect merchant paths), deposits, tips.
- Client-facing: Pet Parent mobile app (book, pay, update pet records, message), PreCheck (vaccinations/waivers/belongings verified before drop-off), Report Cards ("photos and activity notes… before they reach the lobby"), Business Analytics (multi-location view).
- Claims: 5,000+ facilities, 150M reservations, 9M pet parents, 50M report cards (marketing numbers — recorded as vendor claims only).

## Product B — ProPet Software

### Key observations (Tier-2, layer A at product level)

- Positioning: "Software for Kennels, Dog Daycares, Groomers & Trainers" — "Boarding, Dog Daycare, Training, Grooming, and Retail — all in one place." Founded by kennel owners, 2014, Ottawa (Canada), founder-owned.
- **Modules** (explicit module decomposition): Pet and Client Manager; Boarding Kennel Module; Dog Daycare Module; Pet Grooming Software; Dog Training Software; Retail Module; Scheduled Services.
- Features: Online Booking (clients self-serve 24/7), Text Messaging (automated reminders), Report Cards, Integrated Credit Card Processing, **Smart Medications** ("The right meds. The right pet. Every single time."), Companion Mobile App, Availability Calendar, **Smart Pricing Engine**, Customization (custom forms), Email Marketing, Reports and Accounting (revenue, occupancy, payments dashboard), Pet Photography, Setup and Data Migration, **Kennel View**, **Vaccination Manager** (auto reminders, cloud storage), security (GDPR, geo-redundant, 2FA).
- Integrations: QuickBooks, Stripe, Mailchimp, Square, Zapier, Twilio; Open API announced.
- Onboarding: free demo account configured "for the services you offer: boarding, daycare, grooming, training, or any combination" — the multi-line combination is the vendor's own framing of the buyer.

## Product C — Revelation Pets

### Key observations (Tier-2, layer A at product level)

- Positioning: "Dog Daycare, Cattery, Grooming, and Kennel Software" — "Designed with small businesses in mind." FAQ: "Any pet service company that needs to save time, become more organized and take bookings online."
- Features: cloud-based (tablet/laptop/smartphone); **Customer Portal** (check availability, self-register, upload data and vaccine records, schedule recurring appointments, view pet during stay [webcam], pay outstanding invoices, purchase daycare credits); Online Booking (embed on website); **Packages** (credits applied to daycare bookings, purchase credit packages online, credit expiration); **Dashboard** (arrivals, departures, appointments, occupancy; print boarding cards; search bookings/payments; send photos/notes); **Boarding Calendar** (drag-and-drop, view pet records/notes); Pet Updates (email updates with photos during stay); **Reports** (arrivals/departures, occupancy, bookings, payments, sales by service, feedings, birthdays, vaccinations); Digital Agreements (e-signatures); **Vaccination Records** (store, track expiration, automatic reminders); Customize & Upsell (different rates for sharing pets, discounts, upsell products, waitlist with automated notifications); Reservation Reminders (confirmations, reminders, optional SMS); **Appointment Calendars** ("Use staff calendars and block availability, and manage grooming, training, and van drivers"); Integrations (email, SMS, scheduling, payment processing); Profiles (unlimited client and pet profiles, color-coding, notes, credits).
- Accounting export: QuickBooks or Xero.
- Same corporate parent and address as Gingr (Togetherwork, 2 Ravinia Drive, Atlanta) — two products, one population, different depth/positioning tiers.

## Product D — DaySmart Pet (123Pet)

### Key observations (Tier-2, layer A at product level)

- Positioning: "Pet Business Software for Groomers, Kennels, and More"; industries: Grooming, Daycare, Boarding, Mobile Pet Grooming; business tiers: solo groomers, growing grooming shops, high-volume salons. "Powered by 123Pet."
- Solutions: **Scheduling** (Digital Appointment Book — drag-and-drop, color-coded by day/week/employee; Automated Reminders with response tracking; 24/7 Online Booking where "visits are only confirmed after you approve them"; Digital Forms via text/email with drag-and-drop builder); **Communications** (text & email marketing, two-way texting, reputation management/review requests, website builder); **Payments** (chip/swipe/tap, Apple/Google Pay, no-show protection via deposits and stored cards, invoices, low-cost processing); **Operations** (Client & Pet Profiles — "customer info, pet details, and service history… preferences, vaccination records, and past appointments"; Real-Time Reporting — "over 50 customizable reports"; Mobile App with maps for mobile groomers; **Employee Management** — "team schedules, hours worked, commissions… payroll", time clocks).
- POS: integrated; commissions and tips tracked; payment links for prepay/remote billing; inventory tracking (supplies).
- Case-study client operates "Grooming & Daycare" — grooming-led businesses extending into daycare are the vendor's own observed population.

## Product E — MoeGo

### Key observations (layer A; help-center structure Tier-1, marketing claims Tier-2)

- Positioning: "The Intelligent Platform for Pet Businesses." By care type: Mobile grooming, Grooming salon, Boarding, Daycare (live); Retail, Training, Pet Sitting ("Coming Soon"). By business size: Enterprise, Franchise, Multi-locations. "From day one to hundreds of locations."
- Help Center collections: Grooming (39 articles); **Boarding & Daycare** (37); Getting Started; Communication (30); **Client & Pet** (47); Online Booking (29); Payments (44); **Staff Management** (22 — "staff schedule, payroll, staff profile"); Business Management (13 — "staff, payroll, availability rules"); Marketing (12); Insights (29 — "revenue, payroll, and performance reports"); Advanced Tools (25 — workflow automation, loyalty, integrations, enterprise).
- Boarding & Daycare collection structure (Tier-1): Settings (Service Menu, Evaluation, Client Communication); **Pricing Rules** (Overview, Discount Pricing, **Peak Dates Pricing**, **Late Pick-Up / Early Drop-Off Fee**, **Exceed 24-Hour Period**, Feeding and medication fee); Booking & Appointment (create boarding/daycare appointment, apply feeding & medication, print cards, online booking); **Lodging View** (Set Up Lodging, How Lodging Capacity Works, Checkout Cut-off Time, Lodging View, Split a Pet's Lodging Assignment); Home Page (Pet Status, Daycare Quick Check-in, Weekly Summary); **Task Management** (overview, set up and log feeding and medication tasks, Task Management Center, permissions and notifications); **Playgroup** (overview, set up, assign a pet's playgroup, playgroup view, FAQ).
- Client & Pet collection structure (Tier-1): Client Management (Client Profile, Client Data Setting, Client List); Pet Management (Pet Profile, Pet Data Setting, **Pet vaccine**); **Leads Management** (add/convert leads, dashboard, contact via email/SMS/calls, permissions); Fields Management (preset/custom fields); **Client Form** (Intake Form Submission and Processing, Setting Up Intake Forms, Digital Agreement); Pet parent Experience (**Pet Parent Portal**, Pet parent Cancel & Reschedule, **Report Cards**).
- Marketing claims: 10,000+ businesses, 11M+ pets; "Automatically generate and assign daily tasks so that every feeding, walk, and medication is completed on time with clear accountability"; Smart Scheduler, Abandoned Booking Recovery, Review Booster, Grooming Report.

## Cross-product Comparison

| Structure | Gingr | ProPet | Revelation Pets | DaySmart Pet | MoeGo |
|---|---|---|---|---|---|
| Client + pet records of record | Owner Accounts + Animals, detail pages, employee notes | Pet and Client Manager module | Unlimited client and pet profiles | Client & Pet Profiles (service history, vaccines) | Client Profile + Pet Profile + Pet vaccine |
| Multi-line booking in one system | Reservations + Appointments + Group Classes (3 named types) | Boarding/Daycare + Grooming + Training modules + Scheduled Services | Boarding calendar + appointment calendars (grooming, training, van drivers) | Appointment book across grooming/daycare/boarding industries | Grooming appointments + Boarding & Daycare appointments (training/retail coming) |
| Staff/specialists | Staff accounts, Specialist Scheduling, permissions, Employee Mgmt add-on | (staff via modules; Companion app) | Staff calendars, block availability | Employee Management: schedules, hours, commissions, payroll, time clocks | Staff Management: schedule, payroll, profile; task permissions |
| Cross-line billing | Cart/invoice aggregates reservations + appointments + retail; packages/credits/store credit | Integrated processing; reports & accounting | Invoices; QuickBooks/Xero export; daycare credits | Invoices; deposits; commissions/tips | Invoices, refunds, MoeGo Pay |
| Retail/POS | Full retail + inventory + gift certificates | Retail Module | Upsell products | POS + inventory tracking | "Coming Soon" |
| Care delivery records | Run Cards, Employee Notes, Additional Services, Report Cards | Smart Medications, Report Cards, Pet Photography | Feedings report, Pet Updates | — | Task Management (feeding/medication), Playgroup, Report Cards |
| Vaccination machinery | PreCheck ("vaccines OK") | Vaccination Manager | Vaccination Records + expiry reminders | Vaccination records in profiles | Pet vaccine collection |
| Self-service | Pet Parent app/portal, online booking | Online Booking, Companion app | Customer Portal, Online Booking | Online Booking (staff approval), Digital Forms | Online Booking, Pet Parent Portal, cancel/reschedule |
| Communications | Customer Communication section, Report Cards | SMS, Email Marketing | Reminders, Pet Updates | Two-way texting, marketing, review requests | Communication collection (30 articles) |
| Pricing machinery | Pricing Rules, Peak Date Charges, estimates | Smart Pricing Engine | Sharing rates, discounts, waitlist | Deposits/no-show protection, packages | Pricing Rules: peak dates, late fees, >24h, feeding/med fee |
| Capacity/lodging | Areas & Lodging, Capacity Limits (location/lodging/by date) | Kennel View | Occupancy reports, boarding calendar | — | Lodging View, Lodging Capacity, split assignment |
| Reports | Reports section, Business Analytics | Revenue/occupancy/payments dashboard | Arrivals/departures, occupancy, sales by service, feedings, vaccinations | 50+ reports | Insights: revenue, payroll, performance |
| Multi-location | Locations; Enterprise tier | — | — | — | Enterprise/Franchise/Multi-locations |
| Accounting export | (payments focus) | QuickBooks | QuickBooks, Xero | (payments focus) | (Insights exports) |

Reading of the comparison:

- All five products are **multi-line platforms**: the client account, the schedule, and the money span more than one service line in every sampled product. The line sets differ (Gingr adds dog park; Revelation adds cattery; MoeGo ships three lines with more "coming soon"; DaySmart is grooming-led with daycare/boarding industries) — the *shared multi-line system of record* is the constant, not any specific line set. (Layer B)
- The client account with pets is the universal anchor: pets are sub-records of clients, carrying care data (vaccines, medications, temperament/notes) and accumulating service history, credits, and packages across lines. (Layer B)
- Billing consolidates: charges from stays, appointments, classes, add-on services, and retail land on one client account and resolve into invoices/payments; prepaid forms (packages, credits, memberships, deposits) deduct at checkout. (Layer B)
- Staff management depth varies widely (full payroll/commissions at DaySmart/MoeGo; specialist scheduling + paid add-on at Gingr; staff calendars at Revelation) → common mature structure, not defining. (Layer B → L1)
- Retail is NOT universal (MoeGo "coming soon") → optional module. (Layer A, single-product absence proves non-definitional)
- Care-delivery records (feeding/medication tasks, report cards, playgroups) are common but shaped differently per line; a grooming-only operation has no feeding tasks → common mature structure, not defining. (Layer B → L1)
- Self-service surfaces (online booking, portal) are universal in the current cloud sample but absent from the historical desktop pole (carried evidence from the boarding pass) → common/variant, not defining. (Layer B + historical → L1/L2)

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **The client account with pets as the business's customer record of record.** An identified owner account holding one or more animal sub-records; pets carry care data (vaccination status, medications, temperament/notes, veterinarian) and the account accumulates service history, prepaid value (packages/credits), and communications across all service lines. Remove → a generic contact list / CRM with no animals and no care semantics.
2. **Multi-service-line booking on one shared schedule.** The business's services — typically daycare attendance, boarding stays, grooming appointments, training classes — are booked as dated commitments for specific pets against line-appropriate resources (capacity slots, lodging units, specialist time, class sessions), all visible in one scheduling surface. The definitional property is the *shared multi-line* schedule, not any specific line set. Remove the multi-line scope (keep one line) → the single-line sibling Types (Pet Boarding / Daycare / Grooming / Training Management).
3. **Cross-line billing resolving on the client account.** Charges from every service line plus retail accumulate on one account and resolve into invoices and payments; prepaid forms (packages, credits, deposits, memberships) are sold and deducted there. Remove → per-line invoicing or a booking tool with no money loop.

Jointly-held load-bearing:
- 1 alone = client/pet CRM
- 2 without 1 = anonymous booking calendar
- 3 without 1+2 = invoicing shell
- 1+2 without 3 = schedule board
- 1+3 without 2 = billing system with nothing to bill
- 2+3 without 1 = anonymous booking-and-payment
- Trade context lives inside the objects (pets, care data, service lines) — the §29 family pattern.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Staff management: staff user accounts, specialist schedules, roles/permissions; deeper payroll/commissions/time clocks at some products
- Service-delivery records: report cards, photos, care/task logs (feeding/medication), playgroup or group assignment, add-on services during a stay
- Vaccination tracking with expiry reminders; eligibility gating (block or alert — varies)
- Client self-service: online booking (often staff-approved), customer/pet-parent portal, digital intake forms and agreements
- Communications: automated reminders (SMS/email), confirmations, two-way texting, review requests, marketing
- Pricing machinery: pricing rules (peak dates, late pick-up/early drop-off fees, extended-stay thresholds), discounts, promotions
- Prepaid economy: packages, credit bundles with expiration, memberships, store credit, gift certificates, deposits/no-show protection
- Retail/POS with inventory (absent from one sampled product's live feature set)
- Reporting/analytics: occupancy, arrivals/departures, revenue, sales by service, staff performance
- Accounting integrations (QuickBooks/Xero), payment processing, SMS/email integrations
- Multi-location support (enterprise/franchise tier)

### L2 — Variant / Optional Structure

- Service-line mix: which lines the business runs (cattery, dog park/bar, mobile grooming, pet sitting, retail) — the line set is a business choice, not a Type property
- Deployment: cloud SaaS (current norm) vs installed desktop (legacy pole); mobile app vs web-first
- Customer tier: solo operator → single facility → multi-location/franchise/enterprise
- Webcam streaming of pets to owners during stays
- Lead management/CRM funnels, website builder, reputation management
- Loyalty programs, package subscriptions
- Regional vocabulary: cattery (UK/EU), kennel vs boarding, mobile-grooming routing

### L3 — Vendor-specific (Research Notes only)

- Gingr: PreCheck (night-before verification), Run Cards (auto-print at check-in), Employee Management Add-On packaging, dog-park line, "Sell your Business" ownership-transfer workflow
- ProPet: Smart Pricing Engine, Smart Medications, Kennel View, Companion Mobile App, Pet Photography module naming
- Revelation Pets: "Rev Pets Payments" branding, boarding-card printing, van-driver calendars
- DaySmart Pet: reputation management, website builder, no-show protection framing, 50+ reports claim
- MoeGo: Smart Scheduler™, Abandoned Booking Recovery, Review Booster, Task Management Center, Playgroup View, leads pipeline
- Corporate: Gingr and Revelation Pets share a parent (Togetherwork) — market-structure fact, not a Type property

## Rejected Findings (anti-overfit)

- **Online booking / customer portal NOT definitional** — universal in the current cloud sample but absent from the desktop-era pole (carried evidence: current vendors' official migration pages document imports from the ceased-trading Windows-desktop generation that held the same client/pet/booking/billing records with no online layer).
- **Retail/POS NOT definitional** — one sampled product ships retail as "coming soon" while being squarely in-type.
- **Staff payroll/commissions NOT definitional** — depth varies from full payroll to simple staff calendars; solo-operator tier exists.
- **Any specific service-line set NOT definitional** — line sets differ across all five products; the invariant is the shared multi-line system, not the lines themselves.
- **Vaccination blocking NOT definitional** — carried from the boarding pass (block-at-booking vs alert-and-verify both documented); here it is care data on the pet record plus reminders.
- **Capacity/lodging inventory NOT definitional at this Type's level** — it is definitional for the boarding sibling (its L0 leg 3); at whole-business scope it is line-specific machinery inside booking. A grooming-led deployment has no lodging at all.
- **Multi-location NOT definitional** — enterprise tier only.
- **Precise numbers/defaults NOT stated** — no numeric capacity limits, fee percentages, or state names are asserted anywhere (evidence does not support that precision).

## Historical / Market-Sample Check (§24)

- Would older, regional, platform-native products fit? The desktop-era multi-line kennel generation (carried evidence from the pet-boarding pass: KennelSuite/PetLinx/Kennel Connection class) held client/pet records, multi-line bookings, and billing with no cloud, portal, or online booking — all three L0 legs satisfied. Regional vocabulary (cattery) and non-US markets fit without US-specific forms. The definition names no deployment, no app, no AI, no payment rail.
- Conversely: a single-line tool (grooming-only appointment book with client/pet records and billing) fails L0 leg 2's multi-line scope → it belongs to the sibling Type (Pet Grooming Management). A consumer two-sided marketplace fails the operator-side record-keeping core → Dog Walking / Pet Sitting Platform. A human salon system fails the pet/care semantics → Salon Management System.

## Boundary Findings

1. **vs single-line siblings (Pet Boarding / Pet Daycare / Pet Grooming / Pet Training Management)** — same product population, different scope cut. The sibling documents the one line's core (e.g., boarding: client-owned pet + boarding stay + accommodation inventory + per-stay billing). This leaf documents the whole-business system: multi-line booking, cross-line accounts, cross-line billing, staff, retail, reporting. Test: remove the multi-line whole-business scope → sibling Type; add sibling lines to a single-line core → this Type. The seam is real but thin — recorded as a taxonomy observation (see Boundary Issues).
2. **vs Salon Management System / Appointment-based Service Business Management** — structurally rhyming skeletons (appointment book, staff, POS, client records). The distinction is the trade semantics: clients are animal owners, pets are served sub-records with care data (vaccines, medications, temperament), resources include lodging/capacity, and service delivery produces care records (report cards, feeding/medication logs). Remove the animals and care semantics → salon/appointment business management.
3. **vs Veterinary Practice Management** — both hold client+patient records and bill for services. Vet is clinical care (medical records, diagnoses, prescriptions, clinical staff); pet care business is non-clinical service (custody care, grooming, training) with business administration (occupancy, retail, packages) at the center. Some products carry a "veterinarian" field on the pet record — a contact field, not clinical functionality.
4. **vs Dog Walking Platform / Pet Sitting Platform** — consumer-side two-sided matching of strangers (walker/sitter profiles, owner discovery) vs operator-side administration of an identified business's own clients and staff. No marketplace mechanics in the sampled products.
5. **vs Pet Adoption Platform / Animal Shelter Management** — custody retained (animal returns home; paid service) vs custody transfer (intake, placement outcomes). Carried ratification from the boarding pass.
6. **vs Retail POS** — retail is a module inside this Type (and absent from one sampled product), not the core; the core transaction is a booked service, not a product sale.

## Uncertainties

- Exact check-in/check-out state machines vary and were not verified at field level (help-center article bodies beyond outlines not fetched); no state names asserted.
- Whether online booking requests require staff approval at every product — documented at DaySmart only; treated as a common pattern, not a rule.
- The degree to which packages/credits cross service lines within one product (e.g., a grooming package credit used for boarding) was not verified per product; cross-line *account-level* accumulation is documented, cross-line *credit redemption* is not asserted.
- ProPet's staff-management depth (payroll?) unverified — its feature pages do not enumerate it; excluded from cross-product staff claims.
- PetExec / PetLinx / Kennel Connection not re-fetched; the legacy-desktop pole rests on carried evidence from the pet-boarding pass.
- Market-size and count claims (5,000+ facilities, 10,000+ businesses, 50+ reports) are vendor marketing numbers, recorded as claims only.

## Final Synthesis

Pet Care Business Management is the operator-side, whole-business system of record for a pet-care company. Its defining core is three jointly-held structures: (1) the client account with pets — the customer record of record whose animal sub-records carry care data and whose account accumulates service history and prepaid value across all service lines; (2) multi-service-line booking on one shared schedule — daycare, boarding, grooming, training (and optionally more) booked as dated commitments for specific pets against line-appropriate resources; (3) cross-line billing — charges from every line plus retail resolving into invoices and payments on the client account, with packages/credits/deposits deducting at checkout. Around that core, mature products add staff management, service-delivery records (report cards, care tasks), vaccination machinery, client self-service, communications, pricing rules, retail, reporting, and multi-location support — none of them definitional. The Type's reason to exist as a separate leaf is the whole-business scope: the same product population as the single-line siblings, viewed at the level where one login runs the entire business. Remove the multi-line scope and the leaf dissolves into its siblings; remove the pet-care trade semantics and it dissolves into salon/appointment-business management; remove the operator side and it dissolves into consumer marketplaces.
