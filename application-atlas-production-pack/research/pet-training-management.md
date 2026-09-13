# Research Notes — Pet Training Management

Research date: 2026-09-09
Slug: pet-training-management
Directory leaf: Pet Training Management (§29 Home, Family, Personal & Local Services; siblings include Veterinary Practice Management, Pet Grooming Management, Pet Boarding Management, Pet Daycare Management, Pet Care Business Management, Dog Walking Platform, Pet Sitting Platform, Salon Management System, Appointment-based Service Business Management)

## Research Goal

Understand what "Pet Training Management" software actually is as an Application Type: who operates it, what core objects exist inside it, how the training business cycle (publish offerings → enroll dogs → run sessions → get paid) works, what training-specific structure exists (class series vs private lessons, rosters, attendance, packages, graduation), and where its boundary sits against the umbrella sibling (Pet Care Business Management), the other single-line siblings (Grooming / Boarding / Daycare Management), the human class-business analogs (Dance Studio Management, Fitness Studio Management), learning-management Types, and generic appointment scheduling.

Prior-pass context carried into this pass (flags to discharge):

- pet-care-business-management (processed 2026-09-09) recorded the hypothesis: "Pet Training Management | single-line sibling | class-series enrollment as the core; here training is one line among several" — this pass must verify or refute that from the training side.
- pet-grooming-management (processed 2026-09-09) flagged: "expected same family shape (single-line trade leaf; training is class-series/enrollment machinery distinct from hours-billed grooming appointments) — discharge the cluster observation and ratify the seam at that pass."
- pet-daycare-management (processed 2026-09-09): "pet-grooming-management and pet-training-management remain unprocessed siblings and should discharge the cluster observation at their passes" (one product population, multiple scope cuts).
- pet-boarding-management (processed 2026-09-09) listed "board&train" as a boarding variant — the overlap must be addressed from the training side.

## Initial Boundary

Working hypothesis before research:

1. Core use: operator-side administration of a dog-training business (training facilities, trainer-owned businesses, training desks of pet-care facilities) — class schedule + client/dog records + enrollment + billing.
2. Primary users: trainers/instructors, front-desk staff, owner-operator; dog owners as self-service clients.
3. Nearest neighbors: Pet Care Business Management (umbrella), Pet Grooming / Boarding / Daycare Management (same trade family, different unit of work), Dance Studio Management / Fitness Studio Management (same class-series skeleton, human subjects), Corporate LMS / Customer Training (learning-content Types), generic appointment scheduling.
4. Likely seam with the umbrella: the scope cut — training line alone vs whole business.
5. Likely seam with grooming: the unit of work — a multi-session class series with a roster vs a single hours-billed appointment.
6. Unknowns: is the class series definitional, or do private-lesson-only businesses satisfy the Type? Is class capacity (roster limits) definitional? Is package/series payment definitional or a variant? Does vaccination gating carry from the rest of the pet family? Are there dedicated training-only products, or does the Type only exist as a module inside multi-line platforms?

## Research Questions

1. What is the unit of work — how is a group class represented (series vs single session), and how is a private lesson represented?
2. What is the relationship between the class catalog (definition) and scheduled occurrences?
3. What is the enrollment model — what record does enrolling create, and what does it bind (dog ↔ class ↔ sessions)?
4. What is the capacity model — roster limits, waitlists, full/canceled states?
5. What lives on the dog record vs the client record — what training-relevant data does the system hold?
6. How does enrollment resolve into money — series packages, per-session payment, deposits, balances?
7. What happens across the series — attendance, notes, report cards, graduation?
8. What client-facing surfaces exist — online registration, portals, enrollment requests?
9. What rules and exceptions matter — full classes, canceled sessions, un-enrollment, vaccination currency, waivers?
10. What variants exist — private-lesson-only, board-and-train, therapy classes, virtual classes, events/seminars, deployment generations?
11. Where are the boundaries against the neighboring Types (umbrella, grooming/boarding/daycare siblings, human class businesses, LMS, generic scheduling)?

## Representative Products

Selection principles applied: market representation, documentation completeness, different product philosophies (dedicated dog-business software vs multi-line pet-care platforms), different customer tiers (solo trainer → training facility → multi-line facility), and the single-line pole (a vendor that sells training as a standalone subscription).

