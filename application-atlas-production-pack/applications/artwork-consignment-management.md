# Artwork Consignment Management

## Overview

An **Artwork Consignment Management** application operates the consignment relationship between the owner of an artwork and the party authorized to sell or exhibit it on the owner's behalf. The owner — an artist, an estate, a collector, or another dealer — is the **consignor**; the gallery, dealer, or representative holding the work is the **consignee**. Ownership stays with the consignor throughout; the consignee earns a recorded share when a work sells and must account for every work placed, sold, or returned.

The defining core is small:

```text
Consignor (retains title to the work)
└── Consignee (authorized to sell or exhibit on the owner's behalf)
    └── Specific works placed under consignment (tracked one by one)
        └── Recorded terms of the placement
            (commission/split, duration, return basis)
        └── Per-work disposition state
            (placed → on consignment → sold or returned)
```

Everything else commonly associated with these products — generated agreements, settlement statements, connected artist portals, check-in/check-out, reporting — is standard equipment in mature implementations but not what makes the category what it is.

A note on how the market packages this: in the researched sample, consignment management is almost always delivered as a module inside a gallery's operating system (on the consignee side) and inside artist studio tools (on the consignor side), with the two sides sometimes linked by connected accounts. No major standalone product dedicated solely to artwork consignment was found in reachable official sources. The structure described here is the consignment-centered core that those modules implement; see Related Application Types for the packaging boundary.

## Users & Context

The software serves two sides of one commercial relationship, and who sits in front of it depends on the deployment:

**Consignee side (gallery / dealer / representative):**

- **Gallery director / owner** — sets consignment terms and commission percentages, approves what comes in and goes out, oversees what is owed.
- **Gallery manager / registrar** — creates consignment lists, receives and accepts incoming consignments, tracks where each consigned work physically is, processes returns.
- **Bookkeeper / studio manager** — computes and tracks amounts due to consignors, produces statements and consignment reports, reconciles payments.

**Consignor side (artist / estate / collector):**

- **Artist** — sends works to representing galleries, tracks where each piece is and when it is due back, watches for sale notifications and payments.
- **Estate or collection manager** — places works with dealers or auction-side sellers on behalf of an owner, monitors disposition and settlement.

Typical context: a primary-market gallery living on consigned stock from artist studios; a secondary-market dealer taking works on consignment from collectors and estates; an artist working with several galleries at once who needs one place to see all placed works. The work is high-value, unique, and physically mobile, so custody and documentation matter as much as the money.

## Core Model

### The Defining Core

**Consignor.** The party who owns the work and retains title until a sale. A consignor is a tracked record — usually an artist, but also an estate, a collector, or another dealer — and carries the relationship context: default consignment terms, works placed, amounts owed. The consignor is the counterparty the system ultimately accounts to.

**Consignee.** The party authorized to sell or exhibit the work. In gallery-side deployments the consignee is the operator of the system; in consignor-side deployments the consignee is an external party whose sales and returns must be recorded and, in some products, coordinated through a connected account.

**Consigned work.** Consignment is tracked per specific physical work — one record per piece, never per interchangeable stock item. The consigned item carries its attribution and identity (artist, title, medium, dimensions, edition where applicable), its imagery, its price, and its consignment state. Because works are unique, the consignment record is item-level: which exact piece, from which consignor, under which terms, currently where.

**Consignment record.** The placement itself is a managed object: a consignment list or record that binds a set of works to a consignor (incoming) or recipient (outgoing), with a title, optional start and end dates, the commercial terms, and the itemized works. The terms are the commercial substance of the record — commission percentages or splits, duration, and the conditions under which works come back. Mature implementations store default terms per consignor and allow per-work overrides.

**Disposition state.** Every consigned work moves through a tracked state:

```text
Placed / sent
  → accepted & received
  → on consignment (at a named location)
  → sold   (attributed to a specific sale)
  or returned   (recorded back to the consignor)
```

The two terminal dispositions — sold or returned — are what the whole structure exists to reach and record. A work that sells generates the consignor's share; a work that comes back re-enters the consignor's holdings.

### Settlement

What distinguishes consignment tracking from plain custody tracking is the money. When a consigned work sells, the sale must be attributed back to the consignment, and the system must be able to answer: what is now owed to the consignor? Mature implementations compute amounts due from recorded invoice history, track payments due versus paid, and produce statements or payables reports for the consignor. The exact split arithmetic (formulas, tax treatment, payment timing) varies by product and by agreement; the obligation to track and settle the consignor's share does not.

### Standard Capabilities

Mature implementations commonly add:

- **Consignment agreements as documents** — the record can be exported or printed as a formal agreement, sent to the other party, and in some products formally accepted before works move.
- **Check-in / check-out and location tracking** — consigned works carry a location (gallery floor, storage, studio, fair, third-party venue) and a movement history; "where is this work and on what basis do we hold it" is answerable at any moment.
- **Third-party (onward) consignment** — a holding gallery re-consigns works to another gallery or representative on the artist's behalf; the chain of placement remains tracked.
- **Returns management** — return lists with return terms, return forms sent to the consignor, and the work's state moving back to the consignor's holdings.
- **Connected consignor accounts or submission portals** — artists initiate consignments from their side, consignees review and accept or decline; sale and return events propagate as notifications and status changes.
- **Consignment reporting** — shareable reports of what is out, what sold, what was returned, and what is owed, often with control over which columns the consignor sees.

## How It Works

### Placing works on consignment (consign-in)

```text
Select works (from the consignor or from inventory attributed to them)
→ create a consignment record (title, dates, consignor, terms)
→ terms populate from the consignor's defaults; adjust per work if needed
→ send the consignment to the other party to accept (in connected setups)
→ works are received; each becomes (or updates) a tracked record
→ each work's state: on consignment, at a named location
```

In connected-account products the consignor initiates this from their own account and the consignee accepts or declines; in single-sided products the consignee records the placement directly. Either way, the acceptance moment is recorded and the works become item-level consigned records.

### Selling a consigned work

```text
Consigned work is placed on a sale/invoice
→ invoice is closed
→ the sale is attributed to the consignment and the consignor
→ the consignor is notified (in connected setups) and the work's
  consignor-side state changes to sold
→ the consignor's share becomes an amount due
→ payment is recorded; statement reflects due vs paid
```

The sale closes the work's consignment state and opens a settlement obligation. This chain — consignment to invoicing to statement — is the financial spine of the category.

### Returning a consigned work

```text
Select the consigned works coming back
→ create a return record (return terms; defaults configurable)
→ send the return form to the consignor
→ the work's state moves to returned / back with the consignor
```

Returns are first-class recorded events, not silent deletions: the record shows that the work went out and came back, which is what keeps the consignor's account trustworthy.

### Onward placement (third-party consignment)

A gallery holding consigned stock may place works with another gallery or representative on the artist's behalf. The works' location changes to "on consignment" at the new party, the recipient and terms are recorded, and the original consignment chain remains visible. The consignor's relationship is with the chain, not just the first holder.

### The settlement loop

Across all of the above, the recurring operational loop is: **works out → works sold or returned → amounts due computed from sales → payments recorded → statements shared**. A gallery director can answer, per consignor: what of theirs do we hold, where, what sold, what did we pay, what do we still owe.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Consignment dashboard / lists

The operator's primary consignment surface.

- lists consignment records (incoming, outgoing/third-party, returns) with dates, parties, and status
- primary actions: create a consignment (inbound / third-party / return), open a record, send for acceptance, export or print the agreement

### Consignment record

The placement itself.

- overview: title, start/end dates, consignor or recipient, terms
- itemized works: each with identity, price, and consignment state
- primary actions: add works, adjust terms, send to the other party, produce the agreement document

### Consigned-work record

The item-level view inside the inventory.

- attribution, imagery, price, consignment state, current location, movement history, linked consignment and sale records
- primary actions: update location, place on hold, attach to a sale, include in a return

### Consignor (artist/estate) record

The relationship side.

- profile and contact details, default consignment terms, works currently placed, payments due and paid
- primary actions: set default terms, review placed works, record or review payments, share reports

### Settlement / reporting surface

- consignment reports (what is out, sold, returned), payables or statements (amounts due to consignors, due vs paid), commission and split views
- primary actions: generate for a period or consignor, adjust shared columns, export or email to the consignor

### Connected consignor portal (where present)

The consignor's own view.

- their works and where each one is ("on consignment to …"), sale and return notifications, submitted consignments and their acceptance status
- primary actions: send a consignment, review status, view statements

## Important Rules / Behaviors

### Ownership never transfers until a sale

The consignor retains title throughout the placement. The system's records are built on this: works on consignment remain the consignor's property, appear in their holdings, and only leave them through a recorded sale or return. This is the structural difference between consignment and purchase.

### Acceptance is a recorded gate

In connected setups, an incoming consignment is a proposal until the receiving party accepts; acceptance creates the item-level records on the consignee side. Accepted consignments typically cannot simply be deleted — the placement is part of the record.

### The two sides may see the same work differently

Where consignor and consignee each keep their own records of the same work, the views deliberately diverge: the consignor's copy shows the work as "on consignment to [gallery]", the consignee's copy shows it as held stock; numbering and dates can differ per side; edits on one side do not automatically propagate to the other. Coordination of consigned-work details is partly procedural, not fully synchronized.

### Sale attribution changes the consignor's state

When a consigned work is invoiced and the sale closed, the consignor's record of that work flips to sold — attributed to the selling party — and the consignor's amount-due grows. The invoice, not the handshake, is the trigger.

### Returns are events, not reversals

