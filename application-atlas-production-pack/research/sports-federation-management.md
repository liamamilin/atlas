# Research Notes — Sports Federation Management

Research date: 2026-09-09

## Research Goal

Understand what Sports Federation Management software actually is from real products: what objects exist inside a governing body's system (member organizations, registered participants, sanctioned competitions, discipline/clearance records), who operates it, how the affiliation and registration cycles actually run, how multi-level (national → regional → local) structures share one system, and where its boundary lies against the neighboring §28 leaves (League Management Platform, Sports Club Management, Referee Management Platform, Sports Eligibility Management, Sports Registration Platform, Sports Membership / Licensing Platform) and against §25 Association Management.

## Initial Boundary

A sports federation (national governing body / NGB, state or regional association, continental confederation, peak body) governs a sport across many subordinate organizations: affiliated clubs, leagues, districts, schools. Its administrative burden is qualitatively different from a club's or a league's:

- it maintains relationships with **other organizations** (affiliation), not just with individuals;
- it registers **participants across the whole sport** (players, coaches, officials), usually with unique identifiers;
- it exercises **authority instruments**: sanctioning competitions, certifying coaches/officials, clearing participants (background checks/safeguarding), disciplining misconduct;
- it reports **outward** to funders, governments, and confederations.

Temporary hypothesis: the Type is the governing body's administrative system of record over its member organizations and registered participants.