| Product | Positioning | Tier of evidence |
|---|---|---|
| DogBizPro | Dedicated dog-business software ("Software for your dog training business"); Training Module is the founding line beside optional Daycare/Boarding/Therapy modules | A — official support-portal articles fetched at article level + official features page |
| Gingr | US multi-line pet-care SaaS; training sold as the "Group Classes" booking machinery beside reservations and appointments | A — official help-center articles fetched at article level |
| ProPet Software | Multi-line pet-care platform (boarding, daycare, grooming, training, retail) with a named "Dog Training Software" module; explicitly sells a training-only subscription | B — official module page + root page (knowledge base exists, not fetched at article level) |
| PetExec | Multi-line pet-care platform with a dedicated "PetExec for Trainers" page; now part of the Gingr corporate family (observed on-site banner) | B — official product page + official documentation-center structure (Training subject area listed; article PDF not machine-readable) |

Negative / adjacent observations (evidence that the training line has its own product population and its own machinery):

- **Time To Pet** — major pet-care platform whose published solution list covers pet sitting, dog walking, cat sitting, pooper scooper, boarding, daycare, grooming, mobile grooming — and **no training solution** (observed on the official solutions navigation, 2026-09-09). Training is not automatically bundled into every pet-care platform.
- **MoeGo** — grooming-first platform; training listed as "coming soon" (carried from research/pet-care-business-management.md). Same negative direction.
- **Trainer's Best Friend** — transport error on the single attempt; abandoned per the network-restriction rule. Not sampled.

Rejected/abandoned samples:

- Trainer's Best Friend (transport error ×1) — abandoned.
- PetExec documentation PDF ("Adding Group Training Products & Services") — fetched but binary PDF content not machine-readable; the documentation-center listing (Training subject area, article title) is used as structure-level evidence only.

## Sources

Fetched 2026-09-09 (all official vendor surfaces):

- DogBizPro root: https://dogbizpro.com/ (canonical domain; site served from dogbusinessprogram.com)
- DogBizPro features page: https://dogbusinessprogram.com/software/features/
- DogBizPro support portal — Classes category: https://support.dogbizpro.com/category/7-category
- DogBizPro article — Creating Classes & Categories: https://support.dogbizpro.com/article/23-creating-classes-categories
- DogBizPro article — Scheduling Classes: https://support.dogbizpro.com/article/69-scheduling-classes
- Gingr help center home: https://support.gingrapp.com/hc/en-us
- Gingr section — Reservations, Appointments, and Group Classes: https://support.gingrapp.com/hc/en-us/sections/25504731245453
- Gingr section — Group Classes: https://support.gingrapp.com/hc/en-us/sections/25513832034829-Group-Classes
- Gingr article — Group Classes (Topic Outline): https://support.gingrapp.com/hc/en-us/articles/29141960806669
- Gingr article — Set Up a Group Class (Process): https://support.gingrapp.com/hc/en-us/articles/29142173448589
- Gingr article — Enroll a Pet in a Group Class (How-To): https://support.gingrapp.com/hc/en-us/articles/29307536838413
- ProPet root: https://www.propetware.com/
- ProPet Dog Training module page: https://www.propetware.com/dog-training-software/
- PetExec root: https://petexec.net/
- PetExec for Trainers: https://petexec.net/service/trainers
- PetExec documentation center: https://docs.petexec.net/ (subject-area listing incl. Training → "Adding Group Training Products & Services")
- Time To Pet root (solutions navigation): https://www.timetopet.com/
- Carried: research/pet-care-business-management.md (Gingr appointments/specialists, MoeGo training "coming soon", vaccination machinery), research/pet-grooming-management.md (boundary flag), research/pet-daycare-management.md (cluster observation), research/pet-boarding-management.md (board&train variant)

Source-access limitations:

- Trainer's Best Friend unreachable (transport error ×1); the independent training-only vendor pole beyond DogBizPro is not directly sampled.
- PetExec's training documentation exists as PDFs that do not render as text; PetExec training evidence is product-page + documentation-structure depth, not article-body depth.
- ProPet evidence is module-page depth; its knowledge base was not fetched at article level.
- DogBizPro's "Working with Classes", "Class Types", and Private Training article bodies were not fetched (category listing only); roster/attendance mechanics rest on the features page plus the two fetched articles.
- The sample is US-centric (all four primary products are US vendors); regional fit of the definition is argued structurally (no region-specific machinery named in the core), not from sampled regional products.
- No dedicated web-only class-booking platform (human-class SaaS used by dog trainers) was sampled; the generic-scheduler pole is argued structurally.

