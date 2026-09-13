# Research Notes — Election Management System

Research date: 2026-09-07
Slug: election-management-system
Directory location: §24 Government, Public Sector & Civic

## Research Goal

Understand what an Election Management System (EMS) actually is from real products: what the central objects are, what the election lifecycle looks like inside such a system, where it starts and ends relative to sibling Types (Voter Registration System, Election Results Management), and what varies between the voting-system-embedded pole and the broader election-administration-suite pole.

## Initial Boundary (pre-research hypothesis)

- EMS = election-authority-side software for defining, preparing, and administering an election as an event: election definition, ballot definition/production, election geography, polling-place/equipment configuration, election-worker support.
- Sibling leaves in DIRECTORY.md §24: Voter Registration System (the roll of eligible voters) and Election Results Management (tabulation, canvass, reporting). EMS should NOT absorb either — but the three interlock tightly and are often sold as one suite. This was flagged as a likely boundary pressure point before research began.
- Adjacent: Jury Management System (civic-duty processing), Event Management Platform (superficial structural resemblance), Government Service Portal (voter-facing output surfaces), online-voting platforms (casting-side).

## Research Questions

1. What is the central object — is there an "election definition" and what does it contain?
2. How does election geography (precincts, districts, splits) relate to ballots ("ballot styles")?
3. What does ballot production span — printing, device programming, by-mail packets?
4. Where does the system start (candidate qualification? calendar?) and end (tabulation handoff?)?
5. What governance machinery exists (roles, permissions, audit logging, change monitoring) and why?
6. How do voting-system-embedded EMS products differ from broader election-administration suites?
7. What interfaces does the election-office staff actually work in?
8. Historical/regional check: do paper-era election administration, all-mail jurisdictions, and non-US centralized models fit the definition?

## Representative Products

| Product | Vendor | Pole | Why selected |
|---|---|---|---|
| Verity / Verity Vanguard (+ Workspace) | Hart InterCivic | voting-system-embedded EMS, paper-first philosophy | EAC-certified voting system; clear election-lifecycle and management-surface evidence |
| ClearVote family / ClearDesign | Clear Ballot | voting-system-embedded EMS, transparency/audit-oriented, browser-based | vendor self-labels ClearDesign "election management system"; strong ballot-definition evidence |
| Total Vote (+ Poll Print, Poll Pad, ePulse) | KNOWiNK | statewide administration suite: VR + Election Management + ENR + GIS | the broader-administration pole; shows the EMS/VR seam from one vendor |
| Democracy Suite / Electionware (Election Event Designer) | Dominion Voting Systems | voting-system-embedded EMS (largest-tier vendor) | market context only — site blocked; no operational claims rest on it |
| Unity | Election Systems & Software (ES&S) | voting-system-embedded EMS (largest US vendor) | market context only — site blocked |

Selection principles satisfied: market representation (four of the dominant US voting-system/administration vendors attempted), different product philosophies (paper-first vs browser/transparency-first vs unified-suite), different customer tiers (county vs statewide), different packaging poles (embedded vs suite). The UK regional sample (halarose) and poll-worker specialists (Tenex) were attempted for the historical/regional check but were unreachable; the regional check is completed by reasoning, not by those sources.

## Sources

Fetched successfully (2026-09-07):

- Hart InterCivic — homepage, Solutions (Why Verity), Vanguard Family, Better Elections (Verity overview):
  - https://www.hartintercivic.com/
  - https://www.hartintercivic.com/solutions/
  - https://www.hartintercivic.com/vanguard-family/
  - https://www.hartintercivic.com/better-elections/
- Clear Ballot — homepage, All Products, ClearDesign product page, Vote-By-Mail solution page:
  - https://www.clearballot.com/
  - https://www.clearballot.com/products
  - https://www.clearballot.com/products/cleardesign
  - https://www.clearballot.com/solutions/vote-by-mail
- KNOWiNK — homepage (Total Vote / Poll Print / Poll Pad / ePulse descriptions):
  - https://knowink.com/

Attempted and abandoned (per source-access rules):

- https://www.dominionvoting.com/ and /democracy-suite/ — HTTP 403 ×2. Abandoned.
- https://www.ess.com/ and /what-we-do/unity/ — HTTP 403 ×2. Abandoned.
- https://www.halarose.co.uk/ — timeout ×2. Abandoned.
- https://www.tenexsoftware.com/ — transport error. Abandoned.
- https://www.civix.com/ — cookie-wall only, no content. Abandoned.
- https://www.eac.gov/voting-equipment/voting-systems-certified-by-the-eac — 404 (URL guess failed; EAC certification pages not pursued further given budget).

