# Research Notes — Worship Presentation Software

Research date: **2026-09-09**
Leaf: `Worship Presentation Software` (DIRECTORY.md §25 Nonprofit, Membership & Religious Organizations)
Slug: `worship-presentation-software`

## Research Goal

Understand the Application Type "Worship Presentation Software" from real products: what objects exist inside it, what users do with them, how the live display loop works, which capabilities are definitional vs common vs optional, and where the Type's boundaries sit against Presentation Application (§03.04), Worship Planning (§25 sibling), Sermon Management (§25 sibling), and other neighbors.

This pass carries **three pre-hung flags to discharge**:

1. **presentation-application (§03.04, processed 2026-09-08) — advance note**: "live lyric/scripture display for worship services shares slide-display mechanics with this Type's delivery realization — when processed, expected to be defined by its own live-display/liturgy/service semantics rather than absorbed by the generic grammar; cross-reference recommended."
2. **sermon-management (§25, processed 2026-09-09) — forward flag**: "seam = the record that outlives the service vs live in-service display; they meet at slide export — prep products export slides into presentation software; confirm the live-display-vs-record seam."
3. **worship-planning (§25, processed 2026-09-09) — ratify request**: "the preparation-vs-live-display seam is documented from the planning side (WorshipPlanning.com→Proclaim integration copy; WorshipTools Planning↔Presenter sync); ratify from the display side when that pass runs."

## Initial Boundary

Initial hypothesis: this Type is the software an operator (usually a volunteer) runs **during** a worship service to put lyrics, scripture, videos, images, and sermon support on the congregation's screens in real time. Neighbors:

- **Presentation Application** (§03.04): generic slide authoring + delivery. Risk of absorption — worship presentation shares "slides shown to an audience."
- **Worship Planning** (§25 sibling): organizes the service *before* it happens (order of worship, people, files). Risk of confusion via bundling.
- **Sermon Management** (§25 sibling): the sermon as a record that outlives the service. Risk of confusion via sermon-slide features.
- **Church Management System**: congregation records — likely no overlap.
- **Livestream/broadcast production, digital signage**: output-adjacent surfaces.

## Research Questions

1. What are the core objects? (library items — songs/lyrics, scripture, media; the service/presentation container; cues)
2. How does the live loop work — what does the operator see vs what the congregation sees?
3. How is scripture handled (reference retrieval, translations, on-the-fly)?
4. How are lyrics handled (verse blocks, ordering, copyright)?
5. What display outputs exist (audience, operator, stage/confidence, livestream)?
6. What is common mature structure vs definitional?
7. What happens at the seams: planning→presentation hand-off, sermon slides, PowerPoint interchange?
8. Historical check: do late-1990s/early-2000s products (and the pre-software acetate/songbook workflow) satisfy the same core?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers/business models + lineage spread:

| Product | Vendor | Pole |
|---|---|---|
| ProPresenter | Renewed Vision | market leader, pro-grade, worship-first then broadened to live production; subscription |
| EasyWorship | Softouch Development | mainstream volunteer-friendly; subscription; 25+ years |
| MediaShout | MediaComplete | the 1999 original ("the original church presentation software"); one-time purchase |
| OpenLP | OpenLP Developers | free open-source, cross-platform (Windows/macOS/Linux/FreeBSD) |
| Presenter by WorshipTools | WorshipTools (CCLI ecosystem) | free tier, cloud-sync core, sibling of Planning/Charts/Community/Rehearse |

Proclaim (Faithlife) was targeted as the cloud/ecosystem pole but **unreachable ×2** (timeouts) — consistent with the sermon-management pass's sourcing limitation. See Uncertainties.

## Sources

All fetched 2026-09-09 (Tier 1/2 official):

