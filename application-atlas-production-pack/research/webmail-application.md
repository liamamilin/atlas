# Research Notes — Webmail Application

## Research Goal

Identify the smallest stable structure that defines the **Webmail Application** Application Type, and place every other observed feature at the correct abstraction level.

Following `WORKFLOW_v1.1.md §22` and `WRITING_GUIDE_v1.1.md §28`:

```text
L0 Defining Invariant
L1 Common Mature Structure
L2 Variant / Optional
L3 Vendor-specific
```

Evidence layers per `WORKFLOW_v1.1.md §23`:

```text
A Direct Product Observation
B Cross-product Commonality
C Canonical Inference
```

This pass also **discharges the pre-hung boundary flag** from the email-client pass (STATUS.md Boundary Issues, 2026-09-06): "email-client vs webmail-application share the entire L0 core model … may deserve a joint review pass when Webmail Application is processed."

## Initial Boundary

Target:

> Webmail Application (directory section 01.02 Email Communication)

Nearest confusing Types:

- Email Client (same section — highest confusion risk; the email-client pass already documented the shared core model)
- Disposable Email Service (same section — browser inbox, but anonymous expendable address)
- Shared Mailbox Application (same section — multi-person operation of one mailbox)
- Email Collaboration Application (same section — team collaboration around email)
- Email Marketing Platform (section 06 — bulk sender side)
- Email Security Gateway (section 15 — organizational checkpoint; that pass explicitly excluded the consumer webmail junk filter)
- Email Infrastructure Management (section 14 — server-side plumbing)
- Web Portal (section 02.11 — webmail historically embedded in portals)

Working hypothesis:

> A Webmail Application is an email application delivered entirely in the web browser: the user signs in to a mailbox hosted by a mail service and reads, composes, organizes, and searches mail without installing software.

## Research Questions

1. What is the minimal structure that makes a product a webmail application, independent of era, vendor, and organization philosophy?
2. Is the browser surface alone the differentiator, or does the service-hosted mailbox (sign-in access, no client-side connection configuration) belong in the definition?
3. What does the webmail surface assume about the account and the store (server-side only? local store possible?)
4. Which capabilities are standard in mature webmail, and which are suite add-ons?
5. How do products differ: organization philosophy, suite integration, privacy posture, audience/deployment?
6. Where are the boundaries: vs Email Client, vs Disposable Email, vs Shared Mailbox, vs Email Collaboration, vs web-based multi-account clients?
7. Historical / market-sample check: does the definition survive the Hotmail-era founding generation, operator-deployed generic webmail, regional webmail, and platform-native webmail?

## Representative Products

| Product | Why selected | Evidence level |
|---|---|---|
| Outlook.com / Outlook on the web (Microsoft) | dominant consumer webmail bound to a suite; Hotmail heritage; vendor itself distinguishes webmail from the desktop client | A (help root + Get help with Outlook.com article, fetched) |
| Zoho Mail (Zoho) | business email hosting whose primary surface is webmail; admin tier; suite apps | A (help root + Getting Started guide, fetched) |
| iCloud Mail on iCloud.com (Apple) | platform-native webmail; serves "web-only accounts" (surface can be the only surface) | A (iCloud User Guide TOC, fetched) |
| Roundcube | open-source generic webmail client deployed by mail operators; decouples the surface software from any single vendor's service | A (homepage + about page, fetched) |
| Gmail (Google) | largest consumer webmail; label/search philosophy | B only — host unreachable, widely-attested structural facts at low precision |
| Yahoo Mail (Yahoo) | long-lived consumer webmail with portal heritage | B only — host returned 403 |
| Proton Mail (Proton) | privacy/encryption-focused webmail | B only — host unreachable |

The four Layer-A products span four product philosophies and customer tiers: consumer suite-bound, business hosted, platform-native, operator-deployed generic.

## Sources

Research date: **2026-09-09**

### Source-access Limitation

- All Google properties attempted (support.google.com/mail, www.google.com/gmail/about, workspace.google.com, mail.google.com) timed out repeatedly — **abandoned**. Gmail evidence is limited to widely-attested structural facts at low precision; no precise claims drawn.
- proton.me and protonmail.com timed out — **abandoned**. Proton Mail treated the same way.
- help.yahoo.com returned 403; www.yahoo.com/mail returned 403 — **abandoned**. Yahoo Mail treated the same way.
- en.wikipedia.org timed out twice — **abandoned**; no Tier-3 fallback used.
- No precise numeric limits, storage quotas, or default settings are stated anywhere in the final document.

