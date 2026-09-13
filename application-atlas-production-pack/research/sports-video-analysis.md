# Research Notes — Sports Video Analysis

## Research Goal

Understand what "Sports Video Analysis" is as an Application Type: what its world is made of, who operates it, what the defining workflow is, and where its boundaries sit against the neighboring sports-software leaves (Sports Performance Analytics, Tactical Analysis Platform, Sports Scouting Platform, Sports Coaching Platform, Athlete Management System, Referee Management Platform) and against the non-sports neighbors (Video Editor, Media Asset Management, Video Streaming Platform).

## Initial Boundary

- Working hypothesis: software whose center is bringing sports footage in, breaking it down into structured analysis units (tagged events / clipped moments / annotated frames), and delivering that analysis back into a coaching or performance-review loop.
- Nearest neighbors identified up front:
  - **Video Editor (§04.06)** — timeline/sequence editing that produces a finished program; no sport semantics, no team review loop.
  - **Media Asset Management (§27)** — media ingest/catalog/distribution logistics for media organizations; sport-agnostic.
  - **Tactical Analysis Platform (§28, UNPROCESSED)** — expected to center opposition/tactical match content; shared tooling family expected.
  - **Sports Performance Analytics (processed)** — centers a measurement corpus over an athlete population; video there is linked context.
  - **Sports Scouting Platform (processed)** — registry + evaluation of external athletes; video as evidence. That pass recorded the Wyscout→Hudl Instant Save handoff ("with structure preserved") as the market-drawn seam.
  - **Sports Coaching Platform (processed)** — coach-client practice system that embeds an analysis suite as one medium; that pass hung the capability-slice flag and named OnForm as a straddling product.
  - **Athlete Management System (processed)** — owns the programming loop; video review feeds preparation but does not manage it.
  - **Officiating replay / VAR** — expected to be a different user and decision loop (officials, not coaching).

## Research Questions

1. What objects does the system's world consist of (footage, events/tags/clips, annotations, review assemblies, teams/athletes)?
2. How does footage enter the system, and is capture part of the Type?
3. What is the unit of analysis work, and how is it represented?
4. How does analysis reach athletes and staff, and on what surfaces?
5. Live (in-game) analysis vs post-game: same model or different Type?
6. Where does tagging stop and statistics begin (seam vs Sports Performance Analytics)?
7. Where does own-team review stop and opposition/tactical analysis begin (seam vs Tactical Analysis Platform)?
8. What roles exist (analyst, coach, athlete, staff)?
9. What did the analog "game film" practice look like — does the definition overfit modern cloud/AI implementations?
10. Are the match-breakdown pole and the technique/motion-analysis pole one Type or two?

## Representative Products

Selection: market leader + veteran specialist + desktop-license pole + capture-first pole + mobile-first pole; different product philosophies and customer tiers; official documentation reachable for all five.

1. **Hudl** — cloud platform dominant in schools/universities/pro clubs; upload → tag/breakdown → share/review → video exchange; add-on capture (Focus) and human-powered breakdown service (Assist). High school → professional tier.
2. **Dartfish** — Swiss veteran (20+ years); two product poles (game analysis / motion analysis) plus healthcare and education lines; federation/pro tier; Windows/mobile/cloud subscription ladder.
3. **Nacsport** — Spanish desktop-license suite (Basic → Elite) with a cloud companion (Hub); grassroots → pro; team-sport tagging tradition; live bench streaming.
4. **Veo** — Danish capture-first product (AI camera / two-phone setup) with an Editor and analytics add-ons; grassroots/amateur clubs and schools.
5. **OnForm** — US mobile-first app for individual coaches (golf, tennis, track & field, baseball/softball, swimming); technique pole; straddles into coaching-platform territory (student roster, business machinery).

## Sources

Research date: **2026-09-09**. All evidence Tier 1 (official help/documentation) or Tier 2 (official product pages) unless noted.

