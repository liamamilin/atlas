# Research Notes — Film Production Management

Research date: 2026-09-07

## Research Goal

Understand what "Film Production Management" software actually is as an Application Type: its core object model, its defining pipeline (script → breakdown → schedule → daily dispatch), who uses it, what states and rules govern it, and where its boundaries sit against neighboring Types (TV Production Management, Production Scheduling / Call Sheet Application, Production Accounting Platform, Script Breakdown Application, Casting Platform, Media Asset Management, generic Project Management).

## Initial Boundary (hypothesis before research)

- Core hypothesis: software that plans and runs a film production — script breakdown, shooting schedule (stripboard), call sheets, cast/crew/location management, production reports, and commonly budgeting.
- Likely users: line producers, unit production managers, 1st assistant directors, production coordinators, producers.
- Likely confusions:
  - vs TV Production Management (series/episodes) — possibly one Type with a variant split.
  - vs Production Scheduling / Call Sheet Application — possibly a capability slice of this Type.
  - vs Production Accounting Platform — actuals/payroll vs planning/estimating.
  - vs generic Project Management — scene-based units and production-specific semantics.
- Unknowns: is budgeting definitional? Is the call sheet definitional or just universal? Does the Type require AI/cloud? How do products handle script revisions?

## Research Questions

1. What is the core object model? (production/project, script, scene, breakdown element/category, stripboard/schedule, shooting day, call sheet, cast/crew, location, budget, reports)
2. How does the script → breakdown → schedule → call sheet pipeline work, step by step?
3. What happens when the script or schedule changes — how do downstream artifacts propagate?
4. What lifecycle/state does a shooting day and a call sheet have?
5. Who uses the system and what does each role see/do?
6. How does budgeting relate to this Type vs the Production Accounting sibling?
7. What daily-execution machinery exists (call sheet distribution/tracking, time cards, daily reports)?
8. What is invariant across cloud SaaS, desktop, European, and AI-first products — and what would the paper-era / desktop-era equivalents satisfy?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

1. **StudioBinder** — cloud all-in-one production management suite; indie/SMB through enterprise marketing/entertainment teams; production-management-led (writing attached).
2. **Yamdu** — European cloud production management platform; film/TV/commercial/documentary; mid-to-large productions and co-productions; full lifecycle incl. budgeting, time cards, sustainability.
3. **Filmustage** — AI-first pre-production platform; indie to major studios; breakdown/schedule/budget/call sheets generated automatically with human confirmation.
4. **Gorilla (Jungle Software)** — scheduling + budgeting specialist with two decades of desktop heritage, now also online; indie/professional tier; modular products (Scheduling, Budgeting, Koala Call Sheets, Breakdown Assistant AI).
5. **Celtx** — script-first cloud suite (screenwriting-led) with pre-production and production modules; education and business segments.

Also referenced (third-party corroboration only): **Movie Magic Scheduling / Budgeting (Entertainment Partners)** — the long-standing industry-standard professional scheduling/budgeting products. Entertainment Partners' own site could not be reached (see Sources); Movie Magic appears in this research only through other vendors' official integration lists, testimonials, and comparison pages.

Rejected sample: **Wrapbook** — initially considered; its official site positions it as "Digital Production Payroll & Production Accounting" (payroll, accounts payable, production accounting, onboarding, data insights) with no script breakdown / stripboard / call sheet machinery. This is the Production Accounting Platform + payroll territory, not this Type. Recorded as a Product Mismatch per the workflow's escalation conditions.

## Sources

Directly fetched official sources (2026-09-07):

