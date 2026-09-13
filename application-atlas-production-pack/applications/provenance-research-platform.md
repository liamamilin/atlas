# Provenance Research Platform

## Overview

A **Provenance Research Platform** is software for reconstructing and documenting the history of ownership and custody of works of art: who held an object, when, how it moved between holders, and on what evidence each step rests.

The defining structure is small:

```text
Identified artwork record
└── Ownership/custody history as an ordered chain of events
    └── Each event binding agents (holders, transferors) to the object at a point in time
        └── Claims anchored to sources, with gaps and uncertainty explicitly represented
```

Everything else commonly associated with the field — typed transaction vocabularies, agent databases, transcribed sales-catalog corpora, network visualizations, publication surfaces — is widespread in current products but is not part of the defining core. The paper-era provenance line in a catalogue entry and the per-object research file satisfy the same structure without any software at all.

The purpose is verifiability. A provenance record is used for scholarship, acquisition decisions, due diligence, and restitution research — all contexts where an unverifiable claim is worthless and an honest gap is more valuable than a plausible guess.

## Users & Context

The primary user is a researcher investigating an object's history:

- **provenance researchers and curators** in museums — reconstructing ownership chains, often with particular attention to periods of unlawful transfer (war looting, forced sales, colonial contexts)
- **catalogue raisonné teams** — documenting each work's complete biography for scholarly publication
- **registrars and collections managers** — recording prior ownership at acquisition and maintaining the history on object records
- **due-diligence staff** at auction houses, dealers, and art services — reviewing ownership chains before a sale, loan, or purchase

Secondary users include scholars consulting published provenance databases, restitution bodies and claimants, collectors, and art lawyers. The work alternates between two modes: searching external evidence (auction catalogs, dealer stock books, archives) and recording findings against object records — with the internal/verified vs published distinction drawn explicitly.

## Core Model

### The Defining Core

```text
Identified artwork record
└── Ownership/custody history as an ordered chain of events
    └── Each event binding agents to the object at a point in time
        └── Claims anchored to sources, with gaps and uncertainty explicit
```

Three properties. If any one is removed, the product is no longer recognizable as provenance research:

- **Object-anchored history** — individually identified artworks are the anchor records, and the system documents the history *of those objects*. Without this, the product becomes a person database or a generic event log.
- **The event-structured chain** — the history is an ordered sequence of discrete events (acquisition, sale, gift, bequest, consignment, deposit, loan, looting…), each binding agents to the object at a point in time. Without this, the history is a static prose paragraph that cannot be extended, queried, or verified piece by piece.
- **Evidence-and-gap discipline** — events are anchored to sources (documents, catalogs, archives, publications), and incomplete knowledge is explicitly represented: unknown holders, uncertain attributions, gaps in the chain. Without this, the record is unsourced narrative and loses its research, commercial, and legal value.

### What Mature Products Add

- **Agent records** — collectors, dealers, auction houses, and institutions held as reusable identified records, with roles in each event; a dealer flag and a private-collection flag (which suppresses personal details and displays "private collection") are common agent properties.
- **Typed event vocabulary** — a controlled set of transaction types covering three conceptual classes: changes of ownership (sale, gift, bequest, inheritance), changes of possession (loan, deposit, storage, consignment — custody without title), and unlawful changes (looting, forced sale, seizure), with restitution and return semantics that repair the chain.
- **Source-document corpus** — transcribed and indexed sales catalogs, dealer stock books, archival inventories, and collector files that researchers search and cite as evidence for events.
- **Structured search** — keyword and faceted search over objects, agents, events, and sources, with date-range filtering.
- **Reports and publication** — per-object provenance reports; publication of research as catalogues raisonnés, open databases, or public web resources; a deliberate internal-vs-public distinction over unverified content.
- **Accumulation and correction** — records enriched and corrected over time; shared corpora carry correction workflows for incomplete or incorrect entries.
- **Exhibition and literature events** — documented alongside ownership as part of the object's history.

### One Structure, Many Implementations

