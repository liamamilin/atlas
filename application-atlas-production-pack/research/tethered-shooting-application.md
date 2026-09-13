# Research Notes — Tethered Shooting Application

## Research Goal

Understand what a Tethered Shooting Application actually is, from real products: what its world is made of, what users do in it, how the shoot-time workflow flows, what rules and states matter, and where its boundary runs against RAW Photo Editor, Photo Workflow / Catalog Application, Photo Culling Application, Photo Editor, camera import tools, and mobile camera-remote companion apps.

## Initial Boundary

- Leaf: Tethered Shooting Application (§04.04 Photography). Slug: tethered-shooting-application.
- Working hypothesis: software that connects a camera to a computer so the photographer can control the camera from the computer, see a live view, and have each capture appear immediately on the computer during the shoot.
- Nearest neighbors: RAW Photo Editor (develop side), Photo Workflow / Catalog (collection system of record), Photo Culling (review side), Photo Editor, camera import utilities, mobile camera-remote apps (no directory leaf).
- Pre-hung seam to discharge: the raw-photo-editor pass flagged "capture-side vs develop-side — tethering inside a RAW editor is a variant capability; when camera control is the center, the product is the tethered Type."

## Research Questions

1. What is the connection model? (cable/wireless; camera detection; exclusive access)
2. What camera controls does the application expose, and how granular is per-camera support?
3. What is live view and is it definitional or optional?
4. What happens at capture — how do images arrive, where do they land, how are they named?
5. What is the shoot-session working context (folders/sessions/film rolls, naming templates)?
6. What review happens during the shoot (zoom, histogram, ratings, client viewing)?
7. How does the product hand off to post (develop/browse)?
8. What failure modes matter (disconnection, card posture, transfer-format mismatch)?
9. What are the variants (standalone vs module; vendor-locked vs cross-vendor; wireless/mobile)?
10. Where is the boundary vs RAW editor, catalog, culling, import tools, and mobile remote apps?

## Representative Products

| Product | Philosophy | Customer tier | Evidence |
|---|---|---|---|
| Capture One (Phase One) | pro suite where tethering is a flagship pillar | professional studio | Tier-1 help center, deep |
| darktable | open-source RAW developer with a dedicated Tethering view | enthusiast/pro, OSS | Tier-1 user manual, deep |
| digiCamControl | dedicated open-source tethering-only application | budget/prosumer, Windows | Tier-1 site + docs, deep |
| FUJIFILM X Acquire | camera-vendor bundled tethering utility (vendor-locked) | Fujifilm camera owners | Tier-1 vendor download page |
| Adobe Lightroom Classic | tethering as a module inside a catalog/develop suite | pro/consumer mass market | UNREACHABLE — anchor only |

Selection rationale: market representation (Capture One is the professional tethering standard; Lightroom Classic the mass-market suite), different product philosophies (suite / module / OSS dedicated / vendor utility), different customer tiers, and the vendor-locked pole the raw-photo-editor pass explicitly recorded as in-type.

## Sources

- Capture One Help Center (Zendesk) — https://support.captureone.com/hc/en-us — fetched 2026-09-09:
  - Home (category list; "Shooting Tethered — Tethering Essentials – Setup, Workflow and Troubleshooting")
  - Shooting Tethered category (sections: Tethered Capture; Live View; Camera Settings; Wireless Tethering; Capture Naming and Counters; Capture Location; Capture Adjustments; Working with an Overlay; Tethering/Live View/Camera Support FAQ)
  - "Tethered capture overview" — /hc/en-us/articles/360002549137
  - "Starting a tethered Session" — /hc/en-us/articles/360002549817
  - "What operations can I perform in Capture One whilst shooting tethered?" — /hc/en-us/articles/360002411197 (per-brand capability matrix)
- darktable 5.6 user manual — https://docs.darktable.org/usermanual/5.6/en/ — fetched 2026-09-09:
  - Tethering chapter: /tethering/ (overview, view layout, examples, troubleshooting)
  - Tethering overview — /tethering/overview/
  - Utility modules → tethering: camera settings — /module-reference/utility-modules/tethering/camera-settings/; live view — /module-reference/utility-modules/tethering/live-view/; session — (referenced)
