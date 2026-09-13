# Election Management System

## Overview

An **Election Management System** is the election authority's system of record for preparing an election. It holds the election as a defined object — when it happens, in which jurisdiction, and what is being voted on — maps the jurisdiction's geography to the specific set of contests each group of voters sees, and produces the ballots and voting-process configuration that voting and counting depend on.

The system exists to answer a deceptively narrow question: **what exactly will each voter be asked, and on what artifact will they answer it?** Answering it requires holding together legal content (offices, questions, candidates), jurisdictional geography (precincts, districts, boundary splits), and physical production (printed ballots, device programming, mail packets) under strict change control.

Its boundary in the election-technology landscape is likewise narrow. The list of eligible voters is the domain of a **Voter Registration System**; the counting, canvassing, and publication of results belong to **Election Results Management**. An Election Management System sits between them: it takes geography assignments from the roll, and it hands votable ballots and configured voting processes to the counting side. In practice these three are often sold by the same vendors as one family, but they remain distinct responsibilities — and this document describes the middle one.

## Users & Context

The primary users are professional election staff inside government election offices — typically county or municipal election departments, and state election divisions for statewide elections:

- **election directors / election administrators** — own the election as a whole; approve definitions and ballot configurations before anything is produced
- **ballot and election-definition staff** — build contests, candidates, and ballot questions; design and proof ballot styles
- **precinct / GIS data staff** — maintain the geography: precinct boundaries, district assignments, and the address-to-precinct mapping that determines which voter gets which ballot
- **equipment and operations staff** — configure the devices and locations where voting happens, and produce or manage ballot printing
- **office staff running by-mail operations** — produce and manage mail-ballot packets where voting by mail is part of the election

A second tier of users consumes what the system produces rather than working in it: poll workers receive the configured voting locations and ballots; election workers may receive training material through the same product family. Everything downstream — voters, candidates, observers, media — interacts with the system's outputs (ballots, sample ballots, configured devices), not with the system itself.

The work context is unlike ordinary government back-office software in three ways. It is **episodic and deadline-driven**: work is organized around election cycles, with legal deadlines that cannot slip. It is **high-scrutiny and high-integrity**: mistakes in a ballot can disfranchise voters or invalidate contests, so changes are controlled and recorded. And it is **repeatable**: the same machinery must serve primaries, general elections, special elections, and local contests, year after year, often with past elections retained for reference and audit.

## Core Model

### The Defining Core

```text
Election Definition
└── Election Geography → Ballot Styles
    └── Ballot Production / Voting-Process Configuration
        └── (handed off to casting and counting)
```

Three structures carry the Type. If any one is removed, what remains is no longer election management:

**1. The election definition.** The election exists inside the system as a first-class configured object: a dated, jurisdiction-scoped occasion whose contests — offices and ballot questions — are declared with their content: candidate names as they should appear, measure titles and text, contest ordering, and instructions. The election definition is the authoritative answer to "what is being voted on, where, and when." Everything else in the system derives from it. Elections of different types (primary, general, special, local) are built with the same machinery; mature products carry the definitions of past elections alongside current ones.

**2. Election geography mapped to ballot styles.** The jurisdiction's territory is configured as election geography — precincts, districts, and the boundary splits where a district line cuts through a precinct. From this geography the system derives **ballot styles**: the specific set of contests a group of voters sees, determined by where they live. A voter does not choose their ballot; geography assigns it. This is the structural heart of the Type, because it is what makes a single election contain a large number of distinct ballots — a state senate race appears only for voters in that district, a municipal question only for that city's voters. One product in the research sample describes this mechanism directly: address-management software assigns voters to precincts so that each voter receives the correct ballot style on election day.

**3. Ballot production and voting-process configuration.** The definition and its styles are turned into the votable artifact and the configuration that makes voting possible:

- printed ballots — bulk print runs for polling places, and increasingly on-demand printing in the right quantities at the right locations
- ballot media or programming that carries the definition to the devices voters mark and the machines that scan ballots
- by-mail packet content for jurisdictions voting by mail
- the setup of voting locations and their equipment

Without this production step the definition never becomes something a voter can actually use — which is why production belongs to the defining core rather than to a printing "feature."

### What Mature Products Add

Around that core, mature products carry a fairly consistent set of capabilities. They are what makes the system practical, not what makes it an election management system:

- **Ballot proofing and review** — side-by-side review of every ballot style in one place, individual adjustment of any style, and verification passes before anything is printed or loaded onto a device.
- **Governance machinery** — role-based permissions, change monitoring, and audit logging across the system. Election work is legally accountable work; the system records who changed what.
- **Ballot printing management** — jurisdiction-specific print presets, paper sizes and stock, quantity planning, and on-demand printing at vote centers and central offices.
- **Voting-equipment configuration** — preparing and programming the voting devices, simplified polling-place setup, and ballot-activation mechanisms so poll workers can start voting quickly.
- **Absentee and by-mail support** — workflows for producing mail ballots and processing returned by-mail ballots, a first-class mode in some jurisdictions rather than an exception.
- **Election-worker support** — training and reference material for poll workers and election staff, sometimes delivered as a product surface of its own.
- **Precinct and address configuration** — increasingly GIS-assigned, keeping the address-to-precinct-to-ballot-style chain current as boundaries change.
- **Coupling with tabulation** — the counting systems in the same product family tabulate exactly the ballots this system defined and produced; the definition is the upstream half of the count.
- **Multi-election operation** — concurrent preparation of different elections and retention of completed ones.

### One Structure, Many Implementations

The core is conceptual, and products realize it differently:

```text
Concept:   Election definition
Realized as:  election/contest setup inside a voting-system suite, or an
              election module in a statewide administration system

Concept:   Ballot style
Realized as:  per-precinct ballot versions across a range of card sizes
              and paper stocks; device-specific ballot media

Concept:   Ballot production
Realized as:  central print runs; on-demand office/precinct printers;
              device programming media; by-mail packet generation
```

A reader who has only seen one realization — for example, a county office designing ballot styles for scanners — should still be able to recognize the same structures in a statewide administration suite or a paper-ballot-only operation.

## How It Works

The system's central workflow is the **election build**: the repeatable sequence that turns legal requirements into a votable election.

```text
Declare the election
  (date, election type, jurisdiction scope, contests,
   candidates, ballot questions)
→ configure election geography
  (precincts, districts, splits; address-to-precinct assignment)
→ derive ballot styles
  (which contests each group of voters sees)
→ design and proof every ballot style
  (layout, language, review and correction loop)
→ produce ballots and configure the voting process
  (print runs or on-demand printing; device programming;
   by-mail packets; voting-location setup)
→ support the voting period
  (early voting, election day, by-mail intake)
→ hand off to tabulation and canvass
  (the counting side consumes exactly what was defined and produced)
```

Several properties of this workflow matter for understanding the Type:

- **It is iterative under deadline.** Candidate filings change, measures are amended, court rulings alter ballot content. Each change forces regeneration of the affected ballot styles and their downstream artifacts — which is why change control and proofing are central surfaces, not conveniences.
- **It is geography-driven end to end.** A boundary change between elections can reassign large numbers of voters to new precincts and new ballot styles; keeping geography and styles in sync with the voter roll's assignments is continuous work.
- **It runs several elections at once.** A primary and a local special election may be in build simultaneously; the system maintains them as separate definitions with their own styles and productions.
- **It ends deliberately.** Once ballots are produced and devices configured, the system's role shifts to support; aggregation of voted ballots into results belongs to the counting side of the election family.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Election definition workspace

The starting surface for a new election.

- typical information: election name, date, type, jurisdiction scope; contest list with offices, candidates, and questions
- primary actions: create an election, declare contests and content, copy structure from a prior election, lock or approve the definition

### Ballot design and proofing surface

The most distinctive surface of the Type — where each ballot style is composed and verified.

- typical information: per-style ballot layout, contest placement, candidate text, instructions, language variants, card size or paper stock
- primary actions: generate styles from the definition, edit a style individually (commonly with direct manipulation of ballot elements), proof all styles in one review set, mark styles ready for production

### Election geography / precinct configuration

The surface that keeps the territory current.

- typical information: precinct boundaries, district assignments, split precincts, address ranges; in some products a GIS map view
- primary actions: edit precinct and district configuration, assign addresses to precincts, review the resulting ballot-style impact

### Ballot production and printing management

The surface where definitions become physical artifacts.

- typical information: print quantities by style and location, paper sizes and presets, print status, on-demand printer queues
- primary actions: generate print files, print on demand at a vote center or office, track production completeness

### Equipment and voting-location setup

The surface that prepares voting itself.

- typical information: voting locations, devices and their assigned elections, ballot-activation materials, poll-worker-facing setup steps
- primary actions: configure devices for the election, prepare location kits, run pre-election testing and setup verification

### Governance surfaces

Roles, permissions, and audit views.

- typical information: user roles, change history on ballots and definitions, audit logs of system activity
- primary actions: assign roles, review changes, export audit records

### Training and reference surfaces (some products)

- self-paced training material for poll workers, roving technicians, and election staff, covering the technology the election build produced.

## Important Rules / Behaviors