- Hudl product page (Tier 2): https://www.hudl.com/en_gb/products/hudl
- Hudl product-family navigation (Tier 2): Sportscode, Studio, Insight, Replay, Assist, Focus, Instat, Wyscout pages under https://www.hudl.com/en_gb/products
- Hudl Help Center: https://support.hudl.com/ — **UNREACHABLE** (JavaScript-only; returns "CSS Error"). Recorded as sourcing limitation; Hudl claims held at product-page strength.
- Dartfish home / game analysis / pricing pages (Tier 2): https://www.dartfish.com/ , https://www.dartfish.com/game , https://www.dartfish.com/plans (reached via /game pricing section)
- Dartfish knowledge base URL known: https://support.dartfish.tv/support/home — not fetched (stop condition reached; product-page evidence sufficient)
- Nacsport home page (Tier 2): https://nacsport.com/ ; Manuals hub (Tier 1 link hub, mostly video tutorials): https://www.nacsport.com/manuals.php
- Veo product pages (Tier 2): https://www.veo.co/ , https://www.veo.co/product/veo-editor (feature list)
- Veo Help Center (Tier 1): https://support.veo.com/hc/en-us and category "Watching and analyzing": https://support.veo.com/hc/en-us/categories/4429234734993-Watching-and-analyzing
- OnForm home + FAQ (Tier 2): https://onform.com/ (fetched via getonform.com redirect)

Sourcing limitation: no vendor's full operational help articles were read beyond Veo's help-center category structure; Hudl's support portal is JS-rendered and failed with a CSS error (same failure class the sports-scouting-platform pass recorded for a support portal). Per the evidence rules, no precise operational rules (sharing permissions, tag limits, storage quotas, frame-rate figures) are asserted in the final document; vendor-published numeric figures were treated as marketing/plan data and kept in these notes only.

## Product Observations

### Hudl (cloud platform pole)

Evidence layer: A (product page + product-family navigation).

- Self-description: "Online and mobile platform for video sharing and review."
- **Online video library** — "your team can view video and data from any device."
- **Playlists** — "quickly jump to the exact moments you want to study"; "create a presentation for team review, or pull together clips to illustrate what a player needs to improve."
- **Feedback tools** — "comments and drawings" to personalise feedback on performance.
- Player with pan/zoom on any uploaded footage.
- **In-app messaging** to team / group / individual.
- **Video exchange** — "securely share film with any team in seconds, even teams not on Hudl."
- Add-ons: **Focus** (automated capture cameras: capture, upload, livestream), **Assist** ("on-demand video analysis service" — stats/tagging done for the team by the vendor).
- Family context (adjacent products, same vendor): Sportscode ("customisable performance analysis"), Studio ("telestration platform for visual tactical review"), Insight (custom analytics), Replay (instant replay) — the elite tactical/code-window tooling is sold as separate products, not the core Hudl product.

### Dartfish (veteran specialist, game + motion poles)

Evidence layer: A (home, game-analysis, pricing pages).

