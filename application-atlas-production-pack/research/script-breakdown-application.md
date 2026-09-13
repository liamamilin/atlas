# Research Notes — Script Breakdown Application

## Research Goal

Understand what a Script Breakdown Application actually is as an Application Type: its defining core, its standard capabilities, its variants, and its boundaries against the neighboring Types in the production chain (screenwriting upstream, scheduling/call-sheet downstream, production management suites around it).

Research date: 2026-09-09.

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: parse a screenplay scene by scene and inventory every production element (cast, background, props, wardrobe, makeup, vehicles, animals, SFX/VFX, sound, stunts, set dressing, locations…) needed to shoot each scene; output breakdown sheets and category reports.
- Users: 1st AD, production manager/line producer, department heads, producers, coordinators; also film students.
- Nearest neighbors: Production Scheduling / Call Sheet Application (downstream consumer of the breakdown), Screenwriting Application (upstream producer of the script), Film Production Management (broader suite that bundles breakdown), Storyboard Application (shot visualization), Casting Platform (talent pipeline).
- Unknowns: Is the breakdown definitional without scheduling integration? Is the category taxonomy definitional? Is AI/auto-detection now definitional? Where exactly is the seam with the scheduling Type (which was processed as a sibling leaf the same day)?

Important context: the sibling leaf `production-scheduling-call-sheet-application` was processed 2026-09-09 and its synthesis explicitly reserves "scene inventory" as script-breakdown territory and binds the chain "breakdown feeds scheduling, schedule feeds call sheet". This pass must align with that seam.

## Research Questions

1. What is the canonical workflow from script to breakdown outputs?
2. What objects exist (script, scene, element/tag, category, breakdown sheet, report) and how do they relate?
3. What is tagged and how (text selection, auto-detection, AI)?
4. What outputs does the breakdown produce, and which of them belong to the breakdown vs to scheduling?
5. How do script revisions flow into an existing breakdown?
6. How do departments collaborate on the breakdown?
7. Where is the seam vs screenwriting (script text as primary object) and vs scheduling (scenes as schedule units)?
8. Do standalone (non-suite) breakdown tools exist — i.e., is scheduling integration definitional?
9. Historical check: does the paper-era breakdown process satisfy the candidate core?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Evidence quality |
|---|---|---|
| StudioBinder | Cloud all-in-one production management; breakdown as one "solution" beside write/visualize/plan/shoot; US market; indie→studio | Strong: product page + 148-article support collection + getting-started article |
| Yamdu | Cloud production management, European market, film/TV/commercial/documentary; breakdown as "backbone of the entire project"; studio-grade security (TPN) | Strong: root + film page + detailed official blog on collaborative breakdown |
| Gorilla (Jungle Software) | Desktop-first veteran (since 2002) now also online; scheduling/budgeting suite where breakdown feeds stripboard; indie/pro; education mode | Strong: root + Gorilla Scheduling Online page + Breakdown Assistant AI page |
| Celtx | Entry-level / education-heavy all-in-one studio (writing → pre-production → production); 7M+ users, 25k+ institutions | Strong: root + dedicated Breakdown product page |

Boundary references (not sampled as representatives):