- **Geography decides the ballot.** A voter's ballot style follows from their precinct and district assignments — not from preference. The system must keep the geography chain (address → precinct → district combination → ballot style) consistent with the voter roll, or voters receive wrong ballots.
- **Changes are governed, not free.** Ballot and definition changes pass through role-based permissions, are monitored as they happen, and are recorded in audit logs. This is structural: ballots are legal instruments, and the system's record of who changed what is part of the election's defensibility.
- **The definition is upstream of everything.** Voting devices count only what the definition produced; a mismatch between the definition, the printed ballots, and the device configuration is a critical failure. Products in the research sample emphasize that the tabulation side consumes exactly the ballots their election-management side creates.
- **One election definition may exist in many physical forms.** The same ballot style can exist as a printed sheet, an on-demand print, a device screen, and a mail packet — all of which must stay faithful to the definition.
- **The paper artifact is the integrity anchor in the dominant realization.** Several products in the sample explicitly commit to voter-verifiable paper ballots and reject encoding votes in barcodes or similar machine-only representations; this is a strongly held market posture rather than a universal rule.
- **By-mail is a mode, not an edge case.** In some jurisdictions essentially all voting is by mail; the system still performs the same defining work — definition, styles, production — with packet production and central intake replacing polling places entirely.

## Variants

- **Voting-system-embedded.** The dominant realization in the United States: the election management system is the definition-and-production component of a certified voting system family, alongside marking and scanning devices and tabulation. Election building, device programming, and counting are one tightly coupled world.
- **Administration-suite module.** The election management function ships alongside voter registration, election night reporting, and address/GIS management as one statewide or county system. The defining work is unchanged; the surrounding family is wider.
- **Voting-method contexts.** In-person paper, hybrid (device-marked with paper record), all-mail, vote centers, and early-voting-heavy operations each shift the weight of the production and configuration work — all-mail operations remove polling-place setup but not ballot production.
- **Scale and level.** County election departments are the classic operator; statewide deployments add multi-jurisdiction coordination; some vendors package election management as a service for jurisdictions that outsource operation.
- **Regulatory context.** In the United States, voting systems including their election-management components operate under federal certification guidelines, with neighboring technologies (electronic poll books, election night reporting) certified under separate voluntary programs. Other countries run centralized national election machinery with the same defining structures at national scale.
- **Alternative voting methods.** Ranked-choice and other methods appear as configuration layers over the same election build.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Voter Registration System | upstream sibling | maintains the roll of eligible voters and their precinct assignments; the election management system consumes those assignments to derive ballot styles, but does not manage the roll |
| Election Results Management | downstream sibling | tabulates, reconciles, canvasses, and publishes results; the election management system ends where votable ballots and configured processes are handed over |
| Government Service Portal | adjacent, voter-facing | publishes information and services to citizens (including sample ballots and polling-place lookup); it is an output surface, not the authority's system of record for the election |
| Event Management Platform | structural look-alike | both manage a dated occasion with locations, staff, and materials; an election management system is defined by contest content, ballot styles, and legally specified ballots — with no attendees, registrations, or tickets |
| Jury Management System | civic-process neighbor | both draw on citizen lists for a legal civic process; jury management summons and qualifies jurors for courts and involves no ballots or election geography |

The closest seam is with the two sibling election Types, because vendors commonly package all three in one family and market language ("election management") is sometimes stretched over tabulation products as well. The functional test is stable: maintaining the voter roll is voter registration; counting and reporting is results management; defining the election and producing what voters vote on is this Type.

## Representative Products

- Hart InterCivic — Verity / Verity Vanguard with its end-to-end election management workspace
- Clear Ballot — ClearVote family (ballot definition, central count, printing, verification)
- KNOWiNK — Total Vote (statewide registration + election management suite with address/GIS management and on-demand ballot printing)
- Dominion Voting Systems — Democracy Suite (market context; product site not accessible to this research)
- Election Systems & Software — Unity (market context; product site not accessible to this research)

## Sources

Research date: **2026-09-07**

- Hart InterCivic — https://www.hartintercivic.com/ , https://www.hartintercivic.com/solutions/ , https://www.hartintercivic.com/vanguard-family/ , https://www.hartintercivic.com/better-elections/
- Clear Ballot — https://www.clearballot.com/ , https://www.clearballot.com/products , https://www.clearballot.com/products/cleardesign , https://www.clearballot.com/solutions/vote-by-mail
- KNOWiNK — https://knowink.com/

> Sourcing limitation: official documentation for two of the largest voting-system vendors (Dominion Voting Systems, Election Systems & Software) and for a UK regional electoral-services sample could not be reached from the research environment (blocked or timed-out sites). Those products are listed as market context only, and no operational claim in this document rests on them. Evidence for the described structures comes from the three reachable vendors' official product pages; single-product behaviors (GIS-based precinct assignment, training surfaces, one-step polling-place setup) are described as product observations rather than Type-wide rules. Detailed observations, the cross-product comparison, and vendor-specific claims are recorded in the paired Research Notes.
