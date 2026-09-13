# Social Profile Network

## Overview

A **Social Profile Network** is an application whose primary object is the **personal profile of record**: a persistent, self-maintained profile bound to one person, addressable in a shared namespace, and designed to be consumed outside the application itself — embedded in other sites, linked from other platforms, shared person-to-person, or synced into other systems.

It solves a problem every other social application treats as incidental: a person's identity scattered across many surfaces, each holding a stale copy. Here the profile is the whole product. The user maintains one authoritative record of themselves; the application's job is to make that record findable, trustworthy, and consumable everywhere it is referenced.

The defining core is deliberately narrow. A content feed, a follower graph, messaging, and audience analytics are all common in some products of this family, but none of them defines it. What defines it is the profile as a portable, addressable identity object whose primary consumption happens elsewhere.

## Users & Context

The primary user is an individual who needs a single authoritative representation of themselves that others — people, organizations, and software systems — can find and rely on:

- a researcher who needs one unambiguous identity across publications, grants, and institutions
- a creator or professional whose audience lives on other platforms and needs one place those platforms can point to
- a professional who meets people and wants them to receive correct, self-updating contact details
- anyone who wants one consistent name, image, and description across the web

A secondary user class appears in organization-facing variants: administrators who issue and govern profiles on behalf of team members (branded cards, template-controlled profiles).

The context is inherently cross-surface. The profile is edited inside the application but consumed mostly outside it — in another platform's bio, a third-party site's comment section, someone's address book, a manuscript submission system. The application is a hub; the consumption is everywhere else.

## Core Model

### The Defining Core

```text
Personal Profile of Record
└── Shared-namespace addressability
    └── Outward consumption design
```

Three structures, jointly held:

- **Personal profile of record** — a persistent profile bound to one person, owned and maintained by that person (or, in organization-facing variants, issued to them and claimed by them). It accumulates the person's identity content over time and survives any single use. Without it, the product is just an identity-assertion service.
- **Shared-namespace addressability** — the profile carries a stable identifier in a namespace shared across the whole user population: a unique iD, a handle, a username URL, a hash-keyed address. Other people *and other systems* use this identifier to find and reference the profile. Without it, the profile is a private account page — a capability of any product, not a Type.
- **Outward consumption design** — the profile is built to leave the application: fetched by other systems through public interfaces, linked from other platforms, exchanged person-to-person, embedded in third-party contexts. The product's value is the profile's circulation, not time spent inside it. Without this, the product is merely another application's internal profile page.

### What a Profile Holds

Profile content varies by pole, but a common mature content model includes:

- display name and avatar/image
- short bio or description
- role, affiliation, or occupation
- location and contact channels
- links — to other profiles, verified accounts, works, or destinations
- visibility/privacy state per field

### The Network in "Profile Network"

The "network" is the mesh of references around each profile — and it takes different shapes across products:

- links from **other systems** that consume the profile (thousands of third-party sites and services)
- links to **verified external accounts** that attach trust to the profile
- links to **works and affiliations** the person is connected to
- exchanged **person-to-person connections** where two profiles link to each other and stay synchronized
- an explicit **follow graph** between profiles

Person-to-person connection graphs are common in some products but not universal — several mature products in this family carry no social graph at all, and remain clearly in-type. What is universal is that every profile is **linked into a wider identity web**: referenced by other surfaces, connected to external accounts or works, or tied to other profiles.

### One Structure, Many Implementations

```text
Concept:   Personal Profile of Record
Realized:  registry record, hosted profile page, link-hub page, digital business card, on-chain profile

Concept:   Shared-namespace Addressability
Realized:  unique persistent iD, username URL, email-hash address, handle

Concept:   Outward Consumption
Realized:  public profile API, link pasted into other bios, shareable card, embeddable avatar/profile, multi-frontend protocol
```

## How It Works

### Establish the profile

```text
Register in the shared namespace
→ claim a stable identifier (iD / handle / username URL)
→ compose the profile: name, image, description, role, links
→ set visibility per field
```

There is no workspace, no channel, no feed to configure. The entire setup is the profile itself.

### Keep the record authoritative

The owner edits the profile as their identity changes — new role, new links, new image. In products with person-to-person connections, an edit propagates automatically to everyone holding a linked copy of the profile; in products consumed by other systems, the change is picked up the next time those systems read the profile. The record stays authoritative because copies derive from it, not the other way around.

### Circulate the profile

```text
Share the identifier or the profile itself
→ into another platform's bio field
→ into an email signature or document
→ person-to-person (exchange, QR, link)
→ into another system via public API / embed
```

Circulation is the core loop. The application measures success in profile views, lookups, embeds, and exchanges — not in feed engagement.

### Attach trust (where offered)

Some products let the owner connect verified external accounts or institutional affiliations to the profile, so a viewer can judge how much trust to place in the self-authored content. Verification is an optional trust layer over the profile, never the definition of it.

### Browse and discover

Most products expose a directory or search over the shared namespace: look a person up by identifier or name, view their profile, follow a link out. Discovery is lookup-shaped (find a specific person or verify an identity), not feed-shaped (consume a stream).

## Interfaces

Described conceptually; exact layouts vary by product.

### Profile editor

The owner's primary surface.

- purpose: compose and maintain the profile of record
- typical content: name, image, description, role, links, per-field visibility
- primary actions: edit fields, reorder links, upload image, set visibility, save

### Public profile page

The profile as the world sees it, at its namespace address.

