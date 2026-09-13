# Music Distribution Platform

## Overview

A **Music Distribution Platform** is a rights-holder-facing supply-chain service: it takes a packaged music release — the recordings, their metadata, and artwork — and delivers it to a managed network of consumer storefronts and streaming services, controls when and where the release is available, and passes the money those services report back to the rights holder, itemized and paid out after the platform's share.

It solves a structural problem of the recorded-music business: individual artists and labels cannot negotiate delivery agreements with every streaming service, download store, and social platform themselves. The distribution platform maintains those store relationships once, then operates as the pipeline through which many rights holders' releases reach many storefronts — and through which the resulting earnings return.

The defining structure is small: a **release** as the managed unit of record, a **destination network** the platform can place releases on, a **delivery-and-availability lifecycle** (submission, review, go-live, takedown), and an **earnings pass-back** from stores to the rights holder's account. Everything else the modern market attaches — analytics, collaborator splits, Content ID, publishing administration, promotion, physical distribution — is common but optional; the platform never takes ownership of the recordings.

## Users & Context

**Primary users** are the people who own or administer recordings:

- **independent artists** — assemble and submit their own releases, choose destinations, track earnings
- **labels** — run larger catalogs through the same machinery, often across many artists; on some platforms through dedicated label accounts or negotiated agreements
- **managers and self-releasing collectives** — operate releases on behalf of artists

**Secondary actors** inside the platform:

- **review / trust-and-safety staff** — check submissions against content and metadata rules before delivery
- **support teams** — handle corrections, store-specific issues, takedowns, payout problems
- at the enterprise pole, **account managers** who operate the pipeline for contracted labels

The work context is a web dashboard (sometimes with a mobile companion). The rhythm of use is release-shaped: concentrated bursts of authoring and submission around a release, then periodic visits to check delivery status, store links, and earnings.

## Core Model

### The release — the unit of record

The center of the platform's world is the **release**: a packaged body of recordings — a single, EP, or album — assembled by a rights holder from:

- **audio files** for each track
- **metadata**: release and track titles, main artist and featured artists, contributors (performers, producers, songwriters), language, genre, copyright/label lines, explicit flags, lyrics
- **artwork** meeting store-specified requirements
- **standard commercial identifiers**: a UPC (or EAN) for the release and an ISRC for each track — the codes that bind the release's identity across every store it lands on. Platforms commonly generate these codes when the rights holder doesn't have them, and their reuse rules are strict: an identifier stays valid only while the underlying content stays identical.

The release belongs to a **rights holder account** — an individual artist or a label that may represent many artists. A catalog is the account's collection of releases over time.

### The destination network

The second defining object is the **store** — the platform's term for a managed destination release can be placed on. The network is far more heterogeneous than "Spotify and Apple Music":

- interactive streaming services
- download stores
- social and user-generated-content platforms (short-form video especially)
- regional and niche services serving specific markets
- discovery and recognition services
- non-music contexts that license music (fitness platforms, jukeboxes)
- business-to-business content providers that themselves power other services

The platform holds the delivery relationships with all of these; the user does not. Per release, the user selects destinations — usually by accepting the default full network and opting out of specific stores — and optionally restricts territories. Not every destination behaves alike: some are curated and may decline a release; some make content available for preview before the official date; some report and pay through separate industry bodies rather than through the platform.

### The delivery-and-availability lifecycle

A release moves through a lifecycle with visible states. Conceptually, and with labels varying by product:

```text
draft/authored
  → submitted
  → under review (approved, or sent back for fixes / denied)
  → delivered to selected stores
  → live (on the scheduled release date)
  → (corrections / added stores / territory changes)
  → taken down
```

### The earnings pass-back

The fourth defining object is the **earnings loop**. Stores report usage and sales — streams, downloads, monetized plays — back to the platform on their own reporting schedules. The platform aggregates these into statements itemized per store, per track, and per period, nets out its own share according to the fee model, and credits the balance on the rights holder's account. From there the money is paid out automatically once the account meets the configured conditions (payout threshold, valid payout method, completed tax information).

### One structure, many implementations

The core model is conceptual; products realize it differently:

```text
Concept:            Release of record
Implementations:    per-release self-serve uploads (single/EP/album); label catalogs under agreement

Concept:            Destination network
Implementations:    fixed full-network default with opt-outs; per-store selection; curated/optional stores

Concept:            Availability control
Implementations:    scheduled release dates; pre-order/pre-save; immediate go-live; takedown on demand

Concept:            Fee model
Implementations:    flat annual subscription with unlimited releases; one-time fee per release; percentage of royalties; negotiated enterprise deals

Concept:            Earnings pass-back
Implementations:    per-store/track statements; dashboard balances; collaborator splits; advances against future earnings
```

A reader who has only seen the flat-fee self-serve model should still recognize an enterprise label distributor as the same Type — and vice versa.

## How It Works

### Assemble and submit a release

