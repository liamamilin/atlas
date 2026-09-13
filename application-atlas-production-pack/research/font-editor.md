# Research Notes — Font Editor

Research date: 2026-09-07
Leaf: Font Editor (DIRECTORY.md §04.18 Typography)
Slug: font-editor

## Research Goal

Understand what a Font Editor actually is as an Application Type: its core object model, its defining workflow (from empty project to generated font file), its main interfaces, its important rules and constraints, and its boundaries against neighboring Types (Vector Graphics Editor, Pixel Art Editor, font managers, font converters, and the sibling directory leaf "Typeface Design Application").

## Initial Boundary

Initial hypothesis before research:

- A font editor is software for creating and editing fonts (typefaces): the user draws glyph outlines, organizes them into a character set, sets metrics/kerning, and generates font files.
- Primary users: type designers, font foundries, hobbyists, icon designers.
- Nearest neighbors: Typeface Design Application (sibling leaf — suspected alias), Vector Graphics Editor (glyph artwork is vector), Pixel Art Editor (bitmap fonts), font management applications, font conversion utilities.
- Main unknowns: exact core object model across products; whether "font editor" and "typeface design application" are one market family or two; how much of the modern feature set (variable fonts, color fonts, OpenType features) is definitional vs common.

## Research Questions

1. What is the core object model? (project → glyph set → glyph → artwork → font-wide data → generated files)
2. What does the glyph editing surface look like, and what font-specific geometry does it carry?
3. How are glyphs organized, named, and mapped to characters?
4. What is the canonical workflow from empty project to generated font?
5. What inter-glyph behavior does the editor manage (metrics, kerning, features, anchors)?
6. What rules/constraints genuinely shape the work (path direction, outline compatibility, coordinate precision)?
7. Which capabilities are definitional vs common vs optional vs vendor-specific?
8. Where exactly are the boundaries: vs vector editors, pixel editors, font managers, converters, and the sibling leaf?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Evidence level |
|---|---|---|
| Glyphs (Glyphs GmbH, macOS) | professional foundry standard, streamlined macOS-native | A — full official Handbook (TOC + Create chapter fetched) |
| FontLab 8 (FontLab Ltd., cross-platform) | professional engineering-depth editor | A — official FontLab 7 manual TOC (v8 manual under revision; v7 manual is the official current resource per vendor) |
| FontForge (open source) | free/open-source, cross-platform, format-bridge heritage | A — official documentation overview (full text fetched) |
| FontCreator 16 (High-Logic, Windows/macOS) | mid-tier commercial, "accessible to all skill levels" | A/B — official product page (Tier 2); manual URL 404, manual link exists but not fetched |
| Birdfont (Johan Mattsson, free) | free lightweight editor, donation-supported | A/B — official homepage + release notes (official but shallow) |

Coverage check: two professional poles (streamlined vs engineering), one open-source pole, one mid-tier commercial pole, one free lightweight pole. Platforms: macOS-native, cross-platform, open-source cross-platform, Windows+macOS. No web-native editor sampled directly (Glyphr Studio referenced only in passing by Birdfont release notes).

## Sources

- Glyphs Handbook — https://handbook.glyphsapp.com/ and https://handbook.glyphsapp.com/create/ (fetched 2026-09-07)
- FontLab 8 manual index — https://help.fontlab.com/fontlab/8/manual/ ; FontLab 7 User Manual — https://help.fontlab.com/fontlab/7/manual/ (fetched 2026-09-07)
- FontForge Documentation — https://fontforge.org/docs/ (fetched 2026-09-07)
- FontCreator product page — https://www.high-logic.com/font-editor/fontcreator (fetched 2026-09-07); manual at https://www.high-logic.com/fontcreator/manual16/ (linked from product page; not fetched)
- Birdfont — https://birdfont.org/ (fetched 2026-09-07)

Source-access limitations:

- FontLab 8 manual is explicitly "under revision" per the vendor; the FontLab 7 manual is the vendor's recommended current resource. Observations are TOC-level (chapter/section structure), which is official but not full-text.
- FontCreator manual was not reachable at the guessed URL (404); evidence is product-page level. Feature claims kept at product-page strength.
- Birdfont evidence is homepage + release notes; no full manual fetched.
- No numeric limits, default values, or precise format-version facts are asserted anywhere in the final document; vendor-specific numbers stay here.

## Product A — Glyphs

