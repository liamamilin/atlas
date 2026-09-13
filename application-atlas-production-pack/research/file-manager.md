# Research Notes — File Manager

## Research Goal

Understand what a File Manager actually is as an Application Type: what objects it operates on, what it presents, what operations define it, how it differs from cloud-storage / sync / transfer / content-library siblings (§03.15 Files family), and how much of the modern feature surface is definitional versus common or optional.

## Initial Boundary

- Assumed core: browsing, organizing, and operating on files/folders on real storage — navigation, views, copy/move/rename/delete.
- Most-likely confusions (checked in this pass):
  - **Personal Cloud Drive** (sibling, 03.15): storage service + sync; a file manager *browses* storage but provides no storage service.
  - **File Sync Application** (sibling): consistency engine between locations; not a browsing surface.
  - **File Transfer Application** (sibling): point-to-point sending, not organization.
  - **E-book Library Application** (already documented): explicitly drew the line — "file managers operate on files; the library operates on books" (research/e-book-library-application.md).
  - **Construction Document Management** (already documented): "personal or org-internal storage without register/revision/distribution semantics" (research/construction-document-management.md).
  - **Image Viewer / PDF reader**: single-file content rendering, not storage organization.
- Unknowns at start: whether cloud-adjacent and mobile file managers change the core; whether tags/smart folders are definitional; how the platform-native vs third-party split affects the model.

## Research Questions

1. What does a file manager present — a curated catalog or the actual content of storage?
2. What are the core objects (file, folder, volume/location, path) and their relationships?
3. Which operations are definitional (create/copy/move/rename/delete…), and which are optional?
4. How do navigation surfaces work (sidebar, address bar/path, tree, tabs, dual pane)?
5. How do views/sorting/grouping present files, and by which attributes?
6. Where does search sit (name/attribute vs content)?
7. How do annotation layers (tags, smart folders, aliases/shortcuts) relate to the underlying storage — do they replace the hierarchy or overlay it?
8. What do power-user variants add (dual-pane, batch rename, sync/compare, archives, FTP/remote locations)?
9. How does the mobile form factor realize the same core?
10. Where are the hard boundaries vs Personal Cloud Drive / File Sync / File Transfer / content libraries / document management?

## Representative Products

Selection logic: market dominance + different product philosophy + different platform + different customer tier + documentation quality.

| Product | Family / philosophy | Tier / platform | Docs examined |
|---|---|---|---|
| Windows File Explorer | platform-native incumbent | consumer + enterprise, Windows | Microsoft Support "File Explorer in Windows" |
| Finder (macOS) | platform-native, folder/tag/smart-folder philosophy | consumer + professional, macOS | Apple Mac User Guide: "Use the Finder on Mac", "Organize files in folders on Mac" |
| Files (Apple, iOS) | platform-native mobile | consumer, iPhone | Apple iPhone User Guide: "Files basics" (+ section list of Files pages) |
| Total Commander | third-party power-user dual-pane, shareware | power users, Windows (since Win 3.1) | ghisler.com home + full feature list |
| Files (Files Community) | third-party modern open-source file explorer | prosumer, Windows | files.community home + docs (cloud drives, tags, dual pane) |

Non-examined market mentions: Files by Google (Android; help center and product page both timed out twice — see Source-access Limitation), Linux desktop managers (GNOME Files, KDE Dolphin), terminal/TUI managers (Midnight Commander, ranger), web file browsers embedded in cloud consoles.

## Sources

Evidence layers: **A** = directly observed on one product's official documentation; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison and boundary reasoning.