```text
Concept:   Ownership/custody event
Forms:     typed event records with agent links (research platforms) ·
           event-based linked-open-data activities (shared corpora) ·
           date/person/place/details fields on the object record (collection systems)

Concept:   Evidence anchoring
Forms:     documents and media attached to events ·
           the transcribed source document as a first-class record ·
           institutional practice behind a prose field

Concept:   Uncertainty
Forms:     per-agent and per-event certainty flags ·
           "private collection" / "location unknown" conventions ·
           internal-only status for unverified content
```

## How It Works

### Record an ownership event

```text
Open the artwork record
→ select the event type (defines what must be filled in)
→ identify the source party (existing agent record or new; mark dealer / private collection as applicable)
→ identify the receiver, date, credit line, source reference
→ mark certainty (per-agent or per-event) where knowledge is incomplete
→ attach notes, source documents, media
→ save — the event joins the ordered chain on the object record
```

Possession events (loans, deposits, consignments) attach to the last known owner rather than breaking the chain. Unlawful events mark everything after them until a restitution or return event restores legitimate ownership — the chain itself encodes the legal narrative.

### Research from evidence

```text
Search the evidence corpus (sales catalogs, stock books, inventories, archives)
→ locate records mentioning the object, artist, or collector
→ transcribe or link the source
→ record the event it evidences against the object
→ leave what cannot be established explicitly open (unknown holder, uncertain attribution)
```

The gap is a first-class outcome: "location unknown" periods and "private collection" holders are recorded as such, because a documented gap directs future research and an invented link would poison the chain.

### Verify and publish

```text
Review the chain for gaps and inconsistencies
→ keep unverified content internal
→ publish verified content (report, catalogue entry, public database)
→ continue enriching as new evidence surfaces
```

Publication is continuous: mature platforms treat the provenance record as a living document that absorbs new discoveries after initial release.

### Core vs Common vs Optional

**Defining core** — without these, not provenance research:

- identified artwork records as the anchor
- ownership/custody history as an ordered event chain
- evidence anchoring with explicit gaps and uncertainty

**Common mature structure** — present in most current products:

- agent records with roles
- typed transaction vocabulary (ownership / possession / unlawful)
- source-document corpus
- structured search
- reports and publication surfaces
- correction workflows

**Variant / optional** — depends on segment and purpose:

- restitution-focused deployments (Nazi-era, colonial contexts)
- art-market analytics reuse of the same event data
- linked-open-data exposure (APIs, SPARQL, downloads)
- network-graph visualization of ownership relationships
- screening integration with stolen-art registries

## Interfaces

The following surfaces are described conceptually; exact layouts vary by product.

### Object / artwork record

The anchor surface.

- identification, images, signatures and markings, and the accumulated history: ownership events, exhibition references, literature
- primary actions: add an event, attach evidence, generate a report, compare internal vs public rendering

### Event entry form

The provenance-event surface.

- transaction type selector, source and receiver agent pickers, date, credit line, source reference, certainty controls
- primary actions: select agents, set certainty, attach notes/resources/media, save

### Agent directory

The people-and-organizations surface.

- collector, dealer, auction house, and institution records with roles and properties
- primary actions: create agent, link to events, mark dealer/private-collection status

### Evidence search

The corpus surface.

- search over transcribed catalogs, stock books, inventories, and collector files; filters by object, person, place, and date
- primary actions: search, view source records, link findings to objects and events

### Publication / report surface

The output surface.

- per-object provenance reports; published catalogues and databases with public/restricted access
- primary actions: generate reports, choose what to publish, update published content

## Important Rules / Behaviors

### Uncertainty is recorded, not smoothed over

Certainty is a documented property: an agent can be flagged questionable, an event can be marked as possible, and unverified content can be kept internal until research matures. The record's value depends on this honesty — a provenance chain that silently merges speculation with fact is worse than an incomplete one.

### Gaps are first-class content

Unknown holders and unlocatable periods are recorded as explicit chain elements ("private collection", "location unknown"), not omitted. A documented gap is a research finding and a due-diligence signal.

### Possession is not ownership

Custody events (loans, deposits, consignments, storage) are distinguished from ownership events throughout: a possessor is not an owner, and the chain structure keeps the distinction visible.

### Unlawful transfers change the chain's meaning

Events of looting, forced sale, or seizure alter the standing of everything after them; restitution and return events restore it. Products that support this encode it structurally, not just as text.

