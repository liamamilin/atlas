# Research Notes — Email Client

## Research Goal

Identify the smallest stable invariant that defines the **Email Client** Application Type, and place every other observed feature at the correct abstraction level.

Following `WORKFLOW_v1.1.md §22` and `WRITING_GUIDE_v1.1.md §28`, this document separates:

```text
L0 Defining Invariant
L1 Common Mature Structure
L2 Variant / Optional
L3 Vendor-specific
```

It also separates evidence into layers per `WORKFLOW_v1.1.md §23`:

```text
A Direct Product Observation
B Cross-product Commonality
C Canonical Inference
```

## Initial Boundary

Target:

> Email Client (directory section 01.02 Email Communication)

Nearest confusing Types:

- Webmail Application (same section — highest confusion risk)
- Shared Mailbox Application
- Email Collaboration Application
- Email Marketing Platform (section 06)
- Email Security Gateway / Email Infrastructure Management (sections 15 / 14)
- Feed Reader (section 02.08)
- Instant Messaging Application (section 01.01)
- Task Management / To-do (section 03.06) — bridge via flag/convert-to-task

Working hypothesis:

> An Email Client is a user-facing application that connects to one or more mail accounts on the email system and lets a person read, compose, send, organize, and search the messages of a persistent mailbox store.

The hypothesis is intentionally broader than "desktop app with IMAP folders" — protocol, surface, and organization philosophy are implementation choices, not the defining invariant.

## Research Questions

- What makes a product recognizable as an email client at all, independent of era, platform, or protocol?
- What is the smallest unit of the Type, and what envelope structure does it carry?
- What is the client's relationship to the mail system (transport) and to the mailbox (store)?
- What survives across organization philosophies: folders, labels/tags, search-first, smart-inbox?
- What does the client add beyond the raw mailbox: triage state, threading, drafts, contacts, rules, signatures?
- Where is the structural boundary with Webmail (surface difference?), Shared Mailbox (single- vs multi-person operation?), Email Marketing (personal vs bulk sender?), and IM (asynchronous envelope vs real-time conversation)?

## Representative Products

| Product | Why selected |
|---|---|
| Mozilla Thunderbird | open-source classic desktop client; folder/tag model; provider-agnostic; personal/power-user tier |
| Microsoft Outlook | suite-integrated corporate client (mail + calendar + contacts + tasks); Exchange/M365 tier |
| Apple Mail | platform-native client shipped with macOS/iOS; multi-account consumer tier |
| Spark (Readdle) | modern cross-platform "smart inbox" client; team-collaboration add-ons; prosumer/team tier |

Additional products used for **historical / market-sample breadth** (per `WORKFLOW_v1.1.md §24`), not for primary structural evidence:

- Webmail products (e.g. Gmail, Outlook.com) — same core model delivered in a browser; used for the Webmail boundary, not as primary samples
- Historical desktop/terminal clients (e.g. Eudora, Pine/elm era) — widely-attested structural facts only (account config, message list, compose/reply, folders); no precise claims drawn from them

The webmail and historical samples are the reason surface (installed app vs browser) and protocol (IMAP vs proprietary API) must not be promoted into the defining invariant.

## Sources

Research date: **2026-09-06**

### Source-access Limitation

Per `WORKFLOW_v1.1.md §23`:

- `support.mozilla.org` (Thunderbird Knowledge Base) could not be fetched — the site returned a JavaScript client challenge. Thunderbird evidence is therefore limited to the official product homepage (`thunderbird.net`). Operational Thunderbird details are **not** claimed in the final document.
- `support.microsoft.com` deep help articles returned 404 on the attempted URLs (2 attempts). Outlook evidence is therefore limited to the official help & learning root page (`support.microsoft.com/en-us/outlook`). Operational Outlook details are **not** claimed in the final document.
- No precise numeric limits, time windows, or default settings are stated anywhere in the final document.

### Successfully fetched official sources

