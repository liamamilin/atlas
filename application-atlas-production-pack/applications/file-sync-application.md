# File Sync Application

## Overview

A **File Sync Application** keeps a designated set of files consistent across multiple endpoints — several of a person's devices, a team's computers, or a server — by automatically detecting changes on any replica and applying them to the others.

The defining core is small:

```text
Sync scope (a designated folder or file set)
└── Replicas on multiple endpoints (devices and/or a server)
    └── Automatic propagation engine
        └── Convergence toward a consistent state
```

Four properties. If any one is removed, the product is no longer recognizable as file sync:

- **Sync scope** — the user designates a folder (or a defined set of folders/files) for synchronization; everything outside it is out of scope. Without a designated scope, the product is generic file copying.
- **Multiple replicas** — the scope exists in more than one place, each endpoint holding a copy. With a single location, the product is a local file manager.
- **Automatic propagation** — the application itself detects changes and applies them to the other replicas; the user does not perform a per-change action. Without this, the product is manual file transfer.
- **Convergence** — the engine drives all replicas toward the same state, propagating creations, modifications, renames, and deletions, and reconciling divergent states. Without this, the product is a one-shot copy job or a backup.

Everything commonly associated with the modern category — cloud storage, user accounts, web and mobile access, online-only placeholder files, version history, sharing links, polished status icons — is widespread in current products but is not part of the defining core. Peer-to-peer tools with no cloud and no accounts, self-hosted server setups, and command-line synchronizers all satisfy the definition. When the center of gravity shifts from *keeping replicas consistent* to *storing files in one place for access and sharing*, the product is drifting toward a different Application Type (Personal Cloud Drive).

## Users & Context

The primary user is an individual who works on the same files from more than one place — a laptop and a desktop, a computer and a phone, home and office machines — and wants edits made anywhere to appear everywhere without manual copying.

Secondary users and contexts:

- **Team members** who share a synced folder so that everyone's copy of a working set stays current.
- **IT administrators** in organizations who deploy and govern sync clients across many machines, control which folders sync, and manage accounts and policies (common in organizational deployments of hub products).
- **Self-hosters and privacy-conscious users** who run their own server or a device-to-device mesh instead of a vendor's cloud.

The application is unusual among desktop applications in that its normal state is *invisibility*: it runs continuously in the background, and the user interacts with it mainly through a status icon, occasional notifications, and settings — while doing the actual file work in the ordinary file manager and applications.

## Core Model

### The Defining Core

```text
Sync scope (folder / file set)
   held as replicas on:  device A · device B · server (optional)
          ↑ automatic change propagation ↓
   convergence: all replicas driven to a consistent state
```

- **Sync scope** — the unit of designation. In practice it is almost always a folder: the user picks a directory (or accepts a default one) and everything inside it participates. Some products let the user refine the scope further (choose subfolders per device, exclude patterns).
- **Replica** — one endpoint's copy of the scope. A replica can be a full copy of every file, or (in hub products) a partial copy in which some files exist only as online-only placeholders.
- **Change** — a creation, modification, rename, or deletion detected on any replica. Changes are the currency of the system: the engine's job is to move every change to every other replica.
- **Conflict** — the state in which the same file has diverged on two replicas between sync runs. Sync applications do not silently merge file contents; they preserve both versions side by side and leave the merge to the user.
- **Converged state** — the condition in which every replica holds the same content. The engine works continuously toward this state and surfaces progress and problems through status indicators.

### Standard Capabilities

Mature products commonly add the following. They make sync practical and safe, but a product lacking some of them can still be clearly a file sync application.

