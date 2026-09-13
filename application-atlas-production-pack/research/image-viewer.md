# Research Notes — Image Viewer

## Research Goal

Understand the Image Viewer as an Application Type from real products: what its defining structure is, what "viewing" actually consists of as an interaction, how viewers handle the fact that images come in folders and collections, which capabilities cluster around the viewing core without defining it, and where the boundary runs against the neighboring leaves that previous passes already documented seams toward (File Manager, Photo Editor, Raster Image Editor, Image Conversion Application, Image Batch Processor, Photo Culling Application, Photo Workflow / Catalog Application, PDF / Document Reader, Web Archive Viewer).

## Initial Boundary

- Hypothesis: the Image Viewer's center of gravity is **display of image-file content for human looking** — rendering + inspection — with no transformation of the image as the purpose.
- Likely nearest types: File Manager (delegates rendering), Photo Editor / Raster Image Editor (transforms pixels), Image Conversion Application (changes encoding), Image Batch Processor (set-level pipelines), Photo Culling (decisions), Photo Workflow / Catalog (records layer), PDF / Document Reader (document semantics), Web Archive Viewer (a different "viewer" semantics entirely).
- Known prior commitments from sibling passes (STATUS.md):
  - photo-editor: "remove *deliverable* (view only) → Image Viewer"; "viewers render without transforming; editors transform… the same capability-overlap logic applies to viewers with rudimentary adjust-and-save"
  - photo-culling-application: "viewers display; cullers decide… remove per-photo decision recording + selection output → Image Viewer"
  - image-conversion-application: "A viewer's purpose is display; a converter's purpose is transformation. Many viewers embed export/save-as… a conversion capability embedded in another Type's packaging"; noted "Viewer products not sampled in that pass; boundary stated at concept level" — this pass discharges that evidence gap
  - image-batch-processor: "A viewer's purpose is display; XnConvert's sibling browser is a viewer that hands off to batch conversion — the hand-off documents the seam"
  - file-manager: "those render content of one file; the file manager renders *metadata + structure* and delegates content rendering to viewers (Preview pane/Quick Look pattern)"
  - pdf-document-reader: "single raster images vs multi-page paginated documents… Preview bundles both poles in one app… the seam is document semantics"
  - photo-workflow-catalog-application: "displays photos; no record layer, no cycle | remove records + production stages → viewer"
  - raster-image-editor: "remove *direct pixel manipulation* (view only) → Image Viewer"

## Research Questions

1. What is the central object — the image file, the viewing session, or a collection?
2. What does "viewing" minimally include: rendering, zoom/fit/pan, rotation, fullscreen, slideshow?
3. How do viewers handle many images: folder-as-sequence, thumbnail browser, filmstrip, library?
4. What is the viewer's posture toward the file: does viewing modify anything?
5. What format breadth is typical, and how is breadth achieved (native, plugins, codecs)?
6. Which adjacent capabilities (edit, convert, batch, organize) appear inside viewer products, and how are they packaged?
7. What interface shapes exist: single window, browser+viewer, filmstrip, fullscreen, info panes?
8. Do older / platform-native / regional products fit the same core (historical check)?

## Representative Products

Chosen for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Evidence |
|---|---|---|
| IrfanView | lightweight minimal freeware viewer, single-window, hotkey-driven, plugin-extensible (Windows, since 1996) | A — official site + "What is IrfanView" page |
| XnView MP | browser-first freeware viewer/organizer, cross-platform; sibling of the XnConvert batch sample | A — official product pages incl. dedicated image-viewer page |
| Apple Preview | platform-native macOS viewer bundled with PDF/document semantics | A — official Preview User Guide |
| Microsoft Photos | platform-native modern consumer app, collection-first, cloud-integrated | A — official Microsoft Support articles |
| ACDSee Photo Studio | commercial prosumer/pro photo family where the viewer is a named mode (View Mode) inside a management suite; lineage from 1994 viewer | A — official help file (PDF) + about page |

## Sources

All fetched 2026-09-10; all directly reachable (no evidence downgrade required):

