# Shared Mailbox Application

## Overview

A **Shared Mailbox Application** is an application built around a dedicated mailbox that belongs to no single person: an organizational email address with its own store of correspondence, held and administered as an object in its own right, and operated collectively by several identified members under deliberate, revocable access. Mail sent to the shared address is delivered once — into the shared mailbox's own store — and the members work it there, replying and acting under the mailbox's identity rather than their own.

The defining structure is small:

```text
Shared Mailbox Entity (own address · own store of correspondence · administered, not owned)
├── Membership / Access (identified members granted — and revocable — permission
│   to open, work, and send under the shared identity)
└── One Common Store (mail held and worked in place; not copied
    into members' personal mailboxes)
```

Remove the entity and it becomes a personal email client; remove managed multi-member access and it becomes credential-sharing; remove the common store and it becomes a distribution list that forwards copies into personal inboxes.

Everything else commonly associated with shared mailboxes — calendars, aliases, auto-replies, rules, moderation, compliance archiving, particular client behaviors — is widespread but not what makes the Type.

## Users & Context

The primary users are members of an organization who collectively operate correspondence that belongs to a function rather than to a person. Typical roles:

- **members / staff**: open the shared mailbox inside their own mail client, read the mail waiting there, reply as the shared address, and file or act on the correspondence
- **administrators**: create the shared mailbox, manage its address and settings, grant and revoke member access, and control sending permissions

Typical contexts are role and function addresses where continuity matters more than any individual: company information and support addresses, reception and front-desk mailboxes, sales and billing addresses, departmental addresses (payroll, HR, facilities), and similar roles staffed by more than one person. External senders and recipients see only the shared identity — mail from the mailbox appears to come from the mailbox, not from whichever member replied.

The work is spread across two surfaces: an administration surface (where the mailbox exists as a managed object) and the members' own mail clients (where the mailbox's contents are opened and worked day to day).

## Core Model

### The Defining Core

```text
Shared Mailbox Entity (own address · own store · administered, not owned)
├── Membership / Access (grant, revoke; operate per permission)
└── One Common Store (work in place; no copies to personal mailboxes)
```

Three properties. If any one is removed, the product is no longer recognizable as this Type:

- **A mailbox entity held independent of any member.** The shared mailbox has its own address and display name on the mail system, its own store of received and sent mail and its own folders. It exists as an administered object — created, configured, granted, revoked, and deleted by an administrator — and is distinct from every member's personal mailbox. It is not anyone's mail; it is the function's mail.
- **Deliberate multi-member access.** Several identified people are granted permission to open the mailbox and work its correspondence — reading and acting on its mail, and, per the permissions they hold, sending under its identity. Access is granted against the members' own identities and can be revoked when they change roles or leave. This is the structural alternative to sharing a password: the object has no operational login of its own, and membership is the access control.
- **One common store, worked in place.** Mail addressed to the shared mailbox is delivered once, into the mailbox's own store. Members work it there — replying, moving, filing, acting on the shared record that all members see — rather than receiving copies into their personal mailboxes and coordinating outside the mailbox. The mailbox is the place where the correspondence lives, not a forwarding point.

### The Mailbox as an Object

In the dominant realization, the shared mailbox carries more than an inbox:

- **its own address** (and commonly additional alias addresses) on the organization's domain
- **its own folders and state** — the received correspondence, the replies sent under its identity, drafts and filed mail belonging to the function
- **a shared calendar** attached to the shared context in many implementations, usable for the function's appointments and schedules
- **mailbox-level configuration** — automatic replies, forwarding, rules that sort its incoming mail, and in some implementations inbound moderation that holds or filters what reaches the members

A personal mailbox can often be converted into a shared mailbox, and vice versa — evidence that the underlying object is the same class of thing, held under a different model of ownership and access.

### Membership and Permissions

Access is managed as membership, with the rights separable:

- **work access** — open the mailbox and act on its contents: read, move, file, delete, create items
- **send as** — mail leaves appearing to come from the shared mailbox itself
- **send on behalf of** — mail leaves identified as a named person acting on behalf of the shared mailbox, an externally visible distinction

A member may hold work access without any sending right; sending rights are granted deliberately, and the two sending modes are distinguishable permissions rather than one switch.

### One Structure, Many Implementations

