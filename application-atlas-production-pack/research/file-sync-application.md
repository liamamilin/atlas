# Research Notes — File Sync Application

Research date: 2026-09-07
Slug: file-sync-application
Directory leaf: File Sync Application (§03.15 Files)

## Research Goal

Understand what a File Sync Application actually is as an Application Type — not as a marketing category. The goal is to extract the smallest defining structure (what makes a product recognizable as file sync regardless of era, topology, or vendor), the common mature structure layered on top of it, the variant axes, and the precise boundaries against neighboring Types (Personal Cloud Drive, File Transfer Application, File Manager, Backup, Version Control, Managed File Transfer).

## Initial Boundary

Working hypothesis before research:

- Core: a background engine that keeps a designated set of files consistent across multiple endpoints (devices and/or servers) by detecting changes and propagating them automatically.
- Likely confusions:
  - Personal Cloud Drive (storage-first; sync is one capability of it)
  - File Transfer Application (one-shot, user-initiated movement)
  - File Manager (local organization, no propagation)
  - Backup (one-way protective copies, not reconciliation)
  - Version Control System (file sync for source code with commit/merge semantics)
  - Managed File Transfer (enterprise B2B file movement with audit/workflow)
- Key open question: is cloud storage definitional? (Suspected no — P2P tools exist without any cloud.)

## Research Questions

1. What is the core object model? (sync scope/folder, replica, change, conflict, version)
2. How does the sync engine work? (change detection, indexing, transfer granularity, application of changes)
3. What topologies exist? (cloud relay hub, self-hosted server, P2P mesh)
4. What identity/trust model connects endpoints? (accounts vs device keys)
5. How are conflicts detected, represented, and resolved?
6. What selective-sync and placeholder mechanisms exist?
7. What safety nets exist (versioning, trash, restore)?
8. What status surfaces does the user actually see?
9. What rules constrain syncing (exclusions, name/path limits, error quarantine, per-device settings)?
10. Where exactly is the boundary to Personal Cloud Drive, Backup, and File Transfer?

## Representative Products

Selected for market representation + different product philosophy + different customer tier:

| Product | Philosophy / tier | Role in sample |
|---|---|---|
| Syncthing | open-source, P2P mesh, no cloud, no accounts, device-key identity | proves cloud/accounts are not definitional |
| Nextcloud (Desktop Client + Server) | self-hosted server hub + clients; open-source enterprise/self-host pole | proves a private server can be the hub |
| OneDrive (Microsoft) | platform-native cloud hub, OS-embedded, consumer + enterprise | the dominant mainstream realization |
| Dropbox | commercial cloud-hub archetype (consumer/team) | market anchor; docs unreachable — degraded evidence |
| Resilio Sync | commercial P2P (BitTorrent heritage) | secondary anchor for the P2P pole; docs unreachable |

## Sources

Directly fetched (2026-09-07):

- Syncthing documentation (docs.syncthing.net):
  - Welcome / documentation index — https://docs.syncthing.net/
  - Getting Started — https://docs.syncthing.net/intro/getting-started.html
  - Understanding Synchronization — https://docs.syncthing.net/users/syncing.html
  - Folder Types — https://docs.syncthing.net/users/foldertypes.html
  - File Versioning — https://docs.syncthing.net/users/versioning.html
- Nextcloud user manual (docs.nextcloud.com):
  - Files & synchronization (chapter index) — https://docs.nextcloud.com/server/latest/user_manual/en/files/index.html
  - Desktop and mobile synchronization — https://docs.nextcloud.com/server/latest/user_manual/en/files/desktop_mobile_sync.html
  - Desktop Client (chapter index) — https://docs.nextcloud.com/server/latest/user_manual/en/desktop/index.html
  - Using the Synchronization Client — https://docs.nextcloud.com/server/latest/user_manual/en/desktop/usage.html
  - Conflicts — https://docs.nextcloud.com/server/latest/user_manual/en/desktop/conflicts.html