### Successfully fetched official sources

- Roundcube — homepage: https://roundcube.net/ ; about/features: https://roundcube.net/about/
- Zoho Mail — help root: https://www.zoho.com/mail/help/ ; Getting Started: https://www.zoho.com/mail/help/getting-started.html
- Microsoft — Outlook help & learning root: https://support.microsoft.com/en-us/outlook ; Get help with Outlook.com: https://support.microsoft.com/en-us/outlook/get-help-with-outlook-com
- Apple — iCloud User Guide (welcome/TOC, incl. Mail on iCloud.com section tree): https://support.apple.com/guide/icloud/welcome/icloud

## Product Observations

### Outlook.com / Outlook on the web (Microsoft) — Layer A

From "Get help with Outlook.com" (official support article) and the Outlook help root:

- **Service heritage, vendor-stated**: "Outlook.com is the current name for Microsoft's email service, which was formerly known as Hotmail (and later, as Windows Live Hotmail)." Hotmail (1996) is the founding generation of webmail.
- **Front end / back end architecture, vendor-stated**: "Outlook Mail is the web app that lets you browse your Outlook.com email account. It's part of the Outlook on the web suite of web apps. Outlook Mail is the front end while Outlook.com is the back end."
- **Vendor's own client/webmail distinction**: "Outlook (or Office Outlook) is the Microsoft desktop email client. It can be used with Outlook.com email addresses or with any other email addresses." — the desktop client is provider-agnostic machinery; the web app is the service's own front end.
- **Sign-in access**: "Sign in to Outlook.com (or Hotmail.com) with your Microsoft account." "When you sign in to Outlook.com, you'll go straight to your Inbox." No account/connection configuration step.
- **Mail surfaces**: New mail (compose); Folders list (Favorites, Drafts, Sent Items, Archive; create new subfolder); Search box; Message list (unread/attachment/flagged indicators; Filter: All / Unread / Flagged / To me / Has files / Mentions me / Has calendar invites; Sort by Date / Category / From / Size / Importance / Subject; per-message delete, mark unread, flag, pin); Reading pane (delete, archive, sweep, move, categorize, print).
- **Settings**: Focused Inbox on/off; reading pane layout (Right / Bottom / Fill screen / Popout); Conversation view on/off ("Do not group messages").
- **Suite in the same web surface**: Calendar (new event, invite attendees, Teams meetings), People (contacts, contact lists, Groups — joining a group gives a group mailbox, calendar, OneNote notebook, team site), Tasks (To Do), Files & attachments, Premium tier.
- **Service-side account machinery**: change password from the profile menu; "Unblock my Outlook.com account"; "Recover and restore deleted items"; "Fix Outlook.com email sync issues, including sign-in problems".
- **Mobile browser variant**: separate help path "Get help with Outlook.com or Outlook on the web in a mobile browser" — the same web app adapts to mobile browsers.
- **AI**: Copilot in Outlook (help root section).
- Help root also covers the installed franchise (new Outlook for Windows, Outlook for Mac, classic Outlook) — one brand spanning installed clients and webmail.

### Zoho Mail (Zoho) — Layer A

From the help root and Getting Started guide:

- **Positioning**: "Zoho Mail is a collaborative business communication platform… a blend of classic email and modern collaborative tools such as comments, likes, and sharing."
- **Sign-in access**: compose instructions begin "Login to Zoho Mail" at a login URL (mail.zoho.com); "Click on the New Mail button in the left pane of your Mailbox."
- **Compose loop**: New Mail → Composer (To, CC, Subject, content, rich formatting) → Send → "You can find this email in your Sent folder." Optional Outbox delay (mail held in Outbox for a set duration before sending).
- **Viewing**: inbox listing with unread in bold; Classic/Compact views; open in preview / new tab / new window; Conversation View ("groups emails into conversation threads… turn… OFF").
- **Respond**: Reply / Reply All / Forward.
- **Organization**: custom folders (create, Move to); Filters (name, conditions, criteria, actions — move, apply tags, forward, mark as read); Tags (colored); Flag + Flagged view.
- **Search**: across apps (Notes, Tasks, Emails); criteria From / To-CC / In folder / Tag / Contains / Subject / Attachment Name; search history.
- **Suite**: Mail, Calendar, Contacts, Tasks, Notes, Streams ("collaboration within teams, built around email… like/comment"), Bookmarks, Resources (meeting-room booking), eArchive (restore permanently deleted emails).
- **Extensions**: in-house integrations, custom extensions, Zoho Marketplace.
- **Companion apps**: mobile apps (Android/iOS) and "Zoho Mail Desktop Lite" (Mac/Windows/Linux) — companion surfaces of the same service.
- **Admin tier**: "extensive control panel for the administrators to manage their organization users, email accounts and policies"; deployment guides; migration via IMAP or Exchange wizard — Zoho Mail is email hosting with webmail as the user surface.
- **Signatures**: multiple signatures, linkable to email aliases.

### iCloud Mail on iCloud.com (Apple) — Layer A

From the iCloud User Guide (welcome + TOC):

- **Web access by sign-in**: "Use iCloud on the web — See your mail, photos, files, and more on iCloud.com… Sign in and use iCloud.com."
- **Web-only accounts**: a dedicated guide section "Overview of iCloud.com for web-only accounts" — the web surface serves users who have no Apple-device setup at all; the browser surface can be the user's ONLY mail surface.
- **Mail on iCloud.com structure** (TOC):
  - addresses: add/manage email aliases, custom email domain, choose default address, Hide My Email in Mail
  - send: write and send, save/view drafts, reply/forward, reminder to reply, add attachment, signature, save/find addresses, automatic reply (vacation)
  - receive: read email, view all email headers, download attachments, automatically forward email, **Manage junk mail**, delete email
  - organize/find: use categories, automatically clean up, organize email with folders, search/filter/flag email, set up filtering rules, archive email, make a sender a VIP
  - privacy: Mail Privacy Protection; print; keyboard shortcuts
- **Suite on the same web surface**: Calendar, Contacts, Drive, Notes, Photos, Reminders, Find Devices — Mail is one app tile of the iCloud web suite.
- **Account machinery**: Apple Account and iCloud; manage access to iCloud.com; storage management; iCloud+ paid tier (Private Relay, Hide My Email, Custom Email Domain).

### Roundcube — Layer A

From the homepage and about page:

- **Self-label**: "Roundcube webmail… is a browser-based multilingual IMAP client with an application-like user interface. It provides full functionality you expect from an email client, including MIME support, address book, folder manipulation, message searching and spell checking."
- **Deployment model**: "a free and open source webmail solution with a desktop-like user interface which is easy to install/configure and that runs on a standard LAMPP server." Server requirements: web server + PHP + database + "SMTP server and IMAP server with IMAP4 rev1 support" — Roundcube fronts external IMAP/SMTP servers; it is deployed by mail operators.
- **Provider role, vendor-stated**: "There are thousands of services that make use of Roundcube to provide webmail to millions of users." — services deploy it to provide webmail for their users' mailboxes.
- **Features**: drag-&-drop message management, MIME/HTML, multiple sender identities, address book (groups, LDAP connectors), threaded message listing, IMAP folder management, shared/global IMAP folders, external SMTP, ACL, caching, import/export, skins (responsive, light/dark), plugin API, PGP encryption support, OAuth/XOauth login, brute-force login prevention, 80+ languages, three-column view, attachment previews, search.
- **Suite integration is NOT core**: the calendar is a third-party plugin; two-factor auth is a third-party plugin — the mail-only pole of the Type.
- **Governance**: hosted by Nextcloud since 2023; used by services such as KolabNow (Swiss privacy-focused groupware hosting).

### Gmail, Yahoo Mail, Proton Mail — Layer B only (hosts unreachable)

Widely-attested structural facts only, at low precision, no precise claims:

- Gmail: free consumer webmail from Google; label-based organization and search-first philosophy; conversation view; part of the Google account ecosystem and Google Workspace business tier; companion mobile apps. Widely attested; not directly verified on the research date.
- Yahoo Mail: long-lived consumer webmail (RocketMail lineage, 1997), historically embedded in the Yahoo portal; folder-based; companion apps. Widely attested; not directly verified.
- Proton Mail: privacy-focused webmail from Proton; encrypted-mailbox posture; web, mobile, and desktop-bridge surfaces. Widely attested; not directly verified.