### The record is cumulative and corrigible

Provenance records accumulate over the object's life and are corrected as new evidence emerges; shared corpora expose correction channels for their users.

### Internal and public are different renderings

What the research team sees and what the public sees are deliberately separated; publishing unverified information is a decision, not a default.

## Variants

- **Dedicated research platform** — a working environment for research teams: record, extend, verify, and publish (catalogue raisonné projects, museum provenance departments).
- **Open shared corpus** — a public reference database of transcribed ownership evidence (sales catalogs, dealer stock books, archival inventories) that researchers search and cite; read-mostly, openly accessible.
- **Record-keeping realization** — provenance carried as structured fields on object records inside a collection management system; the minimal form, relying on institutional practice for the research discipline.
- **Restitution-focused research** — deployments organized around documenting unlawful transfers and supporting restitution claims; unlawful-event semantics become first-class.
- **Market-analytics reuse** — the same event data analyzed for art-market and collecting trends rather than object biography.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Museum Accession / Cataloging | adjacent, same records | the accession records the intake event into the collection (source, method, title); provenance research reconstructs the object's whole ownership history with evidence and uncertainty machinery the catalogue record does not carry |
| Museum Collections Management | container | owns the object register and custody accountability; provenance research is one documentation layer over (or beside) its records |
| Museum Condition Reporting | content sibling | condition documents physical state; provenance documents ownership history — both attach to object records, different content classes |
| Art Gallery Management | adjacent | the gallery's core is the commercial loop; provenance accumulates on its artwork records as archive, but no investigation apparatus is the product |
| Due Diligence Platform / stolen-art registry | consumer-side adjacent | screening checks an item against risk registries (stolen/lost/disputed); provenance research builds the history — due diligence consumes it |
| Digital Collection Portal | downstream | the portal publishes records governed elsewhere; provenance research produces the content such surfaces may publish |
| Auction Management System | different semantics for the same entity | auction systems execute sales; provenance research treats historical auctions as evidence for ownership events |
| Legal Research Platform | workflow consumer | restitution and title questions consume provenance findings; the object worlds (legal materials vs artworks) differ |

The boundary with Museum Accession/Cataloging is the most important one, because both operate on the same object records. The structural difference is record creation (the accession event and the catalogue record) versus investigation machinery (the reconstructed life history with its evidence and uncertainty apparatus).

## Representative Products

- **Navigating.art** — nonprofit platform for research teams creating digital catalogues raisonnés and archives, with a documented provenance-event subsystem (typed events, agents, certainty marking, publication).
- **Getty Provenance Index** — open access provenance data drawn from millions of archival records (dealer stock books, sales catalogs, archival inventories), provided as a linked-open-data research platform.
- **eHive** (Vernon Systems) — cloud collection management whose object records carry provenance as a field group on the Acquisition tab — the record-keeping realization.
- **Art Loss Register** — included as the boundary anchor: a due-diligence screening service (searching items against a stolen-art database), illustrating the consumer-side complement that is deliberately not part of this Type.

## Sources

Research date: **2026-09-10**

- Navigating.art — platform page: https://navigating.art/solution ; Help Center (Objects / Provenance events / Auctions): https://knowledge.navigating.art/en/ , https://knowledge.navigating.art/en/tutorial/how-to-add-provenance , https://knowledge.navigating.art/en/provenance-transaction-types
- Getty Provenance Index — overview and user guide: https://www.getty.edu/databases-tools-and-technologies/provenance/ , https://www.getty.edu/databases-tools-and-technologies/provenance/gpi-user-guide/
- eHive (Vernon Systems) — field help (Acquisition tab, Provenance fields): https://help.ehive.com/field-help/object/field-help.htm , https://help.ehive.com/acquisition-fields.htm , https://help.ehive.com/field-help/object/provenance-details.htm
- Art Loss Register — https://www.artloss.com/

> Sourcing limitation: operational documentation for enterprise collection systems (TMS Collections, MuseumPlus) is login-gated and was not accessible; their provenance realizations are known only at product-page level via prior sibling passes, and no screen-level claims are made for them. Registry/certificate products (Artory/Verisart-class) were not sampled. Vendor marketing figures (e.g., database sizes) are recorded as claims, not verified facts.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