- Renewed Vision — root: https://renewedvision.com/ ; worship industry page: https://renewedvision.com/industries/worship (note: /propresenter/ returned 404; root + industries pages reachable)
- EasyWorship — root: https://www.easyworship.com/ ; features: https://www.easyworship.com/software/features ; support home: https://support.easyworship.com/support/home
- MediaShout — root: https://www.mediashout.com/ ; features: https://mediashout.com/features/ ; user guide listed at https://mediashout.com/docs/mediashout-7-user-guide/
- OpenLP — root: https://openlp.org/ ; manual: https://manual.openlp.org/
- WorshipTools — Presenter: https://www.worshipextreme.com/en-us/presenter
- Proclaim — https://proclaim.faithlife.com/ : **timed out ×2, abandoned per network rule**

## Product Observations

### ProPresenter (Renewed Vision) — evidence layer A

- Self-label: "Live presentation and worship software for churches, schools, business presentations, and concerts"; "the industry standard in presentation software"; "ProPresenter was first built for houses of worship."
- Worship features page: "Quickly and easily build your worship and sermon content and present them with a reliable video engine."
- **Scripture**: "The only scripture display software with over 130 Bible translations — just a click away… Easily present multiple translations or languages at once, and never have to worry about manually formatting Bible Scripture again."
- **Lyrics/copyright**: "automatic lyric and copyright integration"; "ProPresenter natively integrates with Planning Center Online and CCLI's SongSelect, making it easy for you to pull in lyrics for Sunday morning… This makes it possible for you to have your worship set automatically created"; "Songs imported via SongSelect automatically include copyright information"; "you must display copyright information for projected lyrics to stay legally compliant."
- **Outputs**: "Set up multiple stage displays, lobby feeds, overflow rooms, and even a specific separate feed for online events"; "multiple looks and multiple content streams to various displays and locations throughout your facility."
- **Stage display**: "a stage display, which allows the speaker to see both sermon notes and a clock or countdown timer simultaneously — and running completely independently of the main visual displays"; "Musicians can make use of their confidence monitor by displaying chords on the Stage Screen."
- **Announcement layer**: "scrolling announcement slides to keep playing on lobby displays (or elsewhere) while the main service is happening in the auditorium and on the live stream."
- **Livestream**: "Stream to any destination that accepts RTMP… built in integration with Resi.io"; "automating this process" of formatting content "for in-person screens and online live streams."
- **Remotes**: iOS/Android remote-control apps; "Stage Display apps for Android, iOS, tvOS, and iPadOS."
- **Music software**: compatibility with Ableton Live, MultiTracks Playback, Loop Community Prime.
- **Scale**: campus subscription "up to 20 seats of ProPresenter to present at one physical location"; used by "thousands of big and small churches."
- Comparison guides published vs PowerPoint, Keynote, Prezi, EasyWorship, MediaShout, Proclaim, Presenter by WorshipTools — the vendor itself treats generic presentation tools and sibling worship tools as distinct comparison classes.
- 20+ years ("For over 20 years").

### EasyWorship (Softouch Development) — evidence layer A

- Self-label: "Church presentation software your volunteers can run"; "Lyrics, Scriptures, and slides your volunteers can run confidently every Sunday"; "25+ years serving churches worldwide."
- **Interface model (explicit four areas)**: "**Schedule** — Easily drag and drop any item from the resource area to add it to your schedule… **Preview** — Review every slide in detail before it goes live. See exactly what your congregation will see… **Live** — Monitor what's on screen in real time and keep slides flowing smoothly with your service… **Resources** — Search, organize, and add media, songs, and scripture to your schedule in just a few clicks."
- **Multiple outputs**: "Send your presentation to projectors, confidence monitors, and your livestream at the same time. One computer, every screen."
- **Streaming**: "outputs via NDI and Alpha Channel to OBS, vMix, and most broadcast and livestreaming setups."
- **Live-control behaviors**: "One-Click Web Display — Send any webpage or video full screen with a single click"; "Real-Time Message Alerts — Keep your speakers, congregation, and online viewers in sync with real-time messages and alerts"; "Instant Screen Transitions — Cut, clear, or brand your screen instantly."
- **Songs**: "CCLI SongSelect, built right in — Access 500,000+ licensed worship songs… Lyrics arrive pre-formatted and copyright reporting is handled automatically."
- **Scripture**: "Access to 90+ Bible Translations — Search over 90 Bible translations across 32 languages by book or keyword… Jump to any book, chapter, or verse and read in one continuous scroll."
- **Sermon slides**: "Build sermon slides in our Presentation Editor or import directly from PowerPoint."
- **Themes**: "One theme. Every slide. Set your fonts, colors, and backgrounds once."
- **Remotes**: free iOS/Android remote app; StreamDeck/Companion plug-ins; "Send and receive MIDI cues to control EasyWorship from Playback, Prime, Ableton"; "Sync schedules with MIDI — Keep multiple computers perfectly in sync."
- **Planning (own suite, beta)**: "Plan your service, schedule your team, and send setlists together in one place. Then import your agenda into our presentation software so you aren't starting from a blank screen."
- Pricing: subscription from $17.50/mo (basic) / $27.50 (premium with media).

