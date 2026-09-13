# Research Notes — Museum Loan Management

## Research Goal

Understand what "Museum Loan Management" software actually is from real products and the domain standard: what the loan record is, what workflow it structures, what obligations it tracks, who uses it, and where its boundaries sit against the already-processed §27 siblings (Museum Collections Management, Museum Condition Reporting, Museum Conservation Management, Exhibition Planning Platform, Artwork Exhibition Logistics, Exhibition Installation Management, Artwork Consignment Management) and the unprocessed Museum Object Movement Management.

## Initial Boundary

Hypothesis before research: museum loans are the borrowing/lending of objects between institutions (and from private lenders) for exhibitions, research, or other purposes; loan management is the agreement/transaction layer — requests, approvals, terms, insurance, condition requirements, dispatch, return — distinct from the physical movement layer (logistics) and the assessment layer (condition reporting). The directory also contains financial "Loan Management System" (§08) — a name collision to be kept clearly separate.

Known counterparty positions from prior passes (all to be discharged or confirmed by this pass):

- museum-collections-management: loans in/out are one custody-event family ("Use" events) hosted on the container's object records; this leaf owns the workflow's internal structure.
- museum-condition-reporting: "loans require condition documentation at release/return — loan owns the transaction, condition owns the assessment... loan pass should treat this document as counterparty."
- artwork-consignment-management: "both track custody of specific objects at external locations, but loans carry no commercial split and no sale disposition... Remove the commercial terms and settlement → loan management remains."
- artwork-exhibition-logistics / exhibition-installation-management / exhibition-planning-platform: the loan agreement layer (requests, approvals, terms, returns) is a sibling record type in the same systems; planning consumes loan status at selection; logistics executes the movement the agreements trigger. All three flagged joint review with this leaf.
- museum-conservation-management: loans prompt treatment (consent needed for work on borrowed objects); loan owns the transaction, conservation owns the work.

## Research Questions

1. What is the unit of record — is the loan its own record type, or a field on the object?
2. What lifecycle does a loan move through (request → ? → return)?
3. What obligations does the loan structure (period, care standards, insurance, condition, transport)?
4. Are both directions (lending out / borrowing in) supported in the same system?
5. How does the loan record connect to object records, exhibitions, people (lenders/borrowers)?
6. Is there any standalone dedicated loan product, or does the structure ship inside museum collection systems?
7. What does the domain standard (Spectrum) require, and would older/paper-era practice still fit the definition?
8. Where exactly are the seams: condition reporting, movement, logistics, planning, consignment, financial lending?

## Representative Products

Selected for market representativeness, documentation reachability, and tier spread:

1. **TMS Collections** (Gallery Systems) — enterprise incumbent; loan management named as a core design purpose; deep docs login-gated (consistent with sibling passes).
2. **MuseumPlus** (Zetcom) — European incumbent; loans handled in its Contracts module.
3. **CatalogIt** (It Unlimited) — cloud-native for small museums/historic houses; dedicated Loan In / Loan Out profiles with a full operational help article (best reachable operational documentation in the sample).
4. **CollectiveAccess** (Whirl-i-Gig) — open-source, self-hosted; loans as a primary data-model record type (ca_loans), documented in the official manual.
5. **Lucidea Argus** — mid-tier CMS; loans named among curation tasks and object history.

Domain standard baseline: **Spectrum 5.1** (Collections Trust) — "Loans in (borrowing objects)" and "Loans out (lending objects)" are both **primary procedures** (accreditation-relevant), each with policy questions and minimum requirements.

Rejected/abandoned: eHive (ehive.com returned empty twice — abandoned per network rule); Axiell, Vernon CMS, PastPerfect (unreachable in prior sibling passes; not retried).

## Sources