### Key observations (evidence layer A unless noted)

- **Document model**: a Glyphs document is a saved file (.glyphs, .glyphs package, or UFO export) created from a Start Window; new documents are created "from glyph sets" — the user picks scripts (Latin, Greek, Cyrillic, etc.) and glyph subsets, and the app creates a document "containing empty glyphs for all selected scripts". The document is the persistent unit of work.
- **Font View**: grid view and list view over the font's glyphs; managing the glyph set (adding single/multiple glyphs, adding from a built-in glyph info database or sidebar, copying glyphs between files, deleting); glyph properties include name, metrics, kerning groups, exports (instance membership), Unicode, production name, script, category/subcategory, case, writing direction, sort name, components, last-changed; filtering (search, categories, languages, smart filters); glyph order management; batch processing and batch renaming.
- **Edit View (glyph editing)**: drawing paths (draw tool, pencil tool, primitives); editing paths (node selection, moving, converting node/segment types, "super-smooth" nodes, nodes in alignment zones, scaling/rotating, aligning, duplicating, deleting, opening/closing paths, knife cutting, re-segmenting, path direction control, extremes & inflections); strokes (stroke-to-outline); compositing/masking; anchors (add/edit/remove; mark-to-base, mark-to-mark, cursive attachment, ligature carets); guides (local/global, magnetic); Info Box (numeric metrics readout, horizontal and vertical layout); glyph display (zoom/pan, view options); background layer (reference images); entering text (text tool with glyph insertion, writing direction, text preview, sample strings); measuring (measurement tool, measurement guides/line); annotating; images in glyphs.
- **Palette**: dimensions (numeric), fit curve, layers (master layers, backup layers, special layers), transformations (origin, mirroring, scaling, rotating/slanting, aligning, boolean operations).
- **Font Info**: font-level properties (family name, units per em, version, creation date, axes, custom parameters); masters (managing masters, axes coordinates, metrics & alignment zones, stems, custom parameters); exports/instances (style name, weight & width, axes coordinates, style linking); features (feature code editing, automatic + manual feature code, stylistic sets, implicit features); other settings (grid spacing, font type).
- **Spacing & Kerning**: spacing via Info Box and shortcuts; metrics keys (formulas linking glyph metrics, e.g. derived widths); kerning (modes, Info Box, shortcuts, kerning groups, group exceptions, a dedicated kerning window for viewing/editing/maintaining kerning pairs, manual kerning code).
- **Reusing shapes**: components (building composites, turning paths into components, recipes, editing components, automatic alignment, locking, decomposing, nesting); smart components (parameterized); corner/cap/segment components; brushes; a pixel tool.
- **Interpolation**: axes, masters, instances (static and variable-font settings), outline compatibility checking and correction, intermediate layers, virtual masters, editing multiple masters in sync, variable font options (origin, axis locations/mappings), working with multiple fonts (families, compare fonts/family).
- **Filters**: extrude, hatch, offset curve, roughen, round corners, rounded font, transformations, add extremes, remove overlap.
- **Feature code**: extended OpenType feature editing (tokens, conditional feature code, variable GPOS).
- **Hinting**: full PostScript hinting chapter (standard stems, alignment zones, autohinting, manual stem/ghost hints) and full TrueType hinting chapter (zones, stems, glyph-level instructions: snap/stem/shift/interpolate/delta, preview).
- **Color fonts**: layered color fonts, COLR/CPAL, sbix, SVG color fonts; previewing and exporting.
- **Import & Export**: exporting font files (OpenType export with outline flavor and file-format options, variable fonts, UFO, metrics); source formats (.glyphs, .glyphs package, UFO); opening font files (TrueType import behaviors, importing multiple font files into one document, importing OpenType features and PostScript hints); importing font data (outlines, metrics, feature files); interchange with vector drawing applications (Adobe Illustrator, Affinity Designer, Sketch); file-format interoperability; projects (subsetting a document into a project and exporting it back).
- **Extensions**: plugin manager, scripts (run/create, scripts folder), plug-ins (install/create); Python-based.

## Product B — FontLab 7/8

### Key observations (evidence layer A at TOC level; vendor states v8 manual is under revision and points to v7 manual)

