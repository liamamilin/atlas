# Research Notes — Voter Registration System

## Research Goal

Understand, from real products, what a Voter Registration System is: the election authority's system of record for the roll of eligible voters. Extract the smallest defining structure, the common mature capabilities, the variant axes, and the seams against the neighboring election Types (Election Management System, Election Results Management) — discharging the joint-review flags left by the election-management-system pass (2026-09-07) and the election-results-management pass (2026-09-07).

## Initial Boundary

Working hypothesis before research:

- Core use: maintain the authoritative list of who may vote in a jurisdiction — registration applications, eligibility determination, record updates, removals, and each registrant's placement in electoral geography.
- Primary users: election office staff (registrars, voter-services staff); secondary: voters via public lookup surfaces.
- Nearest neighbors: Election Management System (prepares the vote), Election Results Management (counts the vote), electronic poll books (election-day check-in), Jury Management System (another civic process drawing on citizen lists), Government Digital Identity / civil registries (person-level identity), campaign voter-contact files (political persuasion databases built on roll extracts).
- Unknowns: whether electoral placement is definitional or an add-on; how the lifecycle is realized across jurisdictions with different legal regimes (US decentralized county/state, UK register-publication regime, Canada municipal lists); whether derived-roll jurisdictions (registration automatic from a civil registry) break the Type.

## Research Questions

1. What is the central object — the voter record — and what does it hold?
2. What is the registration lifecycle: how do applications enter, how is eligibility determined, what statuses exist, how do updates and removals happen?
3. Is electoral placement (precinct / polling district) part of the system's defining work or a downstream concern?
4. What does list maintenance look like in practice (external data sources, matching, notices, returned mail)?
5. What does the system serve outward (poll books, register publications, lookups, extracts, upward reporting)?
6. Where exactly are the seams with Election Management, Results Management, e-poll books, and jury systems?
7. Would older / regional / differently-organized products (paper-era registers, derived-roll systems, municipal lists) still fit the definition?

## Representative Products

Selected for market representativeness, documentation reachability, different product philosophies, and different jurisdictional/customer levels:

| Product | Vendor | Market position | Why sampled |
|---|---|---|---|
| Voter Central | Tenex Software Solutions (US) | Dedicated voter registration product inside an elections-office suite; 21 US states claimed | The registration-machinery pole: record-centric, list-maintenance-heavy |
| Total Vote (Voter Registration module) | KNOWiNK (US) | Statewide registration + election management suite; also sells e-poll book (Poll Pad) and ENR separately | The suite pole; also supplies the seam evidence (separate products for VR / e-poll book / ENR) |
| VoterView | DataFix (Canada) | Municipal elector-list management; 300+ municipalities in six provinces | The municipal-list pole; list-quality philosophy; public lookup services |
| Eros (+ modules) | Idox (UK) | Electoral Management System for UK local authorities, 45+ years; register-publication regime | The register-publication pole: canvass, register production/distribution, boundary tooling |

Unreachable (recorded as market context only, no claims rest on them): VR Systems (Voter Focus — 403 on both attempts), Dominion Voting Systems and Election Systems & Software (blocked in the two sibling passes as well), Civica's electoral registration product (site surfaces only a polling-day product, "Civica Polling Station").

## Sources

All fetched 2026-09-09 unless noted.

- Tenex Software Solutions — homepage: https://tenexsolutions.com/ ; Voter Central product page: https://tenexsolutions.com/voter-central.html
- KNOWiNK — homepage / product suite (Total Vote, Poll Pad, Poll Print, ENR, GIS address management): https://knowink.com/
- DataFix — homepage/services tree: https://datafix.com/ ; VoterView: https://datafix.com/services/voterview/ ; Online Voter Services: https://datafix.com/services/internet-voter-lookup/ ; Voter Registration module: https://datafix.com/products-and-services/voterview/modules/voter-registration/ ; Electoral Data Management: https://datafix.com/products-and-services/electoral-data-management/
- Idox — Electoral Services / Eros solution page (incl. module tabs ARCD, DMM, IVR, Atlas, LLPG, Eros Polling, Postal Vote Checking, staffing, canvassing): https://www.idoxgroup.com/solutions/electoral-services/
- U.S. Election Assistance Commission — Election Management Guidelines chapter overview: https://www.eac.gov/election-officials/election-management-guidelines ; National Mail Voter Registration Form: https://www.eac.gov/voters/national-mail-voter-registration-form ; Voter Registration Cancellations: https://www.eac.gov/voters/voter-registration-cancellations
- Sibling passes (context, not evidence): applications/election-management-system.md, applications/election-results-management.md (2026-09-07)

