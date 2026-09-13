# Research Notes — File Transfer Application

## Research Goal

Understand what a File Transfer Application is as an Application Type: what its defining core is, what users actually do with it, how a transfer works end-to-end, and where its boundary lies against neighboring file-handling Types (Personal Cloud Drive, File Sync Application, File Manager, Managed File Transfer) and message-attachment patterns (email, IM).

Directory context: the leaf sits under "03.15 Files" alongside File Manager, Personal Cloud Drive, and File Sync Application — i.e., a personal/productivity tool family, not the enterprise data-movement family (the directory holds "Managed File Transfer" as a separate leaf under 13). This placement guided the initial hypothesis.

## Initial Boundary

Hypothesis before research:

- Core use: get a file or set of files from one holder (person, device, host) to another specific holder, as a delivery event.
- Users: individuals and small teams; also power users moving files between their own devices or to a server.
- Nearest Types: Personal Cloud Drive (persistent storage + sharing), File Sync Application (continuous mirror), File Manager (local organization), Managed File Transfer (enterprise system-to-system pipelines — separate leaf), Email/IM attachments (message-centric).
- Likely boundary: the *transfer event* is the product, not storage, not organization, not a message.
- Unknowns: does the Type include protocol clients (FTP/SFTP)? Is reverse-direction intake (file requests) core or variant? Is the "transfer" a first-class tracked object in products, or just an action?

## Research Questions

1. What is the unit of work — how does each product model "a transfer" (link, key, session, queue entry)?
2. How is the destination addressed — email recipient, shareable link, nearby-device discovery, host credentials?
3. What does the system do with the files — hold them (for how long), stream them through, or never store them?
4. What transfer machinery is exposed — progress, queue, pause/cancel, resume, speed limits, integrity?
5. What lifecycle/states does a transfer have (composing → uploading → awaiting download → downloaded → expired/failed)?
6. What rules and limits shape behavior — size caps, availability windows, recipient counts, passwords, plan tiering?
7. What does the receiving side experience, and is there a reverse direction (file requests / drop links)?
8. Where is the line to Personal Cloud Drive, File Sync, Managed File Transfer, and message attachments?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers — and to cover the three transport families:

| Product | Pole / philosophy | Tier |
|---|---|---|
| WeTransfer | consumer cloud-relay sender; anonymous-first, link/email delivery, expiry-based | consumer freemium → enterprise |
| Smash | cloud-relay sender positioned on no-size-limits + ephemeral links; developer API | consumer freemium → teams |
| LocalSend | open-source, no-infrastructure LAN device-to-device transfer (AirDrop-style) | individual, cross-platform |
| FileZilla | direct protocol client (FTP/FTPS/SFTP); power-user/host-addressed transfers | power user / technical |

Historical / platform-native checks (reasoning targets, not researched products): FTP clients of the dial-up era, IrDA/Bluetooth "send file" utilities, OS-native nearby sharing (e.g., AirDrop-class), Windows folder sharing, email attachments. Enterprise MFT (separate leaf) used only as a boundary reference.

## Sources

- WeTransfer Help Center (reachable): https://wetransfer.com/help-center — index; https://wetransfer.com/help-center/how-to — article index (38 articles); https://wetransfer.com/help-center/how-to/send-a-transfer — send flow. Fetched 2026-09-07.
- Smash: https://fromsmash.com/ — root page incl. quick-start, FAQ (storage, security, availability windows), product surfaces. Fetched 2026-09-07.
- LocalSend: https://localsend.org/ — root page incl. Features, How It Works, FAQ. Fetched 2026-09-07.
- FileZilla Wiki (official documentation base): https://wiki.filezilla-project.org/ — main page; https://wiki.filezilla-project.org/FileZilla_FTP_Client — client features. Fetched 2026-09-07.
- Send Anywhere (planned sample, P2P/cloud-hybrid with key-based addressing): https://send-anywhere.com/ and /faq returned 403 twice → abandoned per source-access rules. **Consequence: no key/short-code-addressed product is directly evidenced in this sample; that addressing pattern is recorded as unverified, not asserted.**
- Dropbox Transfer (planned sample): help.dropbox.com timed out twice → abandoned. Consequence: no drive-vendor transfer module directly evidenced; the drive-vs-transfer boundary rests on the four sampled products plus canonical reasoning.