- **Change detection machinery** — filesystem watching (immediate notice of changes) combined with periodic rescans that catch anything the watcher missed.
- **Local state/index** — each replica keeps a record of what it believes the scope contains, so the engine can compute what differs instead of comparing whole folders by hand.
- **Conflict copies** — when two replicas diverge on the same file, the engine keeps both versions: one keeps the original name, the other is preserved as a renamed copy (typically marked with a timestamp or device marker). The user compares and merges manually.
- **Version history and recovery** — safety nets for the fact that deletions and overwrites propagate: previous versions of files, a trash-like store of replaced or deleted files, and restore facilities; some products extend this to restoring an entire scope after events such as ransomware.
- **Selective sync** — the user chooses which folders a particular device carries. Deselected folders are removed from that device but remain available on the others (and, in hub products, online).
- **Online-only placeholder files** — in hub products, files can be represented on a device as placeholders that download on demand, so the scope is visible everywhere without consuming disk space.
- **Status surfaces** — a background-agent icon with distinct states (up to date, syncing, paused, offline/disconnected, error) plus per-file overlay icons in the OS file manager.
- **Exclusions** — ignore patterns and built-in rules that keep transient files, system files, and unsyncable names out of the scope.
- **Network controls** — bandwidth limits for upload/download, proxy settings, and pause/resume.
- **Sharing** — in peer-to-peer tools, sharing means adding another of your own (or a collaborator's) device to a folder; in hub products it means granting other people access to a folder through links or permissions.
- **Notifications and an activity/error list** — the engine reports problems (a file that could not be synced, a conflict, a lost connection) rather than failing silently.

### One Structure, Many Implementations

The core model is written in conceptual terms. Implementations differ on two major axes:

```text
Concept:      Where replicas live (topology)
Realizations: cloud relay hub (a vendor's cloud holds the reference copy)
              self-hosted server hub (your own server holds it)
              peer-to-peer mesh (devices hold it among themselves, no server)

Concept:      How endpoints are trusted (identity)
Realizations: user account sign-in (personal or organizational)
              device key-pair pairing (mutual exchange of device identifiers, no accounts)
```

A reader who has only seen the cloud-hub, account-based pattern should still be able to recognize a server-hub or device-paired product as the same Type from the core model.

## How It Works

### Connect endpoints and establish trust

```text
Install the sync application on each device
→ sign in to an account (hub products)
   or exchange device identifiers between the two devices (peer-to-peer products)
→ the endpoints can now find and authenticate each other
```

There is no content yet — this step only establishes who may talk to whom.

### Designate the sync scope

```text
Choose or create a local folder as the sync scope
→ connect it to the other side:
   share the folder with another device (P2P)
   or add a "folder sync connection" between a server folder and a local folder (server hub)
   or accept the product's default synced folder backed by cloud storage (cloud hub)
→ optionally refine the scope: choose subfolders for this device, set ignore patterns
```

### Initial reconciliation

The first run is the largest: the engine scans the scope on each side, builds its state index, computes the differences, and transfers whatever is missing until all replicas hold the same content. Depending on product and scope size this can take minutes to hours, and it is the phase most visible to the user.

### The continuous loop

After the initial reconciliation, the application settles into its defining loop:

```text
Detect a change on any replica (watcher event or rescan)
→ record it in the local state index
→ propagate it to the other replicas
   (whole file, or in some products only the changed blocks of a large file)
→ apply each change safely: write to a temporary file, then move it into place
→ update status indicators on all affected surfaces
→ repeat, continuously, in the background
```

Two properties of this loop matter more than any feature list:

- **It is automatic and standing.** Nothing about it is per-change user action; the relationship between replicas persists whether or not the user is thinking about it.
- **It includes deletions and renames.** A file removed on one replica is removed on the others; a renamed file is renamed everywhere. This is what makes the replicas one working set rather than a pile of copies — and it is also the behavior that makes safety nets (versioning, trash, restore) important.

### Handle conflicts

```text
The same file changes on two replicas between sync runs
→ the engine cannot know which version is "correct"
→ it keeps both: one becomes the base file (and continues receiving updates),
   the other is preserved as a renamed conflict copy
→ the user is notified (notification, badge, error list)
→ the user compares the two versions, merges what matters, deletes the copy
```

The invariant across products: **conflicting content is never silently merged or silently discarded.** Both sides survive until a human decides.

### Manage the scope over time

```text
Pause syncing (temporarily stop transfers without dismantling anything)
→ adjust selective sync (carry fewer or more folders on this device)
→ edit exclusions (keep new transient file types out)
→ recover when needed (restore a previous version, a deleted file, or the whole scope)
→ or remove the sync connection entirely (stop syncing; local copy may be kept or removed)
```

### Capability tiers

**Defining core** — without these, not file sync:

- designated sync scope
- replicas on multiple endpoints
- automatic change propagation
- convergence including deletions and renames
- conflict preservation (both sides kept, user resolves)

**Standard capabilities** — present in most mature products:

- change detection machinery and local state index
- version history / deleted-file recovery / restore
- selective sync
- status icon states and per-file overlay icons
- exclusions / ignore patterns
- bandwidth limits, proxy, pause/resume
- sharing of the scope (with devices or with people)
- notifications and activity/error list

**Variant / optional** — depends on product family and deployment:

- online-only placeholder files (hub products)
- web and mobile access to the synced content (hub products)
- direction modes: send-only reference copies, receive-only mirrors
- end-to-end or zero-knowledge encryption; untrusted-device encryption
- organizational administration (deployed clients, policies, org accounts)
- command-line operation and headless daemons

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Background agent icon (system tray / menu bar)

The primary everyday surface. Shows the engine's state at a glance — commonly: up to date, transferring, paused, disconnected, error. A click opens the main dialog; a right-click offers quick actions (pause/resume, open the synced folder, settings, quit).

### Main dialog / settings window

The control surface for the engine: connection and account status, the list of sync scopes (folders) with their per-folder state, storage or quota information where relevant, and actions — add a sync connection, choose what to sync, pause, remove a connection. Network settings (bandwidth, proxy) and exclusion editing usually live here too.

### File manager integration

The user's file work happens in the ordinary file manager; the sync application decorates it:

- **overlay icons** on files and folders showing per-item sync state (in sync, syncing, ignored, error)
- **context-menu entries** for sync-specific actions (share a folder, free up space by making a file online-only, view version history)

### Activity / error list

A running record of what the engine did and what failed: completed transfers, conflicts needing attention, files that could not be synced and why. This is where the user goes when the status icon turns yellow or red.

### Web interface (hub products)

In cloud- and server-hub products, a browser view of the synced corpus: browse, upload, share, and restore — always showing the full scope even on devices whose local selection is narrower. In peer-to-peer products the analogous surface is a local admin GUI for configuring folders and devices rather than for accessing content.

### Mobile clients

Mobile apps in hub products provide viewing, uploading, and sharing, and in some products automatic photo upload from the phone; two-way file-level sync on mobile is shallower than on desktop in some products and should be treated as a variant depth, not a constant.

### Command line / headless operation

Some products (particularly open-source and server-oriented ones) offer command-line clients, configuration files, or a headless daemon with a web-administered GUI — the same engine without a desktop-agent shell.

## Important Rules / Behaviors

### Deletions propagate

The single most consequential behavior of the Type: removing a file inside the scope removes it from every replica. Mature products wrap this in safety nets (trash/versioning/restore), but the propagation itself is the defining behavior — it is what makes the replicas one working set.

### Conflicts are preserved, never merged

When replicas diverge on the same file, the engine's universal answer is to keep both versions — one under the original name, one as a renamed conflict copy — and hand the merge to the user. Products differ in naming and in whether the conflict copy itself propagates to other replicas; the preserve-both principle does not vary.

### Changes are applied atomically

Sync engines commonly write changes to a temporary file and move it into place rather than editing the destination directly, so an interrupted transfer does not leave a half-written file wearing the real filename. Transient temp files may briefly appear in the scope and are excluded from syncing.

### The scope has boundaries, and they are enforced

- Ignore patterns and built-in rules keep transient/system files out.
- Files with characters or path lengths that cannot be represented on some file systems are refused or renamed, with the problem surfaced in the error list.
- Files that fail repeatedly may be quarantined — removed from the sync set — with an option to retry, so one bad file does not stall the whole scope.
- Case-sensitivity differences between file systems can produce conflicts that only manual renaming resolves.

### Device-level settings are independent

Which folders a device carries, and local settings generally, are per-device choices. Deselecting a folder on one computer does not deselect it anywhere else; the content remains on the other replicas (and online, in hub products).

### Pausing is not disconnecting

Pause temporarily halts transfers while keeping the configuration and (in some products) continuing to update file lists; removing a sync connection ends the relationship for that folder. Products make this distinction visible because the consequences differ sharply.

### Direction can be constrained

Some products allow a folder to be configured as send-only (a reference copy whose state can be forced onto the cluster) or receive-only (a mirror or backup destination whose local changes can be reverted). These modes reuse the same engine with the authority deliberately one-sided.

## Variants

- **Cloud-hub sync** — a vendor's cloud holds the reference copy; accounts, web/mobile access, sharing links, quotas, and placeholder files cluster around the engine. The dominant consumer and team realization.
- **Self-hosted server sync** — the same hub shape, but the server is the user's own (or their organization's); chosen for data control. Often bundled with a wider file-sharing and collaboration platform.
- **Peer-to-peer mesh sync** — devices synchronize among themselves with no central store; trust is established by exchanging device identifiers rather than accounts; discovery/relay services may assist connectivity. Chosen for privacy and for avoiding storage quotas.
- **Platform-native sync** — sync machinery embedded in an operating system or platform ecosystem, tied to the platform's account and preinstalled by default.
- **Direction-constrained deployments** — send-only reference copies (publishing one authoritative state) and receive-only mirrors (backup-like destinations).
- **Enterprise-managed sync** — organizationally deployed clients with admin-controlled folder policies, org-scoped accounts, and audit/compliance postures.
- **Encryption-posture variants** — transport-only encryption as the baseline; server-side encryption, end-to-end/zero-knowledge designs, and encrypted-relay storage as stronger postures.

