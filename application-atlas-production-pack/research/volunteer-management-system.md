# Research Notes — Volunteer Management System

## Research Goal

Understand what a Volunteer Management System (generic, §25) is as an Application Type: what core structures define it, who uses it, how the volunteer program actually flows through the product, and where its boundaries sit against neighboring Types — Religious Volunteer Management (§25, processed 2026-09-09), Ministry Scheduling (§25, processed), Volunteer Marketplace (§25, unprocessed), Nonprofit CRM (§25, processed), Nonprofit Management Platform (§25, processed), Employee Scheduling (§09), HR/ATS (§09), Event Management (§26), Membership Management (§25).

## Initial Boundary

Initial hypothesis: a Volunteer Management System is the organization-side system of record for a volunteer program — volunteers held as records, volunteer opportunities as the demand structure, an intake→placement loop, and service (hours/participation) recorded back and reported.

Candidate confusions to resolve during research:

- **Religious Volunteer Management** (processed 2026-09-09) — its pass forwarded a flag: "the congregation-binding seam — generic volunteer management centers the volunteer program over a self-registering public (opportunities/applications/hours/waivers/recognition; the volunteer database is the platform's own), the religious Type centers serving ministry over the congregation's own people records with eligibility gating and engagement framing; VolunteerHub's 'Religious Organizations' solutions vertical proves the seam is structural, not customer-based — ratify from the generic side."
- **Ministry Scheduling** (processed 2026-09-08) — its pass noted for this leaf: "the same domain seam at nonprofit scale, plus market evidence that event-volunteer signup is a DIFFERENT product (MSP sells its 'Unison' signup tool separately from its ministry scheduler)."
- **Nonprofit CRM** (processed 2026-09-08) — its pass forwarded: "vs volunteer-management-system (supporter class + recorded hours vs scheduling/engagement machinery center)."
- **Volunteer Marketplace** (§25 sibling, unprocessed) — seeker-side discovery vs operator-side program system.
- **Employee Scheduling / HR** — paid labor vs unpaid service.
- **Corporate volunteering (CSR) platforms** — no separate directory leaf; expected to be an audience variant of this Type.

## Research Questions

1. What objects exist in the system: volunteer record, opportunity, shift/need, application, requirement/checklist, hour record, group, award, message, report?
2. What is the center: the volunteer (lifecycle), the opportunity (demand), or the hour (impact)?
3. How do volunteers enter the pool: self-registration from public directories vs application/approval vs staff-added?
4. What does qualification/screening look like, and is it definitional or variant?
5. How does placement work: staff assignment vs self-scheduling; shifts vs ongoing roles vs events?
6. How is service recorded (kiosk, self-posted, staff entry) and what is it reported against?
7. What volunteer-facing self-service exists (portal/app)?
8. What recognition/retention machinery exists, and how deep?
9. How do suite-module realizations (Salesforce Nonprofit Cloud) differ from standalone systems?
10. Where are the boundaries: religious binding, marketplace, paid scheduling, events, membership, corporate volunteering?

## Representative Products

| Product | Pole | Why chosen |
|---|---|---|
| **Volgistics** | established standalone system (25+ years); hospitals, zoos, museums, food banks | the operator-side classic; deepest Tier-1 help documentation (full help center fetched) |
| **VolunteerHub** | self-registration / opportunity-centric platform; broad verticals incl. religious, political, public service | the recruitment-and-self-signup pole; strong platform taxonomy + scheduling workflow detail |
| **Better Impact (Volunteer Impact)** | volunteer-lifecycle/engagement-centric; 85,000 organizations; volunteer centres + nonprofits | the lifecycle-articulated pole; explicit definition of the category; sibling solutions expose boundaries (Member Impact, Client Impact, Volunteer Link corporate, Get Connected volunteer centres) |
| **Salesforce Nonprofit Cloud — Volunteer Management** | enterprise CRM-suite module | the suite-module pole; shows volunteer data unified with fundraising/programs |
| **Rosterfy** | enterprise/large-scale volunteer workforce (major events, federations, government, emergency services) | the scale/compliance pole; 100+ volunteer organizations; reward/retain and insights depth |

Rejected/abandoned: none this pass; all five fetched successfully on first or second attempt.

## Sources