- digiCamControl — http://digicamcontrol.com — fetched 2026-09-09:
  - Home page (feature blocks, screenshots, testimonials)
  - Complete feature list — /doc/basics/featurelist
  - Session (user guide) — /doc/userguide/session
- FUJIFILM X Acquire — https://fujifilm-x.com/en-us/support/download/software/x-acquire/ — fetched 2026-09-09 (overview, version history, compatibility notes)
- Adobe helpx (Lightroom Classic tethered capture) — https://helpx.adobe.com/lightroom-classic/help/tethered-capture.html and /tether.html — TIMEOUT ×2 this pass (plus ×2 in the raw-photo-editor pass 2026-09-08). Abandoned per network-restriction rule.
- Canon USA help center (EOS Utility) — https://www.usa.canon.com/support/help-center/eos-utility — 403. Canon Europe software page — 403. Nikon imaging software pages — 404 ×2. Abandoned; Fujifilm X Acquire stands as the directly observed camera-vendor pole.

## Product A — Capture One

### Key observations (evidence layer A — direct)

- **Tethering is a first-class pillar**: "Shooting Tethered" is a top-level help category ("Tethering Essentials – Setup, Workflow and Troubleshooting") with nine sections: Tethered Capture; Live View (16 articles); Camera Settings (17 articles); Wireless Tethering (per-brand guides for Canon/Nikon/Sony/Fujifilm); Capture Naming and Counters; Capture Location; Capture Adjustments; Working with an Overlay; FAQ.
- **Definition of the activity** ("Tethered capture overview"): "The Capture tool tab is the gateway to tethered shooting with a Phase One digital back or supported DSLR. When connected to the computer, you can import photos directly into a Session or Catalog and store them on the hard disk or an external drive, avoiding importing from a memory card."
- **Camera control**: "Capture One allows full control over a compatible camera. You can adjust a wide range of camera settings and parameters, including the exposure and metering modes, exposure compensation, ISO, white balance and release the shutter."
- **Live view**: "Capture One can even activate a camera's live view function and you can adjust the focusing either remotely, or manually, using the computer's monitor for composition and to check focus accuracy with an enlarged live preview." (The word "even" marks live view as an addition, not the base.)
- **Transport**: "supported cameras require a USB cable to connect the camera to the computer… for a simple out-of-the-box 'plug and play' experience." Wireless tethering is a separate section with per-brand setup guides ("limited to these supported cameras" per the FAQ matrix). A FireWire-era FAQ ("Why does not Capture One detect a digital back when shooting tethered via FireWire?") documents the older bus generation.
- **Unsupported cameras**: a Hot Folder mechanism ("Attaching an unsupported camera (Hot Folder)") — a watched-folder fallback for cameras the app cannot control.
- **Shoot destination**: "Starting a tethered Session" — File → New Session dialog: Name; Location (default Pictures/My Pictures); Template (predetermined albums/favorites/sub-folders); Subfolder names; Capture name ("the Session name is adopted automatically for naming images"). "The location can be altered later by using the Next Capture Location tool." Sessions are "popular for tethered capture due to their portable and autonomous folder structure"; tethered work in a Catalog is also documented.
- **Card posture**: "Note that the camera does not save or back up images to the memory card and does not require a memory card to be installed." A separate article covers "Saving to Memory Card and Capture One" (dual-save posture exists as an option).
- **Capture-time automation**: "the Capture tool tab allows you to apply a wide range of image adjustments and multiple styles including image preset, keywords, and IPTC metadata automatically from image to image, as well as photos name and create folders on import." Capture Adjustments section: adjustments/styles/presets at capture, ICC profile selection, capture orientation, metadata.
- **Naming machinery**: "Capture Naming and Counters" section — naming images when capturing; counters (add/set/increment/decrement/reset); import counter for memory-card use.
- **Capture location machinery**: "Capture Location" section — changing capture storage location (Sessions and Catalogs variants), multiple capture folders, Next Capture Location tool, folder creation from Session folders collections.
- **Second surfaces / client viewing**: "The Capture Pilot dialog… has a separate web function that enables you, your Art Director, and your colleagues to view, rate, and color tag captured images from a web browser on a computer, Android (mobile device) or Windows Phone"; the Capture Pilot iOS app lets users "present, rate, and capture images remotely."
- **Per-camera capability granularity** (FAQ matrix, "not all of these cameras behave or operate the same way as their functionality differs depending on the particular model and manufacturer"): Remote Capture — Yes for all listed brands; Camera focus from the application — No for Phase One/Leaf/Canon/Nikon/Sony, Yes for Fujifilm (from 16.7); Capture from Live View — varies; Program modes — varies; Shutter Speed / Aperture / ISO / EV / WB / Image Quality — mostly Yes with exceptions; Auto-Focus — varies; Zoom and Pan in Live View — varies; Wireless Tethering — limited to supported cameras. The camera support matrix (sibling pass, Tier-1) carries a per-camera Tethered / Live View / Wireless triple.
- **Reconnection**: a dedicated "ReTether" article; "Reconnecting a camera" in Camera Settings.
- **Overlay**: "Working with an Overlay" section — overlay tool for composition guides on live view, overlay pan tool, overlays with Capture Pilot.

