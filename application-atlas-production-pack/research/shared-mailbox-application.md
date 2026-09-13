# Research Notes — Shared Mailbox Application

Research date: 2026-09-08

## Research Goal

Understand what a "Shared Mailbox Application" actually is as an Application Type: what the core object (the shared mailbox) is, how it is created and administered, how multiple people operate it, how its delivery model differs from distribution lists and aliases, where the "application" actually lives (admin surface vs member access surface vs client surface), and where the Type's boundaries lie against Email Client, Webmail, Email Collaboration Application (sibling leaf, joint-review obligation), group/collaboration objects, and Help Desk.

This pass also must DISCHARGE the joint review pre-hung by the email-collaboration-application pass (2026-09-07): that pass assigned the "degenerate historical substrate" (Exchange shared mailbox + Outlook delegation, Google Groups collaborative inbox) to this leaf and proposed the discriminator "mailbox-entity-as-object (this leaf) vs collaboration-layer-as-primary (sibling leaf)".

## Initial Boundary (hypothesis before research)

- The leaf sits in the 01.02 Email family between Email Client (one person, own mailbox) and Email Collaboration Application (team collaboration layer over correspondence).
- Hypothesis: the defining structure is a dedicated mailbox entity — its own address and its own store — operated by several identified people under deliberate access control, with mail held once in the common store rather than copied out to members.
- Degenerate neighbors to test: distribution list / alias (copies to personal mailboxes — expected NOT this Type); shared credentials (the anti-pattern the object exists to replace); delegated personal mailbox (a person's mailbox shared — fuzzy edge).
- Confusion risks: Email Client (surface where shared mailboxes are accessed), Email Collaboration Application ("shared inbox" vocabulary collision), Help Desk (queues built on shared mailboxes), Microsoft 365 Groups / group-workspace objects (suite siblings that bundle a group mailbox).

## Research Questions

1. What exactly is a shared mailbox as an object: what does it carry (address, store, folders, calendar, settings), who creates it, and how is it distinct from a user mailbox?
2. How do members get access (membership, permission types, revocation), and how do they operate it (open where, send how, act on what)?
3. What does "send as" vs "send on behalf" mean externally, and how does the identity work?
4. How does the delivery model differ from distribution lists / aliases (copies vs one store)? Which vendors state this explicitly?
5. What is the modern credential model (own sign-in vs members' own identities)?
6. What administration machinery exists (create, aliases, auto-reply, rules, moderation, block, export, delete, conversion, compliance)?
7. Where does the member access surface live (desktop client, web, mobile, group view)?
8. Boundary: when does a shared mailbox + collaboration machinery become the sibling Type? When does it become a Help Desk? What does the vendor-side product taxonomy say (do vendors ship "shared mailbox" and "shared inbox" as different products)?

## Representative Products

Selected for market representation, different product philosophies, and different customer tiers — deliberately staying on the mailbox-entity side of the seam:

| Product | Philosophy / pole | Segment | Docs accessed |
|---|---|---|---|
| Microsoft 365 / Exchange (Exchange Online + on-premises Exchange Server) | the canonical admin-created shared-mailbox entity; the pattern that named the Type | enterprise | Full Tier-1 (Microsoft Learn admin docs + on-prem EAC docs + groups comparison page) |
| Zoho Mail (Shared Mailbox) | group-shaped shared mailbox inside an independent mail suite; vendor documents DL-vs-shared-mailbox delivery distinction explicitly, and ships a separate "shared inbox" collaboration product (TeamInbox) — live seam evidence | SMB → mid-market | Full Tier-1 (admin guide: groups + shared mailbox pages) |
| Fastmail (multi-user accounts) | folder-sharing realization: shared mail folders/contacts/calendars inside a multi-user account rather than dedicated shared-mailbox entities | prosumer / small business | Tier-1 (help center: multi-user accounts) |
| Google Workspace (collaborative inbox / delegated mailboxes) | group-address realization | enterprise / education | UNREACHABLE — support.google.com timed out ×4; held at low assertion, cross-referenced from the sibling pass's recorded findings only |

## Sources

- Microsoft Learn — About shared mailboxes: https://learn.microsoft.com/en-us/microsoft-365/admin/email/about-shared-mailboxes (fetched 2026-09-08, evidence layer A)
- Microsoft Learn — Create a shared mailbox: https://learn.microsoft.com/en-us/microsoft-365/admin/email/create-a-shared-mailbox (fetched 2026-09-08, A)
- Microsoft Learn — Compare types of groups in Microsoft 365: https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/compare-groups (fetched 2026-09-08, A)
- Microsoft Learn (on-premises Exchange Server) — Create shared mailboxes in the Exchange admin center: https://learn.microsoft.com/en-us/exchange/collaboration/shared-mailboxes/create-shared-mailboxes?view=exchserver-2019 (fetched 2026-09-08, A)
- Zoho Mail admin guide — Creating email groups: https://www.zoho.com/mail/help/adminconsole/creating-groups.html (fetched 2026-09-08, A)
- Zoho Mail admin guide — Shared Mailbox admin settings: https://www.zoho.com/mail/help/adminconsole/collaborative-inbox-settings.html (fetched 2026-09-08, A)
- Fastmail help center — Managing multi-user accounts: https://www.fastmail.help/hc/en-us/articles/360060590673-Managing-multi-user-accounts (fetched 2026-09-08, A)
- Cross-referenced in-atlas research (not fetched this pass): research/email-collaboration-application.md (2026-09-07) — records Google Groups collaborative inbox as the substrate and the joint-review seam; applications/email-client.md — places shared-mailbox surfaces in the suite-client variant tier.
- FAILED sources (recorded per source-access limitation): support.google.com/a/answer/167430, support.google.com/groups/answer/1439438, support.google.com/groups/answer/24640 (all timeout ×2 attempts each); zoho.com/mail/help/shared-mailbox.html and /adminconsole/shared-mailboxes.html (404); fastmail.com/help/business/sharing.html (404); support.microsoft.com "Open and use a shared mailbox in Outlook" (404 — content not independently verified).

## Product A — Microsoft 365 / Exchange (shared mailboxes)

Key observations (A = directly observed in official docs):

- **Definition/positioning**: "Create shared mailboxes so a group of people can monitor and send email from a common email address, like info@contoso.com. When a person in the group replies to a message sent to the shared mailbox, the email appears to be from the shared mailbox, not from the individual user." Use cases named: company information addresses, support addresses, reception/front-desk mailboxes.
- **The entity**: a mailbox object with its own display name and email address, created in the admin center (Teams & Groups → Shared mailboxes) or the on-prem Exchange admin center (Recipients → Shared) or PowerShell (`New-Mailbox -Shared`). Creating it automatically creates a shared calendar. A user mailbox can be converted into a shared mailbox.
- **No own login**: "A shared mailbox isn't intended for direct sign-in by using its associated user account. Always block sign-in for the shared mailbox account and keep it blocked." Every shared mailbox has a corresponding user account with a system-generated password that "isn't known or intended for use."
- **Membership & permissions**: "To use the shared mailbox, assign permissions to users through a membership. Only people inside your organization can use a shared mailbox." External users (e.g. Gmail accounts) cannot be granted access — vendors direct that need to a group object instead. Permission triad: **Full Access** (open the mailbox and act as its owner: read, view, delete, change messages, create items/calendar entries; does NOT include sending), **Send As** (mail appears as sent by the shared mailbox itself), **Send on Behalf** (mail appears as "John on behalf of Reception Building 32" — externally visible distinction). On-prem doc: "Both [Full Access and Send As] permissions are required for successful shared mailbox operation."
- **Member access surface**: with automapping (on by default), the shared mailbox appears automatically in members' Outlook desktop app; can also be added to Outlook on the web and Outlook mobile. "Delegate access must be done through the delegate's own mailbox." Automapping is set per-user and does not work when access is managed via security groups (explicit permissions required).
- **Directory visibility**: Send As / Send on Behalf do not work when the mailbox is hidden from address lists (it must be visible in the GAL to send from).
- **Behavioral edges**: there is a documented guidance limit on simultaneous users (before degradation); mail deletion by members cannot be prevented in this object (a Microsoft 365 Group is recommended where deletion restriction is needed); mail sent from a shared mailbox cannot be encrypted from it because the mailbox has no own security context; compliance features (archive, hold, retention) exist but require licenses; storage and rules configuration apply at the mailbox level ("Add rules to a shared mailbox").
- **Taxonomy (vendor's own comparison page)**: shared mailboxes listed alongside distribution groups ("sending email notifications to a group of people"), Microsoft 365 Groups (collaboration workspaces with group email + shared services), mail-enabled security groups, dynamic distribution groups. Shared mailboxes: mail-enabled, no dynamic membership. "It's not possible to migrate a shared mailbox to Microsoft 365 Groups." Deletion semantics differ between the group model and member inboxes — evidence that Microsoft treats the shared mailbox as a distinct object class with its own model.

## Product B — Zoho Mail (Shared Mailbox)

Key observations (A):

- **Explicit DL-vs-shared-mailbox distinction in delivery model**: Groups are "common email addresses, shared by a set of users for a specific purpose," classified into exactly two types: **Distribution List (DL)** — "When an email is sent to the group account, a copy of the email gets delivered to the mailbox of all the members"; external members allowed — and **Shared Mailbox** — "The emails sent to a shared mailbox do not appear in the individual user's mailbox thereby reducing email duplication." No external members; no Streams. This is the clearest obtainable statement of the one-common-store property.
- **Creation/administration**: created in the Admin Console (Groups → Shared Mailbox → Create) with a group name, email address, description, picture; member roles (member/moderator, at least one moderator); "who can send emails to the group" access types (everyone / organization members / group members / only moderators); moderation of inbound mail; block/unblock of the mailbox's incoming and outgoing permissions; export; deletion with re-authentication safeguard (MFA re-auth, time-windowed).
- **Member surface**: "Members of the group can see the shared mailbox in their mail account" (shared mailbox appears inside the member's mail client).
- **Sending**: group advanced settings include "permissions to send emails on behalf of the group email address."
- **Group-shaped container**: the shared mailbox is a subtype of the group object, not a separate mailbox-account class — a structurally different realization from Microsoft's mailbox entity, satisfying the same jobs.
- **SEAM EVIDENCE (live, same vendor)**: the shared-mailbox help pages carry a cross-marketing callout: "Looking for a Shared Inbox solution for your team? Try TeamInbox by Zoho Mail, to make collaboration with your team efficient with shared inboxes." — the vendor itself ships the shared mailbox (mail-system object) and the shared inbox (collaboration product) as two different products with different names and centers. Direct market corroboration of the sibling-leaf boundary.

## Product C — Fastmail (multi-user accounts)

Key observations (A, moderate depth):

- Realization pole: shared operation via **shared mail folders** inside a multi-user account rather than dedicated shared-mailbox entities: "Multi-user accounts can allow users to access information that has been shared in the account, such as shared mail folders, shared contacts, or shared calendars."
- Account administrators manage users, billing, domains, aliases, quotas, retention archive; "one payment to manage for all users."
- Interpretation: the Type's jobs (several people working common mail) can be realized as folder-level sharing within an account; the mailbox-entity shape (own address + own store, admin-granted membership) is the dominant but not the only container. Evidence calibrated as a contrasting implementation pole, weaker on operational mechanics.

## Product D — Google Workspace (collaborative inbox / delegated mailboxes)

UNREACHABLE this pass: all four support.google.com fetch attempts timed out. Per source-access limitation, NO operational claims are made from memory. What is held (cross-referenced from the sibling pass's research, recorded 2026-09-07): Google Groups collaborative inbox and Gmail delegation are the Google-suite realizations of shared mailbox operation; that pass classified them as the degenerate substrate of THIS leaf (shared operation without a native collaboration layer). Google is retained in the representative list for market coverage with this explicit limitation noted.

## Cross-product Comparison

| Structure / capability | Microsoft 365 / Exchange | Zoho Mail | Fastmail | Evidence |
|---|---|---|---|---|
| Dedicated shared object with its own address, created/administered by an admin | ✓ (mailbox entity; admin center / EAC / PowerShell) | ✓ (group-shaped shared mailbox; admin console) | partial (shared folders inside a multi-user account; account-level admin) | A×2 + partial |
| Multiple identified members with grantable/revocable access | ✓ (membership; Full Access; per-user automapping) | ✓ (members + moderators) | ✓ (users in account; admin-managed) | A×3 |
| One common store — mail not copied to members' personal mailboxes | ✓ (mailbox's own store; member sees the mailbox's folders; contrast with DL/group models documented) | ✓ EXPLICIT ("do not appear in the individual user's mailbox thereby reducing email duplication") | ✓ (shared folders are one store) | A×3 (Zoho explicit) |
| Send under the shared identity; "as" vs "on behalf" permission modes | ✓ explicit triad with externally visible distinction | ✓ on-behalf permission in group settings | not directly evidenced | A×2 |
| Members operate via their own identities; no separate credential for the object | ✓ (sign-in blocked; system-generated password not intended for use) | ✓ (members access via own accounts) | ✓ (account users) | A×3 |
| Shared calendar attached to the shared context | ✓ (auto-created with the mailbox) | partial (suite calendar exists; group-calendar linkage implied, not verified) | ✓ (shared calendars in account) | A×2 + partial |
| Aliases / multiple addresses on the shared object | ✓ (address editable; alias machinery suite-level) | ✓ (alias addresses on groups) | ✓ (user alias management) | A×3 |
| Mailbox-level configuration (auto-reply, forwarding, rules, moderation) | ✓ (rules on shared mailbox; forwarding/auto-reply at mailbox level) | ✓ (moderation, access types, block/unblock) | partial (filters are user/account-level) | A×2 + partial |
| Admin management surface (create/delete/block/export/conversion) | ✓ (create, convert, remove; compliance controls) | ✓ (create, export, filter, block/unblock, delete with re-auth) | ✓ (admin manages users/quotas) | A×3 |
| Internal-only collaboration layer (comments/notes on conversations, co-authored drafts, per-person states) | ✗ (absent from the object) | ✗ (explicitly absent; vendor routes that need to a SEPARATE product — TeamInbox) | ✗ | A×3 — the sibling Type's signature is absent here |
| Org-internal membership only; external participation routed to other objects | ✓ (external users denied; "consider creating a group") | ✓ (no external members on shared mailbox; DL allows them) | (account-internal users) | A×2 + partial |

Reading of the matrix:

- **Stable across all three (defining candidates):** a shared object with its own address held/administered independently of members; multi-member access granted to identified people and revocable; one common store worked in place rather than copies distributed to personal mailboxes.
- **Strong commonality (mature structure):** permission modes for sending (as / on behalf), automatic appearance in members' clients, shared calendar, aliases, mailbox-level rules/auto-reply/moderation, admin management surface, org-internal membership boundary.
- **Container-dependent (variant):** mailbox entity vs group-shaped object vs shared folders in a multi-user account; client surface shape; compliance machinery; credential enforcement details.

## Abstraction Hierarchy (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

1. **A mailbox entity held independent of any member.** A dedicated mailbox on the mail system — its own address (and display name), its own store of correspondence and folders — that exists and is administered as an object (created, configured, granted, revoked, deleted by an administrator), distinct from every member's personal mailbox. Remove → personal email client / webmail.
2. **Deliberate multi-member access to operate it.** Several identified people are granted — and can be denied or stripped of — permission to open the mailbox and work its correspondence (read and act on its mail, and, per permission mode, send under its identity); access is granted against members' own identities rather than a shared credential. Remove → one person's mailbox = Email Client; credential-sharing is the anti-pattern this object replaces, not the Type.
3. **One common correspondence store, worked in place.** Mail addressed to the mailbox is delivered once into the mailbox's own store; members work it there — replying, filing, acting on the shared record visible to all members — instead of receiving copies into their personal mailboxes. Remove → distribution list / alias (copies to personal mailboxes) and out-of-band coordination.

Note on sending: permission to send under the shared identity is the expected operating capability and is documented with distinct permission modes, but the invariant in leg 2 is the *operation* of the mailbox by members (read/act/send per grant), not any specific permission mode — a monitored, receive-only shared mailbox remains recognizable.

### L1 — Common Mature Structure (very common, not definitional)

- permission granularity on the object: work/access rights separable from send rights, with "send as" and "send on behalf of" as distinct modes (externally visible difference in the latter)
- automatic appearance of the shared mailbox inside members' mail clients (mapping/approximate equivalents), plus web and mobile access surfaces
- a shared calendar attached to the shared mailbox context
- aliases / additional addresses on the shared object
- mailbox-level configuration: auto-replies, forwarding, rules, inbound moderation
- administration surface: create/edit/delete, membership and role management, block/unblock, export, conversion to/from user mailboxes
- organizational boundary: membership drawn from the organization's own directory; external participation directed to other object types
- compliance machinery at the mailbox level (archive, hold, retention) — commonly licensing-gated

### L2 — Variant / Optional Structure (container-, deployment-, segment-dependent)

- container shape: dedicated mailbox entity (suite-classic) vs group-shaped shared mailbox (group object carrying shared-mailbox delivery semantics) vs shared folders within a multi-user account
- credential enforcement: direct sign-in blocked by policy (modern default) vs historical shared-account practice (discouraged/forbidden today)
- member access surface shape: folder set inside the desktop client / added account in webmail / account switcher / mobile app
- scale & compliance depth: storage tiering, archiving, litigation hold, retention policies — plan/licensing-dependent
- moderation/inbound control depth (who may send to the address; moderation queues; block/unblock)
- the shared mailbox as bare substrate beneath heavier layers (collaboration products, help desks)

### L3 — Vendor-specific (research notes only; not in the final document)

- Microsoft: unlicensed storage cap (50 GB; 100 GB licensed), documented simultaneous-user guidance (25) before degradation, automapping set per-user and incompatible with security-group-based access, Send As/On-Behalf failing for hidden address-list mailboxes, encryption impossible from the object (no own security context), user-mailbox↔shared conversion, pre-2018 legacy sizing, "not possible to migrate a shared mailbox to Microsoft 365 Groups," explicit six-object group taxonomy (shared mailboxes vs distribution groups vs M365 Groups vs mail-enabled security groups vs dynamic distribution groups vs security groups).
- Zoho: shared mailbox as group subtype; no external members; no Streams; mandatory moderator role; four inbound access types; block/unblock with MFA re-auth and 5-minute re-auth window; CSV/cloud import-export (Google Workspace / M365 / WorkMail); 7-day post-deletion recovery window; TeamInbox cross-marketing callout.
- Fastmail: single payment for multi-user accounts; shared folders/contacts/calendars; retention archive; user quota management.
- Cross-referenced (not verified this pass): Google Groups collaborative inbox states (assignment/resolution) and Gmail delegation mechanics — sibling pass recorded these as substrate-level facts.

## Rejected Findings (anti-overfitting)

- **"Shared mailbox = Microsoft's mailbox entity."** Zoho's group-shaped realization and Fastmail's folder-sharing realization both satisfy the same jobs with different containers. The invariant is the structure (own address + own store + managed multi-access + one common record), not the container class.
- **"Send As is definitional."** The permission triad (work / send-as / send-on-behalf) is Microsoft-explicit and Zoho-partial; a receive-and-monitor-only shared mailbox remains recognizable. Operation-per-grant is the invariant; specific modes are mature structure.
- **"No separate login is definitional."** Blocking direct sign-in is a modern enforcement posture (Microsoft explicit). Historically the object existed in credential-shaped forms. The invariant is access granted against members' own identities, which is leg 2's wording.
- **"Shared calendar is definitional."** Auto-created in Microsoft's implementation and present in others, but a shared mailbox without a calendar is still a shared mailbox.
- **"Membership is always org-internal."** Both suite vendors in the sample restrict membership and route external needs elsewhere, but this is a boundary choice of the sampled suites (and sensible security posture), held as common behavior, not invariant.
- **"A shared inbox product is a shared mailbox."** Market vocabulary collision — products marketed as "shared inbox" are mostly the sibling Type (collaboration layer). Zoho itself ships both as separate products. Vocabulary is not structure.
- **"25 users / 50 GB / 5-minute re-auth"** — vendor limits and defaults; never promoted.

## Boundary Findings

- **vs Distribution list / alias (no directory leaf; conceptual):** the sharpest structural contrast, documented explicitly by Zoho ("copy of the email gets delivered to the mailbox of all the members" vs "do not appear in the individual user's mailbox") and by Microsoft's own group taxonomy (distribution groups = "sending email notifications to a group of people"). Test: remove leg 3 (one common store) → the object becomes a distribution list.
- **vs Email Client:** one person's own mailbox vs an entity independent of any member. The email client is also the *surface* through which members often access shared mailboxes — access surface ≠ the Type. Test: remove legs 1+2 → Email Client territory.
- **vs Email Collaboration Application (sibling; JOINT REVIEW DISCHARGED):** the agreed discriminator holds from this side — **the shared mailbox entity as the primary object** (administered object, membership-granted access, common store) vs **the collaboration layer as the primary object** (internal side-channel on conversations, co-authored drafts, ownership states, per-person visibility, extending beyond dedicated addresses to individual inboxes). Corroborations obtained this pass: (1) Zoho ships "Shared Mailbox" (mail-system object, bare) and "TeamInbox" (collaboration product) as two separately-named products — the vendor's own taxonomy confirms the seam; (2) the sampled shared-mailbox implementations carry **no** internal-comment/co-draft/per-person-state machinery — the sibling Type's signature layer is absent throughout this leaf's sample. Light operating states on group-collaborative inboxes (assignment/resolution marks — recorded for the Google substrate in the sibling pass) sit at the seam: they are mailbox-operating states, not a conversation-anchored collaboration layer, and stay in this leaf while the entity remains primary. When the collaboration layer becomes the product's center and extends to individual inboxes and private conversations, it has crossed into the sibling Type.
- **vs group-workspace objects (e.g. suite "Groups" / team spaces):** group objects bundle a collaboration workspace (conversations, files, planning services) with a group email; the shared mailbox is the bare correspondence object. Microsoft's own comparison page holds them as distinct object classes with different deletion semantics and explicitly forbids migration between them. Test: add bundled collaboration services → the object becomes a group-workspace thing, not a shared mailbox.
- **vs Help Desk / Ticketing System:** the shared mailbox is the substrate under many support operations; the Type boundary is the managed object (ticket with fields/SLAs/CSAT vs mailbox correspondence). When queue/assignment/SLA machinery is added on top and the ticket becomes the unit, the product is a Help Desk. Hiver's 2026 drift (recorded by the sibling pass) evidences the axis.
- **vs Webmail Application:** webmail is the browser surface for a personal mailbox; shared mailbox access may appear through webmail surfaces, but the webmail Type's object is the personal mailbox.
- **vs delegated personal mailbox (fuzzy edge):** one person's mailbox shared with an assistant (delegate access) is a person-owned mailbox with granted access, not an entity independent of a member; client-level delegate access belongs to Email Client / platform features. The sibling leaf covers the pattern when a collaboration layer is built over it. Recorded as the deliberate edge of leg 1.
- **vs Email Infrastructure Management (§14 leaf):** creating/granting shared mailboxes is an administration act performed in mail-system consoles; the center of THIS leaf is the shared mailbox object and its operation by members, not infrastructure administration. Facility overlap only.

## Uncertainties

- **Google Workspace mechanics unverified.** All support.google.com fetches timed out; Google's collaborative inbox and delegation semantics are held only at the substrate level cross-referenced from the sibling pass. No operational claims about Google are made in the final document.
- **Member-side client mechanics** (exactly how the shared mailbox renders in desktop/web/mobile clients, per-member read/unread behavior on the shared store) could not be verified at article depth: the "Open and use a shared mailbox in Outlook" support article 404'd. The final document describes the member access surface conceptually and avoids per-client claims. Read/unread-state handling on shared stores is known to vary across products/clients and is deliberately left unspecified.
- **Fastmail evidence depth** is index-level (multi-user account model documented; per-article mechanics not fetched). Its role in the sample is the container-contrast pole; no deep claims made.
- **Zoho group-calendar linkage** and the shared mailbox's user-side operations (beyond "see the shared mailbox in their mail account") were not evidenced beyond the admin guide.
- Numeric limits, plan gating, licensing conditions are documented only in Research Notes (vendor-specific tier), never in the final document.
- The historical reach (pre-cloud role accounts, public folders, Unix shared spools) is reasoned at the conceptual level (layer C): the three-leg definition is satisfied by admin-created role addresses with shared access on any era of mail system; no single legacy product was fetched as a primary source this pass — the on-premises Exchange Server 2016/2019/SE documentation (fetched, Tier-1) serves as the pre-cloud-era anchor.

## Final Synthesis

The Shared Mailbox Application is the application of a mailbox that belongs to no one: a dedicated, administrator-held mailbox entity — its own address, its own store — operated collectively by identified members under deliberate, revocable access, with the correspondence held and worked in one common place rather than copied into personal mailboxes. Its world is built from three things: the shared mailbox entity (address, store, folders, commonly a calendar, and mailbox-level configuration such as auto-replies, aliases, rules, and inbound moderation); the membership/permission structure (who may open and work it, and who may send as or on behalf of it); and the two surfaces through which it is lived — the administration surface (create, membership, permissions, block, delete) and the member access surface (the mailbox's folders inside the member's mail client, the shared identity in the From field). The defining core is exactly the three legs — entity independent of members, managed multi-member operation, one common store worked in place — with the container shape (mailbox entity vs group object vs shared folders), the enforcement posture, the compliance machinery, and the client surfaces all being implementation variants. Everything conversation-collaborative (internal comments, co-authored drafts, ownership states) belongs to the sibling Email Collaboration Type; everything ticket-shaped belongs to Help Desk; everything copy-distributing belongs to the distribution list.
