# Research Notes — Photo Workflow / Catalog Application

## Research Goal

Understand what a Photo Workflow / Catalog Application actually is, from real products: what its world is made of, what users do in it, how the photographic production cycle flows through it, what rules and states matter, and where its boundary runs against Photo Editor, RAW Photo Editor, Photo Culling Application, Image Viewer, Image Batch Processor, DAM/MAM, and Tethered Shooting.

Two pre-hung joint-review flags from sibling §04.04 passes must be discharged here:
- photo-culling-application (processed 2026-09-08): "dedicated culling products and catalog suites share the same per-photo decision vocabulary… keep-both leaning per the market's persistent dedicated-culler segment — recommend joint review when photo-workflow-catalog-application is processed."
- photo-editor (processed 2026-09-08): "(b) per-image editing vs cross-shoot library/pipeline: pro products bundle both…; remove the library → editing core remains a photo editor."

## Initial Boundary

Working hypothesis before research: this Type is the photographer's system of record for their whole photo collection — a persistent library (the "catalog") plus the production pipeline (ingest → organize → select → edit → output). The leaf name's slash ("Workflow / Catalog") names two aspects of one Type.

Nearest neighbors suspected up front:
- Photo Editor / RAW Photo Editor (per-image pixel work vs collection-level system of record)
- Photo Culling Application (shoot-scoped decision machine vs library + pipeline)
- Image Viewer (browsing without records)
- DAM / MAM (§27; organizational media governance vs photographer's own production)
- Tethered Shooting Application (capture side)
- Personal Cloud Drive / photo storage (consumer libraries drift toward sync/storage)
- Image Batch Processor (set transformation, no library)

## Research Questions

1. What does the application maintain about each photo, and where does that state live (catalog database, library container, session document, sidecars, cloud)?
2. How do records relate to files (referenced in place, copied into a managed container, held in the cloud)?
3. What organizational structures exist (albums/collections, keywords/tags, ratings/labels, captions, people/places) and how does retrieval work?
4. What is the production cycle and which stages does the application itself carry (ingest, review/select, edit, output/deliver)?
5. Where does editing sit — embedded non-destructive develop with recipes stored in the library, or handoff to external pixel editors?
6. Does the record layer track derived versions (variants, virtual copies, versions)?
7. What happens when files go offline/missing (does the record survive)?
8. Do consumer/platform-native lifetime libraries fit the same Type?
9. Where exactly do the boundaries vs cullers, editors, viewers, and DAM run?

## Representative Products

| Product | Philosophy / segment | Evidence reached |
|---|---|---|
| digiKam (KDE, open source) | Local-first photo management for personal collections; explicitly documents DAM practice for photographers | Tier-1: manual root + Database page + DAM Workflow page + Organize and Find page (strong) |
| Capture One (Phase One) | Professional studio tool; uniquely ships BOTH a lifetime Catalog document and shoot-scoped Session documents | Tier-1: support hub + "Sessions vs Catalogs" + "The concept of variants" + "How to find missing or lost files" (strong) |
| Apple Photos | Platform-native consumer lifetime library (iCloud-backed) | Tier-1: user guide welcome + TOC + Photo library overview + "Where are the items I imported?" (strong) |
| ACDSee Photo Studio Ultimate | Long-running Windows manager family; folder-first posture ("point it at your photos"); self-positions as "DAM & Photo Editing Software" | Tier-2: vendor root + product page (moderate; help center not fetched) |
| Adobe Lightroom Classic | The canonical professional catalog product (market anchor) | **Unreachable: adobe.com product page timed out ×2. No operational claims made; used only as market context.** |

Sample shape: local-first open-source manager + pro session/catalog duality + platform-native consumer library + folder-first commercial manager = 4 philosophies / 4 customer tiers, all with direct evidence. Lightroom enters only as anchor.

## Sources

- digiKam Manual root — https://docs.digikam.org/en/index.html (fetched 2026-09-08)
- digiKam Manual: Database — https://docs.digikam.org/en/getting_started/database_intro.html (fetched 2026-09-08)
- digiKam Manual: DAM Workflow — https://docs.digikam.org/en/asset_management/dam_workflow.html (fetched 2026-09-08)
- digiKam Manual: Organize and Find — https://docs.digikam.org/en/asset_management/organize_find.html (fetched 2026-09-08)
- Capture One support hub — https://support.captureone.com/hc/en-us (fetched 2026-09-08)
- Capture One: Sessions vs Catalogs — https://support.captureone.com/hc/en-us/articles/30041173920029 (fetched 2026-09-08)
- Capture One: The concept of variants — https://support.captureone.com/hc/en-us/articles/360002478437 (fetched 2026-09-08)
- Capture One: How to find missing or lost files — https://support.captureone.com/hc/en-us/articles/30155399342877 (fetched 2026-09-08)
- Apple Photos User Guide (macOS Tahoe) — https://support.apple.com/guide/photos/welcome/mac (fetched 2026-09-08)
- Apple: Photo library overview — https://support.apple.com/guide/photos/photo-library-overview-pht211de786/mac (fetched 2026-09-08)
- Apple: Where are the items I imported — https://support.apple.com/guide/photos/where-are-the-items-i-imported-pht12e7a8015/mac (fetched 2026-09-08)
- ACDSee root — https://www.acdsee.com/en/ and Photo Studio Ultimate product page https://www.acdsee.com/en/products/photo-studio-ultimate/ (fetched 2026-09-08)
- Adobe — https://www.adobe.com/products/photoshop-lightroom-classic.html — **timed out ×2; unreachable this session**

## Product Observations

### digiKam (evidence layer A — official manual, 4 pages)

- Self-positioning: "the free and open source photo management program." A dedicated handbook chapter covers "Digital Asset Management… to Safely Handle Large Digital Photography Collections."
- **Catalog/database as the core** (Database page): "Like other photograph management programs, digiKam uses its database to avoid data duplication, reduce data redundancy, enable fast search… digiKam stores data (including albums, album roots, tags, thumbnails, face recognition data, image metadata, file paths, settings and others) in four databases" — core (albums/images/search), thumbnail (compressed PGF previews), similarity (fingerprints for fuzzy search), face (recognition histograms). Remote MariaDB on a NAS supported. Migration from other software via XMP sidecars (proprietary DBs not parsed).
- **Dual metadata posture** (Organize and Find): "digiKam supports a dual approach of storing image metadata in a database *and* within the image files, guaranteeing ultra-fast search and secure archiving that is easily accessible to other applications." Database-only metadata stays private; embedded metadata becomes public on export — a documented privacy split.
- **Organization as views over the library**: "digiKam provides a number of methods to classify photographs: filenames, albums, collections, time-stamp, tags, rating, GPS position and captions… The metadata categories listed here are in fact different **views** of your photo library." Left sidebar: Albums, Tags, Labels, Dates, Time-Line, Search, Similarity, Map Search, People. Tags are hierarchical and create "virtual albums." Search combines metadata items (camera model, lens, coordinates, image size).
- **Decision/culling vocabulary embedded**: 5-star ratings (6 levels incl. unrated), Color Labels ("can be used to group items for your workflow stages"), **Pick Labels: "Rejected, Pending or Accepted"** — manual or assigned automatically by the deep-learning Image Quality Scanner. Face detection/recognition and auto-tagging as maintenance tools.
- **The full production cycle documented as the DAM Workflow**: import from camera/card reader/scanner → (optionally) convert RAW to DNG into a DNG archive → "Rate and cull, write metadata into the DNG archive" → backup → "Tag, comment, and geo-locate" → "Edit and enhance the photographs" (in-app editor) → "Use external applications for layered editing… re-apply the metadata recorded in the digiKam database to the edited images" → routine backup + integrity checks → watermarking + "Export to web galleries, slide shows, MPEG encode, contact sheets, printing, etc."
- **Handoff both ways**: the database is the metadata authority — after external pixel editing, metadata is re-applied from the digiKam database onto the edited files.
- **Output surfaces**: Export tools to Flickr/Google/Piwigo/Dropbox/Box/OneDrive/local and more; post-processing tools: HTML Gallery, Print Creator, Calendar, Panorama, slideshow tools, Send Images.
- **Maintenance as a first-class area**: Scan for New Items, Database Cleaning, Rebuild Thumbnails, Rebuild Fingerprints, Find Duplicates, Detect and Recognize Faces, Image Quality Scanner, Metadata Synchronizer.
- Batch Queue Manager: queue-based parallel processing of library items (RAW converter, DNG converter, metadata tools, watermark, custom scripts) — set-level transformation embedded as a capability.
- Showfoto: a stand-alone version of the image editor without the library — the vendor's own editor-only sibling, useful boundary evidence.

### Capture One (evidence layer A — official support articles, 3 pages + hub)

- **Two document models, one product** (Sessions vs Catalogs): "Sessions and Catalogs offer two different ways to organize your photos — each with its own strengths depending on how you work." Sessions: "Each Session has its own folder structure so you can keep everything in one place, images, settings, and adjustments. Great for individual shoots or tethered capture." Catalogs: "work more like a library. They're ideal when you want to manage large photo collections over time, especially across multiple shoots… search and organize across different projects."
- **File posture**: "Images could still be referenced from an external drive… While sessions can do that out of the box, for catalogs you need to import images with 'Add to Catalog' option selected in the Import window" — referenced (in place) vs managed (copied) is a documented, product-level choice. Storage guidance: local drives safest; cloud-synced locations "not supported unless syncing is paused"; NAS workable with caveats.
- **One-way conversion**: a Session can be imported into a Catalog, "but not the other way around."
- **Variants = the record-level edit model** (Concept of variants): "observe Capture One as a kind of non-destructive rendering engine… edits are never saved to the original files… When you adjust an image, the instructions are written to a small BLOB of data called settings… a virtual representation of a variant… This concept of a variant exists as a sort of transition from the source file to the output file." Variants "can be copied as many times as you like and can even exist in more than one place (in the form of albums)." Export "combines the original image data and adjustments… and makes a copy in the chosen format that a pixel editor can read."
- **Records survive missing files** (Find missing files): "Capture One doesn't delete or move images on its own." Files moved outside the app show as **offline**; the user remaps them with **Locate**. Deleted items go to the Catalog/Session **Trash** and are recoverable. While a file is missing, the catalog still holds its **previews**, from which a JPEG **QuickProof** can be exported (catalogs only). Filters can hide images by "rating, color tag, or other criteria" — decision state drives visibility.
- **Culling embedded**: the support tree includes a "Culling images" article (referenced; not fetched); the Workflow Basics section ships Compare Variant (Pro/Studio), Open With / Edit With (external pixel editors), RAW handling, variants.
- **Tethered capture** is a first-class support category ("Shooting Tethered — Setup, Workflow and Troubleshooting") — capture-side machinery embedded in the same product.
- Mobile: Session and Catalog documents exist on iPad/iPhone.

### Apple Photos (evidence layer A — official user guide, 3 pages)

- **The library is the system of record**: "When you first use Photos, you create a new library… The System Photo Library is where Photos routinely stores and accesses your photos." Additional libraries can be created and switched; iCloud Photos syncs only from the System Photo Library; library-level backup and **Repair** machinery documented.
- **Managed container posture**: "New photos and videos that you add to Photos are stored in this library… **You should only use the Photos app to access the photos and videos in a library.** WARNING: … do not manually access or alter the contents of a library in the Finder. If you want to copy, move, or transfer files, first export them from the library." — the inverse of the referenced-file posture: the container, not the folder, is canonical.
- **Guide structure = the consumer pipeline**: Import (camera/phone, storage devices, Mail/Safari/other apps, another photo library) → View and find (browse library/collections; find by date, people and pets, location, media type; filter and search; Live Text; remove duplicates; titles/captions/keywords) → Albums and Memories (albums, folders, **Smart Albums**, auto-curated Memories) → Edit (adjustments, filters, crop; **"Use other apps when editing in Photos"** — external editor extensions) → Share (shared albums, iCloud Shared Photo Library) → Export → Slideshows and projects → Print your own / order professional prints → Manage your photo library.
- Consumer auto-organization: people/pets, places, trips, media types, Memories ("intelligently curates your photos and videos") — organization largely automatic rather than user-built.
- iCloud storage optimization ("Store full-resolution photos and videos in iCloud") — the record layer can outlive the local file.

### ACDSee Photo Studio (evidence layer A- (product page, Tier-2))

- Self-positioning: "DAM & Photo Editing Software"; "File Management Software — ORGANIZATION | FACIAL RECOGNITION | SEARCHING"; "ACDSee has been leading the industry in digital asset management and creative editing software for over 30 years."
- **Folder-first catalog posture**: "Unlike the Adobe® products, ACDSee Photo Studio does not require you to laboriously import photo collections. Simply install ACDSee on your hard-drive and point it to your photos." — an explicit anti-import posture in the same family, showing the record layer need not require a copy-in import step.
- "ACDSee Photo Studio Ultimate 2027 brings your entire photo workflow into one place."
- **Library-building machinery**: "Ratings, keywords, categories, and color labels turn a folder of files into a library you can actually search." Activity Manager runs background jobs (indexing for AI Image Similarity, AI Keywords). AI Face Detection & Recognition "find and name faces… suggest matches you can accept or reject in batches."
- **Culling vocabulary embedded**: new **Reject Tag** ("Mark blinks, blurs, and duds… then pull up your rejects and clear them out in a single pass"), ratings, **stacking** (Auto-Stack by GPS/capture time/visual likeness; Custom Stacking; "Nothing is deleted, and nothing is merged"), Group By AI Image Similarity, AI Reverse Image Search ("no tagging, no keywords, no setup").
- **Editing embedded**: non-destructive RAW develop ("apply powerful adjustments without ever touching the original file"), layered editing, AI filters — plus a separate editor product (Gemstone) in the same family.
- 750+ RAW camera models claimed (marketing figure — not repeated in the final doc).

### Adobe Lightroom Classic (no direct evidence — anchor only)

- Unreachable (2 timeouts). Market standing taken as context only (the canonical catalog workflow product; ACDSee's migration page and Capture One's market position both treat it as the reference competitor). No operational claims recorded here.

## Cross-product Comparison

| Dimension | digiKam | Capture One | Apple Photos | ACDSee Photo Studio | Common? |
|---|---|---|---|---|---|
| Persistent record layer over the photos | 4 databases (albums/images/search; thumbnails; similarity; faces); metadata dual DB+file | Catalog (library DB) **or** Session document (per-shoot folder with settings DB); backups documented | System Photo Library container (+ optional additional libraries); backup/repair | indexing DB over in-place files ("turn a folder of files into a library") | **Common — the layer exists in all; container form varies (DB / library container / session document)** |
| Files vs records | files stay on disk; file paths in DB; metadata optionally embedded (XMP/IPTC) | referenced (in place) or managed (copied in); offline images keep records + previews | copied into managed library; "only use the Photos app to access" | files stay in place; DB indexes | **Common; referenced/managed/cloud is the variant axis** |
| Records survive file problems | DB re-apply metadata onto externally edited files; maintenance/rescan tools | offline images + Locate remap; Trash recovery; QuickProof from previews | iCloud optimization (local file may be downsampled); Repair library | Activity Manager re-indexing | **Common (mechanisms differ)** |
| Organization structures | albums, collections, hierarchical tags → virtual albums, dates/timeline, ratings, color labels, pick labels, captions, geolocation, people | albums, smart albums, session folders/albums; search "across different projects" | albums, folders, Smart Albums, keywords, titles/captions, people/pets, places, media types | categories, keywords, ratings, color labels, stacks | **Common; auto-organization strongest in consumer pole** |
| Retrieval over the whole library | search by camera/lens/coordinates/size; filters; similarity (fingerprints); map search | search + filters (rating/color tag) across the document | filter/search by date/people/place/media; visual search (Live Text/Look Up) | search/sort; AI reverse image search; group by similarity | **Common** |
| Selection/culling vocabulary embedded | Pick Labels (Rejected/Pending/Accepted) + ratings + color labels; auto quality scan | "Culling images" article; Compare Variant; filters by rating/color tag | favorites/curated Memories (weakest) | Reject Tag + ratings + Auto-Stack | **Common in pro/enthusiast poles; consumer pole reduces it to favorites** |
| Editing stage | built-in Image Editor; Batch Queue Manager; handoff to external layered editors with metadata re-sync | non-destructive develop in-app; Open With/Edit With to pixel editors; export "a copy… a pixel editor can read" | built-in editor; "Use other apps when editing in Photos" | non-destructive RAW develop + layered editing in-app | **Common — in-app editing plus a documented external-editor seam** |
| Non-destructive edit recipes in the record layer | metadata workflow; settings in DB | variants = adjustment "settings" blobs; "transition from the source file to the output file" | non-destructive edits in library (revertible) | "without ever touching the original file" | **Common (all 4 sampled)** |
| Derived versions tracked | Versions view (right sidebar) | variants copied "many times… even in more than one place (albums)" | — (edits implicit; no variants concept documented) | stacks ("best shot on top… Nothing is deleted") | Common in pro/enthusiast poles; not universal |
| Output/delivery | export to services; HTML gallery; Print Creator; slideshows; contact sheets; send images | process/export recipes; QuickProof | share, shared albums, export, slideshows, print/order prints | export; SendPix | **Common** |
| Capture-side integration | import from camera/card/scanner/remote/Google/SmugMug | tethered capture (dedicated category); mobile capture | import from camera/phone/storage; iCloud auto-import | Mobile Sync from phone | **Common** |
| Catalog maintenance | scan new items, DB cleaning, rebuild thumbs/fingerprints, duplicates, metadata sync | catalog backups; cache; locate | repair, backup, optimize storage | background indexing | **Common** |
| Scope posture | whole-collection | lifetime Catalog OR per-shoot Session (both first-class) | lifetime library | whole-collection (folder-first) | **Variant: lifetime vs per-shoot container — both in-sample, so lifetime scope is NOT definitional** |
| AI layer | face recognition, quality scan, auto-tags | — (not on fetched pages) | Memories curation, people/pets, Live Text | AI keywords, faces, similarity, generative tools | Variant (era-current; strongest in consumer/auto poles) |
| Explicit import step | yes (import tools) | yes for catalogs; sessions create in place | yes (or automatic via iCloud) | explicitly NOT required ("point it to your photos") | **Variant — import-as-operation is NOT definitional; the record layer is** |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal; three jointly-held structures)