- **Basics concepts documented**: Font (font naming, font sizes and the coordinate system, variable fonts); Glyphs (about glyphs, glyph naming and encoding, layers and masters, curve types, segments, points, contours, elements, components, glyph metrics, measurement line, composite and auto glyphs, color glyphs, glyph positioning, kerning, mark attachment); Hinting; Files (font formats, color font formats, other file formats).
- **Working with a font**: creating a new font (with language support and glyph sets); opening an existing font; navigating a font (font window, fonts and font map panels, searching glyphs, sorting glyphs); saving a font; comparing fonts; printing.
- **Drawing and editing glyphs**: creating a new glyph (add glyphs, generate glyphs, generate names, generate unicodes); editing an existing glyph; drawing environment (glyph window, workspaces, outline appearance, previewing glyphs, guidelines, scope of editing, rounding coordinates); a Sketchboard (free scratch area); importing bitmaps and outlines with autotracing; layers (incl. mask layers); drawing freehand; geometric shapes; vector curves; point editing (add/select/move/delete, node types, smart nodes); contour editing (segment/contour selection, moving, duplicating, changing segment types, outline conversion, TrueType editing); elements (reusable referenced shapes; composite and auto glyphs; element references detection; element stickers); anchors and pins; transformations (free transform, geometric).
- **Drawing workflow aids**: Tunni lines (curve tension), find outline, glue selection, smart corners, power guides, unlink corners, parallel contour, expand contour, create/remove overlap, power brush (parametric stroke), rewind record, expressions.
- **Organizing glyphs**: glyph notes, flagging glyphs, glyph tags and classes.
- **Correcting drawings**: simplify, clean up, harmonize, balance, adding nodes to extremes, eraser, FontAudit (outline problem detection).
- **Italic**: creating an italic font, slanted grid.
- **Color**: making a font from color vector graphics, from color bitmap images, overlaying fonts.
- **Spacing and kerning**: editing glyph metrics, metrics table, editing kerning, kerning classes, importing/exporting metrics.
- **Extending fonts**: organizing font families, working with font variations (variable fonts).
- **Font production**: font info; embedding; hinting a font (TrueType hinting, PostScript hinting, automatic hinting); OpenType features (glyph substitution rules); exporting fonts (before-you-export checks, exporting options, export profiles, additional export features); Python scripting (scripts menu, scripting panel).
- **UI surfaces**: welcome dialog, preferences, font info dialog, font window, glyph window, metrics window, sketchboard, toolbar, property bar, rulers, grid, scoreboard, keyboard shortcuts; a large tool set (contour, element, metrics, kerning, text, eraser, brush, pencil, rapid, pen, knife, scissors, magnet, fill, guides, matchmaker, TrueType hinting, ellipse, rectangle); actions (basic, contour, metrics, effects, hinting); 30+ panels (anchors, brush, classes, color, elements, features, FontAudit, font info, font map, fonts, gallery, glyph, guideline, history, image, kerning, layers and masters, measurements, metrics, node, output, pairs and phrases, preview, scripting, source, stroke, swatches, tables, transform, variations, view).

## Product C — FontForge

### Key observations (evidence layer A — full documentation overview text)

- **The vendor's own definition of the Type** (quoted from "Er… What is a font editor?"):
  - "A font editor is a program designed to create and modify fonts."
  - "The most obvious aspect is that it is a drawing program like FreeHand, Inkscape or Illustrator which lets you draw the outlines of your letters. Unlike other drawing programs it expects you to draw many pictures at once (one or more for each letter) and collects them into a database."
  - "It allows you to describe the way these pictures interact with each other (if you put one picture after the other then they should normally be separated by a certain distance – the font's metrics, or if these two pictures are placed adjacent to one another then they turn into a third – the font's ligatures, and so on)."
  - "Finally a font editor will bundle up all the pictures you have drawn, and all the metadata about how those pictures fit together, and will turn that bundle of stuff into a font that your computer can use to display text."