All fetched 2026-09-09.

- Volgistics root — https://www.volgistics.com/ (Tier 2)
- Volgistics features — https://www.volgistics.com/volunteer-management.htm (Tier 2)
- Volgistics Help — Checklist Overview — https://www.volgistics.com/help/checklist-items/checklist-overview/ (Tier 1; help-center navigation structure also observed)
- VolunteerHub root — https://www.volunteerhub.com/ (Tier 2)
- VolunteerHub Volunteer Scheduling — https://volunteerhub.com/platform/volunteer-scheduling (Tier 2 with operational FAQ)
- Better Impact root — https://www.betterimpact.com/ (Tier 2)
- Better Impact Volunteer Impact solution — https://www.betterimpact.com/solutions-volunteer-impact (Tier 2 with category FAQ)
- Salesforce Nonprofit Cloud Volunteer Management — https://www.salesforce.com/nonprofit/volunteer-management/ (Tier 2; salesforce.org URL redirected here)
- Rosterfy root — https://www.rosterfy.com/ (Tier 2)
- Prior-pass evidence adopted: research/religious-volunteer-management.md (VolunteerHub observations, boundary flags); research/ministry-scheduling.md (Unison signup-tool evidence); research/nonprofit-crm.md (forward note)

> Sourcing limitation: no vendor's full operational help center was read end-to-end (Volgistics help center sampled at the checklist section + navigation tree; VolunteerHub support portal not fetched). Precise numeric limits, pricing, and default settings are therefore not asserted anywhere. Claims are calibrated to product-page and sampled-help-article evidence.

## Product A — Volgistics (established standalone; operator-side classic)

### Key observations (evidence layer A)

- Positioning: "We set the standards in volunteer management software"; "Volgistics helps you manage your volunteers through the entire volunteer cycle. From the online application form to the calculation of awards." 25+ years serving volunteer leaders.
- Feature taxonomy (features page): Volunteer Profiles ("Manage and query detailed records of volunteer information"), Scheduling ("Organize and plan your volunteer opportunities"), Recruiting ("Use online application forms to bring on new volunteers"), Reporting ("Easily customize reports of volunteer hours and information"), Volunteer Portal (VicNet — "Engage volunteers with a mobile app where they can manage their information and schedule themselves"), Sign-In Kiosk (VicTouch — "Seamlessly track volunteer hours with a simple-to-use time clock"), Communication (email/text), Documents (VicDocs), Multi-Site Capabilities ("Oversee managers you assign to individual locations"), Checklists ("Establish volunteer requirements and monitor due dates and completions").
- Help-center structure (Tier 1 navigation) — the system's object model is directly visible: **Volunteer Records** (structure, archived vs non-archived, Sets = saved queries, Group Records), **Assignments (Sites & Places)** (the opportunity structure: assignments, sites, places, assignment roles, coordinators), **Schedule** (schedule openings, scheduling volunteers, schedule qualifications and rules), **Service** (methods of posting service, service tracking ground rules, service measure set up, merit hours), **Awards** (award ground rules), **Checklist Items**, **Application Forms** (applications received from a mailbox), **Opportunity Directory** (public-facing), **Coordinators** (assignment-level coordinators), **System Operators** (admin users with limitable rights), **Messaging** (email/text, scheduled reminders, message preferences, history), **VicNet** (volunteer portal), **VicTouch** (kiosk time clock), **VicDocs** (document storage), **Site Level Access** (multi-site), **Reports** (stock + custom + automatic).
- Checklist Overview (Tier 1 article): "The Volgistics Checklist features provide tools for keeping track of actions that new or current volunteers must complete. Examples… include: Attending orientation, Health screenings, Confidentiality agreements, Parental consent forms, Background checks, Reference checks, and more." Items can apply to all or certain volunteers, can repeat periodically ("like health screenings"), carry expiration dates, appear on the volunteer's History tab, and drive reports ("find volunteers due for a checklist item"). Background screening integrates with a vendor (Verified First).
- Verticals: health care, animal shelters, aquarium/zoo/museum, community outreach, cultural, parks & recreation, education, libraries, hospice, food banks.
- The volunteer record is archived, not deleted ("Archived Versus Non-Archived Records").

## Product B — VolunteerHub (self-registration / opportunity-centric)