- StudioBinder — main site (https://www.studiobinder.com/), film scheduling product page (/film-scheduling-software/), call sheet product page (/call-sheet-builder/). Support subdomain (support.studiobinder.com) returned HTTP 502 — not accessible.
- Yamdu — main site (https://www.yamdu.com/en/).
- Filmustage — main site (https://filmustage.com/); help center exists at help.filmustage.com (not fetched).
- Jungle Software / Gorilla — main site (https://www.junglesoftware.com/).
- Celtx — main site (https://www.celtx.com/) and breakdown product page (/product/pre-production/breakdown/).

Source-access limitations:

- **Entertainment Partners (Movie Magic Scheduling / Budgeting)**: three URL attempts (product page paths, root, support portal) failed (404 / non-documentation portal). Per the network-restriction rule, the source was abandoned after repeated failures. All Movie Magic statements in this research rely on third-party official corroboration (Yamdu's and Filmustage's integration lists, a Filmustage testimonial from a producer citing ~30 years of Movie Magic scheduling use, StudioBinder's public comparison page). No precise Movie Magic feature claims are made.
- StudioBinder help center (502) and Filmustage help center (not fetched): product pages were used instead; operational details below are limited to what product pages state.
- Wrapbook: fetched as a candidate sample; used only as boundary evidence.

## Product Observations

### StudioBinder (evidence layer: A — direct official observation)

- Self-labels: "Video, TV & Film Production Management Software"; homepage pipeline: Write → Breakdown → Visualize → Plan → Shoot.
- Script: write in-product (screenplays, AV scripts, docs) or import Final Draft / PDF / Fountain / TXT; "every scene is automatically added to your stripboard."
- Breakdown: "tag scene elements to create an organized, shareable inventory of props, set dressing, costumes, equipment, VFX, and more"; custom breakdown categories; reports include breakdown summary and element lists.
- Stripboard (shooting schedule): scene strips; drag-and-drop or auto-schedule by scene criteria (setting, day/night, INT./EXT.); day breaks inserted by page count or estimated shoot time; banners for meal breaks, company moves, estimated shoot time, production notes; boneyard for omitted scenes (removable and returnable); duplicate schedule to compare variations; search/filter strips by heading, INT/EXT, cast, location; toggle strip details (cast, shoot location, page count, script day, elements, prep, shoot time); PDF/CSV export.
- Script hygiene: standardize cast names, sets, locations, times of day to prevent duplicate stripboard entries; global or scene-level edits without reimport.
- Reports: shooting schedules, one-liner schedules, DOOD reports, breakdown sheets, daily sides.
- Call sheets: generated from the stripboard, auto-populated with cast, shoot locations and map links, company details, contacts, live weather, banners, schedule details; customizable (show/hide/rearrange elements, logos, colors, columns); templates; call sheet types (shoot day, scout, rehearsal); daily agenda (call times for cast, crew, meal breaks, wrap); parking details; hospital/emergency info; footer notes (walkie channels); attachments (shot lists, storyboards, sides); next-day schedule; atmosphere tally; 12/24-hour and °F/°C toggles.
- Call sheet distribution & tracking: send via email and SMS; per-recipient status dashboard — sent / viewed / confirmed / undeliverable; reminders and last-minute changes; timestamped confirmations.
- People: production contacts ("rolodex"), integrated into all features, transferable between projects.
- Collaboration: share schedule by link or invite editors; comments; task boards; production calendar; media library/file sharing.
- TV: "Episodic Structure" listed as a feature.
- No budgeting module appears anywhere in the product's feature lists (blog offers budget templates as documents, not a product module).

### Yamdu (evidence layer: A)

- Self-labels: "The Production Management Software for Films and Media"; "unifies your media production operations… Create script breakdowns, shooting schedules, call sheets, time cards, and align all your projects in one single source of truth."
- Audience pages: Film, TV Series, Commercial, Documentary; role pages for producers, line producers, production managers, production coordinators (plus DOP, director, writer, casting director, location manager).
- Script import: Final Draft, PDF, Fountain, Celtx; AI-enhanced breakdown suggestions that creative departments confirm and populate.
- Schedule: import existing schedules (Movie Magic, Fuzzlecheck) or assemble stripboard by dragging scenes; DOOD reports generated in real time.
- Call sheets: templates, auto-fill, edit/customize, send and track.
- Budgeting: "Dynamic Globals®" — link shooting and production schedules to the budget; import data.
- Time cards: in-app work-time tracking with visibility and approval, built on reusable labor-agreement templates; estimates; export to payroll provider.
- Sustainability: CO₂e budgeting integrating calculators (PEAR, MEDIA Carbon Calculator, KlimAktiv); multi-country co-production budgeting.
- Calendars: project calendar (all events/off-periods) + production calendar (Gantt from prep to shoot to post).
- People: cast & crew hub — advertise jobs, hire, collaborate, share information.
- Communication: announcements to cast/crew mailing lists, file sharing, structured comments.
- Security: watermarking of scripts/videos/files sent to cast and crew; tracking of who viewed/edited/uploaded/downloaded/commented; advanced per-position permissions; TPN membership; GDPR posture; Azure hosting.
- Integrations: Final Draft, Fountain, PDF, Celtx (script in); Movie Magic, Fuzzlecheck (schedule in); Showbiz Budgeting (schedule out); Google Calendar/iCal/Outlook; Slack; Zapier; Lockit Script; MovieLabs OMC-based API.
- Multi-language product (EN/DE/ES/PT/FR/IT/PL/HU/NO/DA/FI/SV).

### Filmustage (evidence layer: A)

- Self-labels: "The Complete AI Pre-Production Platform"; "Every step from locked script to first shooting day — breakdowns, schedules, budgets, and call sheets, built automatically with your input and kept in sync."
- Content scope: "Films, Series & TV Shows", short & vertical dramas, podcasts; any language & format.
- Core promise: "Every tool feeds the next. Change the script — your breakdown, schedule, budget, and call sheets update with it."
- Breakdown: AI auto-tags cast, props, locations, VFX, wardrobe; tracks every element mention across the script; user confirms/corrects; feeds schedules and budgets.
- Schedule: professional stripboard + drag-and-drop calendar; AI Production Agent analyzes risks, optimizes shooting days, executes structured changes with preview and approval; time estimates; real location tagging; workload balancing; conflict detection; DOOD reports and call sheets auto-update.
- Budgeting: auto-generates budget categories from breakdown and schedule (cast, crew, props, locations become line items); location-based cost estimates; fringes and deductions.
- Call sheets: automatically transformed from the shooting schedule; customizable/editable.
- Sides: assembled from the shooting schedule (shoot or script order); per-department filtered views (cast, location, INT/EXT, tag category); QR code on every page for version confirmation on set; call sheet + sides bundled into one PDF.
- Storyboards/annotations: connected to script scenes and breakdowns; per-department annotation layers.
- Team access: invite by email; per-feature permission levels (None / View / Edit / Full) — e.g., line producer lives in the budget, a VFX vendor sees VFX only; team chat.
- Security: SOC 2 Type II, TPN membership, forensic watermarking, "we do not use your data for training."
- Integrations: Movie Magic, Gorilla Scheduling, Final Draft.

### Gorilla / Jungle Software (evidence layer: A)

- Self-labels: "Production software built for the way you work. Desktop. Online. AI-powered."; "For more than two decades, Jungle Software has helped filmmakers break down scripts, schedule productions, build budgets, and get to set."
- Modular product family: Gorilla Scheduling (desktop + online), Gorilla Budgeting (desktop + online), Combo Pack, Breakdown Assistant AI (web), Koala Call Sheets (desktop), Gorilla Ratebook.
- Online products: "Schedule productions, build budgets, manage cast and crew, create reports, collaborate with your team, and work from anywhere."
- Screenshots on the site show: screenplay tagging (breakdown), breakdown lists, crew management.
- Heritage: desktop Mac/Windows products; academic pricing; training videos/webinars; subscription or one-time purchase models.

### Celtx (evidence layer: A)

- Self-labels: "Screen Writing Software for Storytellers"; script-first suite: Writing → Story Development (beat sheet, storyboard) → Pre-production → Production → Post (Premiere plugin).
- Pre-production modules: Breakdown, Catalog, Shot List, Schedule, Cast & Crew, Script Sides.
- Breakdown flow (product page): upload/import a script (popular formats) or write in Celtx → highlight text and tag it as a production asset with a category and color coding → add/edit/remove details without leaving the script editor → tagged assets automatically populate the catalog and the schedule stripboard → generate breakdown sheets with tagged assets per scene, organized by shoot day.
- Catalog: "talent, props, wardrobe, equipment, and locations organized — all in one place."
- Schedule: "automatically create a stripboard from your script"; schedule data auto-populates shoot-day documents.
- Production: Budget ("track expenses and prevent overruns"), call sheets ("dynamically generated and updated"), reports ("get a snapshot of your shoot").
- Cast & Crew: "track their every detail"; sides generated and distributed.
- Segments: education (educators/students; 25,000+ institutions claimed) and business; episodic projects supported in writing.

### Movie Magic Scheduling / Budgeting (evidence layer: B/C — third-party corroboration only)

- Positioned by other vendors' official materials as the industry-standard scheduling/budgeting reference: Yamdu and Filmustage both offer Movie Magic schedule/script import; a Filmustage testimonial (producer) cites ~30 years of personal Movie Magic scheduling use; StudioBinder maintains a public comparison page against it.
- No direct official documentation was reachable; no precise feature claims are made here. Its role in this research is as the professional-pole reference point whose data formats other products import/export.

## Cross-product Comparison

| Structure | StudioBinder | Yamdu | Filmustage | Gorilla | Celtx | Movie Magic (3rd-party) |
|---|---|---|---|---|---|---|
| Production/project container | ✓ (projects) | ✓ (projects, "single source of truth") | ✓ (project) | ✓ | ✓ (studio projects) | ✓ |
| Script import / authoring | ✓ (write or import FD/PDF/Fountain/TXT) | ✓ (FD/PDF/Fountain/Celtx) | ✓ (any language/format) | ✓ (tagging shown) | ✓ (write or import) | ✓ (implied by integrations) |
| Scenes auto-extracted to schedule | ✓ ("every scene automatically added to stripboard") | ✓ (stripboard assembly; schedule import) | ✓ (AI breakdown → stripboard) | ✓ | ✓ ("automatically create a stripboard from your script") | ✓ (implied) |
| Breakdown / element tagging | ✓ (tag elements, categories, custom categories) | ✓ (AI suggestions + human confirm) | ✓ (AI auto-tag + confirm) | ✓ (Breakdown Assistant AI) | ✓ (highlight & tag, categories, colors) | ✓ (implied) |
| Element catalog | ✓ (element lists/reports) | ✓ | ✓ | ✓ | ✓ (Catalog module) | ✓ (implied) |
| Stripboard / shooting schedule | ✓ (drag/auto-sort, day breaks, banners, boneyard, variants) | ✓ (drag-drop, schedule import) | ✓ (stripboard + calendar, AI optimization) | ✓ | ✓ | ✓ (implied) |
| Cast & crew records | ✓ (contacts, transferable) | ✓ (hub: jobs, hiring, collaboration) | ✓ (team access) | ✓ (crew management) | ✓ (Cast & Crew module) | ✓ (implied) |
| Locations | ✓ (Google Maps) | ✓ | ✓ (real location tagging) | ✓ | ✓ (catalog) | ✓ (implied) |
| DOOD reports | ✓ | ✓ (real-time) | ✓ (auto-update) | ✓ (reports) | — (reports generic) | ✓ (implied) |
| Call sheet generation | ✓ (from stripboard, auto-populated) | ✓ (templates, auto-fill) | ✓ (from schedule) | ✓ (Koala Call Sheets) | ✓ (dynamically generated) | ✓ (implied) |
| Call sheet distribution + tracking | ✓ (email/SMS, sent/viewed/confirmed/undeliverable) | ✓ (send and track) | ✓ (QR version check on sides) | — (not stated) | ✓ (distribute) | — |
| Sides | ✓ | — (not stated) | ✓ (from schedule, QR) | — | ✓ | — |
| Budgeting (estimating) | ✗ (no module in feature lists) | ✓ (Dynamic Globals, schedule-linked) | ✓ (auto from breakdown/schedule) | ✓ (separate product) | ✓ (budget + cost reporting) | ✓ (separate product, implied) |
| Time cards / work time | ✗ | ✓ (labor-agreement templates, payroll export) | ✗ | ✗ | ✗ | — |
| Sustainability / CO₂e | ✗ | ✓ | ✗ | ✗ | ✗ | — |
| Script-revision propagation | ✓ (edit script → stripboard updates; standardize names) | ✓ (implied by single-source-of-truth framing) | ✓ (explicit: change script → breakdown/schedule/budget/call sheets update) | — | ✓ (revision tracking; breakdown sync) | — |
| Per-feature permissions | — (not stated) | ✓ (advanced per-position permissions) | ✓ (None/View/Edit/Full per feature) | — | — | — |
| Watermarking / distribution tracking | ✓ (call sheet view/confirm tracking) | ✓ (watermarks, view/edit/download tracking) | ✓ (forensic watermarking) | — | — | — |
| AI assistance | — (not in sampled pages) | ✓ (breakdown suggestions) | ✓ (AI agent, auto-breakdown) | ✓ (Breakdown Assistant AI) | — (not in sampled pages) | — |
| Episodic/series support | ✓ (Episodic Structure) | ✓ (TV Series audience page) | ✓ (Series & TV Shows) | — (not stated) | ✓ (episodic projects) | ✓ (implied) |
| Deployment | Cloud SaaS | Cloud SaaS | Cloud SaaS | Desktop + Online | Cloud SaaS | Desktop (implied) |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

1. **The production as the container of record** — one identified film project holding its script, plan, people, and documents across prep → shoot. Remove → disconnected documents and point tools, not a management system.
2. **The script-derived scene as the atomic planning unit** — the unit of planning is the scene (with its script day, location, INT/EXT, day/night, cast), extracted from the script rather than authored as abstract tasks. Remove → generic project/task management.
3. **The shooting schedule as the organizing structure** — scenes arranged into shooting days (the stripboard tradition), with day breaks, ordering constraints (location, cast, time of day), and omitted scenes held aside rather than destroyed. Remove → a breakdown tool or a script tool with no plan of record.
4. **The daily operational dispatch to the production community** — the plan is carried to the people executing it, per shooting day, as the call sheet (the standard realization), with distribution and acknowledgment. Remove → planning-only software; the management loop never closes.

Historical check: this core describes the pre-software production office as well — the physical stripboard and the typed/photocopied call sheet are the paper-era realizations of structures 3 and 4; the scene/breakdown discipline predates software. The desktop era (Gorilla's two decades; Movie Magic's ~30-year usage history per third-party testimony) satisfies the same core without cloud, AI, tracking, or permissions. The core is therefore not an artifact of the current cloud-SaaS generation.

### L1 — Common Mature Structure

Very common across the sample (most products, most eras) but not required to recognize the Type:

- **Script breakdown with element categories** — tagging cast, props, wardrobe, vehicles, set dressing, equipment, VFX per scene; near-universal and tightly coupled to scheduling and budgeting, but scheduling can exist from scene headers alone (StudioBinder auto-populates the stripboard before any tagging).
- **Element catalog** — the accumulated inventory of tagged elements (Celtx ships it as a named module).
- **Cast & crew records** — people database with roles/departments and contact details, attached to scenes and documents.
- **Locations management** — location records with maps/notes.
- **Production reports** — DOOD (day-out-of-days), one-liner schedules, breakdown sheets, daily sides.
- **Schedule variants** — duplicate/compare alternate schedules; boneyard for omitted scenes.
- **Call sheet customization & templates** — show/hide/rearrange sections, saved templates, per-recipient notes.
- **Calendars** — production calendar / Gantt across prep–shoot–post.
- **Collaboration** — sharing, comments, tasks.
- **Budgeting (estimating)** — common but NOT universal: absent from StudioBinder's product feature set in this sample; shipped by Yamdu, Filmustage, Gorilla (separate product), Celtx, and (per third-party corroboration) Movie Magic Budgeting. Best classified as a common module, with dedicated budgeting products and the Production Accounting sibling carrying the deep-money work.
- **Document distribution security** — watermarking, view/download tracking (Yamdu, Filmustage; call-sheet confirmation tracking in StudioBinder).

### L2 — Variant / Optional Structure

Depends on segment, geography, era, deployment:

- Packaging: all-in-one suite (StudioBinder, Yamdu, Filmustage, Celtx) vs scheduling+budgeting specialist pair (Gorilla; Movie Magic per corroboration) vs script-first suite (Celtx).
- Deployment: cloud SaaS vs desktop (Gorilla desktop; Movie Magic desktop lineage).
- Content type: feature film vs TV series/episodic vs commercial/music video vs documentary vs short/vertical drama vs photography shoots (StudioBinder markets photoshoot call sheets).
- Customer tier: indie/student (Celtx education, Gorilla academic) vs mid-market vs studio/enterprise (Yamdu's broadcaster clientele; StudioBinder enterprise).
- Regional/regulatory posture: European co-production machinery, GDPR, multi-language (Yamdu) vs US-centric union/labor tooling elsewhere.
- AI posture: manual tagging vs AI-suggested breakdown with human confirmation vs AI agent executing schedule changes with preview/approval (era-typical; not definitional).
- Time tracking / time cards with labor-agreement templates and payroll export (Yamdu in this sample).
- Sustainability / CO₂e budgeting (Yamdu in this sample).
- Budget-to-actual linkage depth (estimating-only vs schedule-linked globals vs full cost tracking → Production Accounting sibling).

### L3 — Vendor-specific (research notes only)

- Yamdu: Dynamic Globals® (branded budget linkage), named CO₂e calculator integrations (PEAR, MEDIA Carbon Calculator, KlimAktiv), MovieLabs OMC-based API, Fuzzlecheck/Lockit Script integrations.
- Filmustage: "AI Dude" production agent, QR-coded sides for on-set version confirmation, call-sheet+sides single-PDF bundling.
- StudioBinder: boneyard terminology, call-sheet confirmation dashboard with per-recipient status, DOOD report generator, photoshoot call-sheet templates.
- Gorilla: Koala Call Sheets as a separate desktop product, Gorilla Ratebook.
- Celtx: beat sheet / story development layer, Adobe Premiere Pro plugin, education-sector positioning.

## Vendor-specific Findings

See L3. None of these were promoted into the canonical model.

## Rejected Findings

- **"Production management = payroll"** — rejected. Wrapbook (fetched candidate) is payroll/accounting; it lacks the scene/schedule/dispatch core. Payroll integration appears only as an export seam (Yamdu time cards → payroll provider).
- **"Budgeting is definitional"** — rejected as L0. StudioBinder, a self-described production management suite, ships no budgeting module; the Type is recognizable without it. Budgeting is a common module (L1) with a dedicated sibling Type for actuals.
- **"AI breakdown is definitional"** — rejected. Manual tagging (Celtx, Gorilla desktop heritage) satisfies the same structure; AI is the current implementation pole.
- **"Cloud collaboration is definitional"** — rejected. Desktop-era products (Gorilla desktop; Movie Magic lineage) satisfy the core without it.
- **"Daily production reports (end-of-day actuals) are core"** — not promoted: the sampled official pages evidence planning reports (DOOD, one-liners, breakdown sheets, sides) clearly, but end-of-day DPR machinery (pages shot, actual times) was not directly evidenced in the sample; kept as uncertain/optional.
- **"Call-sheet-only tools are this Type"** — rejected: they are a slice (see Boundary Findings); the directory carries them as a separate leaf.

## Boundary Findings

- **vs TV Production Management** — thinnest boundary. The sampled machinery is identical (same products serve both: StudioBinder "Video, TV & Film" with Episodic Structure; Yamdu has separate Film and TV Series audience pages over one product; Filmustage covers "Films, Series & TV Shows"). The difference is content-type structure: episodic containers (episodes, seasons, ongoing cycles) vs a single finite production. This looks like one Type with a series/episodic variant rather than two distinct Types. Recorded as a taxonomy question for joint review; this document is written so the film leaf stands on the single-production pole.
- **vs Production Scheduling / Call Sheet Application** — the sibling leaf is a capability slice of this Type (schedule + call sheets without the full production-office breadth: breakdown catalogs, budget, people hub, security). "Remove the surrounding production-office structures and keep schedule+call sheets → you get the sibling Type."
- **vs Production Accounting Platform** — money actuals vs planning. Wrapbook's official positioning (payroll, AP, production accounting, onboarding, reporting; no breakdown/stripboard/call sheets) demonstrates the seam: accounting platforms track what was spent; production management plans what will be shot. Budgeting (estimating) belongs to this Type as a common module; cost tracking/payroll belongs to the sibling.
- **vs Script Breakdown Application** — breakdown is one stage of this Type's pipeline; a standalone breakdown tool stops at tagging/catalogs without the schedule/dispatch loop.
- **vs Casting Platform / Audition Management** — talent discovery and selection vs managing already-chosen cast inside the production plan. Casting output (a cast list) is an input here.
- **vs Media Asset Management / MAM** — MAM governs recorded media/assets; production management governs the plan and people that produce them. Yamdu's file sharing is document distribution, not footage asset management.
- **vs generic Project Management Application** — the scene as script-derived unit, production-specific semantics (day breaks, call times, company moves, DOOD), and industry-standard documents (call sheets, sides) are what generic PM lacks. StudioBinder ships task boards as an auxiliary surface, not the core.
- **vs Screenwriting tools** — the script is an input here (imported, broken down, revised), not the deliverable. Celtx spans both, which makes it the clearest illustration of the seam: its identity is script-first, with pre-production attached.

**"Remove what to become the other Type" tests:**
- Remove scene-based units and production semantics → generic project management.
- Remove the schedule/dispatch loop, keep tagging → script breakdown tool.
- Remove breakdown/people/budget breadth, keep schedule+call sheets → Production Scheduling / Call Sheet Application.
- Replace planning with actuals/payroll → Production Accounting Platform.
- Add episodic containers/ongoing seasons as the primary structure → TV Production Management pole (variant question recorded).

## Uncertainties

- Movie Magic's exact current feature set is unverified (source unreachable); only its role as the professional scheduling/budgeting reference is asserted, via third-party official corroboration.
- Whether the earliest digital scheduling products shipped call-sheet generation is unverified; the call sheet's paper-era existence is common industry practice but was not directly sourced. L0 phrasing treats the dispatch as a structure with the call sheet as its standard modern realization.
- StudioBinder's budgeting absence is inferred from the absence of any budget module across its official feature pages (an absence claim, moderately strong but not from a help-center confirmation).
- Daily production report (end-of-day actuals) machinery: not directly evidenced in the sample; treated as optional/uncertain.
- Gorilla Online's full current surface (collaboration depth, permissions) is only partially evidenced from marketing pages; its desktop heritage and module split are well evidenced.
- Exact numeric limits (scene counts, recipient caps, plan gates) were not researched and are deliberately absent.

## Final Synthesis

Film Production Management is the production office's system of record for planning and running a film shoot. Its defining core is a four-part structure: a production container of record; the script-derived scene as the atomic planning unit; the shooting schedule that organizes scenes into shooting days (the stripboard tradition); and the daily operational dispatch (call sheets) that carries the plan to the cast and crew with distribution and acknowledgment. Around that core, mature products add script breakdown with element categories, people and location records, production reports (DOOD, one-liners, sides), schedule variants, calendars, collaboration, and — commonly but not universally — budget estimating. The script sits upstream as the input that seeds the whole pipeline; revisions propagate downstream through breakdown, schedule, and call sheets, which is why products emphasize a "single source of truth." Money actuals, payroll, and footage assets belong to neighboring Types. The film/TV split in the directory is better understood as a content-type variant of one machinery than as two distinct Types — recorded for joint review.