---

## Product A — DogBizPro

### Key observations (evidence layer A — official support articles + features page)

**Positioning**: "Software for your dog training business." "Our software is designed to help you manage your dog training, dog daycare or dog boarding business…" Multi-module package: Training, Therapy, Daycare & Boarding. "All modules include the ability to manage your Client & Dog Information, Client & Dog History, Client Waivers, Client Transactions, Client Balances, Client Packages, Print & Email Client Invoices, Vaccine Records & more."

**Training Module (features page)**: "Class Scheduling, Event Scheduling, Private Training Sessions, Custom Event types such as Speakers & Seminars, Document Management, Class Attendance, Printing Rosters, Printing Class & Event Lists, Sending Class or Event Emails, Viewing Location & Instructor Availability & More."

**Class catalog vs scheduling (Tier-1, "Creating Classes & Categories")**:
- Categories organize classes for online registration; "Categories also allow you to assign discounts and package credits to a group of classes vs. having to add each class individually." Parent field creates a category hierarchy.
- "This section is where you will enter all of the classes you offer to your clients. **You will not actually schedule any of the classes in this section.**" — the class definition (catalog) is a separate object from its scheduled occurrences.
- Class definition fields: **Title**; **Link** (direct registration-page link, populated on save); **Description** ("visible to your clients"); **Sessions** ("the number of sessions the class lasts. In many cases this is the number of weeks for this class"); **Cost** ("the typical cost for this class. If your class costs vary by location or other details you can specify a different cost when scheduling an occurrence"); **Deposit** ("if you want to require a deposit for this class that is different from the full amount"); **Max Dogs** ("the maximum number of dogs you will allow in this class"); **Session Length** (hours per session); **Client Form** / **Dog Form** (custom registration forms per class); **Auto-Responders** per class (Registration sent on online registration completion; Confirmation sent when registration is confirmed "either by payment or manually depending on your system settings"; Waiting List sent when staff manually move a registration into waiting-list status); **Categories**.

**Scheduling occurrences (Tier-1, "Scheduling Classes")**:
- Reached from the Calendar, the Classes tab, or from inside a dog page ("Sign-up Dog for Class").
- Two class event types: **Class** — "standard classes, meaning classes that have a specific start and end date with a recurring structure that can be easily defined"; **Modularized Class** — "classes that are of an on-going nature, where clients can start on any week, complete the specified number of sessions and then graduate."
- **Public** flag: schedule a class visible or not visible online.
- Cost defaults from the class definition but is editable per scheduled occurrence.
- **Canceled/Full**: manual flags on a scheduled class.
- **Repeat**: Start Date + Duration (session length); **Repeat Indefinitely / Repeat Until / Repeat X Times** — "Repeat X Times … is the preferred selection for standard classes and is defaulted to the number of sessions specified for the class"; Repeat Indefinitely "is the recommended setting for Modularized Classes as they are on-going in nature." Note: "there is only one attendance roster associated with a standard class, so once a client registers they will be on the class list indefinitely."
- **Location**, **Instructor**, **Co-Instructor** fields on the scheduled class.

**Other structures (features page)**:
- **Clients & Dogs**: client information + custom fields; "Keep detailed Dog Records"; "Track dog vaccine dates"; "Add multiple dogs per client"; "Access client and dog history"; invoices (print & email, payable online); notes per client or dog; client waivers.
- **Packages**: "Sell packages of classes to your clients"; "Create packages for private training, daycare, therapy & boarding"; "Easily track the client's remaining and used credits."
- **Private Training**: "Schedule private training appointments"; "Setup multiple sign-up options"; payment tracked in the client's register; "See past private training in the client's history"; "Allow your clients to register online during your openings."
- **Events**: "Schedule seminars & workshops with multiple registration levels"; play groups and parties; online registration.
- **Online Registration**: clients register for "classes, events, private training, therapy & packages online"; pay online (CardConnect / Authorize.NET / PayPal); Client Registration Portal for self-service contact updates; website widgets/embeds.
- **Daycare / Boarding modules**: separate machinery (repeating daycare appointments, check in/out, boarding locations).
- Support-portal category structure: Classes, Events, Daycare, Boarding, Clients & Dogs, Client Portal, Documents, FAQs, Invoices & Transactions, Online Registration, Packages, Payments, **Private Training**, Reporting, **Therapy**, Widgets & Integration.