### Key observations (evidence layer A)

- Positioning: "Helping Organizations Better *Recruit*, *Engage*, and *Manage* Volunteers"; 20+ years; "thousands of organizations… billions of volunteer hours."
- Feature taxonomy — three groups: **Volunteer Management** (Recruitment, Scheduling, Hour Tracking, Database, Fundraising, Liability Waivers, Rewards & Recognition, Reporting); **Opportunity Management** (Landing Pages, Check-In, Multi-Event Editor, Configurable Forms, Group Organization, Advanced Permissions, Mobile App); **Volunteer Communication** (Email, Text, Social).
- Self-registration is the engine: "branded event landing pages, email and text communications, volunteer self-registration from any device, and automated record management"; "Maintain a comprehensive database of your volunteers. Access contact information, skills, availability."
- Scheduling workflow (scheduling page, operational FAQ): volunteers browse opportunities in list/calendar/map view and self-signup for open shifts; capacity limits prevent over-booking; waitlists for full shifts; approval workflows can require approval before signup; volunteers can cancel/modify per org-defined rules; recurring shifts; automated confirmations and reminders (email + optional text); onboarding workflow auto-adds volunteers to groups like "Requires Orientation" or "Requires Background Check"; mobile app with day-of schedule and (when enabled) check-in/out.
- Hours: "coordinators can easily track activity and hours for each volunteer for each individual event"; customer testimonial: "being able to accurately track their hours for grant funding… is very important for us."
- Integrations: Salesforce, Blackbaud, Zapier, Sterling Volunteers + PeopleFacts (background checks), SSO.
- Verticals include Religious Organizations, Political Campaigns, Public Service, Athletics — the generic Type is sold across the whole volunteer economy.

## Product C — Better Impact / Volunteer Impact (lifecycle-articulated)

### Key observations (evidence layer A)

- Scale claims: 85,000 organizations; "500M+ volunteer hours tracked in Volunteer Impact."
- The vendor's own category definition (FAQ): "Volunteer management software is specialized technology that streamlines volunteer program administration and centralizes engagement information for nonprofits and other volunteer-reliant organizations. The best volunteer management solutions… include features that cover every stage of the volunteer lifecycle, from recruitment and training to ongoing communication and data management."
- Lifecycle sections (solution page): **Recruit** ("Post opportunities, collect applications online, and move applicants through screening and approval in one place"); **Database** ("Volunteers update their own profiles, you search by any criteria" — skills, interests, availability); **Onboarding & Training** ("Build eLearning courses with multimedia, assign quizzes, and share training materials through an online document library"); **Scheduling** ("Schedule one-time, recurring, or event-based shifts in one place, enable self-scheduling"); **Communications** (automated shift reminders by email/text; portal & app); **Reporting** ("Track hours, gather feedback, and generate reports… standard reports and customizable raw data reports").
- Volunteer portal & app: view assigned shifts / self-schedule, log hours and activities, access training, contact staff or fellow volunteers, share feedback.
- Multi-site: top-tier plan provides "standardized data reporting, comprehensive oversight, and location-specific administrative permissions for multi-site volunteer programs."
- Security posture: ISO/IEC 27001/27017, encryption, permissions, 2FA, SSO, HIPAA compliance "solving a common pain point for healthcare volunteer programs."
- **Sibling solutions expose the boundaries**: Member Impact (membership management) and Client Impact (volunteer↔client coordination) are separate products; Get Connected by Galaxy Digital (volunteer centres) and Volunteer Link (corporate volunteering) are separate solution lines. The vendor itself separates volunteer management from membership, from corporate CSR volunteering, and from volunteer-centre network operation.

## Product D — Salesforce Nonprofit Cloud, Volunteer Management (suite module)

### Key observations (evidence layer A)

