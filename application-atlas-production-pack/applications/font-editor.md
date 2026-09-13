# Font Editor

## Overview

A **Font Editor** is an application for creating and modifying fonts: it holds a typeface as a persistent project of glyphs, lets the user draw and edit each glyph's artwork directly on a surface that carries the font's own geometry, and generates font files that other software can install and use to render text.

The defining structure is small:

```text
Font project
└── Glyph set (glyphs mapped to characters)
    └── Glyph artwork, edited directly on a font-geometry surface
        └── compiled into
            └── installable font files
```

Everything else commonly associated with font tools — kerning, OpenType features, hinting, variable fonts, color glyphs — is widespread in current products but is not what makes the application a font editor. A tool that only manages installed fonts, only converts font formats, or only draws letter shapes without a font project around them is a different kind of application.

## Users & Context

The primary user is a **type designer** — someone who designs letterforms as a craft. This spans a wide range:

- professional type designers and font foundries building multi-weight, multi-script retail typefaces
- independent designers publishing fonts through marketplaces or their own channels
- graphic designers and brand designers making a custom typeface, wordmark font, or a font from a client's handwriting
- icon and symbol designers assembling icon fonts or emoji-style sets
- hobbyists and students learning type design

Secondary users include localization and script engineers who extend existing fonts to new languages or scripts, and technical font producers who prepare and validate font files for release.

The work context is a long-running desktop craft: a font project is typically opened, edited, and saved across weeks or months, with precision pointer (or stylus) work on glyph outlines as the daily activity. The application is usually a single-user desktop tool; collaboration happens by exchanging project files rather than by live co-editing.

## Core Model

The application's world consists of one central container — the font project — holding a set of glyphs, each carrying artwork and font-specific data, plus font-wide structures that govern how glyphs behave together, and ending in generated font files.

### The defining core

- **Font project** — the persistent, editable container for one typeface (or font family). It is a structured document the user creates, names, saves, and revisits. Everything else in the application lives inside it. A project typically starts from a glyph-set template (a chosen script or character range, pre-populated with empty glyph slots) or from an existing font file opened for editing.

- **Glyph set** — the font's content: the collection of glyphs the typeface contains. Each glyph is identified by a name and/or mapped to character code points, and the set is navigable as a whole through a font view (a grid or list showing every glyph in the font). The glyph set is what distinguishes a font project from a folder of letter drawings: it is a mapped, organized character inventory, not a pile of artwork.

- **Glyph** — the unit of design work. A glyph carries:
  - its **artwork** — the shape, drawn as outline contours (Bézier curves with editable points) or, in some products, as bitmap cells;
  - its **font-specific data** — above all the advance width (how far the pen advances after the glyph) and sidebearings, positioned in the font's own coordinate system.

- **Font-geometry editing surface** — glyph artwork is not drawn on a free canvas but on a surface structured by the font's geometry: an em-based coordinate system (a font-wide unit size chosen when the font is created), a baseline at a fixed vertical origin, and reference lines for heights (cap height, x-height, ascender, descender). This geometry is what makes glyph editing different from ordinary vector drawing: every shape is drawn relative to the same baseline and measured in the same em units.

- **Generated font files** — the project's output. The editor compiles the glyph set, its artwork, and the font-wide data into font files in standard formats (TrueType and OpenType are the common families, with web font formats also common) that operating systems, browsers, and design applications can install and use to set text. The generated file — not the project file — is the deliverable that ships to users.

### Structures mature products add

These are standard capabilities of mature font editors. They are not required to recognize the Type, but a modern product without them would feel incomplete:

- **Metrics and spacing** — tools for setting each glyph's advance width and sidebearings, and for controlling the rhythm of text (spacing between letters), often with numeric entry, on-canvas dragging, and ways to link or copy metrics across related glyphs.
- **Kerning** — adjustments to the space between specific pairs of glyphs, organized as pairs and as kerning classes/groups (many glyphs sharing one adjustment), edited in a dedicated kerning surface that shows the pair in context.
- **Components and composites** — accented and composite glyphs (À, É, and hundreds like them) built by reference to base glyphs and accent marks rather than redrawn; editing the base glyph updates every composite that references it. Anchors mark where marks attach to bases.
- **OpenType features** — rules that change which glyphs are used and how they are positioned in running text: ligatures, alternates, stylistic sets, small caps, contextual substitutions, mark positioning. Mature products expose these as editable rule sets (often in a feature-code language) alongside the artwork.
- **Text testing** — a preview surface that renders sample strings with the in-progress font, so the designer can judge letters in context, not just in isolation; external previews (in browsers or design applications) are common.
- **Font info** — font-wide metadata: family and style names, version, ascent/descent, and similar identity data that ends up inside the generated font file.
- **Vector import and autotracing** — bringing in artwork from vector drawing applications (SVG and Illustrator-class interchange) and converting scanned or bitmap images into editable outlines.
- **Hinting** — extra instructions added to glyphs so they render sharply at small sizes (separate PostScript and TrueType mechanisms in the font formats). Present in professional products; not surfaced in all.
- **Per-glyph layers** — multiple drawing layers per glyph (working layer, reference/background layer for tracing images or other glyphs, master layers for interpolation).
- **Quality checks** — outline validation (finding self-intersections, wrong path directions, stray points) and contour optimization.

