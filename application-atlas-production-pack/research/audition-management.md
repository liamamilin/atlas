# Research Notes — Audition Management

## Research Goal

Understand what Audition Management applications really are in the market: what objects they manage, what workflow they run, who operates them and who participates, and how they differ from the most confusable sibling leaves — Casting Platform, Talent Agency Management, and production-side tools (Film Production Management, Production Scheduling).

Directory context: leaf sits in §27 Media, Entertainment, Creator & Culture, immediately after "Casting Platform" and before "Talent Agency Management".

## Initial Boundary

Working hypothesis before research:

- Audition Management = the operational software for running the audition/selection process for performing-arts roles: defining roles, collecting performer candidacies (submissions, applications, self-tapes), scheduling audition rounds, capturing evaluations, and moving candidates toward a casting decision.
- Most confusable neighbor: **Casting Platform** (breakdown/casting-notice marketplace where talent discovers opportunities). Hypothesis: platform = discovery + submission intake; audition management = the selection funnel around the audition itself.
- Other neighbors: Talent Agency Management (agency-side business), Applicant Tracking System (employment funnel), Event Registration (attendance logistics), Candidate Assessment (evaluation mechanics), Production Scheduling / Call Sheet (downstream logistics).

## Research Questions

1. What is the core object graph: project/show, role, talent/auditionee, submission, audition event/session, self-tape, evaluation, status?
2. What is the end-to-end workflow from intake to decision, and what are the stage names?
3. Who are the user populations (casting director, producers/directors/studio, adjudicators, talent, representatives, parents)?
4. What forms does the "audition" itself take: scheduled live slots, submitted recordings (self-tapes), live virtual rooms?
5. How is evaluation captured: ratings, notes, scorecards, rubrics, collaborative annotations?
6. How do decisions flow: callbacks, offers, booking/casting/acceptance?
7. How does material flow to decision-makers outside the casting team (producers/studio review, secure sharing)?
8. Where does discovery/submission end and selection management begin (the Casting Platform boundary)?
9. How does the type vary by segment: film/TV studio, commercial, community theater, performing-arts education?
10. Historical check: does the definition survive the paper era (sign-up sheets, headshots, live auditions) without self-tapes, virtual rooms, or marketplaces?

## Representative Products

Selected for market spread (enterprise studio ↔ commercial platform ↔ community theater ↔ education) and different product philosophies:

| Product | Segment | Philosophy |
|---|---|---|
| Cast It Systems | Enterprise film/TV studio casting | Security-first studio review workspace; selection workflow separate from discovery |
| Casting Networks | Commercial film/TV/commercial casting | Hybrid: marketplace (breakdowns, submissions) + audition/selection workflow in one product |
| Cast98 | Community theater | Lightweight all-in-one production-cycle tool centered on audition sign-up logistics |
| Acceptd | Performing-arts education & arts organizations | Application/adjudication-centric audition management for programs and ensembles |

## Sources

Research date: 2026-09-06. All Layer-A observations below come from official vendor surfaces.

- Cast It Systems — https://castitsystems.com/ (home, /services/, /clients/); Cast It support: https://support.castitsystems.com/en/articles/11393409 (audition video sharing)
- Casting Networks — https://support.castingnetworks.com/ (support center); key article: "CASTING DIRECTORS: How Do I Manage My Film & TV Casting Workflow on Casting Networks?" https://support.castingnetworks.com/en/articles/11367617
- Cast98 — https://cast98.com/ ; /features/audition-scheduling ; /features/audition-management
- Acceptd — https://getacceptd.com/ ; /audition-scheduling-software ; /auditionroom

Source-access limitations: www.castingnetworks.com root marketing site returned HTTP 403; the official support center was reachable and used instead (stronger evidence tier anyway). Cast It Systems' product documentation is mostly behind its support center; only the video-sharing article and marketing pages were reachable, so Cast It's internal list/session mechanics are kept general. Acceptd's Help Center (Zendesk) was not fetched; observations rely on official product pages.

## Product Observations

### Cast It Systems (enterprise studio casting)

Evidence layer: A (official site + official support article).