## Product B — darktable

### Key observations (evidence layer A — direct)

- **Tethering is a top-level view**: "The tethering view allows you to capture images directly into darktable from a connected camera." Chapter: overview / tethering view layout / examples / troubleshooting.
- **Connection ritual**: connect camera by USB cable; the OS must NOT mount the camera ("Do not mount or view the camera… you will need to 'unmount/eject' the camera before darktable can access it"); "This unlocks the camera so that darktable can take control of it – darktable will then re-lock the camera so that it cannot be used by other applications." Unmount before physical disconnect. → exclusive camera access is an explicit, documented behavior.
- **Underlying library**: "darktable uses gphoto2 to interface with your camera." Troubleshooting section verifies "that your camera has tethering support."
- **Entry flow**: in the lighttable view's import module, a camera section appears with a "mount camera" button; after mounting: "copy & import from camera", "tethered shoot", "unmount camera". "Tethered shoot" enters the tethering view. → import-from-camera and tethered shoot are sibling operations, separated in the product's own UI.
- **Arrival + review**: "In the center view, images are shown while you capture them. You can capture an image by either using darktable's user interface or by manually triggering a capture with your camera. If you are using Live View the image will be shown in darktable's center view." → both trigger sources (app UI and camera body) documented.
- **Shoot container**: "When entering tethering view, a film roll will be created using the same structure as defined for camera import… The job code will be predefined as 'capture'." The session module sets a different job code; "a new film roll will be created and newly-captured images will be added into this new film roll." → film roll + job code = the shoot-scoped destination.
- **Camera control**: camera settings module — "Set up an image capture job. This can include sequence, bracket and delayed captures. You are also able to control other camera settings such as focus mode, aperture, shutter speed, ISO and white balance."
- **Live view**: live view module — "Control your camera's live view mode. Functionality such as focus control, rotation, guides and overlays are supported." (A module — i.e., an optional component within the view.)
- **Scripted capture**: "You can set up timelapse captures, brackets for HDR and even sequential captures of bracketed images."

## Product C — digiCamControl

### Key observations (evidence layer A — direct)

