# Research Notes — Photo Culling Application

## Research Goal

Understand what a dedicated Photo Culling Application actually is, from real products: what its world is made of, what users do in it, how review-and-decision work flows, what rules and states matter, and where its boundary runs against Image Viewer, Photo Workflow / Catalog Application, Photo Editor, Tethered Shooting, and Image Batch Processor.

## Initial Boundary

Working hypothesis before research: culling = reviewing a large batch of photos from a shoot and deciding which survive to editing. The product exists because the review loop at volume (hundreds–thousands of frames) has its own speed and ergonomics problems that editing-centered catalog apps handle poorly.

Nearest neighbors suspected up front:
- Image Viewer (displays, but does it decide?)
- Photo Workflow / Catalog Application (culling embedded as a stage)
- RAW Photo Editor / Photo Editor (decision vs. pixel editing)
- Tethered Shooting Application (capture side vs. review side)
- Image Batch Processor (mass transformation vs. selection)
- DAM / Media Asset Management (long-term collection vs. shoot-cycle selection)

## Research Questions

1. What is the unit of work — how does a batch enter the application (card ingest, folder, session)?
2. What is the selection-state model per photo (ratings, labels, pick/reject flags) and where does it live (XMP sidecar, internal DB)?
3. How does rapid review work mechanically (preview rendering, zoom, keyboard-driven navigation)?
4. How are similar/duplicate shots handled (grouping, stacking, comparison views)?
5. What does the AI layer do in modern products (scoring focus/eyes, auto-grouping, auto-ranking) and does it decide or assist?
6. How do selections flow onward (XMP, folder moves, one-click export to editing apps)?
7. What rules matter (non-destructive decisions, reject semantics)?
8. Where is the boundary against catalog apps and viewers?

## Representative Products

| Product | Philosophy | Segment | Evidence reached |
|---|---|---|---|
| FastRawViewer (LibRaw) | Manual culling on RAW-truth previews; catalog-free folder tool; technical evaluation of the RAW itself | Pro/enthusiast RAW shooters, photojournalists | Tier-1: full homepage + 2 manual pages (strong) |
| Narrative Select | AI-assisted culling — AI assesses, human decides; speed-first import | High-volume wedding/family/portrait pros | Tier-1: homepage + FAQ (good; help center not fetched) |
| Aftershoot | AI culling (automated or assisted modes) as first module of a cull→edit→retouch→deliver platform | High-volume wedding/event pros | Tier-1: homepage + FAQ (good; help center not fetched) |
| Photo Mechanic (Camera Bits) | The long-standing manual ingest/cull standard | Photojournalists, sports, agency | **Unreachable: home.camerabits.com timed out ×2. Market role evidenced only indirectly (named integration target by Aftershoot and Narrative; FastRawViewer ships keymap presets imitating "widely-used applications").** |