- Positions itself as "the casting platform used by every major studio and network"; "comprehensive suite of casting workflow applications". Studios "create briefs and roles, collaborate with casting offices and securely access and share audition videos" (A).
- Users named: studio executives, producers, directors, casting professionals; casting offices as collaborating organizations (A).
- Talent side ("Cast It Talent"): actors and representatives create/manage profiles, store and send video, submit to roles; agents submit headshots, resumes, reels, self-tapes (A).
- Open Calls service: custom landing page, sides sent securely with customizable watermark settings, receive/review submissions, create lists of submissions (A).
- Lite Projects: stripped-down project workspace; "receive and share auditions, self-tapes and reels"; no stated limit on roles/actors/videos; studio-approved security (A).
- Structure confirmed by support docs: **Project → Roles → Talent → video clips**; audition videos are attached per talent per role (A).
- **Quick Links / Email Project Videos**: share audition videos with external users via links; settings include expiration date, password protection, allow download, allow production-team notes to display, display talent age (minors only) / height; clips re-ordered; links are "live" (edits reflect instantly); links can be deactivated/reactivated (A).
- "Trusted by studios and networks since 2004… all casting and production videos to be viewed, organized and securely shared under studio-approved security standards" (A).

### Casting Networks (commercial platform + selection workflow)

Evidence layer: A (official support center, incl. end-to-end workflow guide).

- Distinct user populations documented: Casting Directors, Talent Representatives (agents/managers: roster, submissions, requests, packages), Project Creators (independent filmmakers/advertisers), Talent (A).
- Film/TV workflow (A):
  1. Create **Project** (title, type, production information)
  2. Add **Roles** (character name, breakdown description, age range, other specs)
  3. Post **Breakdown** / publish, with visibility filters (talent type, union status, location)
  4. **Submissions** arrive; sort/filter; review profiles, watch reels; rating tools mark talent **Consider / Hold / Pass**
  5. **Request Self-Tapes**: add custom sides, instructions, due date; talent notified; tape appears in the project's Self-Tapes section
  6. **Scheduling**: create audition time blocks, assign talent to slots, send appointment notifications; talent confirms or requests a change through the platform
  7. **Sessions**: organize audition footage and notes by project and role; add media; leave notes on performances; during live auditions capture notes in real time, flag favorites, update talent status; "whether you're in person or remote"
  8. **Worksheet**: "master list for tracking talent across all roles and stages… from initial submission through callback, offer, and booking"; customizable columns, bulk status updates, export for production meetings
- Branded features (L3): FastCapture® (in-room capture), Sessions & Presentation Links, Reports/Worksheet/Collaborators (A).
- **Copy to Cast It / Send Links Through Cast It**: push talent/project data from Casting Networks into Cast It, then share audition footage/profiles with producers/directors via secure links (recipients need no Casting Networks account) (A). This documents the market division: submission platform ↔ studio review workspace.

### Cast98 (community theater)

Evidence layer: A (official site + feature pages).