1. **Microsoft Support — "File Explorer in Windows"** (Win 10/11). https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows — fetched 2026-09-07. [A]
2. **Apple Support (Mac User Guide) — "Use the Finder on Mac"** (macOS Tahoe 26 guide). https://support.apple.com/guide/mac-help/organize-your-files-in-the-finder-mchlp2605/mac — fetched 2026-09-07. [A]
3. **Apple Support (Mac User Guide) — "Organize files in folders on Mac"**. https://support.apple.com/guide/mac-help/organize-files-with-folders-mh26885/mac — fetched 2026-09-07. [A]
4. **Apple Support (iPhone User Guide) — "Files basics"** (iOS 26 guide). https://support.apple.com/guide/iphone/files-basics-iphe9d46e90f/ios — fetched 2026-09-07. [A]
5. **Total Commander — home page + feature list** ("file manager for Windows 3.1 through 11"). https://www.ghisler.com/ and https://www.ghisler.com/featurel.htm — fetched 2026-09-07. [A]
6. **Files Community — home + documentation**: Overview; Cloud drives (https://files.community/docs/features/cloud-drives); Tag files and folders (https://files.community/docs/features/tags); Dual pane (https://files.community/docs/features/dual-pane) — fetched 2026-09-07. [A]
7. **Bing search result snippet for files.google.com** ("Get personalized space clean-up suggestions for unused apps, large or duplicate files…") — seen 2026-09-07; product page itself unreachable. [A-weak, single snippet]

**Source-access Limitation**: Google's help center (support.google.com/files) and product page (files.google.com) timed out twice each. No Android file manager was directly examined. Mobile conclusions rest on iOS Files; Android-specific behavior (storage scopes, permission model) is not asserted in the final document. Microsoft's own support-site search and Apple guide TOC pages were used only for discovery/section titles.

## Product Observations

### Windows File Explorer (Microsoft Support)

- Definition on the page: "Windows File Explorer helps you find, open, organize, and manage files and folders on your PC and in the cloud." [A]
- Navigation: left navigation pane; address bar; **Up** arrow navigation buttons; default landing page is **Home** (formerly Quick access) or optionally **This PC** ("focused on your PC's drives and network locations"). [A]
- Quick access: known folders (Desktop, Documents, Downloads, Pictures, Music, Videos) pinned by default; users pin/unpin any folder; frequent folders + recent files listed (Win 10: "recently used files are listed there, so you won't have to dig through a series of folders"). [A]
- Operations: **Cut / Copy / Paste / Rename / Delete** at the top of the context menu; move = Cut then navigate then Paste; **Share** from the ribbon / Share tab (hand-off to apps). [A]
- Views: "choose between showing icons, lists, details, and more"; **Compact view**; **Item check boxes** for selection. [A]
- Storage attributes surfaced: **show file name extensions**; **show hidden files**. [A]
- Cloud: "find relevant files from your PC and the cloud" via search from Home (requires signing into cloud accounts); "OneDrive is a part of File Explorer" (Win 10) — cloud storage appears inside the manager as locations. [A]
- Libraries (Win 10): virtual aggregated folders, hidden by default, opt-in in the left pane — an optional overlay, not the primary structure. [A]

### Finder (macOS, Apple Mac User Guide)

- Definition: "You can use the Finder to view, access, and organize almost everything on your Mac." [A]
- Sidebar (customizable) lists apps, documents, downloads, etc.; **Preview pane** to view a document/image without opening it. [A]
- View modes: list and **Gallery** ("flip through your files and folders visually"); sort and group (e.g., group by Date Last Opened; folders kept at top). [A]
- Organization: "Organize with folders and tags" — tags = keywords attached to files/folders, locatable by search or via the tag in the sidebar; **Smart Folder** "automatically collects documents based on criteria you set" (e.g., all spreadsheets, all documents with a phrase in the title) — a saved search, not a moved file. [A]
- Item-level machinery: aliases (shortcuts placed elsewhere that open the item), custom icons for files/folders. [A]
- iCloud Drive storage and iPhone/iPad sync appear in the sidebar; AirDrop for sending items to nearby devices. [A]
- "Organize files in folders on Mac": "Everything on your Mac—documents, pictures, music, apps, and more—is organized in folders." Create folder (File > New Folder); **"If the New Folder command is dimmed, you can't create a folder in the current location"** — location permission/state rule surfaced in the UI. [A]
- Move/copy semantics are drag-based with modifier keys: drag = move; Option-drag = copy; Option-Command-drag = alias; drag to another disk = copy; Command-drag to another disk = move; **Duplicate** (Command-D) copies in place; **New Folder with Selection** groups items into a new folder; **Merge** two same-named folders via Option-drag ("Merge option appears only if one of the folders contains items that are not in the other"; with conflicting same-named files only Stop or Replace). [A]
- See-also links: Get file, folder, and disk information; Rename; Delete files and folders; Restore files (recoverable delete). [A — titles only]

### Files (Apple, iPhone User Guide)

- Definition: "In the Files app, you can locate and view your files, organize and rearrange them in folders, compress, rename, and share them with friends, transfer them to and from iCloud Drive and other devices, and more." [A]
- Surface: **Browse** tab with sidebar locations (Downloads, iCloud Drive); **Recents** ("files you opened recently"); **Shared**; touch-and-hold a file or folder → **Copy / Move / Share / Delete**. [A]
- Section titles of the Files chapter document the mobile operation set: Modify files and folders; Find and view files and folders; Find your downloaded files; Organize files and folders; Send files from the Files app; Set up iCloud Drive; Share files and folders in iCloud Drive; **Transfer files from iPhone to a storage device, a server, or the cloud**. [A — titles]

### Total Commander (ghisler.com)

- Positioning: "file manager for Windows 3.1 through 11" — a third-party manager sold into the platform that already ships one, in continuous commercial life since 1993. [A]
- Layout philosophy: "**Two file windows side by side**"; tabbed interface; history + favorites buttons; thumbnails view; **custom columns**; separate trees. [A]
- Operations machinery: "Extended copying, moving, renaming and deleting of entire trees"; **Multi-rename tool** (rename many files with rules or by editing names in a text editor); select/restore selection; show/select files "with specific search pattern, size, date or contents". [A]
- Search: "Enhanced search function with full text search in any files across multiple drives, even inside archives"; duplicate-file search. [A]
- Archives: "Archives are handled like subdirectories. You can easily copy files to and from archives"; built-in ZIP packer; internal unpackers for common formats; background packing. [A]
- Remote locations: built-in FTP client (FTPS, FXP, resume, background download list) — remote servers are browsable locations. [A]
- Utilities adjacent to management: compare files by content; **synchronize directories** (with subdirs, or a directory with a ZIP); split/combine big files; encode/decode UUE/XXE/MIME; built-in viewer (Lister: text/hex/binary of any size); command line; configurable button bar. [A]

### Files Community (files.community)

- Positioning: "A sleek, open-source file explorer built for Windows, designed to help you organize files and folders with ease" — a third-party replacement for the platform-native manager on the same platform. [A]
- Navigation multitasking: tabs ("manage multiple folders within a single window"); **dual pane** ("view two different locations within the same tab… ideal for comparing folder contents, transferring items between directories"); **column view** ("navigate through different levels of the file system"); omnibar; command palette. [A]
- **Tags**: assign one or more tags to any file or folder; filter/sort/search by tag (`tag:Photos` syntax); tag column in details view; tags widget. Implementation note (product-specific): "Tags are saved using alternate data streams (and not in a database)… allows items to be transferred between locations (even without using Files) without losing their tags"; "Tags only work on drives formatted as NTFS"; "may not work with all cloud storage providers"; tag definitions are exportable/importable per device. [A]
- **Cloud drives**: "Files integrates with various cloud providers by detecting and displaying their drives in the sidebar. These integrations require their respective clients to be installed and running on the device" (OneDrive, Google Drive, iCloud, Box, Dropbox, Mega, Nextcloud, …) — the manager browses cloud storage mounted by the provider's client; it does not provide the storage. [A]
- Other: preview pane; QuickLook/SeerPro spacebar previews; create/extract archives (zip, WinRar, 7zip); Git integration ("manage your Git projects… without leaving Files"); hashes in properties; remappable keys; toolbar customization; folder backgrounds; layout picker. [A]

## Cross-product Comparison

| Structure | Explorer | Finder | iOS Files | Total Commander | Files Community | Layer |
|---|---|---|---|---|---|---|
| Presents actual storage content (drives/locations, everything incl. hidden) | ✔ ("This PC… drives and network locations"; show hidden) | ✔ ("almost everything on your Mac") | ✔ (iCloud Drive, Downloads, device) | ✔ (network neighborhood, drives) | ✔ (drives sidebar; cloud clients mounted) | B |
| Navigable hierarchy: panes/sidebar + path/address + into/up navigation | ✔ (nav pane, address bar, Up) | ✔ (sidebar) | ✔ (Browse sidebar) | ✔ (dual panes, tabs, trees) | ✔ (tabs, dual pane, column view) | B |
| File + folder as unit, organized in folders | ✔ | ✔ ("Everything… organized in folders") | ✔ ("organize and rearrange them in folders") | ✔ | ✔ | B |
| Operations on stored items: copy/move/rename/delete (+ new folder) | ✔ (context menu) | ✔ (drag-modifier semantics) | ✔ (touch-and-hold) | ✔ (extended, whole trees) | ✔ (context menu) | B |
| Storage-attribute presentation: name/type/size/dates; extension & hidden toggles | ✔ | ✔ (Get Info; sort by Date Last Opened) | ✔ | ✔ (size/date/pattern select; custom columns) | ✔ (details view; hashes) | B |
| Multiple view modes (icons/list/details/gallery-columns) | ✔ | ✔ (Gallery) | (list/browse; not page-level) | ✔ (thumbnails, custom columns) | ✔ (layout picker, column view) | B |
| Selection + context/ribbon/touch menu as command surface | ✔ | ✔ | ✔ (touch-and-hold) | ✔ (command line, button bar) | ✔ (context menu, command palette) | B |
| Frequent/recent surfaces (Quick access / Recents) | ✔ | (Recents in sidebar — general macOS knowledge, not page-verified) | ✔ (Recents tab) | ✔ (history+favorites) | (not page-verified) | B-partial |
| Search by name/attributes | ✔ (PC + cloud) | ✔ (tags, Smart Folders) | (not page-verified) | ✔ (full-text, duplicates) | ✔ (`tag:` search) | B |
| Preview / built-in viewer | (not page-verified) | ✔ (Preview pane) | (not page-verified) | ✔ (Lister) | ✔ (preview pane, QuickLook) | B |
| Trash / recoverable delete | (page references delete; recycle semantics not page-verified) | ✔ (Restore files link) | (not page-verified) | (not page-verified) | (not page-verified) | B-weak |
| Archive handling (compress/extract; archives as folders) | (not page-verified) | (not page-verified) | ✔ (compress) | ✔ (archives as subdirectories) | ✔ (create/extract) | B |
| Cloud/network locations as first-class browsing targets | ✔ (PC + cloud search; OneDrive part of Explorer) | ✔ (iCloud Drive in sidebar) | ✔ (iCloud Drive) | ✔ (FTP client) | ✔ (cloud drives sidebar) | B |
| Tags/labels attached to files or saved searches | (not in page) | ✔ (tags + Smart Folders) | (not page-verified) | (not in list) | ✔ (tags, NTFS ADS) | B-partial |
| Dual-pane / two locations side by side | — | — | — | ✔ (core layout) | ✔ (optional) | B (variant-defining for power-user family) |
| Batch rename by rules | (not in page) | (not in page) | (not in page) | ✔ (multi-rename tool) | (not in page) | A (single product in sample) |
| Directory compare / sync | — | — | — | ✔ (synchronize directories) | (Git integration adjacent) | A |
| FTP/remote-server connection | (network locations in This PC) | (servers connect — not page-verified) | ✔ (transfer to a storage device, a server, or the cloud) | ✔ (FTP/FTPS/FXP) | ✔ (FTP docs page) | B |
| Storage clean-up suggestions | — | — | — | — | — | A-weak (Files by Google snippet only) |

## Canonical Model

### L0 — Defining Invariant

Three properties. Remove any one and the application stops being recognizable as a file manager.

1. **A navigable view over an actual storage hierarchy.** The manager presents the real folder structure of one or more storage locations the user's device can reach — local disks, removable media, network shares, cloud-synced or cloud-hosted locations, connected devices. It mirrors what is stored (including items the user did not place there and may not have known about — hence hidden-item toggles), rather than maintaining a catalog of items the user registered. Remove → a library/catalog application (which shows only registered items with content semantics) or a launcher.
2. **File and folder as the unit of operation, addressed by storage attributes.** Items are identified, sorted, grouped, and found by name, kind/type, size, timestamps, location — attributes that come from the storage layer, not from content meaning. Remove → a content-specific organizer (photo/music/book library).
3. **Storage-mutating operations on the items themselves.** Create folder, copy (with in-place duplicates), move, rename, delete — applied to the actual stored objects, so the manager's actions change what the storage contains. Remove → a viewer/browser that renders files without managing them (image viewer, web file listing).

### L1 — Common Mature Structure

Present in nearly all mature modern products; not required for the Type:

- sidebar/places navigation (known folders, drives, saved locations, favorites/pins)
- path/address display; up navigation
- multiple view modes with sort/group; details/columns with attribute toggles (extensions, hidden items)
- multi-select + context/ribbon/touch menus as the command surface; clipboard-style move/copy
- search over names/attributes (content search in some)
- frequent/recent surfaces
- preview pane or built-in viewer
- item properties (size, dates, attributes; hashes in some)
- recoverable delete (trash/recycle) in desktop products
- archive compress/extract, often treating archives like folders
- cloud and network locations surfaced as ordinary browsing targets
- tabs and/or multiple windows for parallel locations

### L2 — Variant / Optional Structure

- **Platform-native vs third-party**: bundled with the OS (Explorer, Finder, iOS Files) vs independently installed on top of the platform's own manager (Total Commander, Files Community) — same core, different posture.
- **Power-user orientation**: dual-pane as the primary layout, keyboard-driven control, batch rename by rules, directory compare/synchronize, selection by pattern/size/date, file splitting, checksums, FTP/FTPS with server-to-server transfer.
- **Mobile form factor**: Browse/Recents/Shared tab structure, provider-aggregated locations, touch-and-hold menus, transfer to external devices/servers.
- **Cloud integration posture**: cloud storage appears as browsable locations (via provider client or account sign-in); degree of integration varies; the manager itself provisions no storage.
- **Annotation overlays**: tags/keywords attached to files, saved searches/Smart Folders, aliases/shortcuts, virtual libraries — always layered over the hierarchy, never replacing it (a tag search is a query over real files; an alias points at a real file).
- **Storage-management assistance**: clean-up suggestions for large/duplicate/unused items (documented only as a market mention for one product in this sample — optional).
- **Embedded adjacent utilities**: Git integration, hashes, encode/decode, file splitting — power-user conveniences, not structural.

### L3 — Vendor-specific Detail (kept out of the final document)

- Files Community stores tags in NTFS alternate data streams (transfers with the item; NTFS-only; may not survive some cloud providers); tag definitions exported via settings import/export.
- Total Commander ships a ZIP-compatible packer based on ZLIB/libdeflate, FXP server-to-server transfer, direct cable/parallel-port transfer, UUE/XXE/MIME codecs, >259-character name support.
- Windows Quick access: known folders pinned by default since Win 11 22H2; default landing page configurable (Home vs This PC); Win 10 Libraries hidden by default.
- macOS drag-modifier copy/move/alias matrix; Merge appears only when folder contents differ, otherwise Stop/Replace.
- Total Commander product-span claim "Windows 3.1 through 11"; versions and dates from ghisler.com (11.58, July 2026).
- Finder's device-sync module in the sidebar (historically iTunes' role).