- **Self-description**: "the free tethered shooting solution"; "Control your camera settings remotely from your Windows PC via USB. Trigger image capture via release button on the camera or remotely from your computer. Handhold the camera, shoot, and have the resulting images displayed on the computer monitor."
- **Instant review**: "Review images right after photo is captured in full screen or display them instantly on the computer and view histogram and photo metadata… option to highlight over and underexposed areas in captured photos."
- **Advanced capture control**: "Shoot a series of bracketed shots with an arbitrary shutter speed, aperture or exposure value. Advanced interval meter to create a series of time-lapse images based on a highly customizable scheduler. Shooting triggered by motion detection for cameras which support live view."
- **Live view**: "see the image live through the camera on your computer's monitor before shooting. You can remotely autofocus or manually adjust the focus. Even zoom in and out so that you can confirm the focus is sharp. For better framing an overlay can be applied to the live image. You can also shoot a series of focus stacked images…"
- **Multiple cameras**: "control multiple connected cameras at the same time, triggering photo capture in parallel, or one by one… settings can be synchronized between connected cameras." External capture devices supported (Arduino triggers, USB relays).
- **Session model** (user guide): Session = name + folder + optional backup folder + file-name template + counter. Template tokens: [Counter N digit], [Camera Counter], [Session Name], [Capture Name], [Series], [File format], [Barcode], [Camera Name], [Date…]; backslash creates subfolders. Counter increments after every photo transfer. Options: download thumbnail only ("may not supported by the all camera model… useful when wifi connection is used"), download JPEG only for RAW+JPEG speed ("only if the transfer mod is set to 3. Save to Pc and camera"), use original camera file name, write tags as Exif/IPTC after transfer, overwrite protection (counter auto-increments until a free name), delete file after transfer ("can be used when the camera not support capture direct to pc").
- **Auto export plugins** (actions executed right after photo transferred): print, FTP transfer, copy to location, email, Facebook album; transforms: resize, overlay (text/image), crop, chromakey (green/blue screen), MagickScript effects.
- **Webserver**: "remote control of application functions via a web browser on a smartphone or tablet" — full-screen slide show, control functions, control live view, execute scripts.
- **Astronomy module**: bulb mode sequences, live view with star-size calculation for focusing, external shutter release devices (serial, DSUSB, USB relay).
- **Documented use cases**: Studio photography, Macro Photography, Astro Photography, Product photography, Books scanning, Stop-Motion Photography, Live View Streaming, Multiple Camera Usage.
- **Per-camera caveat**: "Not all features are supported by all camera models."
- **Connectivity variants**: Nikon via WiFi (router with modified firmware, WU-1a/1b adapter, camera built-in WiFi).
- **Testimonial** (weak, on-site): "while I can't tether into Lightroom, I can tether into Digicam control" (Nikon D200 user) — consistent with Lightroom tethering being camera-model-limited; testimonial-grade only.

## Product D — FUJIFILM X Acquire

### Key observations (evidence layer A — direct)

- **Core function**: "With the FUJIFILM X Acquire, you can send and save images directly to your PC via a USB cable when you take them with a camera connected to your PC." Destination folder specified at first run.
- **Vendor vocabulary**: version notes repeatedly say "Tethered shooting via USB or Wi-Fi" — the vendor itself calls the transfer-pole operation "tethered shooting", and documents wireless as an equal transport.
- **Per-camera, firmware-gated support**: compatibility added version by version (GFX 50S, X-T2, X-Pro2, X-H1, GFX 50R, GFX100, X-Pro3, X100V, X-T4, X-H2S, X-H2, X-T5, GFX100 II, X-S20…), some functions requiring minimum camera firmware ("This function can be used with GFX 50S ver. 1.10 or newer…").
- **Settings backup/restore**: "Backup/restore of camera setting for tethered shooting… this function can save all camera settings as a file and restore the setting from a stored setting. Therefore, you can change the camera settings at a moment and copy them to multiple cameras." (Not remote control — file-based settings management.)
- **Transfer-format negotiation**: "In case that the File Type (JPEG or RAW) to be transferred selected in the software is not selected in the IMAGE QUALITY menu in a camera, the message will appear on a PC screen… 'No image is transferred. Check the IMAGE QUALITY menu settings of camera.'" → the software's transfer selection must match the camera's recording format.
- **RAW+JPEG naming fix**: a version note fixes "a suffix like (1) is added to a file name of a JPG image when shooting with the 'RAW + JPEG' setting."
- **Handoff**: "RAW FILE CONVERTER EX2.0 is added as selectable software. You can browse images by the RAW FILE CONVERTER EX2.0 when using FUJIFILM X Acquire." → browse/develop handed to a companion application.
- **No remote camera control documented** — the page documents transfer + settings backup/restore only. This is the thin pole of the Type.
- **Product line evolution**: "FUJIFILM X Acquire has been integrated into 'FUJIFILM TETHER APP'" — successor product carries the same functions.

## Product E — Adobe Lightroom Classic (unreachable anchor)

- helpx.adobe.com timed out ×2 this pass (and ×2 in the raw-photo-editor pass). No internal operational claims made.
- Role in this research: widely-attested market anchor for the "tethering as a module inside a catalog/develop suite" philosophy. Its existence is corroborated by: (a) digiCamControl's testimonial referencing tethering into Lightroom; (b) the raw-photo-editor pass recording Lightroom Classic as a market anchor.
- digiCamControl testimonial (weak) suggests Lightroom tethering is camera-model-limited (Nikon D200 could not tether into it).

## Cross-product Comparison