Source-access limitation: the two largest US voting-system vendors (Dominion, ES&S) and the UK regional sample could not be fetched. No operational claim in the research below rests on them; they appear only as named market context. All product-specific evidence below is Layer A (directly observed on fetched pages); cross-product commonality is Layer B; the canonical model is Layer C inference.

---

## Product A — Hart InterCivic (Verity / Verity Vanguard)

### Key observations (Layer A)

- Verity is positioned as "a comprehensive election technology solution designed to make the lives of election administrators, poll workers, and voters easier — and more secure."
- "Verity's intuitive software streamlines building and managing your elections." Election-building is an explicit software activity.
- Verity Vanguard (new line): "Vanguard Workspace is a comprehensive solution for end-to-end election management. Built on Verity Voting's industry leading software platform, Vanguard Workspace up levels Verity's intuitive workflows with new efficiencies and enhanced security measures so you can build your elections faster, with greater auditability and transparency."
- Vanguard platform promise: "enables you to move faster at every step of the election lifecycle"; "Highly configurable and modular, Vanguard fulfills your multifaceted election needs."
- Hardware/software family around the management surface: Boost (ballot issuance — "issue ballots on demand or issue voter self service tickets, called VotePasses, for independent ballot activation on a Flex ballot marking device"), Flex (universal ballot marking device), Vault (precinct scanning). "One step polling place set up" is advertised as a software-enabled property.
- Voting-method options in one family: Paper (hand-marked paper ballots scanned), Hybrid (touchscreen marking with voter-verifiable paper trail), By Mail ("Absentee and by mail ballots are easy to manage with scalable, efficient central scanning").
- Governance machinery: "Every product in the Verity platform is equipped with robust audit logging and role-based control measures to ensure end-to-end transparency of your elections."
- Paper-integrity posture: "Verity paper-based solutions never encode voter choices in any digital seal for tabulation. Votes are captured from the same human-readable text that voters use to verify their choices."
- A separate product area exists for "Voter Education and Outreach" (voter-facing layer).

## Product B — Clear Ballot (ClearVote family / ClearDesign)

### Key observations (Layer A)