### MediaShout (MediaComplete) — evidence layer A

- Self-label: "MediaShout is **church presentation software** and **worship presentation software** built specifically for churches — for displaying song lyrics, scripture, sermon points, and all forms of visual media to your screens during worship gatherings and events."
- **Historical anchor (vendor's own claim)**: "In 1999, MediaShout pioneered the switch from limited office-style software like Microsoft Powerpoint to church-specific software to display **non-linear presentations controlled on a separate screen by an operator**." Also "25+ Years as the Original Church Presentation Software"; "80,000+ Churches Served Worldwide."
- **Positioning vs generic tools**: "Not a Generic Presentation Tool. Not an Entertainment Media System… It's not a general-purpose presentation tool adapted for worship."
- **Output model**: "build and run slides on an intuitive, easy to use **control screen** while showing only your presentation to your audience on a **separate 'main display' output**… Most of our software versions even include a **third output for either a 'stage display'** (also known as a confidence monitor) or live streams."
- **Content types (FAQ)**: "Worship lyrics; Sermon slides and pastor notes; Bible verses (70+ translations included); Videos and motion backgrounds; Announcements and service elements. All content is managed in one place, making it easy to run a complete service smoothly."
- **Libraries**: "Song Lyric Library — 2,300+ Songs Included… insert a complete song into your service in seconds"; "CCLI SongSelect Integration & Auto-Reporting — MediaShout automatically tracks every song displayed and generates your CCLI usage reports"; "70 Bible Translations Built In… All publisher royalties are paid"; "Dual Bibles — Display two Bible translations side-by-side on the same slide."
- **On-the-fly**: "Lyrics on the Fly — Pull up any song from your library and display it instantly — even mid-service — without disrupting your planned presentation. Perfect for spontaneous worship moments"; "Bible Scripture on the Fly — Insert any Bible verse mid-service with just a few clicks… and send it to the screen instantly without interrupting the flow of worship."
- **Operator views**: "Presenter View vs. Edit View — Switch between a simplified Presenter View for volunteers running the live service and a full Edit View when building content. Volunteers only ever see what they need."
- **Stage display**: "Send a customized third output to a stage monitor for your pastor or worship leader — showing lyrics, notes, countdowns, or coming-up-next information that the congregation never sees."
- **Service building**: "Sermon Builder — Build your sermon outline directly inside MediaShout. Add points, scripture references, and supporting media all in one place — then run everything from a single presentation"; "Auto-Paginated Text — Long passages of text automatically flow across multiple slides… breaks content at natural reading points"; "Timed Advance & Scheduled Play"; "Time Triggers — Trigger specific cues or presentations at exact times"; "PowerPoint Import — no Microsoft Office installation required"; templates, presets, drag-and-drop.
- **Cues vocabulary**: demo titles "Cues Library Basic/Detailed", "Blank Cues", "Layers Tab", "Key Objects" (persistent clock/song title/logo on every slide).
- **Media**: motion/still backgrounds, Pixabay/Unsplash integration, Shift Worship integration, NDI support, step transitions, plugins.
- Business model: one-time purchase ($599 site license; LE single-computer subscription tier), optional Plus membership.

### OpenLP (OpenLP Developers) — evidence layer A

- Self-label: "Free Worship Presentation Software for your Church"; "a feature rich open-source church presentation platform that doesn't tie you down to subscription renewals, device platforms, or even the presentation computer."
- **Feature set (official)**: "Display songs, Bible verses, presentations, images and more"; "Control OpenLP remotely via your mobile web browser"; "Quickly and easily import songs from other popular presentation packages."
- **Songs**: "Import songs from a variety of sources, **tag verse types, set ordering of verses**, add formatting, manage authors, search through songs and even add backing tracks to songs."
- **Bibles**: "Import Bibles from a number of formats, or even download a few verses you need from a Bible site, display verses in varying formats, easily search verses by **scripture reference (e.g. Luke 12:10-17)** or by phrase."
- **Custom slides**: "Store your **liturgy, announcements, or other custom slides** in OpenLP. Just like a song, but with less structure, custom slides can also contain formatting and can be set to loop."
- **Presentations**: "Integration with PowerPoint, PowerPoint Viewer and LibreOffice Impress… import your presentations into OpenLP and control them via OpenLP."
- **Pictures**: "organise them into folders. Create slide-shows by simply selecting multiple songs and drag-and-dropping the selection into the service, with auto-forwarding."
- **Remote**: "Change slides, or even change what is currently presenting from your phone. Search for songs, Bible verses, images and more without needing to touch the computer"; web app + Android/iOS apps; "Search, **go live**, control slides."
- **Stage view**: "Built-in stage view accessible from any device with a web browser. Use any device on the local network as your stage monitor, meaning unlimited stage monitors without any extra hardware constraints."
- Media via VLC integration (broad format support). Cross-platform: Windows, macOS, Linux, FreeBSD.
- Denominational spread evidence (testimonials): Catholic parish (St Patrick's Church, Canada — "the young lady who does our overheads… our priest was ecstatic"), Bible college (Cape Town), small churches.

### Presenter by WorshipTools (WorshipTools) — evidence layer A

- Self-label: "Sleek, simple, lightweight presentation solution designed exclusively for churches and ministries"; "Free volunteer friendly, feature-rich church presentation solution."
- **Cloud sync as core**: "Cloud syncing is at the core of Presenter, syncing all your presentation assets with our cloud. This means anywhere access to your **song lyrics, videos, images and cue lists** from any computer."
- **Multiple outputs**: "set multiple output screens, each with a different visual layout. There's no limit to how many… Create a **live stream lyrics output or a stage display confidence monitor** with a few clicks."
- **Bibles**: "Built-in Bibles allow you to **display scripture with just the reference**."
- **SongSelect**: "Import song lyrics, chords and lyric videos directly into Presenter from CCLI SongSelect"; SongSelect Lyric Videos ("church-ready, fully legal").
- **Remote + stage display**: "The Presenter Remote allows you to remotely control your presentation from your phone or tablet. The Presenter Stage Display app shows the **active slide and what's coming up next** to musicians and those on stage during service."
- **Suite context**: sibling apps Planning ("Worship service planning and scheduling"), Charts (sheet music), Community (church database), Rehearse. Planning page (per worship-planning pass): "Songs and services sync to the cloud, allowing you to open in Presenter, WorshipTools' presentation software."
- Loop Connect (Prime integration): "automated lyric slides… choose the number of lines per slide & your entire setlist will be added to Presenter with perfect spacing, spelling & timing."

## Cross-product Comparison

| Dimension | ProPresenter | EasyWorship | MediaShout | OpenLP | Presenter (WorshipTools) |
|---|---|---|---|---|---|
| Self-label | presentation & worship software | church presentation software | church/worship presentation software | worship presentation software / church presentation platform | church presentation software |
| Content library | songs (SongSelect + copyright), 130+ Bible translations, media (ProContent) | songs (SongSelect 500k+), 90+ Bibles, media library | lyric library (2,300+ incl.), 70 Bibles, media/backgrounds | songs, Bibles, media, pictures, custom slides (liturgy), presentations | songs (SongSelect), Bibles, media, lyric videos |
| Service container | presentation (cue list) | schedule | presentation / cues | service | presentation / cue lists |
| Operator vs audience separation | yes (operator view; stage displays separate) | yes (Schedule/Preview/Live/Resources) | yes (control screen vs main display; Presenter vs Edit view) | yes (preview + live; "go live") | yes (live output; remote) |
| Stage/confidence output | multiple stage displays | confidence monitors | stage display (third output) | stage view (web, unlimited) | stage display app / output |
| Scripture by reference | yes (130+ translations, multiple at once) | yes (90+, keyword + book/chapter/verse) | yes (70 built-in, dual side-by-side, on the fly) | yes (reference search "Luke 12:10-17") | yes ("just the reference") |
| Lyric structure semantics | SongSelect import, copyright auto | pre-formatted lyrics, song structures | verse-tagged library, lyrics on the fly | verse types + verse ordering | SongSelect lyrics/chords |
| Copyright/licensing | auto copyright display; CCLI/OneLicense | CCLI auto-reporting | CCLI auto-reporting; royalties paid | imports from other packages | SongSelect lyric videos "fully legal" |
| Livestream output | RTMP + Resi + NDI | NDI + alpha (OBS/vMix/Wirecast) | NDI | — | live stream lyrics output |
| Remote control | iOS/Android + stage apps | mobile app + StreamDeck + MIDI | plugins | web + Android/iOS | remote app |
| Announcements/messages | announcement layer | message alerts + web display | announcements; key objects | custom slides (loop) | — |
| Timers/countdowns | stage clock/countdown | countdown media | countdowns, time triggers, timed advance | — | — |
| PowerPoint interchange | (import via ecosystem) | import | import (no Office needed) | import + control | — |
| Planning integration | Planning Center import | own Planning Beta import | — | import from other packages | sibling Planning sync |
| Sermon support | sermon notes on stage display | sermon slides editor + PPT import | Sermon Builder | presentations import | — |
| Business model | subscription (+campus seats) | subscription | one-time (+optional Plus) | free open source | free (+ suite) |
| Age | 20+ years | 25+ years | 25+ years (1999 origin claim) | ~2004– | 2015– |

### Cross-product commonality (evidence layer B)

Present in **5/5**: content library (songs with lyric text + scripture + media); ordered service container; operator/audience separation; live cueing ("go live" / Live area / control screen); stage or confidence output (form varies); scripture by reference; remote control.

Present in **4/5**: CCLI SongSelect integration + copyright handling (all but OpenLP); media/backgrounds; PowerPoint interchange (all but Presenter per fetched pages); announcements (all but Presenter per fetched pages).

Present in **3/5 or fewer**: livestream output (4/5 actually — all but OpenLP); timers/countdowns; planning hand-off; in-product sermon builders; dual translations side-by-side; MIDI/StreamDeck; cloud sync (1/5 as core).

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures + one domain binding:

1. **The worship content library** — the product holds reusable, display-ready worship content: characteristically **songs with lyric text**, **scripture passages**, and **media** (images/videos), organized for retrieval (search by title/reference/keyword). Remove → generic presentation software (content authored from scratch each time, no accumulating library).
2. **The service presentation** — an **ordered cue list for a dated service occasion**, assembled from the library (drag items in, arrange order). Remove → a library browser or media player with nothing to run.
3. **The live cueing loop with separated operator and audience surfaces** — during the service an **operator advances items in real time**; the **audience output shows only what is live**, distinct from the operator's control view (which shows the plan, previews, and what's next). Remove → static deck playback (a slideshow file) or unattended scheduled signage.

**Domain binding**: the content and the occasion are **worship-service** content and occasions (lyrics, scripture, sermon support, announcements; the weekly gathering). Remove the binding → generic presentation/live-display tooling.

Jointly-held load-bearing analysis:

```text
1 alone            = media/asset library or songbook database
2 alone            = a playlist
3 without 1+2      = a media player / teleprompter
1+2 without 3      = a playlist builder with no live display
1+3 without 2      = ad-hoc cueing with no service container
2+3 without 1      = generic presentation software running a slideshow
                     (PowerPoint applied to worship — the boundary edge)
```

### L1 — Common Mature Structure

- **Multi-output display**: audience screen(s) + operator preview + **stage display / confidence monitor** (5/5 in some form; depth varies from a web stage view to multiple independent stage screens).
- **Themes/templates** applied across the service (EasyWorship "one theme, every slide"; MediaShout templates/presets).
- **Slide editing** inside the product (depth varies from basic text slides to multi-layer editors).
- **Announcements / message alerts** (ProPresenter announcement layer; EasyWorship real-time alerts; MediaShout announcements; OpenLP custom slides).
- **Countdowns / clocks / timers** (ProPresenter stage clock; EasyWorship countdown media; MediaShout time triggers).
- **Remote control** from phone/tablet (5/5).
- **CCLI SongSelect integration + copyright display/reporting** (4/5; OpenLP imports from other packages instead). Licensing-regime packaging — see L2 note.
- **PowerPoint interchange** (import; OpenLP also controls imported decks).
- **Media playback**: motion/still backgrounds behind text; video/audio clips.
- **Auto-pagination of long text** across slides (MediaShout explicit; others handle lyric blocks natively).
- **On-the-fly insertion** mid-service without disturbing the plan (MediaShout explicit; OpenLP remote search + go live).

### L2 — Variant / Optional Structure

- **Livestream output** (NDI / alpha channel / RTMP destinations) — era-current; absent in OpenLP's fetched feature set; the 1999-era core ran without it.
- **Cloud sync** (core at Presenter; local-first at the others).
- **Planning hand-off** (Planning Center import at ProPresenter; own-suite sync at EasyWorship/WorshipTools; generic import at OpenLP; absent at MediaShout's fetched pages).
- **In-product sermon building** (MediaShout Sermon Builder; EasyWorship sermon slides; ProPresenter stage-display sermon notes) — prep capability inside a display product.
- **Dual/multiple Bible translations side-by-side** (MediaShout dual Bibles; ProPresenter multiple translations at once).
- **Chord display on stage screens** (ProPresenter).
- **MIDI/StreamDeck/hardware control** (EasyWorship, MediaShout plugins).
- **Multi-camera streaming/recording** (ProPresenter — deepest overlap with broadcast).
- **Business model**: subscription (ProPresenter, EasyWorship) vs one-time (MediaShout) vs free/open-source (OpenLP, Presenter).
- **Platform posture**: Windows-first (MediaShout) vs cross-platform (OpenLP, EasyWorship 8, ProPresenter).
- **Denominational/workflow spread**: evangelical worship-band sets (SongSelect-centric), liturgical use (OpenLP custom slides for liturgy; Catholic parish testimonial), sermon-note-centric teaching churches.
- **CCLI reporting** = licensing-regime packaging, not definitional (consistent with the worship-planning pass's CCLI finding).

### L3 — Vendor-specific (Research Notes only)

- ProPresenter: ProContent media subscription, ProVideoPlayer (separate multi-screen media server product), Lyric Banner, 8-layer slide editor, Resi streaming integration, campus seat licensing, published comparison-guide library.
- EasyWorship: Online Media Designer, contiguous schedule layout, Planning Beta, bundled premium media.
- MediaShout: "Cues" terminology, Key Objects (persistent overlay elements), Shift Worship media integration, Pixabay/Unsplash built-in, Plus membership/support tiers, bundled church computers.
- OpenLP: VLC-based media playback, FreeBSD support, web-browser stage view ("unlimited stage monitors"), portable Windows build.
- WorshipTools: Loop Connect (Prime), Charts sibling integration, SongSelect Lyric Videos, suite packaging (Planning/Charts/Community/Rehearse).

## Historical / Market-Sample Check

- **MediaShout's own 1999 origin claim** (vendor-stated): church-specific software "to display non-linear presentations controlled on a separate screen by an operator" — i.e., library + non-linear service + separated operator screen, with **no** cloud, NDI, livestream, or remote apps. Satisfies the L0 with zero modern machinery.
- **OpenLP** (copyright 2004–2019 on site) — open-source, no subscription, no built-in licensing integrations: satisfies the L0.
- **Conceptual ancestor**: the acetate/transparency-projector workflow — a songbook (library), an order of worship (service), a human operator placing transparencies (live cueing), a screen the congregation watches (audience output) distinct from the operator's table (operator surface). The L0 holds pre-software.
- **Denominational breadth**: Catholic parish (OpenLP testimonial), liturgy storage as custom slides, evangelical SongSelect-centric sets, teaching churches with sermon notes — all fit the same core.
- Conclusion: the definition is not over-fitted to the modern multi-output/livestream/cloud implementation.

## Boundary Findings

1. **vs Presentation Application (§03.04) — advance note DISCHARGED, keep-both RATIFIED.**
   The presentation grammar (ordered visual units delivered to an audience) is shared, but the object models differ:
   - Presentation Application centers the **authored deck artifact** — a self-contained work the author composes slide-by-slide (freeform spatial placement) and delivers as one piece; the deck is the record.
   - Worship Presentation Software centers the **library + cued live display** — content is drawn from an accumulating worship library (songs with lyric blocks, scripture by reference, media), assembled into a dated service's cue list, and **operated live by a dedicated operator** whose control surface is separate from the audience output.
   - The market itself separates them: Renewed Vision publishes comparison guides "ProPresenter vs PowerPoint/Keynote/Prezi"; MediaShout positions itself "Not a Generic Presentation Tool" and claims the 1999 category founding as "the switch from limited office-style software like Microsoft Powerpoint to church-specific software to display non-linear presentations controlled on a separate screen by an operator."
   - The edge case — a church running its service from PowerPoint — is the L0's "2+3 without 1" branch: generic grammar applied to worship, not this Type. Conversely, worship presentation products include slide editors, but authoring serves the library/cueing model (themes applied to lyric/scripture blocks), not freeform deck composition as the center.
   - The advance note's expectation is confirmed: this Type is defined by its own live-display/library/service semantics, not absorbed by the generic grammar.

2. **vs Worship Planning (§25) — ratify request DISCHARGED, keep-both RATIFIED from the display side.**
   Seam = preparation/organization vs live in-service display. Planning software organizes what will happen and equips the team before the service; presentation software displays content to the congregation during it. They meet at the **hand-off**, now evidenced from the display side:
   - WorshipTools: "Songs and services sync to the cloud, allowing you to open in Presenter, WorshipTools' presentation software" (planning→display sync inside one vendor suite).
   - ProPresenter: "natively integrates with Planning Center Online… your worship set automatically created."
   - EasyWorship: Planning Beta "import your agenda into our presentation software so you aren't starting from a blank screen."
   - MediaShout's fetched pages show **no** planning hand-off — confirming the hand-off is common, not definitional (matches the worship-planning pass's "3/5, hand-off depth varies" finding).
   - Keep-both: the plan (content + people + files, pre-service) and the display (cued live output, in-service) are distinct work with distinct objects.

3. **vs Sermon Management (§25) — forward flag DISCHARGED, keep-both CONFIRMED.**
   Seam = live in-service display vs the message as a record that outlives the service. They meet at **slides**: prep products export slides into presentation software (Sermonary → PowerPoint/ProPresenter, per that pass); presentation products import PowerPoint sermon decks (EasyWorship, MediaShout, OpenLP) and some build sermon slides in-product (MediaShout Sermon Builder, EasyWorship Presentation Editor). The in-product sermon builder is a **prep capability inside a display product**, not evidence of Type merger: the sermon record (library, publication, archive) remains Sermon Management's center; the display act remains this Type's center. Proclaim — the record-while-presenting straddler — remained unreachable this pass (see Uncertainties); the seam is held on the evidence above.

4. **vs Church Management System (§25)** — no overlap: ChMS centers congregation people/giving records; this Type is a production/display tool with no congregation-record core. Suite bundling exists (WorshipTools Community = church database sibling; Presenter = display sibling) — packaging, not identity.

5. **vs Digital signage / scheduled media players** — signage is unattended, schedule-driven playback; this Type is **operator-cued live during an occasion**. The overlap edge is pre-service loops and timed advance (MediaShout "Scheduled Play", "Time Triggers") — automation features inside a live-cueing product, not the center.

6. **vs Livestream/broadcast production (§27 neighbors)** — worship presentation **outputs to** the stream (NDI/alpha/RTMP, lyric overlays) but stream switching/production is a different Type. ProPresenter's multi-camera streaming/recording is the deepest overlap edge (vendor-specific breadth), held as L2/L3.

7. **vs Scripture Study Application (§25)** — study centers the corpus + passage-keyed study layer for personal study/sermon prep; this Type **displays** scripture on screens during the service. They meet at Bible translations (presentation tools license translations for display; study tools for reading/study). Reference-addressed retrieval appears in both but serves different acts.

## Uncertainties

- **Proclaim (Faithlife) unreachable ×2** (timeouts; consistent with the sermon-management and worship-planning passes). The cloud/ecosystem pole is therefore evidenced **indirectly** (Renewed Vision's comparison-guide listing; the worship-planning pass's planning-side integration copy). Assertions about Proclaim's own behavior are NOT made. If a future pass reaches Faithlife, re-verify: cloud service assembly, Faithlife ecosystem integration depth, and the record-while-presenting posture.
- Renewed Vision's /propresenter/ product page returned 404; evidence taken from the root and /industries/worship pages (both official). Feature depth (e.g., exact layer counts) not independently verified beyond vendor copy.
- Exact numeric limits (translation counts, song-library sizes, seat counts) are vendor-marketing figures; they vary by plan and are **not** carried into the final document as structural claims.
- MediaShout's 1999 founding claim is vendor-stated (self-description as "the original"); used as lineage evidence, not independently verified.
- Operator-role permission models (multi-user roles inside the presentation product) were not deeply evidenced on fetched pages; not asserted in the final document beyond the operator/volunteer framing the vendors themselves use.

## Final Synthesis

A **Worship Presentation Software** is the live in-service display system of a worshiping congregation. Its defining core is three jointly-held structures: (1) a **worship content library** — reusable display-ready content, characteristically songs with lyric text, scripture passages, and media; (2) the **service presentation** — an ordered cue list for a dated service occasion assembled from that library; (3) the **live cueing loop** — an operator advances items in real time during the service, with the audience output showing only what is live, separated from the operator's control view. The content and occasion are worship-service content and occasions.

Around that core, mature products add: multi-output display (stage/confidence monitors, lobby feeds, livestream lyric outputs), themes/templates, slide editing, announcements and alerts, countdowns/timers, remote control, licensed lyric integration with copyright handling, PowerPoint interchange, and on-the-fly insertion. Variants span business model (subscription / one-time / free / open-source), platform posture, cloud vs local, planning hand-off depth, and denominational workflow (worship-band sets, liturgical rites, sermon-note teaching).

The Type's boundaries: it is not generic presentation software (no accumulating worship library, no operator-cued live loop → Presentation Application); it is not the pre-service organization of the service (→ Worship Planning); it is not the sermon as an enduring record (→ Sermon Management); it is not congregation records (→ ChMS); it is not unattended signage or stream production (adjacent output surfaces).