- Microsoft Support — OneDrive:
  - OneDrive help & learning (hub) — https://support.microsoft.com/en-us/onedrive
  - Sync with OneDrive (category) — https://support.microsoft.com/en-us/onedrive/category/sync-with-onedrive
  - Choose which OneDrive folders you want to sync on Windows or macOS — https://support.microsoft.com/en-us/onedrive/choose-which-onedrive-folders-you-want-to-sync-on-windows-or-macos

Attempted but abandoned (per source-access limitation rules):

- Dropbox: https://help.dropbox.com/sync and https://www.dropbox.com/sync — timed out twice each pattern; abandoned.
- Resilio Sync: https://help.resilio.com/sync/ and FAQ page — timed out twice; abandoned.
- Google Drive for desktop: https://support.google.com/drive/answer/2360403 — timed out twice; abandoned.
- Nextcloud desktop manual direct paths (docs.nextcloud.com/desktop/...) — 404; recovered via the server user-manual mirror of the desktop chapter.

Consequence: Dropbox, Resilio, and Google Drive are retained as market anchors only. No precise operational claims about them are made anywhere in this research or the final document. Claims that would need their evidence are either dropped or worded at cross-product level using the three directly documented products.

## Product Observations

### Syncthing (evidence layer A — direct, official docs)

Model:

- **Devices** are the participants. Each device has a cryptographically generated **device ID** (derived from its key pair, generated at first start). Two devices connect **only if both are configured with each other's device ID** (mutual pairing). No user accounts exist. Device names are cosmetic.
- **Folders** are the sync scopes. A folder is a local directory designated for synchronization and **shared with specific remote devices**. A new install creates a "Default Folder" marked "Unshared" until shared with another device.
- Topology: **P2P mesh**. Optional community **discovery servers** (global + local discovery) help devices find each other; **relays** relay traffic when direct connection (NAT) fails. QUIC/TCP listeners; local discovery on LAN.

Engine (Understanding Synchronization):

- Files are divided into fixed-size **blocks** (size varies with file size); each block's SHA-256 hash forms a **block list** (offset, size, hash).
- To update a file, the engine compares the current block list to the desired one and finds a source for each differing block — locally (another file with the same block hash) or from another device over the network. Received blocks are hash-verified and written to a **temporary copy** of the file, then moved into place. Syncthing "never writes directly to a destination file."
- **Change detection**: filesystem watcher (notifications, with a short accumulation delay) + periodic full scans (default once per hour, randomized). Rescan checks modification time, size, permission bits; rehashes changed files.
- **Index database** tracks, per file: the local version, versions announced by other devices, and the **global version** ("best", usually most recent). When new index data arrives, the engine recomputes the global version and syncs where local ≠ global.
- **Conflicts**: when a file is modified on two devices simultaneously with differing content, one side's file is renamed to `<filename>.sync-conflict-<date>-<time>-<modifiedBy>.<ext>` (older modification time loses; ties broken by device ID). **Both versions are kept.** Conflict copies are themselves propagated as normal files. Modification-vs-deletion conflicts also produce a conflict copy when deletion wins.
- **Case sensitivity**: case-sensitive internally; on case-insensitive platforms a clashing remote name is reported as a **case conflict** and requires manual resolution.
- Temporary files use reserved name prefixes (`.syncthing.` / `~syncthing~`) which are always excluded from sync.

Folder direction types (Folder Types):

- **Send & Receive** (default): bidirectional.
- **Send Only**: reference copy; ignores incoming changes (folder goes "out of sync"); red **"Override Changes"** button enforces this host's state on the cluster (deleting files that don't exist locally).
- **Receive Only**: replication mirror / backup destination; applies and redistributes cluster changes but does not distribute local changes; red **"Revert Local Changes"** button undoes local modifications.

Versioning (File Versioning):