- Final Draft — screenwriting-first; its breakdown/tagging capability could not be confirmed from official docs (knowledge base unreachable, see Sources). Third-party evidence (Jungle's Breakdown Assistant AI) shows tagged `.fdx` files import into Final Draft, i.e., Final Draft participates in the breakdown interchange as a writer/reader of tagged scripts.
- Movie Magic Scheduling — scheduling-side consumer; official docs unreachable (consistent with the sibling pass's finding). The `.sex` (Movie Magic scene-element) export path documented by Jungle confirms breakdown→scheduling interchange.

## Sources

Fetched 2026-09-09 (all Layer A unless noted):

- StudioBinder — Script Breakdown Software product page: https://www.studiobinder.com/script-breakdown-software/
- StudioBinder — Support Center, Breakdown collection (148 articles, titles observed): https://support.studiobinder.com/en/collections/10571900-breakdown
- StudioBinder — "Getting started with breakdowns": https://support.studiobinder.com/en/articles/7874878-getting-started-with-breakdowns
- Yamdu — root: https://www.yamdu.com/en/
- Yamdu — Film page: https://www.yamdu.com/en/for-productions/film/
- Yamdu — official blog "Software for Collaborative Script Breakdown and Shots": https://www.yamdu.com/en/blog/collaborative-script-break-down-sheet/
- Jungle Software — root: https://www.junglesoftware.com/
- Jungle Software — Gorilla Scheduling Online: https://junglesoftware.com/gorilla-scheduling-online/
- Jungle Software — Breakdown Assistant AI: https://junglesoftware.com/breakdown-assistant-ai-web/
- Celtx — root: https://www.celtx.com/
- Celtx — Breakdown product page: https://www.celtx.com/product/pre-production/breakdown/
- Final Draft — Final Draft 13 product page (screenwriting positioning): https://www.finaldraft.com/products/final-draft-13/

Source-access limitations:

- kb.finaldraft.com (Zendesk knowledge base) — two fetch attempts failed (timeout, transport error). Abandoned per network rules. Final Draft's own breakdown/tagging documentation therefore NOT directly observed; Final Draft held as boundary-adjacent, not a sampled product.
- entertainmentpartners.com (Movie Magic) — not fetched this pass; sibling pass on the same date found EP official docs unreachable. `.sex` interchange evidence taken from Jungle's own pages (Layer A for Jungle's claims about its own product; Layer B- for Movie Magic behavior).
- support.studiobinder.com returned 502 twice before succeeding on retry — content obtained on retry, treated as reachable.

## Product Observations

### StudioBinder

Key observations (Layer A):

- Official definition (support article): "A script breakdown is the process of identifying all the script elements needed to prep, schedule and budget a Film Production. This can include cast, extras, props, set dressing and more."
- Product page: "Tag script elements like props, wardrobe, cast and more"; breakdown is one solution beside Stripboards (shooting schedules), Reports (DOOD), Script Sides.
- Script import: "importing an existing PDF, Final Draft, Fountain, or TXT file" or write directly in StudioBinder.
- Tagging: "select-and-tag elements with a clean, easy drop down menu. Every element is highlighted in industry-standard script breakdown colors with customizable categories and script elements."
- Auto-assign: "When characters have dialogue in a scene, we automatically assign cast ID's."
- Script editor + Version Manager: script changes from the breakdown; "all versions are archived and can be restored"; "Roll back between script versions."
- Element Manager: "a complete, searchable inventory of tagged elements. Each element has its own profile page where you can create linked element groups, add notes, images, docs."
- Sync: "stripboards, shot lists, storyboards, calendars, call sheets, etc. … as you break down a script, all of your work is automatically updated across StudioBinder's other features."
- Reports: "breakdown summaries, element lists, DOOD reports, and shooting schedules — all filtered by scenes, elements, cast, locations, or shoot day."
- Scene operations (feature list + support titles): add/duplicate scenes, omit scenes (remove and restore; view omitted; restore omitted), delete scene, scene notes, edit scene synopsis, time estimates (prep/shoot/total), assign shoot locations, search scenes, adjust breakdown columns, keyboard shortcuts, add script days to breakdown strips.
- Element operations (support titles): tag elements, tag an element in more than one category, tag elements that aren't mentioned in the script (manual elements), add elements manually, assign tagged element to a different category, bulk rename, merge multiple elements, merge cast members, remove all mentions of an element at once, view all scenes an element is tagged in, element notes/images, custom element categories, remove categories, cast ID numbers, character list PDF, elements PDF/CSV.
- Revision handling: "How to import a revised script via breakdowns."
- Collaboration: share links/PDFs, invite collaborators to comment, "invite team members, assistants, or multiple departments, to help you tag script elements."
- Positioning: "designed with AD's in mind."

### Yamdu

Key observations (Layer A):

- Root: "Create script breakdowns, shooting schedules, call sheets, time cards…"; "Script Import & AI-Enhanced Breakdowns — Import scripts from our partners Final Draft (plus PDF and other script formats) and let Yamdu's AI create breakdown suggestions for the creative departments to confirm and populate."
- Film page: "import an existing one (e.g., from Final Draft, PDF, or other formats) and utilize it on the same platform that you break down and tag elements with your departments. Allow for cross-departmental collaboration."
- Official blog (detailed workflow):
  - Definition: "A script breakdown is an overview of each scene, showing all narrative elements and production notes by all departments. Think of a breakdown as an essential to-do-list. This collection of 'what is needed to shoot a scene' is the foundation for a meaningful shooting schedule."
  - "Yamdu uses the breakdown as the backbone of the entire project. This information naturally flows to the shooting schedule."
  - Script import with full version control: Final Draft, Celtx, Fountain, PDF (Hollywood format); "With every new version, Yamdu will show you all detected changes to scenes, characters, and sets… merging narrative elements… full control over split and merged scenes… strike-outs for omitted scenes… automatic versioning of imports clearly shows who made changes and when, with the option to go back to older versions."
  - Tagging: "the script tagging tool helps you and your departments quickly run through the script scene by scene and mark every essential element. Whereas characters and sets are detected automatically, every other word or line can be highlighted and turned into an element for your preferred category."
  - Default categories (vendor's own list): Characters; Extras (with quantity field); Costumes; Make-up & Hair; Construction; Set dressing; Props; Vehicles; Graphics; Food; Animals; Visual Effects; Special Effects; Sound; Camera & Lighting; Stunts. "You can either create your own categories or use Yamdu's default ones."
  - Scene-level general info: Scene/Shot ID, episode number, set, description/action line/slug line, environmental setting, color, mood, point in time, storyline, number of pages, page numbers, related shots, estimated time, scheduled duration, unit, cast type, production notes, continuity notes, shooting day.
  - Scene states: 'omitted' (created by an earlier script version, not part of current script); 'shot' (already filmed).
  - Comments with @-mentions per person/department; access rights per department ("departments can work in their areas… without messing with the data of other departments").
  - Scenes vs Shots: shots for commercials; characters/sets/elements linkable to shots; shot list/storyboard PDF export.
  - Downstream: "Everything you add while breaking down the script creates objects that can be used in each specific tool of Yamdu, from Casting to Costume Design, Make-up & Hair, Production Design and Location Scouting"; DOODs "for all elements linked to a scene and a schedule"; breakdown as PPM (pre-production meeting) agenda.
- Integrations: script import from Fountain, Final Draft, PDF, Celtx; schedule import from Movie Magic, Fuzzlecheck.

### Gorilla (Jungle Software)

Key observations (Layer A):

- Root: "For more than two decades, Jungle Software has helped filmmakers break down scripts, schedule productions, build budgets, and get to set." Products: Gorilla Scheduling (desktop + online), Gorilla Budgeting, Breakdown Assistant AI, Koala Call Sheets (separate call-sheet product), Gorilla Ratebook.
- Gorilla Scheduling Online: "Import your screenplay, break down scenes, build stripboards, organize shoot days, manage cast and crew, generate reports, and collaborate…"
  - "Import Final Draft or PDF screenplays and turn scenes into detailed production breakdowns with cast, props, locations, wardrobe, vehicles, and other production elements."
  - Stripboard & shoot days; cast/crew/locations with availability and conflicts.
  - Reports: "breakdown sheets, call sheets, element reports, location reports, and other production documents"; shooting schedules/one-liners; cast & Day-out-of-Days.
  - Education mode: "teach screenplay breakdown, stripboard scheduling, production planning, and reporting."
  - AI-assisted breakdown: "Use Breakdown Assistant AI… to help identify and organize production elements from your screenplay. Start with an AI-assisted breakdown, review the results, and continue refining."
- Breakdown Assistant AI page (standalone web product + Gorilla add-on):
  - "Breakdown Assistant AI reads your screenplay and tags Props, Set Dressing, Wardrobe, and more — so you can start scheduling in minutes, not days."
  - Standalone web version works with ANY scheduling software: upload .fdx or PDF → AI tags scene by scene → review/edit every tag or category → "Download your tagged script as .fdx or .sex" → "Import into any scheduling program" (Movie Magic Scheduling, Final Draft, Gorilla).
  - "Exports tagged .fdx and .sex files that import into Movie Magic Scheduling, Final Draft, Gorilla Scheduling, and any program that reads these formats."
  - "The breakdown is the slowest part of preproduction." / "Your breakdown is the slowest part of getting your script into Movie Magic Scheduling."
  - In-Gorilla version: "review each suggested element with its confidence score and reasoning, then accept or reject — approved elements land directly on your breakdown sheets and stripboard."
  - Marketing framing confirms the manual baseline: "Stop Highlighting. Start Scheduling." (highlighting = the traditional manual tagging act).

### Celtx

Key observations (Layer A):

- Product tree: Writing / Story Development / Pre-production (Breakdown, Catalog, Shot List, Schedule, Cast & Crew, Script Sides) / Production (Budget, call sheets, reports).
- Breakdown page: "Tag script elements and generate a catalog of production assets for your shoot."
- "Why spend hours color-coding and tagging script assets for pre-production, when Celtx can do it for you?" (confirms manual color-coding as the traditional baseline).
- How it works (5 steps, official):
  1. Upload a Script — "a script you wrote with Celtx, or easily import one… accepts many of the popular scriptwriting software file formats."
  2. Tag Assets — "Highlight text in your script and tag it as a production asset. Assign script elements a category and easily identify them using color coding."
  3. Add Details — "add, edit, or remove details and assigned categories of tagged script elements without leaving the script editor."
  4. Sync With Other Pre-Production Tools — "Assets… automatically populate your catalog and schedule stripboard."
  5. Generate Breakdown Sheets — "All tagged assets in each scene are conveniently categorized, and organized by shoot day."
- Root: "break down your script scene by scene"; revision tracking in production tools.

### Final Draft (boundary-adjacent, not sampled)

- Product page confirms screenwriting-first positioning (formatting, Beat Board, revisions, PDF export) with no breakdown claims observed on the fetched page.
- Layer B- (third-party): Jungle documents tagged `.fdx` as an interchange format that Final Draft reads — i.e., Final Draft participates as writer/reader of tagged scripts. Its own breakdown documentation was not reachable; no claims made beyond this.

## Cross-product Comparison

| Structure / capability | StudioBinder | Yamdu | Gorilla | Celtx | Evidence layer |
|---|---|---|---|---|---|
| Script as source (import FDX/PDF/Fountain or write in-product) | ✓ (PDF/FD/Fountain/TXT or write) | ✓ (FD/PDF/Fountain/Celtx) | ✓ (FD/PDF) | ✓ (own or imported, popular formats) | B (4/4) |
| Script parsed into scene records | ✓ (scene navigation, add/delete/duplicate scenes) | ✓ (scene-by-scene; scene IDs) | ✓ ("turn scenes into detailed production breakdowns") | ✓ ("scene by scene") | B (4/4) |
| Tagging = select script text → assign production category | ✓ (select-and-tag dropdown) | ✓ (highlight word/line → element in category) | ✓ (screenplay tagging) | ✓ (highlight text → tag as asset) | B (4/4) |
| Production categories, customizable | ✓ (custom categories) | ✓ (16 defaults + custom) | ✓ (props/wardrobe/etc.) | ✓ (assign category) | B (4/4); specific lists differ per product → A |
| Category color coding | ✓ ("industry-standard script breakdown colors") | ✓ (implied by tagging UI) | ✓ (color-coded AI results) | ✓ (color coding) | B (4/4) |
| Auto-detection of characters/sets | ✓ (auto cast IDs on dialogue) | ✓ (characters & sets detected automatically) | — (AI tags elements) | ✓ ("Celtx can do it for you" auto-identify) | B (3/4 observed) |
| AI first-pass tagging | not observed | ✓ (AI breakdown suggestions) | ✓ (Breakdown Assistant AI) | not observed | B (2/4) — common, not universal |
| Element inventory / per-element records | ✓ (Element Manager, profiles) | ✓ (breakdown objects reused across tools) | ✓ (element reports) | ✓ (Catalog auto-populated) | B (4/4) |
| Manual elements not in script | ✓ (explicit support article) | ✓ (any word/line can become element) | — | ✓ (add details) | B (2–3/4) |
| Per-scene breakdown sheets as output | ✓ (PDF of breakdown) | ✓ (breakdown per scene; PPM agenda) | ✓ (breakdown sheets) | ✓ (Generate Breakdown Sheets) | B (4/4) |
| Cross-scene category reports / element lists | ✓ (element lists, breakdown summaries, character list) | ✓ (objects flow to department tools) | ✓ (element/location reports) | ✓ (catalog) | B (4/4) |
| Scene attributes (synopsis, pages, estimates, notes) | ✓ (synopsis, time estimates, notes, columns) | ✓ (rich scene info list) | ✓ (page counts, scene details) | ✓ (details) | B (4/4) |
| Omit scene (strike-out, restorable) vs delete | ✓ (omit/restore/view omitted; delete separate) | ✓ (strike-outs for omitted scenes) | — | — | B (2/4) — production convention, product-specific depth |
| Script revision re-import / versioning | ✓ (import revised script; version manager) | ✓ (version diffing, merge/split control, who/when) | — | ✓ (revision tracking) | B (3/4) |
| Sync downstream to schedule/stripboard | ✓ (stripboards, call sheets) | ✓ (backbone → shooting schedule) | ✓ (breakdown → stripboard) | ✓ (catalog + stripboard auto-populate) | B (4/4) |
| DOOD reports | ✓ (DOOD reports) | ✓ (DOODs from elements+schedule) | ✓ (Day-out-of-Days) | — | B (3/4) — sits on schedule side |
| Department-scoped collaboration | ✓ (invite departments to tag) | ✓ (department access rights, @-mentions) | ✓ (collaborators) | ✓ (collaboration) | B (4/4) |
| Standalone breakdown without scheduling | Breakdown Assistant AI Web (Jungle) is standalone; paper breakdown historical | — (suite) | — (suite) | — (suite) | A (1 product) + historical practice |
| Shots layer (commercials) | — | ✓ (scenes vs shots) | — | — | A (1 product) — variant |
| Education segment | ✓ (schools & universities page) | ✓ (education pages) | ✓ (built for film schools) | ✓ (education-heavy) | B (4/4) — segment, not structure |

## Canonical Model

### L0 — Defining Invariant (deliberately small)

A Script Breakdown Application is recognizable by exactly four jointly-held structures:

1. **The script as the source of record** — a screenplay (imported in a recognized format or written in-product) held as the authoritative document from which the breakdown is derived. Remove → an element/props database with no script linkage.
2. **The scene as the unit of breakdown** — the script is held as scene-derived records (scene number/heading, synopsis, page count) and the breakdown proceeds scene by scene. Remove → a flat annotation layer over text.
3. **Element tagging bound to script text and classified by production category** — selecting/highlighting text in the script and turning it into an element record assigned to a production category (cast, props, wardrobe, vehicles, effects…). Remove → a screenwriting/reading app, or generic text annotation.
4. **Breakdown outputs** — per-scene breakdown sheets and cross-scene category reports/lists aggregated from the tags. Remove → tagging with no deliverable.

Jointly-held load-bearing:

- 1 alone = screenwriting/script-reading app
- 2 alone = scene list
- 3 without 1+2 = generic text annotation tool
- 4 without 1–3 = report templates over nothing
- 1+2 without 3+4 = script reader with scene navigation
- 1+3 without 2 = flat annotation (no scene structure)
- 2+3 without 1 = scene inventory detached from the script (drifts toward scheduling territory)
- 1+2+3 without 4 = tagging with no deliverable

### L1 — Common Mature Structure

- Element inventory as first-class records (searchable, per-element profile, scenes-tagged-in, merge/rename, notes/images)
- Character/cast handling: auto-detection from dialogue, cast IDs, merging duplicate characters
- Scene attributes: synopsis, page count, time estimates, location assignment, notes
- Script revision handling: re-import revised script, change detection, version archive/rollback
- Manual elements (tag things not literally in the script)
- Downstream sync: tags auto-populate catalog/schedule/stripboard/call sheets in bundled products
- Category color coding (industry-conventional colors)
- Department-scoped collaboration and comments
- Reports: breakdown summaries, element lists, character lists, PDF/CSV export

### L2 — Variant / Optional Structure

- AI first-pass tagging with human accept/reject review (2/4 sampled; era-current)
- Standalone breakdown utility exporting tagged interchange files (.fdx/.sex) for use in other scheduling programs (1 product, plus paper-era practice)
- Shots layer alongside scenes (commercials; 1 product)
- Omit-vs-delete scene machinery depth (2/4 explicit; production convention)
- DOOD reports (3/4; sits on the scheduling side of the seam)
- Budget integration (element categories → budget categories; separate products in-sample)
- Deployment: desktop vs cloud; security posture (watermarking, TPN, permissions) for studio work
- Segment packaging: education modes; indie vs studio tiers

### L3 — Vendor-specific (research notes only)

- Yamdu's 16 default categories and its long scene-attribute list (episode number, unit, cast type, continuity notes…)
- StudioBinder's "solution" packaging (Breakdown/Stripboards/Sides/Reports), breakdown columns, script days on strips
- Jungle's Breakdown Assistant AI pricing/packaging ($19/script, 150 scenes/month, confidence scores), .sex export
- Celtx's 5-step onboarding framing and Catalog auto-population
- StudioBinder's "designed with AD's in mind" positioning

### Historical / market-sample check (§24)

Paper-era breakdown: the production team goes through the physical script scene by scene, highlights/underlines elements with colored pens per category, and fills out a paper breakdown sheet per scene; category lists are then compiled by hand. This satisfies all four L0 structures (script as source; scene as unit; tagging by category; breakdown sheets as output) with no cloud, no AI, no auto-detection, no scheduling integration, no version machinery. The Type therefore predates and is independent of the modern suite packaging. Conversely, modern conveniences (auto-detection, AI, cloud sync, DOOD) must NOT enter the definition. Check passed.

Also checked: a screenwriting tool without tagging (pure writer tool) fails L0-3/4 → not this Type; a scheduling tool holding scene strips without script-bound tagging fails L0-1/3 → scheduling territory (consistent with the sibling pass).

## Vendor-specific Findings

See L3 above. None of these enter the canonical document.

## Boundary Findings

1. **vs Production Scheduling / Call Sheet Application** (sibling leaf, processed same day): the breakdown produces the scene-and-element inventory; scheduling consumes scenes as units to build shooting days and produce call sheets. The seam, from this side: remove the script-bound tagging and the element inventory, keep scene records arranged on a stripboard → scheduling territory. From the sibling side: "remove → scene inventory = script-breakdown territory." The chain binding (breakdown feeds scheduling, schedule feeds call sheet, upstream changes flow downstream) is shared vocabulary across both passes. DOOD reports sit on the scheduling side (they require a schedule), though breakdown tools commonly generate them once a schedule exists.
2. **vs Screenwriting Application**: screenwriting's primary object is the script text itself (writing, formatting, revising); breakdown's primary object is the element inventory derived from that text. The seam: delete the tagging/inventory/outputs and what remains is a screenwriting app. Final Draft straddles the seam (screenwriting-first, participates in tagged-.fdx interchange); breakdown suites all import scripts rather than own them.
3. **vs Film Production Management (broader suites)**: production management adds cast/crew records, calendars, files, budgeting, time cards, security. Breakdown is one module; standalone breakdown utilities exist (Breakdown Assistant AI Web; paper practice), so suite membership is not definitional.
4. **vs Storyboard Application**: storyboards visualize shots (image per shot); breakdown inventories production elements per scene. Different objects, different users' deliverables.
5. **vs Casting Platform**: casting manages the talent pipeline (database, submissions, auditions); breakdown identifies cast requirements per scene (characters, extras, cast IDs). Breakdown objects may flow into casting tools (Yamdu) but the Types are distinct.
6. **vs Budgeting**: element categories can map to budget lines; budgeting is a separate Type (Gorilla Budgeting is a separate product; Celtx Budget separate module).

## Uncertainties

- Final Draft's own breakdown/tagging feature set could not be verified from official docs (KB unreachable). Held as boundary-adjacent; no claims made about its tagging UI depth.
- Movie Magic Scheduling's breakdown import behavior is evidenced only through Jungle's descriptions of the `.sex` interchange (third-party but specific and self-interested-accurate). Not directly verified.
- Whether "industry-standard breakdown colors" constitute a formal standard or a strong convention was not researched beyond the vendors' own use of the phrase; treated as convention.
- Exact default category lists differ per product (Yamdu's 16 observed; others not exhaustively enumerated); the canonical claim is "production categories, customizable", not any specific list.
- Celtx's auto-identification depth ("Celtx can do it for you") is marketing-phrased; treated as auto-assist, not verified in detail.

## Final Synthesis

The Script Breakdown Application is the pre-production inventory tool of the film/TV/commercial production chain. Its defining core is small: a script held as source of record, broken down scene by scene, by tagging script text into production-category element records, and rolled up into per-scene breakdown sheets and cross-scene category reports. Everything else commonly seen — element managers, cast IDs, revision diffing, department collaboration, AI first-pass tagging, downstream sync to stripboards/catalogs/call sheets, DOODs — is standard mature structure or variant machinery layered on that core. The Type sits between screenwriting (upstream, owns the script text) and scheduling/call-sheet production (downstream, owns the shooting days), and is usually bundled inside production-management suites while remaining definitional without them (standalone utilities and the paper-era practice both satisfy the core).