These three anchor the market-presence breadth of the sample (consumer free, portal heritage, privacy posture) but contribute no precise structural claims.

### Historical / market-sample breadth (Layer B, low precision)

- **Hotmail (1996)**: officially confirmed by Microsoft as Outlook.com's former name. The founding webmail generation — a free hosted mailbox accessed through a browser from any machine — satisfies the structure below without labels, AI, suite apps, or mobile apps.
- **Operator-deployed generic webmail (Roundcube generation)**: hosting companies, universities, and organizations deploy webmail clients in front of their IMAP servers; the same structure holds with the operator in the service role.
- **Regional webmail (QQ Mail, Yandex Mail, GMX, Naver Mail, mail.ru)**: provider-coupled browser mailboxes in their respective markets; same structure (widely attested, no precise claims).
- **Platform-native webmail (iCloud Mail)**: directly evidenced above; the web surface complements installed clients and can be the only surface (web-only accounts).

The Type survives all of these without any modern-era machinery in the definition.

## Cross-product Comparison

| Finding | Outlook.com | Zoho Mail | iCloud Mail (web) | Roundcube | Gmail/Yahoo/Proton (B) | Level |
|---|---|---|---|---|---|---|
| full mail surface delivered in the browser, nothing to install | yes (web app) | yes (login URL) | yes (iCloud.com) | yes ("browser-based… client") | yes | L0 |
| mailbox is an account on the service behind the surface; sign-in access, no client-side connection setup | yes ("sign in… straight to your Inbox") | yes ("Login to Zoho Mail") | yes ("Sign in and use iCloud.com") | yes (login to deployed service; OAuth support) | yes | L0 |
| email spine: account + envelope message + send/receive + persistent store | yes | yes | yes | yes | yes | L0 (inherited) |
| store is server-side only (no local-store variant in the surface) | yes (implied by service architecture) | yes | yes | yes (IMAP backend) | yes | L0-consequence |
| standard containers (inbox/sent/drafts/trash/junk/archive) | yes (Folders list) | yes (Sent folder etc.) | yes (folder model) | yes (IMAP folders) | yes | L1 |
| user-created folders (or labels at the label pole) | yes (subfolders) | yes (custom folders) | yes (folders) | yes (IMAP folder management) | Gmail: labels | L1 |
| read/unread + triage (flag, pin, mark unread, archive, sweep) | yes (rich set) | yes (flag/tag/move) | yes (flag/archive) | yes (drag-&-drop) | yes | L1 |
| conversation view (commonly toggleable) | yes (toggle) | yes (toggle) | not asserted | yes (threaded listing) | Gmail: yes | L1 |
| search over the store | yes | yes (multi-criteria + history) | yes (search/filter/flag) | yes | yes | L1 |
| filters/rules for automatic sorting | sweep/categorize observed; rules not asserted | yes (filters) | yes (filtering rules) | not asserted | yes | L1 |
| junk mail management | not asserted in fetched text | not asserted in fetched text | yes ("Manage junk mail") | not asserted | yes | L1 (B-supported) |
| contacts/address book | yes (People app) | yes (Contacts app) | yes (Contacts on iCloud.com) | yes (address book, LDAP) | yes | L1 |
| signatures | not asserted | yes (multiple, alias-linked) | yes | canned responses; not asserted | yes | L1 |
| attachments (add/view/download/preview) | yes (previews, attach message) | yes (search by attachment name) | yes (add/download) | yes (previews) | yes | L1 |
| aliases / multiple sender identities | not asserted | yes (alias-linked signatures) | yes (aliases, default address) | yes (multiple identities) | yes | L1 |
| vacation/auto-reply, auto-forward | not asserted | not asserted | yes (both) | not asserted | yes | L1 (single-product direct; treated common with care) |
| suite integration (calendar/contacts/tasks in the same web surface) | yes (Calendar/People/Tasks) | yes (full suite) | yes (web suite) | **no — calendar is a 3rd-party plugin** | yes | L1/L2 |
| companion mobile/desktop apps of the same service | yes (Outlook franchise) | yes (mobile + Desktop Lite) | yes (device Mail apps + web) | no (surface only) | yes | L1/L2 |
| service-side account machinery (password, recovery/unblock, storage) | yes (unblock, change password, restore) | yes (admin console) | yes (manage access, storage) | partial (brute-force prevention) | yes | L1 |
| appearance/layout settings | yes (reading pane, Focused Inbox) | yes (Classic/Compact, open-in) | yes (customize appearance) | yes (skins, light/dark) | yes | L1 |
| priority-sender / auto-categorization | yes (Focused Inbox) | not asserted | yes (VIP, categories) | no | Gmail: yes | L2 |
| chat/IM inside the mail surface | yes ("Start chat" from contact card) | not asserted | not asserted | no | Gmail: yes | L2 |
| AI assistance | yes (Copilot) | not asserted | not asserted | no | Gmail: yes | L2 |
| organization philosophy | folders | folders + tags | folders + categories | folders | Gmail: labels + search-first | L2 |
| audience/deployment | consumer free + M365 business | business hosting (admin console) | consumer platform-native | operator-deployed generic | consumer free / privacy / portal | L2 |
| privacy/encryption posture | standard | standard (security whitepaper) | privacy features (Mail Privacy Protection) | optional PGP | Proton: E2EE posture | L2 |
| business model | free + Premium tier | paid tiers | free + iCloud+ | free open source (deployed by services) | free/subscription | L2 |