Sample shape: 2 manual-philosophy poles (RAW-technical vs. keyboard/ingest) + 2 AI poles (assisted vs. automated-first-pass), 4 different customer emphases. Lightroom Classic / Bridge / Capture One enter only as boundary + interop evidence (via sampled products' own documentation of XMP/ratings compatibility).

## Sources

- FastRawViewer homepage — https://www.fastrawviewer.com/ (fetched 2026-09-08)
- FastRawViewer manual: Metadata — https://www.fastrawviewer.com/usermanual13/xmp-metadata (fetched 2026-09-08)
- Narrative homepage + FAQ — https://www.narrative.so/ (fetched 2026-09-08; feature pages /select, /select/face-assessments referenced from nav, not fetched)
- Aftershoot homepage + FAQ — https://aftershoot.com/ (fetched 2026-09-08; Selects product page /selects/ referenced from nav, not fetched)
- Photo Mechanic — https://home.camerabits.com/support/ and /products/photo-mechanic-6/ — **both timed out ×2; no direct evidence this session**
- Adobe helpx (Lightroom Classic flags page) — timed out ×1; not used; catalog-app boundary supported instead via sampled products' interop documentation

## Product Observations

### FastRawViewer (evidence layer A — official site + manual)

- Self-positioning: "sort and cull RAW images lightning fast and based on the quality of the RAW itself, not JPEG previews"; renders RAW on-the-fly rather than showing embedded JPEGs; "To Choose Correctly You Need To See a Correct Preview".
- Catalog-free posture: "Works with any file system, access any media from flash card to network server, with no intermediate catalogues created and no disk space wasted."
- Decision vocabulary: "tools for the rating, labeling and sorting photos, and filtering of any number of RAW images."
- Technical evaluation layer (its differentiating philosophy): RAW histogram, RAW statistics, over-/underexposure indication from RAW data, Shadow Boost, Highlight Inspection, Focus Peaking, per-channel view — "features for the rapid and reliable technical evaluation of RAW shots."
- Views: Grid View and Single File View (one keystroke switches); Multi-window view comparing 2 or 4 images "to compare the quality of the shots in the series"; one thumbnail can toggle RAW / embedded JPEG / external JPEG; full-screen mode; filmstrip; zoom/pan ("view it in actual size").
- Selection mechanics: select/deselect one to all images; "move files to _Selected" subfolder; "move to _Rejected" subfolder; save/append/load selection lists to file.
- Metadata (manual, XMP page): records all changes into separate sidecar XMP files ("analogous to Adobe Bridge"); ratings 1–5, clear-rating action, optional XMP Reject rating (−1) for Adobe Bridge compatibility; 4 color-label styles (Adobe Bridge, Adobe Lightroom colors, Lightroom "Review Status" wording, custom); title/description; orientation. XMP read/written immediately; sidecar vs. embedded-XMP recency rules; per-format sidecar support toggles.
- Handoff to converters (documented in detail): Adobe Lightroom ignores XMP while importing straight off a flash card → recommended flow is copy only the needed images (selects) to disk first, then import; for already-cataloged files use Lightroom "Metadata – Read metadata from files"; Lightroom "Automatically write changes into XMP" setting mentioned for reverse sync. Also documents writing exposure/WB/contrast as XMP so "Adobe Lr/ACR will go from there" — preliminary adjustments as a starting point, not editing output.
- Keyboard-centric: shortcuts fully remappable; downloadable keymap sets "which simulate the shortcuts of some widely-used applications."
- Undo machinery for file operations.

### Narrative Select (evidence layer A — official homepage + FAQ)

- Self-positioning: "fast, AI-assisted culling and editing software specifically designed for photographers… for high-volume photographers." Use cases: weddings, family, portrait.
- Gives the canonical definition of the activity in its FAQ: "Culling is the process of going through all the images from a shoot and choosing the best ones (the ones you want to edit). By culling, you will get rid of duplicates and objectively bad images and you will save yourself time when it comes to editing."
- Explicit Type statement: "Culling with a dedicated image selection tool (like Narrative) is very different to culling within your editing program."
- AI posture — assist, not decide: "AI-assisted… you stay in control of the final decisions, while the AI handles the heavy lifting… the selections… are made by you." "The best AI tools don't make creative decisions. They make space for yours."
- AI assessments (FAQ): focus assessment (how well subject is in focus), eye assessment (closed eyes / blinking / looking down), image assessment ("whether there are other images within a scene that may be better than this one").
- "Potential Picks" filtering: "Filtering by Potential Picks means you only need to look through half of your images to pick a great selection."
- Import stage: "Import thousands of RAWs in seconds. Work offline, no cloud required. Ingest from SD cards and create backups simultaneously."
- Culling surfaces named: Scenes View ("see how your shoot unfolded"), Close-ups Panel ("spot the best expressions fast"), Face Assessments.
- End-to-end flow as marketed: Import → Cull → (AI-edit) → "Export your selects… Send your selects to your editing program or publish directly." Handoff: "one click import to edit your shoot in Lightroom Classic (mac and windows) as well as Lightroom CC, Photoshop and Capture One on mac."
- Format list: CR2/CRW/CR3, NEF/NRW, RAF, DNG, RAW, RWL, ARW, RW2, ORF, PEF, FFF, 3FR, JPG, HEIC/HEIF.

### Aftershoot (evidence layer A — official homepage + FAQ)

- Self-positioning: "AI-powered photo post-processing software… helps you cull, edit, and retouch images faster in one app." Cull pitch: "Go from thousands of images to final selections in just minutes" (marketing claim — not quoted as fact).
- Two culling postures: "Choose AI Automated Culling for a hands-off first pass, or AI Assisted Culling to stay in the driver's seat. The workflow adapts to you."
- Duplicate handling: "AI reads the scene and moment behind each frame, separating true duplicates from creative variations — so tight culls never lose the shots that matter."
- Human review retained: "Review AI selections your way — compare duplicates in Survey Mode, rate with one click using Spray Can, and switch between Grid and Loupe views to fine-tune every pick."
- Preference learning: "The more you cull, the sharper Aftershoot gets. It picks up your preferences, patterns, and creative instincts."
- Non-destructive + sidecar (FAQ): "Our workflows are non-destructive, which means we don't overwrite your originals, and ratings for RAW workflows are typically written to XMP sidecar files instead of changing the source files themselves." Works offline; files stay local.
- Handoff: "One-Click Export to the platform of your choice" — Photo Mechanic, Capture One, Photoshop, Lightroom, Lightroom Classic, Bridge (brand logos in export section).
- Suite context: culling (Selects) is one module beside Edit / Retouch / Galleries.

### Photo Mechanic (evidence layer: none direct this session)

- No official page reachable (2 timeouts on support and product pages).
- Market role supported only indirectly: named as an export destination by Aftershoot ("One-Click Export" logo set) and by Narrative's compare page nav (/compare/photo-mechanic-vs-narrative); FastRawViewer's keymap presets reference "widely-used applications."
- No operational claims made in this research about Photo Mechanic's internals. Its inclusion as a representative product rests on its market standing and the integration-target evidence above; treat all Photo Mechanic-specific detail in public lore (contact-sheet workflow, IPTC captioning on ingest) as UNVERIFIED here.

## Cross-product Comparison

| Dimension | FastRawViewer | Narrative Select | Aftershoot | Common? |
|---|---|---|---|---|
| Batch of shoot photos as working set | folder/card of RAWs, "any number of RAW images" | "all the images from a shoot", thousands of RAWs imported | "thousands of images" per shoot/album | **Common (4/4 incl. PM as integration context)** |
| Per-photo decision state | ratings 1–5 + labels (+ reject −1), title/description, in XMP | picks vs. non-picks over AI assessments | ratings via "Spray Can", AI selections reviewed/tuned | **Common; vocabulary graded vs. binary varies** |
| Decisions stored without touching pixels | XMP sidecars (+ embedded XMP) | implied non-destructive (AI preset flow, offline local) | "non-destructive… ratings… written to XMP sidecar files" | **Common (XMP sidecar the named substrate in 2/4, Bridge/Lr-compatible in FRV's own spec)** |
| Selection drives what continues | filter/sort by rating/label; move to _Selected; copy selects to disk for Lightroom import; converters read XMP | "send your selects to Lightroom/C1/Photoshop"; Potential-Picks filter | "One-Click Export" to 6 downstream apps | **Common** |
| Fast preview as working constraint | renders RAW on-the-fly, not embedded JPEG | "no loading bars… thumbnails load immediately" | preview rendering noted in system requirements | **Common (philosophy differs: RAW-truth vs. speed-first)** |
| Zoom/inspect at detail level | zoom/pan, actual size, focus peaking | Close-ups Panel, face focus assessments | Survey/Loupe views | **Common (implementation varies: manual zoom vs. AI assessment)** |
| Similar-shot grouping/comparison | multi-window 2–4-up compare | "other images within a scene that may be better" | duplicate grouping "with intent", Survey Mode | **Common (manual compare vs. AI grouping)** |
| Keyboard-first decision entry | remappable hotkeys, keymap presets | not stated on fetched page | "rate with one click" | Common in manual tools; unstated in AI-assist pole |
| Ingest with backup | works directly off card or disk | SD ingest + simultaneous backups | not stated on fetched page | Common in manual/AI poles |
| AI layer | none | assessments (focus/eyes/scene), Potential Picks | automated or assisted modes, learns preferences | Variant (2/4; era-current) |
| Technical RAW evaluation toolset | RAW histogram, OE/UE, focus peaking, per-channel, Shadow Boost, Highlight Inspection | face-level focus AI | not stated | Product-specific (FastRawViewer philosophy) |
| Part of wider suite | no (single-purpose) | cull + edit + publish | cull + edit + retouch + galleries | Variant (market packaging, not Type identity) |
| Catalog/library across shoots | explicitly none ("no intermediate catalogues") | per-shoot import | per-album | **Common: the shoot/batch is the scope, not a lifetime library** |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal; three jointly-held structures)

1. **The shoot's photo batch as the unit of review.** The working set is a large multi-image batch from one shoot (ingested from card or disk), brought in and reviewed together. Remove → single-image viewer territory; the Type loses its reason to exist.
2. **A recorded per-photo selection decision, held without altering image content.** Every photo receives an evaluative decision — keep/reject, usually graded (ratings, labels, picks) — attached as decision metadata (XMP sidecar, internal state, or destination folder) while the pixels stay untouched. Remove the decision → plain viewer. Alter pixels → editor.
3. **The decision set drives what continues.** Decisions are operational: the user can filter/sort to isolate the keepers, and hand the selected subset onward to editing/delivery (XMP read by converters, moves/copies to selection folders, one-click export to editing applications). Remove → browsing with inert marks.

Jointly-held is load-bearing: 1 alone = file browser/viewer; 2 without 1 = a rating gimmick on scattered images; 3 without 1+2 = a filter with nothing behind it; 2+3 without 1 degenerates the posture (the Type exists for volume review).

### L1 — Common Mature Structure

- fast preview rendering so review never waits (RAW on-the-fly render or prebuilt/embedded previews)
- detail inspection: zoom to 100% / loupe / focus aids
- keyboard-driven navigation and decision entry, with remappable shortcuts
- decision vocabulary of ratings + color labels + pick/reject (graded or binary)
- filter/sort by decision state
- grid (contact-sheet) view + full-screen single-image view; filmstrip
- comparison of similar shots (side-by-side/multi-up; grouping of duplicates)
- ingest step from card/disk, often with backup copies
- orientation/rotate during review
- XMP sidecar (or equivalent portable metadata) so downstream converters read the decisions

### L2 — Variant / Optional

- AI evaluation layer: focus/blur scoring, closed-eye detection, expression assessment, scene/duplicate grouping, auto-ranking ("potential picks"), automated first-pass culling
- preference learning from the user's past culls
- manual-mode vs. automated-mode postures inside one product
- technical RAW-evaluation toolset depth (histograms, highlight inspection, focus peaking)
- handoff style: XMP sidecar vs. one-click project export vs. folder moves/renames
- single-purpose tool vs. module inside a cull→edit→deliver suite
- offline/local vs. cloud processing
- RAW+JPEG pair handling
- metadata entry during cull (title/description/captions)

### L3 — Vendor-specific (research notes only)

- FastRawViewer: _Selected/_Rejected subfolder conventions, selection-list save/append/load files, XMP settings granularity (sidecar-vs-embedded recency rules, label-style presets, Reject-rating toggle, per-format sidecar toggles), Adobe-process-version choice for written XMP, .rpps compatibility, keymap files, undo of file operations.
- Narrative: Scenes View, Close-ups Panel, "Potential Picks" term, Personal/Artist/Core AI Presets, Publish, mac-only Capture One handoff.
- Aftershoot: Survey Mode, Spray Can, duplicate "intent" grouping, opt-out of data sharing on import, Edits/Retouch/Galleries suite packaging.
- Photo Mechanic: unverified this session — no vendor detail recorded.

## §24 Historical / Market-Sample Check

Question: would older, regional, platform-native, differently-positioned products still fit the L0?

- **Analog antecedent** — developed roll + contact sheet + grease pencil: batch (the roll/sheet), per-image decision (circled/marked frames), selection drives next stage (marked frames enlarged/printed). Satisfies all three legs at analog level.
- **Late-1990s/2000s digital culling tools** (the era of Photo Mechanic and its contemporaries): folder ingest, thumbnail sheet, rating/flag, sort/filter, batch rename/copy, handoff to editors — satisfy L0 with no AI, no XMP sidecars, no on-the-fly RAW rendering (internal databases / file moves instead).
- **Platform-native photo apps** (OS Photos apps with "favorites" hearts): carry per-photo decision + filtering, but the posture is lifetime-library browsing, not shoot-scoped review-and-handoff; center of gravity differs — treated as boundary overlap, not a counter-example. L0 phrasing ("shoot's batch as unit of review… selection drives what continues") deliberately excludes them.
- The L0 names no substrate technology: no RAW, no XMP, no AI, no star scale, no speed figure. The abstraction holds across eras.

Conclusion: historical check passed.

## Vendor-specific Findings

See L3 above. Additionally: FastRawViewer's preliminary exposure/WB adjustments written as XMP "starting point" for Adobe converters are cull-adjacent, not editing output — placed as optional capability, not core.

## Boundary Findings

| Neighbor | Distinction | "Remove what → becomes the other Type" |
|---|---|---|
| Image Viewer | viewers display; cullers decide. Capability overlap exists (some viewers offer ratings/filters), but the posture differs: shoot-scoped review-to-selection vs. general browsing. Narrative's own FAQ: "a dedicated image selection tool… is very different to culling within your editing program." | remove per-photo decision recording + selection output → Image Viewer |
| Photo Workflow / Catalog Application | catalog apps center a lifetime library + editing; culling is one embedded stage (FastRawViewer's manual documents Lightroom/Bridge sharing the same ratings/reject/label vocabulary and the card-import XMP limitation — direct evidence the same decision layer exists inside those apps). Dedicated cullers are catalog-free (FRV: "no intermediate catalogues"), shoot-scoped, and hand off. | add cross-shoot library + editing pipeline → Workflow/Catalog; strip those → culler |
| Photo Editor / RAW Photo Editor | culling records decisions; it never transforms pixels. FRV's XMP exposure/WB writes are converter "starting points," not edit output. Aftershoot/Narrative ship editing as separate modules/products. | add pixel transformation → Photo Editor |
| Tethered Shooting Application | capture-side control of the camera vs. review-side decisions on captured images | move to the capture side → Tethered Shooting |
| Image Batch Processor | transforms many images' content en masse; culling decides which images continue, content unchanged | add mass pixel transformation → batch processor |
| DAM / Media Asset Management | long-term collection governance across the organization vs. one photographer's shoot-cycle selection | widen scope to org collections/lifecycle → DAM |

## Uncertainties

1. **Photo Mechanic operational detail unverified** — vendor site unreachable ×2 this session. Its inclusion as representative rests on market standing + integration-target evidence from Aftershoot/Narrative. All PM-specific mechanics excluded.
2. Reject semantics vary: FRV documents a _Rejected subfolder move (and optional XMP −1 reject for Bridge compatibility); Aftershoot states non-destructive sidecar ratings. Whether "delete rejects" is a widespread capability was **not** verified — final doc avoids claiming default-deletion behavior.
3. AI accuracy/speed claims ("minutes", "100% AI precision", fps numbers) are vendor marketing — not repeated as facts.
4. Narrative/Aftershoot help centers not fetched; feature surfaces beyond homepage/FAQ (e.g., exact keyboard model in AI products) unconfirmed.
5. Handoff granularity into Capture One on Windows (Narrative states mac) — minor, unverified.

## Final Synthesis

A Photo Culling Application is the photographer's shoot-review decision machine: it takes the large batch of photos from a shoot as its unit of work, puts the photographer in a fast review loop over every photo, records an explicit keep/reject (usually graded) decision per photo without touching image content, and turns those decisions into the working set that continues to editing and delivery. Fast previews, keyboard ergonomics, similar-shot comparison, and XMP-based handoff are the mature mechanics; AI assessment/automation is the current-era variant that assists (or, in one posture, pre-executes) the decision loop while the photographer remains the deciding party. It is not a viewer (no decisions), not an editor (no pixels), not a catalog (no lifetime library), not a batch processor (no transformation).