- Spectrum 5.1 — Loans out (lending objects): procedure page + the Spectrum standard (minimum requirements): https://collectionstrust.org.uk/spectrum/primary-procedures/loans-out-spectrum-5-0-primary-procedures/ , https://collectionstrust.org.uk/resource/loans-out-lending-objects-the-spectrum-standard/
- Spectrum 5.1 — Loans in (borrowing objects): procedure page + the Spectrum standard: https://collectionstrust.org.uk/spectrum/primary-procedures/loans-in-spectrum-5-0-primary-procedures/ , https://collectionstrust.org.uk/resource/loans-in-borrowing-objects-the-spectrum-standard/
- CatalogIt Help Center — "Managing Loans" (operational article, last published 2026-08-05): https://catalogit.helpjuice.com/en_US/museum-practices/managing-loans
- CollectiveAccess Manual (GitHub source, official) — data modelling, primary tables: ca_loans, ca_movements: https://manual.collectiveaccess.org/ , https://raw.githubusercontent.com/collectiveaccess/CollectiveAccessManual/main/providence/user/dataModelling/primaryTables.md
- Zetcom — MuseumPlus product page (Contracts / Exhibition Management module descriptions): https://www.zetcom.com/en/museumplus-en/
- Gallery Systems — TMS Collections product page + Software for Registrars role page: https://www.gallerysystems.com/solutions/collections-management/ , https://www.gallerysystems.com/roles/software-for-registrars/
- Collections Trust software directory — "TMS Collections and eMuseum" entry (Spectrum procedures supported, lender-anonymity access control): https://collectionstrust.org.uk/software/tms/
- Lucidea — Argus product page: https://www.lucidea.com/argus/

Research date: 2026-09-08.

## Product Observations

### Spectrum 5.1 — Loans out (lending objects) [Layer A — domain standard]

Scope: "Assessing requests for you to lend your objects and managing the lending process until loans are returned to you." "Use this procedure to assess and manage requests for you to lend objects for an exhibition or any other reason."

Policy questions the museum must answer: why lend; who may borrow; why refuse requests; objects not normally lent; minimum/maximum loan length; notice needed; **who can authorise the loan**; terms and conditions for lending.

Minimum requirements (verbatim clusters):

1. All loan requests assessed according to policy (fair and transparent).
2. The reason for each loan clearly stated (borrowers do not use objects beyond the agreed purpose).
3. **All loans are for fixed periods** — "It is clear to borrowers that loans are not 'permanent'. The loan procedure is not used unethically as a backdoor way to dispose of objects."
4. **A written agreement signed by lender and borrower before any loan begins**, with clear reference to the care standards the borrower agrees to meet and other terms and conditions — "a formal record of what was agreed in case any problems arise."
5. **Borrowers have appropriate insurance or indemnity** for the objects while in their care, including in transit.
6. **A written record of all loans is kept** — the loan file consultable if a problem arises after return; "Use of your collections by borrowers forms part of the recorded history of objects."

### Spectrum 5.1 — Loans in (borrowing objects) [Layer A — domain standard]

Scope: "Managing objects you borrow for a fixed period of time and for a specific purpose." "Such loans should always have an end date. At the end date, you either renew the loan for a further fixed period or return the object to its owner. **There should be no 'permanent loans'** in your museum; if there are from years past you should renew them for a fixed period, try to acquire the objects, or return them."

Policy questions: why borrow; legal/ethical checks before borrowing; min/max loan period; **who can authorise loan agreements**; provenance checks on potential loans; **how to deal with borrowed objects if the original lender can no longer be contacted**.

Minimum requirements:

1. Written agreement signed by borrower and lender before the loan begins, with care standards and T&Cs.
2. Reason for each loan clearly stated.
3. All loans fixed periods — "You can review longer-term loans at regular intervals. You do not create a future backlog of objects whose ownership status is unclear."
4. Insurance or indemnity cover for borrowed objects while in the borrower's responsibility, including transit.
5. **Up-to-date information about the location and physical wellbeing of borrowed objects during the loan** — "You can give lenders data on the environmental conditions in which their objects are displayed."
6. Written record of all loans kept — loan file consultable after the object leaves the borrower's care.

