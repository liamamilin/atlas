# Election Results Management

## Overview

An **Election Results Management** system is the election authority's counting-side system of record. It collects the vote totals produced by whatever counted the ballots, holds them as contest-scoped results attached to reporting units, accumulates them into jurisdiction-wide outcomes, reconciles them against ballot accounting, moves them toward a final official standing, and reports them outward — to canvass bodies, to higher election authorities, and to the public.

The defining structure is small:

```text
Results intake from the counting process
└── Contest-scoped result records tied to reporting units
    └── Aggregation into jurisdiction-wide outcomes
        └── Progression to a final / official standing
            └── Outward reporting (canvass · higher authority · public)
```

Everything commonly associated with modern products — ballot imaging, contest-by-contest adjudication queues, interactive public election-night sites, independent audit retabulation — is widespread in current products but is not what makes the system what it is. A paper-era office aggregating precinct tally sheets into a canvass abstract, and a national electoral body consolidating transmitted tallies into a declared national count, both sit inside the same definition.

The boundary against its neighbors is sharp. The system does not define the election or produce ballots — an upstream **Election Management System** does that, and ends where tabulation begins. It does not maintain the list of eligible voters — that is the **Voter Registration System**. Election Results Management takes over once votes have been cast and counted, and its job is complete when the outcome is official and public.

## Users & Context

The primary user is the election office that conducts the count — in decentralized systems a county or municipal election department; in centralized systems a state or national electoral body. The work context is the days surrounding the close of voting: receiving materials from the field, processing them under observer scrutiny, and publishing totals that will withstand legal and public examination.

Typical roles around the system:

- **scanning / intake staff** — feed ballots through central-count scanners or upload results media; in many products this role is deliberately separated from counting
- **adjudication staff** — resolve voter-intent questions on machine-read ballots, contest by contest, with every decision recorded
- **election-office staff** — watch accumulating totals, reconcile ballot counts, produce canvass and certification reports
- **audit staff** — run or support post-election verification, recounts, and independent retabulation

Secondary users sit outside the office: higher election authorities that receive standardized result exports, candidates and party observers who watch the process, and the public and news media who follow election-night reporting.

## Core Model

### The Defining Core

Three structures. If any one is removed, the system stops being recognizable as results management:

- **Contest-scoped result records tied to reporting units** — results exist as vote accumulations organized by contest (an office or a ballot question) and choice (candidate or option), within reporting units of the election: precincts, districts, polling locations, or counting batches. The managed unit is the result — never the ballot (that belongs to election and ballot production) and never the voter (that belongs to the roll).
- **Intake from the counting process** — results enter from whatever performed the count: memory media carried in from counting devices, central-count scanning of paper ballots, electronic transmission from the field, or manual entry of tallies. The system consumes the output of casting and counting; it never manufactures results from definitions.
- **Aggregation to official outcomes with outward reporting** — unit-level results roll up into jurisdiction-wide totals, progress toward a final official standing, and are reported outward: canvass-facing reports, standardized exports to higher election authority, and public election-night reporting.

### Standard Capabilities of Mature Products

These capabilities are common in current products and make the system practical, but they are not what defines the Type:

- **Batch-managed central counting** — ballots are processed as batches; multiple ballot styles and languages can run through one batch; scanning workstations can be networked to a central server.
- **Adjudication workflow** — ambiguous or questionable marks on scanned ballots are routed to contest-by-contest resolution queues with clear flags; scanning and adjudication can run as separate workstations and roles; every resolution decision is logged and attributable.
- **Scan/tabulation separation** — ballots can be scanned long before counting begins, without producing totals; tabulation is a separate, controlled step.
- **Reconciliation / ballot accounting** — ballots cast, ballots counted, and votes per contest are compared so totals can be explained against the ballot inventory.
- **Results reporting and exports** — reports are produced as results accumulate, and results can be exported into standardized formats for reporting to the state or higher authority.
- **Public election-night reporting** — a public-facing display of results, structured by contest and reporting unit, available on most devices.
- **Audit logging and role-based controls** — actions across the results workflow are recorded and permission-scoped, consistent with the high-integrity nature of the domain.
- **Ballot-image capture and inspection** — scanned ballots become inspectable images with filters that locate questionable marks; plain-language notes show how each selection was recorded.
- **Post-election audit and verification support** — independent retabulation of ballots or ballot images, results comparison against the certified count, and threshold reporting.
- **Recount support** — re-examination of specific contests or ballots, including targeted recounts.
- **Multi-election history** — results from past elections remain held and distinguishable.

### One Structure, Many Implementations

The core model is written conceptually; specific products realize each concept differently:

```text
Concept:   Intake from the counting process
Realized as:  memory media from counting devices, central-count scan batches,
              electronic transmission, manual entry of tally sheets

Concept:   Reporting unit
Realized as:  precinct, district, polling location, scanning batch,
              tally sheet (paper-era)

Concept:   Outward reporting
Realized as:  canvass reports, standardized state-export files,
              interactive public election-night sites, published audit dashboards
```