- Apple — Mail User Guide for Mac (welcome / TOC): https://support.apple.com/guide/mail/welcome/mac
- Apple — Add and manage email accounts in Mail on Mac: https://support.apple.com/guide/mail/add-and-manage-email-accounts-mail35803/mac
- Apple — Create or delete mailboxes in Mail on Mac: https://support.apple.com/guide/mail/create-or-delete-mailboxes-mlhlp1021/mac
- Spark — product homepage: https://sparkmailapp.com/
- Spark — Help Center root (full KB category tree): https://sparkmailapp.com/help
- Spark — Connect to Your Email Account in Spark: https://sparkmailapp.com/help/add-manage-accounts/connect-to-your-email-account-in-spark
- Spark — Set Aside vs Pin vs Snooze: https://sparkmailapp.com/help/manage-your-inbox/set-aside-vs-pin-vs-snooze
- Thunderbird — product homepage: https://www.thunderbird.net/en-US/
- Microsoft — Outlook help & learning root: https://support.microsoft.com/en-us/outlook

## Product Observations

### Apple Mail (macOS User Guide) — Layer A

- The guide's framing: "send, receive, and manage email for all of your email accounts in one location on your Mac." Accounts include iCloud, Gmail (Google), Exchange, school, work, or other; accounts can be shared with other system apps via Internet Accounts.
- Every account has a set of **standard mailboxes — Inbox, Sent, Drafts, and Trash**; users create their own mailboxes, optionally nested ("like a subfolder").
- Mailbox location duality: **"On My Mac" (local)** vs **on the account's mail server** (accessible from any device using the account). Removing an account removes its messages from the Mac, while **copies remain on the mail server** ("still available from webmail, for example").
- Deleting a mailbox **permanently deletes the mailbox and its contents** and cannot be undone; deleting a *Smart Mailbox* (a saved search) leaves messages in their original locations.
- In work environments, **public read-only mailboxes** may exist (e.g. company-wide public folders); users cannot create mailboxes inside or save messages into them.
- Other surfaces in the guide TOC: write/send (messages, signatures, attachments), read/respond, mark emails to revisit later, search, notifications, delete & manage storage, automatic sorting into **categories (Primary, Transactions, Updates, Promotions)**, import/export mailboxes, attachment markup, junk-mail reduction, sender blocking, privacy protection, settings, keyboard shortcuts. Recent versions add Apple Intelligence writing tools.

### Spark — Layer A

- Account connection: "Spark works with Gmail, iCloud, Yahoo, Exchange, Outlook, Kerio Connect, and other IMAP/EWS email accounts." Connection is a provider-consent flow: the user signs in with the provider, and "your email provider will ask if you allow Spark to access your account." iCloud requires an app-specific password; a troubleshooting article covers enabling IMAP for Gmail accounts.
- The first added account becomes the user's "**email for sync**": logging in with it on a new device syncs personal settings, added accounts, and emails.
- Inbox management KB section: display each account's inbox separately, Smart Search, bulk actions on multiple emails, create folders, spam handling, **threads**, swipe actions, inbox customization, **Smart Folders** (saved searches), **Mark as Done**, **Set Aside vs Pin vs Snooze**, group by sender/domain.
- Triage semantics (from the Set Aside vs Pin vs Snooze article): **Set Aside** moves mail out of the inbox into a holding bubble for later action; **Pin** keeps mail quickly accessible; **Snooze** removes mail and makes it "re-appear as 'new' in your Inbox at a specific time"; all framed as instruments to reach **Inbox Zero**.
- Compose KB section: compose, signatures, attachments, **schedule an email to send later**, follow-up reminders, aliases, rich text, contact groups, automatic Cc/Bcc, quick replies, accept-or-block new senders, large attachments, undo-send timer.
- Teams KB section: shared drafts ("write emails together"), shared threads (private comments on an email), shared links, delegation, **shared inboxes**, read statuses, team roles.
- Other: +AI (compose, summarize/translate, auto-labels, auto-drafts), calendars, third-party integrations (task apps, Slack, Zoom, HubSpot…), Spark CLI ("unified email layer for the AI Agent era").
- Homepage positioning: "Fast, cross-platform email designed to filter out the noise"; works with IMAP / iCloud / Exchange / Outlook / Yahoo / Google.