## L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product is no longer recognizable as a Webmail Application:

```text
1. Email correspondence spine
   Mail account on the email system
   └── Message (envelope: sender / recipients / subject / time + body, optional attachments)
       ├── Send (compose → submit into the email system)
       ├── Receive (inbound delivery into the account's store)
       └── Persistent mailbox store

2. Browser-delivered application surface
   The full mail application — read, compose, organize, search, configure —
   runs as a web application in the browser at the service's address;
   nothing is installed on the user's device.

3. Service-hosted mailbox behind a sign-in
   The mailbox the surface operates is an account hosted by the mail service
   that operates (or deploys) the surface; the user authenticates to the
   service and lands in the mailbox. There is no client-side
   account/connection configuration step.
```

Jointly-held load-bearing:

- **1 + 2 without 3** → a web-based email client connecting to user-configured third-party servers — a marginal form the market does not label webmail (historically attested as gateway services; not the webmail population).
- **1 + 3 without 2** → an email hosting/back-end service with no user web surface — Email Infrastructure territory, not webmail.
- **2 + 3 without 1** → a sign-in page to nothing — not email.
- **3 without 1 + 2** → an account registry.

Deliberately **not** in L0 (checked against the historical/market samples): folders vs labels, conversation view, search, contacts, suite integration, companion apps, junk machinery details, AI, ads, storage quotas, any protocol (IMAP/POP/Exchange/proprietary API — Roundcube fronts IMAP; provider webmail uses proprietary service APIs; both are webmail). Hotmail-era webmail, operator-deployed Roundcube, regional webmail, and platform-native iCloud Mail all satisfy the three properties without any of those.

## L1 — Common Mature Structure

Common in mature modern webmail; not required for the Type:

```text
Standard containers (inbox / sent / drafts / trash / junk / archive)
User-created organization containers (folders; labels at the label-philosophy pole)
Read/unread state + triage actions (flag/star, pin, mark unread, move, archive, sweep)
Conversation view (commonly the default, commonly toggleable)
Search over the store (often multi-criteria)
Filters / rules for automatic sorting of incoming mail
Junk mail management with user feedback
Contacts / address book (often a full People/Contacts app in the same web surface)
Signatures; aliases / multiple sender identities
Attachments (add on send; view / preview / download on receive)
Vacation / automatic reply; automatic forwarding
Suite integration (calendar, contacts, tasks commonly adjacent in the same web surface)
Companion mobile / desktop apps operated by the same service
Service-side account machinery (password change, recovery/unblock, storage management)
Appearance / layout settings (reading pane placement, density, themes)
```