| Dimension | Capture One | darktable | digiCamControl | FUJIFILM X Acquire |
|---|---|---|---|---|
| Primary surface | desktop (Win/macOS), pro suite | desktop (OSS), RAW developer with Tethering view | desktop (Windows), dedicated tethering tool | desktop utility (Win/mac), vendor-locked |
| Connection | USB (classic); wireless per-brand; FireWire-era backs documented | USB via gphoto2; exclusive camera lock | USB; Nikon WiFi variants; external triggers | USB or Wi-Fi (per-camera, firmware-gated) |
| Camera control | full: exposure/metering/EV/ISO/WB/release; focus varies by brand | focus mode, aperture, shutter, ISO, WB; sequence/bracket/delay jobs | settings remotely; remote autofocus/manual focus; presets | none documented (settings backup/restore files only) |
| Live view | yes (16-article section; zoom/pan varies by brand) | optional module (focus control, rotation, guides, overlays) | yes (zoom, overlay, focus stacking, streaming) | not documented |
| Arrival | "import photos directly into a Session or Catalog… avoiding importing from a memory card" | "images are shown while you capture them" | "resulting images displayed on the computer monitor"; instant review | "send and save images directly to your PC… when you take them" |
| Shoot container | Session (name/location/template/subfolders/capture name) or Catalog; Next Capture Location; multiple capture folders | film roll + job code ("capture" default; session module) | Session profiles (folder, backup folder, name template, counter) | destination folder (first-run setting) |
| Naming | naming templates + counters (dedicated section) | film-roll/job-code structure; import session options | token templates ([Counter]/[Camera Name]/[Barcode]/[Date]…), overwrite protection | camera-original names; RAW+JPEG suffix handling |
| Capture-time processing | adjustments/styles/presets/keywords/IPTC/ICC/orientation applied at capture | (develop happens in Darkroom after) | auto export plugins (print/FTP/email/Facebook) + transforms (chromakey/resize/overlay) | none (handoff to browse software) |
| Review instrumentation | enlarged live preview for focus; Capture Pilot rating/color tags | center view; filmstrip | full-screen review, histogram, metadata, over/under highlighting | via external RAW FILE CONVERTER |
| Client/second surface | Capture Pilot (iOS present/rate/capture) + web function for Art Director | — | webserver (browser control + preview) | — |
| Scripted capture | (counters; capture adjustments) | timelapse, HDR brackets, sequential brackets | bracketing, interval meter/time-lapse scheduler, motion detection | — |
| Card posture | computer-only documented ("does not require a memory card"); dual-save article exists | (import structure shared with camera import) | save-to-PC-only vs PC+card; delete-after-transfer; thumbnail-only | camera IMAGE QUALITY menu must match software transfer selection |
| Handoff | same app (develop in Sessions/Catalogs) | same app (Darkroom view) | auto export / browse sessions | RAW FILE CONVERTER EX2.0 |
| Per-camera granularity | capability matrix per brand; Tethered/Live View/Wireless triple per camera | "verify that your camera has tethering support" | "Not all features are supported by all camera models" | per-camera compatibility + firmware minimums |

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The connected camera as the live source of capture.** The application manages a connection to a camera (detects it, takes control of the link) and receives each capture through that connection as it is taken — during the shoot, not by importing files afterwards. Remove → a file importer / card reader.
2. **The shoot destination as the unit of organization.** Captures land in a shoot-scoped, application-managed container — session, folder set, or film roll — under the application's naming rules (templates, counters). Remove → a bare transfer pipe / background sync with no shoot memory.
3. **The shoot-time working loop.** The computer is the shoot's working surface: each capture is immediately available for review while shooting continues (and, in most products, the camera is operated from the same surface). Remove → a background copy daemon.

Jointly-held is load-bearing:
- 1 alone = transfer daemon; 2 without 1 = empty folder template; 3 without 1+2 = a viewer; 1+2 without 3 = background sync; 1+3 without 2 = an unorganized stream.

### L1 — Common Mature Structure

