# Research Notes — Scholarly Conference Management

Research date: 2026-09-09
Slug: scholarly-conference-management
Directory leaf: Scholarly Conference Management (§23 Education, Research & Knowledge Institutions)

## Research Goal

Understand what a Scholarly Conference Management system actually is in the real market: what objects exist inside it, who operates it, how the conference cycle works end to end (call → submissions → review → program → registration → event → proceedings), which rules and states govern it, and where this Application Type ends relative to its neighbors — above all **Peer Review Platform** (processed sibling with a pre-hung joint-review flag that this pass must resolve), **Event Management Platform** (§26), **Academic Journal Management** (processed sibling), and the §26 event-family leaves (Event Registration, Event Agenda Management, Convention/Exhibition Management).

## Initial Boundary (pre-research hypothesis)

- Core use: the conference organizer's system of record for running a scholarly conference — the submission/review machinery that produces the conference's content, the program/schedule built from accepted works, participant registration, and (commonly) proceedings and virtual/hybrid delivery.
- Primary users: conference/program chairs and organizers (operators); authors/presenters and reviewers (external participants); delegates (attendees).
- Nearest neighbors: Peer Review Platform (the review exchange alone — flag pre-hung by that pass), Event Management Platform (generic event logistics), Academic Journal Management (the publication container), Event Registration Platform, Event Agenda Management, Convention/Exhibition Management, Association Event Management.
- Open questions: is registration definitional or common? Is the program-assembly step (accepted works → sessions/schedule) the seam vs Peer Review Platform? Where does the Type end vs generic event management (Cvent sells "abstract management" inside an event platform)? Is "scholarly" definitional or is the machinery audience-neutral? Does the per-edition instance structure matter?

## Research Questions

1. What is the unit of record — the conference edition? What does one instance contain?
2. What is the content pipeline: how do submissions become program content? Is the same object carried from submission through review into the schedule?
3. What program-building machinery exists (tracks, sessions, session blocks, schedule, rooms, presenters, conflict checking)?
4. What participant machinery exists (registration forms, fee groups, payments, check-in)? Is it definitional?
5. What event-side machinery exists (virtual/hybrid, mobile apps, on-site tools)?
6. What publication machinery exists (proceedings, abstract books)?
7. Where is the seam vs Peer Review Platform (resolve the pre-hung flag), vs Event Management Platform, vs Academic Journal Management, vs the §26 event family?
8. Historical check: would paper-era conference organization satisfy the same core?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer levels:

| Product | Operator / Owner | Philosophy | Customer level | Evidence tier |
|---|---|---|---|---|
| ConfTool | ConfTool GmbH (Germany) | classic full-lifecycle academic event system: submission+review+scheduling+registration+on-site | individual conferences, workshops, congresses; 5,000+ organizers (vendor claim); free Standard edition for small events | Tier 1 (features page, homepage) + Tier 1 user docs (sibling pass) |
| Ex Ordo | Ex Ordo (Ireland) | modern all-in-one "scholarly events partner": Review / Register / Programme / Manage / Virtual pillars + proceedings book + mobile app | scientific, medical, technical societies and associations (1,512 conferences, vendor claim) | Tier 2 (official product pages) |
| Oxford Abstracts | Oxford Abstracts Ltd (UK) | abstract-management-first platform tiered up to a full conference site (program builder, networking, posters, exhibitors) | societies, associations, universities (1,000+ events/yr, vendor claim); per-event pricing | Tier 2 (official product pages + pricing) |
| Indico | CERN (open source) | open-source event platform whose conference shape = programme/tracks + CFA + review + timetable + registration | institutional/event organizers (CERN heritage); self-host or cloud | Tier 1 (official user guide) |
| EasyChair | EasyChair (since 2002) | long-established free/low-cost workhorse: conference management + registration + publishing + Smart Program | individual conferences worldwide (4.9M users / 125k conferences, vendor claims) | Tier 2 (official product pages; help center unreachable per sibling pass) |

Boundary/variant probes (not primary samples): **Microsoft CMT** (Tier 1 docs, this pass + sibling pass — review-workflow pole), **OpenReview** (Tier 1 docs, sibling pass — peer-review-platform pole), **Cvent Abstract Management** (Tier 2 product page — generic event platform with the pipeline as a module).

## Sources

### ConfTool — Tier 1 (conftool.net)

- Homepage ("Web-based event management system… academic conferences, workshops, congresses and seminars"; Standard vs Pro; benefits list) — https://www.conftool.net/en/
- Features page (full feature list: general/roles, submission, reviewing, multi-track, schedule creation, participant registration, on-site, payments, email, import/export, security) — https://www.conftool.net/en/features.html
- Reviewer/PC user documentation (bidding, conflicts, confidentiality, review forms, PC forum, reviews hidden until decision) — fetched in the sibling peer-review-platform pass (2026-09-08)

### Ex Ordo — Tier 2 (exordo.com)

- Homepage (pillars; "managing a research conference"; "scientific, medical, and technical events"; gather content → build event → manage attendees) — https://www.exordo.com/
- Conference Management ("Manage" pillar: one login, access levels, dashboard, insights, communication hub, exports) — https://www.exordo.com/product/conference-management
- Conference Programme ("Programme" pillar: visual builder, assign submissions to sessions, conflict checker, share online, mobile app, Book of Proceedings) — https://www.exordo.com/product/conference-programme