## Product B — Gingr

### Key observations (evidence layer A — official help-center articles)

**Group Class definition (Tier-1, "Group Classes (Topic Outline)")**: "A **Group Class is a series of training classes with pre-set dates**. When you enroll a customer, they can optionally pay for the entire series of classes upfront using a package." "Group classes in Gingr are designed to **create a reservation per class**. Pets should be checked in and out of each group class completed." Portal enrollment requires adding the group-class request link to the portal configuration.

**Set Up a Group Class (Process)** — ordered configuration steps: 1. Create a Group Class Reservation Type; 2. Set Rates for Group Classes; 3. Create a Package for Group Classes; 4. Create a Group Class; 5. Create a Group Class Schedule. "To track class usage and class payment we will utilize the package feature… Customers can purchase the package through the customer portal at the time of enrollment to pay for the program." Open-enrollment note: "When creating a package for an open enrollment group class, only assign a quantity of 1 credit. Customers will be prompted to purchase a package for each group class date they are enrolled in." A "Set Up Virtual Group Classes" process exists.

**Enrollment (Tier-1, "Enroll a Pet in a Group Class (How-To)")**:
- Flow: Reservations » Group Classes → select **Future** or **Current** classes → "Type to **Select Pet(s):** you can select one or more pets from the same owner" → **Enroll Now** → confirm details → **Enroll in Class!** → navigated to the **Cart** to complete payment.
- "If the class you are enrolling is an **open enrollment class**, you will select the dates the pet will attend on this screen by clicking them on the calendar."
- "If your group class is not associated to a package, you will not be navigated to the cart… Instead, **customers will pay after each session**."
- Completing checkout with payment "adds the package for the group class to the customer's profile and **creates reservations for each session of the Group Class on the animal's profile**. It will also add the animal to the list of enrollee's on the group classes page."
- **Check Out With No Payment**: "add the class balance to the customer's account if, for example, you are enrolling them over the phone and the customer plans to pay in person later."
- Portal side: "Show on Customer Side" setting; "Should Customer Purchase Package in Portal?" setting gates whether enrollment requests require a package purchase; enrollment requests flow to the business side with notifications.
- Related machinery: Un-Enroll a Pet from a Group Class; Enrollment Requests from the Customer Portal; Enable Enrollment Request Notifications; Enroll in Group Classes from Customer Portal.
- Section context: the same help-center section also carries Reservations, Appointments, Check-In, During the Stay and Departure, and an **Evaluation Workflow** (Configure Evaluation Types / Managing Evaluation Results) — evaluation machinery shared across the product's service lines.

## Product C — ProPet Software

### Key observations (evidence layer B — official module page + root page)

**Positioning**: "Software for Kennels, Dog Daycares, Groomers & Trainers"; "Boarding, Dog Daycare, Training, Grooming, and Retail — all in one place." Founder-owned since 2014 (Ottawa, Canada).

**Training module page (Tier-2)**: "Manage **private dog training sessions and group classes** in ProPet Software." "Manage your dog training business from its own dashboard… Easily integrate your training with your boarding, daycare, or grooming. **Only offer training? Then you can subscribe to only the training module.**" — direct vendor evidence for the single-line deployment pole.

**Training features (module page)**:
- Customizable pricing: "Customizable pricing options, pricing rules and add-ons"; "Set pricing triggers"; "Clone and archive rates and group classes."
- Organization: "Separate dashboard to manage private training and group classes"; "Create trainer roles and user accounts"; "Set trainer availability and schedule"; "Schedule private appointments and classes"; "Online payments, automated emails, reminders and notifications"; "Upload and store vaccination records and signed contracts"; "Accept and manage training requests"; "Appointment calendar and quick-check availability view."
- **Group Classes**: "Manage ongoing and drop-in classes"; "Ability to clone re-occurring group classes"; "Manage class rosters and attendance"; "Set maximum and minimum registration limits for classes"; "Create Report Cards for group classes."
- Forms & Agreements: "Training agreements, forms, booking sheets"; "Forms to collect information for emergency contacts, veterinarians."
- Automation: "Automated email to trainers when services have been assigned to them"; reminder/confirmation/thank-you emails; "Send emails to group classes."