- In-application camera control: exposure settings (shutter/aperture/ISO), white balance, EV, metering/program modes, remote shutter release; focus control where the camera allows.
- Live view: remote framing on the monitor, remote/zoom focus checking, composition guides and overlays.
- Capture-time application of adjustments/styles/presets/metadata (the "looks right out of the gate" machinery).
- Capture review instrumentation: zoom to check focus, histogram, clipping/over-under highlighting, ratings/labels during the shoot.
- Naming templates and counters.
- Scripted capture jobs: bracketing, interval/time-lapse, delayed/sequence capture.
- Second surfaces: web/mobile companions for presenting, rating, remote capture.
- Handoff to develop/browse software (same suite or external).
- Reconnection handling (ReTether-class).
- Per-camera capability granularity: support matrices; what is controllable varies by camera model and manufacturer.

### L2 — Variant / Optional Structure

- Transport: USB cable (classic), Wi-Fi, older buses (FireWire-era digital backs), vendor-specific wireless adapters.
- Surface: desktop workstation (dominant); mobile/web companion surfaces; phone-as-remote pole (boundary question, below).
- Camera scope: cross-vendor applications vs camera-maker utilities locked to their own cameras.
- Memory-card posture: computer-only, card+computer dual save, delete-from-card-after-transfer, thumbnail/JPEG-only transfer for speed.
- RAW+JPEG handling: full RAW transfer vs JPEG-only preview transfer.
- Integration depth: standalone tethering tool vs module inside a RAW editor/catalog suite.
- Automation: motion-detection triggering, barcode triggering, external hardware triggers (Arduino/USB relay/serial), scripting/CLI/web control.
- Multiple-camera rigs with synchronized settings.
- Domain specializations: astro (bulb mode, star-size focusing), books scanning, stop-motion, product photography, live-view streaming.

### L3 — Vendor-specific Structure

- Capture One: tethered Sessions vs tethered Catalogs; Next Capture Location tool; Capture Pilot (iOS) + web function; ReTether; Hot Folder for unsupported cameras; per-brand capability matrix; per-brand wireless guides; Capture Naming/Counters/Capture Location/Capture Adjustments tool sections.
- darktable: film rolls + job codes; gphoto2 layer; exclusive camera lock with mount/unmount ritual; tethering as one of the app's views; camera settings/live view/session utility modules.
- digiCamControl: session profiles with backup folders; token-based filename template editor; auto export plugins; MagickScript transforms; astronomy module; branding/white-labeling; webserver; Tcl/scripting surfaces.
- FUJIFILM: X Acquire settings backup/restore files; transfer-format negotiation with camera IMAGE QUALITY menu; firmware-gated per-camera compatibility; TETHER APP successor integration; RAW FILE CONVERTER EX2.0 handoff.

## Vendor-specific Findings

- Capture One's Sessions are explicitly "popular for tethered capture due to their portable and autonomous folder structure" — the session document model is vendor-specific packaging of the shoot container.
- darktable's exclusive-lock ritual ("re-lock the camera so that it cannot be used by other applications") is a concrete implementation of camera-access arbitration.
- digiCamControl's barcode token and chromakey transform serve volume/id-photography and e-commerce workflows — vendor-specific realizations of shoot automation.
- Fujifilm's settings backup/restore ("copy them to multiple cameras") is a multi-camera fleet posture unique in this sample.

## Rejected Findings

- **"Camera control is definitional"** — REJECTED. FUJIFILM X Acquire (a camera-vendor tethering utility, called "tethered shooting" by Fujifilm itself) documents no remote control; its functions are transfer + settings backup/restore. Control is L1 — the dominant realization, not the invariant.
- **"Live view is definitional"** — REJECTED. Absent from X Acquire; an optional module in darktable; "Capture One can even activate a camera's live view function" (additive phrasing). L1.
- **"USB cable is definitional"** — REJECTED. Capture One ships a Wireless Tethering section with per-brand guides; Fujifilm documents "Tethered shooting via USB or Wi-Fi"; digiCamControl supports Nikon WiFi variants. Transport is L2.
- **"Desktop surface is definitional"** — HELD for the sampled population (all four directly observed products are desktop-class; mobile/web surfaces are companions), but the mobile camera-remote pole is recorded as an open boundary question, not resolved.
- **"RAW handling is definitional"** — REJECTED. JPEG-only and thumbnail-only transfer options exist (digiCamControl); the Type is agnostic about what arrives.
- **"Tethering requires a memory card" / "excludes a memory card"** — REJECTED both ways. Capture One documents card-less operation; digiCamControl documents card+PC dual save and delete-after-transfer. Card posture is L2.
- **"Tethered shooting = importing from camera"** — REJECTED. Capture One's own FAQ separates "Can I import from a camera over USB?" from tethering; darktable's import module offers "copy & import from camera" and "tethered shoot" as sibling buttons. Import is after-the-fact; tethering is during-the-shoot.