### Oxford Abstracts — Tier 2 (oxfordabstracts.com)

- Homepage ("The Academic Conference Platform"; two products; 4-step pipeline Submission → Reviewing → Decisions → Ticketing; hidden gems) — https://www.oxfordabstracts.com/
- Academic Conference Software page (program builder, live conference site, networking, poster gallery, exhibitors, on-demand/live content; pricing tiers per event) — https://www.oxfordabstracts.com/product/academic-conference-software/

### Indico — Tier 1 (learn.getindico.io, official user guide)

- User guide index (event types; conference feature list) — https://learn.getindico.io/
- Conference introduction ("complex event… Programme definition and Call for Abstracts, Abstract submission, participants' Registration/Application… e-payment facilities and publication Review") — https://learn.getindico.io/conferences/about/
- Defining the Programme (tracks before CFA) — https://learn.getindico.io/conferences/programme/
- Making a Timetable (sessions / session blocks / contributions / breaks; contributions shared across CFA, reviewing, editing, timetable; poster sessions; draft mode) — https://learn.getindico.io/conferences/timetable/
- Configuring the Registration Process (forms, sections/fields, moderated workflow, payments, invitations) — https://learn.getindico.io/conferences/registration_config/
- Reviewing abstracts + paper peer reviewing docs — fetched in the sibling pass (2026-09-08)

### EasyChair — Tier 2 (easychair.org; help center unreachable per sibling pass)

- Homepage (services: conference management, registration, publishing, Smart CFP/Slide/Program; scale claims; since 2002) — https://easychair.org/
- Registration service page (attendee registration + online payment; fee formulas; period/type pricing; currencies; registration managers with permissions; "authors and reviewers can register using the same environment") — https://easychair.org/registration
- Smart Program page (program pages generated from submission data; schedule analysis/constraint violations; automatic schedule generation; collocated joint programs; printable booklet) — https://easychair.org/smart_program
- Conference Management page (CFP → submission → reviewer management → reviewing → communication → program → proceedings → registration) — fetched in the sibling pass (2026-09-08)

### Microsoft CMT — Tier 1 (cmt3.research.microsoft.com; probe)

- Docs index ("conference management system for hosting academic conferences… handles the most complex workflows of academic conferences"; per-year site requests) — https://cmt3.research.microsoft.com/docs/ (fetched; deeper docs from the sibling pass: chair how-tos, FAQ, roles, tracks, deadlines, desk reject, withdraw)

### OpenReview — Tier 1 (docs.openreview.net; probe, sibling pass)

- Venue workflow (venue request → submission → matching → review → rebuttal → meta-review → decision → camera-ready; venue homepage only; no registration/timetable/program machinery)

### Cvent — Tier 2 (cvent.com; probe)

- Abstract Management Software page (Collect → Review → Decide → Publish; "create sessions directly from accepted submissions and publish them into the event agenda"; "integrated with Cvent Event Management"; FAQ naming conferences, association meetings, scientific/medical and academic events, awards programs) — https://www.cvent.com/en/abstract-management-software (first URL guess 404; second attempt succeeded)

---

## Product Observations

### ConfTool — evidence layer A (official features page + homepage; user docs via sibling pass)

**Positioning.** "Web-based event management system developed to support the organization of academic conferences, workshops, congresses and seminars." Scope named on the homepage: submission and review of contributions, scheduling of the conference program, registration/administration/invoicing of participants, communication, "many other of the tasks of the organizer."

**Instance structure.** A separate database is set up independently for each conference; customer configuration can be stored and adapted for future conferences. Two editions: ConfTool Standard (free, ≤150 participants, local install, basic functions) and ConfTool Pro (hosted SaaS, full features).

**Roles.** Access control by user role: "author", "reviewer", "chair", "administrator"; Pro adds "conference assistant", "conference chair", "track chair", "session moderator", "discussant", "meta reviewer", and a "frontdesk" role for on-site check-in staff. One account, several roles, no account switches.

**Submission & reviewing.** Customizable submission process; file uploads with format checks; submission types (full papers, posters, short papers) and three standard form shapes (abstract/paper, symposium proposal for multi-paper submissions, applications for grants/scholarships/summer schools); topics and topic groups; deadlines per type with automatic function disabling; final upload (camera-ready) for accepted submissions; reviewer invitations and import; bidding; priority topics; automatic assignment taking into account conflicts of interest, biddings, priority topics, and workload; customizable review forms (up to 16 criteria, weighing factors, configurable scales); single-blind / double-blind / open review postures; meta-reviewers; rebuttals; PC online forum with voting; acceptance statuses set by chairs based on review results; best-paper nomination and reviewer veto.