**Platform context (root page)**: Pet and Client Manager module; Vaccination Manager feature ("Auto reminders, secure cloud storage"); online booking; report cards; integrated payments; QuickBooks/Stripe/Mailchimp/Square/Zapier integrations; report cards as a platform feature.

## Product D — PetExec

### Key observations (evidence layer B — official product page + documentation structure)

**Positioning**: "Operations Software for Dog Trainers." "PetExec's robust training management tools help you run your training programs with ease." "For facilities with private training, to larger facilities who specialize in private and group training…" "…it's clear why PetExec is the #1 choice for dog daycares and training facilities alike."

**Training features (Tier-2)**:
- "Keep track and create rosters and other information on classes and students with PetExec."
- "Either add the class cost to the cart or take payment right from the Dashboard."
- "Monthly, weekly, or daily calendar view of all training classes"; color-coding per class.
- "Offer your owners the ability to request group training classes through the PetExec Owner Portal or PetExec Mobile app" — and private training classes (features list: "Allow owners to request group training classes… along with private training classes").
- "**Create Board and Train packages.**"
- Training rosters: "Create and organize your training rosters in PetExec."

**Documentation structure (Tier-1 at listing level)**: the official documentation center's "PDF by Subject Area" includes a **Training** subject area containing "Adding Group Training Products & Services" — group training is a configured product/service class in the system, parallel to Daycare/Boarding/Grooming/Scheduled Services product documentation. (The PDF body itself is not machine-readable; no field-level claims made.)

**Corporate note (observed on-site)**: "PetExec is now part of the Gingr family!" with a link to a Togetherwork-acquisition announcement; PetExec's contact/trial links route through gingrapp.com. Market consolidation fact, recorded as observed.

**Platform context**: owner portal/mobile app; vaccinations overview documentation; report cards; paperless contracts; recurring billing; occupancy functionality (limit pets scheduled/signed in per day); QuickBooks export.

## Negative / adjacent observations

- **Time To Pet** (official solutions navigation, 2026-09-09): solutions cover pet sitting, dog walking, cat sitting, pooper scooper, boarding, daycare, grooming, mobile grooming — **no training**. A leading pet-care platform does not serve the training line at all.
- **MoeGo** (carried from the pet-care pass): grooming/boarding/daycare live; training "coming soon." Same direction.
- Together: the training line is served by a distinct product population (dedicated dog-training software and multi-line platforms that chose to build it), not automatically by every pet-care platform.

## Cross-product Comparison

| Structure | DogBizPro (A) | Gingr (A) | ProPet (B) | PetExec (B) |
|---|---|---|---|---|
| Client account with dogs | Clients & Dogs: client info, detailed dog records, multiple dogs per client, history, waivers, notes | Owners & Animals (carried); enrollment selects "one or more pets from the same owner" | Pet and Client Manager; vaccination records; contracts | Owner accounts; pet records; vaccinations overview |
| Class series as scheduled offering | Class definition (Sessions, Session Length) + scheduled recurring occurrence (Repeat X Times defaulted to session count); Modularized Class (ongoing, start any week, graduate) | "A Group Class is a series of training classes with pre-set dates"; reservation per session; open-enrollment variant (pick dates) | "Manage ongoing and drop-in classes"; clone recurring group classes | Group training products; training-class calendar (monthly/weekly/daily) |
| Private lessons | Private Training module: appointments, multiple sign-up options, online registration during openings | Appointments booking type (carried) | "Schedule private appointments and classes"; separate dashboard for private vs group | Private training requests via portal; "facilities with private training" |
| Enrollment/roster | Registration creates roster entry; one attendance roster per standard class | Enroll pet(s) → enrollee list + reservations per session; un-enroll; portal enrollment requests | "Manage class rosters and attendance" | "Create and organize your training rosters" |
| Capacity on offerings | Max Dogs per class; Canceled/Full flags; Waiting List status | (not directly observed in fetched articles) | "Set maximum and minimum registration limits for classes" | (facility occupancy machinery observed; class-level limits not directly observed) |
| Instructor/trainer as resource | Instructor + Co-Instructor on scheduled class; location | Specialists (carried) | Trainer roles/user accounts; trainer availability; assignment emails | Trainers (facilities "who specialize in private and group training") |
| Tuition/money | Packages of classes with remaining/used credits; per-class Cost + Deposit; online payment | Package pays series upfront; per-session payment variant documented; balance-to-account path; cart checkout | Pricing rules, add-ons, online payments | Cart or dashboard payment; Board and Train packages |
| Attendance & progress | "Track class notes & attendance"; print rosters | Check in/out per session (reservation per class) | Rosters and attendance; Report Cards for group classes | Rosters; report cards (platform feature) |
| Vaccination data | "Track dog vaccine dates" | Pet vaccine (carried) | Upload/store vaccination records; Vaccination Manager | Vaccinations overview |
| Online registration/portal | Online registration for classes/events/private training/therapy/packages; website widgets; client portal | Portal enrollment requests; package-purchase gating setting | Online booking; accept/manage training requests | Owner portal/mobile app requests (group + private) |
| Events/seminars | Events: seminars & workshops, multiple registration levels, play groups | — | — | — |
| Therapy classes | Dedicated Therapy module | — | — | — |
| Virtual classes | — | "Set Up Virtual Group Classes" process | — | — |
| Board-and-train | (boarding module separate) | — | — | "Create Board and Train packages" |

