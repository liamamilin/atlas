# Performing Rights Management

## Overview

A **Performing Rights Management** application is the collective-administration system of a performing rights organization — the society (PRO/CMO) that stands between music users and rights holders. It keeps the registry of the works or recordings the society represents, attributes observed and reported public performances to the rights holders behind them, and runs the loop that licenses music users, collects licence fees, and distributes them as royalties under published rules.

The defining structure is small:

```text
Rights holders (writers / publishers / artists / owners)
└── Represented repertoire of record
    │     (works or recordings, with shares — administered, not owned)
    ├── Usage-to-rights-holder attribution chain
    │     (census or sample evidence → matched to the registry → attributed per shares)
    └── Collective licensing-and-distribution loop
          (license music users → collect fees → deduct costs → distribute royalties)
```

Everything else commonly associated with societies — member portals, licensee portals, fingerprinting monitoring, cue sheets, setlist programs, international reciprocity, public repertory search — is standard equipment of mature implementations, not what makes the system a performing rights management system. A century-old society running on paper membership cards, broadcaster cue sheets, sample logbooks, and clerk-calculated distributions satisfies the same definition.

When the subject narrows to one rights owner's own catalog and contracts, the product is a different Application Type (Music Publishing Management). When the money loop disappears and only the data remains, it is a registry or a monitoring service, not this Type.

## Users & Context

The operator of the system is a **collective rights organization** — a performing rights organization (PRO) for compositions, a sound-recording performance society, or a combined society. Its staff are the primary users:

- **member services** — bring rights holders into the system, maintain their records, answer payment questions
- **licensing teams** — sell and administer licences to music users, from national broadcasters to individual venues
- **royalty processing / distribution teams** — run the usage-to-payment pipeline each cycle
- **matching / research teams** — resolve usage that does not automatically match the registry

Two external populations use the system's public faces:

- **rights holders** (songwriters, composers, publishers; recording artists and sound recording owners) — register or claim their repertoire, submit usage evidence such as setlists, and read statements
- **music users / licensees** (broadcasters, streaming services, venues, hotels, restaurants, colleges, background-music services, fitness brands, websites) — obtain licences, report usage, and pay

The work environment is cyclical: licences and usage reports arrive continuously; distributions go out on a fixed rhythm (commonly monthly or quarterly). The system is the organization's system of record — its registry, its money, and its evidence of who performed what all live here.

## Core Model

### The Defining Core

Three structures, jointly held. Remove any one and the product stops being a performing rights management system.

**1. The represented repertoire of record.** A persistent registry of the works or sound recordings the society represents, each carrying its identified rights holders and their shares. The registry is built from the rights holders' own acts: writers and publishers join as members and register their works; recording artists and owners register and then claim their recordings in the society's database. The society **administers** these rights under membership, affiliation, or statutory designation — it does not own them. This is what makes the registry a *representation* record rather than a catalog: the same work can be represented by different societies in different territories, and the society's authority over it is delegated, bounded, and revocable.

**2. The usage-to-rights-holder attribution chain.** The society gathers evidence that its repertoire was publicly performed, broadcast, or streamed — from radio and TV station reports, digital service usage files, fingerprinting-based monitoring, background-music playlist reports, member-submitted setlists, and cue sheets for audio-visual uses. This evidence is matched against the registry so that each performance becomes an attributed event: this work, these writers and publishers (or this recording, these performers and owners), these shares. Usage that cannot be matched is handled as a first-class class of its own — routed to research teams or held in identifiable unclaimed pools — rather than silently dropped, because unmatched usage is unpaid money owed to someone.

**3. The collective licensing-and-distribution loop.** The society licenses music users to perform the whole repertoire — most commonly through blanket licences (one fee, any work in the repertory), sometimes per-program or per-use schemes, and in some jurisdictions by administering a statutory or compulsory licence whose rates are set by a public body rather than negotiated. The money collected is held per source, administration costs are deducted, and the remainder is distributed to rights holders as recurring royalties, calculated under **published distribution rules**. The loop closes back into the registry: every distribution is an attribution chain executed in money.

### Standard Capabilities

Mature implementations commonly add:

- **Member / rights-holder portal** — join and register, register works or claim recordings, maintain payment and tax details, designate users or redirect shares, read statements.
- **Licensee surfaces** — a licensing site with licence finders and rate schedules, plus licensee portals for reporting usage and paying; some societies run separate portals per licensee segment (broadcast, digital, general business).
- **Public repertory search** — a searchable database of the represented works or recordings, used by licensees, researchers, and the societies themselves.
- **Census-and-sample survey machinery** — per medium, a documented choice between counting every performance (where data is cheap) and sampling (where it is not), with the census share expanding as capture technology gets cheaper.
- **Cue-sheet and setlist intake** — structured submission surfaces for audio-visual usage and live performance.
- **Statement generation** — per-cycle royalty statements showing where and when music was used and what it earned.
- **International reciprocity** — machinery for collecting on behalf of affiliated societies' repertoire used in the home territory, and for distributing foreign collections to members.
- **Special programs** — awards, top-tour surveys, and other distributions layered on top of the usage data.

