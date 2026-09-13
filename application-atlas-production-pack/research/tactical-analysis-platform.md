# Research Notes — Tactical Analysis Platform

## Research Goal

Understand what "Tactical Analysis Platform" is as an Application Type: what its world is made of, who operates it, what the defining workflow is, and where its boundaries sit against the neighboring sports-software leaves — Sports Video Analysis (flag hung by that pass), Sports Performance Analytics (forward flag), Sports Scouting Platform (forward flag) — and against non-sports neighbors (tactic-board/diagramming tools, match data providers, video editors).

## Initial Boundary

- Expected center: opposition/tactical match content — preparing for the next opponent, analyzing tactical patterns, building game plans.
- Three prior passes hung flags toward this leaf:
  1. **sports-video-analysis**: shared tooling family (tagging, telestration, match footage); center-of-gravity seam = own-team coaching review vs opposition/tactical preparation; elite market separates them into distinct products (Hudl sells Sportscode/Studio/Insight separately from its team video platform), mid-market merges.
  2. **sports-performance-analytics**: the match-event-data analytics pole (opposition analysis, Tactics modules) drifts here when opposition/tactical match content becomes the center; proposed discriminator = opposition/tactical match content vs athlete/team performance measurement as the analyzed center.
  3. **sports-scouting-platform**: scouting platforms carry match video as athlete evidence while this Type centers opposition/tactical match content; Instat's dual-use packaging shows the seam.
- Risk of confusion with tactic-board / play-diagramming applications (drawing drills and plays without a match content corpus) and with match data providers (feed without analysis loop).

## Research Questions

1. What is the core analyzed object — the match? the opponent? the tactical pattern?
2. What content does the system organize (footage, event data, both)?
3. What does "tactical breakdown" concretely consist of (tagging, coding, scripting, annotation, diagrams)?
4. What is the delivery loop (reports, presentations, playlists, dashboards) and who consumes it?
5. Where does own-team review stop and opposition/tactical analysis begin?
6. Where does tactical analysis stop and performance measurement begin (data-first pole)?
7. Where does tactical analysis stop and player evaluation begin (scouting seam)?
8. Do older / analog practices (opposition dossiers, coded match sheets) fit the definition?

## Representative Products

| Product | Segment | Philosophy | Why selected |
|---|---|---|---|
| Hudl Sportscode / Insight / Studio | elite pro/national teams | fully customizable coding + scripting + data analytics + telestration, sold as a separate elite line from Hudl's team video platform | elite pole; market-drawn separation from Sports Video Analysis |
| Nacsport (Basic→Elite tiers) | mid-market clubs, multi-sport | desktop tagging-window breakdown + presentations + Hub sharing | mid-market pole; opposition-analysis testimonial evidence |
| Dartfish (myDartfish game-analysis line) | federations, clubs, multi-sport | game analysis line ("prepare your team for the next opponent") sold separately from motion analysis and VAR lines | multi-use vendor with market-drawn product lines |
| Hudl Statsbomb | elite football | data-first: event data + models + analytics platform with integrated video; "tactical analysis" named as a primary use | match-event-data pole; boundary data point vs Sports Performance Analytics |
| Hudl Instat | basketball/ice hockey, high school→pro | dual-use video+data library serving both coaching analysis and scouting | dual-use packaging; boundary data point vs Sports Scouting |

## Sources

- Hudl Sportscode product page — https://www.hudl.com/en_gb/products/sportscode (fetched 2026-09-10)
- Hudl product catalog (Insight, Studio, Instat, Statsbomb, Fastmodel descriptions) — https://www.hudl.com/en_gb/products/sportscode (nav) (fetched 2026-09-10)
- Hudl Statsbomb product page — https://www.hudl.com/en_gb/products/statsbomb (fetched 2026-09-10)
- Nacsport homepage — https://nacsport.com/en/ (fetched 2026-09-10)
- Dartfish homepage — https://www.dartfish.com/ (fetched 2026-09-10)
- Prior passes: research/sports-video-analysis.md, research/sports-performance-analytics.md, research/sports-scouting-platform.md (boundary flags)

Sourcing limitation: no vendor help-center / user-manual pages were fetched in this pass (Hudl support portal was unreachable in the sports-video-analysis pass; Nacsport manuals and Dartfish knowledge base exist but were not fetched — product-page-level evidence only). Precise operational details (tag counts, limits, exact workflow steps) are therefore kept out of the final document.

## Product Observations

### Hudl Sportscode / Insight / Studio (evidence layer A)

- Sportscode: "customizable coding and scripting tools that allow you to analyze what matters most to your team"; "customized MacOS offline coding tools"; "powerful scripting capabilities"; "improved timeline and video performance"; coding window screenshot shows button-panel coding over video.
- Customer quote (SC Paderborn assistant manager): "We use Hudl and Sportscode daily to prepare for our next opponents, analyze our last match and to prepare for training sessions." — the preparation loop is explicit.
- Connected products: Insight ("Custom analytics transforming data into tactical insight"), Studio ("Telestration platform for visual tactical review"), Replay (instant replay), Coda (iPad live coding), Assist (outsourced tagging service).
- Market structure: Hudl sells Sportscode/Insight/Studio as a separate elite product family from the Hudl team video platform — the elite market separates tactical tooling from team video sharing.
- Statsbomb data "flows natively through Hudl Sportscode, Studio, and Insight to give you a single unified platform for joined-up pre, post and live custom analysis."