## Product Observations

### Tenex — Voter Central (evidence layer: A, direct)

Page title literally "Voter Central | Voter Registration System". Three named pillars:

- **Register** — "Intuitive data entry interface with comprehensive review processes."
- **Manage** — "Maintain voter rolls with in-depth list maintenance."
- **Archive** — "Record voter activity, documents and communications."

Further direct observations:

- "End-to-end management of voter registration, voter records, and provisional ballots."
- "Stores and maintains extensive data about the voter with an easy-to-use search function."
- "Integrates with various departments to notify teams when changes need to be made to the voter record, such as a change of address."
- Data entry: batch registration; "dual data entry and dual verification to increase accountability and accuracy"; "Manage duplicate or incomplete voter records with automated workflows and review cues."
- Voter profile: "tracks changes and transactions for each voter, stores images and documents associated with the voter, and maintains record of voting history."
- List maintenance: "integrates with other agencies and information sources … Sources span real-time API and file-based interfaces with Department of Correction, Vital Statistics, ERIC files, DMV, USPS, and NCOA processors to verify relevant voter changes to comply with federal and state laws."
- Notices: "tools and templates to automate confirmation notices for full life-cycle management from notice generation to processing returned/undelivered mail."
- Adjacent separate products in the same vendor suite: Precinct Central (e-poll book), Live Results (election night reporting), Vote-by-Mail, Petition Processing, Election Force (election worker mgmt), Campaign Desk (campaign reporting — for candidates, not the office).

### KNOWiNK — Total Vote (evidence layer: A)

- "KNOWiNK's Voter Registration system is a centralized voter registration and election management system that securely captures and manages voter, candidate and all election information."
- Modules listed: Voter Registration ("used to help streamline the voter registration process for state and county election officials"), Election Management, Election Night Reporting, and "GIS-based Address Management Software — … automatically assign voters to the correct precinct, ensuring each voter receives the correct ballot style on Election Day."
- Poll Pad (e-poll book) is a separate product: voter check-in/verification at the polling place; "improved voter history accuracy"; real-time data transfer via "ePulse" centralized election management interface.
- Regulatory frame quoted from EAC ESTEP: the program covers "election technologies not covered by the Voluntary Voting System Guidelines (VVSG), including electronic poll books, electronic ballot delivery systems, election night reporting systems, and voter registration systems" — i.e., voter registration systems are recognized as a distinct certification technology family, separate from voting systems and from e-poll books.

### DataFix — VoterView (evidence layer: A)