### One Structure, Many Implementations

The core is written conceptually. Implementations vary along three axes:

```text
Concept:   Represented repertoire
Realized:  member-registered works with writer/publisher shares
           OR claimed sound recordings with performer/owner shares
           OR both under one organization

Concept:   Usage evidence
Realized:  station reports, DSP usage files, fingerprinting monitoring,
           background-music playlist reports, member setlists, cue sheets

Concept:   Licensing mode
Realized:  negotiated blanket / per-program licences
           OR statutory / compulsory licence administration
```

A reader who has only seen one implementation — say, a composition society with blanket licences and fingerprinting — should still recognize a statutory sound-recording collector, or a paper-era society, from the core model.

## How It Works

### The collective loop

The main workflow runs continuously and settles on a distribution rhythm:

```text
Rights holders join and register works / claim recordings
→ music users obtain licences (blanket, per-program, or statutory)
→ usage evidence arrives (reports, usage files, monitoring, setlists, cue sheets)
→ evidence is matched to the registry (automatically, then by researchers)
→ royalties are calculated under the published distribution rules
→ statements are issued and royalties paid to rights holders
  (and to / from affiliated societies for foreign uses)
```

Each cycle repeats. Registration and claiming never stop; licensing never stops; usage arrives continuously; distributions recur.

### The statutory variant

Where the licence is statutory, the licensing leg changes shape but not substance: the society does not negotiate with licensees. Services that qualify for the statutory licence calculate their own obligation at the publicly set rates, certify it, and submit payment together with the usage data covering their performances. The society's job becomes verification, attribution, and distribution. The attribution chain and the distribution loop are identical to the negotiated case.

### The claim flow (recording side)

On the recording side, repertoire can enter the system before the rights holder does: usage reported by services may put recordings into the society's database first, and the rights holder then registers, searches the database, and **claims** their recordings. Royalties for claimed recordings flow from the next distribution, and historically unclaimed money is held in searchable unclaimed pools. Rights holders can also redirect a share of their royalties to collaborators (producers, mixers, engineers) by instruction.

### The live-performance flow

Members submit setlists — which songs were performed, at which venues — through a portal or app. Some societies explicitly ask submitters to include cover songs, so the performance attributes to the original writers. This member-reported evidence feeds the same matching and calculation machinery as broadcaster and service data.

### The reciprocity flow

Societies represent each other: an affiliate's repertoire used in the home territory is collected by the home society and forwarded; members' foreign performances are collected by the foreign society and returned. Each society's system therefore runs the same loop for two repertoires — its own members' works abroad, and foreign members' works at home.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by organization.

### Member / rights-holder portal

The rights holder's primary surface.

- registration and profile, payment and tax details, designated users
- works registration (composition side) or recording search-and-claim (recording side)
- setlist submission, agreements, statements
- primary actions: register, claim, submit usage evidence, read statements, update payment details

### Licensee portal / licensing site

The music user's surface, often split by licensee segment.

- licence finders and rate schedules; licence purchase and renewal
- usage reporting and payment submission (statutory licensees typically calculate and certify their own obligation)
- primary actions: find a licence, report usage, pay, manage account

### Public repertory search

A searchable registry of represented works or recordings.

- title, writers/publishers or performers/owners, shares and affiliations
- used by licensees clearing music, by researchers, and by other societies

### Statements

The rights holder's money view.

- per-period earnings by source and by work or recording, with payment status
- the visible output of the entire attribution chain

### Internal operations surfaces

Matching queues, research worklists, distribution calculation, and finance reconciliation run the society's back office. These are the least publicly documented surfaces; their existence and function are evident from the societies' own process descriptions, but their detailed layouts are not part of the public record.

## Important Rules / Behaviors

### The society administers, does not own

Every entitlement in the registry is delegated by a rights holder (or conferred by statute). Membership and representation agreements bound the society's authority; rights holders can typically direct shares, redirect payments, and, in some structures, exit. The system's records must therefore always distinguish the work from the society's claim on it.

### Money is pooled per source

Distributions follow the source of the money: fees collected from broadcasters are distributed against broadcast usage, streaming fees against streaming usage, and so on. A society does not blend all revenue into one pot and pay out by global popularity; each licensee class's money is distributed against that class's usage.

### Census versus sample is an explicit economic trade-off

Societies publish which media are counted completely and which are sampled, and state the policy behind it: count everything where capture is cost-effective, sample where it is not, and expand the census as technology gets cheaper. Sampled media still pay — the sample's results are projected — but the completeness of attribution varies by medium, and members are told this.

### Unmatched usage is a managed class

Usage that does not match the registry is not discarded. It is routed to research teams for manual matching, or held in identifiable unclaimed pools that rights holders can search and claim. The registry's completeness directly determines how much money reaches rights holders, which is why claiming one's recordings or registering one's works is repeatedly emphasized to rights holders.

### Distribution rules are published and binding

Calculation is governed by published rules — formulas, weightings, per-medium pools — not by ad-hoc decisions. This is a governance requirement of collective administration: members are paid by rule, and the rules are inspectable.

