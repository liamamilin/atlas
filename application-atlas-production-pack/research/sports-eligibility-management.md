# Research Notes — Sports Eligibility Management

Research date: 2026-09-09
Slug: `sports-eligibility-management`
Directory leaf: "Sports Eligibility Management" (Section 28 — Sports, Fitness & Recreation)

---

## Research Goal

Understand what "sports eligibility management" software actually is: what the eligibility machinery holds, who operates it, who the subject is, how a right-to-participate is computed and maintained over time, and — critically — where its boundary lies against the already-processed sibling School / College Athletics Management, whose pass found the participation gate to be ITS defining core and left a joint-review flag for this leaf.

## Initial Boundary (hypothesis before research)

- Hypothesis: eligibility management = the machinery that determines whether a person may participate in organized sport (registration status, medical clearance, age/identity verification, academic standing, certifications, background checks), held as a standing state over time.
- Likely confusions:
  - School / College Athletics Management (processed sibling — its defining core IS the participation gate; severe overlap flagged for joint review)
  - Sports Registration Platform (signup transactions feeding the gate)
  - Sports Federation Management (federation-run governance; federation-run player registration may be an eligibility realization)
  - Sports Membership / Licensing Platform (membership/licensing as eligibility inputs)
  - Background Check Platform (§15) and Certification Management (§25) as generic machinery
- Unknowns: does a free-standing eligibility market exist outside school athletics? Is the subject always the athlete? Who operates eligibility systems (school / association / governing body / federation)? Is the NCAA Eligibility Center the same Type or a different one?

## Research Questions

1. What does "eligibility" concretely consist of in each product/context — which conditions constitute it?
2. Who is the subject of eligibility — athletes only, or also coaches/officials?
3. Who operates the system (school, state association, governing body, federation) and who sets the requirements?
4. What is the lifecycle of an eligibility determination (collection → evaluation → status → gate → decay → renewal)?
5. How does status gate participation, and who consumes the status?
6. What artifacts carry eligibility (dashboard state, passcard, official roster, certification decision)?
7. Where is the boundary against School / College Athletics Management (joint review), Sports Registration Platform, Sports Federation Management, Sports Membership / Licensing Platform?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and — decisively — different OPERATOR poles, to test whether the Type exists outside the school department system:

| Product | Pole | Operator | Subject | Tier |
|---|---|---|---|---|
| FinalForms (Athlete Eligibility & Clearance) | school eligibility-first product | school / district | student-athletes | A (product page) |
| Arbiter Eligibility | coach & official eligibility product | associations / schools | coaches, officials | A (product page) |
| DragonFly Max (Rosters & Eligibility) | school/association ecosystem | schools via 20+ state associations | student-athletes | A (product page) |
| NCAA Eligibility Center | governing-body clearinghouse | the NCAA itself | college-bound student-athletes | A (official program pages) |
| PlayNAIA | governing-body clearinghouse | the NAIA itself | college-bound student-athletes | A (official portal) |
| US Club Soccer Player Registration (on GotSport) | federation member eligibility | federation (requirements completed by club admins/parents) | club players (youth/adult) | A (official program documentation) |

Notes:
- The first three are the same vendor family as the School/College Athletics Management pass's samples — deliberately included, because the joint review must be grounded in the overlap pole itself.
- The last three are the critical samples: they prove the eligibility machinery exists as a free-standing service operated by authorities, with no school department anywhere in the picture.
- PlayNAIA corroborates the NCAA pole (two clearinghouse instances).

## Sources

All Layer A unless noted. Fetched 2026-09-09.

- FinalForms — Athlete Eligibility & Clearance: https://www.finalforms.com/athletic-management/athlete-eligibility-tracking/
- Arbiter — Coach and Official Eligibility: https://arbiter.io/products/eligibility/ (canonical URL /products/coach-and-official-eligibility/)
- DragonFly — For Schools: https://www.dragonflymax.com/schools
- NCAA — Eligibility Center: https://www.ncaa.org/eligibility-center/
- NCAA — homepage (Eligibility Center registrant count): https://www.ncaa.org/
- PlayNAIA — https://playnaia.org/
- US Club Soccer — Player Registration: https://usclubsoccer.org/playerregistration/