- Positioning: "With volunteer management software built in Nonprofit Cloud, you can easily set up, manage, and track everything that matters to your volunteers and your organization." "Unify volunteer data with fundraising and program management."
- Capability blocks: **Activity Management** ("Improve the setup of volunteer activities, roles, shifts, locations"); **Capacity Planning and Attendance Tracking** ("Assign the number and type of volunteers needed for each activity… check volunteers in and out with start and end times"); **Applications Management** ("Manage and review applications to ensure the best fit"); **Reminders and Follow-up** (automatic reminders and follow-up journeys via Marketing Cloud).
- CRM leg: volunteer profile captures "name, contact info, and other demographics, even their relationship to other supporters or companies in your system"; **Volunteer Engagement and History** ("first and last volunteer activity, total hours volunteered"); **Availability, Locations, and Skills**.
- Self-service portal (Experience Cloud): volunteer opportunities matched to interests/skills, registration, training, share impact (Tableau dashboards).
- AI layer (Agentforce): volunteer support (change shifts, update contact info), volunteer matching suggestions, onboarding guidance.
- FAQ: "centralizing volunteer data and automating key tasks. Easily match volunteers to opportunities, track hours and engagement."
- The module completes with Marketing Cloud, Data 360, Experience Cloud, Slack, MuleSoft, Tableau — the suite posture: volunteer management as one domain of the nonprofit platform.

## Product E — Rosterfy (enterprise / large-scale workforce)

### Key observations (evidence layer A)

- Positioning: "Rosterfy is built for organisations managing 100 or more volunteers"; "Used by more than 5 million volunteers and staff worldwide"; "150M+ volunteer hours managed"; 77+ countries; ISO27001 + SOC 2.
- Platform blocks: **Recruit & Onboard** (recruitment listings, role-specific automated onboarding, ongoing compliance checks); **Train & Induct** (online training, LMS integrations, auto renewals); **Advanced Scheduling** (automated scheduling, attendance tracking, waitlists & emergencies, two-way volunteer messaging); **Reward & Retain** (e-badges, certificates, merchandise, ticket discounts, gift vouchers, inventory management); **Insights & Impact** (dashboards, DEI & ESG reports, surveys); **Volunteer App**; AI agent (Pip) for event/shift management.
- Solutions by industry: Nonprofits & Charities, Cities & Government, Major Events, Sporting Federations, Hospitals & Healthcare, Universities & Colleges, Emergency Services, Corporate Volunteering.
- **Volunteer Passports** use case: "A smarter way to connect volunteers and organisations" — a cross-organization volunteer credential (boundary-blurring with marketplace-type surfaces).
- Integrations: background checks (Sterling Volunteers, uCheck), payroll, fundraising, CRM (Salesforce, Blackbaud, Dynamics), training & compliance, e-signature.
- Case studies show program persistence across occasions: SXSW ("2000 active volunteers and growing" across festival editions), Golf Australia ("centralise volunteer management across national tournaments", "82.3% annual retention rates"), St John NSW ("transform staff and volunteer management" — paid staff and volunteers on one platform).

## Cross-product Comparison

