# Research Notes — Typeface Design Application

Research date: 2026-09-09
Leaf: Typeface Design Application (DIRECTORY.md §04.18 Typography)
Slug: typeface-design-application

## Research Goal

Understand what a Typeface Design Application is as an Application Type — from the craft/discipline angle the leaf name implies: how typefaces are actually designed in software, what the designed object is, what the design workflow looks like, and what the boundaries are.

This pass carries a **mandatory joint review**: the sibling leaf `font-editor` (§04.18, processed 2026-09-07) flagged "Typeface Design Application" as a PROBABLE ALIAS and explicitly delegated the keep-both vs merge/canonical-name decision to this pass (see STATUS.md Boundary Issues, and research/font-editor.md §Boundary Findings #1). The precedent to mirror is digital-whiteboard ≡ collaborative-canvas: confirm or refute the alias on this pass's own fresh evidence; if confirmed, keep both leaves standing with separate lens documents and escalate the merge/canonical-name decision to directory-level review.

## Initial Boundary

Initial hypothesis before research:

- A typeface design application is software in which a typeface is designed: the designer draws letterforms as glyphs, organizes them into a character set and family, shapes the space between letters, tests the design in real text, and produces font files.
- Primary users: professional type designers (independent or at foundries), graphic/brand designers making custom type, students, icon designers.
- Nearest neighbors: Font Editor (sibling leaf — flagged probable alias), Vector Graphics Editor, Pixel Art Editor, font managers, font generators, publishing applications (font consumers).
- Main unknowns: whether any product population "designs typefaces" without being a font editor; how the craft lens differs structurally from the file/engineering lens; which capabilities the discipline emphasizes.

## Research Questions

1. How do vendors themselves position their products — "font editor" vs "typeface design"? (self-label evidence for the alias decision)
2. What is the designed object in this software — what does the user's world consist of when the work is framed as typeface design?
3. What is the canonical type-design workflow as the field itself organizes it (tutorials, documentation taxonomy)?
4. Which craft-specific structures appear (drawing↔spacing interdependence, contour quality, test texts, interpolation compatibility)?
5. Which capabilities are definitional vs common vs optional vs vendor-specific?
6. Where are the boundaries: vs Font Editor (the alias question), vector editors, pixel editors, font managers, generators, and font-consuming applications?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers — deliberately re-sampling the type-design-positioned pole with fresh fetches so the alias decision rests on this pass's own evidence, not only on the sibling pass:

| Product | Philosophy / tier | Evidence level (this pass) |
|---|---|---|
| Glyphs 4 (Glyphs GmbH, macOS) | professional foundry standard, streamlined, type-design community hub | A — official product page fetched 2026-09-09 (handbook previously fetched at layer A by the font-editor pass) |
| FontLab 8 (FontLab Ltd., Mac & Windows) | professional engineering-depth editor, "go-to app for professional typeface designers" | A — official product page fetched 2026-09-09 |
| RoboFont 4 (TypeMyType, macOS) | code-centric scripting platform, UFO-native, extension ecosystem | A — official product page + documentation root + tutorials index + "Making a font" tutorial fetched 2026-09-09 |
| Birdfont (Johan Mattsson, free) | free lightweight editor, donation-supported | A — official homepage + release notes fetched 2026-09-09 |

Sibling-pass evidence (research/font-editor.md, 2026-09-07, layer A): FontForge (open source; the vendor's own definition of the Type), FontCreator (mid-tier commercial). These are used as cross-checks, not re-fetched.

Coverage: two professional poles (streamlined vs engineering vs code-centric — three philosophies), one free pole, plus two sibling-pass cross-checks (open-source, mid-tier). Platforms: macOS-native ×2, cross-platform, free cross-platform.

## Sources

This pass (fetched 2026-09-09):

- Glyphs — https://glyphsapp.com/ (product page: positioning, feature sections, tutorial index, community/foundry list)
- FontLab 8 — https://fontlab.com/font-editor/fontlab/ (product page: positioning, workflow sections, formats, interchange, upgrade page listing other editors)
- RoboFont — https://robofont.com/ (product page: self-label, technical specs, extensions); https://robofont.com/documentation/ ; https://robofont.com/documentation/tutorials/ (tutorial taxonomy); https://robofont.com/documentation/tutorials/making-a-font/ (canonical workflow walkthrough)
- Birdfont — https://birdfont.org/ (homepage: self-label, tabs, release notes)

Sibling pass (fetched 2026-09-07, recorded in research/font-editor.md):

- Glyphs Handbook — https://handbook.glyphsapp.com/ (+ /create/)
- FontLab 7/8 manual — https://help.fontlab.com/fontlab/7/manual/ , https://help.fontlab.com/fontlab/8/manual/
- FontForge docs — https://fontforge.org/docs/
- FontCreator — https://www.high-logic.com/font-editor/fontcreator
- Birdfont — https://birdfont.org/

Source-access limitations:

- All four fresh fetches succeeded at layer A (official pages directly observed). No fetch failures this pass.
- FontLab evidence is product-page level this pass (manual TOC-level in the sibling pass; the vendor states the v8 manual is under revision). No FontLab-specific behavioral rules are asserted beyond what the product page states.
- Glyphs evidence is product-page level this pass; handbook detail comes from the sibling pass's layer-A fetch.
- No numeric limits, default values, or precise format-version facts are asserted in the final document; vendor numbers stay here.

## Product A — Glyphs 4

### Key observations (evidence layer A unless noted)

- **Self-label (alias evidence)**: "Glyphs 4 is the leading Mac **font editor**: draw quickly, manage efficiently, release with confidence." The rotating headline pairs the tool with creative acts: "Create fonts. Love the process." / "Create icons." / "Create lettering." / "Create logos." / "Create pictos." — the same tool positioned across the type-design and lettering/icon poles.
- **Audience**: testimonials from type designers and foundries (Just Another Foundry, Tabular Type Foundry, Mark Simonson, Nadine Chahine "Arabic type and legibility expert"); a large "community" section listing dozens of type foundries and type design studios worldwide (Dalton Maag "Typeface design studio", Typofonderie "independent digital type foundry", Sandoll "Korean type foundry", etc.).
- **Drawing**: pen points ("turn any path into a living shape… command width, height, and angle"), star nodes (G2 curve transitions), advanced bézier control (batch-edit curvatures, segment harmonization, balance handles); "Easily turn your idea into pristine vectors, and do all the things Illustrator never let you do: nudge, edit multiple handles at the same time, lock angles…"
- **Masters/interpolation**: "Draw and manage multiple master drawings, and then easily produce as many steps in between as you like"; intermediate/alternate masters; master selector for browsing large families; tutorials "Multiple Masters, part 1–3" (setting up masters, keeping outlines compatible, setting up instances).
- **Reuse**: components ("edit the original, and all linked components update immediately… make your **a** the same in **äâãāăȧà**"); smart/corner/segment components, brushes; head components for icon systems.
- **Spacing/kerning**: visual kerning groups ("Drag and drop glyphs straight onto the shelf to build your kerning groups"); contextual kerning tutorial; kerning assistant plug-in (Kern On) marketed in the community section.
- **Testing**: live text preview window ("Put your designs to the test in the revamped text preview window… Try different alignments, trackings and leadings, flip through your instances… even test your OpenType features right here").
- **Color**: color layers, COLRv0/CPAL, COLRv1, SVG, sbix, layered fonts.
- **Export**: "Export all static and variable OpenType font formats: CFF, CFF2, TTF, WOFF, WOFF2"; images PNG/SVG/PDF/SFSymbols; icon fonts.
- **Extensibility**: Python 3 API, plug-in manager, scripts; new scripting window with debug sessions.
- **Tutorial taxonomy (the field's own workflow vocabulary)**: Sketching, Drawing good paths, Multiple Masters 1–3, Diacritics, Reusing shapes (component tricks/corner/smart/brushes/segment), color fonts ×4, monoline, pixel font, variable fonts, vertical metrics, Windows compatibility, Adding glyphs, Batch renaming, UFO, Webfonts, SF Symbols, Ligatures, Stylistic sets, Glyph names, Contextual kerning, Scripting 1–4, Plug-ins.

## Product B — FontLab 8

### Key observations (evidence layer A — product page)

- **Self-label (alias evidence)**: "FontLab 8 is an integrated **font editor** for Mac and Windows that helps you create fonts from start to finish." Simultaneously: "FontLab has been the go-to app for professional **typeface designers** to make smooth and consistent curves, comfortably tweak, space and kern a typeface, and then export technically solid fonts in any format." And: "Love **type design** and font making? FontLab 8 has you covered!" Testimonials header: "WHAT TYPEFACE DESIGNERS SAY".
- **Vendor's own classification of the market (strong alias evidence)**: the upgrade page offers discounts "If you own another font editor" and lists: FontLab 7, FontLab VI, FontLab Studio 5, Fontographer 5, TypeTool 3, **RoboFont**, **Glyphs**. The vendor itself classifies RoboFont and Glyphs as font editors.
- **Interchange**: "Seamlessly interchange with other font editing apps like Glyphs, RoboFont, FontForge and Microsoft VOLT." Formats: opens/exports OTF (CFF), TTF, variable (TTF+gvar, OTF+CFF2), color (SVG, COLRv0/v1, CBDT, sbix), Type 1, WOFF2/WOFF/EOT, VFB/VFC/VFJ, UFO 2 & 3, designSpace, .glyphs v2 & 3, FontForge SFD, BDF, Fontographer FOG, Ikarus.
- **Workflow sections (the vendor's own arc)**: Explore & Prepare → Draft & Draw (Power Stroke/Power Brush calligraphic drawing, autotracing) → Edit & Refine (cubic PostScript + quadratic TrueType curves, Power Nudge, Lever precision) → Consistency & Precision (stem widths, curve tension, snapping, fractional/integer precision) → Build & Assemble (components, element references, skins, auto layers) → Metrics & Kerning (auto-space/auto-kern, RTL kerning, kerning audit) → Families & Variation (interpolate/extrapolate, variable fonts, Matchmaker compatibility) → Test & Adjust (Preview panel, waterfalls, HarfBuzz complex-script shaping preview, ClearType screen preview, FontAudit outline QA, action sets) → Color → Glyphs & Fonts → Formats → Scripts & Integrations (Python 3, TypeRig).
- **Audience/tier machinery**: education licensing (student/teacher/course/workshop), Starter (3-month) vs Pro (lifetime) tiers; "Thousands of designers and foundries large and small have been using the FontLab apps"; GetGo Fonts offered as "inspiration or templates for your own font".
- **Made-with claims**: fonts bundled with Windows and Apple systems designed in FontLab apps; Material Symbols (Google) as an icon-font example.

## Product C — RoboFont 4

### Key observations (evidence layer A — product page + documentation)

- **Self-label (alias evidence, the sharpest single sentence in this research)**: "The **font editor** for macOS." Followed immediately by: "A fully featured **font editor** with all the tools required for **drawing typefaces**." — the two names in apposition in one vendor sentence.
- **Philosophy**: "Written from scratch in Python with scalability in mind… Provides full scripting access to objects and interface. A platform for building your own tools and extensions." Community: "a vibrant community of **type designers** and software developers."
- **Technical specs**: UFO3 as native font format; Python 3.12 out of the box; macOS 10.12+.
- **Extension ecosystem** (the scripting-platform pole): MetricsMachine (kerning), Prepolator (interpolation preparation), GlyphConstruction, Outliner (stroke→outline), SpeedPunk (curve quality), GlyphNanny (outline QA), word-o-mat (test-word generation), Ramsay St (interpolated instances), OverlayUFOs, CornerTools, GlyphBrowser; Mechanic + Extension Store; "A rock-solid core application + dozens of specialized extensions."
- **Documentation taxonomy (the field's own workflow organization)**: Tutorials grouped as — Making fonts (making a font; simple font family; complex font family; designspace files/multiple UFOs; italic fonts; building accented glyphs) / Setting font info (font infos; family names) / Drawing & spacing (drawing glyphs; quadratic curves; checking contour quality; introduction to spacing; kerning) / Character set (defining character sets; sorting glyphs; friendly and final [production] names; mark colors; large fonts) / Font generation (generating fonts; installing test fonts; PostScript hinting; TrueType hinting) / Variable fonts (designspace files; creating variable fonts; testing variable fonts) / Building tools (Python; DrawBot proofs; Git; extensions).
- **Workspace surfaces** (reference structure): Font Overview (with Font Info sheet [General/OpenType/PostScript/WOFF], Add Glyphs sheet, Sort Glyphs, Smart Sets, Search Glyphs, Features Editor, Groups Editor, Kern Center), Glyph Editor (Bezier/Editing/Slice/Measurement tools; contours, components, anchors, guidelines, layers, images, display, transform), Inspector, Space Center, Scripting Window, Output Window, Extension Builder.
- **"Making a font" tutorial (the canonical craft walkthrough)**:
  - Setting up: File > New → empty Font Overview with greyed *template glyphs* → Font Info: family name + style name → Add Glyphs: paste a glyph-name list (ASCII set given) → template cells become empty glyphs → save (UFO).
  - Drawing and spacing: drawing in the Glyph Editor (double-click a glyph cell); **"Spacing and drawing are usually done together – the space inside the glyphs and the space between the glyphs are defined in relation to each other."** Spacing in the Space Center.
  - Previewing: "It is important to quickly preview actual text in the font while designing in order to evaluate the drawing and spacing in context." Test-text tradition named: pangrams; Emil Ruder's lists of 'problematic' and 'non problematic' words "well known among typeface designers"; Jonathan Hoefler's texts for proofing fonts; extensions word-o-mat / Adhesion Text / Random Word Generator; DrawBot for PDF proofs.
  - Testing: set font infos → generate the font (OTF) → install test fonts → proof (spacing, OpenType features).
  - Craft guidance: "start small, make sure that the basics work first… the larger the font, the more 'expensive' it becomes to make significant changes"; "minimum viable font" concept (a plain style with the basic ASCII set, ending in "an OpenType font which we can use to set some text in any app").

## Product D — Birdfont

### Key observations (evidence layer A — homepage + release notes)

- **Self-label (alias evidence)**: "Birdfont is a free **font editor** which lets you create vector graphics and export TTF, OTF and SVG fonts. The editor has good support for both monochrome and color font formats."
- **Surfaces** (from release notes): overview tab (glyph grid, Unicode block browsing/search, custom character sets, filtering), editing view (Bézier tools, freehand tool, stroke, background images, rulers, grid, guides incl. overshoot, filled-path display), kerning tab (kerning classes, spacing classes copying sidebearings/kerning between glyphs, word display, RTL), ligature tab (generation), font name tab (license, designer, URL, version metadata).
- **Capability breadth across releases**: variable fonts (variable TTF/OTF/SVG; multiple static exports from one variable master), color fonts (COLR/CPAL, OpenType-SVG, emoji, color ligatures), mark-to-base positioning, stylistic sets ss01–ss20, oldstyle figures, randomized glyphs (rand), SVG import/export (Illustrator/Inkscape/Vectornator), folder batch import, autotrace (incl. CLI utility), import/merge another font, guides, layers, spacing classes, anchor points for diacritics, CNC single-stroke export.
- **Model**: donation-supported free software; Vala codebase; community fonts gallery ("Discover fonts made with BirdFont").

## Sibling-pass cross-checks (from research/font-editor.md, 2026-09-07)

- **FontForge** (layer A, full docs): the vendor's own definition — "A font editor is a program designed to create and modify fonts… a drawing program… which lets you draw the outlines of your letters… expects you to draw many pictures at once (one or more for each letter) and collects them into a database… describe the way these pictures interact with each other (…the font's metrics… the font's ligatures…)… will bundle up all the pictures you have drawn, and all the metadata about how those pictures fit together, and will turn that bundle of stuff into a font that your computer can use to display text." Also documents bitmap-strike editing, stroked fonts, encoding/naming, metrics view, OpenType lookups, hinting, generation to many formats, Python scripting.
- **FontCreator** (layer A/B, product page): "The #1 font editor for Windows & macOS. Create, refine and export OpenType, TrueType and responsive variable fonts." WYSIWYG editing with real-time proofing; preserves OpenType layout features when modifying existing fonts; .glyphs/UFO/designspace interchange; optical metrics; validation; sibling products MainType (font manager) and Scanahand (font generator) as separate categories.

## Cross-product Comparison

| Structure | Glyphs | FontLab | RoboFont | Birdfont | FontForge* | FontCreator* | Evidence |
|---|---|---|---|---|---|---|---|
| Self-labels "font editor" | ✓ ("leading Mac font editor") | ✓ ("integrated font editor") | ✓ ("The font editor for macOS") | ✓ ("a free font editor") | ✓ (defines the Type) | ✓ ("The #1 font editor") | A (6/6) |
| Discipline language on same pages | "Create fonts/icons/lettering/logos/pictos"; foundry community | "professional typeface designers"; "Love type design" | "drawing typefaces"; "type designers" | (fonts gallery) | (letter outlines) | (create/refine fonts) | A |
| Persistent font project | ✓ (.glyphs/UFO) | ✓ (VFB/VFJ/UFO/…) | ✓ (UFO3 native) | ✓ (.birdfont) | ✓ (SFD + many) | ✓ (+ .glyphs/UFO/designspace) | B |
| Glyph set with character mapping | ✓ (glyph names, Unicode, glyph info DB*) | ✓ (naming/encoding, generate names/unicodes*) | ✓ (Add Glyphs by name list; friendly/production names; sorting) | ✓ (Unicode blocks, UCD search) | ✓ (encoding, Adobe naming) | ✓ (categories, subsets, Unicode ranges) | B |
| Font overview over all glyphs | ✓ (Font+Edit views) | ✓ (Font window) | ✓ (Font Overview w/ template cells) | ✓ (overview tab) | ✓ (font view) | ✓ (font overview) | B |
| Direct letterform drawing on font geometry | ✓ (pen points, star nodes, bézier control) | ✓ (cubic+quadratic, Power Nudge, measurement) | ✓ (Bezier/Editing tools, contour quality) | ✓ (Bézier + freehand) | ✓ (splines, point types) | ✓ (quadratic+cubic) | B |
| Drawing↔spacing interdependence | ✓ (Info Box metrics; spacing tutorials) | ✓ ("space and kern… feel like a text editor") | ✓ (explicit: "spacing and drawing are usually done together") | ✓ (spacing classes; sidebearings in edit view) | ✓ (metrics view) | ✓ (sidebearings, optical metrics*) | B |
| Kerning (pairs + classes/groups) | ✓ (visual kerning groups, contextual kerning) | ✓ (auto-kern, RTL kerning, audit) | ✓ (Kern Center, Groups Editor, MetricsMachine ext.) | ✓ (kerning tab, classes) | ✓ (metrics view kerning) | ✓ (pairs, classes, autokerning*) | B |
| Components/composites + anchors | ✓ (components, smart/corner/segment, head components) | ✓ (components, element references, skins) | ✓ (components, anchors; accented-glyph tutorial) | ✓ (anchor marks, ligature tab) | ✓ (references, build accented) | ✓ (composites, anchor manager*) | B |
| OpenType features | ✓ (auto+manual feature code, live syntax check) | ✓ (auto-generated features, FEA/AFDKO) | ✓ (Features Editor) | ✓ (GSUB/GPOS, stylistic sets) | ✓ (lookups/features) | ✓ (visual designer + fea compiler*) | B |
| Text testing/preview in context | ✓ (live text preview window) | ✓ (Preview panel, HarfBuzz shaping, waterfalls) | ✓ (Space Center text; pangrams/Ruder/Hoefler texts; test-install) | ✓ (kerning tab words; preview template) | ✓ (metrics view) | ✓ (proofing tool, external preview*) | B |
| Interpolation/masters/variable fonts | ✓ (MM 1–3 tutorials, master selector) | ✓ (families & variation, Matchmaker) | ✓ (designspace tutorials, Prepolator ext.) | ✓ (variable TTF/OTF/SVG) | (MM heritage*) | ✓ (axes, masters, layers) | B (5/6 direct this+sibling pass) |
| Contour quality/QA | ✓ (harmonize, balance) | ✓ (FontAudit) | ✓ (checking contour quality tutorial; GlyphNanny/SpeedPunk ext.) | (extrema tool) | (not surfaced*) | ✓ (validation wizard*) | B (4/6) |
| Vector/sketch import + autotrace | ✓ (Illustrator/Affinity/Sketch interchange*) | ✓ (PDF/EPS/SVG import, autotracing) | ✓ (background images; images in glyphs) | ✓ (SVG import, autotrace CLI) | ✓ (background images, autotrace) | ✓ (vector+raster import*) | B |
| Font info/metadata | ✓ (font info: family, UPM, axes*) | ✓ (font info dialog*) | ✓ (Font Info sheet: family/style name first step) | ✓ (font name tab) | ✓ (font info dialog*) | ✓ (naming fields*) | B |
| Generation to installable font files | ✓ (CFF/CFF2/TTF/WOFF/WOFF2 + images) | ✓ (batch export, many formats) | ✓ (generating fonts; trial fonts; test-install) | ✓ (TTF/OTF/SVG/EOT) | ✓ (TT/OTF/Type1/SVG/bitmaps*) | ✓ (OTF/TTF/WOFF/WOFF2*) | B |
| Hinting | ✓ (two chapters*) | ✓ (TT+PS hinting) | ✓ (PS+TT hinting tutorials) | (not surfaced) | ✓ (full docs*) | (not surfaced*) | B (4/6) |
| Scripting/automation | ✓ (Python 3 API, plug-ins, debug window) | ✓ (Python 3, TypeRig) | ✓ (Python-first platform, FontParts API, extensions) | ✓ (CLI utilities) | ✓ (Python*) | (not surfaced*) | B (5/6) |
| Color fonts | ✓ (COLRv0/v1, SVG, sbix, layered) | ✓ (SVG, COLRv0/v1, CBDT, sbix) | (via extensions) | ✓ (COLR/CPAL, OT-SVG, emoji) | (not in fetched overview*) | ✓ (COLR, SVG*) | B (5/6) |
| Education licensing | (community/tribe positioning) | ✓ (student/teacher/course/workshop SKUs) | ✓ (free teacher trials, student license service) | (free/donation) | (free) | (not surfaced*) | A (2/4 fresh) |

\* = sibling-pass evidence (research/font-editor.md, 2026-09-07).

## Canonical Model (four-level abstraction)

### L0 — Defining Invariant

Re-derived independently on this pass; structurally identical to the font-editor pass's L0 (as an alias requires), expressed in the craft vocabulary:

1. **The typeface as a persistent designed project** — a saved, re-editable container holding one typeface (or family) that the designer creates, names, and revisits over a long arc. Remove → one-off letter drawing, not typeface work.
2. **The glyph set with character mapping** — the typeface's content: a set of glyphs, each identified by name and/or mapped to character code points, navigable as a whole (the font overview). The mapped inventory is what makes the work typeface design rather than lettering illustration. Remove → a generic vector drawing tool.
3. **Direct letterform drawing on the font's own geometry** — the designer shapes each glyph directly (outline contours with points and curves, or bitmap cells in variant products) on a surface that carries the font's coordinate system (em size, baseline) and per-glyph font data (advance width/sidebearings). Remove → a font manager or converter, which handle fonts but do not let you draw.
4. **Generation of usable font files** — the project compiles/exports into font files in standard formats that other software installs and uses to render text; this is the release step that makes the design a typeface. Remove → a glyph illustration tool.

Supporting evidence: all four fresh products satisfy all four properties (comparison table); FontForge's vendor definition (sibling pass) names the same arc; RoboFont's "Making a font" tutorial walks exactly this arc as the field's own beginner path.

Historical/market-sample check: the definition does not depend on outline editing (bitmap-era type-design tools — Ikarus-class digitizing systems, bitmap font editors — satisfy all four via bitmap cells + font generation; FontForge still documents bitmap editing today). It does not depend on interpolation/variable fonts, OpenType features, kerning, hinting, color, scripting, or any platform/era/business model. Older and regional products fit.

### L1 — Common Mature Structure

Present across the sample; expected in mature products; not definitional:

- Outline drawing machinery (cubic and/or quadratic Bézier contours, node/point editing, path direction, transformations)
- Spacing and kerning as first-class design work (sidebearings, spacing classes/groups, kerning pairs + classes, dedicated surfaces: Space Center / kerning windows / metrics tables)
- Components/composites and anchors (systematic construction of accented and composite glyphs; edit-once-update-everywhere)
- OpenType features (ligatures, alternates, stylistic sets, substitution/positioning rules; feature-code editing)
- Text testing and proofing (in-app live text preview; test-text traditions — pangrams, problem-word lists; external/browser preview; test-font installation; PDF proofs)
- Contour quality tooling (harmonization, curvature visualization, outline audit/validation) — 4/6 observed
- Font info/metadata (family/style names, units per em, version, vertical metrics)
- Vector artwork import (SVG/Illustrator-class) and autotracing of sketches/scans
- Interpolation/multiple masters/variable fonts — modern-common (5/6 direct)
- Color fonts (COLR/CPAL, SVG, sbix) — modern-common (5/6)
- Hinting (PostScript/TrueType) — 4/6
- Per-glyph layers; glyph organization (sorting, smart sets, mark colors, production names)
- Scripting/automation (Python in the professional poles; CLI utilities in the free pole) — 5/6

### L2 — Variant / Optional Structure

- **Product philosophy poles**: streamlined all-in-one (Glyphs) vs engineering-depth (FontLab) vs code-centric scripting platform (RoboFont) vs free lightweight (Birdfont/FontForge) vs mid-tier accessible (FontCreator)
- **Audience tier**: professional foundry vs student/education (education SKUs at FontLab, RoboFont) vs consumer font-makers (template/handwriting generators, in-vector-app extensions — the generator edge)
- **Platform/delivery**: macOS-native, cross-platform desktop, open-source, web-based (Glyphr Studio class, referenced by Birdfont's SVG-font import)
- **Script posture**: closed app vs open scripting platform with extension ecosystems (RoboFont Mechanic/Extension Store; Glyphs plugin manager)
- **Script/style scope**: Latin-only vs multi-script (Arabic/Indic/CJK depth: contextual forms, mark stacking, vertical metrics); icon/symbol fonts; color fonts; monoline/brush-based lettering fonts
- **Interchange posture**: open formats (UFO/designspace) vs proprietary project formats; opening compiled fonts for editing
- **Output breadth**: font files only vs font files + image exports (PNG/SVG/PDF/SF Symbols) + icon fonts

### L3 — Vendor-specific Structure (research notes only)

- Glyphs: .glyphs package; glyph info database; pen points (variable strokes); star nodes; visual kerning shelf; head components; Slanter filter; master selector; SFSymbols export; Kern On/Speed Punk/Hellbox/Remix Tools/LTTR/INK community plug-ins; "Made in Glyphs" foundry directory.
- FontLab: Power Stroke/Power Brush; Power Nudge/Lever; Tunni lines*; Matchmaker; FontAudit; Delta filter; element references/skins; TypeRig; GetGo Fonts; Starter/Pro/Education SKU ladder; upgrade-discount list naming competitor editors.
- RoboFont: UFO3-native; FontParts/vanilla/mojo APIs; Mechanic + Extension Store; Smart Sets; Space Center; DrawBot proofing pipeline; education license service; documentation organized by the divio system (tutorials/how-tos/topics/reference).
- Birdfont: .birdfont format; Vala codebase; CNC single-stroke export; birdfont-import/export/autotrace CLI; donation-goal funding model.
- FontCreator*: optical metrics; transform wizard; "preserve full OpenType feature data" headline; MainType/Scanahand sibling products.
- FontForge*: SFD; Spiro mode; namelists; CID-keyed support; bitmap-strike recalculation.

## Vendor-specific Findings

- FontLab's upgrade page listing RoboFont and Glyphs under "another font editor" is single-vendor but doubly probative: it is the vendor's own market classification, and it matches every product's self-label.
- RoboFont's "A fully featured font editor with all the tools required for drawing typefaces" is the single sharpest alias datum: one vendor sentence equating the two names.
- Vendor numbers (FontLab's "700 reasons"/"500 improvements", FontCreator's "3000+ composites"*) are kept here, not in the final document.
- Test-text traditions (Ruder lists, Hoefler texts) are named by RoboFont's documentation as field knowledge, not product features — usable in the final document as craft context, attributed to the documentation that names them.

## Boundary Findings

1. **vs Font Editor (sibling leaf) — ALIAS CONFIRMED (this pass's joint-review outcome).** Evidence: (a) all four fresh products self-label as "font editor" — Glyphs ("the leading Mac font editor"), FontLab ("an integrated font editor"), RoboFont ("The font editor for macOS"), Birdfont ("a free font editor") — matching the sibling pass's 5/5 (FontForge, FontCreator, Birdfont, FontLab, Glyphs); (b) FontLab's own upgrade page classifies RoboFont and Glyphs as "another font editor", and its interchange copy names "other font editing apps like Glyphs, RoboFont, FontForge"; (c) RoboFont's one-sentence apposition ("a fully featured font editor with all the tools required for drawing typefaces") equates the names; (d) the discipline vocabulary ("type design", "typeface designers", "drawing typefaces") appears on the same pages as the "font editor" self-labels, describing the users and the practice, not a separate product category; (e) no product population was found — in either pass — that "designs typefaces" without being a font editor. Removal tests: from a type-design-framed product remove the craft emphasis → the same tool; from a font-editor-framed product add craft framing → the same tool; nothing structural remains to separate them. Conclusion: **one market family behind two directory names** — "Font Editor" names the tool (file/engineering lens), "Typeface Design Application" names the discipline the tool serves (craft/design lens). Per the digital-whiteboard ≡ collaborative-canvas precedent: both leaves stand with separate lens documents; the merge/canonical-name decision is escalated to directory-level review (DIRECTORY.md untouched).
2. **vs Vector Graphics Editor** — glyph artwork is vector geometry, but a vector editor has no mapped glyph set, no font geometry (em/baseline/metrics), and no font-file generation. Bidirectional seam: type-design tools import vector artwork (all sampled), and in-vector-app font makers (Fontself class) live on this seam — held as the consumer edge of this market, not a separate Type.
3. **vs Pixel Art Editor** — bitmap glyph editing exists inside the Type (FontForge bitmap view; historical bitmap-era tools). The discriminator is the font context (mapping + metrics + generation).
4. **vs Font Management Application** — managers organize/install/preview installed fonts; no glyph editing, no generation. Boundary evidence: High-Logic ships FontCreator (editor) and MainType (manager) as separate products (sibling pass).
5. **vs Font generator utilities** — template/handwriting-to-font products produce fonts with minimal per-glyph editing; the consumer edge of the market, adjacent rather than core.
6. **vs Font conversion utilities** — format conversion without artwork editing; overlap only where converters add editing.
7. **vs Lettering/illustration tools** — lettering draws words as artwork; type design builds a mapped, reusable, generating system of letterforms. Glyphs' own headline rotation ("Create fonts / icons / lettering / logos / pictos") shows one tool serving both poles — the lettering pole without the glyph-set/generation machinery is illustration territory.
8. **vs Publishing/Document applications** — those consume the generated fonts; no boundary risk, listed for completeness.

"去掉什么就变成另一个 Type" 判据:
- 去掉 glyph set/character mapping（只画单个字形艺术）→ Vector Graphics Editor / lettering illustration
- 去掉 direct letterform editing（只管理/转换/预览字体）→ Font Management / Font Conversion
- 去掉 font-file generation（只画字形）→ glyph illustration
- 去掉 persistent project（一次性模板生成）→ font generator utility

## Uncertainties

- FontLab behavioral detail rests on product-page + sibling-pass TOC-level evidence; no FontLab-specific behavioral rules asserted in the final document.
- Web-based editors (Glyphr Studio class) not directly researched; held as a delivery variant via Birdfont's import cross-reference.
- Historical tools (Ikarus, Fontographer, early bitmap-era editors) not directly fetched; the historical check is reasoned from FontForge's documented bitmap editing + the abstract definition + FontLab's own product-line history (Fontographer 5 and TypeTool 3 listed as upgradeable predecessors), not from fetched 1970s–80s sources.
- Whether the directory will merge the two leaves is a taxonomy-level decision outside this pass's authority; escalated, not decided.
- Color-font support in RoboFont core (vs via extensions) not pinned down; kept at "via extensions" strength from the extension-store listing.

## Final Synthesis

A Typeface Design Application is the application Type whose world is: **a persistent typeface project containing a mapped glyph set, each glyph drawn and edited directly as letterform artwork on the font's own geometry, the whole tuned as a designed system (spacing, kerning, components, features, interpolation), tested in real text, and compiled into installable font files.** The type-design workflow the field itself teaches runs: set up the font file → define the character set → draw → check contour quality → space → kern → build accented/composite glyphs → set font info → interpolate/extend the family → generate → test-install → proof.

The joint review is discharged: **Typeface Design Application ≡ Font Editor — one market family, two names, two lenses.** Every sampled product self-labels "font editor"; the discipline name describes the user and the practice. Both documents stand (this one from the craft lens, the sibling from the tool/file lens); the merge/canonical-name decision is escalated to directory review.