- **Font concept**: "a font is a collection of glyphs" plus an encoding (mapping input bytes/characters to glyphs) plus rules for arranging glyphs (ligatures, kerning); character vs glyph distinction (one character may have many glyphs; a ligature is one glyph for several characters).
- **Glyph shape representations**: outline fonts (contours of Bézier splines — cubic for PostScript/CFF, quadratic for TrueType), bitmap fonts (pixel grids), stroked fonts (centerline + width, expandable to outlines). FontForge edits all three; bitmap strikes can be auto-recalculated from outlines and tweaked by hand.
- **Coordinate system**: per-glyph cartesian coordinates with origin on the baseline; em-size chosen at font creation (conventions like 1000/1024/2048 units per em are documented as conventions, not requirements); sidebearings (left/right), advance width, ascender/descender, x-height, cap-height; font-wide ascent/descent; CJK vertical metrics.
- **Outline editing**: outline glyph view with splines/points, point types (corner, tangent, curved), control points, path direction and winding rules (outer clockwise, inner counter-clockwise convention), background image for tracing, grid lines (baseline, ascent, descent), width line draggable to set advance width, tool palette and layer palette; Spiro clothoid spline editing mode (vendor-specific); layers (foreground/background, additional named layers, cubic vs quadratic layers per font, layer comparison/copying); guidelines as a shared mini-layer.
- **References (components)**: glyphs built by reference to other glyphs (e.g., accented glyphs); copy reference / paste / unlink; automatic accented-glyph building; caveat that references may be unlinked at export depending on format.
- **Font view**: displays all glyphs (label + small rasterization), double-click opens the outline glyph view, multi-select for batch operations; supports non-Latin fonts (Kanji example, CID-keyed fonts).
- **Bitmap view**: edit bitmap versions of outline glyphs; recalculate button auto-derives bits from the outline.
- **Metrics view**: see glyphs together in text; change width and bearings by dragging or numeric entry; enter kerning for adjacent pairs; view how OpenType features affect the glyph stream; right-to-left and vertical arrangement support.
- **OpenType machinery**: lookups, features, scripts, languages; GSUB (substitution) vs GPOS (positioning); ~15 lookup types documented; subtables with first-success semantics; anchor points (mark-to-base, mark-to-ligature, mark-to-mark, cursive entry/exit); baseline tables per script (Devanagari, CJK hanging baselines).
- **Hinting**: PostScript stem hints, flex hints, hint substitution, counter hints, BlueValues/StemSnap private-dictionary settings, autohinting; TrueType instructing derived from stem/diagonal hints; instructions preserved on re-generation provided no significant glyph change.
- **Glyph names**: Adobe glyph naming standard; namelists (remappable name conventions); production naming caveats.
- **Generation**: "generate fonts" to many formats — TrueType, OpenType (CFF), SVG, Type1, Type2, Type3, Apple AAT; bitmap generation; layer selection at generation time.
- **Scripting**: Python scripting documented as a first-class area.

## Product D — FontCreator (High-Logic)

### Key observations (evidence layer A/B — official product page; manual not fetched, so claims kept at product-page strength)

- Self-label: "The #1 font editor for Windows & macOS. Create, refine and export OpenType, TrueType and responsive variable fonts."
- **Editing existing fonts**: headline claim — modify an existing font while preserving its full OpenType layout feature data (every substitution, positioning rule, lookup flag, feature parameter).
- **Editing model**: WYSIWYG editing with real-time proofing and testing; upgraded shaping engine and interactive proofing tool; preview in external software or web browser.
- **Interchange**: supports .glyphs, UFO, and designspace formats for exchanging font projects with colleagues and other software.
- **Curves**: both quadratic (TTF) and cubic (CFF) curve editing; choose output format at export.
- **Glyph organization**: font overview with categories — glyph and character category panel, character subsets, Unicode ranges.
- **Formats**: OpenType, TrueType, WOFF, WOFF2.
- **Import**: vector graphics import (copy/paste with vector software); raster image import (scanned signatures, logos, handwriting → glyph outlines).
- **OpenType Layout Designer**: visual editing of lookups for substitutions and positioning; anchor manager for mark-to-base and mark-to-mark; bundled Adobe fea compiler.
- **Validation**: real-time font validation (outline and interpolation issues); font validation features to locate and solve common glyph problems; contour optimization (point reduction).
- **Variable fonts**: define axes, masters, and outline layers.
- **Color fonts**: scalable color fonts supporting COLR and SVG color extensions with backwards compatibility.
- **Kerning**: manual kern pairs (individual glyphs and glyph classes), autokerning.
- **Transform wizard**: add characters for other languages, small capitals, transform to italic/bold.
- **Optical metrics**: analyzes common characters to propose left/right sidebearings (vendor-specific).
- **Composites**: intelligent generation of accented composite characters (vendor claims 3000+; number kept here only), supporting composite data definitions and anchor-based positioning.
- **Ecosystem note**: the same vendor ships MainType (self-labeled font manager) and Scanahand (self-labeled font generator) as separate products — useful boundary evidence that font management and font generation-from-templates are distinct product categories from the font editor.

