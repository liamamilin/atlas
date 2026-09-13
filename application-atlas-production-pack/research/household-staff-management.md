# Research Notes — Household Staff Management

Research date: 2026-09-08

## Research Goal

Understand what "Household Staff Management" software actually is as a class: who operates it (the household itself? a staffed estate? a service provider?), what objects exist inside it (staff members, employment records, schedules, tasks, time, pay, documents), what workflows the household runs around its employed staff, how compliance obligations shape the software, and where the boundaries lie against neighboring Types (home management, family organizer, childcare management, care marketplaces, staffing agencies, payroll systems, HRIS).

## Initial Boundary

Directory location: §29 Home, Family, Personal & Local Services (siblings include Home Management Application, Family Organizer, Household Chore Application, Childcare Management System, Babysitting Marketplace, Family Care Coordination, Personal Concierge Platform).

Working hypothesis: employer-side (household-side) software for managing domestic employees — nannies, housekeepers, house/estate managers, personal assistants, chefs, drivers, gardeners, caregivers. Expected core: staff records + scheduling/duties + employment administration (time, pay, compliance) + household–staff communication. Anticipated confusions recorded up front:

- Home Management Application / Family Organizer / Household Chore Application (family members doing household work — no employment relationship)
- Childcare Management System (operator runs a licensed care business for many families — already documented as a boundary: "a family employing a nanny manages an employee; a care operator manages a licensed business")
- Babysitting Marketplace / Home Services Marketplace (matching venues; sampled marketplace products explicitly disclaim the employer role)
- Staffing Agency Management System (agency places staff; household manages them afterward)
- Payroll System / HRIS / Time & Attendance (§08/§09 — business employers, business compliance regimes)
- Estate/property management platforms (assets, vendors, projects as center; staff as one record among many)
- Family Care Coordination (organizing care for dependents vs employing staff)
- Personal Concierge Platform (delivering services vs administering employment)

## Research Questions

1. Who is the operating user: the principal/family, an estate/household manager acting for them, or a family office?
2. What is the central object — a staff/employee record? What does it carry (role, status, documents, property assignment)?
3. What parts of the employment lifecycle does the software run: hiring/onboarding, duties/scheduling, time & leave, pay, taxes/filings, offboarding/records?
4. How do duty assignment and household operating standards work (tasks, lists, house manuals/protocols, reporting structure)?
5. How is pay handled — in-product payroll, or handoff to a payroll/tax service? What is the "household employer" compliance regime (US vs UK)?
6. How do household and staff communicate/access the system (permissions, employee self-service, members areas)?
7. Where are the boundaries: vs family/household task apps (no employment), vs care businesses (many families), vs marketplaces (no employer role), vs business payroll/HR (different regime)?
8. Historical check: would paper-era household staff practice (household books, duty rosters, wage records, house manuals, employment agreements) satisfy the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, different customer tiers, and two countries:

1. **NINES** (US, ninesliving.com) — household/estate management platform for HNW households, family offices, estate managers; the household-operations pole: staff managed inside the household's operating system, payroll not in evidence.
2. **HomeWork Solutions** (US, homeworksolutions.com) — specialist household payroll & compliance service since 1993; tiered service (self-service → white-glove); the full-service employment-administration pole.
3. **Poppins Payroll** (US, poppinspayroll.com) — self-serve, app-first household payroll for everyday employers (one nanny/housekeeper); flat monthly price.
4. **SurePayroll by Paychex** (US, surepayroll.com) — large payroll brand with "Household Employers" as a named solutions segment; automation-first.
5. **Nannytax** (UK, nannytax.co.uk) — longest-running UK nanny PAYE service (32 years, 70k+ families); regional variant with UK regime (PAYE, workplace pensions, employer's liability insurance) plus HR support and a nanny-facing members area.

**EstateSpace** (US, estatespace.com) was examined as a sixth candidate and retained only as a boundary data point: its current positioning is physical-asset management (properties, art, vehicles, vendors, projects); staff appear as role-based users, not as the managed subject. It is treated as adjacent (estate-asset platform), not a representative.

Rejected/unreachable candidates (see Sources): GTM (gtm.com, HTTP 403 ×2), Breedlove (403), Care.com HomePay (care.com historically 403; gethomepay.com is an unrelated Italian real-estate payments product).

## Sources

Observed directly (2026-09-08):

- NINES — homepage (ninesliving.com); "Manage your household staff with Nines" (ninesliving.com/manage-household-employees-with-nines/); "Are you setting your household employees up for success?" (ninesliving.com/onboarding-household-staff/)
- HomeWork Solutions — homepage (homeworksolutions.com); "Hiring Other Household Staff" (homeworksolutions.com/hiring-other-household-staff/)
- Poppins Payroll — homepage (poppinspayroll.com)
- SurePayroll — "Nanny Payroll Service" (surepayroll.com/household-payroll); "Household Solutions" (surepayroll.com/solutions/household)
- Nannytax — homepage (nannytax.co.uk)
- EstateSpace — homepage (estatespace.com) [boundary case only]

Failed / limited sources:

- gtm.com — HTTP 403 on / and /household-payroll/ (abandoned after 2 attempts). GTM is a known household payroll + HR provider; its absence weakens nothing structural but removes one HR-heavy sample.
- breedlove.com — HTTP 403 (1 attempt, abandoned)
- care.com family (HomePay) — not attempted directly (domain family returned 403 in earlier sibling research passes); gethomepay.com discovered to be an unrelated Italian proptech fintech — name-collision trap noted
- No dedicated help-center/member-area docs were fetchable for any sample (all behind login or JS apps); product/blog/pricing pages are the evidence base. NINES observations are product-page and vendor-blog level, not help-center level.

## Product Observations

Evidence layer per observation: **A** = directly observed on an official source of that product; **B** = cross-product commonality across the observed sample.

### Product 1 — NINES (household-operations pole)

Key observations (Layer A unless noted):

- Positioning: "centralized household manual and operating system for managing properties, assets, vendors, staff, tasks, and more"; users are households, family offices, estate managers, house managers, personal assistants, nannies, housekeepers, private chefs, property managers; also yacht crews and boutique hospitality.
- **Household Employees as a first-class object**: adding an employee = photo, name, job title, contact information, status (full-time / part-time / contractor), assigned property; free-text role overview, full job description, live-in/live-out note, and "the household staffing agency who helped you find them"; built-in fields for birthday, emergency contact, start date, preferences, family members' names.
- **Interaction log on the employee record**: "log any interactions with this employee, like time off requests, HR updates, etc."; promotion example (housekeeper → executive housekeeper) recorded on the profile.
- **Connections**: documents (employment contract, NDA, resume, job descriptions) uploaded to a documents area and connected to staff profiles; documents and calendar events filterable by staff member.
- **Standards & procedures**: household manual/protocols organized in chapters (from household-management expert content), including a Staff chapter; employees @-mentioned to express reporting structure ("a lady's maid reports to our head housekeeper") and link to full profiles.
- **Duty machinery**: tasks and lists assigned to specific employees (single tasks or full weekly task lists — e.g., a laundress's ironing/errands list); assignee notified; completion visible in real time; tasks dashboard filterable by employee.
- **Permissions**: layered settings controlling what each user can see/add/edit/delete — principal and estate manager full access; a baby nurse sees only tasks assigned to her; a caregiver sees only the "Childcare" category; a property manager sees only their property's information.
- **Onboarding discipline** (vendor blog): onboarding vs orientation; handled by estate manager/chief of staff/HR/principals; check-ins at days 1/7/14/30/60/90; track onboarding progress with reminders and milestone notes.
- Payroll/tax machinery: **not observed anywhere** in the fetched material.
- Multi-household accounts for fractional estate managers / multi-family offices (self-serve account switching).

### Product 2 — HomeWork Solutions (full-service employment administration)

Key observations (Layer A):

- Positioning: "Expert household payroll and compliance for families who employ nannies, senior caregivers, and household staff"; since 1993; all 50 states; "household payroll and nanny tax service".
- Segment pages: nannies/au pairs; senior caregivers; **"Other Household Staff"** — "Housekeepers, household managers, personal assistants, and other domestic workers carry the same employer obligations as nannies"; role definitions given (household managers "manage day-to-day household operations, scheduling, and vendor coordination").
- **Household-employer definition articulated**: "If you control the work, set the schedule, and pay the wages, the person is almost certainly a household employee under IRS rules, regardless of what you call them or how you've been paying them"; compliance applies full-time, part-time, or a few hours a week; paying cash "does not change your legal classification."
- **Worker classification guidance**: W-2 employee vs 1099 contractor test (behavioral control, financial control, relationship type); "most common situation we help families correct" is a worker misclassified as 1099.
- Obligations handled on the employer's behalf: FICA (with the employer-paid-both-halves nuance), FUTA, SUTA (state rates/tracking), year-end W-2 + Schedule H, **new-hire reporting**, workers' compensation (connection to coverage).
- **Time & leave inside the employment loop**: online and mobile-app time entry and approvals (Guided tier); PTO & sick balance tracking (Complete tier).
- Service tiers as support gradient: Guided ($59/mo, DIY + tools, provider pays employees and files), Complete ($95/mo, + specialist support, multi-state, compliance monitoring), Premier ($155/mo, + dedicated specialist, **HR consultations**, ad-hoc payrolls, 2 annual background checks). Each additional employee is a flat monthly add-on.
- Retroactive correction: "We can go backwards if you've been paying without payroll — reconstruct records, file what needs to be filed."
- Partners channel: nanny agencies, senior-care companies, CPAs, white-label/embedded services.
- Content/resources arm: household-employment compliance knowledge center (EN/ES), compliance checklist.

### Product 3 — Poppins Payroll (self-serve employment administration)

Key observations (Layer A):

- Positioning: "The easiest way to pay your household employee"; household payroll + tax filings; flat monthly subscription (price stated on page); "100% focused on household payroll"; available in all 50 US states.
- Segments: childcare (nannies, babysitters, tutors); senior care (caregivers, companions, aides); household employees ("housekeepers, gardeners, assistants, and anyone else who keeps your home running smoothly").
- **Employer registration as onboarding**: registers the employer with the IRS, sets up federal/state employer tax accounts, files new-hire paperwork with the state.
- **Payroll loop**: employer picks pay schedule (weekly/biweekly/semimonthly/monthly, constrained by state rules); gross-to-net calculations, withholdings, tax liabilities; direct deposit through the product, or self-pay by check/Venmo/Zelle; payroll processed in arrears.
- **Leave tracking**: custom PTO and sick-leave policies; balances tracked and shown on paystubs.
- **Filings & records**: quarterly federal/state/local filings, W-2/W-3/Schedule H, deadline tracking; paystubs, tax forms, payroll records accessible anytime; records kept "for at least five years" (product-stated).
- Adjacent coverage via partners: workers' compensation and health benefits through named partners; dependent-care FSA usage mentioned in customer reviews; catch-up service for prior wages paid before setup.
- Employee-facing support: dedicated "For employees" site section (nav-level evidence); support "for both you and your employee".
- Explicit boundary statement: "We specialize in household payroll only — it's a different world from business payroll" (refers business payroll to a partner).

### Product 4 — SurePayroll by Paychex (automated employment administration)

Key observations (Layer A):

- "Household" is a **named solutions segment** alongside small business ("The fast way to pay employees who work in your home"); dedicated industry page for nanny; heritage brand NannyChex referenced in resources nav.
- Positioning: "Purpose-built for household employers"; nanny/caregiver payroll with automatic tax filing/deposit; monthly flat price including one employee.
- Segment coverage: "Payroll for every household employer" — nannies & childcare; in-home caregivers & health aides; **housekeepers & gardeners**.
- Feature set: state tax ID registration assistance; payroll from the phone; scheduled/auto payroll; unlimited runs; 2-day direct deposit; signature-ready Schedule H; W-2 generation; reports & paystubs online 24/7; supports W-2 employees and 1099 contractors; onboarding assistance.
- **Household-employer obligations framing**: withhold/file federal and state payroll taxes including Schedule H at year end; missed deadlines → back taxes, penalties, IRS exposure; EIN required for household employers; "can't pay under the table" (employee loses unemployment-insurance access).
- **Classification test in FAQ**: setting the schedule, providing tools, directing the work → employee (W-2), not 1099.
- **Employee self-service**: the employee gets 24/7 access to their own paystubs and account details, "so you're not the go-between."
- Records guidance in FAQ: keep wages, hours, tax forms, filings, contracts, and agency communications — framed as audit protection.
- Extended family of products attachable: workers' comp, 401(k), health insurance, employment law.

### Product 5 — Nannytax (UK regional variant)

Key observations (Layer A):

- Positioning: award-winning nanny payroll service; "the longest running Nanny PAYE company in the UK" (32 years, 70,000+ families stated).
- **UK regime machinery**: PAYE scheme setup, payslips, tax/NI declaration to HMRC, managed workplace pension service (calculations, deductions, payslip updates), employer's liability insurance (top tier), optional service where the provider pays HMRC and the nanny on the employer's behalf.
- **Employment administration beyond payroll**: free bespoke nanny employment contract; "unlimited HR support"; employment-law content (contracts, benefits in kind, redundancy, statutory holiday/sick/maternity/parental pay); employer's checklist; employment pack.
- **Members areas on both sides**: Employer Members Area and **Nanny Members Area** (employee self-service, with satisfaction stat stated); nanny-facing rewards & wellbeing app (GP access, discounts) as retention machinery.
- Subscription tiers by support depth (annual pricing; three named tiers; add-on monthly payment service).
- Resources answering the same structural questions as US samples: employer responsibilities ("setting up a PAYE scheme, running payslips, declaring tax, providing a workplace pension"), gross-vs-net, holiday calculator, DBS checks and Ofsted registration guidance.
- Sibling brands: **Stafftax** (payroll for household staff beyond nannies), Nannyinsure, Carer Insure — the group covers domestic employment generally.
- Agency channel: separate agency service/portal (placement side is a partner channel, not the employer side).

### Boundary case — EstateSpace (not a representative)

- Current positioning: "physical asset management" for private estates — properties, art, vehicles, vessels, aircraft, vendors, projects, budgets; AI onboarding of inventories. Staff appear as role-based users with scoped access ("advisors, staff, and vendors get role-based access"), not as a managed roster of employments. Confirms that estate/asset platforms are a neighboring shape, not this Type's center.

## Cross-product Comparison

| Dimension | NINES | HomeWork Solutions | Poppins | SurePayroll | Nannytax (UK) |
|---|---|---|---|---|---|
| Operating user | estate manager / house manager / principal; family office (A) | family employer; specialist team executes (A) | family employer self-serve (A) | family employer self-serve (A) | family employer; provider executes (A) |
| Staff as employment records | employee profiles: role, status FT/PT/contractor, property, documents, start date, emergency contact (A) | employees on account; W-2 records; classification test (A) | employee info added at onboarding; paystub/tax records ≥5 yrs (product-stated) (A) | employee info; employee self-service accounts (A) | nanny record; employer + nanny members areas (A) |
| Onboarding / new-hire | onboarding tracking, check-ins, milestone notes (A) | new-hire reporting, tax account setup, retroactive cleanup (A) | IRS/state registration + new-hire paperwork (A) | state tax ID assistance, onboarding assistance (A) | PAYE scheme setup, contract, sign-up lead time (A) |
| Duties / tasks / standards | tasks, lists, protocols/house manual, reporting structure, @ mentions (A) | not in product (scheduling framed as employer's control test) (A) | not observed (A-absent) | not observed (A-absent) | not observed (A-absent) |
| Time & leave | time-off requests logged on profile (A) | time entry + approvals; PTO/sick balances (A) | PTO/sick policies + balances on paystubs (A) | hours kept in records guidance; pay runs scheduled (A) | statutory holiday/sick/maternity content; holiday calculator (A) |
| Pay | not observed (A-absent) | gross-to-net, direct deposit, filings (A) | gross-to-net, deposit or self-pay, arrears (A) | auto payroll, deposit, unlimited runs (A) | payslips; optional provider-pays-nanny (A) |
| Tax / filings | not observed (A-absent) | FICA/FUTA/SUTA, W-2, Schedule H (A) | quarterly filings, W-2/W-3, Schedule H (A) | federal/state taxes filed & deposited, Schedule H (A) | PAYE/NI to HMRC, pensions (A) |
| Classification / employer definition | employment-status field FT/PT/contractor (A) | control test; W-2 vs 1099 correction (A) | household-only positioning (A) | control test FAQ; W-2 vs 1099 (A) | self-employment guidance; employer responsibilities (A) |
| Contracts / HR documents | job descriptions, NDAs, contracts connected to profiles (A) | HR consultations (Premier) (A) | sample nanny agreement resource (A) | records-keeping guidance incl. contracts (A) | bespoke contract + unlimited HR support (A) |
| Insurance | not observed (A-absent) | workers' comp connection (A) | workers' comp via partner (A) | workers' comp product family (A) | employer's liability insurance (tier) (A) |
| Background checks | not observed (A-absent) | 2 annual checks (Premier) (A) | not observed (A-absent) | not observed (A-absent) | DBS guidance (content) (A) |
| Employee self-service | staff log in with scoped permissions (A) | — | "For employees" section (nav) (A) | 24/7 paystubs/account for employee (A) | Nanny Members Area + rewards app (A) |
| Multi-property / multi-employer | multi-property assignment; multi-household accounts (A) | multi-state payroll support (A) | single-household focus (A) | one employee base plan (A) | nanny-share guidance (content) (A) |
| Placement involvement | agency recorded as provenance on profile (A) | agencies as partner channel (A) | — | — | agency service/portal (A) |
| Payroll absent? | **yes — operations pole** | no | no | no | no |

Stable commonalities (Layer B, cross-product):

- The staff member is held as an individually identified person/employment record in the household's own system (5/5).
- The software exists to run the employment relationship over time — bringing the person on (registration, contract, new-hire steps), recording time/leave (5/5 in some form), paying and/or reporting on the employment (4/5; NINES is the exception on pay, not on administration), and keeping the record (documents, paystub/tax history, access) (5/5).
- "Household employer" is a named, product-articulated category with its own compliance regime distinct from business employment (5/5; Poppins and HWS state the separation explicitly).
- A control/classification test (who sets schedule, directs work, provides tools) is articulated in product content (US samples A; UK equivalent self-employment guidance A).
- The employer side is the family/principal (possibly via an estate manager); placement (agencies/marketplaces) is upstream and appears as a partner or provenance note, never as the system's own loop (5/5).
- The employee has some direct relationship with the system in mature products — scoped login/permissions, self-service paystubs, or a member area (4/5; strongest at SurePayroll/Nannytax/NINES).

Key divergences: the two structural poles (operations-first platform without payroll vs employment-administration service with payroll at the center); service-vs-software weight; regime (US federal/state vs UK PAYE/pensions); segment breadth (nanny-only vs all domestic roles); employee-facing depth.

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Minimal structure without which the product stops being recognizable as Household Staff Management:

1. **The household's staff roster of record** — the people employed to work in the home(s) are held as individually identified employment records in the household's own system: who they are, their role/job title, employment status, and (in most realizations) the property/place they serve and their start date. Remove → the software is about houses or tasks, not staff (home management / chore apps).
2. **The employment administration loop** — the household runs each employment through its lifecycle in the system: bringing the person on (records, contracts, registrations/new-hire steps), recording their work and leave (duties/tasks, time, absence), administering pay or pay-related records (in-product payroll, or records handed to/from a service), and retaining the employment record (documents, history, access). Remove → a static contact list / document folder; the "management" is gone.
3. **The household-employer regime** — the system's obligations attach to a private household employing domestic staff (a family, principal, estate, or family office acting as employer), with the distinctive compliance and conduct expectations of that regime (worker classification, household employment taxes or PAYE-equivalents, insurance, in-home service standards), not to a business serving customers. Remove → business payroll / HRIS territory.

Jointly held: 1 alone = address book / org chart; 2 alone = generic workflow or payroll engine with no staff subject; 3 alone = compliance content site. Historical check: paper-era household practice — household books/wage ledgers per servant, duty rosters and staff schedules, house manuals with reporting structure, employment agreements and references, kept by the household itself — satisfies all three legs with no software at all; a Gilded-Age or Victorian household staff book and a modern one-employee payroll app are the same Type. Modern capabilities (apps, automated filings, self-service portals) are not in the core.

### L1 — Common Mature Structure (cross-product, not definitional)

- Payroll machinery: pay schedules, gross-to-net, withholdings, direct deposit/check/self-pay, payslips/paystubs (dominant on the employment-administration pole; absent on the operations pole — hence NOT definitional).
- Employment tax/compliance filings executed or orchestrated: FICA/FUTA/SUTA and W-2/Schedule H (US), PAYE/NI, workplace pensions, employer's liability insurance (UK); deadline tracking; IRS/HMRC correspondence handling.
- Time & leave records: time entry with approvals; PTO/sick/holiday balances surfaced on pay documents.
- Employment documents & HR support: contracts (bespoke generation in some), job descriptions, NDAs, handbooks, HR consultations, employer checklists.
- Onboarding support: employer registrations (EIN/PAYE/state accounts), new-hire reporting, onboarding checklists/progress tracking.
- Employee self-service: scoped staff logins, employee paystub/account access, employee member areas, employee-facing support.
- Worker-classification guidance (employee vs contractor) embedded in product content and setup.
- Staff permissions & privacy controls on the operations side: what each staff member can see/edit, category- and property-scoped access, revocable access.
- Duty/standards machinery on the operations side: task/list assignment per staff member, house manual/protocols, reporting structure, onboarding mentorship/check-ins.
- Insurance and background-check attachment (partner- or tier-dependent).

### L2 — Variant / Optional Structure

- Packaging pole: operations-first platform (staff inside a wider household operating system) vs employment-administration service (payroll/compliance as the product, software + human service).
- Segment envelope: nanny-only ↔ full domestic staff (housekeepers, household managers, personal assistants, groundskeepers, chefs, caregivers, gardeners) ↔ senior-care employment.
- Geographic/regime variant: US federal/state nanny tax vs UK PAYE/pensions/EL insurance; products are regime-bound (Poppins refuses business payroll; Nannytax is UK-only).
- Service depth gradient: DIY tools → guided → concierge/white-glove; pricing per employee/tier.
- Scale shape: one employee (mass market) ↔ multi-employee staffed estates (per-employee pricing, multi-property assignment, multi-state/multi-household support); fractional/multi-family-office operation.
- Placement adjacency: agencies as partners/portals; staffing-agency provenance recorded on profiles; nanny-share co-employment guidance.
- Benefits & retention add-ons: workers' comp, health, 401(k), rewards/wellbeing apps for staff.
- Era-current layers: AI onboarding/assistance (boundary-case estate platform), mobile-first payroll.

### L3 — Vendor-specific (research notes only)

- NINES: Easemakers community/podcast; household-management-expert methodology (Marta Perrone) baked into protocol chapters; @-mention linking; fractional-estate-manager multi-account branding; self-hosted option; SOC 2 Type II claim.
- HomeWork Solutions: Guided/Complete/Premier tier names and prices; 2 annual background checks (Premier); IRS "62 hours per year" estimate quoted; retroactive reconstruction service; 30-years/all-50-states claims; Trustpilot/Google ratings displayed.
- Poppins: flat monthly price; 65,000+ families since 2016; Boulder-based specialists; records kept ≥5 years (product-stated); prior-wages catch-up; named partners (Bhalu workers' comp, Take Command Health, Gusto referral); pay-in-arrears weekly default; Forbes "best household payroll service" claim.
- SurePayroll: Paychex backing; 25+ years; NannyChex heritage; "3-tap" mobile payroll framing; 2-day direct deposit; "$2,800/year (2025)" threshold and "60+ hours/year" claims (product-stated); one-employee base plan.
- Nannytax: Enable Ltd; three annual tiers + monthly payment add-on; Stafftax sibling brand for broader household staff; 70,000 families/32 years claims; rewards & wellbeing app with Digital GP; DBS/Ofsted guidance; Telegraph/FT-cited salary guide.
- EstateSpace (boundary case): Lily AI onboarding of physical-asset inventories; asset-centric pricing tiers.

## Rejected Findings

- "Household Staff Management = household payroll" — **rejected**: the operations-pole product (NINES) manages household staff with no payroll at all, while payroll products stop short of duties/standards machinery. Payroll is the dominant implementation of the employment-administration leg on one pole, not the definition. The market brands the payroll sub-population "household payroll" — a realization, not the Type.
- "The employer is always UHNW / a large estate" — **rejected**: the mass-market samples employ exactly one person (a nanny/housekeeper); per-employee pricing and "one employee" plans exist. Estate-scale is the top variant, not the definition.
- "Shift scheduling is definitional" — **not assertable**: no sampled product documents formal shift/roster planning (operations side uses tasks/lists/calendar; employment side uses pay schedules and time entry). Household staff scheduling as a formal module remains unverified; do not claim it.
- "Background checks / vetting are definitional" — **rejected**: tier add-ons or content guidance only (1 of 5 includes checks in a plan).
- "Agencies run this software" — **rejected**: agencies appear as partners, portals, or provenance notes; the employer-side system is this Type. Agency-side systems belong to staffing-agency territory.
- "Employee self-service is definitional" — **rejected**: present in mature products (4/5) but the historical/paper form and the operations pole function without it; held as common mature structure.
- "EstateSpace belongs in the sample" — **rejected as representative**: asset-centric positioning; staff are users, not the managed subject. Kept as boundary evidence.

## Boundary Findings

1. **vs Payroll System (§08)**: the employment-administration pole is payroll-shaped, and generic payroll systems could be configured for a household; what makes the Type is the household-employer regime and the staff subject (classification, registration-for-the-person, in-home context), not the payroll engine. Test: remove the household-employer regime (employer becomes a business) → Payroll System. Worth joint review when Payroll System is processed: "household payroll" is alternatively arguable as a Payroll System variant; this pass keeps the leaf employer-side and umbrella-shaped.
2. **vs HRIS / Employee Record System (§09)**: same people-as-employees skeleton; different employer (private household vs organization), different compliance regime, different scale, no org-unit apparatus. Test: hand the roster to a business HR department → HRIS.
3. **vs Home Management Application / Family Organizer / Household Chore Application (§29)**: those coordinate household work among family members (no employment relationship, no pay, no employer obligations). Test: remove the employment relationship → those Types. The chore app's task list resembles the operations pole's task assignment; the difference is who performs the work and why the record exists.
4. **vs Childcare Management System (§29)**: care operator runs a licensed business serving many families; here the family is the employer of its own staff. Completely different record centers (enrollment vs employment). Consistent with the sibling pass.
5. **vs Babysitting Marketplace (§29)**: marketplaces explicitly disclaim the employer role ("once you hire someone… you are their employer" — sibling research); the employer-side administration that begins at hire is exactly this Type.
6. **vs Staffing Agency Management System (§09)**: agencies source/place staff (their own business records); the household manages the placed person as its employee. NINES records the agency as provenance; Nannytax runs an agency portal as a partner channel — placement and administration are different loops.
7. **vs Time & Attendance System / Employee Scheduling (§09)**: household time records exist but embedded in employment administration; org-side workforce management (shifts, coverage, forecasts) is not the household shape.
8. **vs Family Care Coordination (§29)**: coordinating care for dependents vs employing the people who provide it; senior-caregiver employment by the family belongs here.
9. **vs estate/property management (§17 family, e.g., estate platforms)**: assets/vendors/projects as center vs people/employment as center; suites may carry both.
10. **vs Personal Concierge Platform (§29)**: delivering errands/services to members vs administering the employment of the people who serve the home.

"去掉什么就变成另一个 Type" summary: remove the household-employer regime → payroll/HRIS; remove the employment relationship → home management / family organizer / chore app; remove the staff roster → document storage or a compliance content site; remove the administration loop → contact list; center placement/matching → staffing agency / care marketplace territory.

## Uncertainties

- **No help-center-level docs fetched for any sample** (member areas are login-gated; help sites JS-gated). All observations are from product/pricing/blog pages; precise operational details (exact status names, exact filing turnaround promises, exact permission matrices) are deliberately not asserted.
- **GTM unobserved** (403 ×2) — the most HR-heavy US household provider would likely have reinforced pole B; absence noted, no claims rest on it.
- **Care.com HomePay / Breedlove unobserved** (403s; domain-name trap at gethomepay.com). The largest US brand names in household payroll are therefore evidenced only indirectly (Poppins' comparison pages), which was not used as primary evidence.
- **NINES evidence depth**: product page + two vendor articles; whether NINES carries any time/payroll-adjacent features beyond time-off logging is unverified. Claims about NINES kept strictly to observed features.
- **Formal staff scheduling** (shift/roster planning) unverified on both poles; left out of all definitional and capability claims.
- **Non-US/UK markets** (continental Europe, Middle East, Asia household-staff software) not sampled; the regime-variant picture may be incomplete.
- **Nanny-share co-employment** (two families as joint employers) appears in resource content (HWS, Nannytax) but mechanics in-product were not observed.
- **Family-office suites** possibly combining estate operations with staff administration — plausible, unverified.

## Final Synthesis

A Household Staff Management application is the employer-side system of record for the people a household employs: nannies, housekeepers, house and estate managers, personal assistants, caregivers, and other domestic staff. The household — a family, principal, estate, or family office, personally or through a manager — holds each staff member as an individually identified employment record (role, status, documents, place of service) and runs the employment over time: bringing the person on, recording duties/worked time/leave, administering pay and pay-related records, meeting the distinctive obligations of household employment (classification, household employment taxes or PAYE-equivalents, insurance), and retaining the record with controlled access. The market realizes this in two poles: household-operations platforms, where staff administration lives inside the household's operating system (duties, standards, manuals, permissions) and payroll stays out; and household employment-administration services, where payroll and compliance are the product and duties stay with the employer. Both poles agree on the spine — staff as employment records of the household-employer, administered over time under the household-employment regime. Placement (agencies, marketplaces) is upstream and outside; family-member household work is a different universe; business payroll and HRIS are the same skeleton under a different employer.