**Schedule creation (the program).** "Assign Presentations to Sessions — define sessions and assign each accepted submission to one of them"; "Create Conference Agenda — includes time periods and room assignments for each session"; agenda in table or list view; abstracts and presentation files made available on agenda pages; agenda public or restricted to registered participants; discussants assigned to sessions; overlap/conflict analysis of presenters, moderators, discussants and chairs; personal agenda ("MyAgenda"); author index; links to external resources (live streams, video conferencing) per session and per presentation for virtual events; mobile app interface (Conference4Me); discussion boards for sessions and presentations.

**Participant registration.** Full online registration; participant status groups with specific prices (regular/member/student); time discounts ("early bird", "on-site"); discount codes; customizable registration form with conditional items and availability limits; automatic tax invoice creation (VAT modes); payment options (wire, cheque, cash, PayPal, Stripe, SOFORT, 25+ gateway modules); payment log with refunds/partial payments; invitation letters and visa invitation letters for authors/presenters; online participant list with photos and messaging; registration deadlines; editing/canceling rules; **"Restrain Registration to Authors or Presenters Only"** and **"Make registration for participation mandatory"** as a submission condition — the registration↔submission coupling is explicit.

**On-site.** Check-in and marking attendees at the registration desk; frontdesk role with limited data access; front-desk registration of last-minute participants; real-time lists; bulk printing of invoices/receipts/confirmations; export/print of attendee lists as backup.

**Exports.** Submissions, abstracts, review results, author index, participant lists, payments — "data export to facilitate the creation of proceedings."

### Ex Ordo — evidence layer B (official product pages)

**Positioning.** "Your Scholarly Events Partner… Easy-to-use, efficient software. Designed for scientific, medical, and technical events." "We've built the best software in the world for managing a research conference." Vendor metrics: 1,512 conferences; 799,187 researchers & professionals.

**Product pillars.** Review ("abstract management software… built for painless peer review" — collect abstracts, papers, speaker proposals or symposia/panels through a custom submissions form; "match submissions to the best reviewers, then track their progress. When you're ready, notify presenters right from your dashboard"); Register ("registration system for research conferences, not rock concerts" — card payments/bank transfer; message authors, reviewers, delegates); Programme; Manage; Virtual (virtual/hybrid event space with live sessions and on-demand videos; content stays on the platform for a stated period after the event).

**Programme pillar (the program builder).** "Assign submissions, add downloadable presentations, and share your programme online without coding a thing." Visual builder for "multiple streams, parallel sessions and thousands of submissions": assign existing submissions or add new content; see which submissions are already assigned; preview before going live. **Conflict checker**: "ensure presenters are never scheduled to be in two places at once" — direct time conflicts, potential conflicts, overloaded presenters. Sharing: public link or logged-in only; presenter bios, presentations and posters collected and shared; export as PDF/Excel/Word. Mobile app (Android/iOS) with offline schedule and personalized itineraries. **Book of Proceedings** add-on: print-ready book of abstracts or papers with cover, foreword, table of contents, full submission list, author index.

**Manage pillar.** One login for chairing, submitting, reviewing, registering with access levels; conference dashboard with intelligent cards and submission stats; insights/reports at any stage; communication hub (select contacts, filter e.g. "late reviewers, accepted authors or delegates who haven't paid", macros, templates); exports of submissions, reviews, author details, registration data, presentations.

### Oxford Abstracts — evidence layer B (official product pages + pricing)

**Positioning.** "The Academic Conference Platform… software purpose-built for academic event organisers." "From submission through to presentation, Oxford Abstracts supports you at every step of your academic conference." 20+ years; 1,000+ events per year (vendor claims). Customers: University of Oxford, UCLA, learned societies (Parkinsons UK, Econometric Society, Royal College of Surgeons…).

**Two products, one pipeline.** Abstract Management Software and Academic Conference Software. The pipeline is presented as four steps: **1. Submission** (tailor submission forms) → **2. Reviewing** (reviewer-friendly, auto-save) → **3. Decisions** (streamlined decision process) → **4. Ticketing** (adjustable ticket types, coupons, add-ons; Stripe/PayPal integration).

**Conference tier adds the event.** "Alongside powerful abstract management, you'll have an easy program builder, dynamic networking capabilities, an interactive poster gallery, comprehensive exhibitor options—and much more." Pricing tiers: Abstract Management ($890/event) → Standard Conference ($2290/event: live conference platform, program builder, on-demand & live content, Zoom integration) → Professional Conference ($3450/event: attendee networking, interactive poster gallery, exhibitor spaces & sponsors, event splash page, program access controls).

**Program builder.** "Effortlessly import your abstracts into the program builder and craft your conference. With the ability to design multi-track days seamlessly." Attendees bookmark sessions into a personal itinerary. "Instant Abstract Books — create a fully formatted and beautifully designed abstract book in seconds." Submitters log in to view results; certificates; symposium support; multi-stage submissions.

### Indico — evidence layer A (official user guide)

**Positioning.** "A web application which facilitates the organization of events of all sizes, ranging from meetings and lectures to big conferences." Open source, CERN. Event types: lectures, meetings, conferences. A **Conference** is "a complex event with many features, including Programme definition and Call for Abstracts, Abstract submission, participants' Registration/Application to the event, e-payment facilities and publication Review."

**Programme.** The conference program is divided into **tracks** ("tracks cover the subjects presented at the conference"); tracks must be defined before the Call for Abstracts opens "so that submitters can choose the track their abstracts belong to."