- Positions as all-in-one theatre production management; audition features are the entry of the production cycle; rehearsal scheduling and playbill continue downstream (A).
- **Audition scheduling**: built-in audition form (contact info, experience, conflicts, time slots, role preferences; headshot; emergency contact; training), shareable signup link, time slots with per-slot signup limits, reminder to auditionees one day before their slot, private (invite-only) auditions, optional video auditions, auditions for children (parent manages each child's form from one account), repertory auditions (cast multiple shows from one audition round) (A).
- **Audition management**: auditionee dashboard (snapshot per auditionee; filter by time slot and 20+ other tags), check-in ("track who is waiting in line"), scorable audition reports (director comments + 5 scorable attributes), collaborative reports (multiple show admins leave individual comments), messaging honoring active filters, conflict moderation (review and approve conflict-calendar changes case-by-case), auditionee data export (A).
- **Casting management**: send role offers with cast rules or personalized contract terms; assigning roles/groups grants access to protected resources (rehearsal schedule, chat groups, director notes, contact info) (A).
- Conflict calendars captured at signup auto-sync to rehearsal scheduling (A).

### Acceptd (performing-arts education & organizations)

Evidence layer: A (official product pages).

- Positions as "Application and Audition Management Platform" for auditions, applications, recruiting, adjudication; serves arts organizations, universities/conservatories, festivals (client logos include Carnegie Hall's Weill Music Institute) (A).
- Collect and review applications: custom applications, access for multiple reviewers, payment processing, data reporting/export/API (A).
- Accept online (recorded) video auditions (A).
- **Audition scheduling**: one slot per artist or longer blocked sessions with multiple auditionees; individually plan segments (prepared performances, sight-reading, interviews); schedule concurrent sessions and assign different adjudicators to each; manage in-person and live virtual auditions on one platform; communicate updates and schedule changes to adjudicators and applicants (A).
- **AuditionRoom** (branded virtual audition environment): branded virtual lobby with interactive video forum, auditionee status notifications ("online and ready"), move auditionees between virtual rooms, moderators/ambassadors, store recordings and adjudicator notes, live screen sharing for sight-reading (A).
- **Adjudication**: collaborative, using custom rubrics; notes organized across the process (A).

## Cross-product Comparison

| Structure | Cast It Systems | Casting Networks | Cast98 | Acceptd |
|---|---|---|---|---|
| Selection container | Project | Project | Show (production) | Program / application cycle |
| Defined things to fill | Roles | Roles + breakdown | Roles (cast & crew) | Program/ensemble seats (roles generalized) |
| Candidate intake | Talent/agent submissions to roles | Breakdown submissions; self-tape requests | Signup form + time slots | Applications with recorded media |
| Candidacy per role | video clips per talent per role | per-role submission, Consider/Hold/Pass | role preferences + reports | application per program |
| Audition event | implied sessions; video-centric | scheduled slots + sessions (live or remote) | time slots + check-in | slots/sessions + AuditionRoom |
| Recorded audition | self-tapes/reels stored & shared | self-tape request with sides + due date | optional video auditions | online video auditions |
| Evaluation | lists, review, notes | ratings + notes + flags | scorecards (5 attributes) + comments | custom rubrics, adjudicator assignment |
| Progression toward decision | lists → producer review | submission → callback → offer → booking | signups → callbacks → role offers → cast | application → audition → adjudication → communication |
| Sharing with decision-makers | Quick Links (expire/password/display controls) | Presentation links; push to Cast It | export | reviewer access; stored notes |
| Talent-facing surface | Cast It Talent portal | talent accounts + mobile app | audition form + auditionee dashboard | applicant accounts |
| Intermediary layer | agents/managers | agents/managers | parents (minors) | (none observed) |

Cross-product commonalities (Layer B):

1. **Selection container with defined roles to fill** — all four organize casting around a container (project/show/program) holding defined parts/positions.
2. **Individual performers as candidates** — every product tracks identifiable people with profiles (headshot, experience, media) and a per-role/per-program candidacy.
3. **The audition as organized demonstration** — a scheduled slot/session, a submitted recording, or a live virtual room; in all cases it produces an evaluative record attached to the candidacy.
4. **Staged progression to a decision** — all four track candidates through stages (intake → evaluation → later rounds → offer/booking/casting/acceptance). Casting Networks names the stages explicitly (submission → callback → offer → booking); Cast98 names callbacks and role offers; Cast It implies lists → producer review; Acceptd names adjudication and communicates outcomes to applicants.
5. **Evaluation capture** — ratings/notes at minimum; scorecards or rubrics in half the sample; collaborative evaluation by multiple evaluators in half the sample.
6. **Curated lists / shortlists per role and controlled sharing outward** — lists of submissions (Cast It), presentation links / worksheet export (Casting Networks), export (Cast98), reviewer access (Acceptd). The decision-makers (producers, directors, committees) sit outside the casting team.
7. **Communications to candidates** — notifications, reminders, schedule confirmations, direct messaging (all four).

## Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the product is no longer recognizable as audition management:

1. **A selection context with defined roles/opportunities to fill** — a production, show, or program that holds named parts/positions casting must fill.
2. **Performer candidates tracked individually, with a per-role candidacy** — identified people (profile + demonstration material) considered for specific roles.
3. **Audition/evaluation rounds that produce evaluative records per candidacy** — organized performance demonstrations (scheduled live sessions, submitted recordings, live virtual rooms), each generating an evaluation (rating/notes/score) attached to the candidate-for-role.
4. **Staged selection progression toward a recorded casting decision** — candidates move through statuses (e.g., considered → auditioned → callback → offered/cast or passed) until roles are filled or candidacies end.

Removal tests:
- Remove #1 → generic applicant/event tooling with no casting semantics.
- Remove #2 → a talent/media database, not a selection process.
- Remove #3 → intake + roster only (an application form tool); the audition is the defining act.
- Remove #4 → signup logistics (event registration), not selection toward casting.

Historical/market-sample check: the paper-era version (sign-up sheet, headshot pile, live audition with penciled notes, callback list, cast list posted on the door) satisfies all four invariants. Self-tapes, virtual rooms, breakdown marketplaces, rubrics, and conflict calendars are all later or segment-specific implementations and stay out of L0.

### L1 — Common Mature Structure

Very common in current products, not definitional:

- Role definitions with descriptive specs (character description, age range, requirements) — "breakdown" vocabulary in film/TV
- Intake forms/applications capturing candidate profile data (headshot, experience, training, contact; emergency contact in theater; eligibility data)
- Recorded audition handling: request with sides/instructions/deadline; upload; review playback (self-tape model)
- Audition scheduling machinery: slots/time blocks, capacity limits, reminders, confirmations, check-in
- Live virtual audition support: lobbies, rooms, readiness status
- Evaluation tooling: ratings, flags, notes; scorecards/rubrics where formalized; multi-evaluator collaboration
- Triage statuses on candidacies (consider/hold/pass-style), callback management, offers/booking
- Curated lists/shortlists per role; controlled sharing with external decision-makers (secure links, exports, reviewer access)
- Candidate communications (notifications, reminders, confirmations, direct messaging)
- Persistent talent profiles reused across projects (headshots, resumes, reels)
- Reporting/exports

### L2 — Variant / Optional Structure

Depends on segment, geography, deployment, business model:

- Intake mode: open marketplace-style published breakdowns vs private/invited auditions vs application-based admission (education)
- Media posture: self-tape-first vs live-first vs hybrid
- Adjudication formality: rubric-scored segments (education) vs triage ratings (film/TV)
- Intermediary layer: agents/managers as submitters (film/TV/commercial) vs parents managing minors (theater) vs direct applicants (education)
- Security posture: studio-grade (watermarked sides, expiring/password-protected links, download control, display restrictions for minors) vs lightweight
- Production-cycle integration (theater): conflict calendars syncing to rehearsal schedules; role offers granting resource access
- Payment processing (application/audition fees — education)
- Union/eligibility filtering (US entertainment industry)
- Repertory casting (one audition round feeding multiple shows)
- Asynchronous vs synchronous virtual auditions

### L3 — Vendor-specific (Research Notes only)

- Cast It: Quick Links with per-link display/download/expiration/password controls; "studio-approved security standards"; Open Calls and Lite Projects service packaging
- Casting Networks: FastCapture®; "Consider / Hold / Pass" status labels; Worksheet terminology; Copy-to-Cast-It integration
- Cast98: conflict-calendar auto-sync; 5 named scorable attributes; XL-membership feature gating; Playbill creator; "20+ tags" filtering
- Acceptd: AuditionRoom (branded lobbies, ambassadors, room-to-room moves); Recruitment Network; Marketing Services

## Rejected Findings

- "Audition management = casting marketplace": rejected. Two of four sampled products (Cast It, Acceptd — and Cast98 in practice) operate without a public discovery marketplace; discovery/submission is one intake mode among several, not the defining structure.
- "Self-tape video is the defining object": rejected. Live scheduled auditions and virtual rooms are first-class audition forms in the sample; recorded media is the common modern substrate of evaluation, not the invariant (paper-era auditions had none).
- "Rubric/scorecard scoring is core": rejected as definitional; it is segment-typical (education, community theater) while film/TV triage is rating+notes. Kept in L1 as evaluation tooling generally.
- "Scheduling is the essence": rejected. Scheduling is prominent in Cast98/Acceptd but Cast It is video-review-centric with scheduling less emphasized. Scheduling is L1.
- "Agency/representative layer is definitional": rejected; education and community-theater samples run direct or parent-mediated intake. L2.

## Boundary Findings

1. **vs Casting Platform (§27 sibling)** — most important boundary. Casting Platform's center is discovery and matching: published breakdowns/notices, searchable talent profiles, submission intake at market scale. Audition Management's center is the selection funnel for roles the organization controls: rounds, evaluations, statuses, decision, sharing. Test: remove discovery (public listings, talent search) and the product remains itself (Cast It, Acceptd do); remove the selection machinery (rounds/evaluation/status/sharing) and what remains is a Casting Platform. Several real products bundle both (Casting Networks is a platform with a management workflow inside) — the boundary is porous in the market but holds at the Type level. Directory keeps both leaves; when Casting Platform is processed, this boundary statement should be mirrored.
2. **vs Talent Agency Management (§27 sibling)** — the operator side differs: agency software is run by the talent's representative to manage roster/bookings/commissions; audition management is run by the selecting organization. Agents appear inside audition management as submitters, not operators. If the user of record is the talent's side managing their business, it is Talent Agency Management.
3. **vs Applicant Tracking System (§09)** — same funnel shape (intake → screen → evaluate → decide), different world: ATS selects employees for job openings via resumes/interviews; audition management selects performers for parts via performance demonstration, with entertainment-specific artifacts (breakdowns, sides, self-tapes, callbacks), performance media as central evidence, minors' consent/parent mediation, and union-eligibility rules. Structural kin; distinct domain objects and rules.
4. **vs Event Registration Platform (§26)** — audition scheduling overlaps registration mechanics (slots, reminders, check-in). Registration's terminal state is attendance; audition management's terminal state is a casting decision that fills roles. Remove roles + decision tracking and the audition tool degenerates into event registration.
5. **vs Candidate Assessment Platform (§09) / Examination Platform (§23)** — evaluation mechanics overlap (rubrics, scorecards, multi-evaluator); the purpose differs: selection of performers for roles in a production/program, not general skills certification or testing.
6. **vs Production Scheduling / Call Sheet Application & Film Production Management (§27)** — downstream: they start after casting, managing rehearsals/shoots/crews. Cast98's rehearsal module and role-offer resource grants show the adjacent bundling; the audition tool's center remains the selection funnel.

## Uncertainties

- Cast It Systems' internal list/session/callback mechanics are not publicly documented in detail; its L0 role in the sample rests on the video-sharing workflow and marketing claims. Claims kept general accordingly.
- Casting Networks scheduling internals (slot capacity, waitlists) not verified beyond the workflow guide.
- Acceptd's post-adjudication flow (offer/acceptance/communication) is described only generally on product pages.
- Callback mechanics are named explicitly by two products (Casting Networks worksheet stages; Cast98 callbacks) and implied by the others; treated as common but not universal mechanics.
- Taxonomy: whether "Audition Management" and "Casting Platform" should eventually be one Type with two work-modes is a legitimate question; evidence supports keeping separate leaves because management-only products exist, but market convergence is real. Flagged for Boundary Issues.

## Final Synthesis

Audition Management is the operator-side selection application of the performing arts. Its world consists of a selection container (project/show/program) holding defined roles, performers who become candidates with per-role candidacies, audition rounds — scheduled live, submitted recordings, or live virtual — that attach evaluative records to candidacies, and a staged progression that ends in a recorded casting decision and, in most products, controlled sharing of the evidence with the decision-makers (producers, directors, committees) who ratify it. Everything else — breakdowns and marketplaces, self-tapes, rubrics, conflict calendars, agency layers, studio security — is common mature structure or segment variant, not the definition. The type's closest neighbor is the Casting Platform, from which it is separated by where the work happens: discovery and intake (platform) versus running the funnel to a decision (audition management).