### Thunderbird — Layer B (homepage only; KB inaccessible)

- Positioning: "Access all your messages, calendars, and contacts in one fast app. Filter and organize the way you like. Manage all accounts separately or in a unified inbox."
- Observed on the homepage: **unified inbox** across accounts, **tag feature**, calendars and contacts in the same app, cross-platform (Windows/macOS/Linux) plus Thunderbird for Android, open source and donation-funded, extensible via add-ons.
- Because the Knowledge Base was unreachable, no operational Thunderbird workflow details are asserted.

### Microsoft Outlook — Layer B (help root only; deep articles inaccessible)

- The help root organizes the product into: **Get started, Add accounts, Email, Calendar & To Do, People & profiles, Share & delegate** (explicitly covering "shared mailboxes, shared folders and shared calendars"), Troubleshoot, IT Pro & admin, and **Copilot in Outlook**.
- Product variants surfaced by the help root: new Outlook for Windows, Outlook for Mac, Outlook.com (consumer webmail), classic Outlook — i.e. the same franchise spans installed clients and webmail.
- Because deep help articles were unreachable, no operational Outlook workflow details (rules, categories, focused inbox specifics) are asserted.

### Historical / market-sample breadth (Layer B, low precision)

- Webmail products deliver the same core model (account, message list, compose, folders/labels, search) in a browser, bound to the provider's service.
- Historical desktop/terminal clients (Eudora, Pine/elm era, early Outlook Express) are widely attested to have had account configuration, a message list, compose/reply/forward, and folder-based storage — i.e. the same core structure without modern additions (threading UI, AI, push notifications).
- These samples confirm the abstraction below: surface, protocol, and organization philosophy are all implementation layers. The Type survives all of them.

## Cross-product Comparison