- Two named poles: **Game analysis** ("understand and enhance team & player performances") and **Motion analysis** ("enhance athletic performance and prevent injuries"); plus healthcare and education lines.
- Game-analysis workflow (vendor's own framing): "Breakdown and tag game action – live or post-game. Identify and isolate the most critical events"; "Easily filter match events to identify player and opponent tendencies. Then, deliver objective evidenced feedback"; "Show your players exactly where they need to improve by using powerful drawing and annotative tools"; live in-game adjustment; opponent preparation ("Unlock your opponent's game plan").
- Testimonial (vendor-published): "During the game, I tag. After the game, I work on the tags I generated during the game, without having to rewatch the entire game."
- Pricing ladder exposes the capability set: video-editing tools, annotation tools, overlays and compositing, tagging tools, live tagging tools + tagging panels (sport-specific predefined panels for soccer/tennis/baseball), multi-video analysis, 3D drawings, 3D analysis, live feeds & live video encoding, Simulcam & Stromotion (branded overlay compositing), live collaboration, personal cloud storage with offline sync.
- Platforms: Windows desktop + iOS/Android apps (myDartfish Express, myDartfish Note) + cloud.
- Also sells **VAR systems** (video assistant referee / replay for judging sports) — officiating, a different user and loop; kept out of this Type.
- Motion-analysis pole includes technique evaluation, multi-view, simulcam, stromotion — the individual-athlete lineage (federations, swim/track/tennis education).

### Nacsport (desktop-license pole + cloud companion)

Evidence layer: A (home page; manuals hub).

- Self-description: "Sports video analysis solutions for any level, club or sport… grassroots amateur or seasoned pro."
- Desktop suite in capability tiers: Basic / Basic+ / Scout / Pro / Elite (Windows; macOS icons shown).
- Vendor framing: "Easily breakdown a game into tactical insights, stats and learning moments"; "Easily filter match events… detect strengths and weaknesses."
- **Tagging windows** are the documented central mechanism (samples page dedicated to "Tagging Windows"; button-driven categories and descriptors; Hub's online tagging exposes "automatic and manual categories and descriptors").
- Complementary products: **Live** ("wirelessly stream live video and data from Nacsport directly to any mobile device" — to the bench), **Tag&View** (film and tag a game from iPad/iPhone), **KlipDraw** (telestration), **Viewer** (view presentations without a full license), **Remote**, **AI** ("using your own game data, AI reveals unique insights").
- **Hub** — the online platform: upload analysis and "share uploaded analysis directly with coaches and players"; "Team Channel — a private, secure social network… where the team can come together, converse, learn and grow"; online tagging and analysis; clip export/share; **Exchange** module; **Referee** module (officiating drift, like Dartfish VAR).
- Manuals/courses confirm the workflow teaching order (tagging → presentation → sharing) at tutorial level.

### Veo (capture-first pole)

Evidence layer: A (product pages) + Tier 1 (help-center category structure).

- Capture: **Veo Cam 3** ("record and analyse your matches automatically"; AI follow-cam), **Veo Go** ("turn two iPhones into a match camera"), tripods; livestream add-on (**Veo Live**).
- **Veo Editor** ("watch, clip, and review every match in one place"): AI & manual events ("goals, shots, corners, and free kicks detected automatically. Add your own, and filter by type, team, or player"); clips & sharing ("shots and goals are automatically clipped. Add your own clips and bookmarks, then download as MP4"); drawings on screen ("spotlight players, sketch arrows, shapes, and freehand drawings, and keep timestamped notes"); speedrun ("automatically skips dead time"), match timeline, journal, playback speed controls; team roles (formations, captain, Player of the Match).
- **Veo Analytics 2** (add-on): "turns every recording into match stats, visuals, and coaching insight" — heat maps, shot maps, pass maps, radar "all linked straight to the video"; Veo Vision (player speed/distance overlaid on footage); Coach Assist (chat with match data).
- Help-center top-level categories (Tier 1): Getting started; **Recording and uploading**; **Watching and analyzing** (sections: Watch and edit recordings; Analytics 2; Veo App; Player Profile; Download and share; **League Exchange**); Live streaming; Cams and accessories; Account and billing; Veo Go.
- **League Exchange** — team-to-team video sharing at league level (analogous to Hudl Exchange).
- Stated users: clubs, larger organisations and leagues, parents, universities and schools. Three-step framing: "Record → Instantly relive/break down → Share."

### OnForm (mobile-first technique pole; coaching-platform straddle)

Evidence layer: A (home page + FAQ).

- Self-description: "Sports Video Analysis App & Coaching Platform"; "sports coaching app that helps coaches elevate athlete performance through video analysis."
- Three-step framing: **Record** (multiple recording modes, high-frame-rate capture) → **Analyze** ("break down performance with powerful tools": slow motion, frame-by-frame, drawing tools and voiceovers, 4-way video player, side-by-side comparison over time) → **Share** ("provide instant feedback and share videos effortlessly"; remote/asynchronous annotated feedback).
- **Library organization**: "videos, athletes, and teams stay organized with titles, tagging, and collections"; automatic cloud backup; cross-device access (phone/tablet/web app).
- **Coaching-business machinery** (the straddle evidence): student rostering, bulk invitations, staff management, multi-location academies, coach directory, "grow your coaching business."
- Multi-Cam MAX studio solution (fixed cameras → iPad control room); HIPAA-compliant posture marketed for physical-therapy/medical use.
- FAQ defines the category from the mobile-app side: "frame-by-frame playback, drawing annotation, side-by-side comparisons… leverages HD video capture and cloud-based sharing."

## Cross-product Comparison

| Dimension | Hudl | Dartfish | Nacsport | Veo | OnForm |
|---|---|---|---|---|---|
| Footage ingest | upload any camera; Focus auto-capture add-on | import files; live feeds & encoding; mobile capture | import files; capture devices documented; Tag&View mobile capture | vendor camera / two phones; auto upload | phone/tablet capture; multi-cam studio |
| Persistent library | online team video library | personal/team cloud library + offline sync | local video database + Hub online | match list in Editor; cloud | library organized by athlete/tag/collection |
| Unit of analysis | tagged moments → playlists | tagged events (tagging panels) | tagged clips (tagging windows: categories/descriptors) | AI + manual events; auto-clips; bookmarks | annotated clips of technique attempts |
| Frame markup | comments + drawings | drawing/annotation tools; overlays; 3D drawings | KlipDraw telestration | drawings, spotlight, timestamped notes | drawings + voiceovers |
| Review assembly | playlists / presentations | filtered event lists; reports; playlists | presentations; clips; Hub shares | clips, highlights, timeline review | shared annotated clips; side-by-side compare |
| Athlete delivery | in-app messaging + shared video | published video/feedback | Hub Team Channel + Viewer | app for players; Player Profile; share/download | direct share to athlete app |
| Live support | Focus livestream; Replay (family product) | Live S / Pro S live tagging + encoding | Live app to bench; Tag&View live | Veo Live streaming add-on | in-session instant feedback |
| Video exchange with other teams | Hudl Exchange (even non-Hudl teams) | collaboration/publishing options | Hub Exchange | League Exchange | not observed |
| Stats from tags | Assist service; data in platform | filter events → tendencies; reports | "tactical insights, stats" from breakdown | Analytics 2 add-on (linked to video) | not observed (technique metrics only, vendor-claimed 3D) |
| AI auto-tagging | via Assist (human service) / family | AI era-current, add-on class | AI complementary product | core (auto event detection) | not core |
| Delivery model | SaaS subscription | SaaS subscription ladder | desktop license + SUS + Hub cloud | hardware + subscription | freemium mobile app + subscription |
| Customer tier | school → pro (dominant: schools/universities) | federation/pro/education/healthcare | grassroots → pro | grassroots/amateur clubs, parents, schools | individual coaches, academies |

Findings by evidence layer:

- **B (cross-product, 5/5):** persistent organized footage library with sport context; frame-level markup (drawing/annotation/telestration); delivery of analysis to athletes/team members through the product.
- **B (cross-product, 4/5):** event/tag breakdown as the working unit (team pole); assembled review units (playlists/presentations/clips); feedback comments attached to moments.
- **B (cross-product, 3/5):** team-to-team video exchange; live tagging/streaming to the bench; stats derived from tags.
- **A (product-specific):** AI auto-event detection as a default behavior (Veo); human-powered breakdown service (Hudl Assist); capture hardware as the entry product (Veo Cam / Hudl Focus); technique-measurement tooling (Dartfish Simulcam/Stromotion, OnForm 3D claims).

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being recognizable as Sports Video Analysis:

1. **The footage library of record** — a persistent, organized collection of sports recordings (matches, sessions, technique attempts) carrying sport context (team, opponent or venue, date, athletes). The library accumulates across the season; it is the object of record the whole Type works on. Remove → a generic video player/editor or a media file store.
2. **Sport-purposed analysis structure imposed on the footage** — the video is subdivided and marked up into analysis units that reference moments in time: tagged/clipped events with sport meaning, annotated frames (drawings, telestration, notes), side-by-side comparisons. The markup is held as structured references into the footage, not as re-edited media. Remove → a video archive with playback, or MAM-style media logistics.
3. **The coaching review loop** — analysis units are assembled (playlists, presentations, filtered event lists, shared clips) and delivered back to athletes and staff through the product for review and feedback. The purpose is changed coaching/playing behavior, not media distribution. Remove → a footage archive or a fan-facing highlight product.

Jointly-held load-bearing tests:

- 1 alone = sports video archive / MAM (media logistics).
- 2 without 1 = a one-off markup utility with no season memory.
- 3 without 1+2 = a film session without software (no managed object).
- 1+2 without 3 = a searchable video/tag database nobody works from (data-provider posture when the footage is others').
- 1+3 without 2 = an archive plus wishful watching — no structured analysis.
- 2+3 without 1 = ephemeral markup, no accumulating record.

### L1 — Common Mature Structure

Present in most mature modern products, not definitional:

- tagging windows / button panels with user-defined categories and descriptors (team pole)
- playlists / presentations as review assemblies
- telestration/drawing tools, slow motion, frame-by-frame, pan/zoom
- comments attached to moments; per-athlete visibility of feedback
- team communication surface (messaging/channel) attached to the video
- season-scale archive with search/filter (by opponent, athlete, event type)
- highlight export (MP4 / reel) as a byproduct
- role separation: analyst/coach builds; athlete/staff reviews
- video exchange with other teams
- stats derived from tags (primitive performance analytics)
- live tagging + bench streaming

### L2 — Variant / Optional Structure

- **Capture posture** — vendor hardware camera + auto upload (capture-first pole), phone capture, or plain file import; the analysis layer is indifferent (variant axis, not definitional)
- **AI auto-tagging** — era-current; emerging default at one pole, add-on class elsewhere
- **Delivery model** — desktop license with local database ↔ cloud SaaS ↔ mobile-first freemium
- **Footage pole** — match/game breakdown ↔ technique/motion analysis (individual attempts, compare-over-time, measurement overlays)
- **Sport-specific predefined tagging panels and reports**
- **Adjacent audiences** — education (video-based teaching), healthcare/physio (movement evaluation), officiating modules
- **Fan-facing surfaces** — livestreaming, highlight sharing to supporters (drift surface)

### L3 — Vendor-specific Structure

- Hudl: Assist human breakdown service; Sportscode custom code windows; Studio telestration product; Exchange implementation; Focus camera line
- Dartfish: Simulcam, Stromotion, myDartfish Express/Note naming, VAR product line, predefined panel per sport per plan
- Nacsport: Hub Team Channel, Tag&View, KlipDraw, Viewer, Remote, Hub plan button limits (numeric, plan-specific)
- Veo: Speedrun, Follow-cam, Player of the Match role tiers, Analytics 2 modules (Match Report, Coach Assist, Veo Vision), League Exchange naming
- OnForm: Multi-Cam MAX, 3D swing metrics claims, golf coach directory, HIPAA posture

## Vendor-specific Findings

- The elite tactical/code-window tooling (Hudl Sportscode) is sold as a **separate product** from the team video platform — the market itself distinguishes elite custom-code analysis from standard team breakdown.
- Two vendors in-sample sell officiating replay (VAR) as a separate line (Dartfish VAR Systems, Nacsport Hub Referee) — evidence that officiating replay is a different user/loop from coaching analysis.
- One vendor packages a human analysis service (Hudl Assist) — the breakdown work can be bought rather than done, which confirms tagging is the valuable unit rather than a specific tool.
- One vendor's business layer (OnForm: students/staff/academies/directory) shows the coaching-platform straddle documented by the sports-coaching-platform pass.

## Rejected Findings

- "Sports Video Analysis = button tagging" — **rejected**: the technique pole (OnForm; Dartfish motion) does clip-and-annotate without event tags, and Veo auto-detects events. The invariant is the analysis unit referencing footage moments, not any particular tagging mechanism.
- "Cloud delivery is definitional" — **rejected**: Nacsport's desktop-license + local-database posture is a full member; the historical desktop era fits without cloud.
- "AI tagging is definitional" — **rejected**: human tagging and purchased breakdown services satisfy the same structure.
- "Cameras/hardware are part of the Type" — **rejected**: import-only products are complete members; capture is a variant axis.
- "Highlights/fan sharing are the center" — **rejected**: highlight export is a byproduct; fan-facing distribution without the coaching loop is a different product class (video streaming / social).
- "This Type includes officiating replay (VAR)" — **rejected**: different users (officials), different decision loop; vendors themselves separate the lines.

## Boundary Findings

1. **vs Video Editor / NLE (§04.06)** — the editor's world is a timeline/sequence that renders a program; this Type's world is a sport-contextualized library + referenced analysis units + review loop. Highlights are an edited output but a byproduct. Remove the sport semantics and the review loop → generic video editing.
2. **vs Tactical Analysis Platform (§28, UNPROCESSED — FLAG HUNG)** — same tooling family, different center of gravity: this Type centers own-team/own-athlete footage for coaching and performance review; the tactical leaf is expected to center opposition/tactical match content. Evidence of the seam running through products: Dartfish markets opponent scouting inside game analysis; a Nacsport testimonial is from a Head of Opposition Analysis; Hudl sells elite tactical tooling (Sportscode/Studio/Insight) as separate products. Mid-market products merge both uses; elite market separates them. Directional tests: center the opposition's next-match preparation and the tactical leaf's world applies; center the season-long own-team breakdown archive and this Type's world applies. To be ratified at that pass.
3. **vs Sports Performance Analytics (processed)** — the corpus here is footage with markup; the corpus there is quantified performance data over an athlete population. Tag-derived counts sit at the seam: when numeric measurement becomes the center and video becomes linked context, the product drifts to that Type (Hudl Signal, Veo Analytics 2 as add-ons show the market drawing this seam).
4. **vs Sports Scouting Platform (processed)** — own-team coaching content vs external-athlete registry + evaluation. The Wyscout→Hudl Instant Save handoff (scouting content pushed into a video-analysis workspace "with structure preserved") documents the handoff; Instat's dual-use packaging (one library serving analysis and scouting) shows the center-of-gravity seam.
5. **vs Sports Coaching Platform (processed)** — tool-centered vs relationship-centered (client roster + sessions + exchange). The capability-slice pattern is confirmed from this side: an analysis suite is a standard capability inside coaching platforms; standalone products center the tooling. OnForm straddles (deep analysis suite + roster/business machinery) — documented in both leaves.
6. **vs Athlete Management System (processed)** — video review feeds preparation; the AMS owns the programming loop and the managed roster. No sampled video-analysis product assigns training work.
7. **vs Media Asset Management (§27)** — MAM centers ingest/catalog/rights/distribution of media collections for media organizations; this Type centers sport-purposed breakdown and the coaching loop. A sports broadcaster's MAM is media territory even though it holds sports footage.
8. **vs Video Streaming Platform (§27)** — livestream add-ons exist in-sample (Veo Live, Hudl Focus livestream) but streaming to an audience without library/breakdown/review is a different Type; the fan-facing surface is an adjacency.
9. **vs Referee Management Platform / officiating replay** — officials' replay (VAR) serves the decision loop of the match officials; this Type serves the coaching loop. Vendors split these into separate products.

## Historical / Market-Sample Check

- **Analog game-film practice** (mid-20th-century American football; widespread VHS-era practice worldwide): a tape/film library organized by opponent and date (leg 1), pause-rewind-notepad breakdown and clip sheets / spliced film (leg 2), and the weekly team film session delivering review to players (leg 3). All three L0 legs satisfied with no software, no cloud, no AI — the software Type digitizes an existing practice, so the definition is not overfit to modern implementations.
- **Older software era**: 1990s–2000s desktop video analysis (early Dartfish generation, SportsCode origins, local-file breakdown tools) — local libraries, code/tag windows, CD/DVD exchange; fits L0 without cloud or AI.
- **Regional breadth**: Spanish (Nacsport), Swiss (Dartfish), Danish (Veo), US (Hudl, OnForm) vendors; team-sport and individual-sport traditions both fit.
- **Technique pole lineage**: motion-picture-based biomechanics and technique study predates digital video; the motion-analysis pole is the software continuation and fits L0 (attempt library, annotated comparisons, coach review).
- Conclusion: the definition holds across eras, regions, and sport families. The one axis that changed the market's surface, not the Type, is capture automation.

## Uncertainties

- No vendor's full help-center article set was read except Veo's category structure; operational rules (who may tag, permission models, retention) are unverified. Hudl's support portal was unreachable (JS/CSS error) — the market leader's operational detail is held at product-page strength only.
- The exact product split between "video analysis" and "tactical analysis" in the mid-market is blurry: several sampled products serve both uses. The elite market separates them (separate products). This is the main flag for the tactical-analysis-platform pass.
- Whether tag-derived statistics are common enough to be L1 or remain advanced: observed as add-on or advanced tier in four samples; held as "common advanced" rather than standard.
- OnForm's classification (this Type vs Sports Coaching Platform) is a documented straddle, resolved as "both leaves document their own pole" consistent with the coaching pass's proposal.

## Final Synthesis

One Type with three jointly-held defining structures — footage library of record, sport-purposed analysis structure (tagged/clipped events and annotated frames referencing moments in the footage), and the coaching review loop that returns analysis to athletes and staff. The market realizes it across two footage poles (match/game breakdown and technique/motion analysis), three delivery eras (desktop license, cloud platform, mobile-first), and several capture postures (import, phone, vendor camera with AI upload). Tagging mechanism, AI, cloud, cameras, exchange, and stats are all market layers, not the definition. The boundary with Tactical Analysis Platform is a center-of-gravity seam inside a shared tooling family (flag hung for that pass); the boundary with Sports Performance Analytics and Sports Scouting Platform follows the corpus/center seams ratified by those passes; the boundary with Sports Coaching Platform follows the tool-vs-relationship seam, with OnForm as the documented straddling product.