- Off by default. When enabled, old versions are archived **when a change arrives from another device** (local changes are not archived — the engine cannot know about them before they happen).
- Strategies: **Trash Can** (move replaced/deleted files to `.stversions`, optional age cleanup), **Simple** (keep N timestamped versions per file), **Staggered** (interval-based retention: seconds-level for the first hour, hourly for a day, daily for 30 days, weekly to max age), **External** (delegate to a user script/command).
- Versions folder default: `.stversions` inside the shared folder.

GUI / interfaces:

- Local **web GUI** (default http://127.0.0.1:8384) — folders list on the left (with "Unshared" state), devices list on the right; add remote device / add folder flows.
- Runs as a background daemon; community GUI wrappers exist for desktop/mobile.
- REST API; command-line operation; configuration file.

Security posture:

- Transport encryption between devices (key-pair based); **Untrusted (Encrypted) Devices** feature allows a device to relay/store encrypted data it cannot read.
- Community discovery/relay infrastructure is optional; firewall/direct configuration possible.

### Nextcloud (evidence layer A — direct, official docs)

Model:

- A **Nextcloud server** (self-hosted or provider-hosted) holds the authoritative file store; **desktop sync clients** (Windows/macOS/Linux) and **mobile clients** keep local folders synchronized with it. Topology: **server hub + clients**.
- Identity: **user account on the server** (username/password; two-factor auth documented elsewhere in the manual). The desktop client supports **multiple accounts** (tabs per account).
- Sync scope: **"Folder Sync Connection"** — the user adds a connection between a server folder tree and a local folder; "Choose What to Sync" expands/selects the file tree; "Remove Folder Sync Connection" stops syncing entirely.

Engine / behavior:

- "The Nextcloud desktop client uploads local changes and downloads remote changes." Bidirectional by default.
- **Conflicts**: when a file changed both locally and remotely between sync runs, the client "will be unable to resolve the situation on its own. It will create a conflict file with the local version, download the remote version and notify the user." The remote version becomes the base file (continues receiving remote updates); the local version is preserved as `mydata (conflicted copy 2018-04-10 093612).txt`. Resolution is **manual**: compare, merge, delete the conflicted copy. The conflicted copy is **not uploaded** by default (an experimental env var enables uploading conflict files).
- **Ignored files**: an **Ignored Files Editor** with pattern list (wildcards; directory-scoped patterns ending in `/`), backed by a system file `sync-exclude.lst`; a checkbox marks patterns whose matches are also deleted as "fleeting metadata". The client always excludes files with characters that cannot sync to other file systems; symbolic links are ignored (warning icon).
- **Error quarantine**: files that cause individual errors three times are removed from the sync set; the client offers retrying three additional times.
- **Virtual files** (placeholders): "Enable virtual file support" per connection; an "Availability" action; macOS uses the native **File Provider**. Files can be online-only and hydrated on demand.
- Directory mtime is not preserved (documented limitation).

Interfaces:

- **System tray / menu bar icon** with explicit status states: green check (up to date + connected), blue (syncing), grey pause bars (paused), grey dots (offline/disconnected), yellow "!" (informational), red X (configuration error such as wrong login/server URL).
- Tray right-click menu: Open main dialog, Pause/Resume sync, Settings, Exit.
- **Main dialog**: recent activities, errors, server notifications; account tabs with connection status, server space used/available, current sync status, "Add Folder Sync Connection".
- **File manager overlay icons** (Explorer/Finder/Nautilus): green check (in sync), warning (ignored/symlink), red X (error/blacklisted), blue cycling (waiting/syncing); directory icons aggregate child errors; offline = no icons.
- **Sharing from the desktop**: file-manager context menu → Nextcloud → Share options; create share links and share with internal users, same as the web interface.
- General settings: launch on startup, monochrome icons, server notifications, "Ask confirmation before downloading folders larger than [size]", Edit Ignored Files.
- Network settings: proxy, download/upload **bandwidth limits**.
- Command-line client and configuration file exist (documented chapters).

Server-side complements (user manual): web interface file management, **WebDAV** access, deleted-files (trash) management, **version control** of files on the server, storage quota, sharing/federated shares, server-side and end-to-end encryption.

### OneDrive (evidence layer A — direct, official Microsoft support)

Model:

- Cloud hub (Microsoft-hosted) + a **sync app per computer** (Windows/macOS) + mobile apps + web. Identity: **Microsoft account** (personal) or **work/school account**.
- Sync scope: a local **OneDrive folder**; the user selects **which folders** sync to each computer via **Account tab → Choose Folders** dialog (uncheck folders not wanted locally).
- Documented behaviors of folder selection:
  - Unchecking a folder **removes it from that computer** but keeps it **available online**.
  - Selections are **unique to each computer and each account**.
  - Certain folders **cannot be unchecked** (Documents, Desktop, Pictures, Personal Vault) — these are the "folder backup" set.
  - Only folders already in OneDrive can be selected; arbitrary external folders (e.g., USB drive) cannot be added (and a separate article documents that syncing to SD cards/external USB drives is not supported).
- Web browser and mobile **always see all folders** regardless of local selection.

Surfaces and controls (from the Sync category and related topics):

- Tray/menu-bar icon; **pause syncing**; **stop/cancel an upload or sync**; change the sync app's **upload or download rate**.
- **Files On-Demand** (Windows and macOS): save disk space with online-only files (placeholder mechanism).
- **Folder backup**: "Back up your Documents, Pictures, and Desktop folders with OneDrive" (known-known folder redirection).
- Status/error surfaces: "OneDrive icons" meanings article; troubleshooting set — "Fix sync problems", "Reset OneDrive", "Sync pending error", "Processing changes error", "This file can't be synced", "Fix paths that are too long to sync", filename-change article, error codes list.
- Recovery: **Restore files / Restore entire OneDrive** (ransomware-oriented), **Restore deleted files**, **Restore previous versions**.
- Sharing: share files and folders; shortcuts to shared folders; see files shared with you.
- Storage: quotas, "OneDrive says it's full", storage management.
- Enterprise: separate "OneDrive for work or school" track; IT-admin help center exists.

### Dropbox (evidence layer: degraded — official docs unreachable)

- Not directly verified in this pass. Retained as the commercial cloud-hub archetype and market anchor. No operational claims are made about Dropbox anywhere in this research or the final document. Its role in the sample is to justify that the cloud-hub consumer/team pole is represented in the market, not to supply evidence.

### Resilio Sync / Google Drive for desktop (evidence layer: degraded — unreachable)

- Resilio Sync: retained as a secondary anchor for the commercial P2P pole (BitTorrent-protocol heritage). No operational claims made.
- Google Drive for desktop: retained as an additional cloud-hub + desktop-integration anchor. No operational claims made.

## Cross-product Comparison

| Aspect | Syncthing | Nextcloud | OneDrive | Dropbox / Resilio / GDrive |
|---|---|---|---|---|
| Topology | P2P mesh (optional discovery/relay) | self-hosted server hub + clients | cloud hub + clients | (anchor only) |
| Identity / trust | device key-pair IDs, mutual pairing, no accounts | server user account (+2FA) | Microsoft account (personal / work-school) | (anchor only) |
| Sync scope unit | folder shared with specific devices | folder sync connection (server tree ↔ local folder) | OneDrive folder + per-computer folder selection | (anchor only) |
| Change detection | FS watcher + periodic full scan; mtime/size/perms | client scan (implied by upload/download loop) | sync app (mechanism not detailed in fetched pages) | — |
| Transfer granularity | block-level delta with SHA-256 block lists | file-level upload/download (documented at that level) | file-level (not detailed) | — |
| Conflict handling | conflict copy renamed with date+device; both kept; copies propagate | "conflicted copy" file with local version; remote becomes base; manual merge; not uploaded by default | conflict handling implied by troubleshooting set (not detailed in fetched pages) | — |
| Selective sync | per-folder sharing decision | Choose What to Sync / folder sync connections | Choose Folders dialog (per computer) | — |
| Placeholders / online-only | none (full replicas) | virtual files + macOS File Provider | Files On-Demand | — |
| Versioning / recovery | trash can / simple / staggered / external (.stversions) | server version control + deleted files + trash | previous versions, deleted-file restore, full restore | — |
| Status surfaces | web GUI folder/device states | tray icon states + per-file overlay icons | tray icon + file icon meanings + error codes | — |
| Exclusions | ignore patterns (.stignore documented in docs index) | Ignored Files Editor + sync-exclude.lst + always-excluded characters | unsupported characters / path length (troubleshooting) | — |
| Bandwidth / network | send/receive rate limits | network settings: proxy + bandwidth limits | change upload/download rate | — |
| Direction control | send&receive / send only (Override) / receive only (Revert) | bidirectional default (server permissions govern) | bidirectional default | — |
| Pause semantics | (device/folder pause in GUI) | Pause Sync vs Remove connection (explicit distinction) | Pause syncing; stop/cancel upload | — |
| Sharing | share folder with devices | share links + internal users from desktop context menu | share files/folders, shortcuts | — |
| Web/mobile access to content | none (no cloud) | web interface + WebDAV + mobile apps | web + mobile always see all folders | — |
| Multiple accounts | n/a (no accounts) | multiple accounts in one client | multiple accounts documented | — |

Reading of the table:

- The **engine loop** (scope → detect → propagate → converge, with conflicts preserved not merged) is present in every directly documented product.
- **Cloud storage, accounts, web/mobile access, placeholders** are present in hub products and absent in Syncthing → they cannot be definitional.
- **Selective sync, exclusions, bandwidth controls, pause, status icons, versioning/recovery, sharing** appear in all three directly documented products in different forms → common mature structure.
- **Block-level delta transfer** is documented only for Syncthing in this sample → "some products", not universal.
- **Direction modes (send-only/receive-only)** are explicit, first-class configuration only in Syncthing in this sample → variant.

## Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the product is no longer recognizable as a File Sync Application:

1. **A designated sync scope** — a folder or defined set of files that the user designates for synchronization (everything else is out of scope).
2. **Multiple replicas** — the scope exists in more than one place: on several devices and/or on a server, each holding a copy of the scope.
3. **An automatic propagation engine** — the application itself detects changes to the scope and applies them to the other replicas, without the user performing a per-change action.
4. **Convergence** — the engine drives replicas toward a consistent state, including propagating creations, modifications, renames, and deletions, and reconciling divergent states.

Removal tests:

- Remove the scope → generic file copying / storage. Not sync.
- Remove multiple replicas → a local file manager. Not sync.
- Remove automatic propagation → manual file transfer (user moves each file). Not sync.
- Remove convergence/reconciliation → one-shot copy jobs or backup. Not sync (or a different Type).

Deliberately NOT in L0 (checked against the historical/market sample):

- cloud storage or any central server (Syncthing has none; rsync/Unison-era tools have none)
- user accounts (Syncthing pairs devices by key)
- GUI, tray icons, mobile apps (command-line synchronizers satisfy the core)
- placeholders/online-only files, version history, sharing with other people, bandwidth controls
- bidirectionality as a hard requirement (send-only/receive-only modes exist; the canonical case is bidirectional, direction is configurable)

Historical check: command-line synchronizers (rsync-style one-way and Unison-style bidirectional tools), platform-native folder-pairing mechanisms (e.g., briefcase/offline-files concepts), and 2000s P2P sync services all satisfy the four properties without cloud, accounts, or modern UI. The L0 holds.

### L1 — Common Mature Structure

Present across the directly documented sample in different forms; expected in mature products but not definitional:

- change detection machinery (filesystem watching plus periodic scanning)
- a local state/index of file versions per replica
- conflict detection with **conflict copies** (both sides preserved, never silently merged) and user-mediated resolution
- version history / deleted-file recovery / restore (per-folder versioning in Syncthing; server versioning + trash in Nextcloud; previous-versions + restore in OneDrive)
- selective sync (choose which folders a device carries)
- placeholder / online-only files in hub products (virtual files, Files On-Demand)
- status surfaces: tray/menu-bar agent icon with distinct states + per-file overlay icons in the OS file manager
- pause/resume, and the distinction between pausing and removing a sync connection
- exclusions/ignore patterns and handling of unsyncable names/characters
- bandwidth limits and proxy/network settings
- sharing of the synced scope (with devices in P2P; with people via links/permissions in hub products)
- notifications of sync problems and an activity/error list

### L2 — Variant / Optional Structure

- **Topology**: cloud relay hub / self-hosted server hub / P2P mesh / hybrid (LAN-first with relay fallback)
- **Identity substrate**: user account (personal or organizational) vs device key-pair pairing
- **Direction modes**: send-only (reference copy with override), receive-only (mirror/backup destination with revert), bidirectional default
- **Placeholder depth**: full replicas everywhere vs virtual/online-only files with on-demand hydration
- **Encryption posture**: transport-only, server-side encryption, end-to-end/zero-knowledge, untrusted-device encryption
- **OS integration depth**: OS-embedded (platform-native) vs third-party background agent vs headless daemon + web GUI
- **Enterprise management**: admin consoles, policy deployment, org-scoped accounts (OneDrive for work/school track; Nextcloud admin manual)
- **Content services around the sync core**: web file management, WebDAV, photo management, quotas, collaboration — common in hub products, absent in pure sync tools

### L3 — Vendor-specific (research notes only)

- Syncthing: device ID format and mutual-configuration rule; `.sync-conflict-<date>-<time>-<modifiedBy>` naming; `.stversions` folder; `.stignore`; reserved temp-file prefixes; BEP block-exchange protocol; community discovery/relay servers; watcher delay values; scan interval defaults; staggered retention intervals.
- Nextcloud: "conflicted copy <date> <time>" naming; `sync-exclude.lst`; "fleeting metadata" deletion checkbox; error-quarantine counts (removed after 3 errors, 3 retries offered); `OWNCLOUD_UPLOAD_CONFLICT_FILES` experimental env var; directory-mtime limitation; "Ask confirmation before downloading folders larger than [size]".
- OneDrive: Choose Folders dialog location (Account tab); uncheck-removes-locally-keeps-online rule; per-computer/per-account uniqueness; un-uncheckable backup folders (Documents/Desktop/Pictures/Personal Vault); Files On-Demand; Personal Vault; folder backup redirection; error-code catalog; reset procedure; SD-card/USB sync restriction.
- Dropbox / Resilio / Google Drive: nothing recorded — sources unreachable; no claims made.

## Rejected Findings

- "File sync = cloud storage" — rejected. Syncthing (and the historical tooling) sync without any cloud; hub products add storage as a companion service.
- "File sync requires user accounts" — rejected. Device-key pairing satisfies the trust need.
- "File sync is defined by its UI (tray icon + blue syncing icon)" — rejected. Command-line synchronizers satisfy the core; UI is the common mature surface.
- "Delta/block transfer is definitional" — rejected as definitional (documented directly only for Syncthing in this sample); recorded as a common optimization, worded as "some products".
- "One-way sync is not sync" — rejected. Send-only/receive-only are direction configurations of the same engine; the boundary against backup is drawn on working-copy-vs-protective-copy semantics, not on direction alone.
- "Sync apps also do backup of system folders" — kept as a variant (OneDrive folder backup), not definitional.

## Boundary Findings

- **vs Personal Cloud Drive**: the drive is storage-first — a place where files live, accessed via web/mobile, with quotas, sharing, and content services; sync is the engine that keeps replicas consistent. Test: remove the sync engine → a cloud drive remains (web storage); remove the cloud storage → a sync engine remains (Syncthing). Many products are bundles of both (OneDrive, Dropbox, Nextcloud); the Type boundary follows the engine, not the bundle. The sibling leaf Personal Cloud Drive should own the storage-first framing.
- **vs File Transfer Application**: transfer is one-shot, user-initiated, point-to-point delivery of a file or batch ("get this file there"); sync is a standing relationship in which the engine continuously reconciles replicas. Test: does anything happen automatically after the initial act? If no → transfer.
- **vs File Manager**: organization/navigation of local files; no propagation, no replicas. Sync clients *integrate with* file managers (overlay icons, context menus) but the file manager is not the sync engine.
- **vs Backup Management / backup software**: backup creates protective copies where the source remains the working set and the destination is not expected to be edited; retention and restore are the point. Sync maintains *working replicas* that can all be sources of change, reconciles them, and propagates deletions. Overlap exists (receive-only folders are backup-like; OneDrive folder backup is backup-flavored use of sync machinery) — the direction-of-authority test distinguishes them: in sync, any replica may be authoritative; in backup, only the source is.
- **vs Version Control System**: VCS records explicit commits/history with semantic merge for (mostly text) source files; sync propagates current file state with no semantic merge — conflicts are preserved as parallel copies for the human to merge. A VCS is file sync for code with a fundamentally different conflict model.
- **vs Managed File Transfer (Data & Analytics family)**: MFT moves files between organizations/systems on schedules with audit, encryption, and workflow guarantees; it is logistics for file exchange, not replica convergence of a user's working set.
- **vs Data Replication Platform**: replicates database/data-store state, not user-visible file scopes.

Boundary issue for STATUS.md: none blocking. The leaf is a valid independent Type. The strongest adjacency is with Personal Cloud Drive (bundle overlap in mainstream products); the recommended presentation — sync engine as the Type, storage as common companion — keeps both leaves distinct.

## Uncertainties

- Dropbox, Resilio Sync, and Google Drive for desktop could not be directly documented (timeouts). The cloud-hub consumer pole therefore rests on OneDrive + Nextcloud direct evidence plus Dropbox's uncontroversial market position; no Dropbox/Resilio/GDrive-specific claims are made.
- OneDrive's internal change-detection/transfer mechanics were not detailed in the fetched pages; the document avoids asserting them.
- Nextcloud's change-detection internals are likewise only implied by the upload/download loop description.
- Whether block-level delta transfer is common across hub products could not be verified in this sample; it is worded as product-dependent.
- Historical claims (rsync/Unison/briefcase-era tools) are used only as conceptual anchors for the historical check, not as researched products; no precise claims about them are made.
- Mobile-client behavior varies (Nextcloud documents that bidirectional sync is not fully implemented in its Android client); mobile depth is treated as a variant, not asserted uniformly.

## Final Synthesis

A File Sync Application is a background propagation engine over a designated file scope: the user designates a folder (or set of folders) as a sync scope, the scope is replicated on multiple endpoints (devices and/or a server), and the application continuously detects changes on any replica and applies them to the others, driving all replicas toward a consistent state — including deletions — while preserving both sides of any conflicting change as separate copies for the user to reconcile.

Everything else that defines the modern category — cloud storage, accounts, web/mobile access, online-only placeholders, version history, sharing, bandwidth controls, polished status icons — is the common mature structure or a variant layered on that engine, not the definition of the Type. The topology (cloud hub, self-hosted server, P2P mesh) and the identity substrate (account vs device keys) are variant axes; the engine loop is the invariant.
