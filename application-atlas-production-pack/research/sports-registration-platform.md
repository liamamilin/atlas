# Research Notes — Sports Registration Platform

## Research Goal

Understand what "Sports Registration Platform" software actually is from real products: what the sign-up offer is (program/season/division structure), what the registration transaction produces, what the organization does with the output, which parts of the surrounding sports stack (teams, eligibility, membership, federation, league, meet, scheduling) are bundled vs separable, and where the boundary sits against the seven sibling §28 passes that pre-hung flags at this leaf, against Event Registration Platform (§26, processed), and against form-builder machinery (§03.11).

## Initial Boundary

Working hypothesis before research:

- Core use: organization-side intake software whose center is the sign-up transaction — a sports organization (league, club, school athletics program, governing body) defines programs/seasons, participants (players/athletes, commonly registered by guardians) sign up through the platform's own flow, fees are commonly collected, and the output is a working roster of registered participants.
- Primary users: administrators/registrars of sports organizations (often volunteer-run at the youth pole; athletic directors at the school pole); registrants are parents/guardians of players or adult players.
- Nearest neighbors (all flagged or processed): Event Registration Platform (§26 — event-occurrence semantics), Youth Sports Management (unprocessed — org-led), Sports Club Management (processed — member-org-led), Sports Academy Management (processed — program/tuition-led), Sports Eligibility Management (processed — standing gate), Sports Membership / Licensing Platform (processed — standing renewable relationship + credential), Sports Federation Management (processed — governance register), Sports Meet Management (processed — entries bound to an event program), League Management Platform (processed — season competition loop), Team Management Application (unprocessed — team life after registration), Sports Scheduling Platform (unprocessed), Online Form Builder (§03.11 — bare intake), Course Registration System (§23), Camp Management System (§26 — camp session operation).
- Known unknowns: is the season/division structure definitional or just vocabulary? Is money definitional? Is guardian-linked registration definitional? Does the registration platform own teams? What does renewal/rollover look like? Where does the NGB/federation data flow enter?

## Research Questions

