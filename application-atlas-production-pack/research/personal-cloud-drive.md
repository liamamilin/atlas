# Research Notes — Personal Cloud Drive

## Research Goal

Understand what a Personal Cloud Drive is as an Application Type: what must exist for a product to be recognizable as one, what is merely common in today's market, and where its boundaries lie against the three already-processed sibling leaves in §03.15 Files (File Manager, File Sync Application, File Transfer Application) and against other adjacent Types (backup, enterprise file sync & share, photo cloud, web hosting).

## Initial Boundary

Working hypothesis before research:

- Core use: an individual stores their own files on remote storage and reaches them from any of their devices.
- Primary users: individuals (consumer), sometimes households.
- Nearest neighbors: File Sync Application (engine vs store), File Manager (local organization), File Transfer Application (delivery event), online backup (restore copy), enterprise file sync & share / Team Workspace (organizational container), photo cloud (parsed media library), web hosting (publishing).
- Unknowns: whether sync is definitional or just the dominant mechanism; whether "personal account" is load-bearing vs the enterprise pole; how platform-native drives (iCloud Drive) fit; whether self-hosted products fit.

## Research Questions

1. What is the minimal structure every personal cloud drive has — including pre-sync-era online storage?
2. What role does the personal account and its storage capacity play?
3. What surfaces do users operate the collection through (web / desktop / mobile), and how do they differ per product philosophy?
4. Which capabilities are common mature structure (sync, sharing, recovery, placeholders, auto-upload) vs definitional?
5. Where exactly is the seam with File Sync Application, File Manager, File Transfer Application (all three already documented)?
6. Do self-hosted (Nextcloud) and platform-native (iCloud Drive) products satisfy the same core?
7. What fails the definition: backup services, photo clouds, transfer tools, enterprise EFSS?

## Representative Products

Selected for market representation + different product philosophy + different customer level + documentation availability:

| Product | Philosophy / pole | Customer level | Doc access |
|---|---|---|---|
| Apple iCloud Drive | platform-native, invisible infrastructure | Apple device owners (consumer) | ✅ deep (iCloud User Guide) |
| Microsoft OneDrive | OS-integrated (Windows), suite-bundled | consumer + Microsoft 365 | ✅ deep (help center) |
| pCloud | independent vendor, privacy/lifetime-purchase | consumer, family, business tiers | ✅ (help center + product pages) |
| Nextcloud Files | self-hosted / sovereign, open source | home users + organizations | ✅ (product page) |
| Dropbox | sync-first archetype, freemium | consumer → prosumer | ❌ timeouts ×2 — market anchor only |
| Google Drive | web-first, ecosystem-bundled | consumer + Workspace | ❌ timeouts ×2 — market anchor only |

## Sources

Fetched 2026-09-08:

- Apple — iCloud User Guide: "Set up iCloud Drive on all your devices" (https://support.apple.com/en-us/HT201104 → guide page mm203b05aec8); "Keep your files up to date and share them with iCloud Drive" (guide page mm19ef899373); full iCloud User Guide TOC (iCloud Drive on iCloud.com section: upload/download, view, organize, share, manage sharing, delete/recover files)
- Microsoft — OneDrive help & learning hub (https://support.microsoft.com/en-us/onedrive); "Upload and save files and folders to OneDrive" Quick Start (personal-accounts version); full help-category taxonomy (Get started / Files / Share & collaborate / Sync / Mobile & Mac / Accounts & storage / Troubleshoot)
- pCloud — product home (https://www.pcloud.com/); "Remote access & flexibility" feature page (/features/synchronization); Help center hub (https://help.pcloud.com/); File Management & Collaboration topic page
- Nextcloud — "Nextcloud Files" product page (https://nextcloud.com/files/)

Unreachable (recorded per source-access limitation):

- Dropbox: help.dropbox.com/learn-more/what-is-dropbox timeout; dropbox.com/learn-more/what-is-dropbox timeout → abandoned after 2 failures
- Google Drive: support.google.com/drive/answer/2374987 timeout ×2 → abandoned after 2 failures

Consequence: no product-specific claims are made about Dropbox or Google Drive anywhere in this research or the final document; they appear only as market anchors.

## Product Observations

### Apple iCloud Drive (Layer A — direct, official user guide)

- "With iCloud, your files and folders stay up to date on all your devices, and you can share and collaborate on files and folders with friends, family, and colleagues."
- "When you set up iCloud Drive, you can store files and folders in the cloud, which frees up space on your device. You can see them on any device that has iCloud Drive turned on."
- Surfaces: Files app (iPhone/iPad), Finder sidebar (Mac), File Explorer (Windows, via iCloud for Windows), iCloud.com in a web browser. Same Apple Account required on every device; without sign-in the files are not accessible on that device.
- Change propagation: "changes you make on one device—like adding a file to a folder, renaming a file, or deleting a file—automatically appear on all your devices."
- Capacity: "All files you add to iCloud Drive count toward your iCloud storage." Storage is a personal iCloud plan (free tier + iCloud+ paid tiers); storage is shared across iCloud services and can be shared with family.
- Organization: files and folders; user organizes (iCloud.com: view files and folders, organize files and folders, upload and download files).
- Deletion/recovery: deleting moves files to Recently Deleted (iPhone/iPad/iCloud.com) or Trash (Mac); "Recently deleted files can be recovered for 30 days" (product-specific number, directly observed); permanent removal possible.
- Sharing: share files and folders by link; collaborators' changes visible in real time; permission choice edit vs view-only; owner can allow invitees to add other people; people outside iCloud can download via link; iWork files can be link-editable. Separate "manage sharing", "add or remove shared files", "delete shared files" surfaces.
- Platform-native extras: Desktop & Documents Folders option (device folders absorbed into the drive); per-app iCloud containers (apps store their data in iCloud Drive); iCloud Backup is a separate feature (device backup, not the drive).
- Storage management: check storage on any device, buy more with iCloud+, family sharing of storage.

### Microsoft OneDrive (Layer A — direct, official help center)

- Explicit personal pole: the Quick Start is titled "for OneDrive for home and personal accounts"; the desktop location is "OneDrive – Personal"; a separate article explains "What is OneDrive for work or school?" — the personal/organizational split is a first-class product distinction.
- Generic files: "You can store over 300 types of files on OneDrive."
- Surfaces: browser (office.com → app launcher → OneDrive), File Explorer ("OneDrive – Personal" in Navigation pane; on Windows 10/11 OneDrive "may have already asked you to sign in to sync your files"), mobile apps (Android/iOS), Office apps' Save dialog ("Save a Copy > OneDrive - Personal", "Add a Place").
- Upload: web upload (Add new > Files upload / Folder upload) or drag into the File Explorer OneDrive location when the sync app is installed.
- Help taxonomy confirms the capability set: Files (change views, delete, import other cloud files, upload, change OneDrive folder location, download, AutoSave, copy/transfer/import into personal OneDrive, ransomware detection and recovery, install on external drive); Photos (auto-save on Android/iOS, organize/find, group by people, Samsung Gallery, AI restyle); Sharing (share files/folders, shortcuts to shared folders, files you shared / shared with you, share with family or Outlook groups); Restore (restore files, restore entire OneDrive, restore deleted files, restore previous versions); Storage (quotas, "My OneDrive says it's full", Files On-Demand for Windows/macOS/Android); Account (frozen account, blocked account, add/remove account); Troubleshoot (sync problems, reset, path-too-long, SD-card/USB, lost/missing files, filename changed, "files will be erased" message, unlink/re-link, icon states).
- Sync: dedicated "Sync" category — sync files & folders, choose which folders to sync (selective sync), pause syncing, stop/cancel syncing.
- Space: "Save disk space with OneDrive Files On-Demand" (online-only placeholders) for Windows and macOS.
- Device-folder backup: "Back up your Documents, Pictures, and Desktop folders with OneDrive" (folder backup / known-folder protection).
- Protection extras: Personal Vault ("Protect files with Personal Vault"), ransomware detection and recovery, restore entire OneDrive to a point in time.
- Era-current AI: Copilot in OneDrive (summarize files, compare files, ask about topics without opening files, audio overviews, shareable AI agents).

### pCloud (Layer A — direct, official help center + product pages)

- Positioning: "Store, access, and manage your files on your own terms, from anywhere." Swiss privacy posture; user chooses data region (Europe or USA); encryption offered (client-side encryption as a separate paid product pole).
- Access: "Access from anywhere — On a laptop, phone, or tablet"; mobile apps with integrated media player (stream content from the cloud).
- Sync: "Thanks to the automatic Sync feature, every change you make is instantly reflected across them all" (across devices).
- Offline: "You can pre-select your files so they are available on your device even without an internet connection. Any changes you make will sync automatically once you're back online."
- Space: "Free up room on your device without saying goodbye to what matters" (automatic upload of photos/videos); auto-backup & sync ("your files update automatically"); document scanning from phone.
- File management (help center topics): uploading, downloading, and organizing files across all platforms (Web/Desktop/Android/iOS).
- Sharing machinery: Shared Links (link settings, password protection, traffic management); Invite to Folder Collaboration (invite other pCloud users to folders with customizable permission levels); Managing Shares and Access Control (access levels, view shares, terminate access); File Requests (collect files from anyone, even without pCloud accounts).
- Distinctive: Public Folder — "a special folder in pCloud that allows you to create direct links to files and folders, host static HTML websites, and embed images" (web-hosting capability inside the drive — vendor-specific).
- Business model: free plan, subscription plans, lifetime plans, family plan, business plan — the lifetime-purchase pole.
- Adjacent products kept separate by the vendor itself: pCloud Transfer (transfer service), pCloud Pass (password manager), pCloud Save — the drive is distinct from the transfer tool in the vendor's own product split.

### Nextcloud Files (Layer A — product page depth; self-hosted pole)

- "Nextcloud Files is a cloud storage and file sharing software that provides easy access to sharing and collaboration from anywhere, anytime."
- Deployment: self-hosted server, or provider-hosted ("Sign up now — Get free account at a provider"); on-premises, cloud, or hybrid. "Nextcloud at home — For families, students & you" — a home/household pole exists.
- Surfaces: "A modern and easy-to-use web interface, desktop clients and mobile apps."
- Key capabilities listed: search in folders; secure file and folder sharing; flexible access permissions; link protection and expiration dates; file locking; desktop and mobile synchronization; co-editing with office suite integration; ownership transfer for files and folders; version control with ability to restore old versions; client-side protection and end-to-end encryption; File Drop (others upload into a secure folder via link); file requests.
- Mobile clients: "automatic upload of pictures and videos users take and they can synchronize selected files and folders"; multiple accounts; activity feed and notifications.
- Enterprise machinery (organizational pole of the same product): File Access Control rules, compliance kit, auditing, external storage backends (FTP/SMB/S3/SharePoint), LDAP/SSO — confirms that the same file-store core scales into the enterprise EFSS territory when an organization governs it.

### Dropbox / Google Drive (no direct evidence — anchors only)

- Unreachable in this environment (timeouts ×2 each). Both are canonical market anchors for the Type (Dropbox as the sync-folder archetype that defined the modern category; Google Drive as the web-first ecosystem-bundled pole). No product-specific claims are made about either. Their existence as dominant products is used only as market-structure evidence, not as operational detail.

## Cross-product Comparison

| Structure | iCloud Drive | OneDrive (personal) | pCloud | Nextcloud Files | Dropbox / Drive (anchors) |
|---|---|---|---|---|---|
| Personal account owns the collection | Apple Account (required per device) | Microsoft account ("OneDrive – Personal") | pCloud account | account on the (self-hosted) server | yes |
| Personal storage capacity | files count toward iCloud storage; plans; family sharing | quotas; "full" state; frozen account | plans incl. lifetime/family | server storage (self-provisioned) | yes |
| Generic files + user-managed folders | files and folders | "over 300 types of files" | upload/download/organize | files and folders | yes |
| Web surface | iCloud.com Drive | OneDrive web | web app | web interface | yes |
| Desktop surface | Finder / File Explorer (via iCloud for Windows) | File Explorer + sync app | desktop app / drive | desktop sync clients | yes |
| Mobile surface | Files app | mobile apps | mobile apps | mobile apps | yes |
| Automatic change propagation across devices | explicit ("automatically appear on all your devices") | Sync category, pause/stop | "automatic Sync feature" | "desktop and mobile synchronization" | yes |
| Online-only / free-up-device-space | "frees up space on your device" | Files On-Demand | "free up room on your device" | not directly observed | yes |
| Mobile auto-upload (camera) | via iCloud Photos (separate surface) | auto-save photos Android/iOS | automatic upload | automatic upload of pictures/videos | yes |
| Link sharing + permissions | link share, edit/view, allow adding people, non-account download | share files/folders, shared-with-you, family groups | shared links w/ password + traffic limits, invite-to-folder w/ permission levels, terminate access | sharing, permissions, link expiration | yes |
| File requests / inbound collection | not observed | not observed | File Requests | File Drop, file requests | — |
| Deleted-file recovery | Recently Deleted, 30 days (product-specific) | restore deleted files | file recovery | version restore | yes |
| Version history | not directly observed for Drive | restore previous versions | recovery features | version control with restore | yes |
| Search | not directly observed for Drive | organize and find (photos observed) | search in folders | search in folders | yes |
| Offline availability | not directly observed | implied by On-Demand model | offline access (pre-select) | sync selected folders | yes |
| Device-folder backup into the drive | Desktop & Documents Folders | Documents/Pictures/Desktop backup | auto-backup | not observed | yes |
| Identity substrate | platform account | platform account | email account | server account (self-hosted) | varies |
| Encryption posture | not claimed in fetched docs | Personal Vault (protected area) | client-side encryption add-on; data-region choice | E2EE capability | varies |
| AI assistance | — | Copilot in OneDrive | — | Nextcloud Assistant | era-current |
| Static web hosting of files | — | — | Public Folder (HTML hosting) | — | vendor-specific |
| App data containers inside the drive | per-app iCloud containers | — | — | — | platform-specific |

Reading of the comparison:

- Every sampled product, across every philosophy (platform-native, OS-integrated, independent, self-hosted), holds: a personal account owning a capacity-bounded collection of generic files in user-managed folders, on storage remote to the user's devices, reachable through web + desktop + mobile surfaces, operated on through file operations (upload/download/organize/delete/share), with recovery from deletion.
- Sync (automatic change propagation) is present in all modern samples but is a mechanism, not the store: the pre-sync-era online-storage pattern (web upload/download only) and the web-only usage of every modern product satisfy the store without continuous propagation. Sync belongs to common mature structure.
- Sharing is present in all samples but a drive without sharing is still a drive (early personal online storage had little or none); sharing is common mature structure with rich per-product machinery.
- The personal-vs-organizational seam is confirmed from inside the products themselves: OneDrive ships "OneDrive – Personal" vs "OneDrive for work or school" as distinct poles; Nextcloud's enterprise machinery (access-control rules, auditing, LDAP) is what turns the same store into organizational territory.

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The personal file collection of record** — the user's own files held as a persistent, growing collection on storage remote to the user's devices (provider-operated cloud or self-operated server), owned by a personal account with its own storage capacity; files kept as generic files addressed by name/type/size/location — not parsed into domain objects. Remove → local file manager / external disk; remove the generic-file nature → photo cloud / media locker.
2. **Device-independent reachability** — the collection is reachable from whichever of the user's devices the user is at, through the product's own surfaces (web plus device clients); the remote copy is a primary working copy, not a transfer waypoint and not a restore-only backup. Remove → file transfer tool (waypoint) or backup vault (restore copy).
3. **The file-operation loop against the remote collection** — the user organizes the collection (folders as the near-universal implementation) and performs file operations — upload, download, move, rename, delete, share — against the remote copy itself. Remove → read-only archive; remove the remote collection → local file manager.

Jointly-held is load-bearing:

- 1 alone = an unreachable vault (backup store territory)
- 2+3 without 1 = ephemeral remote workspace / transfer tool
- 1+3 without 2 = a remote disk operated from a single fixed surface
- 1+2 without 3 = a read-only archive

### L1 — Common Mature Structure

- device sync clients with automatic change propagation (the modern default mechanism)
- selective sync / online-only placeholders (keep the cloud copy, spare device storage)
- mobile auto-upload of camera media
- link-based sharing with permissions; invite-based folder collaboration; inbound collection (file requests / drop)
- deleted-file recovery (trash / recently-deleted) and version history / restore points
- search over the collection
- previews / built-in viewers
- offline availability marking
- storage-tier monetization (free tier + paid capacity)
- device-folder backup (Desktop/Documents/Pictures absorbed into the drive)
- sync status surfaces (icons, progress, activity/error lists)

### L2 — Variant / Optional Structure

- identity substrate: platform account (Apple/Google/Microsoft), standalone email account, self-hosted server account
- deployment: provider-operated cloud vs self-hosted server vs hybrid
- interaction posture: sync-folder-first vs web-first vs virtual-drive vs OS-integrated (drive appears as native filesystem location)
- encryption posture: server-side only vs optional client-side/E2EE vs E2EE-native
- business model: freemium subscription vs one-time/lifetime purchase vs bundled with platform or productivity suite vs self-hosted software
- household/family sharing of one storage pool
- content-aware layers on top of the generic store: photo management, media players, document scanning (optional; deep media-library center of gravity = photo cloud territory)
- AI assistance over the collection (era-current)

### L3 — Vendor-specific (research notes only)

- iCloud Drive: 30-day Recently Deleted window; Desktop & Documents Folders absorption; per-app iCloud containers; iCloud+ bundle (Private Relay, Hide My Email); storage shared across iCloud services
- OneDrive: Personal Vault; ransomware detection & recovery; restore entire OneDrive; account freezing on quota/abuse; "over 300 file types"; Copilot surfaces; Samsung Gallery integration; known-folder backup
- pCloud: Public Folder with direct links + static HTML hosting + embedding; link traffic management; lifetime plans; EU/USA data-region choice; product split (Transfer / Save / Pass as separate products)
- Nextcloud: external storage backends; File Drop; federation between servers; rich workspaces; file locking; team folders; access-control rule engine; app ecosystem
- Dropbox / Google Drive: no claims (docs unreachable)

## Historical / Market-Sample Check

- Early-2000s personal online-storage services (web-upload/download lockers with folders, personal account, paid capacity; e.g. the Xdrive/i-drive/early-Box.net class): satisfy all three L0 legs with no sync, no mobile, no sharing machinery. ✓ The definition does not require the sync era.
- Personal FTP/WebDAV server + client: remote storage + reachability + file operations. ✓ (Confirms "remote storage", not "provider cloud", is the invariant — the operator can be the provider, the platform vendor, or the user themselves.)
- Platform-native drives (iCloud Drive): ✓ — identity substrate is the platform account; the drive is partly invisible infrastructure for app containers, but the user-facing file collection satisfies the core.
- Sync-first drives (Dropbox class): ✓ — sync is the mechanism layer, the store is still the core.
- E2EE drives (Sync.com / Mega class, pCloud's encryption folder): ✓ — encryption posture is L2.
- Self-hosted (Nextcloud at home): ✓ — deployment is L2.
- Fails the definition, correctly: Google Photos-class photo clouds (parsed media library, not generic files); WeTransfer-class transfer tools (delivery event, no standing collection); backup services (restore-oriented copies, not a working collection); P2P-only sync tools (no standing remote collection of record); enterprise EFSS/ECM (organizational container, admin governance — the personal-ownership leg fails).

## Vendor-specific Findings

See L3 above. None of these enter the canonical core. The pCloud Public Folder (static web hosting) and OneDrive Personal Vault are the clearest examples of capabilities that would pollute the Type if promoted.

## Boundary Findings

- **vs File Sync Application** (processed 2026-09-07): engine vs store. Remove the sync engine → the cloud drive remains (web-only operation satisfies the core). Remove the standing remote collection → the sync engine remains (P2P topology). The two are bundled in mainstream products, but both leaves stand. This pass confirms the seam the sync pass asserted.
- **vs File Manager** (processed 2026-09-07): the drive provisions and holds remote storage as a service; the manager only operates on whatever storage exists (the file-manager pass recorded that platform Files apps require the provider's client to mount cloud drives). The drive's collection is the storage the manager may merely browse.
- **vs File Transfer Application** (processed 2026-09-07): delivery event vs persistent organized store — the storage-posture test. A transfer tool keeps at most a temporary copy; the drive's defining property is the standing collection. pCloud's own product split (pCloud vs pCloud Transfer) confirms the seam from the vendor side.
- **vs Online backup**: backup holds protective copies for restore; the drive holds the working collection (the remote copy is primary). Products blur this (drive-side "backup your folders" features), but the center of gravity differs. Personal backup is not a leaf in this directory; enterprise Backup Management (§14) is out of scope here.
- **vs Team Workspace Platform / Enterprise Content Management / enterprise EFSS**: organizational container with admin governance vs personal account with personal capacity. Confirmed by OneDrive's own Personal vs work-or-school split and by Nextcloud's enterprise machinery being additive to the same store.
- **vs Photo Cloud / media lockers**: generic files vs parsed media library. Drive products add photo-aware layers (OneDrive photos, pCloud photos) without the library becoming the core.
- **vs Web hosting**: pCloud's Public Folder can host static sites — a capability inside the drive, not the Type. When publishing is the purpose, files-as-website is a different application territory.
- **vs Virtual Data Room** (§11): deal-scoped, controlled, transaction-bounded repository vs standing personal collection.

## Uncertainties

- Dropbox and Google Drive official documentation unreachable (timeouts ×2 each) — no product-specific claims about either; the sample's two anchors are carried by market position only. Assertion strength for "all major products" claims is accordingly capped at the four directly observed products.
- Version history for iCloud Drive was not directly observed in the fetched pages (recovery of deleted files was; version restore was not) — kept out of any universal claim.
- Search in iCloud Drive / OneDrive files was not directly observed on the fetched pages (pCloud and Nextcloud search was) — search is held as common, not universal.
- Sync mechanics (block-level vs file-level delta transfer) were not researched at precision level — deliberately omitted everywhere.
- Exact quota sizes, retention windows (other than iCloud's directly observed 30-day Recently Deleted), and link-expiry defaults are deliberately omitted per the precision rule.

## Final Synthesis

A Personal Cloud Drive is defined by three jointly-held structures: the personal file collection of record (generic files in user-managed folders, owned by a personal account with its own capacity, on storage remote to the user's devices), device-independent reachability (the collection reachable from all the user's devices through the product's web and client surfaces, the remote copy being a primary working copy), and the file-operation loop (the user organizes and operates on the remote collection — upload, download, move, rename, delete, share). Sync, sharing machinery, recovery, placeholders, auto-upload, search, and previews are the common mature structure that makes the Type practical today but do not define it; identity substrate, deployment, interaction posture, encryption posture, and business model are variants. The Type sits between the File Sync Application (the engine), the File Manager (local organization over whatever storage exists), and the File Transfer Application (delivery events) — all three seams already ratified from the sibling passes and confirmed here from the drive side.