### One structure, many implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Glyph artwork
Forms:     outline contours (cubic or quadratic Bézier), bitmap cells,
           stroke centerlines expanded to outlines

Concept:   Character mapping
Forms:     Unicode code points, glyph names following naming conventions,
           legacy encodings for older formats

Concept:   Project file
Forms:     proprietary project formats, open interchange formats
           (UFO / designspace), or opening compiled font files directly
```

## How It Works

The canonical workflow runs from an empty project to a shipped font file:

### 1. Start the project

```text
Create a new font project
→ choose the glyph set (script / character range template)
→ or open an existing font file to modify it
→ set font-wide basics (family name, em size, reference heights)
```

### 2. Draw and edit glyphs

```text
Open a glyph from the font view
→ draw outlines (Bézier pen, primitives, freehand, or traced artwork)
→ adjust points, curves, and path direction
→ build accented/composite glyphs from components
→ repeat across the glyph set
```

This is the daily loop of the application. Reference material (scanned lettering, imported vectors, other glyphs) is commonly placed on a background layer and traced. Outline quality is actively maintained: consistent curves, correct path directions, clean joins.

### 3. Space and kern

```text
Set each glyph's advance width and sidebearings
→ test letters in strings
→ adjust spacing until the rhythm is even
→ add kerning pairs / classes for combinations that need it
```

Spacing is typically done while looking at the glyph in text context, not in isolation.

### 4. Add behavior

```text
Define OpenType features (ligatures, alternates, substitutions, positioning)
→ place anchors for mark attachment
→ test the features on sample text
```

### 5. Test in context

```text
Type sample strings and see them rendered with the in-progress font
→ preview in external applications or a browser
→ iterate
```

### 6. Manage the family (professional products)

```text
Define masters (e.g., a light and a bold design)
→ interpolate intermediate weights or a variable font
→ check outline compatibility across masters
→ define the instances/styles to export
```

This tier is standard in professional products and absent or limited in lighter ones.

### 7. Generate and check

```text
Run validation / outline checks
→ export font files in the target formats
→ install or distribute the generated files
```

The generated file is a snapshot: the project remains the living source, and regeneration is the normal way to ship updates.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Font view (glyph grid)

The project's home surface.

- shows every glyph in the set as a grid or list, with names and character mappings
- surfaces work state (which glyphs are drawn, flagged, or empty)
- primary actions: open a glyph for editing, add/remove glyphs, filter/search, batch operations across selected glyphs

### Glyph edit view (outline canvas)

The core editing surface.

- the glyph's contours and points on the font-geometry canvas (baseline, height lines, em grid)
- background layer for tracing references; measurement and annotation tools
- primary actions: draw and edit contours, move/scale/rotate, set the advance width, edit components and anchors

### Metrics / spacing view

- glyphs shown in text context with their sidebearings visible
- primary actions: adjust advance width and sidebearings (drag or numeric), compare spacing across strings

### Kerning view

- a pair (or string) shown with the kerning value applied
- primary actions: create/edit kerning pairs, manage kerning classes, step through pairs

### Features editor

- the font's OpenType feature rules, usually as editable code with preview
- primary actions: write/edit feature rules, define glyph classes, test features on sample text

### Font info

- font-wide identity and geometry: family/style names, em size, heights, version
- primary actions: edit metadata, manage masters/instances (where supported)

### Preview / test surface

- sample text rendered with the in-progress font, including feature behavior
- primary actions: enter test strings, switch styles/masters, export previews

### Bitmap view (where supported)

- pixel-grid editing of bitmap versions of glyphs, alongside outline editing

## Important Rules / Behaviors

- **Glyphs live in the font's coordinate system.** All artwork is positioned relative to the baseline and measured in em units; the advance width is part of the glyph's data, not an afterthought. Moving a glyph's drawing does not move its metrics.
- **Path direction matters.** Outline fonts use winding rules: outer contours and inner contours (counters) must run in correct, opposite directions or the shape renders wrong. Editors surface and can fix direction as a first-class operation.
- **The glyph set is the unit of completeness.** A font is judged by its coverage: which characters it maps. Adding a glyph means adding it to the set with a proper name/mapping — drawing alone does not put a character in the font.
- **Components stay linked.** A composite glyph references its base glyphs; editing the base updates the composites. Decomposing (flattening) a composite is an explicit, usually irreversible step.
- **Outline compatibility governs interpolation.** Where multiple masters/variable fonts are used, corresponding glyphs must have matching point structures across masters; editors detect and help repair incompatibilities.
- **Coordinate precision is constrained by the target format.** Some font formats require integer coordinates; editors round or manage precision when generating, which can subtly alter shapes.
- **Editing an existing font is a supported path.** Opening a compiled font file for modification is a normal workflow; products differ in how completely they preserve the font's existing feature data through edits (at least one product makes round-trip feature preservation a headline capability; others document partial preservation).
- **The project is the source; the font file is the artifact.** Regeneration after edits is the normal release loop; the generated file is not expected to be re-edited as a project without importing it back.

## Variants

- **Professional foundry tools** — deep interpolation/variable-font systems, full hinting, scripting, multi-script support; aimed at type design as a profession.
- **Mid-tier accessible editors** — the same core model with a gentler interface and guided tools (autokerning, transform wizards, optical metrics); aimed at designers and serious hobbyists.
- **Free / open-source editors** — the full core model, often with strong format-bridge and scripting capabilities; documentation and polish vary.
- **Lightweight / consumer font-makers** — simplified editors or vector-application extensions that turn existing artwork into fonts with minimal per-glyph engineering; the core model is present but shallow.
- **Outline-first vs bitmap-capable** — most current products are outline-first; bitmap glyph editing survives as a secondary mode in some products, and historically bitmap-first editors existed.
- **Platform spread** — macOS-native, cross-platform desktop, open-source, and web-based editors.
- **Variable-font and color-font depth** — from none (static fonts only) to full design-space and color-glyph (COLR/SVG-class) support.
- **Icon/symbol font workflows** — fonts used as delivery vehicles for icons and symbols rather than text.
- **Complex-script specialization** — editors or configurations tuned for Arabic, Indic, CJK, or other scripts with contextual forms, mark stacking, and script-specific baselines.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Typeface Design Application | sibling / probable same family | the craft-oriented name for the same product population; the market overwhelmingly self-labels these tools "font editors" — flagged for joint review |
| Vector Graphics Editor | adjacent | draws vector shapes but has no font project, glyph set, character mapping, metrics, or font-file generation; font editors import vector artwork across this seam |
| Pixel Art Editor | adjacent | bitmap art without font mapping, metrics, or generation; bitmap glyph editing inside a font editor is a mode, not this Type |
| Font Management Application | adjacent | organizes, previews, and activates installed fonts; no glyph editing and no generation (the same vendor can ship both as separate products) |
| Font conversion utilities | adjacent | convert font formats without artwork editing |
| Font generator utilities | adjacent | produce fonts from templates (e.g., handwriting) with minimal per-glyph editing; a consumer-edge capability slice |
| Icon design tools | adjacent | create icon artwork; may export icon fonts, but glyph-level font engineering is minimal |
| Desktop Publishing / Document Editors | downstream | consume the generated fonts; never produce them |

The most important boundary is with the **Vector Graphics Editor**: glyph artwork is vector geometry, so the two share drawing techniques — but the font editor's world (project, mapped glyph set, em geometry, metrics, generation) is entirely absent from a vector editor, and that world is the Type.

## Representative Products

- **Glyphs** — macOS-native professional editor; streamlined workflow around a document-per-typeface model
- **FontLab** — cross-platform professional editor with engineering-depth tooling
- **FontForge** — free open-source editor with broad format support and scripting
- **FontCreator** — commercial editor for Windows and macOS positioned as accessible to all skill levels
- **Birdfont** — free lightweight editor supporting monochrome and color font formats

The defining core was checked against this spread of philosophies and tiers (professional streamlined, professional engineering, open-source, mid-tier commercial, free lightweight) rather than against a single market segment.

## Sources

Research date: **2026-09-07**

- Glyphs Handbook — https://handbook.glyphsapp.com/ (incl. the "Create" chapter)
- FontLab 8 manual index (under revision per vendor) and FontLab 7 User Manual — https://help.fontlab.com/fontlab/8/manual/ , https://help.fontlab.com/fontlab/7/manual/
- FontForge Documentation — https://fontforge.org/docs/
- FontCreator product page — https://www.high-logic.com/font-editor/fontcreator
- Birdfont — https://birdfont.org/

> Sourcing limitations: FontLab observations are based on the official manual's structure (the vendor states the version-8 manual is under revision and points to the version-7 manual); FontCreator's manual was not reachable during research, so its evidence is product-page level; Birdfont's official documentation is homepage and release notes. Behavioral rules in this document are therefore stated at cross-product strength, and no numeric limits, default values, or format-version specifics are asserted. Detailed product-by-product observations are recorded in the paired Research Notes.