## Product E — Birdfont

### Key observations (evidence layer A/B — official homepage + release notes; shallow but official)

- Self-label: "a free font editor which lets you create vector graphics and export TTF, OTF and SVG fonts. The editor has good support for both monochrome and color font formats."
- **Surfaces** (from release notes): overview tab (glyph grid with Unicode block browsing/search, custom character sets, filtering glyphs), editing view (Bézier drawing tools, freehand tool, stroke, background images, rulers, grid, guides tab with overshoot guides, filled-path display while editing), kerning tab (kerning classes, spacing classes that copy sidebearings/kerning between glyphs, word display, RTL support), ligature tab (ligature generation), font name tab (metadata fields: license, designer, URL, version).
- **OpenType features**: ligature substitution (GSUB), mark-to-base positioning (GPOS), stylistic sets (ss01–ss20), stylistic alternates, small caps, oldstyle figures, randomized glyphs.
- **Variable fonts**: variable TTF/OTF/SVG, multiple static exports from one variable master.
- **Color fonts**: COLR/CPAL, OpenType-SVG, emoji support, color ligatures.
- **Import/export**: SVG import/export (Illustrator, Inkscape, Vectornator), folder batch import of SVGs, import/merge another font, export selected glyphs as SVG, autotrace (raster → vector, incl. command-line utility), TTF/OTF/SVG/EOT export.
- **Misc**: .birdfont native format; automatic backups; command-line utilities (birdfont-import, birdfont-export, birdfont-autotrace); CNC single-stroke font export (vendor-specific); can import SVG fonts from web-based editor Glyphr Studio (passing reference confirming the web-editor variant exists).

## Cross-product Comparison