**Timetable anatomy (the program structure).** Four elements: **Sessions** (group related contributions), **Session blocks** (a scheduled instance of a session with start/end — e.g. morning and afternoon blocks; only blocks are scheduled, never sessions directly), **Contributions** (the talks/presentations), **Breaks**. Poster sessions schedule their contributions in parallel. **The pipeline link, verbatim:** "In a meeting, a contribution is an entry in the timetable… and it has no other purpose outside the timetable. In conferences, contributions are much more versatile and besides the timetable, they are also used for the Call for abstracts and the Peer reviewing and Editing modules." — the same contribution object flows from submission through review into the schedule. Scheduling operations: drag to retime, move between days/blocks (auto-assigns to the session), reschedule (stack entries, fill gaps), fit-to-content.

**Publication states.** By default contributions are in **Draft mode**: regular users cannot see the contributions list, the timetable, the book of abstracts, or the author/speaker list; draft mode is turned off to publish the program.

**Registration.** Registration forms per event with sections and typed fields (e.g. an Accommodation field with priced options and place limits); **moderated workflow** option (manager approves each registration); payments enabled per event (bank transfer with IBAN, PayPal); modification rules explicitly tied to payment state ("wise to allow modifications only until the payment is done… change of such settings after payment may entail change of the total due amount"); invitations (Indico users or external people) with optional skip-moderation; registration opened/closed by the manager.

**Event-side modules.** Room booking module (locations selectable for session blocks); Zoom plugin; event surveys; reminders; calendar import; document generation (templates → e.g. books of abstracts); custom roles; people management.

### EasyChair — evidence layer B (official product pages; conference-management page via sibling pass)

**Positioning.** "You chair a conference. We have all you need. One platform: EasyChair." Services: Conference management ("From managing program committees to publishing proceedings"), Registration, Publishing, Smart CFP, Smart Slide, Smart Program. Since 2002; vendor claims 4.9M users, 125,287 conferences, 21M+ pages/month.

**Conference management scope (sibling pass, product page).** (1) Call for submissions (Smart CFP); (2) abstract and paper submission; (3) reviewer management (PC management, reviewer database, access/COI management, preference-based assignment); (4) reviewing (reviews, online discussion, author rebuttal phase); (5) communication and monitoring; (6) program editing/publishing (Smart Program); (7) proceedings preparation; (8) attendee registration and online payment. Standard (single PC) and multi-track (per-track PCs + track chairs + superchair) models.

**Registration service.** "Implements attendee registration and online payment"; flexible forms; "complex pricing and fee calculations using formulas"; different prices for different registration periods and registration types; online payments in a stated number of currencies, wire transfers in fewer; registration managers with data-access policies; "A unique feature for updating registrations, including payment-related information, even after payments have been made." **Coupling, verbatim:** "Your authors and reviewers can register using the same environment they used for submission and reviewing."

**Smart Program (program generation).** Program pages generated with "very little cost to the organizers… In many cases this data was taken from submissions already available in EasyChair, so very little work, or no work at all, was required to use this data in the online program." Capabilities: program committee and accepted-papers pages in minutes; thousands of pages in one click; author-editable data; **constraint checking on the program** ("schedule analysis can find constraint violations, including automatically found constraints, and other problems such as empty sessions, talks without presenters, a presenter scheduled to chair a parallel session"); automatic discovery of similar talks to ease session mapping; automatic schedule generation based on talk similarity; **joint programs of collocated conferences**; printable booklet (Word).

**Publishing.** "Publication services are integrated with conference management, this providing a seamless process of submission-to-publication of reviewed content."

### Microsoft CMT — evidence layer A (probe; docs index this pass + chair docs/FAQ via sibling pass)

"Conference Management Toolkit (CMT) is a conference management system for hosting academic conferences, sponsored by Microsoft Research… CMT handles the most complex workflows of academic conferences." Per-year site requests; Azure-hosted; 12,000+ conferences (vendor claim). Documented machinery: submission configuration (multi-track, deadlines, supplementary material, desk reject, withdraw), review workflow with roles (author, reviewer, meta-reviewer, senior meta-reviewer, track chairs), conflict-driven review visibility. **No registration, no session/schedule/program-building, and no proceedings machinery are evidenced in the accessible documentation** — CMT is the review-workflow engine of the conference cycle.

### OpenReview — evidence layer A (probe; sibling pass)

Venue request → submission → matching → review → rebuttal → meta-review → decision → camera-ready. The "venue" is a review venue with a homepage; **no registration, no timetable, no program building, no event logistics of any kind**. This is the Peer Review Platform product shape.

### Cvent Abstract Management — evidence layer B (probe)

Cvent is a generic event platform (registration, venue sourcing, diagramming, check-in, event app, hospitality). Its **Abstract Management** module implements the same content pipeline in four stages — **Collect → Review → Decide → Publish**: customized submission forms for "abstracts, sessions, papers, or awards"; reviewer assignment by track/topic with a scoring portal; accept/reject decisions with automated notifications; "Finalize and publish speakers and content, then build your agenda and open sessions for registration… create sessions directly from accepted submissions and publish them into the event agenda… Abstract Management is integrated with Cvent Event Management." FAQ: the pipeline is "especially valuable for conferences, association meetings, scientific/medical and academic events, awards programs, and any event with many sessions or speakers." — the pipeline exists inside generic event management as an add-on module; the organizing whole is the event platform, not the pipeline.

