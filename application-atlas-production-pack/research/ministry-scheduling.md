# Research Notes — Ministry Scheduling

## Research Goal

Understand what a Ministry Scheduling application is as an Application Type: what core structures define it, who uses it, how the scheduling work actually flows through the product, and where its boundaries sit against neighboring Types (Worship Planning, ChMS volunteer-scheduling modules, Religious Volunteer Management, Volunteer Management System, Employee Scheduling, Group Availability Scheduling).

## Initial Boundary

Initial hypothesis: Ministry Scheduling = software that schedules volunteers into serving positions for recurring congregational occasions (services, masses, classes), with an availability/response/substitution loop.

Candidate confusions to resolve during research:
- Worship Planning (sibling §25 leaf) — Planning Center's own product is branded "Worship planning & scheduling"; is scheduling just a capability of worship planning?
- ChMS volunteer scheduling — the ChMS pass (processed 2026-09-07) flagged ministry-scheduling as a "capability slice that exists both as ChMS modules and as standalone specialists."
- Religious Volunteer Management / generic Volunteer Management System — recruitment/onboarding/engagement vs the scheduling act.
- Employee Scheduling — paid shifts vs unpaid volunteers.
- Group Availability Scheduling — finding a common meeting time vs assigning people to positions.

## Research Questions