## Historical / Market-Sample Check

Asked: would older, regional, platform-native products still fit the L0?

- 1980s desktop/TUI managers (pre-GUI era: DOS-era shells, XTree-class listers, Norton Commander-class dual-pane tools; early Mac Finder 1984) — navigable storage view over a real hierarchy + attribute-addressed copy/move/rename/delete, without tags, search, preview, or cloud. **Fit.**
- Linux desktop and terminal managers (GNOME Files, Dolphin, Midnight Commander-class) — same core over Unix hierarchies and remote mounts. **Fit** (concept-level check; not directly fetched).
- Web file browsers embedded in cloud consoles — a navigable view of a remote hierarchy with upload/download/move/rename/delete. **Fit** (concept-level; medium-agnostic L0 holds: "storage locations the device can reach").
- Modern cloud-era managers — same core plus cloud locations and overlays. **Fit.**

Conclusion: L0 is era-, platform-, and medium-neutral. Cloud, tags, search, tabs, dual-pane are all correctly outside the definition.

## Vendor-specific Findings

See L3. Most consequential for boundary work: even the strongest annotation layers (Finder tags + Smart Folders; Files Community tags in ADS) are implemented *against the file/storage object*, not in an app-side catalog — corroborating that the storage layer, not an app catalog, is what a file manager operates on.