| Finding | Apple Mail | Spark | Thunderbird | Outlook | Webmail (boundary ref.) | Abstraction level |
|---|---|---|---|---|---|---|
| connects to external mail account(s) | yes (iCloud/Google/Exchange/other) | yes (IMAP/EWS/Exchange/…) | yes (provider-agnostic) | yes (M365/Exchange-centric) | yes (provider-bound) | L0 |
| message as structured unit (sender/recipients/subject/body/attachments) | yes | yes | yes | yes | yes | L0 |
| compose → send into the email system | yes | yes (+ send later, undo send) | yes | yes | yes | L0 |
| receive → persistent mailbox store | yes (server + "On My Mac" local) | yes (server + vendor sync layer) | yes | yes | yes (server) | L0 |
| standard containers (inbox/sent/drafts/trash…) | yes (explicit standard set) | yes (folders + system views) | yes | yes | yes | L1 |
| user-created containers (folders/labels) | yes (nested mailboxes) | yes (folders, smart folders) | yes (folders + tags) | yes | yes (labels) | L1 |
| read/unread + triage actions | yes | yes (Done/Set Aside/Pin/Snooze) | yes | yes | yes | L1 |
| conversation threading | yes (modern versions) | yes (threads KB section) | yes | yes | yes (conversation view) | L1 |
| search over the store | yes | yes (Smart Search) | yes | yes | yes | L1 |
| contacts / recipient autocomplete | yes (system contacts) | yes (contact suggestions) | yes (contacts in-app) | yes (People) | yes | L1 |
| drafts | yes (standard mailbox) | yes (drafts; shared drafts in teams) | yes | yes | yes | L1 |
| signatures | yes | yes | yes | yes | yes | L1 |
| attachments handling | yes (view/save/markup) | yes (attach, large-attachment flow) | yes | yes | yes | L1 |
| multiple accounts | yes | yes (+ unified or per-account inbox) | yes (separate or unified inbox) | yes | usually single | L1 |
| junk/spam surface + sender blocking | yes | yes (spam handling, block senders, Gatekeeper) | yes | yes | yes | L1 |
| rules / automatic sorting | yes (auto-sort categories) | yes (smart folders, auto-labels) | yes (message filters, per KB index) | yes (rules, per help structure) | yes (filters) | L1 |
| notifications | yes | yes (badges, customization) | yes | yes | yes | L1 |
| protocol substrate (IMAP/POP/EWS/API) | mixed (provider-dependent) | IMAP/EWS + provider APIs | IMAP/POP (provider-agnostic) | Exchange/M365-centric | proprietary (provider) | L2 |
| surface: installed app vs browser | installed (macOS/iOS) | installed (Mac/Win/iOS/Android) | installed (desktop/Android) | installed + webmail variant | browser | L2 |
| organization philosophy | folders + auto categories | smart inbox / triage-first | folders + tags | folders + suite views | labels + search-first | L2 |
| suite integration (calendar/contacts/tasks) | system apps adjacent | calendar + integrations | calendar + contacts in-app | deep (Calendar & To Do, People) | varies | L2 |
| vendor sync layer across devices | iCloud (platform) | Spark sync ("email for sync") | local profiles / account sync | Microsoft account / Exchange | provider account | L2 |
| team collaboration on email | no (public read-only mailboxes only) | yes (shared drafts/threads/inboxes, delegation) | no (per homepage evidence) | yes (shared mailboxes/delegation, per help root) | varies | L2 / adjacent Type |
| AI assistance | yes (Writing Tools) | yes (+AI compose/summarize/auto-labels) | no (per homepage evidence) | yes (Copilot) | yes (varies) | L2 |
| triage-state innovations (Done/Set Aside/Snooze) | partial (mark to revisit) | yes (first-class) | no (per homepage evidence) | not asserted | varies | L2 / L3 |

## L0 — Defining Invariant

The smallest structure without which the product would no longer be recognizable as an Email Client:

```text
Mail Account (addressable mailbox on the email system)
└── Message (envelope: sender / recipients / subject / time + body, optional attachments)
    ├── Send: compose → addressed submission into the email system
    ├── Receive: inbound delivery into the account's store
    └── Persistent store: the mailbox, presented by the client for reading and management
```

Four properties. If any one is removed, the product either stops being recognizable as an email client or becomes a different Application Type:

- remove the **mail account connection** → a local notes/document tool (no email system involvement)
- remove the **message envelope** (no recipients/subject; live exchange instead) → Instant Messaging
- remove **send/receive** (no transport) → an archive viewer for imported mail files at best
- remove the **persistent managed store** (send-only utility, no mailbox) → a mailto submitter, not a client

Deliberately **not** in L0 (checked against §24 historical/market samples): installed-app surface, IMAP/SMTP or any specific protocol, folders, threading, HTML rendering, address book, search, multiple accounts, AI. Historical terminal clients, modern webmail, and platform-native clients all satisfy the four properties without those.

## L1 — Common Mature Structure

Common in mature modern email clients; not required for the Type:

```text
Standard containers (inbox / sent / drafts / trash / junk) per account
User-created organization containers (folders, or labels/tags, or saved searches)
Read/unread state + triage actions (mark, flag/star, move, archive, delete)
Conversation threading (grouping related messages)
Search over the store
Contacts / recipient autocomplete
Drafts (compose state persists)
Signatures
Attachments (add / view / save)
Multiple accounts (unified or per-account inbox)
Junk/spam surface (junk mailbox, mark as junk, block sender)
Rules / automatic sorting of incoming mail
Notifications (new-mail badges/alerts)
```

A product can be a fully recognizable email client without threading, without rules, even without a contacts pane — but a typical modern client includes most of these.