---

## Cross-product Comparison

| Dimension | ConfTool | Ex Ordo | Oxford Abstracts | Indico | EasyChair | CMT (probe) | OpenReview (probe) | Cvent (probe) |
|---|---|---|---|---|---|---|---|---|
| Edition as managed instance | separate database per conference; config reuse for future editions | per-conference dashboard/branding | per-event pricing & setup | event instance of type "conference" | create conference; per-conference license | per-year site requests | venue instance (review venue) | event project linked to abstract project |
| Call & submission forms | customizable; 3 standard form shapes (paper/abstract, symposium, applications); types & tracks | custom submissions form (abstracts/papers/proposals/panels) | tailored forms; multi-stage; symposium | CFA module; tracks chosen by submitters | Smart CFP; abstract/paper submission | multi-track submission config | submission invitations per venue | customized forms (abstracts/sessions/papers/awards) |
| Evaluation stage | bidding, COI, review forms, PC forum, meta-reviewers, acceptance statuses | match to reviewers, track progress | reviewing → decisions | abstract review (ratings/judges) + paper peer review module | preference-based assignment, discussion, rebuttal | full review workflow w/ meta-reviewers | matching, review, meta-review, decision | reviewer portal, scores/votes, accept/reject |
| Accepted works → program | "assign each accepted submission to one of them" (sessions); agenda with periods & rooms | visual builder assigns submissions to sessions/streams | "import your abstracts into the program builder" | contributions (from CFA/review) scheduled into session blocks | Smart Program built from submission data | NOT EVIDENCED | none | "create sessions directly from accepted submissions" |
| Program structure | sessions; discussants; MyAgenda; author index | streams, parallel sessions; conflict checker | multi-track days; session bookmarks | sessions → session blocks → contributions → breaks; poster sessions | sessions, talks, chairs; constraint analysis | — | — | event agenda sessions |
| Program publication | public or participant-restricted agenda | public link or logged-in; mobile app | live conference site | draft mode → publish (timetable, abstract book, author list) | public program pages (thousands, one click) | — | — | publish into event agenda |
| Registration & payments | full module: groups/prices, early-bird, invoices, gateways, on-site frontdesk | Register pillar: card/bank transfer, messaging | ticketing tier: types, coupons, add-ons, Stripe/PayPal | forms, moderated workflow, bank transfer/PayPal, invitations | registration service: fee formulas, period/type pricing, currencies | NOT EVIDENCED | none | via Cvent Registration |
| Presenter↔registration coupling | restrain registration to authors/presenters; mandatory registration as submission condition | presenters notified from dashboard; register pillar | submitters view results; ticketing integrated | — | "authors and reviewers can register using the same environment" | — | — | sessions opened for registration |
| Proceedings / abstract book | export "to facilitate the creation of proceedings" | Book of Proceedings add-on (print-ready) | instant abstract books | document generation (book of abstracts) | proceedings preparation + publishing services | NOT EVIDENCED | camera-ready hosting only | — |
| Virtual / hybrid | links to external resources per session/presentation; alternative time display; time zones | Virtual pillar (live + on-demand; retention window) | live conference site, on-demand & live content, Zoom | Zoom plugin; external links | Smart Slide (slides before/after) | — | — | virtual/hybrid via Cvent stack |
| On-site | check-in, frontdesk role, badge lists | — | — | room booking module (locations) | — | — | — | OnArrival check-in (separate product) |
| Deployment | SaaS (Pro) / local install (Standard, free ≤150 participants) | SaaS | SaaS, per-event pricing | open source, self-host or cloud | free/low-cost per-conference licensing | free cloud toolkit | nonprofit-operated service | enterprise event platform |

**The pipeline is the invariant across all eight products** (including the probes): call → submissions → evaluation → decisions → accepted works become the event's program content. What varies is the organizing whole around it: full conference systems (ConfTool, Ex Ordo, Oxford Abstracts conference tier, Indico, EasyChair) wrap the pipeline in the edition container + program + registration; CMT wraps it in almost nothing (review workflow only); OpenReview wraps it in nothing; Cvent embeds it as a module in a generic event platform.

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the software stops being recognizable as a scholarly conference management system:

1. **The conference edition as the managed event of record.** A persistent, individually identified event instance — dated, per-edition — that anchors the call, the committee, the program, and the participants. Conferences are run as instances (separate databases, per-year sites, per-event setups), with configuration commonly carried over between editions. Remove → disconnected review runs and generic tools; there is no "the conference" being managed.
2. **The submission-to-acceptance content pipeline.** Works (papers, abstracts, posters, panels, proposals) are submitted against the conference's call through configured forms, evaluated (peer review the dominant mechanism; light screening and no-review acceptance are configured postures of the same machinery), and resolved into recorded acceptance decisions. The conference's content is *produced* by this pipeline — contributed from the research community and selected by evaluation — not curated by organizers. Remove → generic event management (invited speakers, curated agenda).
3. **The program assembled from accepted works.** Accepted submissions become presentations placed into the event's program structure — sessions (grouped by tracks/subjects), scheduled into time blocks with rooms/locations, with their presenters — and the program is published as the conference agenda (public or participant-restricted). Remove → a review exchange with decisions but no event program (peer-review-platform territory).