```text
create release (single or album)
→ add release details (title, artist, genre, language, release date)
→ upload tracks with full credits (performers, producers, songwriters) and audio
→ upload artwork
→ select stores / social platforms (or accept the full network)
→ set the release date
→ submit for review
```

Authoring is metadata-intensive by design: stores reject or misplace poorly formed releases, so platforms enforce formatting rules, require complete contributor credits, and check artwork against store specifications. The identifiers (UPC/ISRC) attach here — brought by the user or generated by the platform.

### Review and delivery

The platform's review team (or, at the enterprise pole, an account manager's process) checks the release against content, metadata, and fraud rules. Approved releases are delivered to the selected stores. From delivery onward the platform's control is partial by nature: **each store processes and goes live on its own schedule**, so a release may appear on different services at different times even with a single release date. Platforms therefore recommend submitting well ahead of the target date, and they typically cannot force a store to speed up. Curated services may accept or pass on a release regardless of the user's selection.

### Go live and manage

On the release date the release becomes available in each store that has processed it. The platform surfaces what it can — store links, status indicators, sometimes only for the major services — and the user manages the live release under strict change rules (see below). Stores can be added later to an already-live release; territories can be adjusted.

### Take down

Takedown is a first-class capability, not an exception: rights retire releases, replace mixes, or switch distributors. A takedown removes the release from the stores it was delivered to; processing again depends on each store. Granularity is release-level — individual tracks generally cannot be pulled from an album without taking down the whole release. A takedown is usually final: re-releasing the same music means creating a new release, with new or carefully reused identifiers.

### Collect and get paid

```text
stores report usage/sales on their own cycles
→ platform aggregates per store / per track / per period
→ platform's share deducted per the fee model
→ balance credited to the rights holder's account
→ payout triggered automatically when threshold + payment + tax conditions are met
→ statement history retained
```

Reporting lag is inherent: store-reported earnings arrive weeks after the consumption that generated them, so a release's earnings picture trails its listening activity. Collaborator splitting, where offered, divides the credited balance automatically among contributors before payout.

### Switching distributors

Catalogs move. A rights holder taking a catalog to a new platform requests takedown from the old one and re-delivers through the new one, reusing the same UPCs and ISRCs so that streams, playlist placements, and follower history survive the move. Platforms compete on making this migration safe, and the identifier discipline (reuse only when content is unchanged) is what keeps the catalog's identity intact across the switch.

### Capability tiers

**Defining core** — without these the product is not a music distribution platform:

- release of record (audio + metadata + artwork + identifiers) owned by a rights holder
- managed third-party destination network, selectable per release
- delivery lifecycle: submission → review → delivery → scheduled go-live → takedown
- earnings pass-back: store-reported revenue itemized to the account and paid out after the platform's share

**Standard capabilities** of mature products:

- per-store/per-track analytics and audience data
- release links and store-URL surfacing
- collaborator/royalty splitting on earnings
- pre-order / pre-save support
- YouTube and social-platform Content ID monetization
- cover-song licensing assistance
- publishing administration as a companion service
- catalog-transfer tooling that preserves identifiers and stream history
- label / multi-artist account structures
- fraud enforcement around artificial or manipulated streaming

**Optional / advanced**, depending on product and tier:

- physical distribution and disc/vinyl manufacturing
- mastering, promotion, playlist pitching, sync licensing, royalty advances
- enterprise account management under negotiated agreements
- deep regional network coverage and specialty destinations (audiobook/AI services, fitness, jukebox)

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Catalog / releases list

The account's discography at a glance.

- each release with its status (draft, in review, live, taken down), release date, and key identifiers
- primary actions: create a release, open a release, filter by status

### Release editor

The authoring surface — usually a step-by-step flow through release details, tracks, stores, and artwork.

- per-track metadata forms with contributor credits and required fields
- audio upload, artwork upload against published specifications
- store/destination selection with territory options
- primary actions: save, review, submit

### Release status / tracker

Where the waiting happens.

- current lifecycle state, review outcomes, per-store delivery progress and links
- primary actions: respond to review requests, view store links, request changes

### Earnings / statements

The money surface.

- statement views by store, track, and period; quantity × per-unit earnings = payable amounts after deductions
- account balance, payout threshold and method configuration, tax information, payout history
- primary actions: read statements, configure payout, withdraw

### Settings / account

Payout and tax configuration, payout methods, account roles (for label accounts), and connected-service controls (Content ID, artist-profile claiming on the major streaming services).

## Important Rules / Behaviors

### The platform never owns the music

Ownership of the recordings stays with the rights holder. What the platform holds is the right to distribute the delivered release for a contractual term — and that grant can be release-scoped: a release delivered through one platform generally cannot be simultaneously re-delivered by another until its term ends. Terms vary by product and deal.

### Stores go live on their own clocks