- IrfanView — official homepage — https://www.irfanview.com/
- IrfanView — "What is IrfanView?" — https://www.irfanview.com/main_what_is_engl.htm
- XnView — XnView MP product page — https://www.xnview.com/en/xnviewmp/
- XnView — dedicated image-viewer page — https://www.xnview.com/en/image-viewer/
- Apple — Preview User Guide for Mac — https://support.apple.com/guide/preview/welcome/mac
- Microsoft — "Manage photos and videos with Microsoft Photos app" — https://support.microsoft.com/en-us/windows/apps/photos/manage-photos-and-videos-with-microsoft-photos-app
- Microsoft — "Changes in the new Photos app" — https://support.microsoft.com/en-us/windows/apps/photos/changes-in-the-new-photos-app
- Microsoft — "Get help with Microsoft Photos app" — https://support.microsoft.com/en-us/windows/apps/photos/get-help-with-microsoft-photos-app
- ACD Systems — ACDSee Photo Studio Ultimate 2026 Help File (PDF) — https://help.acdsystems.com/en/acdsee-ultimate-19/acdseeultimate19.pdf
- ACD Systems — About page (lineage) — https://www.acdsee.com/en/about

## Product Observations

### IrfanView (evidence layer A)

- Self-labels: "fast, compact and innovative FREEWARE (for non-commercial use) **graphic viewer** for Windows"; homepage: "One of the Most Popular Viewers Worldwide"; "Designed to be simple but powerful"; single-EXE posture ("Only one EXE-File, no DLLs"); copyright 1996–2026.
- Feature list mixes viewing core with adjacent capabilities: "View Images", "Convert", "Optimize", "Scan & Print", "Create Slideshow", "Batch Processing", "Multimedia".
- Viewing-relevant: "Many supported file formats"; "Thumbnail/preview option"; "Fast directory view (moving through directory)"; "Slideshow (save slideshow as MP4 video, or as EXE/SCR or burn it to CD/DVD)"; "Show EXIF/IPTC/Comment text in Slideshow/Fullscreen"; "Show transition effects between images in Slideshow/Fullscreen"; "Support for alpha layer/transparency"; "Many hotkeys"; "Many command line options"; "Many PlugIns"; "Support for embedded color profiles" (JPG/TIF); "Print option".
- Explicit-modification capabilities (separate acts, not the viewing act): "Lossless JPG rotation, crop and EXIF date change (also in batch mode)"; "Paint option"; "Cut/crop"; "Effects (Sharpen, Blur, …)"; "IPTC editing"; "Multiple undo".
- Philosophy markers: "simple for beginners and powerful for professionals"; claims first-mover status on animated GIF / multipage TIF / multiple ICO support in Windows viewers.

### XnView MP (evidence layer A)

- Self-labels: "Professional Image Viewer, Photo Management, Image Resizer & Batch Converter"; dedicated page: "The Fast, Free Image Viewer for Windows"; "a direct Windows Photo Viewer replacement"; "XnView is built around a browser, not a single-image window."
- Viewing surfaces: "Thumbnail View", "FullScreen View", "FilmStrip View", "SlideShow with Effects", "Image Compare (up to 4 images)"; thumbnail view "with adjustable size and a persistent cache"; "designed to browse folders containing thousands of photos".
- Format posture: "opens more than 500 image formats" read vs "Export to about 70 different file formats" write — the decode-broad/encode-narrow asymmetry, stated by the vendor; RAW/HEIC/AVIF/JPEG XL/PSD/DICOM readable; PDF via free Ghostscript add-on; per-format viewer guide pages (jpeg-viewer, raw-viewer, dicom-viewer, …) as market vocabulary.
- Explicit-modification capabilities: resize/rotate/crop, "Lossless Rotate & Crop (jpeg)", brightness/contrast/gamma, auto levels, filters/effects, metadata editing (EXIF/IPTC/XMP read-edit-remove), paint (lines/circles/arrows/watermark).
- Adjacent packaging: "Powerful Batch Convert (same module also powers XnConvert)", batch rename, contact sheets, duplicate finder, print module, screen capture, scan support, multimedia player, face detection (MP).
- Integration: "set as your default photo viewer" instructions (Open with → Always); portable ZIP distribution; freeware private/educational, paid company license.
- Vendor-published comparison vs Microsoft Photos: formats ("Common formats; HEIC, AVIF and RAW need Store extensions" vs "500+ built in"), browsing ("Single-image window with a strip" vs "Full folder browser"), batch tools ("—" vs built in). (Vendor-stated; used as positioning evidence, not as neutral fact.)