## Boundary Findings

- **vs Personal Cloud Drive** (sibling, undocumented yet): a cloud drive's essence is the storage service (provisioned space, sync, web access); a file manager's essence is operating on whatever storage exists. A file manager *browses* cloud locations but provisions nothing and syncs nothing (Files Community docs explicitly require the provider's client). **Remove storage-service/sync and keep general browsing + operations → File Manager; remove storage-agnostic browsing and keep the service → Personal Cloud Drive.**
- **vs File Sync Application**: sync engines keep selected folder sets consistent across devices/locations; they have no general navigation or operation surface as their center. Boundary interlock to be exercised when that sibling is processed.
- **vs File Transfer Application**: transfer products move files point-to-point between devices/people (often size- or time-bounded shares); they do not organize storage. A file manager's "send/share" is a hand-off, not the product.
- **vs Image Viewer / PDF / Document Reader**: those render content of one file; the file manager renders *metadata + structure* and delegates content rendering to viewers (Preview pane/Quick Look pattern).
- **vs Photo/Music/E-book Library**: libraries impose content semantics (unit = the work/photo/book, aggregated across files) — already codified in the e-book pass ("remove book semantics → File Manager"). Confirmed from this side: file managers treat same-typed files as indistinguishable members of a folder.
- **vs Enterprise/Construction Document Management / ECM / Records**: governance machinery (registers, revisions, controlled distribution, retention, multi-party issue) is absent; file managers are explicitly named there as the "not the Type" contrast (construction-document-management.md).
- **vs Backup Management / Archive Storage Management**: versioned recovery of systems/volumes vs live organization of current files. Archive *formats* inside a file manager (ZIP browsing) are a convenience, not backup.
- **vs standalone archive utilities / batch renamers / image batch processors**: single-purpose transformation tools; the file manager's versions are generic operations over any item, embedded in a browsing surface.
- **"去掉什么就变成另一个 Type" summary**: remove *navigable truthful storage view* → launcher/library; remove *file/folder-as-unit (storage attributes)* → content library; remove *storage mutation* → viewer; constrain *locations* to one provider's space → cloud drive file surface; add *register/revisions/distribution* → document management.

## Uncertainties

- Android file-manager behavior unverified (source timeouts). Mobile claims in the final document are limited to iOS Files evidence and neutral phrasing.
- Terminal/TUI and Linux desktop managers were not directly fetched; they inform the historical/edge check at concept level only.
- Trash/recoverable delete: cross-product page evidence is partial (Finder link titles; Explorer page references delete but the recycle semantics were not on the fetched page). Written as "common, product-dependent" rather than universal.
- Windows "Libraries" virtual aggregation evidenced only via the Win 10 section; treated as optional overlay.
- The exact split of "content search" support (Explorer search includes cloud content per Microsoft page; TC full-text per vendor page; others not verified) — final document says "some products" for content search.
- Whether any mainstream *web* file manager exists as an independent product (not embedded in a cloud service) — not researched; does not affect L0 (medium-agnostic).

## Final Synthesis

A File Manager is the application that lets a person **see and operate on the actual contents of a storage hierarchy**: it navigates real folders across the locations the device can reach, identifies items by their storage attributes, and mutates storage through create/copy/move/rename/delete. Everything else — views, search, preview, tags, smart folders, tabs, dual-pane, archives, cloud and remote locations, mobile tab structures, clean-up suggestions — is the common or optional accretion of three decades of products, layered over an invariant that has not changed since the earliest file managers and that survives unchanged on phones, in the cloud, and in terminal windows.