| Structure | Glyphs | FontLab | FontForge | FontCreator | Birdfont | Evidence |
|---|---|---|---|---|---|---|
| Persistent font project/document | ✓ (.glyphs/.glyphs package/UFO) | ✓ (save font; proprietary + interchange formats) | ✓ (native SFD + opens/saves many formats) | ✓ (opens/saves; .glyphs/UFO/designspace interchange) | ✓ (.birdfont) | B |
| Glyph set with character mapping (names, Unicode, encoding) | ✓ (glyph info database, naming rules, Unicode, CID) | ✓ (glyph naming and encoding, generate names/unicodes) | ✓ (encoding, Adobe naming standard, namelists) | ✓ (categories, subsets, Unicode ranges) | ✓ (Unicode blocks, UCD search) | B |
| Font view over all glyphs (grid/list) | ✓ (grid + list views) | ✓ (font window, font map panels) | ✓ (font view) | ✓ (font overview) | ✓ (overview tab) | B |
| Direct outline editing (Bézier nodes/contours) | ✓ (draw/edit paths, node types, direction) | ✓ (points/contours, curve types, TrueType editing) | ✓ (splines, point types, direction/winding) | ✓ (quadratic + cubic) | ✓ (Bézier + freehand) | B |
| Font-specific coordinate surface (em, baseline, metrics lines) | ✓ (units per em, metrics & alignment zones, Info Box) | ✓ (coordinate system, glyph metrics, measurement line) | ✓ (em units, baseline origin, sidebearings) | ✓ (metrics, optical metrics) | ✓ (baseline tools, sidebearings) | B |
| Metrics/spacing editing | ✓ (Info Box, metrics keys) | ✓ (metrics table, metrics window) | ✓ (metrics view, width line) | ✓ (sidebearings, optical metrics) | ✓ (spacing tab/classes) | B |
| Kerning (pairs + classes/groups) | ✓ (kerning window, groups, exceptions) | ✓ (kerning editing, kerning classes) | ✓ (metrics view kerning, lookups) | ✓ (pairs, classes, autokerning) | ✓ (kerning tab, classes) | B |
| Components/composites/references for accented glyphs | ✓ (components, smart/corner/cap/segment) | ✓ (components, elements, composite/auto glyphs) | ✓ (references, build accented glyphs) | ✓ (complete composites, anchors) | ✓ (ligature/diacritic machinery) | B |
| Anchors / mark positioning | ✓ (mark-to-base, mark-to-mark, cursive) | ✓ (anchors and pins, mark attachment) | ✓ (anchor points, 4 attachment styles) | ✓ (anchor manager) | ✓ (mark classes) | B |
| OpenType features (GSUB/GPOS) editing | ✓ (feature code, automatic + manual) | ✓ (features panel, substitution rules) | ✓ (lookups/features/scripts/languages) | ✓ (visual designer + fea compiler) | ✓ (ligature/stylistic sets) | B |
| Text preview / testing in context | ✓ (text tool, sample strings, external previews) | ✓ (preview panel, pairs and phrases) | ✓ (metrics view) | ✓ (proofing tool, external/browser preview) | ✓ (preview template, kerning tab words) | B |
| Font info/metadata | ✓ (font info: family, UPM, version, axes) | ✓ (font info dialog) | ✓ (font info dialog) | ✓ (font naming fields) | ✓ (font name tab) | B |
| Generation/export to standard font files | ✓ (OTF/TTF/variable/UFO) | ✓ (export profiles) | ✓ (TT/OTF/Type1/SVG/bitmaps) | ✓ (OTF/TTF/WOFF/WOFF2) | ✓ (TTF/OTF/SVG) | B |
| Vector artwork import (SVG/Illustrator-class) | ✓ (Illustrator/Affinity/Sketch interchange) | ✓ (import artwork, autotracing) | ✓ (background images, autotrace) | ✓ (SVG import, clipboard) | ✓ (SVG import, folder import) | B |
| Autotracing bitmaps → outlines | ✓ (background images; pixel tool adjacent) | ✓ (autotracing chapter) | ✓ (autotrace background) | ✓ (raster import → outlines) | ✓ (autotrace + CLI) | B |
| Hinting (PS/TT) | ✓ (two full chapters) | ✓ (hinting chapters, hinting tool/actions) | ✓ (full hinting docs) | (not surfaced on product page) | (not surfaced) | B (3/5 observed) |
| Layers per glyph | ✓ (master/backup/special layers) | ✓ (layers and masters, mask layers) | ✓ (foreground/background + named layers) | (outline layers for VF) | ✓ (layers) | B |
| Multiple masters / interpolation / variable fonts | ✓ (full interpolation system) | ✓ (variations, variable fonts) | (not in fetched overview; MM heritage) | ✓ (axes, masters, layers) | ✓ (variable TTF/OTF/SVG) | B (4/5 observed directly) |
| Color fonts | ✓ (COLR/sbix/SVG/layered) | ✓ (color glyphs, color font formats) | (not in fetched overview) | ✓ (COLR, SVG) | ✓ (COLR, OT-SVG, emoji) | B (4/5 observed) |
| Bitmap glyph editing | (pixel tool adjacent) | (bitmap import/effects) | ✓ (bitmap view, bitmap strikes) | (raster import only) | (not surfaced) | A (FontForge only, full) — treat bitmap editing as variant |
| Validation / outline QA | (filters + third-party plugins) | ✓ (FontAudit) | (not surfaced) | ✓ (validation wizard, optimize contours) | (not surfaced) | B (2/5) — common-not-core |
| Scripting/automation | ✓ (Python scripts/plugins) | ✓ (Python) | ✓ (Python) | (not surfaced) | ✓ (CLI utilities) | B (4/5) |
| Interpolation compatibility checking | ✓ | (harmonize/balance aids) | (not surfaced) | ✓ (interpolation validation) | (not surfaced) | B (2/5 direct) |

## Canonical Model (four-level abstraction)

### L0 — Defining Invariant

The smallest structure without which the application stops being a font editor:

1. **The font project** — a persistent, editable container holding one typeface (or font family) as a structured document that the user creates, opens, saves, and revisits over time. Remove → one-off glyph drawing, not font work.
2. **The glyph set with character mapping** — the project holds a set of glyphs, each identified by a name and/or mapped to character code points, navigable as a collection (a font view over the whole set). Remove → a generic vector drawing tool.
3. **Direct editing of glyph artwork on a font-specific surface** — the user edits each glyph's shape directly (outline contours with points and curves, or bitmap cells) on a canvas that carries the font's own geometry: an em-based coordinate system with a baseline, and per-glyph font data such as advance width. Remove → a font manager or converter (which handle fonts but do not let you draw glyphs).
4. **Generation of usable font files** — the project compiles/exports into font files in standard formats (TrueType, OpenType, web fonts, etc.) that other software can install and use to render text. Remove → a glyph illustration tool.