## Boundary Findings

1. **vs RAW Photo Editor (04.04, processed) — DISCHARGES the pre-hung seam from this side.** The seam proposed by the raw-photo-editor pass ("capture-side vs develop-side; tethering inside a RAW editor is a variant capability; when camera control is the center, the product is the tethered Type") is CONFIRMED with first-hand evidence. The tethered Type's object of work is the shoot in progress — connection, control, arrival, destination, review; the RAW editor's object is the captured file's interpretation. Removal tests both directions: remove the camera connection from Capture One → a RAW editor/catalog remains (DxO PhotoLab's documented structure, per that pass, has no tethering chapter and remains a full RAW editor); remove the develop loop from a tethered tool → a tethered tool remains (digiCamControl has no develop loop at all and is fully in-type; Fujifilm X Acquire hands browsing to a separate converter). Capture One and darktable bundle both sides — packaging, not identity. **Keep-both RATIFIED.**
2. **vs Photo Workflow / Catalog Application (04.04, processed)** — the catalog Type's record layer is the collection system of record across shoots; the tethered Type's session/film-roll is a shoot-time working container. Straddle documented: Capture One's tethered Sessions are shoot-scoped documents that can live inside a Catalog — the same container serves both centers. Test: remove the camera connection → the Session becomes a folder-based working document (catalog-side); remove the collection ambition → the shoot container remains tethered-side. Consistent with that pass's "make camera control the unit → tethered shooting."
3. **vs Photo Culling Application (04.04, processed)** — culling is review-and-decide over an imported batch after the fact; tethered review is on-arrival during the shoot. Rating during tethered review (Capture Pilot "rate, and color tag"; digiCamControl tag selector written as Exif/IPTC) is capability overlap, consistent with the culling pass's "capture-side control of the camera vs review-side decisions on captured images."
4. **vs Photo Editor (04.04, processed)** — capture-time adjustments/styles are recipes applied on arrival, not an interactive per-image editing loop; no editing center exists in the tethered core. Consistent with the photo-editor pass's L2 placement of tethered capture.
5. **vs camera import tools / Image Batch Processor (04.05)** — import-from-camera after the shoot is a different activity (Capture One FAQ separates them; darktable UI separates them). Tethering's defining property is arrival during the shoot.
6. **vs Stop-motion Animation Application (04.08, processed)** — digiCamControl documents "Stop-Motion Photography" as a use case; that pass's Type centers the per-frame physical-scene capture studio. Tethered capture is a capability inside such studios; no boundary failure. Consistent.
7. **vs mobile camera-remote companion apps (no directory leaf)** — phone apps that remotely control a camera and receive its images (camera-maker companion apps) share the connection/control/transfer structure but center camera operation (framing, triggering from a distance) rather than the shoot workflow (destination, naming, review loop, handoff). All sampled tethered products are desktop-class shooting workstations with mobile surfaces as companions. Recorded as a boundary question for the taxonomy owner; no leaf exists to merge with.
8. **Camera-vendor tethering utilities** — Fujifilm X Acquire (and the EOS Utility-class products it stands for) satisfy the L0 with vendor-locked camera support; they are in-type instances (vendor-locked variant), not a separate Type. Mirrors the raw-photo-editor pass's treatment of camera-vendor bundled converters.

## Uncertainties

- **Adobe Lightroom Classic unreachable** (helpx timeouts ×2 this pass; ×2 in the raw-photo-editor pass). Held as a widely-attested anchor only; no internal operational claims. If a later pass reaches Adobe docs, the module-inside-suite variant and its camera-support limits should be re-verified.
- **Canon/Nikon vendor utility documentation unreachable** (403/404). The camera-vendor pole is directly observed only through Fujifilm X Acquire; Canon EOS Utility-class products are named as market context, with no mechanism claims.
- **Mobile camera-remote apps** unsampled (no leaf; camera-maker app domains not fetched). The boundary question is recorded, not resolved.
- **Exact per-camera capability lists** vary by product version; no precise per-model claims are made in the final document beyond the sampled products' own statements.
- **Wireless tethering reliability machinery** (best-practices article exists at Capture One) not fetched in detail; held as "reconnection/best-practice machinery exists", no specifics.