A reader who has only seen a modern image-based central-count product should still be able to recognize a media-upload accumulator or a manually fed results consolidation from the same core model.

## How It Works

### Receive results from the counting process

```text
Voting closes (or by-mail ballots arrive continuously)
→ results arrive as batches, media, transmissions, or entered tallies
→ intake is recorded (which unit, which batch, which source)
→ results become inspectable records in the system
```

In central-count products, batches are the operational unit: a batch may mix precinct styles and languages, and scanning staff need not be the same people as adjudication staff.

### Accumulate and tabulate

```text
Batches are tabulated
→ votes accumulate per contest and per reporting unit
→ running totals become visible as results are accumulated
→ aggregation across units produces jurisdiction-wide standings
```

Scanning and tabulation are deliberately separable in mature products: capture can proceed without producing countable totals, which lets offices spread the physical work of scanning across days while keeping the release of totals under control.

### Resolve voter intent on machine-read ballots

```text
Scanner or analysis flags a questionable mark (outside the target area, marginal mark, write-in)
→ ballot enters an adjudication queue for that contest
→ an authorized staff member resolves the voter's intent
→ the decision is recorded with a complete log entry
→ totals update
```

Adjudication is contest-by-contest work with color-coded or otherwise explicit flags, and the system keeps a full record of every resolution decision — end-to-end transparency is a selling point in this domain for good reason.

### Reconcile

```text
Ballots received / cast are compared against ballots counted
→ votes per contest are compared against ballot inventory
→ discrepancies are investigated before totals are treated as final
```

Reconciliation is the discipline that makes results credible: the count must be explainable against the physical ballot record. Some products also support independent retabulation — re-counting ballots or ballot images through a separate system and comparing the outcome against the certified count.

### Move from unofficial totals to the official outcome

```text
Early totals are published as unofficial
→ the jurisdiction's canvass process reviews and confirms totals
→ the outcome reaches its official / certified standing
→ official results are the basis for final publication and any recounts or contests
```

The exact legal machinery of canvass and certification varies by jurisdiction; what the system consistently provides is the managed progression of results from early provisional totals toward the final official standing, with the documentation that process requires.

### Report outward

```text
Internal reports for canvass and audit purposes
→ standardized exports in the formats required by the higher election authority
→ public election-night reporting as results accumulate
→ published audit or verification results where offered
```

Outward reporting runs in two directions with different audiences and different finality: upward, standardized and official; public, fast and clearly provisional until made official.

### Core vs Standard vs Optional

**Defining core** — without these, not results management:

- contest-scoped result records tied to reporting units
- intake from the counting process
- aggregation into jurisdiction-wide outcomes
- progression toward a final / official standing
- outward reporting

**Standard capabilities** — present in most mature products:

- batch-managed central counting
- adjudication workflow with logged decisions
- scan/tabulation separation
- reconciliation / ballot accounting
- results reporting + standardized higher-authority exports
- public election-night reporting
- audit logging and role-based controls
- ballot-image capture and inspection
- audit / verification and recount support
- multi-election history

**Optional or variant** — depends on jurisdiction, scale, and product family:

- interactive public drill-down and published audit dashboards
- alternative voting-method tabulation (e.g., ranked-choice)
- electronic transmission topologies and national consolidation machinery
- orchestration of the jurisdiction's formal canvass workflow inside the software
- independent retabulation as a separate product

## Interfaces

Surfaces are described conceptually; exact layouts and names vary by product.

### Results / tabulation console

The staff's primary working surface during the count.

- batches, per-contest and per-unit totals, accumulation status
- primary actions: accept/tabulate batches, watch totals, generate reports

### Adjudication screen

Where voter intent is resolved.

- ballot image, the flagged contest, flags and annotations, prior decisions
- primary actions: review the mark, resolve intent for the contest, record the decision, move to the next flag

### Reconciliation / ballot accounting view

Where the count is explained against the ballot record.

- ballots received/cast/counted, per-contest comparisons, discrepancies
- primary actions: compare, investigate, annotate, confirm

### Reporting and export surface

Where results leave the system in controlled forms.

- report templates, accumulation-time reports, export formats for the higher authority
- primary actions: generate, export, schedule

### Public election-night reporting site

The public face of the count.

- contests, choices, totals, reporting-unit breakdowns, timestamps, unofficial/official status
- primary actions: browse contests, drill into reporting units (in interactive realizations)

### Audit / verification surfaces

Where post-election verification is run or reviewed.

- retabulation runs, comparison against certified results, threshold reports, image inspection filters
- primary actions: run audit, compare, produce threshold report

### Administration

Role and permission configuration and audit-log review — first-class surfaces in this domain, not afterthoughts.

## Important Rules / Behaviors

### Results are unofficial until the authority makes them official

Early totals are deliberately provisional. Election-night publication coexists with a later, controlled progression to the official outcome. Products keep this distinction visible.

### Capture can precede counting

Scanning or receiving results media is decoupled from tabulation. Physical processing can spread across days without totals existing early — a deliberate control, not a limitation.

### Adjudication decisions are logged and attributable