1. What is the central object — the program, the season, the form, the registration record, or the roster?
2. What does the offer structure look like (program types, seasons, divisions/levels, age groups, gender, youth vs adult modes)?
3. What does the registration transaction run through (public listing → form → questions → waivers/documents → payment → confirmation)? What states does the offer move through?
4. Is money definitional or common? What direct evidence exists for registration without a fee leg?
5. What roster operations exist post-registration (search/sort/filter, edit/cancel/refund, communicate, export, handoff to teams)?
6. How do renewals/rollovers work (copy program, auto-filled returning data)?
7. Where do eligibility-style requirements (physicals, birth certificates, background checks) enter — as signup inputs or as a standing gate?
8. What does the platform NOT do — where do teams/scheduling/results/competition machinery begin?
9. Which poles exist (youth-volunteer, club/league operator, school athletics, NGB/governing-body, adult self-registration)?
10. Historical check: does paper-era registration (registration night, mail-in forms, the registrar's ledger) satisfy the proposed core?

## Representative Products

Selected for market representation, documentation availability, different product philosophies, and different customer tiers:

| Product | Pole | Tier | Evidence quality |
|---|---|---|---|
| LeagueApps | registration-first platform for league/club/camp operators (program-type machinery; deepest Tier-1 docs) | SMB→mid youth sports operators | product home + registration feature page + help center root + Program Registration category + Program Creation article (Tier 1) |
| Jersey Watch | small volunteer-run org pole (forms-fast, websites + registration) | SMB youth sports / rec leagues | registration feature page (Layer A, rich) |
| FinalForms | school athletics registration pole (forms/status/compliance emphasis) | K-12 schools/districts | product home + athletic registration solution page (Layer A, rich) |
| Sports Connect (Stack Sports) | NGB + local league pole (governing-body integrations) | NGBs/state associations + local clubs/leagues | product home (Layer A) |
| TeamSnap (cross-referenced) | club/league suite whose registration machinery was captured this date by the sibling sports-club pass | SMB→mid clubs & leagues | Tier-1 help-center category inventory recorded in research/sports-club-management.md (same date) — reused as cross-product evidence, not freshly fetched |

Abandoned samples (network rule): SportsEngine / help.sportsengine.com (403 twice — the NGB-side enterprise pole evidenced only indirectly via Sports Connect and the federation/membership passes). PlayMetrics unreachable per prior passes (JS-rendered); noted via Sports Connect's own merger banner.

## Sources

Fetched 2026-09-09:

- LeagueApps — product home: https://leagueapps.com/ ; registration feature page: https://leagueapps.com/youth-sports-management-platform/registration/ ; help center root: https://support.leagueapps.com/hc/en-us ; Program Registration category: https://support.leagueapps.com/hc/en-us/categories/1500001458141-Program-Registration ; "Getting Started With Program Creation": https://support.leagueapps.com/hc/en-us/articles/360039382354-Getting-Started-With-Program-Creation
- Jersey Watch — registration feature page: https://jerseywatch.com/features/sports-registration-software (footer navigation of the same page: who-we-serve audience set, compare pages, help center link)
- FinalForms — product home: https://www.finalforms.com/ ; "Athletic Forms & Registration": https://www.finalforms.com/athletic-management/athlete-registration-software/
- Sports Connect — product home: https://www.sportsconnect.com/
- TeamSnap — help center category evidence recorded 2026-09-09 in research/sports-club-management.md (Clubs & Leagues / Invoicing-Registration-Financials categories, 82 articles): https://helpme.teamsnap.com/ (cross-referenced, not fetched this pass)
- Sibling research consulted for boundary alignment: research/sports-club-management.md, research/sports-eligibility-management.md, research/sports-federation-management.md, research/sports-membership-licensing-platform.md, research/sports-meet-management.md, research/sports-academy-management.md, research/event-registration-platform.md, STATUS.md boundary entries

Source-access limitations:

- SportsEngine (major NGB-side registration vendor, Stack Sports family) returned 403 on both attempts (help.sportsengine.com, sportsengine.com). No SportsEngine-specific claims are made anywhere.
- FinalForms' fetched pages do not surface a fee/payment leg for athletic registration; no claim is made in either direction about FinalForms payment machinery.
- All sampled products are US-market. Regional registration platforms (AU/UK/NZ governing-body stacks) were not sampled; assertions kept implementation-neutral.
- TeamSnap evidence is Tier-1 but cross-referenced from the sibling pass of the same date rather than fetched here; used only for machinery commonality, not for product-specific claims.

## Product Observations

### LeagueApps — evidence layer A (product/feature pages) + Tier 1 (help center)

- Self-label (root): "The Best Youth Sports Management Software … Power your registration, payments, communications, scheduling, reporting, facilities, and website design to more effectively run your clubs, camps, tournaments, and leagues."
- Registration feature page: "A winning online registration flow for your youth sports organization makes it easy for your members to sign up…"; registration configurable per program kind — Clubs, Lessons, Tournaments, Leagues, Camps, Classes, Tryouts, Fundraisers (tabbed selector).
- Payments in-flow: auto-pay at registration, stored credit cards, customized payment plans; "spend more time doing what you love, not chasing down what you're owed."
- Capacity: "automatic waitlists and capacity limits at the program level so you won't miss registrations even when your capacity is reached."
- Signup-attached commerce/attachments: ecommerce, donations, compliance management, registration fee insurance integrated into the signup flow.
- Data posture: "You can power your members' data via registrations; it will never be sold or shared."
- Testimonial evidence of registration-first usage: tryout registration ("gather everything we need at registration"); "set up and launch new programs in under five minutes" (Total Package Hockey case study).
- Help center taxonomy (Tier 1): Program Registration, Member Management ("Manage member registration and information, and family accounts"), Payment Collection, Team Management ("copy and move players and teams"), Communication, Reporting ("registration stats, payment activity"), Schedules & Standings, Ecommerce, Content & Marketing Tools, Facilities, Mobile Apps.
- Program model (Tier 1, Program Creation article): seven program types — Club, League, Event, Tournament, Camp, Classes, Bookings. Configurations: **classic** (single program accepting Staff, Individual, Team, or Team Player registrations), **grouped** (one master program with sub-programs — "a good choice when dealing with multiple age groups, skills levels, locations, divisions"), **session-based** (registrant selects one or multiple sessions in a single registration, pays all at once).
- Program criteria (Tier 1): **League Type** — "Youth/Family Accounts" ("Parents or Staff Members registering child players") vs "Adult" ("Adults registering themselves as players"); site mode switchable between them; **Sport**, **Season**, **Level**, **Gender** (Season/Level customizable via site terminology settings); **Visibility** — Public (shows on registration listings pages) vs Private (direct link or invitation only).
- Program dates (Tier 1): **Activity Start/End Date** (when the program runs — start required) distinct from **Registration Start/End** (when signup opens/closes; blank = immediately open / open indefinitely; open 12:00 AM start date, close 11:59 PM end date, site time zone).
- Registration status state machine (Tier 1, admin-controlled on top of automatic date behavior): Open Soon → Open; Sold Out (button becomes "At Capacity"; team-player link may remain); Limited Spots; Accepting Waitlist; Accepting Free Agents Only (gender variants); Accepting Team Captains Only / Team Players Only / Team Players and Free Agents Only (adult programming — "lock the number of teams… but still want team players and free agents to join"); Cancelled. Labels render on the public program listings.
- Related Tier-1 articles: program divisions, session-based programs, classes ("register for multiple 'classes' at once"), tryouts, "How To Renew Your Programming", copy program, cancel/delete program, password-protected programs, small-group registration, run a test registration.
- Registrant types: Staff, Individual, Team, Team Player; Free Agents (adult pole).

### Jersey Watch — evidence layer A (feature page, rich)

- Self-label: "Simple & Fast Online Sports Registration Software — Register Players & Manage Payments, Faster than Ever. Set up player registration forms and collect payments for your sports league, club, or teams. Trusted by over 2,800 organizations to register over 1 million athletes."
- Form building: custom questions to collect player information; waivers/codes of conduct/acknowledgments embedded in the form and required during registration; required document uploads during registration ("player photos, age verification, or proof of address").
- Money machinery: family & multi-player/multi-event discounts (automatic); discount codes; payment plans ("pay over a period of time… automatic installments"); donations during registration; item sales during registration; full or partial refunds "with a few clicks".
- Player management: "Sort players during and after registration by name, age, division, or any other criteria"; contact info (names, emails, mobile numbers) "automatically collected and stored during registration"; bulk messages via communication tools; export all participant data to spreadsheets "so you can share with volunteers and coaches".
- Team registrations: "Collect fees from teams registering for tournaments. Sort registrants by team name, division, and coaching info."
- Mobile: "Registration forms are accessible from any device so players can easily register and pay from their phone."
- FAQ (vendor's own articulation of the Type): "Sports league registration software allows you to create player registration forms for your organization. You can register all of your athletes and collect payments online. Most league registration software also allows you to manage players during and after registration by searching, exporting data to spreadsheets, and creating teams." Volunteer-led orgs need fast form building. Multiple age divisions and skill levels supported; "no limit to the amount of programs you can create"; per-age-group form and pricing customization.
- Registration embedded in the org's website: "Registrants can click on a registration module on your website homepage, complete their registration form with payment, and submit."
- Audience set (footer): Youth Sports, Rec Leagues, Club Programs, Sports Camps, High School Teams, Travel Teams. Background Checks offered as a separate feature. Compare pages position it against Sports Connect, SportsEngine, LeagueApps, TeamSnap, TeamLinkt, Crossbar, LeagueLineup, PlayMetrics.

### FinalForms — evidence layer A (product home + athletic registration page)

- Self-label: "School Registration, Compliance & Safety Software… FinalForms isn't a forms software. It's the system of record for compliance, communication, and safety." K-12 audience: enrollment/back-to-school registration, athletic management, staff forms, parent communication, emergency medical, state/district compliance. "Trusted by 3,000+ schools" / "10,000+ Schools Nationwide" (both figures on-site; treated as positioning).
- Athletic Forms & Registration page: "FinalForms eliminates paperwork and confusion from athlete registration by guiding families through a mobile-friendly process and giving athletic departments full visibility into what's signed, what's missing, and who's cleared. From sport-specific packets to emergency contacts and physicals, FinalForms handles it all."
- Staff-side configuration: **Sport-Specific Form Packs** ("Assign different forms for each sport, including waivers, handbooks, physicals, and acknowledgments"); forms configurable "by sport, season, or level"; **Auto-Filled Returning Info** ("Carry forward data year to year, allowing families to skip re-entering the same details each season"); **Digital Signatures & Document Storage** ("parents, athletes, and staff… full audit trails and form version control"); **Emergency Contact Management** ("Centralize up-to-date medical and contact info linked directly to athlete rosters").
- Stakeholder surfaces: parents/athletes — one workflow for all required forms, real-time validation, automated reminders; coaches — "instantly view which athletes are registered, cleared, or flagged for missing info… everything is time-stamped and permissioned"; athletic directors — "track form completion by team or building… accurate, time-stamped records."
- FAQs: unique form packets "for every sport, level, and season"; returning families review/update pre-filled data; physicals, emergency contacts, and medical alerts integrated into the registration workflow; coaches get "real-time clearance dashboards with visibility into form status and medical flags"; signatures "legally binding, time-stamped, and securely stored for audit."
- Payment machinery: NOT surfaced on the fetched athletic registration or home pages. No claim made either way.
- The eligibility/clearance layer is sold as a separate named pillar ("Athlete Eligibility & Clearance — track forms, clearance, and return-to-play in real time") — the registration pillar collects; the clearance pillar gates.

### Sports Connect (Stack Sports) — evidence layer A (product home)

- Self-label: "SPORTS MADE EASY — Websites, Registration, Youth Sports Management Tools, & More!" Feature list: Mobile First Registration, Professional Websites, Payment Processing, Team Management, Reporting, Scheduling, Communication Tools, Premium Support, Online Fan Wear, Safety & Compliance.
- Who we serve (three-tier structure): **National & State Governing Bodies** ("National, Regional, and State associations can manage their governing body like never before"); **Local Clubs & Leagues** ("Online Registration, payments, and management tools to help local sports leagues run more efficiently"); **Parents, Coaches, & Athletes** (consumer-facing side).
- Sport verticals with governing-body integration: "Official partner of US Youth Soccer and U.S. Soccer with **integrations to the USSF National Data Center**"; USA Football and Pop Warner; Little League Baseball and PONY ("pitch count tracking"); AAU; US Lacrosse ("easy scheduling and automated team creation").
- Testimonials: "easily manage hundreds of registrations year after year, including all the pains that come with a youth sports program"; "we run multiple registrations for our regular season, camps, and fundraisers all at the same time."
- Market-structure note (banner): "Sports Connect & PlayMetrics: A new era for youth sports!" — consolidation recorded as L3 context.
- The governing-body page's existence documents the drift seam the federation pass named: the same registration machinery is sold into governing bodies, where adding the organization register + authority instruments crosses into Sports Federation Management.

### TeamSnap (cross-referenced from the sibling sports-club pass, same date) — Tier 1 category evidence

- Registration machinery inventory (Clubs & Leagues help-center categories, 82 articles, recorded 2026-09-09 in research/sports-club-management.md): creating a registration form; fees and advanced fee adjustments; payment methods; documents and waivers; form field customization; installment plans; org-issued invoices; invoice management; refunds; registration discounts; multi-child registration discounts; capacity limits and waitlists; delete/cancel a registration entry; recording cash/check/offline payments; payment disputes; merchant account guide.
- Structure context from the same pass: registration happens at the season level ("allowing you to focus forms on the needs of that specific program"); forms duplicated within a season and copied to the next season; Program > Season > Division > Team > Participant hierarchy.

## Cross-product Comparison

| Structure / capability | LeagueApps | Jersey Watch | FinalForms | Sports Connect | TeamSnap (x-ref) | Layer |
|---|---|---|---|---|---|---|
| Program/season as the sign-up offer with open/closed state | ✓ (program types; reg start/end vs activity dates; status machine) | ✓ (programs per age group/division) | ✓ (form packets "by sport, season, or level") | ✓ (registrations per season/camp/fundraiser) | ✓ (season-level registration) | B |
| Participation structure on the offer (divisions/levels/age groups, sport, gender) | ✓ (Season/Level/Gender attributes; grouped sub-programs; divisions article) | ✓ (sort by age/division; per-age-group pricing) | ✓ (sport/season/level) | ✓ (sport verticals; automated team creation) | ✓ (program attributes: age divisions, genders, levels) | B |
| Platform-run signup flow producing a persistent registration record | ✓ (listings page → Register button → flow) | ✓ (form + payment, embeddable on website) | ✓ (guided family workflow) | ✓ (mobile-first registration) | ✓ (registration forms) | B |
| Guardian/family-linked registration for minors | ✓ (Youth/Family Accounts mode; family accounts category) | ✓ ("parents" upload docs; family discounts) | ✓ (families; parent+athlete signatures) | ✓ (parents/coaches/athletes surface) | ✓ (multi-child discounts) | B — dominant realization; adult self-registration also first-class (LeagueApps Adult mode) |
| Custom questions / form fields | ✓ | ✓ | ✓ (form packets per sport) | ✓ (implied by registration tooling) | ✓ (form field customization) | B |
| Waivers/signatures collected at signup | ✓ (default waivers; password-protect; docs) | ✓ (waivers, codes of conduct, acknowledgments) | ✓ (signatures, audit trails, version control) | ✓ (safety & compliance tools) | ✓ (documents and waivers) | B |
| Requirement documents at signup (photos, age verification, physicals) | ✓ (member profile fields; docs) | ✓ (uploads: photos, age verification, proof of address) | ✓ (physicals, emergency contacts, medical alerts) | ✓ (safety & compliance) | ✓ (documents) | B |
| Fee collection in-flow (plans, discounts, refunds) | ✓ (auto-pay, plans, stored cards) | ✓ (plans, discounts, donations, merch, refunds) | not surfaced on fetched pages | ✓ (payment processing) | ✓ (fees, installments, refunds, offline recording) | B — common, deeply integrated; NOT definitional (FinalForms pole runs the same transaction on forms/status; offline payment recording documented) |
| Capacity/waitlists | ✓ (program-level; At Capacity/Waitlist statuses) | not surfaced | n/e | n/e | ✓ (capacity limits and waitlists) | B — 2 of 5 at Tier-1/A depth; common |
| Offer status machinery (open/sold out/waitlist/cancelled) | ✓ (richest: full status list) | implied | ✓ (completion/clearance status tracking) | n/e | implied (cancel/delete registration entry) | B at LeagueApps depth; status visibility common |
| Registered roster as working record (search/sort/filter, edit/cancel/refund) | ✓ (Member Management; program dashboard) | ✓ (sort/manage players; refunds) | ✓ (form completion by team/building) | ✓ (registration management implied) | ✓ (cancel entry, refunds) | B |
| Communication to registrants | ✓ (communication category) | ✓ (bulk messages) | ✓ (automated reminders; email/text by status) | ✓ (communication tools) | ✓ (org-wide comms) | B |
| Export / handoff (spreadsheets, teams) | ✓ (Team Management: copy/move players; reporting) | ✓ (exports to share with volunteers/coaches) | ✓ (linked to athlete rosters; SIS integration) | ✓ (team management; NGB data center integrations) | ✓ (roster building) | B |
| Season renewal/rollover | ✓ ("How To Renew Your Programming"; copy program) | n/e | ✓ (auto-filled returning info, carry forward year to year) | n/e | ✓ (copy forms to next season) | B — common-mature |
| Websites as the registration storefront | ✓ (Youth Sports Websites; public/private listings) | ✓ (registration module on website) | n/e (school portals) | ✓ (professional websites) | ✓ (website builder) | B — common, optional |
| Bundled season operations (scheduling, teams, standings) | ✓ (scheduling/standings categories — bundled) | ✓ (scheduling feature; light) | n/e (dept suite) | ✓ (team management, scheduling) | ✓ (full bundling) | B — bundled-neighboring capability, NOT definitional |
| Governing-body data flow | n/e | n/e | n/e (state association compliance instead) | ✓ (USSF National Data Center integrations; NGB audience) | n/e | A — variant (Sports Connect only) |

Reading: (1) all five products realize the same three-part core — the org's program/season offer held in the platform, the platform-run signup transaction producing a persistent registration record, and the registered roster as the working record; (2) the participation structure (season/division/level/age/gender, sport) is on the offer everywhere — this is what separates the Type from generic event intake; (3) money is universal in the youth/club poles but the school pole runs the same transaction on forms/status/signatures; (4) everything around the core (websites, teams, scheduling, communication, compliance, NGB flows) is bundled capability that other Types own as their centers.

## L0 — Defining Invariant

Three jointly-held structures. Each is stated with its removal test:

1. **The organization's participation offer held in the platform.** The sports organization defines what people sign up INTO — a program of participation in the organization's season structure (by sport, season, age/skill division/level, commonly gender; youth-family vs adult registrant modes; public listing or private/invited access) — and the platform holds it as the registration target with live open/closed state and distinct registration vs activity windows. Remove → a catalog of links, or the offer collapses into a dated event occurrence (Event Registration territory) or a bare form (form builder).
2. **The platform-run signup transaction producing the registration record.** The platform itself runs the intake — the registrant (or their guardian) steps through the platform's own flow: participant data, custom questions, waivers/signatures, requirement documents, commonly fee payment — and the result is a persistent registration record binding the person to the offer. Remove → link-out to forms elsewhere; the platform is a billboard.
3. **The registered roster as the season's working record.** Registration records accumulate into participant lists the organization works in the same system — search/sort/filter by division/age/status, edit/cancel/refund, communicate to registrants, export for coaches/volunteers, hand off toward teams. Remove → a response pile or a payment processor's transaction log.

Jointly-held load-bearing: 1 alone = a program catalog/listing; 2 without 1 = a form tool; 3 without 1+2 = a spreadsheet; 1+2 without 3 = intake with no working record; 2+3 without 1 = generic form-and-list; 1+3 without 2 = paper-forms era practiced with software labels. The three legs together are the Type; the same legs describe the paper-era registrar (registration night, mail-in form, ledger sorted into teams) — the historical check passes with zero modern machinery.

## L1 — Common Mature Structure

Present across the sample, expected by the market, not required to recognize the Type:

- fee collection integrated into the flow (payment plans, stored cards, discounts incl. family/multi-player, refunds, donation/merch add-ons at signup)
- custom form fields and per-program (per-age-group/per-sport) form variants
- waivers, acknowledgments, digital signatures with audit posture
- requirement documents collected at signup (photos, age verification, proof of address, physicals)
- capacity limits and waitlists
- registrant communication (bulk email/SMS, automated reminders)
- export/reporting (registration stats, spreadsheets for coaches/volunteers)
- season renewal/rollover (copy program, auto-filled returning data)
- website/storefront embedding of the registration listings
- roster handoff toward teams (copy/move players, team creation)

## L2 — Variant / Optional Structure

- guardian/family account machinery as the dominant realization vs adult self-registration (both first-class; site-mode configurable in one sampled product)
- offer status depth (a full admin-controlled status machine in one product vs simple open/closed elsewhere)
- free/feeless or offline-payment registrations (recording cash/check documented; the school pole emphasizes forms/status over money)
- NGB/governing-body data flows (national data center integrations — one sampled product; state-association compliance posture in the school pole)
- bundled season operations (scheduling, standings, team management) — present in suite-form products
- attached commerce (ecommerce, fan wear, fundraising, registration-fee insurance, background checks)
- websites, mobile apps, and parent-facing season apps as bundled surfaces
- camp/class/tournament/tryout program types — one platform's own taxonomy of offer shapes

## L3 — Vendor-specific (Research Notes only)

- LeagueApps: seven named program types (Club/League/Event/Tournament/Camp/Classes/Bookings); classic/grouped/session-based configurations; the full registration-status list (Open Soon/Open/Sold Out/Limited Spots/Accepting Waitlist/Free-Agent variants/Team Captain/Team Player variants/Cancelled); site terminology settings for Season/Level; test registration; "How To Renew Your Programming"; FundPlay/PLAYS advocacy; MLB & MiLB Clubs support category; Elite Academy League member support.
- Jersey Watch: "2,800+ organizations / 1 million athletes" claims; compare-page set; schedule generator and registration fee calculator tools; product roadmap page.
- FinalForms: NFHS/NIAAA/state-association partnerships; E-Cards (real-time team-synced medical info); SIS integrations (PowerSchool/Infinite Campus/Skyward); "3,000+ schools" vs "10,000+ schools" figures both on-site; 98% athletic compliance / 99.7% retention claims.
- Sports Connect: Blue Sombrero lineage (Capterra listing still under the old name); PlayMetrics merger banner; USSF National Data Center integration; pitch count tracking (Little League/PONY); Stack Sports privacy/legal stack.
- TeamSnap: season-level bank accounts driving financial reporting; program structure example names including "Academy"; org-issued invoices; disputes machinery.

## Vendor-specific Findings

See L3. None of these enter the canonical core. The only cross-vendor structural note worth keeping: suite-form vendors (LeagueApps, Sports Connect, TeamSnap) bundle the neighboring season operations, while single-pillar vendors (Jersey Watch at the small-org pole) push roster work out through exports — both realizations satisfy the core.

## Boundary Findings

**vs Event Registration Platform (§26, processed).** The shared machinery is real (offer → intake → roster); the seam is the offer's semantics. Event registration centers a dated occurrence set (an event happens, attendees come); sports registration centers a participation offer in the organization's season structure (the participant joins a season/division/team framework that plays out over weeks). Bundling is documented inside one product (LeagueApps ships "Event" as one of seven program types with the same basic functionality — the vocabulary, not the machinery, changes). Directional test: strip the season/division/participation semantics → event registration; add event-day occurrence machinery (agendas, session attendance) as the center → event registration. Keep-both.

**vs Youth Sports Management (unprocessed — flag from the sports-club pass).** The club pass proposed the center-of-gravity discriminator: youth sports orgs are "registration/season-led" vs clubs "membership/competition-led". From this side: the registration platform's memory is the registration record and the roster output; the youth-sports organization system's memory is the organization itself (its seasons, teams, volunteers, schedule, communication life) with registration as its busiest single step. Same products serve both poles (Jersey Watch's "who we serve" spans six org labels; Sports Connect serves governing bodies to parents). Directional test: strip the org's year-round operation machinery (schedules, teams, volunteer coordination, website-as-presence) → this Type; make the organization's own operation the center → Youth Sports Management. Joint review recommended at that pass.

**vs Sports Club Management (processed — flag left by that pass: "one-shot registration transactions vs the ongoing club relationship").** Ratified from this side. The club's center is the standing member organization (member records with renewal standing, teams, seasons, dues year over year); the registration platform's center is the signup transaction machinery that any sports organization runs per program/season. Club suites embed registration as one step (TeamSnap ONE's Registration & Payments pillar; Spond Club's registration forms). Directional test: remove member standing/teams/dues → registration platform; add the member organization as the center → club. Keep-both.

**vs Sports Academy Management (processed — flag from that pass: "one-shot registration transactions vs the ongoing academy relationship").** Held. The academy's center is the tuition-bearing program portfolio (classes/lessons/camps with rosters, sessions, recurring billing); the registration platform's center is the intake transaction. The seam surfaces inside products: LeagueApps' "Classes" program type ("register for multiple classes at once") is the academy-shaped offer realized as one registration program type — a capability slice, not a center change.

**vs Sports Eligibility Management (processed — flag from that pass: "signup transaction feeds the gate").** Ratified from this side. Registration collects; eligibility gates standing status computed from collected evidence over time. Requirement documents at signup (physicals, age verification) are inputs the transaction gathers; the managed, decaying, gate-serving status is the sibling Type's center. FinalForms itself sells the two as separate named pillars (Athletic Forms & Registration vs Athlete Eligibility & Clearance) — vendor-side corroboration of the seam. US Club Soccer's pattern (registration purchase as one requirement among several) recorded from that side. Directional test: remove the standing gate → this Type.

**vs Sports Membership / Licensing Platform (processed — flag from that pass: "standing renewable relationship + credential vs one-off signup transaction").** Ratified from this side. The membership Type centers the purchasable, renewable, rights-carrying relationship; registration centers the signup transaction. Season renewal/rollover in registration platforms (copy program, auto-filled data) is season-over-season intake convenience, not a standing member relationship with a credential. USA Hockey's two-stage pattern (national registration purchase → local processing) acknowledged from that side as the seam inside one system.

**vs Sports Federation Management (processed — flag from that pass: "registration = one transaction feeding the register").** Ratified from this side. The federation's center is the governance register (member organizations + affiliation + authority instruments); registration is the transaction that feeds participant records. The drift is real and vendor-documented: Sports Connect sells the same registration machinery into "National & State Governing Bodies" — when the product adds the organization register and authority instruments, it crosses into federation territory. Directional test confirmed from this side.

**vs Sports Meet Management (processed — flag from that pass: "entry collection is one step inside the meet loop bound to the event program; registration platform has no program/results record").** Ratified. Registration platforms hold no event program, entries-with-seed-marks, or results record; meet platforms hold no season-long program catalog. Bundling expected (tournament program types; race platforms in §26).

**vs League Management Platform (processed — flag from that pass: "capability-first siblings whose job is one step of the league season loop").** Held from this side. The league platform owns the recurring competition cycle (programme → fixtures → results → standings); registration owns the season's intake. Suite products bundle both (LeagueApps' Schedules & Standings categories; Sports Connect's scheduling) — the registration center stands independent of the competition loop.

**vs Team Management Application (unprocessed).** Flag left for that pass. After registration, team life (rosters, availability, chat, game logistics) is the team app's center; registration hands off — Jersey Watch's own framing ("export… to share with volunteers and coaches") documents the handoff as an export edge, and suite products pull team management in as a module.

**vs Sports Scheduling Platform (unprocessed).** Flag left for that pass. Scheduling (fixtures, practices, facilities) is bundled capability inside registration suites (LeagueApps, Sports Connect); the registration transaction does not arrange time.

**vs Online Form Builder (§03.11, processed).** Same pattern that pass held vs event registration: form machinery subordinated to a participation offer + roster output. A form builder has no program catalog, no season structure, no fee-per-program machinery as its center.

**vs Course Registration System (§23) / Camp Management System (§26).** Vocabulary collision only. Course registration enrolls students into academic sections; camp management centers the camp session operation. Sports registration platforms ship camp/class as program types (capability slices); the centers differ. Consistent with those passes' recorded boundaries.

**vs School / College Athletics Management (processed — that pass named "standalone eligibility/registration tool = Sports Eligibility/Registration territory" as the removal outcome).** Held from this side. The department system centers the program portfolio + participation gate + authority loop; FinalForms' athletic registration pillar is the intake transaction within that suite, and the same vendor's registration pillar sold standalone would be this Type. The school pole documents that the registration transaction does not require the club/league commercial shape.

## Uncertainties

- SportsEngine unreachable (403 ×2). The NGB-side enterprise pole is evidenced only indirectly (Sports Connect's governing-body page; the federation/membership passes' observations). No SportsEngine claims made.
- FinalForms payment machinery not evidenced on fetched pages — the "money is common-not-definitional" finding rests on (a) the school pole's forms/status emphasis and (b) offline-payment recording at TeamSnap; it is NOT claimed that any sampled product lacks payment support.
- Volunteer-signup machinery (roles, background-check gating at signup) was not directly documented as a registration flow in the sample (background checks appear as adjacent features; exports-to-volunteers observed). Not included in any tier above L1; not asserted.
- Whether any registration platform supports join-link-only intake with no form was not verified; not asserted.
- Regional (non-US) registration products unsampled; the historical check covers the pre-digital era, and the adult-vs-youth modes cover the audience axis, but regional variant depth is unverified.
- Capacity/waitlist evidence is deep at two products (LeagueApps Tier 1, TeamSnap Tier-1 category) and absent from the others' fetched pages — held common, not universal.

## Historical / Market-Sample Check

Paper-era realization: the registration night at the community hall / the mail-in form — the league advertises its season's divisions (the offer), the parent completes the paper form and writes a check (the transaction), the registrar's ledger of registered players is sorted into teams and consulted all season (the working record). All three L0 legs hold with zero modern machinery. School athletics: the packet of consent/physical forms returned to the athletic director's office and the clearance list posted by the gym door. Regional/platform-native: a state association running its own registration portal satisfies the legs without any bundled suite. The definition therefore does not depend on online payment, websites, mobile apps, or NGB integrations.

## Final Synthesis

A Sports Registration Platform is the sports organization's intake machinery: it holds the organization's participation offer — programs defined by sport, season, age/skill division, and commonly gender, offered publicly or by invitation, with distinct registration and activity windows and live open/closed state; it runs the signup transaction itself — the participant (or their guardian, in the market's dominant youth realization) completes the platform's flow of participant data, custom questions, waivers/signatures, and requirement documents, commonly paying fees in-flow; and it turns the completed signups into the registered roster the organization works on for the season — searchable, editable, refundable, communicable, exportable lists that hand off toward teams. Around that core, mature products add integrated fee machinery (plans, discounts, refunds), capacity/waitlists, season renewal with auto-filled returning data, website storefronts, registrant communication, reporting, and bundled season operations (teams, scheduling, compliance). The Type's boundaries do the heavy lifting: the event's dated occurrence, the club's standing member relationship, the academy's tuition portfolio, the eligibility gate, the membership credential, the federation register, the meet's event program, and the league's competition loop are all different centers that registration feeds or feeds on — and every one of those sibling passes independently located this Type as "the signup transaction" on the other side of their seam.