### CatalogIt — "Managing Loans" [Layer A — operational help article]

- Dedicated **Loan In** and **Loan Out profiles**; "manage every stage of a loan, from **initial request and approval through shipping, receipt, renewal, and return**."
- Loan In = "Objects borrowed from another individual or organization for exhibitions, research, evaluation, and other institutional purposes." Loan Out = "Objects from your collection that are lent to another institution or individual."
- Creating a loan: Profiles menu → Loan In or Loan Out → Create New Loan → enter loan details → attach supporting documentation ("loan agreements, correspondence, shipping records, condition reports, and more"). "The loan profile serves as the primary record for managing the loan throughout its lifecycle."
- Tracking: "Borrower or lender information; Loan status and dates; Shipping and insurance details; Related documentation; Associated exhibitions and objects." "As the loan progresses, update the status to reflect its current stage, from request and approval through return and closure."
- Link loans to exhibitions (Exhibition profile relationship — "which loans support a particular exhibition").
- Associate objects (entries) with the loan — "a clear connection between the loaned item, the loan agreement, and any associated exhibition."
- Documentation stored in one place: "agreements, insurance documents, correspondence, condition reports, photographs" — screenshot shows an attached "Outgoing Loan Agreement."
- Benefits: centralize documentation; track status and deadlines; connect loans to exhibitions and object records; "maintain accurate records for reporting and audits."

### CollectiveAccess — ca_loans [Layer A — official data model]

- **Loans (ca_loans)** is a primary record type: "Loan records record details of both **incoming and outgoing loans** of objects. Loan records... can be used to track **all aspects of a loan, including dates, shipping, and insurance information**."
- Loan intrinsics: identifier (idno, under a configured numbering policy), **type** (from a configurable loan_types list — the in/out distinction is a record type value), status (workflow status), labels; fully customizable.
- **Movements (ca_movements)** is a separate record type: "movement of objects between storage locations, **while on loan or while on exhibition**" — i.e., the physical movement event is distinct from the loan agreement record.
- Loans relate to objects through the relational model (objects ↔ loans relationships).

### MuseumPlus (Zetcom) [Layer A module description — product page]

- **Contracts** module: "Management of agreements and contracts relating to **exhibitions, loans and collection objects**."
- **Exhibition Management** module: "Coordination of participants, venues and **lenders**, as well as input and output protocols."
- SaaS or in-house deployment; 900+ museum clients.

### TMS Collections (Gallery Systems) [Layer A/B — neutral directory + product pages]

- Collections Trust software directory: "designed specifically for collections, content, media, exhibition, and **loan management**"; "comprised of 11 interrelated modules."
- Directory lists supported Spectrum procedures including **"Loans In - borrowing objects (primary)"** and **"Loans Out - lending objects (primary)"** — the vendor claims conformance to both loan procedures.
- Special feature: "Control access to the names of **lenders and donors, who wish to remain anonymous**, by individual user account" — lender confidentiality is an access-control surface on loan-related records.
- Registrar role page: manage exhibitions "with up-to-date data on object storage, insurance policies, and shipping status"; share reports "with partnering museums and art handlers."
- Sibling-pass evidence (exhibition-planning-platform pass, TMS): prior-request status is visible before filing a loan — request state is tracked and consultable at selection time.
- Deep operational docs are login-gated (community.gallerysystems.com) — no screen-level claims made.

### Lucidea Argus [Layer B — product page]

- "Handle **accessions, loans**, and related files with ease using a single system"; "handle annotations, accessioning, circulation, **loans**, and other curation tasks."
- "See the history of each object (including accessions, **loans**, and exhibits)" — loans appear in the per-object history picture.
- Spectrum Partner (standards alignment claimed).

## Cross-product Comparison