Jointly-held is load-bearing:

- 1 alone = generic event management (curated agenda, invited speakers)
- 2 without 1 = the review exchange alone = Peer Review Platform (OpenReview shape) or an abstract-management module
- 3 without 2 = a schedule builder over curated content = Event Management territory
- 1+2 without 3 = a review venue attached to an event shell with no program assembly (CMT-shaped straddle)
- 1+3 without 2 = an event with a program nobody submitted to (contradiction; collapses into curated event management)
- 2+3 without 1 = pipeline + program publishing with no event container (the abstract-management-module shape inside a host platform)

**Historical / market-sample check (§24-style, conceptual + in-sample).** Paper-era conference organization satisfies all three legs with no software: the secretariat issues a call for papers; authors mail submissions; the program committee reviews them and records accept/reject; accepted papers are scheduled into a printed program of sessions with their speakers; participants register by mail and pay fees. The 2000s web generation (EasyChair since 2002, CMT, ConfTool) satisfies the legs with no virtual events, no mobile apps, no algorithmic matching, no conflict checkers. The definition therefore names **no format (in-person/virtual), no registration module, no anonymity mode, no pricing model, no proceedings pipeline, no matching algorithm, no mobile app** — all are era-, posture-, or packaging-specific realizations. The word "scholarly" reflects the leaf's placement and the market's center of gravity (academic conferences), not a structural requirement: the same three-leg machinery serves association and technical conferences with contributed content (Cvent's own FAQ names "conferences, association meetings, scientific/medical and academic events, awards programs").

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- **Registration & payments** — participant groups with differentiated prices, time-discount periods (early bird), configurable registration forms with conditional items and availability limits, invoices/receipts (VAT handling), payment gateways and manual payment entry, refunds/partial payments, late-payer tracking. Present in ConfTool, EasyChair, Ex Ordo, Oxford Abstracts, Indico, Cvent; absent in CMT and OpenReview.
- **Presenter↔registration coupling** — registration restricted to authors/presenters, mandatory registration as a submission condition, presenters registering in the same environment they submitted in, accepted presenters notified to register. (Direction and enforcement vary by product.)
- **Camera-ready / final upload** — accepted submissions re-enter to deposit final versions (ConfTool final upload, Indico paper editing, OpenReview camera-ready, EasyChair proceedings input).
- **Communication machinery** — bulk personalized email to authors/reviewers/delegates, templated automatic notifications at every stage transition (submission received, review assigned, decision released, registration confirmed), reminder scheduling.
- **Role system over one account** — author/reviewer/chair/administrator plus program-level roles (track chairs, meta-reviewers, session moderators, discussants, conveners, frontdesk); one account carrying several roles with access levels.
- **Multi-track support** — per-track forms, deadlines, committees, and chairs.
- **Personal agendas** — attendee-built itineraries (MyAgenda, session bookmarks, mobile-app schedules).
- **On-site operations** — check-in/attendance marking, frontdesk roles, badge/attendee lists, last-minute registration.
- **Exports & reports** — submissions, reviews, registrations, payments, author indexes; proceedings-data exports; dashboards/stats at every stage.
- **Proceedings / abstract book output** — in-product book generation (Ex Ordo Book of Proceedings, Oxford Abstracts instant abstract books, Indico document generation), proceedings preparation + publishing services (EasyChair), or export-for-publisher (ConfTool).
- **Virtual/hybrid delivery surfaces** — external links per session/presentation, embedded live streams, on-demand content, Zoom integration, slide hosting.
- **Session-level discussion/networking** — discussion boards on sessions and presentations, attendee networking, poster galleries.
- **Awards** — best-paper nomination flows, award galleries.

### L2 — Variant / Optional Structure

- **Event format** — in-person, virtual, hybrid; virtual-only venues with on-demand content.
- **Scale & collocation** — workshop → mega-conference; joint programs across collocated conferences/workshops (EasyChair Smart Program).
- **Review intensity** — full paper peer review; abstract review with presentation-type decisions; light screening; no-review acceptance — configured postures of the same pipeline.
- **Anonymity postures** — single-blind, double-blind, open (inherited from the review stage; configurable).
- **Proceedings posture** — generate in-product, hand off to a publisher, or publish via integrated services.
- **Venue/room logistics depth** — integrated room booking (Indico module) vs external venue tools.
- **Deployment & pricing** — SaaS subscription/quote, per-event pricing, free tiers (ConfTool Standard, Oxford Abstracts Basic, CMT), open-source self-hosting (Indico).
- **Exhibitor/sponsor machinery** — exhibitor spaces, sponsor content, poster galleries (Oxford Abstracts Professional tier, Cvent).
- **Certificates & letters** — attendance certificates, presentation certificates, invitation/visa letters.
- **Surveys** — event surveys (Indico).
- **Mobile apps** — native event apps with offline schedules (Ex Ordo, ConfTool's app interface, Cvent).

### L3 — Vendor-specific (research notes only)

- **ConfTool**: Standard/Pro edition split (free ≤150 participants, local install); frontdesk role; Conference4Me mobile-app interface; discussant role; reviewer veto and best-paper nomination; review-criteria weighing factors (0–100%); up to 9 alternative review forms; German hosting, per-conference databases, data deletion after project end; visa invitation letters; pro-forma invoices; multi-currency limits (one main currency per conference).
- **Ex Ordo**: pillar naming (Review/Register/Programme/Manage/Virtual); Book of Proceedings and Mobile as add-ons; conflict checker framing (direct/potential/overload); content retention window after the event (stated as 60 days); Postmark delivery; PCI/GDPR posture claims; vendor metrics.
- **Oxford Abstracts**: per-event pricing tiers ($890/$2290/$3450, vendor-stated); "hidden gems" (title-case tool, reviewer auto-save, scheduled reminders, bulk assign by category); Zoom integration; program access controls; event splash page.
- **Indico**: contribution/session-block model (sessions never scheduled directly; blocks are the schedulable units; poster sessions schedule in parallel); draft-mode publish toggle covering timetable + book of abstracts + author list; category tree of events; room booking module; event series; document-generation templates; reschedule/fit-to-content operations; moderated registration workflow; modification-until-payment rule.
- **EasyChair**: Smart CFP/Smart Slide/Smart Program services; PC-expert; superchair multi-track model; schedule analysis with named constraint violations (empty sessions, talks without presenters, presenter chairing a parallel session); automatic schedule generation from talk similarity; collocated joint programs; 15-currency online payments (vendor-stated); registration updates after payment; publishing services list; VSL 2014 mega-conference example (2,196 program pages).
- **CMT**: per-year site requests; Azure hosting with geo-replication; ~2-year data retention then deletion (sibling pass); supplementary material as separate activity; desk-reject visibility options.
- **Cvent**: abstract management as a module of the event platform; Speaker Resource Center companion; OnArrival check-in; Attendee Hub; hospitality-side products (out of scope).

## Vendor-specific Findings / Rejected Findings

- **Rejected from core**: "registration is definitional" — CMT (a self-described conference management system) and OpenReview carry no registration; ConfTool/EasyChair/Ex Ordo/Oxford Abstracts/Indico/Cvent all do. Registration is the strongest L1 item, not an invariant.
- **Rejected from core**: "full peer review is definitional" — the pipeline's selection stage runs at varying intensity (full paper review, abstract screening, light/no-review acceptance); the invariant is evaluation-gated selection of contributed content, not the review protocol.
- **Rejected from core**: "virtual/hybrid delivery is definitional" — era-current machinery; ConfTool satisfies the core by linking out to external streams; the paper era satisfies with none.
- **Rejected from core**: "proceedings are definitional" — the export-for-publisher pole (ConfTool) and camera-ready-only pole (OpenReview) show proceedings machinery is packaging depth, not identity.
- **Rejected from core**: "algorithmic scheduling/matching is definitional" — manual assignment and manual scheduling satisfy the core everywhere; conflict checkers and auto-scheduling are mature conveniences.
- **Rejected**: "the Type is scholarly-only" — the machinery is audience-neutral (Cvent's association/awards customers); "scholarly" is the market center of gravity and the directory's placement, not a structural requirement.
- **Rejected**: precise numeric limits (file sizes, participant caps, currency counts, retention windows) — vendor-documented figures kept in research notes only; not asserted in the final document beyond what evidence supports.

## Boundary Findings

1. **vs Peer Review Platform (§23 sibling, processed) — JOINT REVIEW DISCHARGED from this side; keep-both RATIFIED.** The sibling's flag: 5/6 of its sampled review platforms bundle event/program machinery while OpenReview runs the exchange alone; proposed seam "remove event/program/registration → peer review platform remains; remove review exchange → event management remains." This pass confirms the seam from the conference side and adopts it: the discriminator is **the organizing whole**. Peer Review Platform = the review exchange as the entire product (submissions → pairing → reviews → outcomes; OpenReview proves the shape with no event container, no program, no registration). Scholarly Conference Management = the conference event as the organizing whole (edition container + submission→program pipeline + commonly registration/proceedings/event surfaces), with the review exchange as one stage of its pipeline. Removal tests hold in both directions: strip the event/program/registration machinery from a bundled product and a peer review platform remains (OpenReview is exactly that shape); strip the review/pipeline machinery and a generic event management system remains (Cvent's event stack without its abstract module). The bundled products (EasyChair, ConfTool, Indico, OpenWater — and CMT) are conference management systems whose review machinery realizes the same exchange the Peer Review Platform Type specializes in; bundling is packaging, not identity. **CMT is documented as the straddler**: it self-labels "conference management system" and is used by conferences, but its evidenced machinery is the paper workflow (submission/review/decisions/roles/tracks) with no program, registration, or event machinery — it sits exactly on the seam, review-side-heavy. Both leaves stand; both documents cross-reference each other.
2. **vs Event Management Platform (§26).** The seam is the content pipeline. Generic event management centers the event's logistics: registration/checkout, venue sourcing, curated agenda of invited speakers, check-in, apps, analytics. Scholarly conference management centers the produced-content pipeline (submission → evaluation → program) wrapped in the edition container. The Cvent probe shows the pipeline existing *inside* generic event management as an add-on module ("create sessions directly from accepted submissions and publish them into the event agenda") — same machinery, different organizing whole. Remove the pipeline → generic event management remains; remove the event logistics → the pipeline remains (peer review platform / abstract-management module). Keep-both.
3. **vs Convention / Exhibition Management (§26).** Convention/exhibition centers trade-show semantics (exhibitors, booths, lead retrieval, floor plans); scholarly conference management centers the contributed-content pipeline. Exhibitor/sponsor modules appear inside conference products (Oxford Abstracts Professional tier, Cvent) as packaging. Keep-both.
4. **vs Academic Journal Management (§23, processed).** The seam is the container and the lifecycle: the journal is an ongoing publication container (sections, issues, production pipeline) with review as a stage; the conference is a dated edition whose pipeline produces the event's program, with proceedings as an output that is often handed to a publisher or published via services (EasyChair publishing: "submission-to-publication of reviewed content"). Remove the event/program → the pipeline serves journals (journal management / peer review platform); remove the journal container → conference management stands. Consistent with the journal pass's joint-review resolution.
5. **vs Event Registration Platform (§26).** Registration is one module of the conference system (L1); standalone registration platforms center ticketing/checkout for events generally, with no content pipeline and no program. Keep-both.
6. **vs Event Agenda Management (§26).** Schedule building exists on both sides; the discriminator is the source of the agenda content: assembled from evaluated submissions (this Type) vs curated by organizers (event management). A schedule builder without the pipeline is event-management territory.
7. **vs Association Event Management (§25).** Associations run conferences with this exact machinery (Oxford Abstracts' society customers; OpenWater's abstract modules; Cvent's association solutions). The seam is the same content-pipeline line: association event management centers the association's broader event program (multi-event calendars, chapters, membership context); when a single contributed-content conference is the center, this Type applies.
8. **vs Attendee Management / Event Mobile App (§26).** Both are capability slices of the event side (L1 here, standalone Types there for the generic event market). No conflict.
9. **Naming observation.** The market says "conference management system/software" (EasyChair, CMT), "event management system" for academic events (ConfTool), "academic conference platform" (Oxford Abstracts), "scholarly events partner" (Ex Ordo), and "abstract management" for the pipeline module (Cvent, Oxford Abstracts tier 1). The leaf name "Scholarly Conference Management" is defensible: the conference edition + its content pipeline is the defining structure the sampled products share.

## Uncertainties

- CMT's exact feature edges (program building? registration?) could not be verified — the docs index was fetched but deeper pages sit behind a help-center structure the sibling pass partially 404'd on; CMT claims are calibrated to "review-workflow machinery documented; program/registration machinery not evidenced."
- EasyChair operational depth rests on product pages (help center unreachable per sibling pass); Smart Program's constraint vocabulary is vendor-stated.
- Ex Ordo and Oxford Abstracts evidence is product-page level; their help centers/knowledge bases were not fetched, so operational detail (exact scheduling constraints, refund rules, registration editing states) is not asserted.
- Indico registration detail beyond the fetched configuration page (invoices, confirmation flows) not verified.
- ConfTool organizer-side scheduling documentation was not fetched page-by-page; the features page documents the agenda module's capabilities at feature-list level.
- Vendor scale figures (ConfTool 5,000+ organizers; Ex Ordo 1,512 conferences; Oxford Abstracts 1,000+ events/yr; EasyChair 4.9M users/125k conferences; CMT 12k conferences) are vendor-stated marketing claims, recorded as such.
- The exact boundary behavior of association-focused abstract systems (OpenWater) vs this Type was resolved in the sibling pass (review core + program-family packaging); not re-litigated here.

## Final Synthesis

A Scholarly Conference Management system is the conference organizer's system of record for producing and running a scholarly conference. Its defining core is three jointly-held structures: the **conference edition** as a managed, per-edition event instance anchoring the call, the committee, the program, and the participants; the **submission-to-acceptance content pipeline** (call → configured submission forms → evaluation, peer review the dominant mechanism → recorded decisions) that produces the conference's content from the research community rather than curating it; and the **program assembled from accepted works** — accepted submissions become presentations placed into sessions on a published schedule, with their presenters. Around this core, mature products layer registration and payments (with explicit presenter↔registration coupling), camera-ready uploads, communication machinery, role systems over one account, multi-track support, personal agendas, on-site check-in, exports, proceedings/abstract-book output, and virtual/hybrid delivery surfaces. The Type is bounded against the Peer Review Platform (the review exchange alone, no event whole — joint-review flag discharged, keep-both), against generic Event Management (logistics-centered, pipeline as add-on module), against Academic Journal Management (publication container vs dated edition), and against the §26 event-family leaves (registration, agenda, convention/exhibition — capability slices or curated-content poles of the event side).