A variant remains a variant unless it changes the core model itself. For example, a product whose primary surface is *storing and accessing files in one place* (web-first storage with sync as an add-on) is better understood as a Personal Cloud Drive that includes a sync capability, not as a pure File Sync Application.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Personal Cloud Drive | closest sibling; frequently bundled | storage-first: a place where files live, accessed via web/mobile with quotas and sharing; sync is one capability of it. Remove the sync engine and a cloud drive remains; remove the cloud storage and a sync engine remains (P2P tools) |
| File Transfer Application | adjacent | one-shot, user-initiated, point-to-point delivery of files; no standing relationship, no reconciliation, no deletions propagation |
| File Manager | adjacent | local organization and navigation of files; no replicas, no propagation. Sync clients integrate with file managers but the manager is not the engine |
| Backup Management / backup software | overlapping use, different semantics | protective copies where the source stays the working set and the destination is not edited; retention and restore are the point. In sync, any replica may be a source of change and the engine reconciles them all |
| Version Control System | structural cousin for source code | records explicit commits and history with semantic merge; sync propagates current file state with no semantic merge — conflicts become parallel copies for a human to merge |
| Managed File Transfer | same noun, different world | enterprise B2B movement of files between organizations on schedules with audit and workflow guarantees; logistics for exchange, not replica convergence of a working set |
| Data Replication Platform | same verb, different object | replicates database/data-store state, not a user-visible file scope |