### Shares distinguish writers and publishers (or performers and owners)

The registry carries the split of each work or recording among its entitled parties, and distributions respect it. On the composition side this commonly means a writer share and a publisher share; on the recording side, featured performers and rights owners. Some societies pay writer shares directly to writers regardless of publishing arrangements; mechanics vary by territory and affiliation type.

### Reciprocity is structural, not optional

A society's system routinely handles repertoire it does not originate — foreign affiliates' works performed locally — and forwards money outward on the same logic. The attribution chain and distribution rules apply to both directions.

## Variants

- **Composition-side PRO** — performing rights in musical works; membership of writers and publishers; blanket licensing of venues, broadcasters, and digital services.
- **Sound-recording / performer side** — digital performance and neighboring rights in recordings; registration-and-claim of recordings; statutory collection in some jurisdictions; performer and owner shares.
- **Combined society** — performing rights and mechanical/reproduction rights administered under one roof, with parallel portals and rules.
- **Negotiated vs statutory licensing** — the same loop with the licensing leg realized as sales (blanket/per-program schemes) or as administration of a compulsory licence with externally set rates.
- **Census-heavy vs sample-heavy operations** — the same survey machinery with different completeness per medium, driven by data economics.
- **Society-operated vs shared machinery** — some functions are bought or shared: fingerprinting monitoring and usage processing from specialist vendors, joint licensing initiatives with other bodies (including the sound-recording side), and cross-society data platforms that reconcile ownership shares across repertoires.
- **Production music and special schemes** — dedicated licence classes and portals for production-music users, education, events, and background-music services.

A variant remains a variant unless it changes the core: a monitoring vendor or a shared registry serves the Type but is not it; a rights-owner-side catalog system is a different Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Music Publishing Management | rights-owner side: one publisher's catalog, its contracts, and its receipts from many pay sources (the society is one of those sources); this Type is the society side: the market-wide repertoire and the collective loop |
| Royalty Management Platform | generic contractual royalty computation over licensees and products; this Type's calculation is collective usage attribution under published distribution rules, not contract-term computation |
| Media Rights Management | grant-of-record lifecycle — who may use what, when, where — as the center; this Type's center is the money loop fed by usage attribution |
| Music Distribution Platform | delivers recordings to stores and returns earnings through the supply chain; society collection (statutory performance royalties) deliberately sits outside that earnings loop |
| Record Label Management | label business operations (roster, campaigns, releases); no collective licensing or society distribution machinery |
| Music Promotion Platform | pitches recordings to curators for exposure; no registry, licensing, or distribution loop |

The most important boundary is with **Music Publishing Management**: the two share vocabulary (works, shares, royalties, societies) and meet in real money flows — the society appears in the publisher's income loop as a pay source, and the publisher appears in the society's registry as a member. The structural test is whose catalog the system centers: one owner's, or the market's.

## Representative Products

- **ASCAP** — US composition-side PRO; blanket and per-program licensing; documented census/sample survey system and matching platform; member and licensee portals; co-founder of the Songview cross-society data platform.
- **SoundExchange** — US sound-recording digital performance society; statutory-license collector; registration-and-claim model with unclaimed pools; licensee portal for self-calculated, certified submissions.
- **APRA AMCOS** — Australian/NZ combined society (performing + mechanical rights); published five-step distribution process and data-source taxonomy; reciprocal administration for affiliated societies; joint public-performance licensing initiative with the recording side.
- **BMAT** — specialist vendor (not a society) supplying fingerprinting monitoring, digital usage processing, and claim-conflict resolution to societies; included to show that the observation layer is a bought capability, not the Type itself.

The registry-without-money-loop boundary was checked against **Songview** (a joint ASCAP/BMI copyright data platform), which reconciles ownership shares across repertoires but performs no licensing, collection, or distribution.

## Sources

Research date: **2026-09-09**

- ASCAP — https://www.ascap.com/about ; https://www.ascap.com/help/royalties-and-payment/payment (and its who-collects and surveys pages) ; https://www.ascap.com/songview
- SoundExchange — https://www.soundexchange.com/about/ ; https://www.soundexchange.com/what-we-do/for-digital-service-providers/ ; https://www.soundexchange.com/what-we-do/for-artists-labels-and-producers/
- APRA AMCOS — https://www.apraamcos.com.au/ ; https://www.apraamcos.com.au/music-creators/membership-explained/distribution-overview ; https://www.apraamcos.com.au/music-licences/music-licensing-explained/where-does-my-money-go
- BMAT — https://www.bmat.com/ ; https://www.bmat.com/cmo/

> Sourcing limitation: multi-society service providers (ICE-class) and several European societies (PRS for Music-class) could not be reached from the research environment on 2026-09-09 (timeouts; script-blocked or erroring help portals). The shared/outsourced-machinery variant is therefore described at lineage strength, and European-society specifics are not asserted. Precise operational figures published by the organizations (payout ratios, member and licensee counts, catalogue sizes) are treated as product-specific claims and are deliberately not stated in this document; they are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical market-sample check are recorded in the paired Research Notes.