### Nacsport (evidence layer A)

- Desktop suite (Basic→Elite tiers) "created by and for sports analysts and coaches"; "Easily breakdown a game into tactical insights, stats and learning moments."
- Tagging windows are the core mechanism (samples page dedicated to tagging windows); live tagging (Live app streams video+data to the bench), post-game analysis, presentations shared via Hub platform.
- Testimonial: Greg Mathieson, "Former Head of Opposition Analysis, Liverpool FC" — opposition analysis is a named use case at the elite end of a mid-market product.
- Hub: online tagging, Team Channel, season tracking — cloud delivery layer.
- AI add-on: "Using your own game data, AI reveals unique insights into the game allowing you to adapt strategies."

### Dartfish (evidence layer A)

- Game-analysis line sold separately from motion-analysis line and VAR line: myDartfish 360 S ("entry-level solution for delayed game analysis"), Live S ("complete solution for live game performance analysis"), Pro S ("most advanced live video & data analysis solution for pro games").
- Positioning: "Prepare your team for the next opponent. Identify weaknesses and optimize your athlete's performance." — next-opponent preparation named directly.
- "Use video and data analysis to detect vulnerabilities. Decide what to focus on and develop technical and tactical strategies."

### Hudl Statsbomb (evidence layer A)

- Data-first pole: "Power your player recruitment, tactical analysis, and performance evaluation with the best football data ever created."
- Event data (3,400+ events/match claimed), player-location data, proprietary models (xG, OBV, Phases of Play, Defensive Responsibility, xPass).
- Delivery: "advanced-but-intuitive analytics platform with customisable data visualisation tools and integrated video"; APIs; JSON/XML/CSV files.
- Customer quote (Club Brugge): "design advanced metrics and tailor them to our club's philosophy for opposition analysis and player recruitment" — opposition analysis named as a first-class use of match-event data.
- Sits inside Hudl Pro Suite alongside Sportscode/Studio/Insight — the data layer and the coding/telestration layer are separate products that integrate.

### Hudl Instat (evidence layer A, product-page level)

- "Video and data solution for analysis and scouting" — one library serving both coaching analysis and scouting (dual-use packaging; already documented in the sports-scouting pass).

## Cross-product Comparison

| Dimension | Sportscode/Insight/Studio | Nacsport | Dartfish game line | Statsbomb | Instat |
|---|---|---|---|---|---|
| Analyzed center | match content (own + opponents), customizable | match content, tagging-window driven | match content, next-opponent framing | match event data, opposition analysis named | match content, dual-use |
| Content substrate | footage + integrated data | footage | footage + data | event/tracking data + integrated video | footage + data |
| Breakdown mechanism | coding buttons + scripting (user-built) | tagging windows (user-built) | tagging/live coding | vendor-collected event data + models | vendor + user mix |
| Tactical markup | telestration (Studio) | KlipDraw telestration | visualization tools | data visualisation (pitch plots) | annotation |
| Delivery loop | reports/player reports linked to video, shareable | presentations via Hub, Team Channel | analysis outputs to staff | dashboards/visualisations, APIs | reports, shared library |
| Live in-game use | Replay/Coda live coding | Live app to bench | Live S/Pro S live | Hudl Live Data | — |
| Who builds the analysis | team analysts | team analysts | team analysts | vendor data team + club analysts | vendor + club analysts |

## Canonical Model (L0/L1/L2/L3)

### L0 — Defining Invariant (minimal)

One Type with three jointly-held structures:

1. **The match content corpus** — an organized, persistent record of matches (own and/or opponents') carrying match context (teams, competition, date), accumulating across the season as the object the whole Type works on. Substrate is a variant axis: match footage, match event data, or both. Remove → a generic video editor or a bare data feed.
2. **The tactical breakdown structure** — analysis units with tactical meaning imposed on the content and referencing moments in it: tagged/coded events, tactical patterns and sequences, annotated/telestrated frames, tactical visualisations — organized around tactical questions (opponent tendencies, set plays, formations, phases). Remove → a video archive or a stats database with no tactical structure.
3. **The preparation loop** — breakdown assembled into deliverables (reports, presentations, filtered event lists, dashboards) consumed by coaching staff to inform preparation for upcoming matches. Remove → an archive nobody works from.

Jointly-held load-bearing: 1 alone = video archive/data feed; 2 without 1 = one-off markup with no memory; 3 without 1+2 = presentations over nothing; 1+2 without 3 = a tagged database nobody prepares from; 1+3 without 2 = watching without structure; 2+3 without 1 = ephemeral markup.

### L1 — Common Mature Structure

- tagging/coding windows (button panels) as the standard breakdown mechanism
- telestration / drawing on frames
- filtered event lists and playlists
- presentations/reports delivered to staff and players
- live in-game coding and bench streaming
- statistics derived from tagged events
- multi-match comparison and season accumulation
- sharing with roles (analyst builds, coach consumes, players view)

### L2 — Variant / Optional

- content substrate: footage-only ↔ data-only ↔ footage+data
- who collects the data: user coding vs vendor-collected event data vs AI auto-detection
- delivery era: desktop license ↔ cloud platform ↔ mobile companion
- live in-game use (bench streaming, instant replay)
- sport breadth: single-sport deep vs multi-sport
- dual-use packaging with scouting (one library serving analysis and recruitment)
- scripting/customization depth (elite end)

### L3 — Vendor-specific

- Sportscode scripting engine and Design Toolkit; Insight as separate analytics product; Studio as separate telestration product
- Nacsport tier ladder (Basic→Elite), Hub Team Channel, KlipDraw
- Dartfish product-line split (game vs motion vs VAR), simulcam/stromotion
- StatsBomb proprietary models (OBV, HOPS, Phases of Play, Defensive Responsibility, xPass)
- Instat per-sport portals

## Vendor-specific Findings

See L3. None promoted to the final document.

## Boundary Findings

1. **vs Sports Video Analysis — RATIFIED (flag from that pass discharged)**. Same tooling family (tagging, telestration, match footage), different center of gravity. This Type centers opposition/tactical match content and next-match preparation; that Type centers own-team/own-athlete footage for coaching review. Evidence the seam runs through products: Hudl sells elite tactical tooling (Sportscode/Studio/Insight) as products separate from its team video platform; Dartfish frames its game-analysis line as "prepare your team for the next opponent"; a Nacsport testimonial comes from a Head of Opposition Analysis. Mid-market products merge both uses (one tool serves both loops); the elite market separates them into distinct products. Directional tests: center the opposition's next-match preparation and this Type's world applies; center the season-long own-team breakdown archive for athlete development and Sports Video Analysis's world applies. Keep both.
2. **vs Sports Performance Analytics — RATIFIED (forward flag from that pass discharged)**. The match-event-data pole drifts here when opposition/tactical match content becomes the center. StatsBomb names "tactical analysis" as a primary use alongside recruitment and performance evaluation; Club Brugge tailors metrics "for opposition analysis". Discriminator: opposition/tactical match content as the analyzed center (this Type) vs athlete/team performance measurement as the analyzed center (that Type). Keep both.
3. **vs Sports Scouting Platform — RATIFIED (flag from that pass discharged)**. Scouting platforms carry match video as evidence about athletes; here the match itself is the analyzed object and the deliverable is a game plan, not a player evaluation. Instat's dual-use packaging (one library serving coaching analysis and scouting) shows the center-of-gravity seam. Keep both.
4. **vs tactic-board / play-diagramming tools** — diagram authoring (playbooks, drill drawing) without a match content corpus is a different tool family (e.g. FastDraw under Hudl's own taxonomy sits beside FastScout, not inside Sportscode). No directory leaf conflict in §28; noted for completeness.
5. **vs match data providers** — a bare feed without breakdown structure and preparation loop is a data product, not this Type. StatsBomb crosses into this Type because it ships an analytics platform and names tactical analysis as the use.
6. **vs referee/VAR systems** — officials' decision loop, different users and rules; Dartfish sells VAR as a separate line.

## Historical / Market-Sample Check

Pre-digital practice fits: opposition dossiers, coded match sheets, annotated photographs, and hand-drawn tactical diagrams satisfy all three legs (match content corpus on paper, tactical breakdown by hand, preparation deliverables to staff). The definition does not depend on tagging buttons, AI, cloud, or video. Historical check passed.

## Uncertainties

- The exact product split between "video analysis" and "tactical analysis" in the mid-market is blurry: several sampled products serve both uses. The elite market separates them. This is documented as a center-of-gravity seam, not a hard product boundary.
- No help-center-level evidence was reached in this pass; workflow detail is held at product-page strength.
- Whether "Tactical Analysis Platform" should eventually be folded into Sports Video Analysis as a variant cannot be settled from this sample alone: the elite market's separate products and the data-first pole (which needs no footage) argue for keeping both; the mid-market's merged products argue the other way. Recorded as a standing observation, keep-both ratified.

## Final Synthesis

A Tactical Analysis Platform is the staff-facing analysis application whose center of gravity is opposition/tactical match content: an organized match content corpus (footage and/or event data), a tactical breakdown structure imposed on it (tagged/coded events, patterns, annotated frames, tactical visualisations), and a preparation loop that turns breakdown into deliverables consumed by coaching staff for upcoming matches. It shares its tooling family with Sports Video Analysis but centers the opponent and the next match rather than own-team development; it shares its data layer with Sports Performance Analytics but centers match/opposition content rather than athlete performance measurement; it shares its content with Sports Scouting but centers the match rather than the athlete. The market realizes one Type across content poles (footage ↔ event data), collection postures (user coding ↔ vendor data ↔ AI), and delivery eras (desktop ↔ cloud ↔ mobile), with the elite market separating tactical tooling into distinct products and the mid-market merging both uses in one tool.