## Historical / Market-Sample Check

- The Type is inherently digital-era: there is no film-era instant-review ancestor (the defining property — captures arriving on a screen during the shoot — has no analog equivalent; Polaroid proofing and video assist are different mechanisms). The earliest generation in evidence: tethered digital backs and DSLRs over FireWire/USB (Capture One's own docs: "gateway to tethered shooting with a Phase One digital back or supported DSLR"; FireWire detection FAQ; gphoto2-lineage OSS support).
- The L0 names no transport (cable/wireless), no live view, no camera control, no AI, no cloud, no subscription. A cable-era vendor utility (X Acquire pole: transfer + destination + availability) satisfies all three legs; a modern wireless pro suite satisfies the same three legs with more machinery. Historical check PASSES.
- Vendor-locked utilities, OSS tools, and pro suites across a decade of product generations fit without era machinery.

## Final Synthesis

The Tethered Shooting Application is the **capture-side** photographic application: its object of work is the shoot in progress. Its floor is three jointly-held structures: (1) the connected camera as the live source of capture — the application manages the camera connection and receives each capture as it is taken; (2) the shoot destination as the unit of organization — captures land in a shoot-scoped, application-managed container under the application's naming rules; (3) the shoot-time working loop — the computer serves as the shoot's working surface where captures are immediately available for review while shooting continues. Everything else — camera control, live view, capture-time adjustments, review instrumentation, second surfaces, scripted capture, wireless transport, mobile companions — is common mature structure or variant capability that packages around that loop.

The category is real and distinct from the RAW Photo Editor by center of gravity (the shoot in progress vs the captured file's interpretation), from the Photo Workflow / Catalog by what is the system of record (the shoot container vs the collection), and from camera import by timing (during the shoot vs after it). The market's own vocabulary supports the split: Capture One maintains "Shooting Tethered" as a top-level help category; darktable ships a dedicated Tethering view beside its Lighttable and Darkroom; digiCamControl self-identifies as "the free tethered shooting solution"; Fujifilm's own version notes call the transfer operation "tethered shooting". The per-camera support model is the Type's load-bearing external dependency, structurally parallel to the RAW editor's per-camera RAW support.

```text
L0 (defining invariant)
- Connected camera as the live source of capture (application-managed connection; captures received as taken)
- Shoot destination as the unit of organization (shoot-scoped container + naming rules)
- Shoot-time working loop (captures immediately available for review while shooting continues)

L1 (common mature structure)
- In-application camera control (exposure settings, release; focus where allowed)
- Live view (framing, focus checking, guides/overlays)
- Capture-time adjustments/styles/metadata
- Capture review instrumentation (zoom, histogram, ratings)
- Naming templates + counters
- Scripted capture jobs (bracketing, interval/time-lapse)
- Second surfaces (web/mobile companions for present/rate/remote-capture)
- Handoff to develop/browse
- Reconnection handling
- Per-camera capability granularity (support matrices)

L2 (variant / optional)
- Transport (USB / Wi-Fi / legacy buses)
- Surface (desktop workstation; mobile/web companions; phone-remote pole — open question)
- Camera scope (cross-vendor vs vendor-locked)
- Memory-card posture (PC-only / dual / delete-after / thumbnail-only)
- RAW+JPEG transfer handling
- Integration depth (standalone vs module in RAW editor/catalog)
- Automation (motion detection, barcode, external triggers, scripting)
- Multiple-camera rigs
- Domain specializations (astro, books scanning, stop-motion, product, streaming)

L3 (vendor-specific)
- Capture One: Sessions/Catalogs tethered documents, Capture Pilot, ReTether, Hot Folder, capability matrix
- darktable: film rolls/job codes, gphoto2, exclusive lock ritual, Tethering view
- digiCamControl: session profiles + backup folders, token templates, auto export plugins, astronomy module, webserver
- Fujifilm: settings backup/restore, transfer-format negotiation, firmware-gated compatibility, TETHER APP
```