- ClearDesign is explicitly labeled by the vendor: "ELECTION MANAGEMENT / BALLOT CREATION — The secure, intuitive, and flexible election management system."
- "ClearDesign enables election officials to design ballots with easy-to-use browser navigation and familiar formatting tools."
- "Election department staff can quickly generate, modify, and proof all their ballot styles for a wide range of card sizes and review and modify each ballot individually using drag & drop capabilities."
- "Review all ballot types in one set" (streamlined proofing); "Assign roles and monitor any changes made in the system" (systemwide protection); "Flexible Ballot Printing — develop a printing solution tailored for your jurisdiction with different presets and paper sizes."
- ClearCount is also categorized by the vendor under "ELECTION MANAGEMENT": "browser-based central count tabulation system... ClearCount can tabulate ballots created by all major voting systems." Central count and ballot definition share the "Election Management" bucket — notable boundary evidence.
- VerifyNow: "independent results verification... provides a ballot inventory tool, ensures ballot reconciliation, and improves canvassing and transparency" (auditing category — adjacent to results management).
- PrintNow and Marathon printer: "flexible... solution for printing ballots" with "uses at both central election offices and individual vote centers"; Marathon prints "hand-markable paper ballots across polling places and early voting centers... print only the ballots they need — right when they need it"; integrates "into the PrintNow ecosystem and major pollbook vendors."
- Clear Ballot Academy Online: "self-paced, mobile, and web-based hub for poll workers, rovers, and election administrators" (training surface — election-worker support).
- Solutions categories: Vote-By-Mail ("trusted, efficient vote-by-mail and absentee tabulation solutions"), Post-Election Audits and Results Verification, In-Person Voting, Ranked-Choice Voting, Paper Ballot Delivery, "Elections as a Service."
- Integrity posture: "committed to paper ballots that voters can review, verify, and trust. We will never conceal votes within a barcode."
- Customer base named on product pages: counties (Lycoming PA quote about the county's "voting system search"; Pierce WA, Harney OR, Snohomish WA, King WA, Multnomah OR, Elbert CO) — county election departments are the buyer.

## Product C — KNOWiNK (Total Vote / Poll Print / Poll Pad / ePulse)

### Key observations (Layer A)

- Total Vote: "centralized voter registration and election management system that securely captures and manages voter, candidate and all election information. It is the only software system that encompasses the entire election process into one system."
- Election Management module: "provides all election functions in a single, unified manner for ALL elections including statewide primary, special and general elections plus local elections" — multi-election-type support.
- GIS-based Address Management Software: "help elections officials automatically assign voters to the correct precinct, ensuring each voter receives the correct ballot style on Election Day" — the geography → ballot style mechanism, stated directly.
- Election Night Reporting is a separate module ("display Election Night Reporting results that are easy for the public to understand") — results reporting exists as its own product line, supporting the EMS/results boundary.
- Poll Print: "secure, high-quality on-demand ballot system... provides convenience, giving jurisdictions the right quantity of ballots for every election, and during early voting" — on-demand ballot production tied to election setup.
- Poll Pad (electronic poll book): voter check-in, "customizable workflows allow each election official to meet required steps according to their jurisdiction's requirements"; ePulse is "a centralized election management interface" enabling "real-time data transfer, audit capabilities, and improved voter history accuracy."
- Context from the vendor's own certification press release: the EAC's ESTEP program covers "election technologies not covered by the Voluntary Voting System Guidelines (VVSG), including electronic poll books, electronic ballot delivery systems, election night reporting systems, and voter registration systems" — i.e., the voting system itself (which contains the EMS) is certified under VVSG; neighboring election-supporting technologies are a separately standardized family. Useful regulatory-side boundary evidence.
- Buyer side: "state and county election officials" (registration), Secretaries of State quoted (statewide context).

## Unreachable market context (no operational claims rest on these)

- Dominion Voting Systems — Democracy Suite (the suite includes an "Election Management System" component; its ballot-design tool is publicly known as Election Event Designer). Site 403. Named only because its suite component is literally marketed under the Type's name — strong market-context evidence that the Type label is real industry vocabulary.
- ES&S — Unity (election management software). Site 403.
- halarose (UK electoral services software for councils) — timeout. Would have been the non-US, register-centric regional sample.
- Tenex Software Solutions (poll worker management / election night reporting) — transport error.
- Civix — cookie wall.

---

## Cross-product Comparison

| Dimension | Hart (Verity/Vanguard) | Clear Ballot (ClearDesign family) | KNOWiNK (Total Vote) |
|---|---|---|---|
| Self-label for the Type | "end-to-end election management" (Workspace) | "election management system" (ClearDesign) | "Election Management module" (Total Vote) |
| Election definition | implied by "build your elections" lifecycle wording | ballot styles as first-class objects (generate/modify/proof) | election functions for named election types (primary/special/general/local) |
| Geography → ballot style | implied by voting-method family; not spelled out on fetched pages | ballot styles for "a wide range of card sizes", per-style proofing | explicit: GIS address management assigns precincts → "correct ballot style" |
| Ballot production | Boost ballot issuance on demand; VotePass activation | flexible printing presets/paper sizes; PrintNow/Marathon on-demand | Poll Print on-demand ballots "right quantity... for every election" |
| Voting-equipment configuration | "one step polling place set up"; device family programmed from the platform | device ecosystem consumes ballots the design produces | poll-book workflows configured per jurisdiction |
| By-mail/absentee | "easy to manage with scalable, efficient central scanning" | dedicated Vote-By-Mail solution (absentee tabulation) | not observed on fetched page |
| Governance machinery | audit logging + role-based control on every product | roles + "monitor any changes made in the system" | audit capabilities in ePulse/Poll Pad |
| Results/tabulation relationship | Verity family includes scanning/tabulation hardware | ClearCount (central count) shares the "Election Management" vendor bucket | Election Night Reporting is a separate module |
| Election-worker support | poll workers named as beneficiaries; "one step" setup | Academy training hub for poll workers/rovers/administrators | poll-book workflows for check-in |
| Buyer scale | counties/jurisdictions | "counties of all sizes" | statewide + county |

Layer B findings (cross-product commonality, ≥2 products): election definition as configured object; ballot styles as derived per-geography artifacts; ballot proofing; ballot printing/production incl. on-demand; roles/audit/change-control machinery; by-mail support; tight family coupling with tabulation devices.

Layer B qualified (2 of 3): training/education surface for election workers.

Layer A single-product (kept qualified): GIS-based precinct assignment (KNOWiNK); multi-election-type enumeration (KNOWiNK); "Elections as a Service" packaging (Clear Ballot); one-step polling place setup (Hart).

## Canonical Model (Layer C)

### L0 — Defining Invariant

Three structures. Removing any one makes the product stop being an Election Management System:

1. **The election definition** — the election exists inside the system as a first-class configured object: a dated, jurisdiction-scoped occasion whose contests (offices and ballot questions) and their content (candidates, measures, instructions) are declared and maintained. The system of record for what is being voted on, where, and when.
2. **Election geography → ballot style mapping** — the jurisdiction's territory is configured as precincts/districts/splits, and the system derives which contests each group of voters sees: ballot styles. A voter's ballot is determined by where they vote, not chosen by them.
3. **Ballot production / voting-process configuration** — the definition is turned into the votable artifact and its supporting configuration: printed ballots (central runs or on-demand), ballot media/programming for marking and counting devices, and by-mail packet content. The EMS output is what the casting and counting processes consume.

Justification for minimality:

- **Polling places / poll workers are NOT L0.** All-mail jurisdictions (several named Clear Ballot customers are Oregon/Washington counties) run elections through the same EMS structures with no traditional polling places. Polling-place and worker administration is common mature structure, not defining.
- **Voter registration is NOT L0.** The roll is a sibling Type; the EMS consumes district/precinct assignments from it.
- **Tabulation/reporting is NOT L0.** Counting belongs to Election Results Management; the EMS ends where votable artifacts and configured processes are handed off.
- **Historical check:** a pre-computer election office performing "define the election → map precincts to ballot layouts → produce ballot papers and poll books" satisfies all three structures with paper. Centralized national election authorities and decentralized US counties both satisfy them. The definition does not depend on software-era features (GIS, browser UI, certification regimes).

### L1 — Common Mature Structure

- Ballot proofing/review surfaces (per-style review, all ballot types in one set, change monitoring)
- Roles, permissions, and audit logging as first-class machinery (high-integrity government domain)
- Ballot printing management (presets, paper sizes/stock, quantities, print-on-demand at vote centers)
- Voting-equipment configuration (device programming/activation media, simplified polling-place setup)
- Absentee/by-mail ballot administration support (central scanning workflows, by-mail solutions)
- Election-worker support surfaces (training hubs; simplified poll-worker-facing setup)
- Precinct/district configuration incl. GIS-assigned address management (single-product direct; common pattern)
- Coupling with tabulation: the EMS sits in a product family whose other members count what it produced
- Multi-election operation over time (different election types; archival of past elections)

### L2 — Variant / Optional Structure

- Packaging pole: EMS as the definition/production component inside a certified voting system (dominant US realization) vs EMS as part of a broader administration suite that also spans voter registration and election night reporting vs standalone election-administration software (regional models)
- Voting-method context: in-person paper, hybrid (BMD + paper), by-mail-heavy, vote centers, early voting
- Government level: county/municipal vs statewide; "Elections as a Service" packaging
- Regulatory regime: federal certification (VVSG) for voting systems, voluntary certification programs for neighboring technologies (e-pollbooks, ENR); non-US centralized models
- Ballot media/physical-form diversity (card sizes, thermal vs cut-sheet printing)
- Ranked-choice and other alternative voting-method support as a configuration layer
- Voter-facing outputs (sample ballots, polling-place lookup, results pages) produced by adjacent modules/products

### L3 — Vendor-specific (research notes only)

- Hart: Verity/Vanguard/Workspace/Boost/Flex/Vault/VotePass naming; "first VVSG 2.0 EAC certified voting system"; "only voting system" EO-14248 claims; "80% of switchers" survey claim; "smallest platform on the market."
- Clear Ballot: ClearDesign/ClearCount/ClearMark/ClearCast Go/ClearAccess/VerifyNow/PrintNow/Marathon/Nexus naming; "nation's first browser-based central count"; Fujitsu/ibml scanner integrations; "more than ten years" VBM claim; tabulate-other-vendors'-ballots claim for VerifyNow.
- KNOWiNK: Total Vote/Poll Print/Poll Pad/ePulse naming; "first-in-the-nation EAC certified poll book"; "35 to 40 seconds" check-in claim; "36 million voters across 29 states / 1 in 4" claim; "61% of jurisdictions" claim; flat-fee pricing posture; Nevada/Georgia Secretary of State endorsements.
- None of these numbers or claims are asserted in the final document.

## Historical / Market-Sample Check

- Paper-era election administration (election notice, candidate qualification, ballot layout & printing, poll books, precinct organization) satisfies the L0 structures without any modern feature → definition survives.
- All-mail jurisdictions (Oregon/Washington counties are named Clear Ballot customers) use the same definition/production structures without polling-place administration → confirms polling logistics is not definitional.
- US decentralized county model vs hypothetical centralized national authority: both define elections, map geography to ballot styles, and produce ballots; only the scale and who operates differ → definitional robustness across government models.
- The two largest vendors were unreachable; the historical check therefore leans on the three reachable products plus reasoning. Confidence: adequate for the L0 model, lower for fine-grained L1 breadth (e.g., exact candidate-filing machinery, legal-notice calendars — flagged in Uncertainties).

## Boundary Findings

- **vs Voter Registration System:** VR maintains the voter roll (identity, eligibility, registration lifecycle). EMS defines the election and produces ballots. Interlock: precinct/district assignment on the roll determines ballot style (KNOWiNK states this explicitly). One vendor sells both in one suite (Total Vote) — the seam is real but commercially co-packaged. Test: if the product's world is voter records/roll lifecycle, it's VR; if it's election events, ballot styles, and ballot production, it's EMS.
- **vs Election Results Management:** results management = tabulation, reconciliation, canvass, certification, public reporting. EMS = everything needed to make voting possible (definition → styles → votable artifacts → configured processes). The boundary blurs in-market: Clear Ballot labels its central-count tabulation product under "Election Management"; vendors ship both halves in one family; the EAC/ESTEP treats "election night reporting systems" as a separate technology family. Recorded as a Boundary Issue.
- **vs Event Management Platform:** superficial structural resemblance (dated occasion, venues, staff, materials). EMS is defined by contests/ballot styles/jurisdiction-legal ballots and produces votable artifacts under election law; no attendee registration, tickets, or program agenda. Remove ballot production and election-legal semantics → an EMS fragment collapses into generic event planning.
- **vs Jury Management System:** both process citizen lists for civic duty. Jury = court process (summons, qualification, panels); no ballots, no election geography.
- **vs online-voting / e-voting platforms:** those are casting-side systems (ballot delivery to voters + vote collection); they may include ballot definition but are not the election authority's management system of record for the whole election. Adjacent, not the same Type.
- **vs Government Service Portal / voter-facing surfaces:** sample ballots, polling-place lookup, and results pages are outputs of adjacent modules (voter education/outreach; election night reporting), not the EMS itself.

## Uncertainties

1. Candidate filing/qualification machinery: commonly associated with election administration, but no fetched page documents it directly (only KNOWiNK's "manages voter, candidate and all election information" hints). Kept out of L1 details; mentioned as common function with qualified wording in the final doc.
2. Election-calendar/task-management depth (legal deadlines, notice periods): expected in the Type, not directly evidenced on fetched pages. Qualified wording only.
3. Exact scope split between EMS and e-pollbook systems: e-pollbooks are a separate certified technology family (ESTEP evidence) but interact heavily with EMS output (ballot styles, precincts). Treated as adjacent, not variant.
4. Non-US regional realizations (UK halarose-style electoral services software; national election commissions): unreachable; regional variant description is reasoned, not sourced.
5. Dominion/ES&S EMS specifics: market context only; the final document does not describe their features.

## Final Synthesis

An Election Management System is the election authority's system of record for preparing an election: it holds the election definition (date, jurisdiction scope, contests, candidates/measures), maps election geography to ballot styles, and produces the votable artifacts and device/polling configuration that the casting and counting processes consume. Its defining trio — election definition, geography→ballot-style mapping, ballot production — is stable across paper-era, all-mail, and machine-voting realizations. Around that trio, mature products add proofing, role/audit governance, printing management (increasingly on-demand), by-mail support, election-worker support, and tight family coupling with tabulation. The market's dominant US realization embeds the EMS inside a certified voting system; a second realization packages it with voter registration and results reporting in a broader administration suite. Sibling Types hold: Voter Registration System (the roll), Election Results Management (the count), with the EMS boundary drawn at "makes voting possible" vs "counts what was voted."