Not reached (limitations):
- https://www.eligibilitycenter.org/ (the dedicated NCAA EC site) — transport error; substituted with ncaa.org/eligibility-center/ (same operator, official).
- Vendor help centers (FinalForms documentation portal, Arbiter Zendesk, DragonFly help articles, GotSport support) not fetched this pass; school-pole evidence is product/marketing-page strength, while NCAA/NAIA/US Club Soccer pages are operational program documentation (requirement lists, gate rules) — stronger.
- No pricing, no numeric limits asserted beyond quoted page text.

---

## Product A — FinalForms (Athlete Eligibility & Clearance)

### Key observations (Layer A)

Positioning: dedicated product page "Athlete Eligibility & Clearance" inside the Athletic Management solution; "FinalForms gives athletic directors, coaches, and medical staff the tools they need to track athlete eligibility and clearance in real time… no athlete steps onto the field without full clearance."

Eligibility machinery (page's own feature list):
- **Eligibility dashboards** — "View clearance status by athlete, sport, school, or coach — updated in real time."
- **Physical expiration tracking** — "Monitor countdowns and send automatic reminders before athletes fall out of compliance."
- **Return-to-play documentation** — "Track injury reports, upload doctor clearances, and verify status before athletes return."
- **Form status filters & flags** — "Instantly identify athletes who are missing forms, overdue for physicals, or flagged for medical reasons."

FAQ (vendor's own definition): "Eligibility is determined by form completion, physical clearance, medical flags, and required acknowledgments — all tracked in real time." Expiration behavior: "FinalForms tracks expiration dates and automatically alerts families and coaches before compliance lapses." Audit: "Every action — submission, approval, expiration — is time-stamped and stored for future reference or audit purposes." Compliance: FERPA; "district and state eligibility rules."

Stakeholders: coaches ("Know who's cleared and who's not — before practice starts"), athletic directors ("Ensure athletes meet district and state eligibility rules across all teams… full visibility across levels and seasons"), parents ("automated alerts… submit forms and updates from any device").

Reading: the eligibility machinery = requirement set (forms + physical + acknowledgments + medical flags) → evidence → real-time status → gate before activity → decay/alerts → audit trail. Operator: school; authority: district/state. No scheduling/events on this product surface — eligibility is the center.

## Product B — Arbiter Eligibility (Coach and Official Eligibility)

### Key observations (Layer A)

Positioning: "Arbiter Eligibility simplifies compliance for officials and coaches by providing flexible tools to track progress, enforce rules, and stay ahead of challenges." **The subject is coaches and officials, not athletes** — a standalone product in the Arbiter suite.

Machinery (page's own feature blocks):
- **Stay Compliant Without the Guesswork** — "Ensure officials and coaches meet certification requirements. Arbiter Eligibility tracks progress, verifies credentials… Build custom eligibility rules for your state and organization's needs. Monitor compliance for coaches and officials. Use tiered eligibility to differentiate between roles like postseason officials or coaches. Integrate background checks for added security."
- **Training Tools Built for Accountability** — "Offer online training and certification for officials and coaches. Track their progress through refresher courses… Offer training through clinics, online tests, and USSF certification. Set pass/fail thresholds to meet organizational standards. Track completion and compliance progress easily."
- **One Place for Every Form and Fee** — "Automate the collection of critical data and forms… Manage thousands of users with a single intuitive registration system. Reconcile registration fees on one platform. Collect all critical data, like BGC consent and personal information."
- **Track Eligibility With Zero Lag** — "Monitor eligibility, badges, and credentials in real time. Stay ahead of deadlines and verify eligibility before event participation… Use achievement badges to quickly assess levels. Maintain detailed histories to address questions quickly. Use live dashboards to track eligibility instantly. Verify compliance before participation in events."

Reading: same machinery as the athlete pole — custom rules (state/organization), evidence (credentials, training completion, background-check consent, forms, fees), real-time status, gate before event participation, histories. Distinctive: tiered eligibility (role-differentiated), pass/fail thresholds, badges. Operator: associations/organizations; subject: coaches/officials.

## Product C — DragonFly Max (Rosters & Eligibility)

### Key observations (Layer A)

Positioning: "DragonFly is a streamlined tool for Athletics Management… connect your school administrators, coaches, athletic trainers, parents, and players into one platform." Pain list includes "A lot of work managing rosters and eligibility."

For Schools — **Rosters & Eligibility** block: "It's Your School's Athletic Data Hub — streamlined and easy to filter"; "Simplify roster management for teams and levels"; **"Easily see who is eligible to play"**; "Custom forms for simplified, paperless registration"; "3rd party data integration for academic eligibility."

Player Safety: "Fingertip access to physicals and medical information"; injury reports. Trainer quote: "quickly communicate info to coaches regarding their athletes' playing status, compliance with rehab, & restrictions."

Association side (nav): "For Associations — Membership Management; … Eligibility & Certifications" — the same machinery operated at association scale. State-association partners displayed (AHSAA, GHSA, NCHSAA, MHSAA, OHSAA, etc.).

Reading: eligibility as the school's data hub with roster management, custom forms, academic-eligibility integration, physicals; the association pole runs "Eligibility & Certifications" for its member schools. Operator: school + association; authority: state association.

## Product D — NCAA Eligibility Center

### Key observations (Layer A)

Positioning (official): "The NCAA Eligibility Center helps college-bound student-athletes understand and complete the academic and athletics eligibility steps needed to compete at an NCAA school." — **"Initial eligibility certification determines whether you may practice, compete and receive athletics aid during your first year as a full-time college student."**

Machinery (official program pages):
- **Registration** — "Students desiring to compete at any NCAA school must register with the NCAA Eligibility Center. Students may register at any age." Account types: Profile Page vs Academic and Athletics certification account (division- and student-type-dependent).
- **Requirements** — "Learn Initial Eligibility Requirements: Understand the academic and athletics standards needed to compete at an NCAA school." Division-specific academic requirements (DI/DII academic certification; DIII amateurism standards, no academic certification).
- **Pathways** — international student-athletes, homeschooled students, transfer students (transfer rules and eligibility).
- **School side** — "Access tools to manage school accounts, submit transcripts and support students through the NCAA Eligibility Center process" (high school resources); "Compliance Administrator Resources" (college side).
- Scale (homepage): "200,000+ ELIGIBILITY CENTER REGISTRANTS."

Reading: the clearinghouse pole — the registrant is the ATHLETE (self-registration, account types), the certifier is the GOVERNING BODY itself, requirements are the authority's own rules (academic + amateurism), evidence flows in from third parties (high schools submit transcripts), the output is a certification decision that colleges consume. No school department system, no teams, no schedules — pure eligibility certification.

## Product E — PlayNAIA

### Key observations (Layer A)

Positioning (official portal): "PlayNAIA.org helps future student-athletes discover and connect with NAIA schools, coaches and athletic scholarships. **PlayNAIA is also the official clearinghouse for NAIA eligibility. Every student-athlete must register with the NAIA Eligibility Center to play sports at an NAIA college or university.**"

Value framing for athletes: "Eligibility — Make sure your eligibility is in order; Increase your opportunity for scholarships; Show coaches you are ready to play." Audience surfaces: For High Schools / For Parents / For Recruiters / For Colleges and Universities. Registration wall: "REGISTER STUDENT"; access note: "Please contact your Athletic Director or Registrar to be granted access to the PlayNAIA system" (for school-side users).

Reading: second clearinghouse instance — same structure as NCAA EC (athlete self-registration, authority-run certification, mandatory gate: "must register… to play"). Adds recruiting visibility riding on the eligibility record ("let our coaches find you").

## Product F — US Club Soccer Player Registration (on GotSport)

### Key observations (Layer A)

Positioning (official program documentation): "Registration is required of all players participating in US Club Soccer-operated or -sanctioned programming. **Players who are not currently registered with US Club Soccer are not allowed to participate in US Club Soccer programming, nor are they covered by US Club Soccer insurance.**"

The page's own heading: "PLAYER REGISTRATION / **MEMBERSHIP ELIGIBILITY REQUIREMENTS**" — "One is registered with US Club Soccer when the following requirements are completed and current."

Requirement set (each with applicability, timeframe, who completes it):
1. **Registration/membership purchase** — all players; each registration year (ex: 2026-27); completed by the club (Org Member) administrator on behalf of the player. "To be fully registered, all requirements must be fulfilled, including the payment of US Club Soccer player or staff fees."
2. **Proof of birth verification** — youth competitive players; once; uploaded by parent/player or club admin, **verified by US Club Soccer**; accepted documents enumerated (government-issued birth certificate, passport, driver's license…); altered documents → "tendered to US Club Soccer's Safeguarding and Compliance team… disciplinary action, including suspension."
3. **Form R002** (Player Info, Medical Treatment Authorization, Liability Waiver/Release and Consent) — all players; via GotSport or certified on file by club registrar.
4. **SafeSport Core or Refresher training** — annual cycle (Core yr 1, Refreshers yr 2–4, repeat); applicable to youth players turning 18+ and adults on teams with minor athletes; "A player's registration will not be valid, **a passcard will not be issued, and the player will not appear on an Official Roster** until SafeSport training (and any other applicable requirement) is completed and approved in the player's account."
5. **Sex Offender Registry–Adverse Eligibility List Review Certification** — club admin verifies the player is not on sex-offender registries, SafeSport Centralized Disciplinary Database, U.S. Soccer Risk Management Disqualifications, US Club Soccer Suspensions list; ongoing checks managed by US Club Soccer.

Mechanics: admin adds person with role Player + affiliation + competitive level → "the applicable requirements and forms will be available via the dashboard of that person being registered." Also: "FIFA & U.S. Soccer player eligibility / international clearance" referenced upstream.

Reading: the federation pole — eligibility = registered status computed from a multi-item requirement set; evidence verified by the federation itself (birth documents) or synced (SafeSport); the gate is total ("not allowed to participate… not authorized to travel, practice, train, scrimmage, play"); the artifacts are the **passcard** and **Official Roster placement**; the state renews per seasonal year and decays when requirements lapse. Operator: federation; completed by club admins/parents on behalf.

---

## Cross-product Comparison

| Structure | FinalForms | Arbiter Elig. | DragonFly | NCAA EC | PlayNAIA | US Club Soccer |
|---|---|---|---|---|---|---|
| Participant as subject of record | ✔ athletes | ✔ coaches/officials | ✔ athletes | ✔ college-bound athletes | ✔ college-bound athletes | ✔ club players (youth/adult) |
| Requirement set configured by/for the operator | ✔ forms+physical+acknowledgments+medical flags; "district and state eligibility rules" | ✔ "custom eligibility rules for your state and organization" | ✔ custom forms; association eligibility & certifications | ✔ academic + amateurism standards by division | ✔ NAIA eligibility standards | ✔ 5-item requirement list incl. fees, birth verification, SafeSport, registry checks |
| Evidence collection (forms/documents/training) | ✔ submissions, uploads, doctor clearances | ✔ forms, credentials, training, BGC consent, fees | ✔ custom paperless forms; physicals | ✔ registration, transcripts from high schools | ✔ registration | ✔ uploads (PoB), forms (R002), training sync, admin certifications |
| Evaluation → participation status | ✔ clearance status real-time | ✔ real-time eligibility, badges, pass/fail thresholds | ✔ "see who is eligible to play" | ✔ certification decision (may practice/compete/receive aid) | ✔ eligibility in order | ✔ "fully registered" only when ALL requirements fulfilled |
| Status gates participation before activity | ✔ "no athlete steps onto the field without full clearance"; coaches check before practice | ✔ "verify compliance before participation in events" | ✔ playing status to coaches | ✔ determines whether you may practice/compete | ✔ "must register… to play" | ✔ "not allowed to participate… not authorized to travel, practice, train, scrimmage, play" |
| Decay & renewal over time | ✔ physical expirations, countdowns, alerts | ✔ deadlines, refresher courses | (seasonal rosters) | ✔ (account valid through process; transfer rules) | ✔ (annual cycle implied by clearinghouse model) | ✔ each registration year; SafeSport annual cycle; "completed and current" |
| Audit-ready records | ✔ time-stamped, audit | ✔ detailed histories | (data hub) | ✔ (certification records) | ✔ | ✔ (verification records; altered-doc disciplinary path) |
| Reporting to authority | ✔ district/state rules, compliance dashboards | ✔ association/state rules | ✔ association eligibility & certifications | ✔ IS the authority's record | ✔ IS the authority's record | ✔ IS the federation's record; ongoing checks managed centrally |
| Eligibility artifact consumed downstream | ✔ dashboard status to coaches/ADs | ✔ badges/status to event organizers | ✔ status to coaches | ✔ certification consumed by colleges | ✔ eligibility consumed by NAIA schools | ✔ passcard + Official Roster |
| Third-party data integration | ✔ SIS (academic) | ✔ background checks, USSF certification | ✔ 3rd-party academic eligibility | ✔ high-school transcripts | ✔ school/registrar access | ✔ SafeSport sync, registries |
| Return-to-play / medical re-gate | ✔ explicit | ✖ | ✔ injury reports, playing status | ✖ | ✖ | ✖ (medical treatment authorization form only) |
| Tiered eligibility (role/level) | ✖ (levels/seasons) | ✔ postseason officials vs coaches | ✖ | ✔ division/account-type differentiation | ✔ | ✔ youth-competitive vs rec vs adult requirement mixes |
| Fees/payment inside eligibility | (implied elsewhere) | ✔ reconcile registration fees | ✖ | ✔ (registration fees exist; not on fetched page) | ✔ | ✔ explicit requirement |
| Recruiting visibility on the record | ✖ | ✖ | ✖ | (recruiting rules adjacent) | ✔ "let our coaches find you" | ✖ |

### Reading of the comparison

- **Participant + requirement set + evidence → status + gate + decay/renewal + authority reporting** appear in all six products across all three operator poles → definitional candidates.
- The **subject axis varies** (athletes / coaches+officials / club players) → the invariant is "participant", not "student-athlete".
- The **requirement content varies** by pole (medical/physical in K-12; academic/amateurism in college clearinghouses; age/identity + safeguarding in federation youth sport; certifications/background checks for coaches/officials) → the invariant is the configured requirement set, not any specific requirement type.
- **Return-to-play** is K-12-pole-dominant → common, not definitional.
- **Tiered eligibility** appears in two products in different forms (role tiers; division/account tiers; competitive-level requirement mixes) → common mature structure.
- **The operator model varies** (school-purchased, association-scale, authority-run clearinghouse, federation-run) → variant axis, not definition.
- **Recruiting visibility** is single-pole → optional.

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

The participant-eligibility machinery as a system of record, holding exactly four jointly-held structures:

1. **The participant as subject of record** — an identified person whose right to participate is the tracked object (athlete in most realizations; coach/official in others; several systems track more than one participant kind). Remove → document manager / form tool / people database.
2. **The requirement set as the eligibility rule** — the configured set of conditions that constitute eligibility (registration/consent forms, medical clearance, age/identity verification, academic standing, training/certification, background/registry checks, fees), set by the operating organization or its governing authority. Remove → a checklist with no rule semantics, or generic document collection.
3. **Evidence collection and status evaluation** — the participant's submissions (forms, documents, verifications, training completions) gathered and evaluated against the requirement set into a participation status (eligible / not eligible / pending), per person and commonly per sport/season/role. Remove → requirement list with no state, or data collection with no gate.
4. **The standing eligibility state over time, surfaced to gate participation** — the status persists across the participation period, decays (expirations, annual cycles), renews per season/registration year, is surfaced to those who must honor it before activity (coaches, clubs, colleges, event organizers) and reported to those who govern it (audit-ready records). Remove → one-shot registration transaction (Sports Registration Platform territory) or a static document archive.

Jointly-held load-bearing:
- 1 alone = people database
- 2 alone = rulebook
- 3 without 1+2 = document upload
- 4 without 1–3 = empty status board
- 1+2+3 without 4 = one-shot registration (Sports Registration Platform)
- 2+3+4 without 1 = anonymous compliance checklist
- 1+4 without 2+3 = roster with asserted statuses nobody computed

### L1 — Common Mature Structure

- self-service registration/forms for participants or families (e-signature, document upload, status indicators)
- real-time eligibility dashboards filtered by person / sport / season / role / school
- expiration tracking with countdowns and automated reminders before compliance lapses
- requirement configuration (custom rules per state/organization; tiered eligibility by role or level)
- document verification (birth/identity documents, physicals, doctor clearances) with reviewer roles
- third-party data integration (academic eligibility from SIS, background-check providers, safeguarding-training sync)
- automated communication to participants/families/stakeholders (alerts on missing items, expirations, status changes)
- audit-ready time-stamped records and detailed histories
- reporting/oversight for associations and governing authorities
- eligibility artifacts consumed downstream (dashboard status, passcards, official-roster placement, certification decisions)
- fee collection reconciled inside the registration/eligibility flow (pole-dependent)

### L2 — Variant / Optional Structure

- operator model: school/district-purchased product; state-association-scale platform (member schools); governing-body-run clearinghouse (athlete self-registration); federation-run member registration (club admins complete on behalf)
- subject scope: athletes only vs athletes + coaches + officials
- requirement-content mix: medical/physical + return-to-play (K-12); academic + amateurism (college clearinghouses); age/identity + safeguarding + registry checks (federation youth); certifications + background checks + pass/fail training thresholds (coaches/officials)
- tiered eligibility (postseason vs regular officials; division/account types; competitive-level requirement mixes)
- return-to-play machinery (injury-driven re-gate) — K-12-dominant
- recruiting visibility riding on the eligibility record (clearinghouse pole)
- multi-organization hierarchies (state → school; federation → club → player)
- insurance coverage tied to eligibility standing (federation pole)

### L3 — Vendor-specific (Research Notes only)

- FinalForms: E-Cards (emergency medical), countdowns vocabulary, "3,000+ schools" claim, FAQ-defined eligibility formula.
- Arbiter: achievement badges, tiered eligibility for postseason officials, USSF certification delivery, BGC consent collection, "thousands of users" registration claim.
- DragonFly: "+1 communication" oversight, Key People reports for game-day resource officers, free-for-schools model, 20+ state associations / 1.5M+ athletes / 300k officials counts (from sibling pass's fetch of the same site family).
- NCAA: Profile Page vs Academic and Athletics certification account types; "nearly 8 million high school students play sports" framing; 200,000+ registrants; 877 support line; Guide for the College-Bound Student-Athlete.
- PlayNAIA: 87K student-athletes / 250 schools / $1.3B scholarships / 20 conferences / 30 championships; recruiter/parent/high-school audience surfaces.
- US Club Soccer: GotSport platform, Form R002, passcard, Official Roster, Policy 13.08, SafeSport annual cycle (Core yr 1 → Refreshers yr 2–4 → repeat), PoB accepted/rejected document lists, adverse-eligibility-list review, FIFA/U.S. Soccer international clearance reference.

## Rejected Findings (not promoted)

- **School/K-12 framing as definitional** — rejected: NCAA EC, PlayNAIA, and US Club Soccer satisfy the core with no school department anywhere; the clearinghouse and federation poles are operator variants.
- **Medical/physical clearance as definitional** — rejected: NCAA certifies academics/amateurism; US Club Soccer's requirement list has no physical-exam item; Arbiter's coach/official eligibility has none. The invariant is the requirement set, not any specific requirement.
- **Academic eligibility as definitional** — rejected: only school/college contexts carry it; federation and coach/official poles do not.
- **The department portfolio (teams/coaching staff/schedules/events) as definitional** — rejected: the clearinghouse and federation poles hold no program portfolio and no event operations; this is precisely the seam with School/College Athletics Management.
- **Online forms as definitional** — rejected: paper-era eligibility sheets, physical cards, and federation player passcards satisfy the core (historical check below).
- **Background checks as definitional** — rejected: one requirement type among several; present in Arbiter (coach/official) and US Club Soccer (adult/18+ players), absent in the K-12 athlete pole's stated formula.
- **Payment as definitional** — rejected: explicit in US Club Soccer and Arbiter, not part of FinalForms' stated eligibility formula.
- **"Clearinghouse" operator model as definitional** — rejected: school-operated and association-operated realizations are equally in-type.
- **Specific status vocabularies, expiration windows, numeric limits** — no cross-product evidence; not stated.

## Boundary Findings

### vs School / College Athletics Management (processed sibling) — JOINT REVIEW, DISCHARGED FROM THIS SIDE

The athletics pass found the participation gate to be ITS defining core and flagged severe overlap, proposing the discriminator "eligibility machinery bound to a department's standing program portfolio and governing-authority loop vs eligibility as a free-standing right-to-compete service." This pass's research **ratifies keep-both** on a center-of-gravity seam, with the discriminator refined by evidence:

- **Pure-play realizations exist outside the department system.** The NCAA and NAIA Eligibility Centers are governing-body-run certification services: the registrant is the athlete, the certifier is the authority itself, and there is no school department, no program portfolio, no event operations anywhere in the system. US Club Soccer's player eligibility is federation-run for club players. No one would describe these as "school athletics management systems."
- **The subject axis extends beyond the department pass's scope.** Arbiter's standalone Eligibility product centers on coaches and officials (certifications, background checks, tiered postseason eligibility) — subjects the department-system pass never covered.
- **The overlap pole is real but separable.** FinalForms, DragonFly, and Arbiter appear in both passes' samples — the same vendors sell the department system and the eligibility machinery. But the eligibility machinery is a separable center of gravity: FinalForms' eligibility product has no scheduling, facilities, officials, or event operations at all; strip those from a connected department platform and the eligibility machinery stands alone as this Type.
- **Refined discriminator:** School/College Athletics Management = the department's administrative system of record — its center is running the department (program portfolio + participation gate + authority loop + event operations). Sports Eligibility Management = the right-to-participate machinery itself as the system's center — participants + requirement sets + evidence + standing status, with no program portfolio and no event operations. The gate appears in both; in the department system it is one leg of a three-leg core; here it is the whole system.
- **Directional test:** strip the department's program portfolio (teams by sport/level/season with coaching staff as the unit of record) and event operations → what remains (participants, requirements, evidence, status, authority reporting) is Sports Eligibility Management. Add the portfolio and event operations → School/College Athletics Management.
- Same pattern as the registration seam the athletics pass recorded: capability-slice Types kept because pure-play forms exist in the market.

### vs Sports Registration Platform

Registration is the collection transaction (signup for a program/event/season); eligibility is the standing gate computed from collected evidence and maintained over time. Registration feeds eligibility. US Club Soccer shows the seam inside one system: the registration/membership purchase is ONE requirement among five; the player is "fully registered" — i.e., eligible — only when ALL requirements are fulfilled and current. A registration platform's unit is the signup without a managed, decaying, gate-serving status. Remove the standing gate → Sports Registration Platform. (Same seam the athletics pass recorded from its side.)

### vs Sports Federation Management

The federation governs member organizations (affiliations, sanctioning, competitions). Federation-run player eligibility (US Club Soccer) is the eligibility machinery operated BY a federation — the center is the individual participant's status, not the governance of member clubs. Remove the participant-status center → Sports Federation Management; the eligibility system is one program a federation operates.

### vs Sports Membership / Licensing Platform

Membership = belonging + dues; licensing = permission to practice a role (coach license, official license). Eligibility = right to participate in sanctioned activity under a requirement set. They overlap heavily at the input layer — US Club Soccer literally titles its page "registration/membership eligibility requirements," and Arbiter's coach/official eligibility tracks credentials. The seam is the center: the participation gate over a requirement set vs the credential/dues relationship. A membership system can exist with no participation gate; an eligibility system can gate participation with no membership relationship (e.g., NCAA certification of a college-bound athlete who belongs to no member organization yet).

### vs Background Check Platform (§15)

Background checks are one requirement type inside eligibility (Arbiter integrates them; US Club Soccer requires registry reviews). The generic Type centers on the screening workflow itself, not on participation rights. Remove the participation-gate semantics → background-check territory.

### vs Certification Management (§25)

Generic credential lifecycle management vs the sports participation gate. The closest overlap is the coach/official pole (Arbiter: certifications with pass/fail thresholds gating event participation) — held inside this Type because the output gates participation in sport; a generic certification system has no participation semantics.

### vs Student Information System / School Management System

The SIS owns enrollment/grades/attendance for the whole school; eligibility systems consume academic-standing data from it (DragonFly's "3rd party data integration for academic eligibility"; FinalForms SIS sync; NCAA high-school transcript submission). Complementary, data-flow seam.

### vs Athlete Injury / Availability Management (processed)

Medical availability for training/competition decisions (team-staff view, injury lifecycle) vs the administrative clearance gate (eligibility). Return-to-play sits at the seam: FinalForms treats it as eligibility documentation (a re-gate inside the eligibility machinery); the injury/availability Type treats the injury record itself as the center.

### vs Athlete Recruiting Marketplace (processed)

Clearinghouse eligibility records carry recruiting visibility (PlayNAIA: "let our coaches find you"; NCAA recruiting rules adjacent), but the center is certification, not two-way marketplace interest between athletes and coaches. Remove the certification machinery → recruiting marketplace; add it → this Type.

**"Remove what to become the other Type" judgments:**
- Remove the requirement set + evidence evaluation → people/roster database.
- Remove the standing state over time (keep one-shot collection) → Sports Registration Platform.
- Remove the participation-gate semantics → document collection / compliance checklist.
- Add the department program portfolio + event operations → School / College Athletics Management.
- Add member-organization governance → Sports Federation Management.
- Narrow to the credential/dues relationship → Sports Membership / Licensing Platform.

## Historical / Market-Sample Check

- **Paper-era school athletics:** the AD's master eligibility sheet + physical cards + consent forms + birth-certificate checks, compiled before the season and checked by coaches before practice — satisfies all four L0 structures (participant, requirement set, evidence, standing status gating play) with no software. Passes.
- **Paper-era federation:** the federation player registration card/passcard in association football — a player registered with the federation is eligible to play in sanctioned matches; the physical card is checked before matches; registration renews per season. Satisfies all four structures; the passcard is the artifact leg. Passes.
- **Paper-era clearinghouse:** a governing body certifying college-bound athletes by mailed transcripts and paper certification letters satisfies the core (participant self-registration, authority-set requirements, evidence evaluation, standing certification consumed by colleges). No dates asserted — conceptual check. Passes.
- **Regional:** the sampled market is US-shaped (state associations, NCAA/NAIA, US Club Soccer). The abstract core also describes non-US federation player-registration/qualification systems (the US Club Soccer page itself references FIFA international clearance regulations — the same eligibility semantics at international level), but no non-US product was sampled. Recorded as a limitation, not a boundary failure.
- **Older software generations:** desktop registration/eligibility trackers with printed eligibility lists satisfy the core without dashboards, integrations, or portals. Passes.

## Uncertainties

1. School-pole evidence (FinalForms, Arbiter, DragonFly) is product/marketing-page strength; vendor help-center operational detail (exact workflow steps, status vocabularies, permission matrices) was not fetched. Assertion strength kept at "commonly/typically" for anything below the products' explicit statements.
2. eligibilitycenter.org unreachable (transport error); NCAA evidence rests on ncaa.org's official Eligibility Center pages — same operator, official program documentation.
3. Youth-club registration products (TeamSnap, Sports Connect class) were not sampled; the federation pole (US Club Soccer on GotSport) covers club-level eligibility, but consumer-club products' eligibility depth is unverified.
4. The registration↔eligibility vocabulary varies by vendor (Arbiter separates Student Registration from Eligibility; US Club Soccer merges registration and eligibility into one requirement list; FinalForms sells separate registration and eligibility pages) — recorded as implementation variance, not a structural split.
5. Non-US school-eligibility software not sampled; the federation-pole generalization to non-US federations is structural reasoning, not sampled evidence.
6. Whether the NCAA Eligibility Center's internal workflow (evaluation steps, timelines) matches the school-pole loop is unverified — the clearinghouse's internal process detail was not fetched; only its registration/certification framing is evidenced.

## Final Synthesis

Sports Eligibility Management is the right-to-participate machinery as a system of record. Its defining core is four jointly-held structures: (1) the participant as subject of record — an identified person (athlete; commonly also coach/official) whose right to participate is the tracked object; (2) the requirement set as the eligibility rule — the configured conditions that constitute eligibility, set by the operating organization or its governing authority; (3) evidence collection and evaluation — submissions gathered and evaluated into a participation status per person (commonly per sport/season/role); (4) the standing eligibility state over time — decaying, renewable, surfaced to gate participation before activity and reported to the governing authority with audit-ready records. The market realizes the Type in three operator poles — school/association eligibility products (FinalForms, Arbiter, DragonFly), governing-body clearinghouses (NCAA, NAIA Eligibility Centers), and federation member-registration systems (US Club Soccer on GotSport) — plus a subject axis (athletes vs coaches/officials). The joint review with School / College Athletics Management ratifies keep-both on the center-of-gravity seam: the department system's center is running the department (portfolio + gate + authority loop + event operations); this Type's center is the participants' right to play, with no portfolio and no event operations. Pure-play realizations (the clearinghouses, the federation pole, the coach/official pole) exist entirely outside the department system, which is what makes this a definable Type rather than a capability slice with no independent market.