| Structure | Spectrum (standard) | CatalogIt | CollectiveAccess | MuseumPlus | TMS Collections | Argus |
|---|---|---|---|---|---|---|
| Loan as own record/agreement unit | written agreement + written record of all loans | Loan In/Loan Out profiles ("primary record") | ca_loans primary table | Contracts module (agreements re: loans) | loan management core; 11 modules | loans as curation task family |
| In/out directions as one structure | two mirrored procedures | Loan In + Loan Out profiles | incoming + outgoing types (loan_types) | agreements re: loans (both directions implied) | Spectrum Loans In + Loans Out both supported | loans (direction not split on page) |
| Request → approval stage | "assess requests according to policy"; who can authorise | "initial request and approval" stage; status through "request and approval" | — (configurable) | — | prior-request status visible before filing (sibling pass) | — |
| Fixed period + end date + renewal | "all loans are for fixed periods"; renew or return at end date | "renewal" named stage; "track loan status and deadlines" | dates tracked | — | — | — |
| Agreement document | written signed agreement before loan begins | attach "loan agreements" / "Outgoing Loan Agreement" | customizable record | Contracts = agreements | — | — |
| Insurance / indemnity on the loan | minimum requirement both directions | "shipping and insurance details" tracked | "insurance information" on loan record | — | insurance policies (registrar page) | — |
| Shipping / transport on the loan | cover "including in transit" | "shipping records"; shipping details | "shipping" on loan record | — | shipping status (registrar page) | — |
| Condition documentation at handover | care standards in agreement | attach "condition reports" | — | — | — | — |
| Objects linked to the loan | objects are the subject of the agreement | associate entries with loan | objects ↔ loans relationships | objects in contracts | object records | object history includes loans |
| Exhibition linkage | loans "for an exhibition or any other reason" | link loan ↔ Exhibition profile | — | contracts re: exhibitions | exhibitions + loans modules | — |
| Written record retained / part of object history | "written record of all loans"; "forms part of the recorded history of objects" | "accurate records for reporting and audits" | persistent record type | — | — | per-object history incl. loans |
| Lender confidentiality | policy-level (who may borrow; refusal) | — | access flags on records | — | lender-name access control by user account | — |
| Borrowed-object accountability while in care | up-to-date location + physical wellbeing; environmental data to lenders | — | — | — | — | — |

Reading: every sampled system holds the loan as its own record/agreement unit typed by direction, tracks its progression and dates, and attaches or references the agreement's supporting documents (agreement, insurance, shipping, condition). The standard requires exactly this structure at minimum. No sampled product treats a loan as merely an object field.

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures:

1. **The loan agreement of record** — a persistent, identified record binding the two parties (lender and borrower), the specific identified objects, and the agreed terms (stated purpose, fixed period with end date, care and insurance obligations), with **ownership retained by the lender** and custody temporarily transferred. Remove → object records and correspondence, but no loan to manage.
2. **The request-to-return progression** — the loan advances through tracked stages (request/assessment → approval → agreement → dispatch and receipt → return or renewal → closure), with current status held on the record. Remove → a filed contract with no managed workflow.
3. **The obligation-and-evidence layer** — the agreement's obligations (fixed period, care standards, insurance or indemnity including transit, condition documentation at handovers) held as checkable states with supporting documents attached to the record, and the loan's written record retained as part of the objects' history. Remove → an informal arrangement; the accountability purpose collapses.

Jointly-held load-bearing: 1 alone = a signed contract in a filing cabinet; 2 without 1 = generic task tracking; 3 without 1+2 = a checklist with no transaction; 1+2 without 3 = a tracker with no accountability structure.