- "Canada's most widely used elector management system … an electronic view of their electoral information including the ability to make corrections to the voters list and to access various voter counts needed for electoral planning as well as the capability to provide an electronic copy of all changes to the provincial authority at the end of the electoral event."
- "Sophisticated data cleansing tools to identify and correct problems with elector information."
- "The ability to update the elector list dynamically from multiple polling locations for advance polls or on election day. Bar code technology to streamline and improve the accuracy of the elector list update process."
- Voter Registration module: elector completes an "Application to Amend Voters' List" online → "presented to election officials for preliminary verification. If approved, the elector would be added to the list with a provisional status. Once the credentials have been validated at the voting location, the elector would be added to the voters' list by changing the status from provisional to eligible."
- Electronic "voter strike-off": electors with eligible/provisional status searchable through "record elector" functionality; paper-based strike-off extracts carry a provisional-status column.
- Online Voter Services (public): "Am I on the Voters' List?" (name + property address → positive/negative; negative response routes to add-to-list messaging, can initiate the registration flow online); "Where do I vote?" (voting dates/times/locations derived from the elector's address; vote-anywhere configurations show nearest locations); "Who are my candidates?" (optional).
- Electoral Data Management: "the success of any electoral event hinges directly on the quality of your elector information"; "advanced data cleansing utilities, comprehensive reports and extracts".

### Idox — Eros + Electoral Services suite (evidence layer: A)

- "Eros is our secure, cloud-based Electoral Management System … Accurate, reliable electoral register management – maintain a single, trusted source of truth with intelligent data validation and automated updates." "Fully compliant and audit-ready … built-in compliance, clear audit trails."
- "45+ years of electoral expertise. Supporting millions of elector records." (Eros trusted by UK electoral teams for over four decades.)
- Modules (each a tab on the product page):
  - **IVR — Online Canvass Response Portal**: supports the annual canvass and monthly rolling-registration updates; electors confirm/update details; "first provider to enable electors to submit full registration data within the canvass response journey; including nationality, date of birth, and National Insurance number."
  - **DMM — Data Matching & Mining**: "Import and match external data sources … identify potential electors, spot gaps, and confidently manage removals"; sources like Council Tax and Benefits; "identify new residents and flag electors who may no longer live at an address"; UPRN-based matching; duplicate filtering; generate IER (Individual Electoral Registration) applications from imported data.
  - **ARCD — Automatic Register Creation and Distribution**: "Every month, Electoral Services teams need to produce and send updated registers to over 100 recipients … automatically creates, formats and distributes registers"; recipients include "Credit reference agencies, Political parties, candidates and agents, Elected representatives, Jury Central Summoning Bureau, British Library."
  - **Atlas**: boundary reviews on a map — "View and compare existing and proposed boundaries … Draw, adjust, and refine boundaries directly on the map … apply changes instantly"; polling-district management.
  - **LLPG**: links electoral records to the council's official address gazetteer; "Maintain a single, consistent source of truth between LLPG and electoral records."
  - **Eros Polling**: polling-day app (check-in, turnout dashboards) — the e-poll-book-like surface, separate module.
  - **Postal Vote Checking**, **GOV.UK Notify** (canvass communications), **Online Staffing Portal** (election workers), **Telephone/Tablet Canvassing** (doorstep/phone canvass operations).
- Managed services around the platform: electoral print (poll cards, postal vote packs, ballot papers), Postal Vote Management Service, eCount (STV electronic counting — the counting side, a separate service).

### U.S. EAC (regulatory frame; evidence layer: A for the pages themselves)

- National Mail Voter Registration Form: "can be used to register U.S. citizens to vote, to update registration information due to a change of name, make a change of address or to register with a political party … send it to your state or local election office for processing." → the application carries identity, address, name, party; the office processes it.
- Voter Registration Cancellations: cancellation/withdrawal is a managed, jurisdiction-specific process (forms, online portals); one state's form is titled "Request to Inactivate Voter Record" → inactivation as a distinct status operation.
- Election Management Guidelines chapter list has no standalone voter-registration chapter (registration is treated as part of overall election office administration); the technology-side recognition of "voter registration systems" as a distinct family comes via ESTEP (quoted on KNOWiNK's page).

## Cross-product Comparison

| Structure | Tenex Voter Central | KNOWiNK Total Vote | DataFix VoterView | Idox Eros |
|---|---|---|---|---|
| Voter record of record (identity + eligibility attributes + address) | ✔ "extensive data about the voter"; images/documents on record | ✔ "captures and manages voter … information" | ✔ elector records on the Voters' List | ✔ "single, trusted source of truth"; "millions of elector records" |
| Application → authority determination lifecycle | ✔ review processes; dual verification; provisional ballots | ✔ "streamline the voter registration process" | ✔ application → preliminary verification → provisional → eligible at voting location | ✔ canvass + rolling registration applications (IER data capture) |
| Statuses on records | ✔ (statuses implied by workflows; provisional named) | ✔ (not detailed on reachable pages) | ✔ provisional / eligible named; inactivation via strike-off | ✔ (register additions/removals; monthly register cycle) |
| Electoral placement (precinct / polling district / voting place) | ✔ (districts; suite-level geography) | ✔ GIS address management assigns voters to precincts → ballot style | ✔ "Where do I vote?" derived from the list; voting places from elector address | ✔ Atlas polling-district boundaries; LLPG address truth |
| Updates (address, name, party where applicable) | ✔ change-of-address notifications to teams | ✔ (in registration management) | ✔ "Application to Amend Voters' List"; corrections | ✔ electors confirm/update details; monthly updates |
| Removal / cancellation with process | ✔ confirmation notices; returned/undelivered mail processing | ✔ (in registration management) | ✔ strike-off; data cleansing | ✔ DMM "manage removals"; "flag electors who may no longer live at an address" |
| External-source list maintenance / data matching | ✔ DOC, Vital Statistics, ERIC, DMV, USPS, NCOA | ✔ (not detailed on reachable pages) | ✔ data cleansing utilities | ✔ DMM: Council Tax, Benefits; UPRN matching |
| Voter history / participation | ✔ "maintains record of voting history" | ✔ via Poll Pad "voter history accuracy" | ✔ (updates from polling locations) | ✔ (turnout analytics at polling; register history) |
| Duplicate detection / merge | ✔ duplicate/incomplete record workflows | (not observed on reachable pages) | ✔ cleansing tools | ✔ DMM duplicate filtering |
| Public lookup ("Am I registered", "Where do I vote") | (not observed on reachable pages) | (not observed on reachable pages) | ✔ OVS: all three functions | ✔ (canvass portal is elector-facing; lookup not observed) |
| Controlled outward distribution | ✔ (suite-level extracts) | ✔ (suite-level) | ✔ extracts; electronic copy of changes to provincial authority | ✔ ARCD: monthly register to statutory recipients incl. Jury Central Summoning Bureau |
| Audit / governance | ✔ dual verification; accountability emphasis | ✔ (suite-level security emphasis) | ✔ (secure access) | ✔ audit trails, compliance |
| Adjacent capabilities in-family | petition processing, vote-by-mail | election management, ENR, ballot printing | vote-by-mail, election worker mgmt, candidate access | postal vote services, eCount (counting), print, staffing |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being a voter registration system:

1. **The voter record of record.** A persistent, identified record per registrant — identity, eligibility-relevant attributes, residence address — held in the jurisdiction's authoritative roll: the system's answer to "who may vote here." (Remove → a form processor or a people/contact database with no standing as the electoral roll.)
2. **The authority-operated registration lifecycle.** Applications and changes enter from multiple channels; election officials review and determine; records move through statuses (pending/provisional → active/eligible → inactive/challenged → canceled/removed); updates and removals are governed record operations with notices and verification — never silent edits. (Remove → a static voter list snapshot, not a maintained roll.)
3. **Electoral placement.** Each record sits in the jurisdiction's electoral geography — precinct or polling district — which determines where the person votes and, downstream, what they are entitled to vote on. (Remove → a civil registry of eligible persons; the roll can no longer run an election.)

Jointly-held load-bearing:

- 1 alone = civil registry / contact database
- 2 without 1+3 = form-processing workflow over nothing
- 3 without 1+2 = boundary map / GIS with no people
- 1+2 without 3 = eligibility registry that cannot place voters (civil-registry territory)
- 1+3 without 2 = a snapshot list nobody maintains
- 2+3 without 1 = process machinery with no record of record

### L1 — Common Mature Structure

- Registrant search and the full-record view (the daily workhorse; Tenex "easy-to-use search", DataFix "record elector")
- Voter history / participation record per election (Tenex, KNOWiNK/Poll Pad, DataFix polling-location updates)
- Duplicate detection, review cues, record merging (Tenex, Idox DMM, DataFix cleansing)
- List-maintenance integrations with external data sources (Tenex: DOC/Vital Statistics/ERIC/DMV/USPS/NCOA; Idox DMM: Council Tax/Benefits; DataFix cleansing utilities)
- Confirmation-notice generation and returned/undelivered-mail processing (Tenex; Idox canvass chasing cycle)
- Public-facing lookup services (DataFix OVS; Idox elector-facing canvass portal)
- Extracts and reports: poll-book extracts, voter counts for planning, register publications, upward reporting to higher authority (DataFix provincial copy; Idox ARCD; Tenex suite extracts)
- Audit trails, role-based controls, change tracking (Idox explicit; Tenex dual verification; domain-wide expectation)
- Multi-election persistence — the roll spans election cycles; history retained
- Absentee/mail-ballot request handling in many products (Tenex Vote-by-Mail, Idox postal services, DataFix Vote by Mail)
- Petition/nomination signature verification support (Tenex Petition Processing; UK practice)

### L2 — Variant / Optional Structure

- Registration channels: paper forms, online registration, agency/DMV-based automatic registration, same-day/election-day registration, third-party registration organizations
- Party affiliation recording (jurisdiction-dependent; meaningless in some systems)
- Canvass regime: UK annual canvass + rolling monthly registration vs continuous US-style list maintenance vs event-driven municipal list refresh
- Register publication regime: UK monthly published register with statutory recipients (parties, credit reference agencies, jury bureau, library) vs no public register publication
- Provisional-until-verified flows (DataFix: provisional → eligible at the voting location; US provisional ballots)
- Boundary/redistricting tooling depth: in-product geospatial boundary management (Idox Atlas) vs external GIS/address modules (KNOWiNK address management as a separate module)
- Derived-roll jurisdictions: where registration is automatic from a civil/residents' registry, the VR function becomes derivation + maintenance of the electoral roll — the market population thins but the function persists
- Centralization: statewide (US), national (some countries), county, municipal (Canada)

### L3 — Vendor-specific (Research Notes only)

- Tenex: dual data entry/dual verification; batch registration; named source list (ERIC files, NCOA processors); Campaign Desk for candidate-side reporting
- Idox: module names ARCD/DMM/IVR/Atlas/LLPG; GOV.UK Notify integration; UPRN matching; managed print/PVMS/eCount services; "45+ years" positioning
- DataFix: bar-code list updates; OVS delivery via web services or IFrames; "strike-off" terminology; "Application to Amend Voters' List"
- KNOWiNK: ePulse interface; Poll Pad integration; GIS-based Address Management as a separately named module; EAC-certification marketing
- VR Systems: unreachable — no claims recorded

## Rejected Findings

- **"Voter registration = online registration portal."** The portal is one intake channel (L2). Paper-era and paper-channel systems satisfy the core. Rejected as definitional.
- **"Party affiliation is definitional."** Jurisdiction-dependent; several sampled markets have no party registration. L2.
- **"Automatic/DMV registration is definitional."** A channel variant of one market. L2.
- **"The VR system computes precinct boundaries."** Boundary *management* varies (in-product in Idox Atlas; separate GIS module at KNOWiNK). The invariant is that the record *carries* placement, not that the system draws boundaries. Held at L0 as placement-on-record, with boundary tooling as variant.
- **"Voter history is definitional."** Common and important for list maintenance, but a roll without history is still a roll. L1.
- **"The VR system counts votes / reports results."** No sampled product claims this; counting is explicitly a separate product/service in three vendor taxonomies (Tenex Live Results, KNOWiNK ENR, Idox eCount). Rejected.
- **"The VR system is the election-day check-in tool."** Check-in is the e-poll book's job (separate products at Tenex, KNOWiNK, Idox; separate EAC certification family). The VR system produces the extract and receives participation updates back. Rejected as definitional.

## Boundary Findings

1. **vs Election Management System** (discharges the 2026-09-07 flag from this side): the seam is **roll vs election definition**. The VR system holds who may vote and where they sit in electoral geography; the EMS consumes those assignments to derive ballot styles and produces what voters vote on. The EMS pass described this Type as "maintains the roll of eligible voters and their precinct assignments" — this pass confirms that description from VR-side evidence (KNOWiNK: address management assigns voters to precincts "ensuring each voter receives the correct ballot style"; Idox: Atlas polling districts inside the electoral system). **Ratify keep-both.** Handoffs: geography assignments + register extracts → EMS ballot-style derivation; poll-book production → election day.
2. **vs Election Results Management** (discharges the 2026-09-07 flag from this side): the seam is **roll vs count**. The VR system never holds vote totals; the results system never holds eligibility. Interaction is indirect: voter history flows from participation records (poll books), not from results; provisional processing touches both worlds but the records live on their own sides. Vendor taxonomies agree: Tenex (Voter Central vs Live Results), KNOWiNK (Total Vote vs ENR module), Idox (Eros vs eCount). **Ratify keep-both.**
3. **vs Electronic Poll Book**: the poll book is the election-day check-in surface consuming a roll extract; the VR system is the system of record that produces the extract and receives back participation updates. All three multi-product vendors separate them; EAC ESTEP certifies them as separate technology families. Keep separate.
4. **vs Jury Management System**: jury systems run the summons/qualification process for courts; the voter roll is one *source list* (Idox ARCD names the Jury Central Summoning Bureau as a register recipient). The VR system supplies; it does not manage jury service. Keep separate.
5. **vs Government Digital Identity / civil registry**: identity proofing and population registries concern the person generally; the VR system concerns the person *as elector* — eligibility + electoral placement. In derived-roll jurisdictions the VR function collapses toward the civil registry plus derivation; recorded as a boundary note, not a definition change.
6. **vs campaign/constituent voter-contact platforms**: those are persuasion databases built *from* roll extracts (Tenex even ships a separate Campaign Desk for candidates). The VR system is the authority's legal record, not a targeting database. Keep separate.
7. **vs Public Benefits Management**: different eligibility domain (benefits vs franchise); no shared core beyond "government eligibility records."

## Historical / Market-Sample Check

- Paper-era practice: bound registers of electors organized by polling district, card files, annual canvass forms, hand-marked poll books — record + lifecycle + placement all present with no software. The definition holds.
- Regional regimes: UK register-publication regime (canvass → monthly published register → statutory distribution), Canadian municipal lists with provincial upward reporting, US decentralized statewide/county systems — all inside the definition.
- Derived-roll jurisdictions (registration automatic from residents' registries): the *function* (maintaining the electoral roll) persists but may be realized as derivation from a civil registry; the standalone market population thins there. Recorded as a variant/boundary note; the definition is written at the function level so it still applies.
- The definition does not depend on: online channels, party registration, ERIC-style data exchanges, GIS tooling, or any specific status vocabulary.

## Uncertainties

- VR Systems (Voter Focus), one of the largest dedicated US VR vendors, was unreachable (403 ×2). No claims rest on it; the US dedicated-vendor pole is covered by Tenex instead.
- Dominion and ES&S remain unreachable (consistent with both sibling passes); treated as market context only.
- Exact status vocabularies (active/inactive/challenge/cancel; provisional/eligible) vary by jurisdiction and product; this document keeps statuses conceptual. Only DataFix names provisional→eligible explicitly; Tenex names provisional ballots (not statuses).
- Whether precinct assignment is held inside the VR product or a sibling address/GIS module varies by packaging (KNOWiNK separates the module); the record carries placement either way.
- ERIC's exact role is evidenced only as a named integration source at Tenex; no deeper claims.
- Public lookup surfaces were directly observed only at DataFix (OVS) and Idox (elector-facing canvass portal); their ubiquity is asserted at common-not-definitional strength.

## Final Synthesis

A Voter Registration System is the election authority's system of record for the roll of eligible voters. Its defining core is three jointly-held structures: the voter record of record (persistent identified registrant records — identity, eligibility-relevant attributes, residence address — constituting the authoritative answer to "who may vote here"); the authority-operated registration lifecycle (multi-channel intake → official review/determination → active → updates → process-governed removal, with intermediate statuses such as provisional/inactive); and electoral placement (each record placed in the jurisdiction's electoral geography, determining where the person votes and what they are entitled to vote on). Around that core, mature products add search, voter history, duplicate handling, external-source list maintenance, notices, public lookups, controlled extracts/publications, audit governance, and multi-election persistence. The Type's seams are stable and vendor taxonomies corroborate them: election definition belongs to Election Management, counting to Election Results Management, election-day check-in to electronic poll books, jury process to jury systems, and general identity to identity/civil-registry territory. The joint-review flags from the election-management-system and election-results-management passes are discharged: all three Types stand, with the roll / definition / count division of labor confirmed from the registration side.