Changing how a ballot is interpreted is the most sensitive operation in the system. Every resolution is recorded against an authorized user, and the full decision log is part of the record. There are no silent edits to voter intent.

### Entry happens at the unit level; totals are derived

Results are entered and corrected at the reporting-unit or batch level; jurisdiction-wide figures are computed by aggregation. Corrections flow upward by recomputation, not by editing the aggregate.

### Reconciliation gates credibility

Totals are treated as final only alongside a satisfactory ballot-accounting comparison. Unexplained differences between ballots cast, ballots counted, and votes recorded are investigated, not averaged away.

### The workflow is governed

Role-based access, audit logging, and observer-visible transparency run across the whole workflow — a structural expectation in this domain, consistent across the products researched.

## Variants

- **Voting-system-embedded (dominant US realization)** — the results half lives inside a certified voting-system family alongside ballot marking, precinct scanning, and election building.
- **Standalone central-count products** — tabulation software (often browser-based) that may even tabulate ballots produced by other voting systems, frequently paired with an independent audit product.
- **Public-reporting specialists** — products whose flagship surface is the election-night reporting site, consuming tabulated results from the counting systems.
- **Statewide suite modules** — election-night reporting packaged alongside voter registration and election management in one system for state/county use.
- **National-scale solutions** — vote counting, central operations monitoring, and public results reporting packaged for national electoral bodies, often with transmission-based consolidation.
- **Counting context** — precinct-count (totals produced at the polling place), central count (by-mail/absentee and early-voting focus), or hybrid; all-mail jurisdictions lean almost entirely on central count.
- **Scale** — a single county's count, a state roll-up fed by county exports, or a national consolidation.
- **Public transparency posture** — interactive drill-down sites, flat files and exports, published audit dashboards, or combinations.
- **Alternative methods** — ranked-choice and other alternative voting methods change the tabulation and reporting logic substantially.

A variant remains a variant of this Type as long as the core model — result records, intake, aggregation to official outcomes, outward reporting — still describes it.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Election Management System | upstream sibling — defines the election, maps geography to ballot styles, produces the votable artifacts; ends where tabulation begins. This Type counts what was voted. Vendors often ship both halves as one family, and market labeling sometimes blurs them |
| Voter Registration System | maintains the roll of eligible voters (identity, eligibility, registration lifecycle); interacts with results only indirectly through geography, never through vote totals |
| Government Transparency Portal | generic publication surface over government data; results reporting is election-specific and is the system that produces what such portals would publish |
| Government Open Data Portal | publishes results files as open datasets; consumes exports, does not tabulate, reconcile, or progress results to official standing |
| Online-voting platform | casting-side system that produces counts, but it is not the election authority's results system of record; adjacent rather than the same Type |

The boundary that most needs care in practice is with the Election Management System: the two are sold together, and vendor site taxonomies sometimes file tabulation products under "election management." The structural test is simple — if the product's world is contests, ballot styles, and ballot production, it is preparation; if its world is vote totals accumulating per reporting unit, it is results.

## Representative Products

- Clear Ballot (ClearCount central-count tabulation; VerifyNow independent audit) — transparency-first central-count pole
- Hart InterCivic (Verity family, incl. Verity Central central scan/adjudication) — voting-system-embedded pole
- KNOWiNK (Total Vote, Election Night Reporting module) — statewide-suite public-reporting pole
- Comitia (electoral technology incl. vote counting and election night reporting; the scytl.com domain now serves this offering) — international/LATAM pole
- SOE Software's Clarity election-night reporting network — public ENR portal infrastructure widely used by US jurisdictions (existence observed; not operationally examined)

The two largest US voting-system vendors (Dominion Voting Systems, Election Systems & Software) are major market participants in the results half but their sites could not be examined in this research; no claims in this document rest on them.

## Sources

Research date: **2026-09-07**

- Clear Ballot — ClearCount product page: https://www.clearballot.com/products/clearcount
- Clear Ballot — VerifyNow product page: https://www.clearballot.com/products/verifynow
- Hart InterCivic — Verity (Better Elections): https://www.hartintercivic.com/better-elections/
- Hart InterCivic — Vote by Mail / Verity Central: https://www.hartintercivic.com/vbm/
- KNOWiNK — homepage and Total Vote module descriptions: https://knowink.com/
- Comitia (scytl.com domain) — English homepage and solution list: https://www.scytl.com/en/
- U.S. Election Assistance Commission — Election Management Guidelines (chapter overview): https://www.eac.gov/election-officials/election-management-guidelines
- SOE Software — Clarity ENR portal root (existence only): https://results.enr.clarityelections.com/

> Sourcing limitation: the full official canvass-and-certification guidance (EAC Election Management Guidelines PDF) and several vendor help resources were not retrievable from the research environment on 2026-09-07, and two major voting-system vendors were unreachable. Claims about the canvass/certification stage, state-side consolidation, and vendor-internal workflows are therefore stated at reduced strength and avoid precise operational details.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical / market-sample check are recorded in the paired Research Notes.