Supporting evidence: FontForge's own definition of the Type names exactly this arc (drawing program that draws many pictures at once into a database → describes how pictures interact → bundles everything into a font the computer can use). All five sampled products satisfy all four properties.

Historical/market-sample check (§24 reasoning): the definition does not depend on outline editing specifically — a bitmap-era font editor (bitmap glyph cells + font resource generation) satisfies all four properties; FontForge still documents bitmap-strike editing and generation today, showing bitmap editing inside the Type's scope. The definition does not depend on OpenType features, variable fonts, color, hinting, or kerning — none of these are required to recognize the Type. The definition does not depend on any platform, business model, or era.

### L1 — Common Mature Structure

Present across the sampled products; expected in mature products but not definitional:

- Outline editing machinery: Bézier contours (cubic and/or quadratic), node/point manipulation, path direction control, boolean operations, transformations, filters/actions
- Metrics and spacing: advance width, sidebearings, baseline/alignment zones, spacing tools and metric linking
- Kerning: pair kerning plus kerning classes/groups, with a dedicated editing surface
- Components/composites: accented and composite glyphs built by reference to base glyphs and marks, positioned via anchors
- Anchors and mark positioning (mark-to-base, mark-to-mark, cursive attachment)
- OpenType features: ligatures, alternates, stylistic sets, substitution and positioning rules (GSUB/GPOS), feature-code editing
- Text preview/testing: rendering sample strings with the in-progress font, including external/browser preview
- Font info/metadata: family and style names, units per em, version, ascent/descent
- Font view organization: grid/list of glyphs, glyph naming conventions, Unicode mapping, categories/scripts/languages, search/filter, glyph order
- Vector artwork import (SVG/Illustrator-class) and autotracing of bitmap artwork
- Hinting (PostScript and/or TrueType, with autohinting) — observed in 3/5 sampled products
- Per-glyph layers (foreground/background, master layers)
- Validation/outline QA tooling — observed in 2/5 (common-not-universal)
- Scripting/automation (Python in three products; CLI utilities in one)

### L2 — Variant / Optional Structure

- **Interpolation / multiple masters / variable fonts** — full design-space systems in professional products; absent or recent in lighter products. Modern-common, not definitional.
- **Color fonts** (COLR/CPAL, SVG, sbix, emoji) — modern optional capability.
- **Bitmap glyph editing** (bitmap strikes alongside outlines) — FontForge-only in the sample at full depth; historically bitmap-first editors existed; today mostly outline-first.
- **Stroke-based drawing** (draw centerline strokes, expand to outlines) — present in several products as an alternative authoring mode.
- **Audience tier**: professional foundry tools vs mid-tier "accessible" editors vs free/open-source vs consumer font-makers (extension-based or template-based generators live at this edge).
- **Platform/delivery**: macOS-native, cross-platform desktop, open-source, web-based editors (referenced via Glyphr Studio import in one sample).
- **Icon/symbol font workflows** — fonts as delivery vehicles for symbols/emoji.
- **Complex-script depth** (Arabic/Indic/CJK: contextual forms, mark stacking, vertical metrics, script-specific baselines).
- **Interchange posture**: open formats (UFO/designspace) vs proprietary project formats; opening existing compiled fonts for editing.

### L3 — Vendor-specific Structure (research notes only)

- Glyphs: .glyphs package format; glyph info database; smart/corner/cap/segment components; pixel tool; custom parameters; projects (sub-documents); plugin manager; metrics keys formula language.
- FontLab: elements/element references/stickers; Tunni lines; Power Brush; Power Guides; Smart Corners; Matchmaker tool; Scoreboard; FontAudit; Sketchboard; export profiles; workspaces.
- FontCreator: optical metrics (auto sidebearing proposal); transform wizard; validation wizard; visual OpenType designer with bundled Adobe fea compiler; autokerning; "preserve full OpenType feature data when modifying existing fonts" headline claim; MainType/Scanahand sibling products.
- FontForge: SFD format; Spiro clothoid spline mode; namelists; CID-keyed font support; Type3 multi-layer (per-glyph operation layers) editing; stroked-font editing; Apple AAT awareness; bitmap-strike recalculation.
- Birdfont: .birdfont format; CNC single-stroke export; command-line utilities (birdfont-import/export/autotrace); donation-supported development model.

## Vendor-specific Findings

See L3 above. Additionally:

- FontCreator's "modify an existing font and preserve its full OpenType layout feature data" is a single-product headline claim (evidence A, product page). FontForge documents a related but weaker behavior (TrueType instructions preserved "provided no significant change has happened"). Cross-product generalization kept moderate in the final document.
- FontCreator's "3000+ composite characters" and FontLab's tool/panel counts are vendor numbers — kept out of the final document.
- FontForge's em-size conventions (1000/1024/2048) are documented as conventions, not requirements — final document says only "a font-wide em size chosen at font creation".

## Boundary Findings

1. **vs Typeface Design Application (sibling leaf)** — probable alias. Evidence: every sampled product self-labels as a "font editor" (FontForge: "A font editor is a program designed to create and modify fonts"; FontCreator: "The #1 font editor"; Birdfont: "a free font editor"; FontLab's own URL slug is /font-editor/fontlab/). The craft-oriented name "typeface design application" describes the same product population from the user's discipline angle (Glyphs is positioned around typeface design, and is the same category of tool). No product population was found that "designs typefaces" without being a font editor. Recommendation: joint review when the sibling leaf is processed; likely merge/canonical-name decision.
2. **vs Vector Graphics Editor** — glyph artwork is vector geometry, but a vector editor has no font project, no glyph set with character mapping, no metrics/em geometry, and no font-file generation. The seam is real and bidirectional: font editors import vector artwork (all five sampled products), and at least one product family (extension-based font makers inside vector apps) lives exactly on this seam — treated as a variant pole of the font-editor market, not a separate Type.
3. **vs Pixel Art Editor** — bitmap glyph editing exists inside the Type (FontForge bitmap view; historical bitmap-first editors). The discriminator is the font context: mapping + metrics + generation. A pixel editor without those is not a font editor.
4. **vs Font Management Application** — font managers organize/install/preview installed fonts but do not edit glyphs or generate fonts. Boundary evidence: High-Logic ships FontCreator (editor) and MainType (manager) as separate products with separate manuals.
5. **vs Font generator utilities** — template-based generators (e.g., handwriting-to-font) produce fonts with minimal per-glyph editing; they are a capability slice at the consumer edge, adjacent rather than core.
6. **vs Font conversion utilities** — convert between font formats without artwork editing; overlap only where converters add editing (then they are editing-capable font tools).
7. **vs Document/Publishing applications** — those applications consume fonts; the font editor produces them. No boundary risk, listed for completeness.

"去掉什么就变成另一个 Type" 判据:
- 去掉 glyph set/character mapping（只画单个图形）→ Vector Graphics Editor
- 去掉 direct artwork editing（只管理/转换字体）→ Font Management / Font Conversion
- 去掉 font-file generation（只画 glyph 图形）→ glyph illustration / vector drawing
- 去掉 font project 容器（一次性生成，无持久工程）→ font generator utility

## Uncertainties

- FontLab observations are TOC-level; chapter content not verified beyond structure. No FontLab-specific behavioral claims made in the final document.
- FontCreator evidence is product-page level; manual not fetched. Claims kept at feature-description strength; no behavioral rules asserted from it.
- Birdfont documentation is shallow; used to confirm the free/lightweight pole and the breadth of the common structure, not for precise behavior.
- Web-based font editors (Glyphr Studio class) not directly researched; mentioned only as a delivery variant with a passing cross-reference from Birdfont's release notes.
- Historical bitmap-era font editors not directly researched (no reachable official documentation); the historical check is reasoned from FontForge's documented bitmap editing + the abstract definition, not from fetched 1980s sources.
- Whether the directory intends "Typeface Design Application" as a distinct Type could not be resolved from market evidence; flagged for joint review.

## Final Synthesis

A Font Editor is the application Type whose world is: **a persistent font project containing a mapped glyph set, each glyph directly editable as artwork on a font-geometry surface, the whole compiled into installable font files.** Around this defining core, mature products add a stable set of structures — metrics/spacing, kerning, components, anchors, OpenType features, text testing, font metadata, vector import/autotrace, hinting, layers — and a variant space spanning interpolation/variable fonts, color fonts, bitmap editing, audience tiers, platforms, and scripting depth. The Type's own vendor-community definition (FontForge's documentation) matches this abstraction almost verbatim, which is strong evidence that the abstraction is the market's own self-understanding, not an imposed schema.

The sibling leaf "Typeface Design Application" almost certainly denotes the same market family under a craft-oriented name; flagged in Boundary Issues for joint review.