Easily confused neighbors: League Management Platform (one competition body's season), Sports Club Management (one member organization), Association Management System §25 (generic membership org), Sports Registration Platform (intake transaction), Sports Eligibility Management (participant status machinery), Referee Management Platform (officials assigning), Sports Membership / Licensing Platform (membership/licensing as the whole job).

Vocabulary note: the market says "governing body", "NGB", "state association", "peak body", "federation", "confederation" for the same customer position. The directory leaf uses "federation"; the researched products use all of these labels. Treated as one customer position.

## Research Questions

1. What objects exist inside a federation platform? (member organizations, participants, competitions, credentials, cases, fees)
2. Who operates it, and what roles exist? (federation staff, regional admins, delegated club admins, participants themselves)
3. How does the affiliation cycle work? (application/renewal, approval, fees, status)
4. How does participant registration work, and how does it cascade across hierarchy levels?
5. How does sanctioning work? (request → terms → review/approve → membership enforcement)
6. What compliance machinery exists? (certifications, background checks, safeguarding, discipline, policy acceptance, audit)
7. How do hierarchy levels share one database, and how are multi-level fees handled?
8. What does the federation report outward, and to whom?
9. Where is the boundary vs league platforms, club systems, registration platforms, eligibility machinery, and generic association management?

## Representative Products

Selected for market position + documentation quality + different product philosophies + different geographies/sports:

1. **Sport:80** (UK/US) — NGB-first commercial platform; 90+ national governing bodies (USA Track & Field, USA Cycling, USA Archery, USA Water Polo, USA Judo, Boxing Ireland…). Philosophy: membership + certification + governance as the center; competitions as events/bolt-ons.
2. **GotSport / GotSoccer** (US) — soccer-specific association platform; US Youth Soccer state associations, US Club Soccer, CBF (Brazil), Concacaf, Conmebol. Philosophy: registration + compliance + referee machinery for associations.
3. **SportyHQ** (global) — racquet-sport competition platform with an explicit governing-body solution; Squash Australia, Tennis South Africa, UAE Badminton, Scottish Squash. Philosophy: competitions/rankings first, governance layer (sanctioning, hierarchy fees) on top.
4. **RevolutioniseSPORT** (Australia) — peak-body platform; 260 governing bodies, 18,000 local clubs (Netball NSW, Australian Sailing, Athletics Australia, Hockey Australia…). Philosophy: whole-of-organization suite (memberships, finances, governance records, competitions) sold to peak bodies and clubs alike.

Market observation (not sampled): Demosphere, a classic US governing-body platform, has been absorbed into OTTO SPORT AI (demosphere.com now serves OTTO's club/league/tournament products) — the federation-first vendor landscape consolidates into suites that also serve clubs and leagues.

## Sources

All fetched 2026-09-09. Tier 1/2 official pages.

- Sport:80 — homepage, /platform, /features/membership-management, /features/compliance-management (sport80.com)
- GotSport — home.gotsport.com homepage, /governing-body-solution/
- SportyHQ — homepage, /solutions/governing-bodies, /features/membership-management, /features/rankings-and-sanctioning
- RevolutioniseSPORT — homepage, /platform-features
- OTTO SPORT AI — demosphere.com (redirect target), otto pages via redirect

Sourcing limitations: no vendor help-center article pages were fetched (product/feature pages only); GotSport support portal (support.gotsport.com) not fetched; RevolutioniseSPORT help center not fetched. Operational details below are therefore calibrated to what product pages state; no numeric limits, default values, or time windows are asserted.

## Product Observations

### Sport:80

Evidence layer: A (direct, official product/feature pages).

- Positioning: "The Sport:80 Platform enables sport organizations to unlock the power and value of their communities"; "trusted by 80+ NGBs and sports organizations"; customers are "international or national governing body, a sports membership organization or community sports organization".
- Core features: Membership Management, Certification Management, Event Registration, CRM & Contact Management, Data Management & Reporting, Coaches & Workforce, Governance & Compliance, Marketing & Communications, Customer Support Center, Payments & Finance, Donations, Data Security, Third-Party Integrations.
- Membership across the pyramid: "Seamless Member Management Across Your Entire Pyramid" — "Individuals can effortlessly purchase their Governing Body and club memberships, whereas clubs, leagues, colleges, and other affiliated bodies can efficiently manage their affiliation, allowing you to grow your membership on a single platform." "3-in-1 membership (club, affiliated body, and governing body)". Multiple membership tiers, configurable data collection, intelligent forms, waivers and consents, digital membership cards (mobile wallets), automated renewal reminders, member portal, cross-sell/upsell.
- Member portal: members "manage their sporting profiles, renew memberships, update qualifications, enter competitions, and track results".
- Governance & Compliance: "Certification requirements are configured at NGB level, with each member's status visible in one place. Automated alerts fire before expiry dates are reached, and configurable rules determine what happens when a certification lapses: restricted access, administrator notifications, or a flagged record for review." Compliance reports cover "membership, event participation, credential status, and policy acceptance" as "the evidence trail needed to demonstrate compliance to funding organizations and external regulators". "Every action taken within the Platform is recorded in a detailed audit log: who actioned what, when, and what the outcome was."
- Safeguarding: integrates with the U.S. Center for SafeSport and NCSI; background checks tracked against member records; automated renewal alerts; "configurable rules determine what happens when a clearance expires".
- Disciplinary case management: "log and manage disciplinary cases linked directly to individual member records via an integrated case management tool"; every case has a full activity log.
- Policy acceptance: "Capture and store records of members and officials accepting your NGB's policies and codes of conduct."
- Data protection: consent recorded at registration, role-based access controls, subject-access/removal tooling, logged data actions.
- Bolt-on Club Management: "An innovative solution designed to support grassroots organizations" — the club layer is a separate product the federation platform connects to.
- Case study: USA Track & Field — services to 120,000+ members.

### GotSport

Evidence layer: A (direct, official product pages).

- Positioning: "The ultimate sports management platform offering powerful solutions for every level of sports. We have tools for Players and Teams all the way up to Governing Bodies and Professional Leagues."
- Governing Body Solution: "Manage every aspect of your sport in one simple-to-use place"; "Our software is packed with tools built with the end user in mind, helping your members get the most out of the sports you offer"; "can accommodate all membership models".
- Client wall: US Youth Soccer and ~30 state youth soccer associations; US Club Soccer; CBF (Brazil); Concacaf; Conmebol; USL; Girls Academy.
- Governing-body tools:
  - Registration: customizable online form, mobile responsive, register multiple children from a single parent account, digital waivers & e-signatures, "Track & view members' registration status".
  - Communication: "Connect with all your members", dynamic contact lists updating in real time, custom mailing lists, newsletters.
  - Background Checks & Compliance: "Integrated Risk Management Qualification system (API to JDP, SafeSport, CDC, & Learning Center)", upload certification, "Track members' background status", "Only allow certified members on rosters", safety training.
  - Referee Management: game official registrations, "Track ref credentials, availability and preference", "Integrate ref assignments with your competitions schedule", calendar integrations, auto game change notifications.
  - Financial: track & reconcile payments, custom payment plans, discount codes/vouchers, full & partial refunds.
  - Data Analytics: dashboard, visual analytics, "Contrast your membership with Census Bureau data", trends.
- Sibling products sold separately: Club Management, Competition Solution, Referee Solution, Team App, Ticketing, Website Builder, GotSport Live — the governing body solution is one suite member among many.

### SportyHQ

Evidence layer: A (direct, official product pages).

- Positioning: "Competition and membership management for clubs and governing bodies"; "a web platform built to power sports facilities and governing bodies, run competitions, manage membership and so much more."
- Governing bodies solution page — the richest single source on federation semantics:
  - CRM: "add your players, coaches, officials and other contacts"; unlimited custom data fields; search/view/export/email.
  - Membership & affiliation: "SportyHQ recognizes the relationship between governing bodies and facilities within their region… we make it easy to automatically sync membership information from facilities or other governing bodies within your region to your contacts"; "easy for facility administrators to affiliate their members with you using our bulk renewal membership tools."
  - Hierarchy: "SportyHQ recognises the multiple levels of organizations that exist in sports management. From international to national, regional and local, SportyHQ's platform will allow you to create and support this structure. SportyHQ then lets you easily recognise a user's relationship within that hierarchy to do things such as collect sanctioning and membership fees at each level."
  - Multi-level money: "if you are a national organization with regional associations throughout your country, SportyHQ can collect regional, national and event fees all in a single transaction, and then disperse that payment automatically to the appropriate recipients."
  - Sanctioning: "The entire event sanctioning process can be handled through the SportyHQ platform. From an event organizer requesting sanctioning and agreeing to your sanctioning terms, through to you reviewing and approving the request. If a sanctioned event then requires its participants to hold an active membership with your governing body, SportyHQ is able to check and add on any applicable membership fees. There's also the option of a guest fee in instances where you allow non-members to participate."
  - Rankings: out-of-the-box algorithm or bring-your-own points tables; ranking lists auto-grouped by affiliations ("a new member of a governing body is added to its rankings"); criteria include membership status (active members only).
  - Code violation management: "Setup all of your code violation offenses and point levels. Event officials are able to directly create code violation cases. If appeals are allowed, that entire process can be managed… Any applicable suspension points can be applied and enforced."
  - User agreements: track who has seen/accepted; auto-accept option after a set number of days.
  - Website builder with hierarchy-aware content sharing between levels' sites.
  - Translation support; API.
- Membership feature page: players (contact info, **affiliation status**, membership type, playing privileges), coaches (credentials, qualifications, accreditation history, public coach directory), officials (qualifications, accreditation status, assignment to events/matches), external contacts; member self-service login; auto-issued membership IDs; **membership syncing cascade**: "if a club automatically affiliates its members to its regional body, which then affiliates those members to its national body, SportyHQ can automate that entire process, growing membership numbers at each level"; payment plans (auto-recurring or fixed-date periods; "As soon as your members complete payment, their membership status automatically updates"); analytics (demographics, location, membership length, activity).
- CEO quotes: Squash Australia ("go from many systems to one", member database +40%); Tennis South Africa (rankings automation).

### RevolutioniseSPORT

Evidence layer: A (direct, official product pages).

- Positioning: "online management platform for sports of all shapes and sizes"; counters: "260 governing bodies", "18,000 local clubs".
- Audience selector: "local club or association / state or national sport / industry body" — one platform, three customer positions.
- Peak-body pitch: "As a peak sporting body, you need all the information, here and now. Imagine having all your members and organisations in one central place, and drawing actionable insights whenever you need, plus integrated portals for all your child organisations."
- Platform features: memberships (one member profile, tailored forms, age verification, participation tracking, demographic reporting); finances (online payments, auto-reconciliation, payment plans, MYOB/Xero export); events (RSVP + ticketed); communications (bulk email & SMS); free website; online shop; competitions ("originally developed for a water polo competition" — complex fixtures, **restrict participant eligibility**, live scores fieldside, dynamic point score rankings); classes & training; asset & venue bookings; rostering (volunteers/umpires, linked to matches, timesheets); governance tools (meeting minutes & attendance, action items, searchable motions & resolutions, incident reporting & risk management, injury & medical tracking, granular administrator access).

### Market observation — Demosphere → OTTO

Evidence layer: A (redirect observed).

- demosphere.com now serves OTTO SPORT AI: club & league management, tournaments (OTTO EVENT, formerly SportWrench), referee management, ticketing, athlete recruiting, integrated insurance and risk management. The Demosphere brand — historically a governing-body platform — no longer has a standalone site. Recorded as market consolidation context; OTTO's own pages are club/league/tournament-first, so it was not used as a federation sample.

## Cross-product Comparison

| Aspect | Sport:80 | GotSport | SportyHQ | RevolutioniseSPORT |
|---|---|---|---|---|
| Customer position | NGBs (90+), UK/US | Soccer governing bodies (state associations → confederations) | Racquet-sport governing bodies | Australian peak bodies (260) |
| Member-organization register | "clubs, leagues, colleges, and other affiliated bodies… manage their affiliation" | clubs under state associations (implied by suite structure) | facilities + sub-organizations; "international to national, regional and local" structure | "all your members and organisations in one central place"; child-organization portals |
| Participant register | members: athletes, coaches, officials, fans; profiles, renewals, qualifications | players, coaches, referees, parents; registration status tracking | players, coaches, officials, external contacts; auto membership IDs; affiliation status | one member profile; participation tracking; age verification |
| Affiliation cascade | 3-in-1 membership across club/affiliated body/governing body | registration under association structure | membership syncing club → regional → national; bulk renewal affiliation | pooled membership database across child orgs |
| Hierarchy-aware money | payments & finance module | payment plans, refunds, reconciliation | regional + national + event fees in one transaction, auto-dispersed | payments, payment plans |
| Sanctioning / event approval | event registration (federation-run events) | competition solution (separate product) | full sanctioning workflow: request → terms → review/approve; membership enforcement; guest fees | competitions with eligibility restriction |
| Certification / credentials | certification management; NGB-configured standards; expiry alerts; lapse rules | risk management qualification system; API to JDP/SafeSport/CDC | coach/official credentials & accreditation history | classes & training (light) |
| Background checks / safeguarding | SafeSport + NCSI integrations; lapse rules | background status tracking; "only allow certified members on rosters" | (not on fetched pages) | incident reporting & risk management |
| Discipline | disciplinary case management linked to member records; audit log | (compliance side) | code violation management: offenses, point levels, cases, appeals, suspension points | incident reporting |
| Governance records | audit log; policy acceptance recording | — | user agreements | meeting minutes, motions & resolutions, granular admin access |
| Member self-service | member portal (profiles, renewals, qualifications, entries) | parent account, registration | member login, event entries, results recording | member-driven payments, profiles |
| Reporting outward | compliance reports "to funding organizations and external regulators" | analytics dashboard; Census Bureau comparison | statistics & reports | demographic reporting |
| Competition running | Results & Rankings bolt-on | Competition Solution (separate product) | tournaments, team/solo/box leagues, ladders (native) | fixtures, live scores, ladders (native) |
| Websites | integrations | website builder | website builder (hierarchy content sharing) | free website |
| Other | donations, campaigns, travel module, mobile apps | team app, live streaming, ticketing | court bookings, API | shop, venue bookings, rostering |

Reading: every sampled product holds (a) a register of member organizations with affiliation, (b) a register of individual participants bound to those organizations, (c) the governing body's authority instruments (sanctioning, certification/clearance, discipline) in some depth, and (d) hierarchy-aware money and reporting. The depth of each instrument varies by sport and market — racquet-sport federations lean on sanctioning + rankings; US soccer associations lean on registration + background clearance; NGBs on membership + certification + safeguarding.

## Canonical Abstraction

### L0 — Defining Invariant

The governing body's administrative system of record. Three jointly-held structures:

1. **The governing-body position** — the system is owned and operated by an organization that governs a sport across many subordinate organizations. Its constituents are other organizations and the participants registered under them — not one club's own life, not one competition's season. Remove → club management, league platform, or generic association management.
2. **The member-organization register with affiliation** — subordinate organizations (clubs, leagues, districts, schools, other associations) held as records with an affiliation relationship to the governing body: affiliation status, renewal cycle, affiliation fees, approval. Remove → a directory, or a participant register with no organizational governance.
3. **The participant register bound to member organizations** — individuals registered with the governing body (players, coaches, officials — the sports role set), each linked to a member organization, carrying registration/membership status and commonly a unique registration/membership identifier. Remove → a chapter list, or a generic CRM.

Jointly-held is load-bearing:

- 1 alone = generic association management (§25 territory)
- 2 alone = a directory of clubs
- 3 alone = a registration platform / eligibility machinery
- 1+2 without 3 = chapter management with sports vocabulary
- 1+3 without 2 = a governing body running a registration portal (drifts toward Sports Registration Platform)
- 2+3 without 1 = a league's club-and-player database

### L1 — Common Mature Structure

Present across the sample; expected in mature products; not definitional:

- affiliation/renewal cycle with fees (annual renewal, bulk affiliation, auto-renewal, status updates on payment)
- membership sync cascade (club → regional → national affiliation automation)
- hierarchy-aware fee collection and disbursement (multi-level fees in one transaction, split to recipients)
- competition sanctioning workflow (request → terms → review/approve) with membership enforcement at sanctioned events (guest fees for non-members)
- certification/credential tracking for coaches and officials (requirements configured by the governing body, expiry alerts, lapse rules such as restricted access)
- background checks / safeguarding clearance tracked against member records (third-party screening integrations)
- disciplinary case management (cases linked to member records, appeals, suspension points)
- member self-service portal (profile, renewal, entries, digital membership cards/IDs)
- segmented communication (email/SMS to membership slices)
- reporting/analytics (participation, demographics, compliance evidence for funders/regulators)
- policy/user-agreement acceptance tracking
- audit logs

### L2 — Variant / Optional Structure

Depends on sport, market, and customer scale:

- running competitions directly (fixtures/results/ladders) vs delegating to league/tournament products — racquet-sport and Australian samples run competitions natively; the NGB and US-soccer samples sell competition machinery as separate products/bolt-ons
- rankings systems (racquet sports: points tables, rating algorithms)
- hierarchy-aware website builders
- online shop/merchandise, donations/fundraising, event ticketing
- facility/court bookings, rostering of volunteers/umpires, classes & training
- insurance and travel modules
- grant management
- translation/multi-language

### L3 — Vendor-specific Structure

(Research Notes only)

- Sport:80: "3-in-1 membership" packaging; named SafeSport/NCSI integrations; service wrap (annual audits, webinars); Campaign Manager; Travel Module.
- GotSport: Census Bureau data comparison in analytics; JDP/CDC/Learning Center API list; GotSport Live streaming; parent-account multi-child registration.
- SportyHQ: proprietary ranking algorithm + bring-your-own points tables; box leagues; auto-accept of user agreements after a set number of days; translation engine; combined ranking lists (e.g., weighted singles/doubles/mixed).
- RevolutioniseSPORT: MYOB/Xero export; motions & resolutions record; water-polo heritage; free-website bundling.

## Vendor-specific Findings

See L3. Additionally: Sport:80 and RevolutioniseSPORT sell to the club layer as a separate product/portal (club management bolt-on; child-organization portals) — evidence that the federation platform's center is the governance register, with club operations delegated to a club-facing layer. GotSport likewise sells Club Management and Competition Solution as separate suite members.

## Boundary Findings

### vs League Management Platform (discharges that pass's joint-review flag)

The league platform runs ONE competition body's season: its defining loop is programme → results → standings. The federation platform governs many organizations; its defining register is organizations + participants + authority instruments. Overlap pole is real: federations sometimes run competitions directly (SportyHQ governing bodies run team/solo leagues; RevolutioniseSPORT runs fixtures/ladders; LeagueRepublic's customers include county associations; SportyHQ sells to governing bodies directly). In those cases the federation product embeds a league module, but the center of gravity remains the governance register — the league loop is one program among the federation's instruments. Directional test: strip the member-organization register + affiliation + authority instruments → what remains is a league platform; wrap a governance register around a league operator → federation territory. Keep both, center-of-gravity seam.

### vs Sports Club Management (discharges that pass's flag)

The club is ONE member organization; its system centers its own teams, members, and money. The federation governs many clubs. The club↔federation data flow (Spond/NIF member synchronisation observed at the club pass; SportyHQ membership syncing; Sport:80 club affiliation; RevolutioniseSPORT child-organization portals) is an integration edge for the club Type and the affiliation cascade for the federation Type. Directional test: if the system's constituents are other organizations → federation; if it is one organization's own life → club. Keep both. Vendor-side corroboration: federation vendors ship club management as a separate bolt-on/product rather than claiming the club's center.

### vs Referee Management Platform (discharges that pass's note)

Officials are one participant class inside the federation register (GotSport registers game officials inside the governing body solution; SportyHQ tracks officials' accreditation and assigns them to events/matches). A dedicated referee platform centers on the assigning/availability/game-official workflow; the federation platform centers on the register and governance. A federation running assigning is using referee-platform capability as one function. Keep both.

### vs Sports Eligibility Management (discharges that pass's flag)

Federation-run player registration and clearance (GotSport-class; US Club Soccer federation eligibility observed at that pass) is the eligibility machinery operated BY a federation. The eligibility Type's center is the individual participant's right-to-participate status (requirement sets, evidence, standing); the federation Type's center is the governance register over organizations + participants. The eligibility gate is one enforcement use of the federation register ("only allow certified members on rosters" — GotSport; "restrict participant eligibility" — RevolutioniseSPORT; membership enforcement at sanctioned events — SportyHQ). Keep both.

### vs Sports Registration Platform (unprocessed sibling)

Registration is one transaction feeding the register. The federation platform holds the ongoing governance relationship: affiliation of organizations, sanctioning, discipline, certification, reporting. A registration-led product operated by a state association drifts toward this Type when it adds the organization register and authority instruments. Forward flag recorded for that pass.

### vs Sports Membership / Licensing Platform (unprocessed sibling)

Vocabulary collision expected: "membership" is the federation register's participant leg; "licensing" appears as certification/credential instruments. The dedicated membership/licensing Type (if distinct) centers the membership/licensing transaction itself; the federation platform centers the governance register that membership feeds. Forward flag recorded for that pass.

### vs Association Management System (§25)

A generic AMS manages member organizations and individual members — the structural genus is shared. The sports-specific layer is what makes this Type: participants carry sports roles (player/coach/official) with registration tied to competition participation and clearance; affiliation cascades across sport hierarchies; sanctioning/discipline instruments exist. Sports federations demonstrably run on generic membership software for thin needs — which is why the sports governance layer, not "membership" as such, is the center.

### vs Chapter Management Platform (§25)

Chapters are internal units of one association; federation member organizations are independent affiliated bodies with their own legal existence and their own members. The affiliation edge (approval, fees, sanctioning authority) is the structural difference.

## Historical / Market-Sample Check

Paper-era federation (e.g., a 1920s county football association): a handbook register of affiliated clubs with annual affiliation fees; registered-player forms (registration, transfer); a list of sanctioned competitions; disciplinary minutes; correspondence. All three L0 legs hold with no digital machinery. A small regional association running on spreadsheets + a generic membership tool also fits (thin participant register). Modern additions — online self-registration, safeguarding integrations, digital cards, hierarchy fee splitting, websites — are standard-not-definitional. The definition does not depend on the current NGB-platform packaging.

## Uncertainties

- No help-center articles were fetched; lifecycle details (exact renewal windows, approval states, transfer mechanics between clubs) are inferred from product-page descriptions only. No precise values asserted in the final document.
- Insurance and grant management appear in the market (OTTO integrated insurance; Sport:80 travel; grant references) but were not deeply evidenced in this sample — held as L2/optional with weak wording.
- The boundary vs Sports Membership / Licensing Platform and vs Sports Registration Platform is proposed, not ratified — those leaves are unprocessed; forward flags recorded.
- SportyHQ's sanctioning workflow is the fullest documented; whether all federation platforms implement a formal request→approve sanctioning state machine (vs. lighter event approval) is not established. Final document uses moderate wording.

## Final Synthesis

Sports Federation Management is the governing body's administrative system of record. Its world: a governing body (national federation/NGB, state or regional association, confederation, peak body) holds a register of member organizations — affiliated clubs, leagues, districts, schools — each with affiliation status renewed through a cycle of application, approval, and fees; and a register of individual participants — players, coaches, officials — bound to those member organizations, each carrying registration/membership status and commonly a unique identifier, with registrations cascading up the hierarchy (club → regional → national) and multi-level fees collected in one transaction and dispersed to the right recipients. Around that spine, mature products add the governing body's authority instruments: sanctioning of competitions run by others (request → terms → approval, with membership enforcement at sanctioned events), certification/credential tracking for coaches and officials with expiry-driven lapse rules, background-check/safeguarding clearance recorded against members, disciplinary case management with appeals and suspension points, policy-acceptance records, and audit logs — plus the outward-facing obligations: participation/demographic/compliance reporting to boards, funders, and regulators, and self-service portals for members and delegated club/region administrators. The Type is defined by the governance register, not by any one instrument: remove the member-organization register and it is a registration platform; remove the governing-body position and it is club management or generic association management; remove the participant register and it is chapter management.