After delivery, availability is governed by each store's processing. Platforms document per-store timing as approximate and disclaim control over it; a uniform "release day" across all stores is an aspiration managed by submitting early, not a guarantee.

### Delivered metadata is effectively immutable

Once a release is delivered, its metadata is locked. What remains adjustable differs by product and tier: typo corrections and explicit-flag changes often go through support within defined windows; audio replacements, artwork swaps, and identifier changes are typically impossible without takedown and re-release. Store selection, territory settings, and cancellation remain open. This immutability is a structural consequence of releases being identified across many independent stores by shared codes.

### Takedown is final; identifiers are single-use across content changes

A removed release generally cannot be resurrected in place; it must be re-created as a new release. Identifiers bind to content: the same UPC/ISRC may be reused only for an identical release, which is exactly what makes catalog migration between distributors possible without losing streaming history.

### Not all money flows through the platform

Certain royalty streams — most notably non-interactive radio performance royalties — are collected by industry bodies outside the distributor relationship. A platform's statement is authoritative for the revenue it intermediates, not for all revenue a release generates.

### Fraud enforcement is partner-driven

When a store judges consumption inauthentic (artificial streaming, manipulation), the associated earnings can be zeroed and, on some platforms, the penalty the store levies is passed through to the account. The platform typically cannot overturn the store's determination.

### Review gates delivery

Releases are checked before delivery — against content policies, metadata formatting, artwork specs, and fraud rules. A submission can be sent back for fixes or denied outright; approval, not upload, is what starts the supply chain moving.

## Variants

- **DIY self-serve** — instant signup, flat annual subscription with unlimited releases, dashboard everything; the dominant consumer-facing pole
- **Per-release economics** — one-time fee per release (sometimes with optional paid renewals to keep it live); the oldest self-serve model
- **Percentage-of-royalties** — the platform takes a share instead of upfront fees; typical of partner tiers and the enterprise pole
- **Partner / label tier** — application or approval gated, dedicated account management, catalog management, playlist pitching, marketing services under agreement
- **Enterprise label distribution** — negotiated deals, custom statements, deep catalogs; the oldest form of the Type and still its top end
- **Full-service extensions** — the same platform adding physical distribution/manufacturing, publishing administration, sync, advances, video distribution
- **Regional specialists** — platforms built around specific markets' store networks and languages

## Related Application Types

| Application Type | Distinction |
|---|---|
| Music Streaming Platform | the consumer destination the distribution platform feeds; listening surface vs supply chain |
| Record Label Management | runs a label's business operations (roster, campaigns, releases planning); a distributor is the pipeline labels and artists *use* to reach stores |
| Music Publishing Management | administers compositions and songwriter royalties; the distribution platform handles recordings (masters), with songwriter data present only as delivery metadata |
| Royalty Management Platform | computes contractual royalties across catalogs and deals; the distributor's store statements are an input, not a substitute |
| Podcast Platform | similar deliver-to-directories shape for audio, but organized around shows/episodes without a per-store royalty pass-back loop |
| Content Distribution Platform | same provider→many-destinations shape for video channels/VOD; different object world |
| Digital Goods Store | sells directly to fans from the seller's own storefront; the distribution platform's defining move is placement on *third-party* storefronts |
| Music Promotion Platform | campaigns/audience growth; appears here only as an optional add-on service |

The closest structural sibling is Content Distribution Platform (video): both are provider-side supply chains to many consumer destinations. The medium's economics separate them — releases carry commercial identifiers and a money pass-back loop that the video Type realizes through channels and ad infrastructure instead.

## Representative Products

- TuneCore — self-serve, subscription/per-release pricing; artist-first pole
- CD Baby — one-time-fee self-serve; oldest independent distributor, with physical-era roots
- Symphonic Distribution — two-tier (DIY Starter / label Partner) bridge between poles
- The Orchard — enterprise label-side distribution within a major-label group

## Sources

Research date: **2026-09-08**

- TuneCore — official help center: Release Statuses; go-live timing; creating a release; switching distributors; takedown; renewal/removal — https://support.tunecore.com/hc/en-us (plus https://www.tunecore.com/)
- CD Baby — official help center: payouts; sales & accounting; post-delivery change rules — https://support.cdbaby.com/hc/en-us ; distribution partners list and product pages — https://cdbaby.com/
- Symphonic Distribution — official site and FAQ (plans, exclusivity, identifiers, payout terms) — https://symphonic.com/ , https://www.symphonic.com/faq/
- The Orchard — official site (positioning, client portal) — https://www.theorchard.com/

> Sourcing limitations: DistroKid's site did not respond during research and was omitted. The Orchard publishes no operational documentation publicly, so no workflow claims are drawn from it — it anchors only the enterprise pole. Symphonic's detailed knowledge base was unreachable; its operational claims come from its official FAQ. All store counts, prices, and payout figures observed during research are point-in-time facts and are deliberately kept out of the body of this document. Detailed evidence and per-product observations are in the paired Research Notes.
