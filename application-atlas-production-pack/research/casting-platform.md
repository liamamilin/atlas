# Research Notes — Casting Platform

## Research Goal

Understand what Casting Platform applications really are in the market: what objects they manage, what the two-sided workflow looks like, who the user populations are, how talent profiles and submissions work, and how the Type differs from its most confusable siblings — Audition Management (flagged for joint review from the audition-management pass), Talent Agency Management, and structurally similar Types (Job Board, Artist Booking Platform).

Directory context: leaf sits in §27 Media, Entertainment, Creator & Culture, between "Script Breakdown Application" and "Audition Management".

## Initial Boundary

Working hypothesis before research (informed by the audition-management pass's flag):

- Casting Platform = the two-sided market for performer casting: productions publish role opportunities (breakdowns/casting notices) at market scale; performers maintain profiles; the core transaction is the submission (profile → role), made by the performer or their representative; discovery runs both directions (talent finds roles; casting finds talent).
- Most confusable neighbor: **Audition Management** — hypothesis per the sibling pass: platform = discovery + submission intake at market scale; audition management = running the selection funnel (rounds, evaluations, decisions) for roles an organization controls. Joint review required.
- Other neighbors: Talent Agency Management (rep-side business software), Artist Booking Platform (dated live appearances), Job Board / Listings (structurally similar opportunity+application shape), Script Breakdown Application (vocabulary collision only), Film Production Management (downstream).

## Research Questions

1. What is the core object graph: project, role, breakdown/casting notice, talent profile, submission, request/alert, status?
2. Who are the user populations, and what does each do (casting directors, producers/filmmakers, talent representatives, talent, parents of minors)?
3. What does the demand side publish, and how is visibility controlled (who may see and submit)?
4. What does the supply side maintain: profile structure (headshots, resume, reels, attributes), privacy posture?
5. What exactly is a submission: who can make it, what it carries, can it be customized or retracted?
6. How does discovery work in both directions: role search/match alerts (talent side), talent database search (casting side)?
7. What feedback loop exists after submission (statuses, requests, audition invitations)?
8. Where does the platform end and the selection funnel begin (the Audition Management boundary)?
9. How does monetization and openness vary (talent subscriptions, per-submission fees, rep-paid, production-paid; agents-only vs open self-submission)?
10. Historical check: does the definition survive the paper era (breakdowns delivered to agents, headshot submissions from agency files)?

## Representative Products

Selected for market spread (industry infrastructure ↔ open marketplace; rep-mediated ↔ self-submission; studio tier ↔ indie tier) and different product philosophies:

| Product | Segment | Philosophy |
|---|---|---|
| Casting Networks | Film/TV/commercial casting platform | Hybrid: full two-sided market + selection workflow bundled in one product; four distinct user populations |
| Breakdown Services (Actors Access + Breakdown Express) | US film/TV/theatre/commercial/voice infrastructure | Industry-utility model: casting controls breakdown release; rep-mediated submission is the default track, self-submission is a paid add-on |
| Cast It Talent | Talent side of the studio casting database (Cast It) | Feeder model: talent platform exists to feed a studio-side management system; direct submission into studio inboxes |
| Casting Frontier | US commercial/print/film/TV marketplace | Open marketplace model: public casting-call listings, one-click applications, tiered talent subscriptions |

Backstage, Mandy Network, StarNow were considered as consumer-marketplace samples but were unreachable (403 ×2 each) — see Sources.

## Sources

Research date: 2026-09-06. All Layer-A observations come from official vendor surfaces.

- Casting Networks — support center (Front KB): https://support.castingnetworks.com/
  - Casting Director Support category: /en/categories/2301441-casting-director-support
  - End-to-end Film & TV workflow guide: /en/articles/11367617
  - Talent Support → Casting Billboard® Projects and Submissions: /en/categories/2314177-casting-billboard-projects-and-submissions
  - TALENT: How Do I Navigate the Casting Billboard®: /en/articles/11229185
  - TALENT: How do I track my requests and submissions (Role Tracker): /en/articles/11229057
  - Talent Representative Support: /en/categories/2301825-talent-representative-support
  - Section Four: Submitting Talent to a Role: /en/articles/11237569
  - Project Creator Support: /en/categories/2302273-project-creator-support
- Breakdown Services, Ltd. — official FAQ: https://breakdownservices.com/index.cfm/main/faq ; Actors Access root: https://www.actorsaccess.com/
- Cast It Talent — official site: https://www.castittalent.com/ ; Help Center: https://support.castitsystems.com/hc/en-us/categories/15394406062477-Cast-It-Talent-Support ; TALENT: FAQs: https://support.castitsystems.com/en/articles/11395265 ; Talent category: /en/categories/2393857-talent
- Casting Frontier — official site: https://castingfrontier.com/ (talent / casting-directors / agents-managers pages linked from root)

Source-access limitations: www.backstage.com, help.backstage.com, mandy.com (with and without www), and www.starnow.com all returned HTTP 403 on 2026-09-06 (abandoned after 2 attempts each per the network-restriction rule) — the consumer-marketplace segment (theater-heavy, international) is under-evidenced and no claims are made about those products. www.castingnetworks.com marketing root was 403 in the sibling pass; the official support center (stronger tier) was used instead. Casting Frontier evidence is product-page level (Tier 2); its support center was not fetched. Vendor market-share claims (e.g., "97% of scripted content", "85% of network TV / 95% of studio features", audience counts) are recorded as vendor claims only.

## Product Observations

### Casting Networks (hybrid platform + selection workflow)

Evidence layer: A (official support center, multiple role-specific sections).

- Four documented user populations: **Casting Directors** ("exclusive"), **Talent Representatives** (agents/managers), **Project Creators** (independent filmmakers, advertisers, other creatives), **Talent**. Separate support sections per population (A).
- Casting-director workflow (end-to-end guide, A): log in → dashboard (active projects, recent submissions) → **Create New Project** (title, type — Film/TV etc., production information) → **Add Role** (character name, breakdown description, age range, other specs; unlimited roles) → **Post Breakdown / Publish** with visibility filters (talent type, union status, location, more) → **Submissions** tab (sort/filter by role, submission date; review profiles, watch reels; rating tools mark talent **Consider / Hold / Pass**) → **Request Self-Tapes** (custom sides, instructions, due date; talent notified; tape lands in project's Self-Tapes section) → **Scheduling** (audition time blocks, assign talent, appointment notifications; talent confirms or requests change through the platform) → **Sessions** (organize audition footage and notes by project and role; real-time notes, flag favorites, update status during live auditions, in person or remote) → **Copy to Cast It** / **Send Links Through Cast It** (push data to the studio review workspace; recipients need no Casting Networks account) → **Worksheet** ("master list for tracking talent across all roles and stages… from initial submission through callback, offer, and booking"; customizable columns, bulk status updates, export for production meetings).
- Talent side (A): **Casting Billboard®** is the role-discovery surface — default filters derived from the profile (age range, gender appearance, location); further filters (project type, role type); **saved searches** with default search; **Open Call filter** (open calls = projects accepting direct submission via dedicated link; notifiable only by browsing). Submitting requires a **Premium Membership** and a **personal profile not managed by an agent**. Submit flow: browse → filter → project/role details → **Submit to Role** → customize (choose which media casting sees, upload requested media, add submission note) → **Send Submission** → lands in **Your Submissions**. **Unsubmit** possible until the casting director has reviewed.
- Talent feedback loop (A): **Your Alerts** inbox aggregates callback requests, audition requests, media requests, question requests across all profiles; **Role Tracker** (Premium/Ultimate) shows submission status: **Submitted / Selected / Under Consideration**; **Submission History** lists past self-submissions. Rep-submitted projects are explicitly out of the talent's platform view ("contact your representative directly").
- Representative side (A): **Talent page = roster**; Projects list; **Submitting Talent to a Role**: open project → roles accepting submissions (due date, work date, requested media, # selected, # submitted) → **Find Talent** → Select and Submit section (role details, rate details, dates/location, requested media type + instructions) → roster loads → **Auto Fill by Role Criteria** (project union status, playable age range, working location, gender or ethnic appearance) or manual/advanced filters (skills, sizes) → select talent → **Customize** each submission (primary photo, include/hide media, requested media, submission note, overscale status) → Review → **Submit Selections**; unsubmit possible until casting views. **Worksheet** is where auditions, callbacks and requests land once casting distributes them. **Talent Scout®** lets reps search the network for talent seeking representation. **Packages** share the roster outside the platform. Reports.
- Project Creator side (A): create projects and **submit for approval** (platform gates posting for this population), create/manage requests, review submissions.
- Security/trust (A): watermarked audition sides and documents; a "how to spot a casting scam" guide ("legit casting calls never ask for…"); FastCapture® (in-room capture) and FastCapture Live (virtual audition) branded features; mobile apps for talent and reps.

### Breakdown Services, Ltd. (Actors Access + Breakdown Express)

Evidence layer: A (official FAQ + product root).

- **Breakdown defined**: "a synopsis of the entire script including complete character descriptions of each role, the key Creative and Production team members, location, start dates, rate of pay, union affiliations and any special notes or requests." Casting instructs where breakdowns are released; agents/managers use it to submit talent; actors use it to decide interest and prepare auditions (A).
- Three integrated surfaces: **Actors Access** (actors), **Breakdown Express** (casting directors, filmmakers, agents, managers), **Enterprise Solution** (studios/networks) (A).
- Canonical flow (A): casting sends project info → breakdown prepared → released to agents/managers and/or actors in chosen regions → reps view on Breakdown Express, actors view on Actors Access → **the Actors Access profile is submitted** → casting views submissions and selects actors to audition → auditions via **Eco Cast** (self-tape, in-person, or Eco Cast Live) → casting finalizes with collaborators.
- Publisher-controlled visibility (A): "Some Breakdowns are posted to Actors Access while others are posted to only Agents and Managers on Breakdown Express. The Casting Director determines where a project is posted." Union and non-union both posted. Vendor claim: 97% of scripted content requiring actors in North America.
- Talent profile (A): free Actors Access profile — headshots (2 free), 1 SlateShot, résumé, size card, special skills, role match alerts, secure Eco Cast invitations and sides; "one profile for every Talent Representative in any location" (profile shared across reps).
- Self-submission is the paid track (A): **Actors Access PLUS** ($68/yr or $9.99/mo) adds "submit yourself to unlimited Actors Access Breakdowns"; free accounts submit via representatives (or per-project basis). SAG-AFTRA member discount. Performance media added for a fee.
- Representative side (A): subscription service; roster built by inviting actors (name + email); each actor must have an Actors Access account; per the California Privacy Act "every Actor has the right to control their own Actors Access profile and who has access to this information."
- Mobile app (A): role match notifications, match-criteria management, view/submit to projects, **CMail** messages, audition requests (view/confirm/decline/reschedule), upload self-tapes to Eco Cast invitations.
- Adjacent services (A): **Talent Link** (find representation), **CastingAbout** (track casting directors).

### Cast It Talent (feeder into the studio casting database)

Evidence layer: A (official site + official help center).

- Positioning: "the platform that every major film and television studio uses to make their casting decisions"; the FAQ distinguishes **Cast It** ("the business database used by studios and casting directors to manage the casting process") from **Cast It Talent** ("the actor's direct link into Cast It. Submissions here are uploaded directly to the Cast It system for review by production executives") (A). Vendor claims: 400,000+ talent, 12,000+ studios/production companies, 78,500+ roles posted; Cast It used for 85% of network TV and 95% of studio features.
- Public **Find Roles** listing: recent/past roles shown as project (feature film / TV series) + role name (A).
- Membership (A): open to union and non-union, represented and unrepresented, any geography; agents/managers join free. **Basic (free)**: submit headshot, resume, video to roles on the Roles Tab; video submissions may carry a $5 fee. **Pro** ($19/mo or $180/yr): 20GB media hosting, free unlimited submissions, **packages** (e.g., comedy or drama package), send packages to 700+ casting-director and studio inboxes via dropdown, shareable package URL.
- **Family Accounts**: manage multiple child profiles from a single login (A).
- Privacy (A): profile not publicly discoverable unless the Actor URL is shared; every submitted video auto-set to Private (only the talent and the casting office submitted to can access); profile visibility toggle ("Casting Directors Only" vs "Actors, Agents, and Casting Directors"); per-media include/remove from public profile.
- Submission process (A): locate role on Roles page → upload media (headshot, resume, demo reel, or self-tape) → Submit. Sides not always posted. **Eligibility**: "If a role states strict age or location requirements, there are no exceptions. Only submit to roles that fit your description." Deadlines: casting may turn off roles at any time. **Gig-Finder** filters roles by location; casting offices use the platform to find talent outside LA/NY.
- Talent account management (A): submission history, add/remove representation, subscription management, media/resume organization, video conversion pipeline (500MB file limit — product-specific).

### Casting Frontier (open marketplace)

Evidence layer: A for structure claims on official product pages (Tier 2 — marketing/product pages, not help center).

- Three user types with dedicated portals: **Talent**, **Casting Directors & Content Creators**, **Agents & Managers** (A).
- Talent pitch (A): create profile (headshots, video clips, resume, social media links) → search roles ("dozens of new projects posted daily", filter to fit) → "apply to casting calls and auditions with a single click" → "audition from anywhere" (remote invitations). Tiered subscriptions: Basic free (1 headshot, limited submissions), Premium / Premium Plus (unlimited headshots/clips/submissions, featured reels, website link). SAG-AFTRA discount.
- Casting side (A): post casting calls; "get submissions from talent, agents or both"; "filter acting profiles in our database by criteria including age, gender, skills, union status, and more"; schedule casting calls & auditions ("request video, share live, taped, or virtual video auditions"); chat with talent and agents.
- Agent side (A): roster upload/update, submit talent to casting calls, cancel or confirm auditions, **Agent Finder** ("find your next great client" among unsigned talent).
- Market scope (A): "one of the largest talent databases and casting call listing services in the U.S." — commercial, digital, film, print, TV; LA/NY/nationwide. Talent Systems company ("Powered By TS" — same parent group as Cast It Talent).

## Cross-product Comparison

| Structure | Casting Networks | Breakdown Services (AA/BDS) | Cast It Talent | Casting Frontier |
|---|---|---|---|---|
| Demand-side unit | Project → Roles → Breakdown (published) | Breakdown (script synopsis + character descriptions) | Roles on public Roles Tab | Casting call / project |
| Supply-side unit | Talent profile (personal + rep-managed variants) | Actors Access profile (one profile, shared across reps) | Cast It Talent profile (+ family accounts) | Talent profile |
| Publication visibility control | Filters: talent type, union status, location | Casting chooses release: agents-only vs actors too, by region | Public roles tab; strict eligibility stated | Public casting calls |
| Discovery (talent side) | Casting Billboard® + saved searches + Open Call filter | Breakdown listing + role match alerts | Roles Tab + Gig-Finder (location) | Casting-calls listing + filters |
| Discovery (casting side) | Submissions inbox; talent search via workflow | Submissions view | Submissions into Cast It | Database filter search (age/gender/skills/union) |
| Who submits | Talent (self, Premium + personal profile) or rep | Rep default; talent self-submit via PLUS | Talent or rep (agents join free) | Talent or agent |
| Submission content | Profile + chosen media + note (+ requested media) | Actors Access profile | Headshot/resume/video per role | Profile (+ media) |
| Per-submission customization | Yes (media selection, note, overscale) | not observed | media upload per submission | not observed |
| Feedback loop | Alerts inbox; Role Tracker (Submitted/Selected/Under Consideration) | CMail; audition requests (confirm/decline/reschedule) | Submission history | not observed |
| Rep layer | Full rep account (roster, submit, packages, Talent Scout®, worksheet) | Roster + submit (subscription service) | Free agent accounts | Roster + submit + Agent Finder |
| Minors | not observed | not observed | Family accounts (child profiles) | youth segment present (testimonials) |
| Monetization | Talent Premium membership | Free profile; PLUS subscription; per-media fees | Free basic + $5/video; Pro subscription | Tiered talent subscriptions |
| Union regime | Union-status visibility filter | Union affiliations in breakdown; SAG-AFTRA discount | Union/non-union both welcome | Union-status filter; SAG-AFTRA discount |
| Downstream (selection) | Self-tape requests, scheduling, sessions, worksheet (bundled) | Eco Cast (self-tape/live/desktop) | Uploads feed Cast It (studio side) | Schedule auditions; request video; live/taped/virtual |

Cross-product commonalities (Layer B):

1. **Published role opportunities** — every product's demand side publishes roles/notices into a shared market, with publisher-controlled visibility (who may see/submit: reps only vs talent too; union, location, talent-type filters; regions).
2. **Persistent performer profiles** — every product maintains per-person talent profiles carrying appearance attributes (age range, gender appearance, location, union status, sizes, special skills) and performance media (headshots, resume, reels/clips).
3. **The submission as core transaction** — every product's pivotal act is putting a profile forward for a specific role, by the performer or their representative; submissions land in a casting-side review space.
4. **Two-directional discovery** — talent side: searchable/filterable role listings plus match alerts/saved searches (all four). Casting side: submissions review in all four; proactive talent-database search directly evidenced in two (Casting Frontier, Casting Networks' rep-facing Talent Scout®), implied in the others' "database" framing.
5. **Representative layer as an alternative submitting party** — all four support rep accounts (roster + submit-on-behalf); all four also support direct talent submission in some mode. Neither mode is universal-default.
6. **Status/feedback machinery** — alerts/requests inbox and submission-status tracking observed in three of four (Casting Frontier's not observed on fetched pages).
7. **Handoff into selection** — all four connect to audition/selection mechanics (self-tape requests, scheduling, live/virtual auditions), with bundling depth varying from full workflow (Casting Networks) to a feeder link (Cast It Talent).
8. **Talent-pays monetization is dominant** — three of four charge talent subscriptions for self-submission/media; the rep/production side is free or subscription in different products. Per-submission fees appear product-specific.
9. **Trust/privacy machinery** — profile non-discoverability by default, private media, watermarked sides, scam guidance (observed in three of four).

## Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the product is no longer recognizable as a casting platform:

1. **Published casting opportunities** — roles/breakdowns/casting notices released by productions or casting offices into a shared market, with publisher-controlled visibility over who may see and submit.
2. **Performer talent profiles** — persistent, per-person records carrying appearance/eligibility attributes and performance media, maintained by the performer (and/or their representative).
3. **Submissions** — the transaction binding a talent profile to a published opportunity, initiated by the performer or their representative, and delivered into a casting-side review space.
4. **Market-scale two-sided discovery** — searchable/filterable/match-notified surfaces through which talent finds opportunities and casting finds talent, serving many unrelated productions and many performers simultaneously (a shared intermediary, not a single organization's funnel).

Removal tests:
- Remove #1 → a talent database/portfolio directory, not a casting platform.
- Remove #2 → a job/listings board with no candidate identity.
- Remove #3 → disconnected listings + directory (classifieds shape); the casting transaction is gone.
- Remove #4 → a single organization's private intake funnel (audition-management territory), not a market.

Historical/market-sample check (Layer C): the paper-era model — breakdowns physically released to agents (and sometimes actors), headshot/resume files as profiles, headshot drops as submissions, agents and casting reviewing piles — satisfies all four invariants; the current Breakdown Services FAQ still describes exactly this release model in digital form. Digital-era features (self-tapes, match alerts, self-subscription memberships, video hosting, family accounts, saved searches) are accretions and stay out of L0. The L0 does not over-fit to the modern self-subscription marketplace.

### L1 — Common Mature Structure

Very common in current products, not definitional:

- Breakdown/role detail conventions: character description, age range, union status, rate/pay, usage, work dates, location, requested media, special skills
- Role match alerts, saved searches, notification machinery
- Submission-status tracking (submitted/selected/under-consideration-style) and submission history
- Self-tape request & upload machinery (sides, instructions, deadlines)
- Media management: headshots, demo reels/clips, resume, size card, special skills; per-submission media selection and notes
- Talent representative accounts: roster, submit-on-behalf with criteria-based autofill, packages, rep-facing request worksheets
- Proactive talent search on the buyer side (database filtering) — evidenced in two of four; common but not universal
- Audition scheduling and virtual-audition entry points (the handoff to selection)
- Privacy/visibility controls: non-public profiles by default, private media, watermarked sides, scam guidance
- Mobile apps
- Family/minor account handling (observed in one; treated as common-mature at most)

### L2 — Variant / Optional Structure

Depends on segment, geography, business model:

- Who pays: talent subscription (dominant), per-submission fees, rep-side subscription, production-side free/paid
- Openness posture: rep-mediated default (breakdowns released to agents only) vs open self-submission vs open calls via links
- Segment scope: film/TV scripted, commercials (rate/usage detail), modeling/print, voice-over, background, theatre, student films
- Regional/union regime centrality (US SAG-AFTRA discounts and union-status filters; regional release targeting)
- Poster gating: platform approval before publishing (project-creator tier)
- Bundling depth of the selection funnel (full workflow inside the platform vs feeder link into a separate studio system vs light scheduling)
- Adjacent market services: find-representation directories, rep-seeking-talent search, casting-director tracking services
- Enterprise vs indie tiering

### L3 — Vendor-specific (Research Notes only)

- Casting Networks: Casting Billboard®, Talent Scout®, FastCapture®/FastCapture Live, Consider/Hold/Pass labels, Worksheet, Copy to Cast It / Send Links, Project-creator approval flow, overscale-status flag
- Breakdown Services: Eco Cast (Live/Self-Tape/Desktop), CMail, SlateShot, size card, Actors Access PLUS pricing ($68/yr, $9.99/mo), SAG-AFTRA 20% discount, "97% of scripted content" claim, Talent Link, CastingAbout
- Cast It Talent: Cast It vs Cast It Talent split, Gig-Finder, 20GB hosting, 500MB upload limit, $5 video-submission fee, "700+ inboxes", 85%/95% claims, family accounts, Talent Systems parentage
- Casting Frontier: tier names/pricing, Agent Finder, BlueJeans virtual auditions (testimonial mention), "largest talent databases" claim

## Rejected Findings

- **"Casting platform = audition management"** — rejected (see Boundary Findings #1). The market bundles them, but management-only products exist without any marketplace, and platform-only value (matching at scale) exists without funnel machinery.
- **"Self-tape video is the defining object"** — rejected. Submissions can be headshot+resume; self-tape machinery is common mature structure (L1); the paper era had none.
- **"Talent-pay subscription is definitional"** — rejected; monetization varies across the sample (L2).
- **"Agent/representative mediation is definitional"** — rejected; direct self-submission is a first-class mode in half the sample and the rep is an alternative submitting party, not a structural requirement.
- **"A public open marketplace is definitional"** — rejected; publisher-controlled release (agents-only breakdowns) is an equally structural mode; what is invariant is publisher-controlled visibility, not openness.
- **"Video hosting is definitional"** — rejected (paper-era check).
- **"Proactive talent-database search is definitional"** — downgraded to L1: directly evidenced in two of four products; the submissions inbox is the universally evidenced casting-side surface.

## Boundary Findings

1. **vs Audition Management (§27 sibling) — JOINT REVIEW COMPLETED (this pass closes the flag recorded by research/audition-management.md).** The boundary holds at Type level from both directions. Casting Platform's defining work is the market exchange: publishing opportunities at scale, maintaining the talent-profile population, and moving submissions across the match — its natural terminal state is a reviewed submission pool plus early signals (requests, audition invitations). Audition Management's defining work is running the selection funnel for roles an organization controls: rounds, evaluations, statuses, decision, evidence sharing. Two-directional test: remove the market/discovery layer (published listings, talent search, match alerts, multi-production scale) → what remains is still audition management (Cast It studio workspace and education adjudication products do exactly this); remove the selection machinery (rounds/evaluation/decision) → what remains is still a casting platform (open listing-and-submission marketplaces do exactly this). Real products bundle both (Casting Networks runs the full funnel inside the platform; Cast It Talent feeds a separate studio-side system) — porous in the market, distinct at the Type level. Both leaves stay in the directory; no taxonomy change.
2. **vs Talent Agency Management (§27 sibling)** — operator perspective. Agency software is run by the talent's representative to manage the agency business (roster economics, commissions, contracts, bookings). The rep accounts inside casting platforms exist only to submit into the market and handle resulting requests; commissions/contract economics are absent. If the rep's business is the center → Talent Agency Management.
3. **vs Job Board / Listings Platform (§02.11 / §05.03 analogs)** — same abstract shape (posted opportunities + candidate applications). Different world: the candidate object is a media-bearing performer profile with appearance attributes (not a resume), the opportunity carries casting-specific artifacts (breakdowns, sides, union eligibility, rate/usage), a representative layer submits on behalf of candidates, and the outcome is casting into a production, not employment hiring. Remove the performer-profile/media semantics and rep layer → a job board.
4. **vs Script Breakdown Application (§27 sibling)** — vocabulary collision only. A script breakdown application decomposes a screenplay into production elements in pre-production; a casting breakdown is a role notice published to talent. Different objects, different users, different workflows.
5. **vs Artist Booking Platform (§27 sibling)** — booking engages a performer for a dated live appearance via offer/hold/confirm; casting selects performers for production roles via published opportunities and submissions. Different occasion semantics and lifecycle vocabulary (per the artist-booking pass's own boundary note).
6. **vs Recruiting/ATS (§09)** — structural kin (opportunity market + candidate profiles + submissions + funnel). Different domain: employment vs performance casting; media-first profiles; representative mediation; union eligibility; self-tape/sides artifacts. Recorded as awareness for the §09 passes.
7. **vs Social/Portfolio platforms** — talent profiles resemble portfolio pages, but the platform's center is the opportunity↔submission exchange with eligibility filtering and status tracking, not self-promotion or social graph.

## Uncertainties

- Backstage, Mandy Network, StarNow unreachable (403 ×2 each) — the consumer-marketplace segment (theatre-heavy, international, hobbyist) is under-evidenced; no claims made about those products. The sample skews to US film/TV/commercial infrastructure.
- Casting-side proactive talent search is directly evidenced in only two products; treated as common-mature with a qualifier, not invariant.
- Exact status vocabularies vary by product; only Casting Networks' statuses (Submitted/Selected/Under Consideration) were directly observed; treated as one product's labels, not industry standard.
- The historical paper-era check is canonical inference from the current Breakdown Services FAQ's release-model description, not from fetched historical pages.
- Whether the market eventually converges Casting Platform + Audition Management into one Type with two work-modes is a legitimate open question; current evidence (management-only products exist; platform-only products exist) supports separate leaves.
- Casting Frontier evidence is product-page level (Tier 2); its help center was not fetched, so its workflow details are positioning-level.

## Final Synthesis

A Casting Platform is the two-sided market intermediary of performer casting. Its world consists of published casting opportunities — roles and breakdowns released by productions and casting offices into a shared market under publisher-controlled visibility — a population of persistent performer profiles carrying appearance attributes and performance media, and the submission: the transaction that binds a profile to an opportunity, initiated by the performer or their representative and delivered into a casting-side review space. Around this exchange, mature products add two-directional discovery (role search with saved filters and match alerts; talent-database search), a representative layer (rosters, submit-on-behalf with criteria autofill, packages), status feedback (alerts, requests, submission tracking), self-tape and scheduling entry points that hand off to the selection funnel, privacy and trust machinery, and talent-side monetization. The Type's defining work ends at the matched exchange; running the funnel from audition to recorded casting decision belongs to Audition Management, which platforms commonly bundle but which does not define them. The definition survives the paper era (breakdown releases, headshot files, submission drops) and does not depend on any digital-era feature.