The core model is written conceptually. The Variants section below enumerates how implementations realize each concept.

```text
Concept:          The shared entity
Implementations:  a dedicated mailbox object administered in a management
                  console; a group-shaped object carrying shared-mailbox
                  delivery semantics; shared mail folders inside a
                  multi-user account

Concept:          Access
Implementations:  membership with named permissions; moderator/member roles;
                  account-level user sharing

Concept:          Member surface
Implementations:  the mailbox's folder set appearing inside the member's
                  desktop client (often automatically), an added account or
                  identity switcher in webmail, mobile app access
```

## How It Works

### Provision the mailbox

```text
Administrator creates the shared mailbox (name + address)
→ configures aliases, automatic replies, forwarding, rules, moderation as needed
→ adds members from the organization's directory
→ grants permissions: work access, and send-as or send-on-behalf where warranted
→ the mailbox appears in members' mail clients (in many implementations,
  automatically, without any setup on the member's side)
```

### Work the correspondence

```text
Mail arrives at the shared address → delivered into the shared mailbox's store
→ a member opens the shared mailbox from inside their own client
→ reads the mail waiting there (the same record every member sees)
→ replies as the shared address — or on behalf of it, per their permission
→ the reply is filed with the mailbox's sent mail; the external party
  corresponds with the shared identity, not the individual
→ the member moves, files, or deletes mail as the function requires;
  the action applies to the common record
```

### Manage access over time

```text
People join the function → administrator adds them as members; they gain access
People leave or change roles → administrator removes them; access ends,
  the mailbox and its correspondence are untouched
The function ends → the mailbox is deleted or converted (for example,
  a departing employee's mailbox converted to a shared one)
```

### Housekeeping

Around the daily loop, administrators handle the mailbox-level machinery: adjusting addresses and aliases, setting automatic replies for closed periods, controlling inbound moderation, blocking or unblocking the mailbox's mail flow, and applying retention or compliance controls where the organization requires them.

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Administration surface

Where the mailbox exists as a managed object — a dedicated section in the mail platform's admin console.

- lists the organization's shared mailboxes (name, address, members)
- primary actions: create, edit address/name/settings, add or remove members, grant or revoke send permissions, block/unblock, delete

### Member access surface (inside the mail client)

The day-to-day surface: the shared mailbox's contents opened within the member's own mail client.

- the shared mailbox's folder set (inbox, sent, drafts, calendar) alongside or beneath the member's personal mailbox, or reachable through an account switcher
- primary actions: read, reply as / on behalf of the shared address, move, file, delete

### Compose surface

- the standard compose window with the shared identity selected in the From field
- the sent message is filed with the shared mailbox's sent correspondence

### Directory entry

The shared mailbox is an addressable entry in the organization's directory, so colleagues can address mail to the function and the mailbox can appear in address completion.

## Important Rules / Behaviors

### Actions apply to the common record

What a member does to the shared mailbox's mail — replying, moving, filing, deleting — is done to the mailbox's shared state, the record all members see. Fine-grained per-member behaviors (such as exactly how read/unread marking behaves on the shared store) vary by product and client.

### The external party sees the function, not the person

Replies leave under the shared identity. The two sending modes differ visibly on the receiving end: mail sent "as" the mailbox appears to come from the mailbox alone; mail sent "on behalf of" it carries the acting person's name alongside the mailbox. Members can only send this way if the corresponding permission was granted to them.

### No operational login for the object itself

In current implementations the shared mailbox is not something anyone signs into directly: members operate it through their own identities, and direct sign-in for the mailbox's underlying account is blocked or discouraged. The historical practice of sharing one account's credentials among staff is what this model exists to replace.

### Access is organizational and revocable

Membership is drawn from the organization's own directory; external people are not members of the mailbox (suites route external collaboration to other object types). Membership can be granted and revoked at any time without touching the correspondence itself.

### Work access and sending rights are separable

Holding work access does not by itself confer the right to send under the shared identity; the sending permissions are distinct grants.

### Members can act, and the object does not police it

In the bare object model, the system does not prevent a member from deleting or moving mail, and does not arbitrate who works which message — coordination is the team's discipline, not the mailbox's enforcement. Heavier control machinery (restricting deletion, arbitrating work) belongs to other object types and products built on top.

## Variants

The Type is realized in several recognizable shapes. Common variants:

- **dedicated mailbox entity** — an administered mailbox object with its own address and store, no operational login, members granted access by permission; the dominant enterprise-suite pattern
- **group-shaped shared mailbox** — a group object configured with shared-mailbox semantics (one shared delivery, no copies to members), administered through group management with member and moderator roles
- **shared folders within a multi-user account** — the team's common mail held as folders shared among the account's users, rather than a separate entity per address
- **delegation-style access** — a mailbox surfaced to a small set of operators through delegate access from their own clients; structurally at the edge of the Type when the underlying mailbox is a person's own
- **the shared mailbox as substrate** — the bare object serving as the base layer under shared-inbox collaboration products and support desks, which add queue, ownership, and service machinery on top

A variant should remain a **Variant**, not become a separate Type, unless it changes the users, core objects, workflow, or rules so much that the defining core no longer applies. The two drift axes most likely to cross that line: adding a native collaboration layer over the conversations (internal discussion, co-authored drafts, ownership) — the territory of the Email Collaboration Application — and converting the correspondence into tickets with service machinery — the territory of Help Desk.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Email Client | one person operating their own mailbox; also the surface through which members often access shared mailboxes — access surface, not the Type itself |
| Webmail Application | browser surface for a personal mailbox; a shared mailbox may be opened through such a surface, but the managed object there is personal mail |
| Email Collaboration Application | the collaboration layer over correspondence is the primary structure (internal side-channels, co-authored drafts, ownership states, extending to individual inboxes and private conversations); here the shared mailbox entity itself is the primary object, typically without a conversation-anchored collaboration layer |
| Team Messaging Application | internal chat with no email transport and no external mail identity |
| Help Desk / Ticketing System | the managed unit is a ticket with its own fields and service machinery; here it is the mailbox correspondence itself — shared mailboxes are a common substrate beneath support desks |
| Email Marketing Platform | outbound bulk sending to lists; no shared operation of a live correspondence store |
| Email Infrastructure Management | system-level administration of the mail platform; this Type centers on the shared mailbox object and its collective operation |

The closest boundary is the **Email Collaboration Application**. The market vocabulary overlaps heavily — "shared inbox" is used by products on both sides — and several vendors ship both kinds of products separately: a bare shared mailbox inside the mail platform, and a separately-named shared-inbox collaboration product. The working discriminator is whether the shared mailbox entity (administered object, membership-granted access, one common store) is the primary structure, or a collaboration layer built over conversations is.

## Representative Products

- Microsoft 365 / Exchange (shared mailboxes)
- Zoho Mail (shared mailboxes)
- Fastmail (multi-user account sharing)
- Google Workspace (collaborative inboxes / delegated mailboxes)

The sample spans the main realizations: the canonical administered mailbox entity, a group-shaped implementation inside an independent suite, a folder-sharing model in a multi-user account, and the group-address realization of the other major suite.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces:

- Microsoft Learn — About shared mailboxes; Create a shared mailbox; Compare types of groups in Microsoft 365: https://learn.microsoft.com/en-us/microsoft-365/admin/email/about-shared-mailboxes , https://learn.microsoft.com/en-us/microsoft-365/admin/email/create-a-shared-mailbox , https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/compare-groups
- Microsoft Learn (Exchange Server) — Create shared mailboxes in the Exchange admin center: https://learn.microsoft.com/en-us/exchange/collaboration/shared-mailboxes/create-shared-mailboxes?view=exchserver-2019
- Zoho Mail admin guide — Creating email groups; Shared Mailbox admin settings: https://www.zoho.com/mail/help/adminconsole/creating-groups.html , https://www.zoho.com/mail/help/adminconsole/collaborative-inbox-settings.html
- Fastmail help center — Managing multi-user accounts: https://www.fastmail.help/hc/en-us/articles/360060590673-Managing-multi-user-accounts

> Sourcing limitations: Google's support documentation was unreachable from the research environment (repeated timeouts), so the Google Workspace realization is described only at the level of shared-operation structure, with no operational mechanics asserted for it. The member-side client documentation for one sampled suite was not retrievable (404), so member client behavior is described conceptually rather than per-client. Precise operational details (storage caps, user-count guidance, plan gating, licensing conditions, per-product limits and defaults) are intentionally not stated in this document; such details remain in the paired Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