A product can be fully recognizable webmail without suite apps (Roundcube's calendar is a third-party plugin), without VIP/priority machinery, and without AI — but a typical modern webmail includes most of the above.

## L2 — Variant / Optional Structure

```text
Organization philosophy
- folder-centric (Outlook.com, Zoho, iCloud, Roundcube)
- label + search-first (Gmail — widely attested)

Suite depth
- mail-only webmail (Roundcube pole)
- webmail as one app of a web suite / workspace (Outlook on the web suite, Zoho suite, iCloud web suite)

Audience / deployment
- free consumer webmail (Outlook.com, Gmail, Yahoo Mail)
- business email hosting with admin console (Zoho Mail; Workspace/M365 tiers)
- platform-native webmail (iCloud Mail; serves web-only accounts)
- operator-deployed generic webmail (Roundcube in front of IMAP servers)

Privacy / encryption posture
- standard service posture
- privacy-focused / encrypted-mailbox posture (Proton Mail — widely attested; PGP support optional in Roundcube)

Business model
- ads-funded free / freemium / subscription premium tiers

Priority-sender & auto-categorization machinery (Focused Inbox, categories, VIP senders)
Chat/IM integration inside the mail surface
AI assistance (summarize / draft / catch up)
Offline access (limited and optional in a browser surface)
Portal embedding (webmail as one tile of a larger portal — Yahoo heritage)
```

## L3 — Vendor-specific Structure

Belongs in Research Notes only:

- **Outlook.com**: Focused Inbox, Sweep, pin-to-top, attach-an-email-to-another-email, To Do integration, Groups (group mailbox + calendar + OneNote + team site), Premium tier, Hotmail → Windows Live Hotmail → Outlook.com rebrand lineage, "Outlook Mail front end / Outlook.com back end" architecture sentence, mobile-browser help variant.
- **Zoho Mail**: Streams (likes/comments collaboration built around email), eArchive (restore permanently deleted emails), Resources (meeting-room booking), Outbox delay, Zoho Marketplace extensions, Desktop Lite app, deployment/migration guides (IMAP/Exchange wizard).
- **iCloud Mail**: Hide My Email, Custom Email Domain, Mail Privacy Protection, VIP senders, categories, "web-only accounts" framing, reminder-to-reply, automatically clean up.
- **Roundcube**: plugin API, skins/template system, PGP support, LDAP address book connectors, ACL/shared IMAP folders, brute-force prevention, Nextcloud governance (since 2023), KolabNow as a contributing service.
- **Gmail**: labels, confidential mode, Gemini assistance — widely attested only; no precise claims drawn (host unreachable).

## Boundary Findings

### vs Email Client (the pre-hung flag — discharged from this side)

- The **core model is shared**: mail account, envelope message, send/receive, persistent store (established by the email-client pass and confirmed here).
- The difference is **surface + coupling**: webmail delivers the full surface in a browser with nothing to install, and the mailbox is an account on the service behind the surface (sign-in, no client-side connection configuration); an email client is installed software the user points at account(s) via connection setup, normally provider-agnostic.
- **Vendor-articulated distinction (Layer A)**: Microsoft's own help text separates "Outlook Mail — the web app… front end" of the Outlook.com service from "Outlook (or Office Outlook) — the Microsoft desktop email client… can be used with Outlook.com email addresses or with any other email addresses."
- **Structural consequences of the surface** (why this is more than a UI skin): no installation/device requirement (iCloud serves web-only accounts); the store is server-side only (no local-store variant); account lifecycle is service-side (unblock/recover/admin console); features ship server-side for all users at once (no version fragmentation); the account typically doubles as identity for a wider service ecosystem.
- **Boundary test**: strip the browser surface from a webmail product and you have an email client (or a bare hosting service); give an installed client a service-hosted sign-in mailbox and remove connection setup — it is drifting toward webmail. The Outlook franchise deliberately spans both (fuzzy commercial edge, structurally two surfaces).
- **Resolution**: keep-both, as **surface-defined sibling Types sharing the email spine** — the same resolution pattern the corpus ratified for mobile-pos vs retail-point-of-sale (surface carries real structural consequences: users, hardware/rules analogues, deployment). The webmail leaf is documented on its own terms; the email-client leaf already cross-references it. Recommend no consolidation; record for any future taxonomy pass.

### vs Disposable Email Service

- Both show an inbox in a browser. Webmail's mailbox is the user's **durable address backed by their identity** on the service (aliases, recovery, account machinery). A disposable address is an **anonymous, expendable token** with no identity continuity. (Consistent with the disposable-email pass's own boundary statement.)

### vs Shared Mailbox Application

- Webmail's object is the **personal mailbox** of a signed-in user. A shared mailbox application makes **multiple people operating one mailbox** the primary structure. Shared-mailbox access may appear through webmail surfaces (Outlook.com/OWA exposes shared mailboxes), but that is an add-on surface, not the Type's center. (Consistent with the shared-mailbox pass.)

### vs Email Collaboration Application

- Collaboration modules exist **inside** webmail as add-ons (Zoho Streams — likes/comments around email; Outlook.com Groups). The dedicated Email Collaboration Type makes team collaboration on email the primary structure; webmail's primary loop remains personal correspondence.

### vs Email Marketing Platform

- Sender-side bulk systems (campaigns, lists, templates, tracking) have no personal mailbox store and no correspondence reading. Different users, objects, and flow.

### vs Email Security Gateway

- The gateway pass explicitly excluded the consumer webmail junk filter: a webmail product has **no organizational checkpoint** under admin control; its junk machinery is a per-user judgment surface. Server-side filtering may act before the webmail surface sees the message.

### vs Email Infrastructure Management

- Webmail is the **user-facing front end**; infrastructure management is the server-side plumbing (routing, authentication, provisioning) with no end-user mailbox surface. Microsoft's own front-end/back-end sentence marks this seam.

### vs Web Portal

- Historically webmail was embedded in portals (Yahoo heritage). The portal is a container; the webmail surface remains the mail application. Portal embedding is a variant, not the Type.

### Cleanest boundary test

> Removing the browser surface leaves an installed email client (or bare mail hosting).
> Removing the service-hosted sign-in mailbox leaves a web-based client for arbitrary servers — a marginal form outside the market's webmail population.
> Removing the email spine leaves a login page to nothing.
> Making the address anonymous and expendable leaves a Disposable Email Service.
> Making multi-person operation primary leaves a Shared Mailbox Application.

## Uncertainties

- Gmail, Yahoo Mail, and Proton Mail could not be fetched (host timeouts / 403). Their inclusion rests on market presence and widely-attested structural facts at low precision. No precise claims are drawn from them anywhere.
- The marginal counterfactual — a browser-based client connecting to user-configured arbitrary servers — is historically attested (gateway-style services) but is not the market's webmail population; its classification is a residual edge, recorded rather than resolved.
- The exact division of junk-filtering labor (service-side pre-filtering vs surface-side user feedback) is only directly evidenced at iCloud ("Manage junk mail"); treated as common structure with moderate confidence.
- Whether vacation/auto-reply and auto-forward are universal is not asserted; directly evidenced at iCloud only, treated as common-with-care.
- The taxonomy question — whether email-client and webmail-application should eventually consolidate — is recorded as discharged keep-both from this side; final taxonomy authority rests with a future joint review.

## Final Synthesis

Canonical Webmail Application, v1.1:

```text
L0 (defining invariant) — three jointly-held structures:
- Email correspondence spine (account + envelope message + send/receive + persistent store)
- Browser-delivered application surface (full mail app in the browser, nothing to install)
- Service-hosted mailbox behind a sign-in (surface is the front end of the mail service
  that hosts the mailbox; no client-side connection configuration)

L1 (common mature structure):
- standard containers; user folders (or labels); triage actions; conversation view
- search; filters/rules; junk management; contacts; signatures; aliases
- attachments; auto-reply/auto-forward; suite integration; companion apps
- service-side account machinery; appearance/layout settings

L2 (variant / optional):
- organization philosophy (folders vs labels+search-first)
- suite depth (mail-only vs workspace suite)
- audience/deployment (consumer free / business hosting / platform-native / operator-deployed generic)
- privacy/encryption posture; business model
- priority-sender machinery; chat integration; AI; offline; portal embedding

L3 (vendor-specific): Focused Inbox/Sweep/Groups (Outlook.com), Streams/eArchive/Resources (Zoho),
Hide My Email/VIP/web-only accounts (iCloud), plugin API/PGP/LDAP (Roundcube), Gmail label machinery.
```

The Application Document will present the defining core and the common mature structure in natural language, with a Variants section naming the variant axes. L3 stays in these Research Notes.