1. **The photo collection as the application's library of record.** The application maintains persistent records about the photographer's photos — identity, metadata, organizational state — held across sessions and shoots, over and above the image files themselves. The files are referenced in place, held in a managed library container, or stored in a cloud library; the records persist, accumulate, and (documented in-sample) can even outlive the file's location (offline images, remapping, cloud-optimized storage). Remove → an image viewer / file browser: browsing without a record layer.
2. **Organization-and-retrieval as a standing surface over the whole collection.** The user builds and uses structure — albums/collections, keywords/tags, ratings/labels, captions — and searches/filters across the entire library rather than one folder; modern products add automatic structure (people, places, similarity). Remove → an importer with a flat list; the collection cannot be managed.
3. **The photographic production cycle as the application's job.** The library exists to carry photos through the cycle: ingest from camera/card/mobile, review and select, develop/edit (in-app or handed to external editors), and output/deliver (export, share, print, publish) — with the record layer tracking each photo's state and derived versions along the way. Remove → a passive archive/organizer; the "workflow" is gone.

Jointly-held is load-bearing: 1 alone = file browser; 2 without 1 = a tag editor on loose files; 3 without 1+2 = a batch converter with a UI; 1+2 without 3 = a passive archive (below the Type — the market's managers always ship the production stages); 2+3 without 1 = per-folder tools (culler/batch-processor territory).

Notes on deliberate exclusions from L0 (anti-overfitting):
- **Lifetime/cross-shoot scope is NOT invariant**: Capture One ships shoot-scoped Session documents as a first-class alternative to Catalogs, and the vendor's own framing ("manage large photo collections over time, especially across multiple shoots" for Catalogs) describes the catalog pole of a scope gradient, not the Type's floor. What is invariant is the record layer, whatever its scope.
- **An explicit import step is NOT invariant**: ACDSee explicitly requires none ("point it to your photos"); iCloud auto-imports. The invariant is the resulting record layer, not the intake ceremony.
- **Embedded editing is NOT invariant as a depth matter** (the seam vs Photo Editor is center of gravity), but *an editing-and-output stage in the cycle* is: every sampled product carries one, in-app or handed off.

### L1 — Common Mature Structure

- ingest/intake machinery (camera/card/scanner/mobile/cloud; optional rename, conversion, backup-on-import)
- preview generation so the library browses without touching originals
- non-destructive editing with recipes stored in the record layer (adjustment instructions re-applied on render/export)
- derived versions/variants (virtual copies, version stacks) tracked per photo in pro/enthusiast poles
- decision vocabulary embedded as one stage of the cycle (ratings, color labels, pick/reject flags)
- similar-shot comparison (light table, compare variants, stacks)
- automatic organization (face detection/recognition, places/geolocation, duplicates, similarity, quality assessment)
- in-app editing plus a documented external-editor seam (Open With / Edit With / extensions)
- output machinery: export recipes, web galleries, slideshows, print/books, service publishing
- catalog maintenance: backup, repair, rebuild previews/index, duplicate finding, metadata sync
- batch/set-level processing as a capability (queue managers, batch export)

### L2 — Variant / Optional

- scope posture: lifetime catalog vs per-shoot session documents vs folder-first whole-collection
- file posture: referenced-in-place vs managed/copy-in container vs cloud-held
- tethered capture module (→ Tethered Shooting Application when it is the product's center)
- RAW-development depth (→ RAW Photo Editor when central)
- DAM-flavored depth: DNG archiving, authorship/copyright fields, data-integrity doctrine
- consumer lifetime-library pole: memories curation, shared/family libraries, storage optimization, messaging-adjacent sharing
- platform delivery: local-first/open-source, commercial desktop, platform-native, cloud service
- AI layer: auto-tagging, similarity/reverse-image search, generative editing
- mixed media (video, Live Photos) riding in the same library
- team/workgroup editions (ACDSee Workgroup/Enterprise naming observed)

### L3 — Vendor-specific (research notes only)

- digiKam: four-database split (core/thumbnail PGF/similarity fingerprints/face histograms), remote MariaDB hosting, metadata privacy doctrine (DB-private vs embedded-public), Pick Label vocabulary, Image Quality Scanner, DNG-archive workflow step, KML export, Showfoto stand-alone editor, Batch Queue Manager with custom scripts.
- Capture One: Session folder structure doctrine, Session→Catalog one-way import, "Add to Catalog" vs referenced import, EIP packages, QuickProof export, Compare Variant (Pro/Studio tier), cloud-sync/NAS storage guidance, iPad/iPhone session documents.
- Apple: System Photo Library concept, iCloud-only-from-System-Library sync rule, Finder-access warning, iCloud Shared Photo Library, Memories/Personalize memories, Live Text/Visual Look Up.
- ACDSee: Activity Manager, Light EQ, Auto-Stack thresholds/presets, AI Reverse Image Search, SendPix, Photoshop/Lightroom migration page, Workgroup/Enterprise editions.

## §24 Historical / Market-Sample Check

Question: would older, regional, platform-native, differently-positioned products still fit the L0?

- **Analog antecedent (conceptual)**: the photographer's working archive — labeled binders/albums of sleeves, contact sheets with grease-pencil selection marks, caption notes, and prints produced from selected frames. Library of record (the binder with its organizational scheme), organization-and-retrieval (labels/index), production cycle (select → develop/print → deliver). Satisfies all three legs at analog level.
- **2000s desktop photo-manager generation (conceptual — no primary source reachable this session; Wikipedia-class sources timed out in sibling passes)**: camera import wizard → albums → tags/ratings → red-eye/quick-fix editing → share/export/burn. Satisfies the three legs with no cloud, no AI, no RAW variants, no non-destructive recipe model. The definition does not depend on any modern mechanism.
- **Platform-native consumer libraries** (Apple Photos — directly documented): satisfy; the pipeline is realized as light edit + share/print rather than shoot-to-delivery. The consumer pole is in-Type.
- **Shoot-scoped session documents** (Capture One Sessions — directly documented): satisfy with scope = one shoot container; confirms lifetime scope is not definitional.
- **Folder-first managers** (ACDSee — directly documented): satisfy without a copy-in import ceremony; confirms import-as-operation is not definitional.

Conclusion: historical check passed. The L0 names no database technology, no import ceremony, no lifetime scope, no RAW, no AI, no cloud.

## Vendor-specific Findings

See L3. Additional: ACDSee's explicit "no import required" marketing is itself evidence about the market's self-definition (the competitor contrast with Adobe frames import-ceremony as the variable). digiKam's handbook devotes a chapter to "Digital Asset Management" for personal photo collections — the market itself blurs the DAM vocabulary at the individual scale, which the boundary section must handle.

## Boundary Findings

| Neighbor | Distinction | "Remove what → becomes the other Type" |
|---|---|---|
| Photo Editor / RAW Photo Editor | the editor's unit of work is the single image being transformed; no standing record layer over the collection is required to be an editor. Pro products bundle both (ACDSee Ultimate, Capture One, Lightroom) — bundling is packaging, not Type identity. | remove library + cycle → the editing core remains a Photo Editor; make RAW development the center → RAW Photo Editor |
| Photo Culling Application | shoot-scoped decision machine; its only output is the selection set; dedicated cullers are catalog-free ("no intermediate catalogues"). Catalog apps embed the same decision vocabulary as one stage among several (digiKam Pick Labels; Capture One "Culling images" article; ACDSee Reject Tag). | remove the record layer + edit/output stages → culler; add them → this Type. **Keep-both RATIFIED** — the dedicated-culler segment persists in the market |
| Image Viewer | displays photos; no record layer, no cycle | remove records + production stages → viewer |
| Image Batch Processor | set-level content transformation without a library; embedded in this Type as a capability (digiKam BQM) | remove library + per-photo records → batch processor |
| DAM / MAM (§27) | organizational media governance across teams, asset types, and lifecycle (ingest→archive→rights→distribution); this Type is one photographer's (or household's) photo production. Vendor vocabulary overlaps (ACDSee/digiKam self-describe as DAM) | widen to org-wide multi-stakeholder media governance → DAM/MAM |
| Tethered Shooting Application | capture-side camera control is the job; here it is one intake mode (Capture One embeds tethering as a support category) | make camera control the center → Tethered Shooting |
| Personal Cloud Drive / photo storage | storage/sync/file access is the center; no photographic production machinery. Consumer photo libraries sit near this seam (Google Photos pole NOT verified this pass — no source reachable) | remove edit/output machinery + photographic organization → file-drive territory |
| Photo-centric Social Network | distribution loop runs through person-ties and publication; here sharing is an output stage of the production cycle | make the social loop the center → photo-centric social network |

**Joint-review discharges (both recorded from this side):**
1. photo-culling-application flag: keep-both ratified. Shared vocabulary (ratings/labels/pick-reject) confirmed inside catalog-class products (digiKam Pick Labels "Rejected/Pending/Accepted"; ACDSee Reject Tag; Capture One culling article) — but scope (shoot batch vs collection library) and output (selection set vs full production cycle) separate the Types; the market persistently sells dedicated cullers.
2. photo-editor flag: ratified from this side — the library + cycle are what this Type adds over editing; removing them leaves a photo editor's core. Same for RAW development depth (→ raw-photo-editor when central).

## Uncertainties

1. **Adobe Lightroom Classic unreachable** (2 timeouts). The canonical catalog product is documented here as market context only; no operational claims. The catalog/variants/offline behaviors are evidenced from the other sampled products instead.
2. **Capture One "Culling images" and "Complete Guide to Catalogs/Sessions" articles not fetched** (referenced from section pages only); culling-embedded evidence for C1 rests on the article listing + filters-by-rating/color documentation.
3. **Consumer cloud-library pole (Google Photos-class) not verified** — no source fetched; the consumer-pole evidence is Apple-Photos-based. Boundary wording vs file-drive territory kept conservative.
4. **referenced-vs-managed Catalog detail** (Capture One) taken from the Sessions-vs-Catalogs article + the existence of a dedicated "referenced vs managed" article (title only); not the article body.
5. Marketing figures (ACDSee "750+ RAW models", "30 years") not repeated as facts in the final document.
6. Whether "photo organizer/manager" deserves its own Type was considered: no such leaf exists in DIRECTORY.md; the consumer lifetime-library pole is documented here as a variant. Flagged in STATUS.md Boundary Issues for a future taxonomy pass.

## Final Synthesis

A Photo Workflow / Catalog Application is the photographer's system of record for a photo collection and the vehicle for its production cycle. Its floor is three jointly-held structures: (1) a persistent record layer the application itself maintains over the photos — whatever the container (catalog database, managed library, session document, cloud library) and whatever the file posture (referenced, managed, cloud-held); (2) organization-and-retrieval as a standing whole-collection surface (albums/tags/ratings/captions + search, increasingly auto-built); (3) the photographic production cycle — ingest, select, edit (in-app or handed off), deliver — tracked in the record layer, which also accumulates derived versions and survives file moves, offline drives, and cloud optimization. Scope can be lifetime or per-shoot; import can be a ceremony or a formality; editing can be native or handed off — none of that moves the Type. What moves it: strip the record layer → viewer/browser; strip the cycle → passive archive; shrink to a shoot-scoped decision machine → culler; make the single image the unit → editor; make camera control the unit → tethered shooting; widen to org-wide multi-asset governance → DAM.