1. What are the core objects — position? team? occasion/need? assignment?
2. How are schedules generated: manual placement, rotation/preassignment rules, auto-scheduling, self-signup?
3. How do volunteers participate: availability/blockout input, accept/decline, substitution/trades?
4. What does the publication/notification loop look like (publish, finalize email, reminders)?
5. What role structure exists (scheduler, team leader, volunteer) and what can each do?
6. What is the seam with Worship Planning — is planning the service content part of this Type?
7. What denominational/segment variants exist (Catholic liturgical ministries vs evangelical worship teams vs children's ministry)?
8. What is NOT part of the Type (recruitment, background checks, giving, membership...)?

## Representative Products

| Product | Pole | Why chosen |
|---|---|---|
| Planning Center Services | modular-suite leader; separately-sold scheduling+planning product; US evangelical/megachurch scale | market leader, richest docs, straddles the worship-planning seam |
| Ministry Scheduler Pro (Rotunda Software) | pure standalone parish specialist; strong Catholic liturgical base | the dedicated-scheduler pole; Tier-1 "Scheduling Cycle" documentation |
| Churchteams | all-in-one ChMS with volunteer-scheduling module | the ChMS-module pole; explicit FAQ statements about scheduling vs service planning |
| Tithe.ly Church Management / Service Planning (Elvanto heritage) | bundled ChMS + service planning + worship app; international vendor | bundling pole; shows the planning/scheduling/product seam from a suite vendor |

Rejected as samples: SignUpGenius / VolunteerHub (generic event-volunteer signup tools — Volunteer Management System territory, not ministry-position scheduling), Breeze (domain now redirects to Tithe.ly after acquisition — vendor absorbed, not independently documented).

## Sources

- Planning Center Services product page — https://www.planningcenter.com/services (research date 2026-09-08)
- Planning Center Services help center root — https://pcoservices.zendesk.com/hc/en-us (limited category listing; Church Center blurb: volunteers "see their schedules, respond to scheduling requests, and chat")
- Ministry Scheduler Pro homepage — https://ministryschedulerpro.com/
- MSP Benefits — https://ministryschedulerpro.com/benefits
- MSP Help Center — https://ministryschedulerpro.com/help-center
- MSP "Scheduling Cycle" — https://ministryschedulerpro.com/help-center/scheduling-cycle (Tier-1 workflow doc)
- MSP online documentation root (zendesk; fetch failed with transport error — not retried per source-access rule)
- Churchteams homepage — https://www.churchteams.com/
- Churchteams Volunteers feature page — https://go.churchteams.com/volunteers-churchteams/ (includes FAQ with operational detail)
- Tithe.ly Service Planning — https://get.tithe.ly/product/service-planning (incl. Elvanto/Worship-app FAQ)
- breezechms.com/features — now redirects to Tithe.ly (market consolidation evidence only)

## Product A — Planning Center Services

### Key observations (evidence layer A unless noted)

- Positioning: "Service planning and volunteer scheduling, for any team"; navigation classifies it under "Worship & Teams" as "Worship planning & scheduling". FAQ: "Services is for anyone who needs to coordinate volunteers or plan services, regardless of the ministry area."
- **Service Types**: "Create a Service Type for any kind of service at your church, like Traditional, Contemporary, Liturgical, and Youth. Store plan information and volunteer teams under each type."
- **Plans**: each service occasion is a plan with service times; plan notes; order of service items (songs, sermon, announcements, communion); files; public view of the plan.
- **Volunteer teams & positions**: "Create a team for every volunteer role. Place people on the volunteer schedule according to the team they're part of—Nursery, Hospitality, Ushers... add a team leader, create custom positions within the team, and even assign people to those positions."
- **Scheduling forward**: "Schedule volunteers as far out as you need—weeks, months, or just for next Sunday"; Matrix view of multiple plans; templates for regular teams.
- **Auto-schedule**: "Fill in needed volunteer positions automatically based on when someone was scheduled last, preferences, and blockout dates."
- **Volunteer-side preferences**: blockout dates ("mark any days they won't be available to serve so their team leader knows when scheduling"); signup sheets ("schedule themselves whenever they're available"); household preferences ("serve alongside other family members, or indicate if they don't want to be scheduled at the same time"); "Email My Leader" button for availability changes.
- **Mobile app**: volunteers "responding to serve requests, viewing plans, chatting with team members." Church Center help-center blurb: "see their schedules, respond to scheduling requests, and chat."
- **Reminders**: "Set up emails to send automatically and remind people of their upcoming volunteer commitments."
- Permissions levels; CCLI reporting; Media library; Services LIVE (real-time item display); Music Stand; integrations (RehearsalPack, SongSelect, PraiseCharts).
- Pricing: per-number-of-team-members, as a separately purchasable product within the Planning Center suite (people data comes from the People product).

## Product B — Ministry Scheduler Pro

### Key observations (evidence layer A)

- Positioning: "Painless ministry scheduling... Trusted by 3,800 parishes to organize volunteer lectors, EMHCs, servers, and more!" — explicitly the Catholic liturgical-ministry pole (lectors, Extraordinary Ministers of Holy Communion, altar servers); also Lutheran testimonial. Sibling product "Unison" sold separately for "simple, ad-free volunteer signups for any other need" — the vendor itself separates generic event signups from core Sunday-ministry scheduling.
- **Scheduling Cycle** (Tier-1, 7 steps):
  1. "Update services" — service times/dates; "the number of volunteer positions looks right for each service"
  2. "Update rotations" — "Preassignments or rotating Teams"; "rotating assignments are placed on the schedule as soon as they are created"
  3. "Request availability" — email template: "requesting that volunteers update their availability online will reduce conflicts in your next schedule"
  4. "Fill your schedule" — "hand picking volunteers, creating repeating assignments, auto-scheduling volunteers, or a mix of all three"
  5. "Check your schedule" — "Run the Conflict Report to see any potential issues"; "check the Distribution Report to ensure a fair distribution of services"; then "make it Live"
  6. "Send 'Schedule Finalized' email" — "notify volunteers of their scheduled positions"
  7. "Reminders and subs" — "email or text reminders to help reduce no shows. They can request subs, fill positions and propose trades online, or through the iPhone or Android app."
- Auto Scheduler: "keeping families together (or apart), preventing double bookings, and honoring special requests"; testimonial: "less than three minutes to fill a three-month schedule."
- Volunteer self-service: "volunteers sub for each other, sign up for positions, and update their own scheduling preferences"; "Easy substitutions: find a replacement online when something unexpected arises"; automatic notifications about "upcoming assignments, unfilled positions, and pending sub requests."
- Ministry-leader empowerment: "Empower ministry leaders to manage their own scheduling or communication, giving them access to just what they need."
- Publishing: "Publish easy-to-read schedules online or on your church website."
- Communication: targeted email/text blasts with personalization tokens; open/bounce tracking; polls & RSVPs for trainings.
- Attendance: "tracking attendance using printable sign-in sheets or an integrated sign-in kiosk."
- Scheduling patterns highlighted: "Families, Teams, Rotations, Self sign-up, Experience levels."
- Desktop application heritage ("Installing the application on a new computer? Download MSP", license activation) plus mobile apps and online components.

## Product C — Churchteams (ChMS-module pole)

### Key observations (evidence layer A)

- Positioning: "Recruit, train, schedule, remind, and track how people serve with our complete volunteer scheduling system" — a named feature module of the ChMS suite.
- Scheduling: "Create volunteer schedules for a single team or several groups across multiple dates"; "Use templates to quickly create and duplicate schedules"; "Block out dates and substitute preferences save you time"; "Help prevent no-shows with automated reminders."
- Invitation/response loop: "Volunteers get an invite to serve along with a link to their schedule, and reminders before their scheduled date"; "The software finds conflicts, allows substitutes and block out dates, tracks replies, and enables team communication."
- FAQ on substitutes: "When creating a schedule, there is an option to choose to either allow or require volunteers to see contact information for all available substitutes, and then affirm that they have contacted and confirmed their replacement. The default option is simply to Accept or Decline an invitation to serve."
- FAQ on the worship-planning seam: "Does Churchteams schedule volunteers and service planning? Our volunteer scheduling features allows you to schedule, remind, attend, and track volunteer engagement for any event including worship services. A service planning feature is scheduled to be released in mid-2026." — i.e., scheduling volunteers exists today; planning the service content is a separate, not-yet-shipped capability.
- Upstream (recruitment) integration: "Use registration forms, reports, and referrals to recruit volunteers. Our system pools form information into a group, which makes tracking training and background checks easy. Use automation to sort people onto serving teams according to their interests." FAQ: background checks via Protect My Ministry integration.
- Shepherd layer: "spiritual gifts and member notes"; "Automated attendance not only measures involvement but also prevents burnout"; email/text volunteers from the group dashboard.

## Product D — Tithe.ly Church Management / Service Planning (Elvanto)

### Key observations (evidence layer A)

- Positioning: "Worship and Service Planning, Volunteer Scheduling, and more." Service Planning is a named module inside Tithe.ly Church Management (Elvanto heritage per FAQ references).
- Planning side: "Plan songs, sermon notes, transitions, and more"; song library; custom setlists; rehearsal resources; SongSelect integration; "Keep your team in sync — Share service outlines so everyone knows exactly what's happening."
- Scheduling side: "Schedule worship leaders & volunteers — Assign roles and send automatic reminders."
- Worship app (mobile music reader) pulls set lists from Elvanto service plans — the plan (content) and the scheduled people (roles) are distinct data joined by the service.
- Breeze domain redirect: breezechms.com/features now serves Tithe.ly product-demo pages — market consolidation; Breeze no longer independently documented.

## Cross-product Comparison

| Structure | Planning Center Services | Ministry Scheduler Pro | Churchteams | Tithe.ly/Elvanto | Layer |
|---|---|---|---|---|---|
| Teams/positions as schedulable records | teams + custom positions | positions per service; teams; experience levels | serving teams (groups) | roles assigned per service | B (4/4) |
| Dated occasions generating needs | plans + service times | services with times/dates/positions | schedules across multiple dates for any event | services/service plans | B (4/4) |
| Assignment binding person × position × occasion | assign people to positions on plans | repeating assignments / preassignments / manual pick / auto | invite to serve on schedule | assign roles | B (4/4) |
| Multiple fill methods: manual / rules (rotation) / auto / self-signup | all four documented | all four documented | manual + templates (+ self-serve substitutes) | manual roles (auto not observed) | B (3-4/4) |
| Volunteer availability input | blockout dates; household prefs | availability update requests | block out dates | not observed | B (3/4) |
| Response to assignment | respond to serve requests (app/Church Center) | schedule finalized notification; subs/trades online | accept or decline (default); track replies | not observed in fetched pages | B (3/4) |
| Substitution/trade machinery | signup sheets; Email My Leader | request subs, fill positions, propose trades; "unfilled positions" notifications | volunteer-arranged subs with confirmation affirmation | not observed | B (3/4) |
| Publication + notifications | share plan; reminder emails | Live schedule post; Schedule Finalized email; reminders | invite + link to schedule; reminders | automatic reminders | B (4/4) |
| Fairness/conflict tooling | auto-schedule by last-served/prefs/blockouts | Conflict Report; Distribution Report | software finds conflicts | not observed | B (3/4) |
| Attendance tracking | not on fetched pages (Check-ins product exists separately) | sign-in sheets/kiosk | automated attendance; burnout prevention | not observed | B (2/4) |
| Recruitment/onboarding attached | not in Services (People/Registrations products) | polls/RSVPs for trainings only | recruit/train/background checks in-module | background checks module in suite | B (2/4, module-dependent) |
| Service-content planning (order, songs) | plans with order of service; songs/media | none (pure scheduling) | explicitly not yet ("mid-2026") | core of Service Planning | B (2/4) |
| Leader-scoped permissions | permissions levels; team leaders | ministry leaders manage own scheduling | team communication from group dashboard | access permissions implied | B (4/4) |
| Mobile volunteer app | Services app / Church Center | iPhone/Android app | member app | Tithely Worship app (content-side) | B (4/4) |
| Pricing is people-counted, separate product | yes (team members) | license/subscription | ChMS suite pricing | suite/module pricing | B (2/4) |

## Canonical Model — Four Abstraction Levels

### L0 — Defining Invariant

Four jointly-held structures; the ministry-scheduling character lives in their combination:

1. **Ministry serving positions/teams held as schedulable records** — defined roles in the congregation's ministry life (usher, lector, nursery worker, worship team member) that identified people fill. Remove → a generic calendar/rota with nothing ministry-shaped to schedule into.
2. **Dated occasions that generate positions to fill** — recurring congregational gatherings (weekly services, masses, classes, events) for which each occasion needs certain positions staffed. Remove → a team roster with no occasion structure; nothing to schedule people into.
3. **The assignment binding person × position × occasion** — an identified volunteer scheduled to fill a position at a specific occasion, placed by hand, by rotation/preassignment rules, by auto-scheduling, or by self-signup, and forming the schedule of record. Remove → availability tracker or task list; nothing is scheduled.
4. **The people-side reconciliation loop** — the schedule is reconciled against who will actually serve: volunteers convey availability constraints, are notified of and respond to assignments, and resolve changes through the product (substitutions, trades, refills, reminders). The analog pre-history implemented the same loop by phone and posted rosters. Remove → one-way rota publication; the "scheduling" reduces to publishing a static list.

Jointly-held is load-bearing: (1) alone = team/roster management; (2) alone = event calendar; (3) without (2) = shift patterns with no occasions; (4) without (1–3) = a chat/polling tool. Domain binding: positions belong to a congregation's ministry life and the fillers are volunteers (unpaid members), which is what separates the Type from employee scheduling.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Rotation/preassignment machinery and schedule templates
- Auto-scheduling honoring last-served, preferences, blockout dates, family grouping rules, double-booking prevention
- Conflict detection and fair-distribution reporting before publish
- Publish/finalize step with notification to scheduled volunteers
- Automatic reminders (email/text) before the occasion
- Online published schedule views + calendar sync + mobile apps
- Self-service sign-up sheets (volunteers schedule themselves)
- Team-leader empowerment with scoped permissions
- Communication tooling (targeted email/text, personalization)
- Attendance/no-show tracking
- Multi-service/multi-plan management views

### L2 — Variant / Optional Structure

- Upstream volunteer lifecycle attached (recruitment forms, training, background checks, spiritual-gifts matching) — strong in ChMS modules, absent/thin in standalone specialists
- Service-content planning attached (order of service, songs, media, setlists) — present in Planning Center Services and Tithe.ly Service Planning; absent in pure schedulers
- Denominational shapes: Catholic liturgical-ministry scheduling (lectors/EMHCs/servers, mass times, preassignments), evangelical worship-team scheduling (bands, rehearsals), children's-ministry scheduling (ratios, check-in adjacency)
- Household/family scheduling preferences
- Skills/experience-level qualification rules
- Multi-campus operation
- Sign-in kiosks / printable sheets
- Desktop-installed vs cloud SaaS delivery (MSP retains desktop-install heritage)
- Separate product vs ChMS module vs worship-planning bundle (packaging variants)

### L3 — Vendor-specific (kept out of the final document)

- Planning Center: Matrix multi-plan view, Service Types vocabulary, Services LIVE, Music Stand, CCLI reporting, per-team-member pricing tiers
- MSP: "Unison" sibling product for event signups; "Preassignments" terminology; Conflict/Distribution Report names; 6-month money-back guarantee; desktop license activation
- Churchteams: Text-to-Church; Protect My Ministry integration; service-planning feature "mid-2026" roadmap
- Tithe.ly: Tithely Worship app; SongSelect integration; All Access bundling; Elvanto account-credential reuse

## Vendor-specific Findings

See L3. One structural market observation worth recording: the standalone specialist (MSP) sells generic event-volunteer signups as a *separate product* (Unison), while the ChMS module (Churchteams) treats scheduling as one feature among recruit/train/track — evidence that "ministry scheduling" and "generic church volunteer signup" are different market products, and that scheduling sits at the specialized end.

## Rejected Findings

- "Auto-scheduling is definitional" — REJECTED. Manual placement is first-class in all samples (MSP lists hand-picking first; Churchteams templates; PCO manual assign); auto-scheduling is a mature implementation of leg 3, not the invariant.
- "Accept/decline buttons are definitional" — REJECTED as stated. The invariant is the reconciliation loop; the accept/decline UI is one implementation (Churchteams calls it the "default option"; MSP offers subs/trades instead; PCO offers responses + signup sheets). Historical analog loop ran by phone.
- "Email/SMS/reminders are definitional" — REJECTED. Notification channel is implementation; the paper pre-history used posted rosters and phone trees.
- "Service planning (order of worship, songs) is part of the Type" — REJECTED. Only 2/4 sampled products include it; the pure scheduler (MSP) and the ChMS module (Churchteams, pre-2026) prove the Type stands without it.
- "Recruitment/background checks are part of the Type" — REJECTED as core; they are upstream volunteer-lifecycle machinery bundled in ChMS modules.
- "Ministry Scheduling = capability slice of ChMS only (alias)" — REJECTED. Standalone specialists (MSP, PCO Services as a separately-priced product) are sold and operated without the ChMS record core; but the module realization must be documented in Related Types.

## Boundary Findings

1. **vs Worship Planning (§25 sibling)** — the tightest seam. Bundling vendors (PCO, Tithe.ly) join "who serves where/when" (assignments) with "what happens in the service" (order, songs, notes, setlists); the pure scheduler and the ChMS module carry only the former. Churchteams' own roadmap (scheduling today, "service planning" mid-2026) shows a vendor treating them as distinct capabilities. Seam test: remove position-filling and keep order/songs → Worship Planning; keep position-filling without plan content → Ministry Scheduling. Joint review recommended when worship-planning is processed.
2. **vs Church Management System / ChMS (§25, processed)** — ChMS volunteer scheduling is a standard capability of ChMS (documented there), and ChMS is the dominant packaging. This Type stands as its own leaf because standalone, separately-sold scheduling specialists exist and their whole product is the schedule. Seam test: remove the ChMS record core (membership, giving, groups, check-in) and the scheduling product still exists → this Type; make the record core the center → ChMS. This discharges the ChMS pass watch-item from the scheduling side.
3. **vs Religious Volunteer Management (§25 sibling, unprocessed)** — this Type is the scheduling act on an existing volunteer pool (availability → assignment → confirmation → substitution). Volunteer-lifecycle machinery (recruiting, onboarding, training, engagement tracking) is adjacent and bundle-dependent. Flag for joint review.
4. **vs Volunteer Management System (generic §25)** — same seam at domain level: generic volunteer management centers on the volunteer program (opportunities, applications, hours, events); ministry scheduling centers on filling ministry positions on the congregation's recurring occasions. MSP selling event signups as a separate product (Unison) supports the split.
5. **vs Employee Scheduling Platform (§09)** — paid staff shifts vs unpaid volunteers in ministry roles; no wages, labor-law compliance, or HR employment records here. Position ≠ job.
6. **vs Group Availability Scheduling Application (§03.09)** — finding a common meeting time for a one-off gathering vs assigning identified people to defined positions across a recurring calendar of occasions. No poll mechanics here.
7. **vs Calendar Application / Resource Calendar (§03.08)** — occasions are dated like calendar events, but the scheduled unit is a person filling a ministry position, not an event or a room.

## Uncertainties

- Tithe.ly/Elvanto volunteer-side response mechanics (accept/decline, blockouts, subs) were not visible on fetched pages — response-loop claims for that vendor stay weak; the loop's cross-product status rests on PCO + MSP + Churchteams (3/4 sampled, layer B).
- Planning Center Services help-center articles were only reachable as a category listing; detailed operational rules (e.g., exact notification triggers) not verified — no precise numeric/behavioral claims made for PCO.
- MSP zendesk documentation root failed with a transport error; the vendor's own "Scheduling Cycle" page (fetched, Tier-1) carries the workflow evidence instead.
- Historical samples (paper sacristy rosters, printed schedules) are conceptual, not source-verified; the historical check is therefore conceptual, not evidential.
- Attendance/kiosk machinery sampled in 2/4 only — held as common-to-optional, not standard.

## Final Synthesis

Ministry Scheduling is the congregation's serving-schedule system of record. Its defining core is the four-part loop: ministry positions/teams as schedulable records + dated congregational occasions generating positions to fill + person × position × occasion assignments forming the schedule of record (by hand, by rotation rule, by auto-scheduling, or by self-signup) + the people-side reconciliation loop (availability input, response to assignments, substitution/trade/refill, reminders) that turns the intended schedule into who will actually serve. Everything else — auto-scheduling sophistication, notification channels, mobile apps, fairness reports, planning content, recruitment machinery, denominational shapes — is standard, optional, or vendor-specific structure layered on that loop. The Type is realized in the market as standalone specialists (MSP), separately-sold suite products (Planning Center Services), ChMS modules (Churchteams, Tithe.ly), and worship-planning bundles (PCO, Tithe.ly Service Planning) — packaging varies, the loop does not.