Historical check (§24): a paper-era loan file — a signed paper agreement held by both parties, insurance documentation, condition reports at dispatch and return, correspondence, filed by loan number and consultable after return — satisfies all three legs. Spectrum itself allows paper-based systems. The definition names no software surface, no cloud, no digital signature machinery. Older and regional practice (long-held "permanent" loans) still fits the record structure — the standard's fixed-period rule is a policy posture on top of the same record, not a structural difference.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Both directions in one system (Loan In + Loan Out as parallel record families).
- Object linkage: associating specific object records with the loan (and the loan appearing in each object's history).
- Exhibition linkage: connecting loans to the exhibition they support.
- Document attachment: agreements, insurance documents/certificates, shipping records, condition reports, correspondence, images.
- Status tracking with dates and deadlines; renewal handling.
- People/constituent records for lenders, borrowers, and contacts.
- Loan registers and reports (for governance, insurers, audits).
- Request-state visibility at selection time (observed on TMS via the exhibition-planning pass).
- Lender/donor confidentiality access control (observed on TMS).
- Shipping/transport details held on the loan record (execution itself belongs to the logistics layer).

### L2 — Variant / Optional Structure

- Loan duration posture: short-term exhibition loans vs long-term display loans (the standard pushes fixed periods with renewal; legacy "permanent loans" are a managed exception to be regularized).
- Lender mix: institution-to-institution vs loans in from private collectors, galleries, and individuals.
- Purpose mix: exhibition, research, conservation evaluation, education (CatalogIt and Spectrum both name several purposes — loans are not exhibition-bound).
- Touring exhibitions: one agreement structure repeated across venues.
- Insurance mechanism: commercial insurance vs indemnity schemes (the standard says "insurance or indemnity" without fixing the mechanism; national schemes vary by jurisdiction — not asserted further).
- Packaging: loans as a named module (TMS), a Contracts module (MuseumPlus), dedicated profiles (CatalogIt), a data-model record type (CollectiveAccess), or an undifferentiated curation task (Argus).

### L3 — Vendor-specific (Research Notes only)

- CatalogIt's profile-based implementation and its named stage sequence ("request and approval through shipping, receipt, renewal, and return").
- CollectiveAccess's ca_loans/ca_movements table split and configurable loan_types list.
- TMS's 11-module architecture, Registration menu, and lender-anonymity account control.
- MuseumPlus's "Contracts" module naming (covering exhibitions, loans, and collection objects).
- Argus's "circulation" vocabulary.

## Vendor-specific Findings

See L3. None of these were promoted to the canonical model. The CatalogIt stage vocabulary is the only directly observed end-to-end stage list in the sample; other products' stage names are not asserted.

## Boundary Findings

1. **vs Museum Collections Management (container, processed)** — loans in/out are one custody-event family ("Use" events) hosted on the container's object records; the container owns the register, the location picture, and the event layer as a whole; this leaf owns the loan workflow's internal structure (agreement, progression, obligations). Consistent with the containment precedent set by the accession-cataloging, condition, and conservation passes. Removal test: remove the loan workflow → the container stands (register + location + other events); remove the container → loan management has no object records to bind.
2. **vs Museum Condition Reporting (processed)** — DISCHARGES that pass's counterparty guidance from the loan side: loans *require* condition documentation at release and return (Spectrum care standards in the agreement; CatalogIt's condition-report attachments). The loan owns the agreement/transaction lifecycle; condition owns the assessment discipline. Removal tests: remove condition reports → loan management stands with a liability gap at handovers; remove loans → condition reporting remains (transit, storage surveys, treatment baselines, intake). Verdict: distinct, clean seam.
3. **vs Museum Conservation Management (processed)** — loans prompt treatment (borrowed objects require owner consent for work); the loan owns the transaction, conservation owns the work. Confirmed from the loan side.
4. **vs Artwork Exhibition Logistics (processed)** — the agreement layer (requests, approvals, terms, return obligations) vs the physical movement chain. Every sampled system ships them as sibling structures (TMS Loans vs Shipping/Exhibitions; MuseumPlus Contracts vs Exhibition Management; CollectiveAccess ca_loans vs ca_movements). Remove the movement chain → loan management remains; remove the agreement terms → logistics remains. Confirms that pass's flag from the loan side.
5. **vs Exhibition Planning Platform (processed)** — planning *consumes* loan status during selection (prior-request visibility) but does not constitute the agreement machinery; the loan record is the agreement of record. Confirms that pass's boundary from the loan side.
6. **vs Exhibition Installation Management (processed)** — install state (in/out of the display context) vs the agreement layer that usually triggers the install. Sibling modules in the same systems. Confirms that pass's flag from the loan side.
7. **vs Artwork Consignment Management (processed)** — both track specific objects at external locations under retained ownership, but loans carry no commercial split, no sale disposition, and no settlement; the loan is defined by agreement terms + fixed period + return obligation. Remove the commercial terms and settlement → loan management remains. Confirms that pass's boundary from the loan side.
8. **vs Museum Object Movement Management (unprocessed sibling)** — movement records track physical relocation for any reason; loan records structure the legal agreement that authorizes and bounds the object's absence. CollectiveAccess models them as separate record types (ca_loans vs ca_movements — movements happen "while on loan or while on exhibition"); Spectrum keeps Loans in/out and Location and movement control as separate procedures. Expected clean seam; this pass leaves the counterparty guidance for that leaf.
9. **vs Contract Lifecycle Management (§11)** — CLM manages commercial contracts generically (parties, clauses, renewals, approvals). Museum loan management is object-anchored: the agreement's subject matter is specific identified collection objects, and its obligations are collections-care obligations (care standards, condition at handover, environmental data to lenders). MuseumPlus naming its loan module "Contracts" shows the vocabulary overlap, not a Type identity.
10. **vs Loan Management System / Loan Origination (§08)** — financial lending (money, repayment schedules, credit). Name collision only; completely different object world. The directory's "loan" family in §08 must not absorb this leaf.
11. **Packaging reality (load-bearing finding)** — in the reachable sample, **no standalone dedicated museum-loan product exists**: the loan structure ships as modules/profiles/record types inside museum collection systems (TMS Loans; MuseumPlus Contracts; CatalogIt Loan In/Out profiles; CollectiveAccess ca_loans; Argus loans tasks). Same pattern as the exhibition cluster's three passes. The Type stands on workflow structure, not suite packaging. Flagged for joint review consistent with the sibling flags.