- typical information: identity content, links, verification marks, associated works or destinations
- primary actions: view, follow a link out, share the address, (where supported) connect or follow

### Directory / search

Lookup over the shared namespace.

- purpose: find a person's profile by identifier, name, or attributes
- primary actions: search, view profile, (where supported) save or connect

### Sharing / circulation surface

The tools that push the profile outward.

- purpose: place the profile or its identifier into external surfaces
- typical forms: shareable URL, QR code, embed snippet, exchange action, public API for other systems
- primary actions: copy link, generate code, exchange with a nearby person, fetch/integrate (API side)

### Connection / contact surface (where person-to-person linkage exists)

The holder's view of profiles they are linked to.

- typical information: linked profiles and their current content, sync state
- primary actions: exchange/connect, view updated details, remove connection

### Analytics (audience-facing variants)

For profiles consumed by an audience: views, clicks, referrers — feedback on circulation.

## Important Rules / Behaviors

- **The profile is the record; copies derive from it.** Wherever the profile is consumed — an embedded avatar, an exchanged card, a third-party fetch — the application-side record is authoritative. Linked copies update when the record changes; this "self-updating copy" behavior is the family's signature promise.
- **Addressability is stable.** The namespace identifier is designed to persist across role, employer, and platform changes — that stability is precisely what other systems build on.
- **Visibility is field-level.** Profiles mix public and private content; mature products give the owner per-field control over what the namespace exposes.
- **Self-authored, optionally verified.** The profile's content is the owner's own assertion. Verification features (verified accounts, institutional links) attach external trust to selected fields but do not replace self-authorship.
- **No feed obligation.** Nothing in the core model requires a content stream. Products that add one treat it as an extension; when the stream becomes the primary consumption surface, the product has drifted toward a feed-centered social network Type.

## Variants

- **Identity registry** — the profile as a scholarly/professional persistent identifier connected to works and affiliations, consumed by thousands of external systems; typically non-profit infrastructure with governance over the namespace (e.g. ORCID).
- **Global profile layer** — profiles keyed to an existing identifier (commonly an email address), fetched by third-party sites to populate avatars and profile data everywhere the identifier appears (e.g. Gravatar).
- **Link-in-bio hub** — the profile as a curated hub page whose address is placed into other platforms' profile surfaces; audience and content live on those other platforms (e.g. Linktree).
- **Digital business card** — the profile as an exchangeable card; exchanging creates live person-to-person connections whose copies self-update; often extends to organization-issued branded cards (e.g. HiHello).
- **Protocol social graph** — profiles and their follow graph as owned, portable protocol objects consumed by many independent frontends; the substrate is the product, the frontends are interchangeable (e.g. Lens Protocol).
- **Organization-issued variant** — profiles (cards) created and governed by an organization's administrators, claimed by members; adds template, branding, and team-contact machinery on top of the personal core.

## Related Application Types

| Application Type | Distinction |
|---|---|
| General Social Network | core consumption loop is a content stream over a self-curated graph; here the loop is profile lookup and circulation — a social network's profile page is one surface among many, here it is the whole product |
| Professional Social Network | centers a career audience with feed and recruiting machinery; a profile network has no feed and no audience-specific workflow |
| Friend Discovery Application | centers finding new people to interact with; a profile network centers maintaining and circulating one's own identity record |
| Member Directory | organization-scoped roster largely maintained by the organization; here profiles are self-maintained by the person in a public, cross-organization namespace |
| Identity Verification / KYC | asserts real-world identity against documents; here the profile is self-authored presentation, with verification only an optional attachment |
| Customer Identity / CIAM | authentication and access-control infrastructure; here there is no access contract — the profile is presentation and circulation |
| Contact Manager | holds your inbound copies of other people's details; the profile network holds each person's own record of themselves — some products bundle both, anchored on the profile |
| Microblogging Platform | broadcast posts consumed in a merged stream; here there is no post stream — the profile and its references are the content |

The closest family relationship is with the social networks: every social network contains a profile, and this Type is what remains when the feed, the stream, and the audience machinery are removed and the profile is left standing alone as the product.

## Representative Products

- ORCID — scholarly identity registry
- Gravatar — global profile layer
- Linktree — link-in-bio hub
- HiHello — digital business card
- Lens Protocol — decentralized social-graph protocol

The core model was checked across these five deliberately different poles (registry / layer / hub / card / protocol) so that the definition would not collapse into any one market's implementation — in particular, so that the absence of a person-to-person connection graph in three of the five poles would not disqualify them.

## Sources

Research date: **2026-09-10**

Official vendor surfaces (retrieved via web search excerpts; live full-page fetch was not possible from the research environment on this date):

- ORCID — https://orcid.org/ , https://info.orcid.org/what-is-orcid/ , https://support.orcid.org/
- Gravatar — https://gravatar.com/ , https://support.gravatar.com/your-profile/ , https://docs.gravatar.com/
- Linktree — https://linktr.ee/ , https://help.linktr.ee/
- HiHello — https://www.hihello.com/ , https://support.hihello.com/
- Lens Protocol — https://lens-protocol.github.io/ , https://api-v2-docs.lens.xyz/ , https://github.com/lens-protocol/core

> Sourcing limitation: vendor help-center pages could not be fetched directly; evidence comes from official-domain content returned through web search. Precise operational details (numeric limits, exact field schemas, plan-specific behavior) are intentionally not stated in this document; such details remain in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, and the boundary analysis against the neighboring social-network Types are recorded in the paired Research Notes.