### Apple Preview (evidence layer A)

- User guide top-level organization: "View PDFs or images" / "Edit PDFs" / "Edit images" / "Share PDFs or images" / "Manage PDFs or images" / "Print PDFs and images" — one app spanning viewer + editor + converter + manager semantics (the strongest straddle evidence, consistent with the PDF-reader pass).
- Viewing-relevant sections: "View PDFs and images"; "View information about PDFs and images" (info/metadata panel); "See where a photo was taken" (GPS metadata); "Display a PDF as a slideshow"; "View an animated GIF's frames"; "Interact with text in a photo" (text extraction from image content); "Import images from a camera".
- Explicit-modification capabilities: "Crop, resize, or rotate an image"; "Convert image file types" (stated format list: HEIC, JPEG, JPEG 2000, OpenEXR, PDF, PNG, TIFF); "Remove a background or extract an image"; "Annotate an image"; "Apply a color profile to an image"; "See what an image looks like on another device".
- Non-destructive posture documented: "Revert changes to PDFs and images"; "Save PDFs and images"; "Lock PDFs and images"; "Export PDFs and images".
- Print is a first-class section ("Print PDFs and images").

### Microsoft Photos (evidence layer A)

- Self-description: "a built-in application for Windows operating systems that allows users to view, organize, edit, and share their photos and videos"; "view, edit, and enhance the quality and appearance of your media files, and share selected items… browse, sort, and search photos and videos, import media from devices, organize your content into folders".
- Collection-first posture: "Once the Photos app is open, you'll see a list of all the photos allowing you to scroll through and choose the one you desire"; "By default, the Photos app shows all the photos in your Pictures folder"; other locations added via folders; sorting and search by name/date/type/location.
- Formats stated: JPEG, PNG, GIF, BMP, TIFF for photos; MP4, MOV, AVI for videos. (XnView's comparison page adds that HEIC/AVIF/RAW "need Store extensions" — vendor-stated, cross-source.)
- New Photos app features: "Filmstrip | …jump to other photos without leaving the filmstrip"; "Multi-view | Compare multiple photos and videos side by side in the same window"; "Memories"; enhanced folder navigation; iCloud integration alongside OneDrive.
- Editing as a separate explicit mode: crop/rotate/adjust/filter/mark-up; "press the spacebar to view the original photo" (before/after); "Reset" to cancel edits.
- Photos Legacy split: legacy app retains Video Editor, People tab, Albums, slideshow creator — evidence that the platform itself treats viewer/library/editor as separable concerns packaged one way or another.

### ACDSee Photo Studio (evidence layer A)

- Positioning: "digital photo and document management software"; About page: product line "since 1994", "Branching out from image viewing, digital asset management, format conversion…" — the company's origin is an image viewer, later expanded into a suite.
- The viewer survives as a named, separable mode: **View Mode** — "display images and documents in full resolution, one at a time. You can also open panes to view image properties, display areas of an image at varying magnifications, or examine detailed color information." "…use the Filmstrip in View mode to flip quickly between all of the files in a folder. View mode contains a toolbar with shortcuts to commonly-used commands, and a status bar… which displays information about the current image."
- View Mode capability inventory (from the help file's View-mode chapter): zoom drop-down list, Zoom Lock ("Displays all images at the zoom option of the current image… applied to all images that you view"), Actual Size, rotate left/right, Viewing File Properties in View Mode, Viewing Documents, Viewing PDF Files in View Mode, Printing Images and Documents in View Mode, Synchronizing View Mode to a Folder, Setting an Image as the Desktop Wallpaper, Viewing Offline Images, Viewing Images in Another Application, Showing Originals, Displaying Text on Images, Viewing Images with Image Advance, Recording Audio to an Image.
- Surrounding modes: Manage (folder browsing + catalog into the ACDSee database), Media (cataloged content only), Develop/Edit (RAW and pixel editing), People (facial recognition), 365 (cloud sharing), Dashboard (statistics) — the suite packaging where viewing is one mode among many.

## Cross-product Comparison

| Dimension | IrfanView | XnView MP | Preview | Photos | ACDSee View Mode |
|---|---|---|---|---|---|
| Self-label | "graphic viewer" | "image viewer" / "photo management" | (platform viewer; guide: "View PDFs or images") | "view, organize, edit, and share" | "View Mode" inside Photo Studio |
| Image rendering as primary purpose | yes | yes | yes (shared with PDF) | yes (shared with videos/library) | yes (one mode of the suite) |
| User-controlled presentation (zoom/fit/pan) | yes (hotkeys) | yes (fullscreen/fit; compare) | yes (view + zoom documented) | yes (filmstrip + zoom) | yes ("varying magnifications", zoom list, Actual Size, Zoom Lock) |
| Sequence navigation over a file set | "fast directory view" | filmstrip / thumbnails | multi-file open, sidebar | filmstrip over library/folder | "Filmstrip… flip quickly between all of the files in a folder" |
| Thumbnail browser / grid | optional thumbnail window | browser-first ("built around a browser") | (sidebar of opened files) | collection list/grid default | Manage mode (separate) |
| Fullscreen / slideshow | yes (+ transitions, export slideshow) | yes (+ effects) | slideshow documented | slideshow (legacy feature) | (print/wallpaper; slideshow not highlighted in View chapter) |
| Rotation | lossless JPG rotation as explicit save | lossless rotate & crop (jpeg) | crop/resize/rotate (edit section) | rotate in edit mode | rotate left/right in View mode |
| Metadata display | EXIF/IPTC/Comment in fullscreen/slideshow | EXIF/IPTC/XMP read-edit-remove | "View information about PDFs and images" | search by date/type/location | properties pane in View mode |
| Print | yes | print module | first-class section | (not highlighted) | "Printing Images and Documents in View Mode" |
| Color profiles | embedded profiles (JPG/TIF) | embedded color profiles supported | apply a color profile | (not documented in sampled pages) | "examine detailed color information" |
| Editing capability inside product | paint/crop/effects (explicit acts) | full adjust set + lossless ops | Edit images section | edit mode with reset | separate Develop/Edit modes |
| Conversion/export embedded | convert; batch conversion | export ~70 formats; batch convert | "Convert image file types" | (share/export) | export via suite |
| Library/records layer | none (folder-driven) | none (folder-driven; search/sort) | none (file-driven) | library from folders + cloud (OneDrive/iCloud), folders-as-albums | catalog database (Manage/Media modes) |
| Format breadth posture | "many supported file formats" + PlugIns | 500+ read / ~70 write; no codec pack | platform format list | common formats; extensions for others | RAW viewing documented |
| Extensibility | PlugIns page | Ghostscript add-on (PDF) | (platform codecs) | Store extensions | (suite modules) |
| Non-image content | multimedia player; icon extraction | PDF (add-on), DICOM, video thumbnails | PDF as co-equal object | videos (MP4/MOV/AVI) | documents, PDFs, media files |
| Platform-native integration | shell extension plugin; wallpaper | default-viewer replacement; portable | OS-bundled; share sheet | OS-bundled; OneDrive/iCloud | wallpaper; "Viewing Images in Another Application" |

## Canonical Model

### Level 0 — Defining Invariant

Three properties, held together. Remove any one and the product stops being recognizable as an Image Viewer:

1. **Image-content rendering** — the application decodes image files and presents their visual content on screen as its primary purpose. What is displayed is the picture itself, not an icon, a metadata record, or a file listing. Remove → file manager / catalog territory.
2. **Viewer-controlled presentation** — the user steers how the displayed image is presented: at minimum changing its display scale (fit to window, zoom in/out, actual size) and moving around within an image larger than the viewport. Remove → a slideshow player / kiosk display, not the interactive viewer Type.
3. **Non-modifying viewing** — the act of viewing leaves the image unchanged; any change to pixels or encoding happens only through an explicit separate command (save, edit, export). Remove → the product is an editor, not a viewer.

### Level 1 — Common Mature Structure

Present across the sampled products (mostly all five) without defining the Type:

- **Sequence navigation over a file set** — next/previous movement through a folder or selection; the filmstrip is the mature shared realization (IrfanView "fast directory view", XnView filmstrip, Preview sidebar, Photos filmstrip, ACDSee filmstrip).
- **Thumbnail browsing** — a grid of small previews for choosing among many images; packaged differently (dedicated browser in XnView, optional window in IrfanView, separate Manage mode in ACDSee, default collection view in Photos).
- **Fullscreen presentation and slideshow** — with transition effects in several products; IrfanView can export the slideshow itself.
- **Rotation** — display rotation is ubiquitous; lossless JPEG rotation as an explicit save exists in the desktop freeware samples.
- **Metadata / info display** — an info surface showing EXIF/IPTC/properties (all five in some form).
- **Print** — present in four of five sampled surfaces.
- **Broad format support beyond platform defaults** — RAW, HEIC, AVIF, JPEG XL etc. as the classic viewer selling point; achieved natively, via plugins, or via codec/extensions. Decode breadth exceeds write breadth (mirroring the converter asymmetry).
- **Hand-off to other tools** — open in editor, open in another application, send to batch converter.
- **Default-app / OS integration** — set as default viewer, shell/open-with integration, set as wallpaper.
- **Color-profile handling** — embedded ICC profile support in three of five samples; a correctness feature of mature viewers.

### Level 2 — Variant / Optional Structure

- **Editing capability inside the viewer product** — ranges from paint/annotate to full adjustment panels; platform-native products bundle it (Preview, Photos), freeware viewers offer explicit lossless ops, suites separate it into modes. The drift marker: when editing becomes the purpose, the product is a Photo Editor.
- **Conversion / batch capability embedded** — save-as/export, batch conversion, batch rename (IrfanView, XnView). Capability overlap with the converter and batch-processor Types.
- **Library / records layer** — catalog database (ACDSee), cloud-synced library with albums/memories/people (Photos), folders-as-albums. Drift toward Photo Workflow / Catalog Application or the platform photo library.
- **Cloud integration** — OneDrive/iCloud library sources (Photos).
- **Non-raster content breadth** — PDF (Preview co-equal; XnView via add-on; ACDSee documents), DICOM (XnView), video/multimedia playback (IrfanView, Photos, ACDSee) — breadth straddles, not identity.
- **Text extraction from image content** (Preview "interact with text in a photo") — modern platform capability.
- **Animated-format handling** — GIF frame viewing, APNG, animated WebP/AVIF.
- **Packaging variants** — portable/no-install (IrfanView single EXE, XnView portable ZIP), plugin ecosystems, codec-extension dependency (Photos), suite mode (ACDSee).

### Level 3 — Vendor-specific (research notes only)

- IrfanView: slideshow export to MP4/EXE/SCR/CD-DVD; icon extraction from EXE/DLL/ICL; single-EXE/no-registry posture; first-mover claims (animated GIF, multipage TIF, multiple ICO); vendor rivalry statement about XnView.
- XnView: per-format SEO viewer pages; "Windows Photo Viewer replacement" positioning; license pricing tiers (€29 single, volume discounts); MP vs Classic edition split.
- Apple Preview: AutoFill PDF forms, password-protect PDF, background removal, bookmark PDF pages — mostly PDF-side capabilities riding the same app.
- Microsoft Photos: Memories, iCloud integration, Clipchamp hand-off, Photos Legacy vs new app split, Store codec extensions.
- ACDSee: eight-mode taxonomy (Manage/Media/View/Develop/Edit/People/365/Dashboard), 365 seedrive sharing, facial recognition, AI features, database cataloging.

## Boundary Findings

Removal tests, each consistent with the sibling pass that documented the other side:

- **Remove rendering purpose** (keep storage organization/metadata/structure) → **File Manager**. The file manager delegates content rendering to viewers (preview pane / Quick Look pattern — documented by the file-manager pass).
- **Add per-image creative/repair transformation as the purpose** → **Photo Editor**. Viewers render without transforming; rudimentary adjust-and-save inside a viewer is capability overlap (photo-editor pass: "remove deliverable (view only) → Image Viewer").
- **Add authoring from a blank canvas / layered composition** → **Raster Image Editor** (raster pass: "remove direct pixel manipulation (view only) → Image Viewer").
- **Make encoding transformation the purpose** → **Image Conversion Application**. Viewers embed save-as/export; converters embed preview. Purpose test: where the user goes to look at images vs to change encoding (conversion pass; this pass supplies the viewer-side evidence).
- **Make a set-level operation pipeline the defining object** → **Image Batch Processor**. The XnSoft family itself demonstrates the seam: XnView (viewer/browser) hands off to XnConvert (batch) — the hand-off documents the boundary (batch pass).
- **Add per-photo selection decisions** (keep/reject, ratings as decisions) → **Photo Culling Application**. "Viewers display; cullers decide" (culling pass). Viewers may offer ratings/filters — capability overlap, different posture.
- **Add a records layer** (albums, ratings-as-data, catalog database, production cycle) → **Photo Workflow / Catalog Application** or the platform photo library (workflow pass: "remove records + production stages → viewer").
- **Add multi-page document semantics** (pages, text layer, forms, permissions) → **PDF / Document Reader**. For a single-page scanned PDF the two Types nearly coincide; the seam is document semantics, not raster vs fixed-layout (pdf pass; Preview is the documented straddle).
- **Time-addressed replay of archived web captures** → **Web Archive Viewer** — shares only the word "viewer"; its object is archived web resources addressed by URL + capture time, not image files.
- **Remove inspection control (zoom/pan), keep display** → slideshow/kiosk player — a drift out of the Type rather than into a documented neighbor.

## Historical / Market-Sample Check

- IrfanView (1996) and ACDSee (origin 1994 as a viewer) satisfy the three-property core with none of the modern additions (no cloud, no AI, no editing modes required) — the 1990s desktop viewer passes unchanged.
- Windows Photo Viewer (the removed Windows default, referenced by XnView's replacement page) — a platform-native viewer satisfying the core.
- Phone gallery apps (platform-native mobile viewers) fit the core with a collection-first surface; not directly sampled from official docs in this pass — treated as a variant posture, evidence-qualified.
- The core names no substrate technology: no thumbnails-cache, codec-pack, GPU, or cloud requirement is definitional.

Check passed: the definition is not fitted to the current browser-first or platform-native market alone.

## Uncertainties

- **Zoom-as-invariant**: strongly supported across the sample (all five document magnification/fit machinery), but a hypothetical slideshow-only product was not sampled; the claim is kept at concept level ("at minimum scale and pan control") rather than tied to specific UI mechanics.
- **Navigation in L0 vs L1**: sequence navigation is present in all five samples and central to the use case, but a minimal single-image displayer is plausibly still market-classified as a viewer; navigation was therefore placed in common mature structure rather than the defining core. Flagged for any future joint review.
- **Format counts** ("500+ read / ~70 write") are vendor-stated figures from XnView's marketing pages — recorded here, deliberately not stated as category facts in the final document.
- **Phone-gallery apps** were not researched from official vendor docs; their classification as a variant posture rests on the platform-native pattern (Photos/Preview) plus general market knowledge — evidence-qualified.

## Final Synthesis

The Image Viewer is the display leg of the image-tool ecosystem. Its defining core is exactly three jointly-held properties: rendering image-file content as the primary purpose, user-controlled presentation of the displayed image (scale/fit/pan), and non-modifying viewing. Everything else the market associates with viewers — folder navigation, thumbnail browsers, filmstrips, slideshows, metadata panels, format breadth, print, editing hooks, conversion exports, library layers — is common mature structure or variant capability that clusters around the viewing act without defining it. The Type's boundaries are all "purpose" boundaries already documented from the neighboring sides: display vs organize (File Manager), display vs transform (editors), display vs re-encode (converter), display vs pipeline (batch), display vs decide (culling), display vs record (catalog), image vs document (PDF reader), files vs archived web (web archive viewer). The viewer is also the most commonly bundled leg: platform-native products fold viewer + editor + converter + library into one app, and management suites keep the viewer as a named mode — in both cases the viewer function remains separable and recognizable.