## Uncertainties

- TMS Collections and MuseumPlus operational documentation is login-gated; observations for them rest on product pages, the neutral Collections Trust directory entry, and sibling-pass evidence — no screen-level claims made for either.
- eHive was unreachable (two empty fetches) and was dropped; Axiell, Vernon CMS, PastPerfect were unreachable in prior sibling passes and were not retried. The sample is therefore 5 products + the standard, weighted to systems with reachable documentation.
- Whether any standalone loan-request-portal product exists in the wider market could not be verified; absence in the reachable sample is not proof of absence market-wide.
- Exact stage vocabularies are product-local; only CatalogIt's stage list was directly observed end-to-end.
- Whether loan fees (lender fees, hire charges) are tracked as a standard capability was not directly observed in the reachable documentation and is deliberately not asserted.
- Facilities-report handling (a common museum loan practice) was not directly observed in the sampled documentation and is not asserted.

## Final Synthesis

Museum Loan Management is the museum's loan-agreement system of record: the structure that turns "may we borrow/lend this object?" into a managed, accountable transaction. Its defining core is three jointly-held structures — the loan agreement of record (parties × objects × terms, ownership retained), the request-to-return progression with tracked status, and the obligation-and-evidence layer (fixed period, care standards, insurance/indemnity, condition at handovers, retained written record). Both directions — lending out and borrowing in — are the same structure mirrored, and mature systems hold both. The structure ships inside museum collection systems rather than as a standalone product, and its seams are clean: condition reporting owns the assessment, logistics owns the movement, planning consumes the status, conservation owns the treatment, the container owns the object records — the loan owns the agreement and its lifecycle.