Evidence layers used below: **A** = directly observed on an official product source; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + boundary reasoning.

---

## Product Observations

### WeTransfer (cloud-relay sender)

Evidence layer A unless noted.

- Core object is the **"transfer"**: "Add your files, choose between an email or link transfer, and click Transfer." A transfer = file set + recipient/addressing + message/title + settings (expiry, password).
- Two addressing modes: **email transfer** (sender enters own + recipients' addresses; recipients get a download link by email, each sent separately so recipients don't see each other) and **link transfer** (upload produces a shareable link the sender distributes themselves).
- Flow (desktop/mobile/app): add files (+ button or drag-drop, folders supported — folder structure otherwise flattened into a zip), fill recipient details or switch to link mode, click Transfer; upload to WeTransfer servers.
- **Handover semantics, directly documented**: "WeTransfer uploads a copy of your files to our servers. Your originals stay on your device. Once a transfer expires, the copy on our servers is deleted, but your local files are unaffected."
- **Expiry is a first-class transfer property**: set/modify expiry before uploading, change after sending, set a default expiry (paid); article "How long are transfers available to download?" (availability by plan; recovery option for top plans). Precise day-counts are plan-dependent — not asserted here.
- Transfer is a **managed, stateful record**: "Your account's Transfers panel" reviews sent and received transfers (Sent panel actions; Received panel layout; what happens to expired transfers); "view a summary of a transfer — recipients, files, expiry, and message — while a transfer is in progress or after it completes".
- **Delivery/download supervision**: confirmation email on upload; second confirmation when the recipient downloads; download counts and download-status labels across "public email, tracked, and restricted transfers"; Access Control enables tracked or restricted downloads with an access list and download activity.
- Security options: password on transfers (stored so it can't be recovered — sender shares it); watermarked preview that prevents downloading; (Security & Privacy category exists with 22 articles — encryption posture not fetched, so not asserted).
- **Reverse direction exists**: File Requests — create a request link, others upload to it (uploading requires a verified email so the requester sees who uploaded); received uploads behave like transfers with expiry control; managed in a "Requested" section.
- Transfer manipulation after sending: add/remove files and folders ("editing a transfer after sending"); forward an active transfer to new recipients; give specific recipients permission to add files (recipient edit access); name/title transfers; delete transfers from Sent panel.
- Recipient side: download a transfer on desktop/mobile/app; "where downloaded files are saved" (per-platform); previews ("which file formats can be previewed, file size limits"); comments on previews.
- Notifications: emails and push notifications for upload, download, expiry reminders, bounced recipients.
- Sender identity: email address required (verification for anonymous senders on mobile); account optional for basics; free accounts have recipient caps (≤10 per email transfer; paid ≤50; mobile web ≤3 without login) — plan-shaped limits, direct evidence.
- Adjacent surfaces that are **not** the Type: Albums (shared photo albums), WeTransfer Sign (document signing), WeTransfer Collect (request/gather), paid transfers (sell files via Stripe), personal WeTransfer page with custom URL and wallpapers, branded email/backgrounds, editorial backgrounds. These are L3; noted to avoid scope creep in the final doc.

### Smash (cloud-relay sender, no-size-limit positioning)

Evidence layer A (root page + FAQ; help center exists at /help/ but was not fetched).

- Same core flow: click/drag-drop files or folders → set options → upload → hosted on Smash's regional servers "awaiting download by your recipient" → download link generated → share the link via any communication tool (email, WhatsApp, text, iMessage).
- Explicit framing of the Type's semantics: "You aren't sending a large file; you're sending a link to download it."
- Options: Email or Link transfers, password protection, expiry dates, email notifications.
- **Ephemerality is a design principle**: "ephemeral Transfers"; documents available for a limited time, 1–30 days (FAQ, direct evidence); drop links 1–365 days. Availability managed by the link creator; positioned as both security and sustainability feature.
- **Reverse direction (paid)**: Receive mode — create a drop link, share it, others upload, requester is notified and downloads; "track and manage your received file transfers".
- Notifications at "every step of the sending and downloading process" (email).
- Infrastructure posture: uploads land on servers geographically close to the sender, nine storage regions; encryption in transit and at rest; password protection; external security audits (named firm) — marketing-level claims, recorded as such.
- Adjacent surfaces (L3): Outlook plugin (send/receive without leaving the mail client — explicitly framed as bypassing attachment size limits), developer API ("managing petabytes… integrate into websites/apps/SaaS"), mobile/Mac apps, pricing tiers (Freemium/Pro/Team), carbon-footprint positioning, "Smash vs WeTransfer" comparison page.
- No size limits (positioning claim; "any size" repeated across FAQ — marketing-level, recorded as positioning not as a measured fact).

### LocalSend (no-infrastructure LAN transfer)

Evidence layer A (official site: Features / How It Works / FAQ).

- Positioning: "Share files without the cloud. Fast, private, offline." Open source, cross-platform (Windows, macOS, Linux, Android, iOS); web app variant.
- Model: install on all devices → no account, no login, no servers → **select files → tap a nearby device → transfer over the local network**. Destination addressing = **nearby-device discovery** (device list), not links or emails.
- "Any file type is supported" — photos, videos, documents, or text (text/message payload evidenced).
- Security: transfers encrypted (HTTPS/"end-to-end encryption" claimed on the site); optional PIN verification for extra security (receive-side confirmation).
- Handover semantics: files "saved to your device's Downloads folder by default, but you can change this in settings" — the receiver's file store is the endpoint; nothing is warehoused in between.
- "Works completely offline. Your data never leaves your local network." "No bandwidth limits" (local-network-speed transfers).
- No expiry, no stored copy, no sender-side tracking panel — delivery is synchronous device-to-device. This is the minimal-infrastructure pole of the Type.

### FileZilla (direct protocol client)

Evidence layer A (official wiki main page + client page).

- Self-description: documentation for "download[ing], install[ing], compil[ing] and us[ing] the FileZilla Client and FileZilla Server software to transfer files across the Internet."
- Client supports FTP, FTPS (FTP over SSL/TLS), SFTP; cross-platform (Windows, Linux, *BSD, macOS).
- Transfer machinery: **transfer queue**, **resume** and transfer of large files (>4GB noted), configurable speed limits, drag & drop, filename filters, remote file search, network configuration wizard, proxy support (HTTP/1.1, SOCKS5, FTP), logging to file.
- **Destination addressing = host endpoint**: Site Manager (powerful, with bookmarks) stores hosts + connection settings; credentials/protocol per site. The remote side is a file server, not a person.
- Two-way relationship with the remote store: directory comparison, synchronized browsing, and remote file editing implemented as "downloading it to a temporary place and re-uploading it upon saving" — the client is a window onto a remote file system, not a store of its own.
- The project also ships a Server product — evidence that the same file-transfer job can be split into client and server applications; the client remains the transfer application.
- This pole passes the historical check trivially: an FTP client of the 1990s has the same structure (choose local files → addressed host → supervised transfer → files land on the other side).

---

## Cross-product Comparison

| Dimension | WeTransfer | Smash | LocalSend | FileZilla |
|---|---|---|---|---|
| Primary job (A) | send file set to person(s) via email/link | send file set via link ("you're sending a link to download it") | send files to a nearby device over LAN | transfer files between local machine and remote host via FTP/FTPS/SFTP |
| Unit of work (A) | "transfer" — a named, tracked record with recipients/files/expiry/message | "transfer" with link + options | a transfer request to a selected device | queued transfer items in a session; site-scoped |
| Destination addressing (A) | recipient email addresses, or shareable link | shareable link; drop link for receiving | nearby-device discovery (device list); optional PIN | host address + protocol + credentials (Site Manager) |
| Storage posture (A) | copy held on servers until expiry, then deleted; originals untouched | ephemeral availability window (1–30 days evidenced) | none — direct device-to-device | none — client streams through; remote store is external |
| Delivery supervision (A) | upload confirmation + download confirmation; download counts/status; tracked/restricted downloads | email notifications every step; received-transfer tracking | in-app transfer progress | queue with progress; resume; speed limits; logs |
| Rules/limits observed (A) | plan-shaped recipient caps; expiry by plan; password option | availability windows; password; plan tiers | local-network scope; PIN | protocol/network constraints; speed limits |
| Identity model (A) | optional account; verified email for anonymous send | optional account | none | host credentials only |
| Reverse direction (A) | File Requests (verified-email upload) | Receive mode / drop links (paid) | bidirectional (any device can send) | client↔server both directions |
| Common-not-core extras seen (A) | previews, comments, transfer editing after send, forwarding, watermarks | Outlook plugin, API, receive mode | text sharing, web app | remote editing, directory compare, synchronized browsing |

Cross-product reading (B):

- All four share: a sender-selected file set; a *specific* destination (person, device, or host); application-managed, supervised delivery; handover semantics (the endpoint's store receives the files; the application itself is not the user's long-term store).
- All four expose delivery supervision: progress/queue plus some form of completion signal (download confirmation, notification, queue status).
- Three of four expose transfer records the sender can revisit (WeTransfer Transfers panel, Smash received-transfer tracking, FileZilla queue/site history); LocalSend's synchronous model has the least record-keeping — record-keeping depth scales with asynchrony.
- Low-friction addressing for human recipients (link or discovery) appears wherever the recipient is a person; credential addressing appears where the destination is a host.
- Reverse-direction intake appears in both cloud-relay products; LocalSend is inherently bidirectional; FileZilla is inherently two-way against a host. Direction is a variant axis, not a definition.

---

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (deliberately minimal)

```text
Sender-selected file set
└── Addressed destination (a specific person / device / host — never broadcast)
    └── Application-managed delivery (the transfer is supervised: connection,
        progress, completion or failure — a trackable event, not a manual copy)
        └── Handover semantics (the destination's store receives the files;
            the application itself is not a persistent file warehouse)
```

Removal tests:

- Remove the sender-selected file set → no unit of work; not this Type.
- Remove the addressed destination (make it public broadcast/discovery) → file-hosting/distribution surface, not a transfer.
- Remove application-managed delivery → the OS copy dialog / manual media handoff; no application Type.
- Remove handover semantics (the system holds an organized persistent store of the user's files) → Personal Cloud Drive.

Historical check (§24): 1990s FTP clients (file set → addressed host → supervised transfer → handover) fit; IrDA/Bluetooth send-file utilities fit; OS-native nearby sharing fits as a platform-native realization. Nothing in L0 assumes the web, accounts, links, or the cloud — a link-less, account-less, server-less product (LocalSend) satisfies it, and so does a host-addressed protocol client. **The L0 is transport-agnostic by construction.**

### L1 — Common Mature Structure (very common, not definitional)

- Progress/queue machinery: progress surfaces, pause/cancel, **resume after interruption** (A: FileZilla resume; WeTransfer uploader; implied in cloud uploaders — generalize as "common").
- Delivery & download signaling to the sender (download confirmations, notification emails/push, download counts/status) (A: WeTransfer, Smash; B: cross-product).
- Low-friction addressing for human recipients: shareable links, discovery of nearby devices (A: WeTransfer link transfer, Smash link, LocalSend discovery).
- Availability windows/expiry on relayed copies, often user-settable and plan-dependent (A: WeTransfer expiry property, Smash 1–30 days).
- Protection of the delivered file set: passwords, access control / tracked or restricted downloads, receive-side PIN (A: WeTransfer password + Access Control, Smash password, LocalSend PIN).
- Folder support, including bundle/flatten handling (A: WeTransfer folder upload + zip flatten note; Smash folders).
- A transfer-management surface on the sender side (sent/received panels, summaries, delete/forward) (A: WeTransfer; Smash tracking; B).
- Cross-platform clients for both ends of the delivery (desktop/mobile/web/CLI-ish) (A: all four).

### L2 — Variant / Optional Structure

- **Transport family**: cloud relay with temporary storage (WeTransfer, Smash) vs local-network P2P with no infrastructure (LocalSend) vs direct protocol connection to a host (FileZilla). Same L0; different implementations.
- **Identity substrate**: none at all (LocalSend), verified email/account optional (WeTransfer, Smash), host credentials only (FileZilla).
- **Direction**: one-shot send; pull-link download; reverse intake (file requests, drop links — A: WeTransfer, Smash); two-way client↔host (FileZilla); bidirectional device pair (LocalSend).
- **Encryption posture**: protocol-level (FTPS/SFTP), claimed in-transit+at-rest (Smash), HTTPS/E2E claim (LocalSend), transport security implied but not verified for WeTransfer (Security & Privacy articles not fetched — do not assert).
- **Scale/monetization shape**: freemium with plan-shaped size/expiry/recipient caps; paid plans adding recoverability, longer windows, branding; free open-source with none of that.
- **Optional extensions**: previews of transferred formats; comments on previews; transfer editing after send; forwarding; custom sender pages/branding; paid transfers (commerce); Outlook plugins; developer APIs; text-as-payload (LocalSend).
- **Recipient-side behavior**: where downloads land, whether the recipient needs an account (evidence: none of the four require recipient accounts — B), whether download is browser- or app-mediated.

### L3 — Vendor-specific (research notes only; excluded from the final document)

- WeTransfer: email-vs-link toggle mechanics; recipients blind to each other; free ≤10 / paid ≤50 / mobile-web ≤3 recipient caps; "Recoverable" expired transfers for top plans; watermarked previews; recipient edit access; Albums; WeTransfer Sign; WeTransfer Collect; paid transfers via Stripe; personal page with custom URL/wallpapers; Mac app with Finder extension; editorial backgrounds.
- Smash: nine storage regions with sender-proximate upload; named external security-audit firm; 1–365-day drop-link windows; CO2-reduction marketing; "Smash vs WeTransfer" comparison page; API petabyte claims.
- LocalSend: Downloads-folder default with settings override; no ads/trackers stance; web.localsend.org; Apache-2.0 project governance.
- FileZilla: Site Manager/bookmarks; synchronized browsing; directory comparison; >4GB+resume; remote-file edit via temp download+re-upload; companion Server product.

---

## Vendor-specific Findings

(Consolidated from L3 above; all excluded from the canonical document. The most load-bearing exclusions: transfer editing after send (WeTransfer-only evidence), recoverable expired transfers (WeTransfer plans), drop-link day ranges (Smash), synchronized browsing/remote editing (FileZilla). None generalize to the Type on current evidence.)

## Rejected Findings

- **"File transfer = sending links to large files"** — rejected as the definition: it fits only the cloud-relay family and fails the historical check (FTP clients, Bluetooth-era utilities, and LAN tools are unmistakably the same Type).
- **"Transfer apps store files"** — rejected: storage in relay products is explicitly temporary (expiry deletes the copy; Smash's ephemerality is a selling point); LocalSend and FileZilla store nothing. Storage is a transitional implementation detail, not the product.
- **"Accounts are required"** — rejected: LocalSend has no accounts; WeTransfer/Smash make them optional for basics.
- **"The recipient must install the same app"** — rejected: link/email delivery requires only a browser; recipient-install applies to the LAN family only (variant).
- **"6-digit/short-code key addressing is common"** — not asserted: the planned key-based sample (Send Anywhere) was unreachable; no direct evidence in this sample.

## Boundary Findings

| Neighboring Type | Distinction | Removal test ("去掉什么就变成另一个 Type") |
|---|---|---|
| Personal Cloud Drive | Drive = persistent, organized store of the user's own files; sharing/sending is an overlay on that store. Transfer app = delivery event; any copy held is temporary by design. | Make the held copy persistent and organized (no expiry, browsable tree, "my files") → cloud drive. |
| File Sync Application | Sync = continuously maintains a mirror of a folder across devices; transfer = one-shot delivery event with a defined end. | Replace one-shot delivery with continuous two-way mirroring → sync. |
| File Manager | Manager = browsing/organizing a local store; transfer = crossing a boundary between holders. A manager may *invoke* transfers, but its center is the store. | Remove the boundary-crossing delivery (files stay local, organized) → file manager. |
| Managed File Transfer (separate leaf, §13) | MFT = enterprise, system-to-system, scheduled/audited/governed pipelines with compliance machinery. This Type = ad-hoc person/device/host delivery. | Add organizational scheduling, governance, and system-of-record pipelines → MFT. The product families barely overlap in practice (consumer freemium vs enterprise procurement). |
| Email / Instant Messaging | Message-centric: a file is the payload of a message in a conversation. Transfer-centric: the file delivery is itself the object with its own lifecycle and management surface. | Make the message primary and the file incidental → messaging/email. Smash's Outlook plugin explicitly exists to *bypass* message-attachment limits — the products position themselves against attachment failure. |
| Content distribution / file-hosting platform | Broadcast to an anonymous audience with discovery; transfer is to a *specific* addressed destination. | Remove addressing (publish to whoever has/finds the URL as a catalog item) → distribution/hosting. |
| Data Exchange Platform / managed data pipelines | Moves structured data between systems under schema/governance semantics; this Type moves files between holders. | Swap file sets for governed datasets with schema contracts → data exchange. |

Boundary decision recorded for STATUS: **the leaf is defined transport-agnostically** (cloud-relay sender, LAN device-to-device, and protocol-client realizations all satisfy the L0). A narrower reading ("send large files" web services only) would fail the historical check and strand the FileZilla-class family. The transfer-vs-drive seam is held by handover-vs-warehousing semantics, evidenced directly (WeTransfer expiry deletion; LocalSend "no servers").

## Uncertainties

1. **Key/short-code addressing** (pick-up code entered on another device) is a widely known pattern but was **not directly evidenced** (Send Anywhere unreachable ×2). Recorded as unverified; excluded from the final document's claims. A future pass with an accessible key-based product should confirm or refute.
2. **WeTransfer encryption posture** — Security & Privacy category (22 articles) not fetched; no claim made in the final document beyond "password protection" (directly evidenced).
3. **Recipient-account requirement** — none of the four sampled products requires recipient accounts (B-level reading of the flows), but the claim in the final document is kept soft ("typically requires nothing more than a link/notification") because recipient-side surfaces were only partially observed (no recipient download page fetched directly).
4. **Directory intent** — whether the directory author intended protocol clients (FTP) inside this leaf is unverifiable; the research conclusion (include, transport-agnostic) is documented as a judgment with the historical check as justification. Flagged in STATUS as a mild interpretive note, not a taxonomy error.
5. **Relative market size of the poles** — no direct evidence; the final document deliberately does not rank the transport families by popularity.

## Final Synthesis

A File Transfer Application is an application whose defining job is **delivering a sender-selected file set to a specific addressed destination** — a person, a nearby device, or a remote host — **as a supervised, trackable delivery event**, after which the files belong to the receiving side and the application retains at most a temporary copy. Its world contains exactly one primary object — the **transfer** — which may be realized as a tracked record (relay products), a request to a discovered device (LAN products), or queued work against a host (protocol clients). Everything else commonly seen (links, expiry windows, passwords, download receipts, previews, recipient caps, reverse intake links) is market-standard machinery around that one object, and varies by transport family, identity model, and monetization.

The Type's cleanest discriminators: **delivery event vs persistent store** (vs cloud drive), **one-shot vs continuous mirror** (vs sync), **boundary-crossing vs local organization** (vs file manager), **ad-hoc person/device delivery vs governed system pipeline** (vs Managed File Transfer), **file-delivery-centric vs message-centric** (vs email/IM).