A return is recorded as its own consignment-type event with its own terms and form. In some connected products the return must be recorded on the holding side and communicated, rather than automatically restoring the work in the consignor's account.

### Terms are defaults with overrides

Commission percentages, durations, and return conditions are commonly stored as defaults per consignor and applied automatically to new consignments, with per-work or per-consignment overrides. This keeps terms consistent without making them rigid.

### Status coordination is not always enforced

Some products do not block a consignor from sending a work already marked sold, or a holding party from recording events out of order; the systems track states but rely on the parties communicating about discrepancies. Consignment software records the relationship; it does not replace the trust and communication underneath it.

## Variants

- **Consignee-side module** — the dominant form: consignment management as one capability inside a gallery's operating system, alongside inventory, clients, and direct sales. The gallery runs the consignment world for its artists and estates.
- **Consignor-side studio tool** — the same structure operated by artists: works placed out to multiple galleries, tracked from the owner's side ("where is each piece, when is it due back, what sold, what am I owed").
- **Connected two-sided deployment** — consignor and consignee accounts linked in one product family; consignments, notifications, and status changes flow between them.
- **Auction-adjacent consignment** — auction houses run a lot-based variant of consignor relations (intake, estimates, reserves, hammer-price settlement); the mechanics differ enough that it is treated as a neighboring structure, not a variant of this one.
- **General-resale consignment** — retail consignment of interchangeable goods shares the ownership-retaining concept but replaces unique-work tracking with SKU-style inventory and POS-integrated payouts; a different Application Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Art Gallery Management | parent suite in the current market | centers the gallery's full world — artwork inventory, custody, clients, and the sale loop; consignment is one module inside it. Strip the inventory, clients, and direct sales, keeping only the consignor↔consignee relationship, and what remains is this Type |
| Consignment Management Platform (resale) | shares the consignment concept | operates interchangeable retail goods with consignor accounts and POS-integrated payouts; artwork consignment operates unique works with agreements, custody, sale attribution, and consignor-share settlement |
| Museum Loan Management | custody without commerce | tracks specific objects at external locations like consignment does, but carries no commercial terms, no sale disposition, and no settlement |
| Auction Management System | adjacent consignor relations | lot-based intake, estimates, reserves, and hammer mechanics; consignment here is fixed-price placement with a commission split |
| Artist Studio Management | consignor-side sibling | centers production and portfolio with consignment-out as one capability; this Type centers the consignment relationship itself |
| Customer Relationship Management / CRM | component relationship | consignor records are relationship records, but the center is the consignment — works, terms, disposition, settlement — not a sales pipeline |

The most important boundary is with Art Gallery Management, because that is how the market actually packages this capability: in the researched sample, every consignment implementation lives inside a gallery or artist suite. This leaf documents the consignment-centered structure those implementations share; whether it warrants a fully independent Type is a packaging question flagged for joint review.

## Representative Products

- **Artlogic** — UK platform for galleries and artists; consignment tracked as a basis layer over owned stock (terms, owners, locations, movement history), with a documented consignment-to-invoicing-to-statement chain and due-consignor reporting.
- **ArtCloud** — US gallery and artist platform with connected artist accounts; consignment lists (inbound, third-party, returns), accept/decline flows, sale attribution with consignor notifications, and consignment-payment reporting.
- **Art Galleria** — AU/global art-inventory platform for galleries and artists; consignment check-in/check-out, professional consignment reports, and artist submission portals.

An independent artist-side consignment tracker (Artwork Archive) could not be reached during research and is not characterized here.

## Sources

Research date: **2026-09-06**

- ArtCloud Knowledge Base — https://help.artcloud.com/knowledge — sections: Manager–Inventory (Consignment), Manager–Artists (Consignment, Payments), Analytics (Artist/Consigner Payments, Commission), ArtCloud for Artists (Gallery Connections and Consignments); articles: "How to Create a Consignment List", "Receive and Manage Artist Consignments", "Send a Gallery Consignment"
- ArtCloud — https://artcloud.com/manager-for-artists ; https://artcloud.com/consignment-reports
- Artlogic Support — "How to Create Artist Payables Documents from Advanced Reports" — https://support.artlogic.net/hc/en-gb/articles/15406651760028
- Artlogic — https://www.artlogic.net/products/artist/management
- Art Galleria — https://www.artgalleria.com/for-galleries ; https://www.artgalleria.com/for-artists

> Sourcing limitations: Artwork Archive (www.artworkarchive.com) returned access errors on two attempts and was abandoned; search-engine discovery was unusable (one timeout, one region-polluted result set). No standalone dedicated artwork-consignment product was identified through reachable official sources — the sampled market implements this capability inside gallery and artist suites. Settlement arithmetic (split formulas, tax treatment, payment timing) is not stated at formula level in any sampled source and is deliberately kept qualitative in this document. Detailed evidence, cross-product comparison, and the packaging-boundary analysis are recorded in the paired Research Notes.