Convergent observations across the sample (evidence layer B unless noted):

1. Every product holds **client accounts with dog sub-records** carrying care/eligibility data (vaccination dates, behavior notes) — the animal is the enrolled subject.
2. Every product holds **scheduled training offerings** in two shapes: group class series (multi-session, pre-set or recurring dates) and private lessons (appointments).
3. Every product holds **enrollment as a persisted per-dog binding** forming a roster (class) or a booking (lesson), with the enrollee list visible on the offering.
4. Every product resolves **enrollment into money on the client account** — series packages, per-session payment, deposits, balances.
5. Class capacity (roster limits) is documented at DogBizPro (Max Dogs, A) and ProPet (max/min limits, B); Gingr/PetExec class-level limits not directly observed — held as common, not invariant.
6. Attendance/progress records (attendance, notes, report cards) are common; graduation semantics documented at DogBizPro (Modularized Class, A) and ProPet (report cards, B).
7. Vaccination data is universal in-sample; enforcement style not directly observed at article level for training — held as standard capability, not invariant (consistent with the family's boarding/daycare/grooming rulings).
8. Online registration/portal is universal in-sample but not definitional (paper-era training clubs satisfy the core without it).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Four jointly-held structures. The Type is recognizable only when all four are present:

1. **The client account with dogs.** An identified owner account holding animal sub-records; the dog — not a person-learner — is the enrolled subject, carrying training-relevant data (vaccination status, behavior/temperament notes, history). Remove → human class management or a generic booking tool.
2. **The scheduled training offering.** The business's training services exist as scheduled structures in two canonical shapes: the **class series** (a named multi-session program — pre-set dates or a recurring structure — with one roster) and the **private lesson** (a dated one-to-one appointment). The offering definition (catalog) is distinct from its scheduled occurrences. Remove → client/dog CRM.
3. **The enrollment binding.** A persisted per-dog binding to a specific offering — the class roster entry (spanning the series) or the lesson booking — held against bounded capacity (class spots; trainer time for lessons). Remove → schedule board with no participants.
4. **The tuition loop.** Enrollment resolves into money on the client account: series/package payment, per-session payment, deposits, balances carried to resolution. Remove → free roster.

Jointly-held load-bearing:

```text
1 alone                          → client/dog CRM
2 without 1+3                    → class brochure/schedule nobody attends
3 without 1+2                    → anonymous sign-up sheet
4 without 1–3                    → invoicing shell
1+2 without 3                    → catalog with no rosters
1+3 without 2                    → waitlist with no offerings
2+3 without 1                    → anonymous class booking (generic class platform)
1+2+3 without 4                  → free community class roster
```

### L1 — Common Mature Structure

- Trainer/instructor as the assigned resource (instructor/co-instructor fields; trainer roles, availability, assignment notifications) — the specialist-time model; a solo operator self-delivering satisfies the core without named assignment.
- Class capacity machinery (max/min registration limits, full/canceled flags, waitlists).
- Attendance tracking and per-session check-in/out; class notes.
- Progress records: report cards, graduation (modularized/open-enrollment classes).
- Vaccination records on the dog with expiry tracking/reminders; eligibility gating (style varies).
- Client self-service: online registration/booking, customer portal, enrollment requests, website embeds.
- Forms and agreements (training agreements, liability waivers, emergency-contact/vet forms).
- Communications: confirmations, reminders, class emails.
- Pricing machinery: pricing rules, add-ons, discounts, deposits.
- Staff management; reporting; payment processing; accounting exports.

### L2 — Variant / Optional Structure

- Offering-mix posture: classes-led vs private-lesson-led vs both (all sampled products carry both; emphasis varies).
- Session structure: fixed series (pre-set dates, enroll once) vs open/modularized enrollment (start any week, complete N sessions, graduate) vs drop-in classes.
- Payment form: series package paid upfront vs per-session payment vs deposits vs cart/dashboard payment.
- Board-and-train (training delivered during a boarding stay — overlaps Pet Boarding Management machinery; packages documented at one sampled product).
- Events/seminars/workshops with registration levels (single-occasion offerings riding adjacent machinery).
- Therapy-dog class programs (dedicated module at one sampled product).
- Virtual/online classes (one sampled product documents a setup process).
- Deployment: cloud SaaS current; the sampled dedicated product's support corpus shows a long-lived web-app generation (article update dates 2019–2020); paper-era clubs are the conceptual pre-history.
- Species scope: dog-dominant in-sample; the structures are not dog-specific (class/roster/tuition machinery is species-agnostic).

### L3 — Vendor-specific (research notes only)

- DogBizPro: category-level discount/package-credit assignment; per-class auto-responders (Registration/Confirmation/Waiting List); "Sign-up Dog for Class" from the dog page; CardConnect/Authorize.NET/PayPal integrations; Therapy module; website widgets.
- Gingr: reservation-per-session implementation of the series; "Should Customer Purchase Package in Portal?" setting; open-enrollment 1-credit package pattern; Evaluation Workflow shared with daycare; virtual-class setup process.
- ProPet: training-only subscription; clone/archive rates and classes; pricing triggers; trainer assignment emails.
- PetExec: Board and Train packages; color-coded class calendar; Togetherwork/Gingr family ownership (market consolidation).

## Vendor-specific Findings

See L3 above. None of these enter the canonical core.

## Boundary Findings

1. **vs Pet Care Business Management (umbrella)** — DISCHARGED from this side. Same product population, different scope cut. Gingr, ProPet, and PetExec all realize the training line exactly as this Type's core (client/dog records + class series + private lessons + enrollment + tuition), and ProPet sells the training line **as a standalone subscription** ("Only offer training? Then you can subscribe to only the training module") — direct vendor evidence that the single-line core stands alone. Test: remove the multi-line whole-business scope → this Type; add sibling lines (boarding/daycare/grooming/retail) on one shared schedule/account/billing → the umbrella. The umbrella pass's hypothesis ("class-series enrollment as the core") is **confirmed with one refinement**: the core is the scheduled training offering in two shapes (class series + private lesson) with enrollment and tuition; the class series is the distinctive structure, private lessons are equally first-class.
2. **vs Pet Grooming Management** — seam ratified as expected by the grooming pass: the unit of work differs. Grooming's appointment is a single hours-bounded service consuming groomer time, priced from a breed/coat/size menu. Training's unit is the **enrollment**: a multi-session series with one roster and series-level payment (or a lesson appointment with lesson packages). Training has no drop-off→groom→pick-up service loop and no menu pricing by animal attributes; grooming has no roster/attendance/graduation machinery.
3. **vs Pet Boarding Management** — board-and-train is the overlap: a training business may board dogs while training them. The boarding pass listed board&train as a boarding variant; this pass observes board-and-train packages at one training-side product. The seam holds because the cores differ: boarding's unit of work is the stay consuming accommodation inventory; training's is the enrollment consuming class spots/trainer time. A board-and-train program uses boarding machinery for the stay and training machinery for the program; neither core subsumes the other.
4. **vs Pet Daycare Management** — daycare's unit is the same-day attendance consuming daily capacity; training's is the enrollment in a scheduled program. Daycare has no roster/series/tuition semantics; training has no drop-off care-day loop. (Gingr's evaluation machinery is shared platform infrastructure, not a Type-level structure.)
5. **vs Dance Studio Management / Fitness Studio Management (human class businesses)** — the class-series skeleton rhymes (offering catalog → scheduled series → enrollment/roster → tuition), but the served subject differs structurally: here the "student" is an animal (dog records, vaccination eligibility, behavior data, owner as payer), and the offering mix includes private lessons and board-and-train. Human class Types carry guardian/family accounts, levels, recitals/costumes (dance) or membership/entitlement economies (fitness) that have no counterpart here. Both sides stand as separate Types.
6. **vs Corporate LMS / Customer Training / education LMS** — those Types manage learning content and learner records (courseware, completion, certificates) for people in employment/commercial/academic relationships. Here the system of record is the service business: the class is a **scheduled service consuming capacity and producing revenue**, not a content container; there is no courseware layer, no learner profile of record, no completion/certification machinery in the sampled products (report cards are service-delivery records, not transcripts).
7. **vs Appointment-based Service Business Management / generic appointment scheduling** — the generic skeleton (appointments + clients + billing) lacks all three training-specific structures: the animal as enrolled subject, the multi-session class series with roster, and the series/tuition payment semantics. A solo trainer on a generic scheduler sits at the Type's edge; the dedicated products exist precisely because the generic skeleton does not carry the class machinery.
8. **vs Event Management** — single-occasion seminars/workshops ride adjacent registration machinery (observed at one product); the Type's center is the recurring series and the lesson, not one-off events.
9. **vs Dog Walking Platform / Pet Sitting Platform** — operator-side administration of the business's own clients and offerings vs two-sided consumer matching of strangers (family-consistent).
10. **vs Veterinary Practice Management** — vaccination data here is eligibility data on the dog record, never a clinical workflow (family-consistent).

**Cluster observation DISCHARGED**: the §29 pet-care cluster (boarding / daycare / grooming / training single-line leaves + whole-business umbrella) is confirmed as one product population at multiple scope cuts. The training leaf is the training-line scope cut; its unit of work (class-series enrollment + private lessons) is structurally distinct from the other three lines' units (stay / attendance / appointment), which is why it survives as an independent single-line Type.

## Uncertainties

- **Class-level capacity at Gingr/PetExec**: not directly observed in fetched articles (DogBizPro and ProPet document it). Capacity is held as common, not invariant; if Gingr/PetExec lack class limits the L0 is unaffected (capacity sits with the roster structure, not as a separate leg).
- **Private-lesson-only pole**: no sampled product is private-lesson-only; the shape is evidenced as a first-class module/feature everywhere, and the L0 is written to admit it (offering = series and/or lesson). A dedicated private-lesson-only training product was not sampled.
- **Vaccination enforcement style for training** (block vs alert): not observed at article level in this sample; held as standard capability with variant enforcement, consistent with the family's rulings.
- **Regional products**: sample is US-centric; UK/EU training-club structures (Kennel Club Good Citizen classes, regional club software) not sampled — regional fit argued structurally.
- **Generic-scheduler pole**: solo trainers using generic booking tools were not sampled; the boundary against generic scheduling is argued from structure, not from a sampled generic-tool deployment.
- **PetExec training documentation depth**: the Training subject-area PDF is not machine-readable; PetExec's training model rests on product-page + documentation-structure evidence.

## Final Synthesis

Pet Training Management is the training business's operator-side system of record. Its world has four load-bearing structures held jointly: the client account with dogs (the animal as enrolled subject), the scheduled training offering (class series and private lesson, catalog distinct from occurrences), the enrollment binding (per-dog roster/booking against bounded capacity), and the tuition loop (enrollment resolves into money on the client account). Everything else modern products carry — trainer assignment, attendance, report cards, graduation, vaccination gating, portals, waitlists, events, virtual classes — is standard capability or variant, not definition. The Type is the training-line scope cut of the §29 pet-care cluster: same product population as the umbrella sibling, distinct unit of work from the grooming/boarding/daycare siblings, and structurally distinct from human class businesses and learning-management Types because the enrolled subject is an animal and the offering is a scheduled service, not content.