## L2 — Variant / Optional Structure

```text
Account/protocol substrate
- IMAP/POP + SMTP (provider-agnostic classic)
- Exchange / EWS / Microsoft 365 (corporate)
- proprietary provider APIs (provider-bound clients)
- OAuth consent / app-specific passwords as connection mechanics

Surface
- desktop installed app
- mobile app
- terminal client (historical/minority)
- browser surface → Webmail Application (adjacent leaf)

Organization philosophy
- folder-centric (classic)
- label/tag-centric
- search-first ("search, don't sort")
- smart-inbox / triage-first (priority senders, done/snooze semantics)
- auto-categorization of incoming mail

Suite integration
- mail-only client
- mail + calendar + contacts (+ tasks) in one app
- mail + platform system apps (OS-native integration)

Store & sync model
- server-side store (client as synchronized view)
- local store (download-and-remove or local-only mailboxes)
- vendor sync layer layered over accounts

Security posture
- transport-only (default)
- S/MIME or PGP signing/encryption (optional in some clients)
- privacy stance as product philosophy (open source, no ads, no data sale)

Team / collaboration add-ons
- shared drafts, comments on threads, delegation, shared inboxes
- (these bridge toward Shared Mailbox / Email Collaboration Types)

AI assistance
- summarize, draft, auto-label, translate
```

## L3 — Vendor-specific Structure

Belongs in Research Notes only:

- Spark: Smart Inbox, Gatekeeper, Done marker, Set Aside/Pin/Snooze semantics, "email for sync" concept, Priority senders, Group by Sender, Spark CLI, shared threads/comments, read statuses, +AI module names
- Apple Mail: "On My Mac" local store, Smart Mailboxes, Internet Accounts integration, iCloud+ custom domains and alias addresses, categories (Primary/Transactions/Updates/Promotions), Apple Intelligence Writing Tools, public read-only mailboxes (work environments)
- Thunderbird: unified inbox, tags, add-on extensibility, donation funding model, Thunderbird for Android, Thundermail (tb.pro)
- Outlook: Copilot in Outlook, shared mailboxes/folders/calendars delegation surface, the franchise's span across new Outlook / classic Outlook / Outlook for Mac / Outlook.com
- Specific provider lists (Gmail/iCloud/Yahoo/Exchange/Outlook/Kerio…), app-specific-password mechanics, and any numeric limits

## Canonical Model (v1.1)

```text
L0
Mail Account
└── Message (envelope + body + optional attachments)
    ├── Send (compose → submit)
    ├── Receive (deliver → store)
    └── Persistent managed store (the mailbox)
```

This is the entire Core Model. Everything else is L1 or lower.

## Boundary Findings

### vs Webmail Application