The boundary with **Personal Cloud Drive** is the most important one, because mainstream products bundle both. The structural test: the File Sync Type is defined by the *engine* (scope, replicas, propagation, convergence); the cloud drive is defined by the *store* (a place files live, accessed and shared from anywhere). Products that lead with the store are cloud drives with a sync capability; products whose essence is the engine — including ones with no store at all — are file sync applications.

## Representative Products

- **Syncthing** — open-source peer-to-peer sync; device-key identity, no cloud, no accounts; the clearest demonstration that the engine alone constitutes the Type.
- **Nextcloud (Desktop Client + Server)** — self-hosted server hub with desktop/mobile clients; the self-hosting and organizational pole.
- **OneDrive** — platform-native cloud-hub sync embedded in the operating system ecosystem; the dominant mainstream realization, consumer and enterprise.
- **Dropbox** — the commercial cloud-hub archetype for consumers and teams (market anchor; its documentation was not directly reachable during research, so no product-specific claims are made about it).
- **Resilio Sync** — commercial peer-to-peer sync descended from BitTorrent technology (secondary anchor for the P2P pole; not directly documented in this research).

## Sources

Research date: **2026-09-07**

- Syncthing documentation:
  - Getting Started — https://docs.syncthing.net/intro/getting-started.html
  - Understanding Synchronization — https://docs.syncthing.net/users/syncing.html
  - Folder Types — https://docs.syncthing.net/users/foldertypes.html
  - File Versioning — https://docs.syncthing.net/users/versioning.html
- Nextcloud user manual:
  - Desktop and mobile synchronization — https://docs.nextcloud.com/server/latest/user_manual/en/files/desktop_mobile_sync.html
  - Using the Synchronization Client — https://docs.nextcloud.com/server/latest/user_manual/en/desktop/usage.html
  - Conflicts — https://docs.nextcloud.com/server/latest/user_manual/en/desktop/conflicts.html
- Microsoft Support (OneDrive):
  - OneDrive help & learning — https://support.microsoft.com/en-us/onedrive
  - Sync with OneDrive (category) — https://support.microsoft.com/en-us/onedrive/category/sync-with-onedrive
  - Choose which OneDrive folders you want to sync — https://support.microsoft.com/en-us/onedrive/choose-which-onedrive-folders-you-want-to-sync-on-windows-or-macos

> Sourcing limitation: official documentation for Dropbox, Resilio Sync, and Google Drive for desktop could not be fetched from the research environment (repeated timeouts). These products are retained as market anchors only, and no product-specific operational claims about them appear in this document. Claims that would have required their evidence are worded at cross-product level using the three directly documented products, or omitted.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