| Structure | Volgistics | VolunteerHub | Better Impact | Salesforce NP Cloud | Rosterfy | Layer |
|---|---|---|---|---|---|---|
| Volunteers held as identified records in the program's own database (profile: contact, skills/interests, availability; self-maintained) | Volunteer Profiles; query; Sets; archived-not-deleted | Volunteer Database; self-registration "automated record management" | Centralized database; "volunteers update their own profiles" | CRM profile incl. relationship to other supporters | volunteer records; 5M+ users | **A — 5/5** |
| Volunteer opportunities as the demand structure (activities/roles/shifts/events with capacity) | Assignments (Sites & Places) + Schedule openings | Opportunities/events; capacity limits; multi-event editor | "Post opportunities"; one-time/recurring/event shifts | Activity Management: activities, roles, shifts, locations; capacity planning | Events & shifts; recruitment listings | **A — 5/5** |
| Intake into the pool (application/self-registration) | Application Forms (online, from mailbox) | self-registration + configurable forms | "collect applications online" | Applications Management | recruitment listings + automated onboarding | **A — 5/5** |
| Readiness/qualification before placement (screening, orientation, training, requirements with expiry) | Checklist Items (orientation, health screenings, background/reference checks; periodic; expiration) | onboarding groups "Requires Orientation"/"Requires Background Check"; approval workflows; waivers | screening & approval; eLearning + quizzes; document library | training in portal; applications review | ongoing compliance checks; online training + auto renewals | **A — 5/5 (depth varies; realization varies)** |
| Placement into opportunities (staff assignment and/or self-scheduling) | Scheduling volunteers into openings; VicNet self-scheduling | self-signup for open shifts; approval-gated | self-scheduling portal/app; staff scheduling | registration via portal; staff review | automated scheduling + volunteer app | **A — 5/5** |
| Service recorded back (hours/attendance against volunteer × opportunity) | Service tracking (methods of posting service; service measures; merit hours); VicTouch kiosk | Hour Tracking per volunteer per event; check-in | "log hours and activities"; 500M+ hours | attendance check-in/out with start/end times; total hours | attendance tracking; 150M+ hours | **A — 5/5** |
| Program-level reporting (hours, impact, funders/board) | stock + custom + automatic reports | Reporting; grant-funding hours | one-click impact reports; raw data reports | engagement history; Tableau impact sharing | dashboards; DEI & ESG reports; surveys | **A — 5/5** |
| Volunteer self-service portal/app | VicNet portal + mobile | Mobile App; self-schedule; cancel/modify | portal & app (shifts, hours, training, feedback) | Experience Cloud portal | Volunteer App | **A — 5/5** |
| Communication (email/text reminders + outreach) | Messaging (email/text, scheduled reminders, preferences) | automated emails/texts; social | automated reminders email/text | reminders + Marketing Cloud journeys | two-way messaging | **A — 5/5** |
| Recognition/rewards | Awards (calculation of awards; merit hours) | Rewards & Recognition | thin on fetched pages | not on fetched page | Reward & Retain (e-badges, certificates, inventory) | **B — 3/5 strong, 2/5 unobserved** |
| Public-facing opportunity directory / landing pages | Opportunity Directory | Landing Pages + embeds | "post opportunities to your website" | portal opportunities | recruitment listings; Volunteer Passports | **A — 5/5 (publicness varies)** |
| Groups (volunteer as group/family) | Group Records; Group Tracking | Group Organization | not on fetched pages | relationship to companies (corporate) | not on fetched page | **B — 3/5** |
| Multi-site / multi-location | Multi-Site + Site Level Access | Advanced Permissions | location-specific admin permissions (Impact Plan) | locations on activities | enterprise multi-program | **A — 5/5** |
| Check-in machinery (kiosk/app) | VicTouch kiosk | Check-In + app check-in/out | not on fetched pages | check in/out with times | attendance tracking | **B — 4/5** |
| Background checks | via screening vendor (Verified First) + checklist items | Sterling/PeopleFacts integrations | screening & approval (mechanism not detailed) | not on fetched page | Sterling/uCheck integrations | **B — integration-dominant, realization varies** |
| AI assistance | not observed | not observed | not observed | Agentforce (support, matching, onboarding) | Pip agent | **C — era-current, 2/5** |
| Fundraising linkage | not observed | Volunteer Fundraising | not observed | unify with fundraising | fundraising integrations | **B — 3/5, suite/module posture** |

## Canonical Model — Four Abstraction Levels

### L0 — Defining Invariant

Four jointly-held structures; the Type lives in their combination:

1. **The volunteer population of record** — identified people held as the program's own records (self-registered or staff-added), each carrying profile state relevant to placement — contact, skills/interests, availability — and accumulating service history. The database is the volunteer program's own; it is not borrowed from a membership roster or a congregation roll (that binding is the religious sibling's mark). Remove → a contact/CRM database.
2. **Volunteer opportunities as the demand structure** — the organization's work that needs volunteer service, held as records volunteers can be placed into: activities, roles, shifts, events, with capacity. Remove → a people database with no demand side.
3. **The intake→placement loop** — people enter the pool (apply or self-register), are brought to readiness (screening, approval, orientation, training, requirements — depth and mechanism vary), and are placed into opportunities (staff assignment or self-scheduling). Remove → a directory nobody flows through; remove readiness → an open signup board.
4. **Service recorded back and reported** — participation (hours the dominant realization) is recorded against the volunteer and the opportunity — via kiosk/app check-in, self-posting, or staff entry — and aggregated into program-level reporting for leadership, funders, and recognition. Remove → a signup tool with no memory; the "management" dies.

Jointly-held is load-bearing: (1) alone = contact database; (2) alone = opportunity listings/job board; (3) without (1)+(2) = generic recruiting pipeline; (4) without (1)–(3) = a timesheet; (1)+(2) without (3) = directory with no flow; (1)+(3) without (2) = recruiting pipeline with nothing to fill; (2)+(3) without (1) = anonymous signup board; (1)+(2)+(3) without (4) = placement with no memory (the signup-tool pole); (1)+(4) without (2)+(3) = hour log with no program.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Shift/event scheduling machinery: recurring shifts, capacity limits, waitlists, approval workflows, reminders (shared with Employee Scheduling and Ministry Scheduling as machinery)
- Volunteer self-service portal/app: browse opportunities, self-schedule, manage registrations, log hours, view schedule, training, feedback
- Communication: automated confirmations/reminders by email and text; targeted outreach by criteria
- Check-in/check-out (kiosk or app) feeding attendance and hours
- Requirement/checklist tracking with expiration and renewal (orientation, screenings, background checks, consent forms)
- Multi-site/multi-location operation with scoped coordinator permissions
- Recognition/awards (hour-threshold awards, e-badges, certificates)
- Program reporting: hours by volunteer/opportunity/site/period; impact reports for boards and funders
- Document storage (waivers, agreements, credentials)
- Group volunteering (corporate groups, families, clubs) tracked as groups with individual members captured
- Integrations: background-check vendors, CRM/donor systems, LMS, e-signature

### L2 — Variant / Optional Structure

- Program shape: ongoing placement (hospital, museum docent) vs event-driven (festivals, food banks, political campaigns) vs shift-rostered (emergency services) — most products span all three
- Operator type: nonprofit/charity, hospital/healthcare, museum/zoo/aquarium, city/municipal, university, sports federation, church/religious organization (as customer), corporate CSR program (employees as the volunteer population; ESG/DEI reporting)
- Publicness: public opportunity directory/landing pages vs private program (invite/application only)
- Screening depth: formal background-check integration vs checklist items vs waivers only
- Scale posture: single-site small org → multi-site → mega-event workforce (10k+ volunteers)
- Packaging: standalone system vs CRM-suite module (Salesforce posture) vs volunteer-centre network platform (Get Connected pole)
- Hours verification posture: honor-system self-posting vs kiosk-verified vs staff-approved
- Fundraising linkage (volunteer→donor conversion) — present in some products, absent in others
- AI assistance (matching, support agents, onboarding) — era-current
- Cross-organization volunteer credentials (volunteer passports) — emerging, blurs toward marketplace territory

### L3 — Vendor-specific (kept out of the final document)

- Volgistics: VicNet (portal), VicTouch (kiosk), VicDocs (documents), Assignments/Sites/Places terminology, Sets (saved queries), merit hours, Verified First screening integration, dormant accounts
- VolunteerHub: landing pages + embeds, multi-event editor, "Requires Orientation" auto-groups, BetterGood ownership, 66%-more-likely-to-donate claim
- Better Impact: Volunteer Impact / Member Impact / Client Impact / Get Connected / Volunteer Link product names, Impact Plan tier, 85,000 orgs & 500M hours claims, HIPAA compliance emphasis
- Salesforce: Nonprofit Cloud, Experience Cloud portal, Agentforce agents, Marketing Cloud journeys, Tableau impact dashboards, Power of Us licensing
- Rosterfy: Pip AI agent, Volunteer Passports, e-badges/merchandise inventory, DEI & ESG reports, 100+ volunteer threshold, SXSW/Golf Australia/World Scouting case studies

## Vendor-specific Findings

See L3. Two structural market observations:

1. **The category definition is vendor-articulated and lifecycle-shaped.** Better Impact's FAQ defines volunteer management software as covering "every stage of the volunteer lifecycle, from recruitment and training to ongoing communication and data management"; Volgistics frames "the entire volunteer cycle. From the online application form to the calculation of awards"; Rosterfy's platform blocks are Recruit→Train→Schedule→Reward→Insights. The lifecycle loop is the market's own mental model of the Type.
2. **The suite-module and standalone poles coexist.** Salesforce ships volunteer management as a Nonprofit Cloud module unified with fundraising ("relationship to other supporters"); standalone systems (Volgistics, VolunteerHub, Better Impact, Rosterfy) integrate *toward* CRMs instead. Both realize the same four-part core.

## Rejected Findings

- "Hours tracking is the definitional center" — REJECTED as stated. All 5 products track hours, but the invariant is *service recorded back onto the volunteer and opportunity*; hours are its dominant realization (attendance/participation the general form; merit-hour schemes and hour-threshold awards are realizations). A program that records participation without hour quantification still fits.
- "Background checks are definitional" — REJECTED. The invariant is readiness before placement; background checks are one realization (integration-dominant across the sample: Verified First, Sterling, uCheck, PeopleFacts). Waivers, orientation, and training are alternative realizations.
- "Self-service portals are definitional" — REJECTED. All 5 modern products have them, but the paper-era volunteer office (card file, phone scheduling, paper hour sheets) satisfies the core without any portal. The portal is the modern realization of intake/placement/recording.
- "Public opportunity directories are definitional" — REJECTED. Volgistics ships the Opportunity Directory as a feature; private programs (hospital volunteer departments, corporate employee programs) run without public posting. Publicness is an operator posture.
- "This Type is nonprofit-only" — REJECTED. The sample spans hospitals, zoos, museums, cities, universities, sports federations, emergency services, and corporate CSR programs. "Volunteer-reliant organization" (Better Impact's phrase) is the accurate scope.
- "Corporate volunteering is a different Type" — REJECTED for now (no separate directory leaf). Better Impact (Volunteer Link) and Rosterfy (Corporate Volunteering solution) sell it as a separate *solution line* but on the same platform machinery; the volunteer population is employees and reporting is CSR/ESG-shaped. Held as an audience variant; recorded for the taxonomy pass if a corporate-volunteering leaf is ever proposed.
- "Volunteer management = volunteer scheduling" — REJECTED. Scheduling is one capability of the loop; every sampled vendor frames scheduling as one block inside a larger lifecycle (VolunteerHub: "Volunteer scheduling is just one part of a complete volunteer management software").

## Boundary Findings

1. **vs Religious Volunteer Management (§25, processed)** — the congregation-binding seam, RATIFIED from this side; DISCHARGES that pass's forward flag. The generic Type holds the volunteer population in the program's own database, built from self-registration and applications from the general public; the religious Type holds volunteers as the congregation's own people records (members), with eligibility gating and discipleship/engagement framing. VolunteerHub's "Religious Organizations" vertical proves the seam is structural, not customer-based: a church can run the generic structure (self-registering volunteers, opportunities, hours, waivers) or the religious structure (serving ministry over member records) — the structures differ, not the customer. Seam test: replace the self-registering public with the congregation's member records and add eligibility-gated placement → the religious Type; strip the congregational binding → this Type.
2. **vs Ministry Scheduling (§25, processed)** — the scheduling act is shared machinery. Ministry Scheduling is the serving-schedule system of record (positions × dated occasions × assignments + response loop); here the schedule is one capability of the program loop and the volunteer's program state is the record of record. The ministry-scheduling pass's evidence that event-volunteer signup is sold as a separate product (MSP "Unison") corroborates that signup/placement and schedule-keeping are distinct centers.
3. **vs Volunteer Marketplace (§25, unprocessed) — FORWARD FLAG for that pass.** The operator-side program system (this Type) vs the seeker-side discovery/matching venue (marketplace). The shared surface is the public opportunity directory (Volgistics Opportunity Directory, VolunteerHub landing pages/embeds, Better Impact "post opportunities to your website") — but here it is a recruitment channel of one organization's program, not a multi-organization venue where volunteers search across opportunities. Rosterfy's Volunteer Passports (cross-organization volunteer credentials) is the clearest blur point. Joint review recommended at that pass.
4. **vs Nonprofit CRM (§25, processed)** — DISCHARGES that pass's forward note from this side. The nonprofit CRM centers the constituent relationship (volunteering one act class on the supporter record); this Type centers the volunteer program loop (intake→placement→service→report). The Salesforce posture shows the fusion point: in the suite module, the volunteer profile carries "relationship to other supporters" and volunteer data unifies with fundraising — the CRM-module realization of the same program core. Keep-both; center-of-gravity seam.
5. **vs Nonprofit Management Platform (§25, processed)** — umbrella suite vs single-domain system. That pass recorded volunteers as one companion domain of the umbrella; this leaf is the domain itself, documented from its own center. Products bundle (Salesforce) or integrate (VolunteerHub→Salesforce/Blackbaud).
6. **vs Employee Scheduling (§09) / HR** — volunteers are unpaid; no wages, shifts-for-pay, or labor-compliance machinery is definitional here. Rosterfy's payroll integrations and St John NSW "staff and volunteer management" show paid staff riding the same platform at the enterprise pole — an edge, not the center. The application/screening machinery resembles recruiting, but the outcome is unpaid service placement, not employment.
7. **vs Event Management Platform / Nonprofit Event Management (§26/§25)** — the event is not the record of record here; the volunteer program persists across occasions (SXSW "2000 active volunteers and growing" across editions; Golf Australia across national tournaments). Event-volunteer signup appears as one occasion type.
8. **vs Membership Management (§25)** — Better Impact sells Member Impact as a separate product from Volunteer Impact — vendor-side evidence that member lifecycle and volunteer program are distinct centers even inside one vendor.
9. **vs Corporate Volunteering (no leaf)** — held as an audience variant (employees as volunteers, CSR/ESG reporting); see Rejected Findings.
10. **vs Sports Club Management (§28, processed)** — that Type centers the member organization (members, teams, seasons, dues); volunteers appear as club workers. Here the volunteer program itself is the center.

## Uncertainties

- Help-center depth: only Volgistics' checklist section + navigation tree was read at Tier 1; VolunteerHub's support portal, Better Impact's help files, Salesforce help docs, and Rosterfy's helpdesk were not fetched. Workflow claims are calibrated to product-page + sampled-help-article evidence; no numeric limits, pricing, or default settings are asserted.
- Better Impact recognition/rewards depth was not observed on fetched pages (the vendor's blog covers appreciation topics, suggesting capability, but this pass does not assert it).
- Salesforce background-check machinery was not observed on fetched pages — the qualification leg rests on the other four products plus Salesforce's applications/training blocks.
- The historical check is conceptual (paper-era volunteer office), not source-verified.
- Corporate volunteering as variant vs separate Type: held as variant on the absence of a directory leaf; if the taxonomy later adds a corporate-volunteering leaf, the seam should be re-drawn (employee population + CSR reporting as the discriminators).
- Volunteer Marketplace leaf unprocessed — the marketplace boundary is a forward flag, not a ratified seam.

## Historical / Market-Sample Check

Paper-era volunteer office: a card file of volunteers (names, contact, skills, availability), an opportunity binder or wall chart of needs, phone-and-paper scheduling, hour sheets signed at the desk and tallied monthly, an annual recognition dinner, and service reports typed for funders. This satisfies all four L0 legs with zero modern machinery: volunteer population of record (card file), opportunities (binder), intake→placement (application interview → phone placement), service recorded back (hour sheets → reports). Regional and platform-native realizations (UK volunteer centres brokering placements, hospital auxiliaries, museum docent corps, emergency-service volunteer brigades with paper rosters) fit without any of the modern extras. The definition therefore does not depend on portals, kiosks, background-check integrations, cloud delivery, or AI.

## Final Synthesis

A Volunteer Management System is the volunteer-reliant organization's program system of record. Its defining core is the four-part structure: a volunteer population held as the program's own records (self-registered or staff-added people carrying profile state and service history) + volunteer opportunities as the demand structure (activities, roles, shifts, events with capacity) + the intake→placement loop (people apply or self-register, are brought to readiness, and are placed — by staff or by self-scheduling) + service recorded back against volunteer and opportunity and aggregated into program reporting. Everything else the market ships — portals and apps, kiosk check-in, requirement expiry tracking, multi-site scoping, recognition and awards, group volunteering, background-check integrations, fundraising linkage, AI matching — is standard mature capability or variant, not definition. The market realizes the Type as standalone systems (Volgistics, VolunteerHub, Better Impact, Rosterfy) and as CRM-suite modules (Salesforce Nonprofit Cloud); the lifecycle loop (recruit → qualify → place → serve → record → report → recognize/retain) is the market's own articulation of the Type. The sharpest seams: the religious sibling binds the volunteer population to the congregation's own people records; the marketplace sibling (unprocessed) owns the seeker-side discovery venue; employee scheduling owns paid labor; event management owns the occasion rather than the program.