- The core model is **identical** (account, message, compose, store). The difference is the delivery surface: an installed/native application vs a browser application, and typical account coupling (webmail is bound to the provider's own service; a client is normally provider-agnostic).
- Boundary test: strip the browser surface from a webmail product and you have an email client; strip the installed-app surface from a client and you have webmail. The two directory leaves differ by **surface, not structure** — recorded as a boundary issue for a future joint review pass.
- Outlook makes the boundary explicitly fuzzy: one franchise spans installed clients and Outlook.com webmail.

### vs Shared Mailbox Application

- An email client is a **single person operating their own mailbox(es)**. A shared mailbox application makes **multiple people operating one mailbox** the primary structure (assignment, ownership, answered/unanswered state per human).
- Bridge evidence: Spark's shared inboxes and Outlook's shared-mailbox surface exist as add-ons inside clients; the dedicated Type is defined by multi-person operation being primary, not optional.

### vs Email Collaboration Application

- Collaboration around email (shared drafts, private comments on a thread, delegation) is an L2 add-on in clients like Spark. A dedicated Email Collaboration Type would make that layer primary. The client's primary loop remains personal read/compose/organize.

### vs Email Marketing Platform

- Marketing platforms are **sender-side bulk systems**: campaigns, recipient lists, templates, tracking. No personal mailbox store, no read/reply of one's own correspondence. Different users (marketers), different objects (campaign/list), different flow (broadcast, not correspondence).

### vs Email Security Gateway / Email Infrastructure Management

- Those are **server-side infrastructure** types: filtering, routing, authentication (SPF/DKIM/DMARC), mailbox provisioning. They have no end-user mailbox surface. The client is the user-facing end of the same pipeline.

### vs Feed Reader

- A feed reader stores **subscriptions to published content**; there is no addressing, no reply, no envelope. An email client's store is **correspondence**: addressed messages to/from identified parties. The "inbox-like list" is superficial resemblance only.

### vs Instant Messaging Application

- Email is **asynchronous store-and-forward with envelope semantics** (subject, recipients, formal headers, server-side mailbox). IM is **live conversation** bound to personal identity with no envelope and no folder store. Threading exists in both, but the email thread is a persisted correspondence record, not a live session.

### vs Task Management / To-do

- Clients offer flag/star/convert-to-task bridges, and some integrate task apps. The primary object remains the **message**; a task application's primary object is the **task** with its own lifecycle. If task objects and workflows become primary, the product has drifted to a different Type.

### Cleanest boundary test

> Removing the account connection and transport from an email client leaves a document tool.
> Removing the envelope semantics leaves a chat product.
> Removing the personal single-owner mailbox (making multi-person operation primary) leaves a Shared Mailbox Application.
> Removing the user-facing surface entirely (server-side only) leaves email infrastructure.

## Uncertainties

- Thunderbird's Knowledge Base and Microsoft's deep help articles were unreachable on the research date; Thunderbird and Outlook observations are limited to their product/help root pages. Claims about those two products are intentionally coarse (positioning and section structure only).
- Whether "Webmail Application" should remain a separate directory leaf or be treated as a surface variant of Email Client is a taxonomy question for a joint review pass; this research documents the boundary but does not rewrite the directory.
- The exact L1 status of "standard containers" (inbox/sent/drafts/trash): every sampled product has them, and Apple documents them as the standard set per account; they are placed at L1 (not L0) because a hypothetical flat-store client would still be recognizable. This placement could be revisited if a future sample contradicts it.
- Historical samples (Eudora/Pine era) were used only at the level of widely-attested structural facts; no precise claims were drawn from them.

## Final Synthesis

Canonical Email Client, v1.1:

```text
L0 (defining invariant)
- Mail account connection (addressable mailbox on the email system)
- Message as structured unit (envelope: sender/recipients/subject/time + body, optional attachments)
- Send (compose → submit) and Receive (deliver → store) against the email system
- Persistent managed store (the mailbox), presented for reading and management

L1 (common mature structure)
- Standard containers (inbox/sent/drafts/trash/junk)
- User-created containers (folders / labels / saved searches)
- Read/unread + triage actions
- Conversation threading
- Search
- Contacts / autocomplete
- Drafts, signatures, attachments
- Multiple accounts
- Junk surface + sender blocking
- Rules / automatic sorting
- Notifications

L2 (variant / optional)
- Protocol substrate (IMAP/POP/Exchange-EWS/proprietary API; OAuth/app passwords)
- Surface (desktop / mobile / terminal; browser → Webmail leaf)
- Organization philosophy (folders / labels / search-first / smart-inbox / auto-categories)
- Suite integration (mail-only vs mail+calendar+contacts+tasks)
- Store & sync model (server-side / local / vendor sync layer)
- Security posture (transport-only vs S/MIME/PGP; privacy stance)
- Team collaboration add-ons (shared drafts/threads/inboxes, delegation)
- AI assistance (summarize / draft / auto-label / translate)
```

The Application Document will present only L0 and L1, with a Variants section naming L2 options. L3 stays in these Research Notes.
