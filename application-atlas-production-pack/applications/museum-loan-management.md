# Museum Loan Management

## Overview

A **Museum Loan Management** system is the museum's loan-agreement system of record: it turns the borrowing and lending of collection objects between institutions — and from private lenders — into a managed, accountable transaction. It holds the loan record that binds the two parties, the specific objects, and the agreed terms; it tracks the loan's progression from request through approval, dispatch, and receipt to return or renewal and closure; and it holds the loan's obligations — fixed period, care standards, insurance or indemnity, condition documentation at handovers — as checkable states with the supporting documents attached.

The defining problem it solves is accountability across a custody boundary: an object leaves the institution's direct control but remains its responsibility (when lending) or enters its care under borrowed terms (when borrowing). The loan record is the formal structure that makes that arrangement inspectable — before the object travels, while it is away, and after it comes back.

The defining core is deliberately small:

```text
Loan agreement of record
├── Parties (lender × borrower) — ownership retained by the lender
├── Specific identified objects
├── Agreed terms (purpose, fixed period, care and insurance obligations)
├── Request-to-return progression (tracked status on the record)
└── Obligation and evidence layer (documents attached, written record retained)
```

Everything else commonly associated with loan work — document templates, shipping coordination, exhibition linkage, loan registers — is standard capability of mature products, and a few refinements (such as confidentiality controls over lender identities) appear only in some products; none of it is what makes the system a loan-management system. A paper loan file — signed agreement, insurance documentation, condition reports, correspondence, filed by loan number — satisfies the same structure; the domain standard for this practice explicitly allows paper-based systems.

Both directions are the same structure mirrored: lending out and borrowing in are held as parallel record families in the same system, and the museum plays the opposite party in each. Loans are not financial lending — no money changes hands as the subject of the record; the subject matter is always specific identified objects whose ownership never transfers.

## Users & Context

Primary users are the museum staff who own and execute loan transactions:

- **Registrar** — the customary owner of loan work: receives and assesses incoming requests, prepares outgoing loan proposals, negotiates and records terms, tracks statuses and deadlines, and keeps the loan file complete for governance, insurers, and auditors.
- **Authorising roles (director, head of collections)** — under institutional policy, loan agreements carry a named authorisation step; policy determines who may commit the museum to lend or borrow.
- **Curator** — initiates borrowing proposals for exhibitions, research, and other projects, and nominates objects to lend; consults loan status when planning what can be where.
- **Collections manager** — prepares objects for dispatch, updates locations as borrowed objects arrive and depart, and keeps the physical picture reconciled with the loan record.
- **Conservator** — produces the condition documentation the agreement requires at release and return.

The work is inherently two-sided: every record has a counterparty institution or individual on the other end. Much of the workflow is correspondence-bound (requests, agreement drafts, confirmations), with the loan record holding the authoritative state while documents move between parties. The governing context is the institution's loan policy — why it lends and borrows, whom it lends to, minimum and maximum loan lengths, notice periods, who may authorise, and its standard terms and conditions.

## Core Model

### The loan record

The unit of the system is the **loan record** — one persistent, identified record per loan, serving as the primary record for managing the transaction through its whole lifecycle. It binds:

- **The parties** — the lender and the borrower, held as people/organisation records. Ownership stays with the lender throughout; the borrower holds custody for the agreed period. This is what separates a loan from an acquisition (title never passes) and from disposal (the object is expected back).
- **The objects** — the specific identified objects the agreement covers, linked to their object records. The loan appears in each object's history, and borrowed objects live in the same system under their loan records, clearly distinct from owned collection.
- **The terms** — the stated purpose of the loan, the fixed period with start and end dates, the care standards the borrower agrees to meet, and the insurance or indemnity arrangement.

### Two directions, one structure

The same record structure serves both directions, typed accordingly:

- **Loan out (lending)** — the museum's objects travel to a borrower; the museum assesses the request, sets terms, and expects return.
- **Loan in (borrowing)** — objects from a lender enter the museum's care; the museum signs the agreement, assumes the care and insurance obligations, and owes the lender accountability for the objects' whereabouts and wellbeing.

### The progression

A loan advances through stages held as tracked status on the record. A typical modern implementation runs: **request → assessment and approval → agreement → dispatch and receipt → display or use → return or renewal → closure**. The status, the dates, and the deadlines live on the loan record, so at any moment the institution can answer what is where, on whose authority, until when, and what remains to be done.

### The obligation and evidence layer

The agreement's obligations are held as checkable states, and the transaction's paperwork accumulates on the record:

- the **written agreement**, signed by both parties before the loan begins
- **insurance or indemnity documentation**, covering the objects while in the borrower's care and in transit
- **condition documentation** at the handover points (release and return)
- **shipping records** and transport details
- **correspondence** between the parties

The completed loan record is retained — it is consultable if a problem surfaces after the object has gone home, and a loan's use of an object forms part of that object's recorded history.

### Standard capabilities

Mature products commonly add:

- both directions in one system, as parallel record families
- document attachment against the loan record
- linkage from loans to the exhibitions they support
- loan registers and reports for governance, insurers, and audits
- status-and-deadline tracking with renewal handling

## How It Works

### Lending an object out

```text
Request arrives from a borrower
→ assess against loan policy (who may borrow, is the object lendable, notice, purpose)
→ approve or decline
→ agree terms: purpose, dates, care standards, insurance, transport, condition requirements
→ written agreement signed by both parties
→ condition-check and dispatch the object
→ track the loan while it is away (status, dates, deadlines)
→ object returns → condition-check on return
→ confirm return and close the loan — or renew for a further fixed period
```

The museum's leverage over the whole transaction is the agreement: nothing ships before it is signed, and the care standards written into it are what the borrower has committed to.

### Borrowing an object in

```text
Proposal to borrow for a stated purpose (exhibition, research, other)
→ approve under policy (including provenance checks on the offered loan)
→ agree terms with the lender and sign the agreement
→ receive the object; record its arrival condition and location
→ hold it in care: keep its location and physical wellbeing up to date
→ return the object at the end date — or renew for a further fixed period
→ close the loan
```

While the object is in the museum's care, the loan record carries the borrower-side accountability: where the object is, how it is housed and displayed, and the environmental conditions in which it is kept — information lenders are entitled to.

### Renewal and the end date

Every loan has an end date. At the end date the loan either closes with the object's return or is renewed for a further fixed period. Long-running loans are reviewed at intervals rather than left to drift.

### Core vs standard vs optional

- **Defining core** — the loan agreement of record (parties, objects, terms, retained ownership); the tracked request-to-return progression; the obligation-and-evidence layer with the written record retained.
- **Standard capabilities** — both directions in one system, document attachment, exhibition linkage, registers and reports, deadline tracking, request-state visibility, lender confidentiality.
- **Optional / variant** — the insurance mechanism (commercial insurance or indemnity schemes), loan duration postures, touring-exhibition reuse of one agreement across venues, the depth of transport coordination held on the record versus delegated to a logistics layer, request-state visibility when checking whether an object is already promised elsewhere (supported in some products), and confidentiality controls over lender identities where lenders wish to remain anonymous (supported in some products).

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Loan list / register

The working surface over all loans.

- Typical information: loans in and out with parties, status, key dates, and outstanding deadlines; filters by direction, status, or date
- Primary actions: create a loan (in or out), open a loan, update status, generate registers and reports

### Loan record detail

The hub surface — one screen per loan.

- Typical information: parties, linked objects, purpose, start and end dates, current stage, care and insurance terms, attached documents, linked exhibition, status history
- Primary actions: edit terms, update status, attach documents, associate objects, link an exhibition, record return, renew, close

### Document attachments

The evidence surface of the loan.

- Typical information: the agreement, insurance or indemnity documents, shipping records, condition reports, correspondence, photographs
- Primary actions: attach, organize, retrieve

### Object-record loan panel

The loan picture as seen from the object.

- Typical information: the object's loan history — where it has been, on whose authority, when it went and came back; current loan status
- Primary actions: associate the object with a loan, navigate to the loan record

### Exhibition linkage

Where loans support an exhibition, the loan connects to that exhibition's record, so staff can see which loans underpin which display and navigate between the records.

### Reports and registers

The accountability surface: loan registers by period, direction, or status, and the per-object loan history used for governance, insurance, and audit purposes.

## Important Rules / Behaviors

**All loans are for fixed periods.** Every loan carries an end date; at the end date the object is returned or the loan is renewed. The domain standard is explicit that there should be no "permanent loans" — long-held loans are to be renewed for fixed periods, acquired, or returned — and warns that the loan procedure must not be used as a backdoor way to dispose of objects. Ownership retention plus a fixed period is what keeps a loan from silently becoming something else.

**Nothing moves before the agreement is signed.** The written agreement — signed by both parties, referencing the care standards the borrower will meet and the other terms — exists before the loan begins. This is the formal record of what was agreed if problems arise during or after the loan.

**Insurance or indemnity follows custody, including transit.** Whichever direction the object travels, the party holding it in care carries the coverage obligation, and the coverage must not lapse while the object is being transported.

**Condition documentation marks the handovers.** The object's physical state is documented at release and again at return, so responsibility for any change can be located in time and the agreement's care standards can be checked against evidence.

**The borrower owes the lender accountability.** While objects are in the borrower's care, their location and physical wellbeing are kept up to date on the record, including the environmental conditions in which they are displayed — information the lender can be given.

**The stated purpose bounds the use.** The reason for each loan is recorded, and the borrowed objects are not used beyond the purpose agreed with the other party.

**Authorisation is a named step.** Policy determines who may authorise the museum's loan agreements in either direction; requests are assessed against that policy consistently.

**Loan records accumulate and persist.** A written record of every loan is kept and retained after closure; an object's loan history becomes part of its documented history, consultable if a problem becomes apparent after the object has left the borrower's care.

**Lender identities can be confidential.** Some lenders wish to remain anonymous; some products restrict access to their names on loan-related records by role.

**Borrowed objects are not owned objects.** Objects on loan in live in the same system as the collection but under loan semantics, clearly distinct from owned collection — conflating the two is a named failure the record structure exists to prevent.

## Variants

- **Short-term exhibition loans vs long-term display loans** — the same agreement structure at different durations; long-running loans reviewed at intervals and regularized to fixed periods.
- **Lender mix** — institution-to-institution lending and borrowing alongside loans from private collectors, galleries, and individuals.
- **Purpose mix** — loans for exhibitions, research projects, conservation evaluation, and educational use; the loan is not exhibition-bound even though exhibitions are the most common driver.
- **Touring exhibitions** — one agreement structure repeated across the venues an exhibition travels to.
- **Insurance mechanism** — commercial insurance or public indemnity schemes, varying by jurisdiction; the obligation to cover the object is constant, the mechanism is regional.
- **Packaging** — the same structure ships as a named loans module in enterprise suites, as a contracts module covering loans among other agreements, as dedicated loan-in/loan-out record profiles in cloud products for small institutions, and as a data-model record type in open-source systems. No standalone dedicated museum-loan product was found in the researched sample; the capability lives inside museum collection systems.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Museum Collections Management | container | the collection register, object records, locations, and the custody-event layer as a whole; the loan workflow runs on its object records as one event family |
| Museum Condition Reporting | interlock | condition owns the assessment discipline; the loan requires condition documentation at release and return but does not constitute it |
| Museum Conservation Management | interlock | loans prompt treatment (borrowed objects need owner consent for work); the loan owns the transaction, conservation owns the work |
| Artwork Exhibition Logistics | downstream executor | the physical movement chain (packing, transport, custody handovers) that the loan agreement authorizes and bounds; commonly sibling modules of one system |
| Exhibition Planning Platform | upstream consumer | planning consults loan status when selecting objects but does not constitute the agreements |
| Exhibition Installation Management | adjacent | the venue-side in/out install state of borrowed and owned works; the loan is the agreement layer behind the borrowed ones |
| Museum Object Movement Management | sibling workflow | movement records track physical relocation for any reason; the loan record is the legal agreement that authorizes and bounds the object's absence — separate record types in the same systems |
| Artwork Consignment Management | custody without commerce | both place specific objects at external locations under retained ownership; consignment carries commercial terms and a sold/returned settlement, a loan does not — its terminus is return, not sale |
| Contract Lifecycle Management | name-adjacent | CLM manages commercial contracts generically; here the agreement's subject matter is specific collection objects and its obligations are collections-care obligations |
| Loan Management System (financial) | name collision only | financial lending (money, repayment, credit) — a completely different object world despite the shared word "loan" |
| Art Gallery Management | commercial neighbor | galleries move stock commercially (sale, consignment settlement); museums lend objects under non-commercial return obligations |

## Representative Products

- **TMS Collections** (Gallery Systems) — enterprise incumbent with loan management as a named core capability, supporting both standard loan procedures; deep documentation is client-gated
- **MuseumPlus** (Zetcom) — European incumbent handling loan agreements within its contracts module alongside exhibitions and collection objects
- **CatalogIt** (It Unlimited) — cloud-native system for small museums and historic houses with dedicated loan-in and loan-out record profiles
- **CollectiveAccess** (Whirl-i-Gig) — open-source, self-hosted collections management with loans as a first-class record type
- **Argus** (Lucidea) — mid-tier collections management system with loans among its curation workflows and per-object loan history

The definition was checked against the domain standard (Spectrum, the UK museum collections-management standard used internationally, which treats lending and borrowing as primary procedures and explicitly allows paper-based systems) and against the sibling leaves already documented in this atlas.

## Sources

Research date: **2026-09-08**

- Collections Trust — Spectrum 5.1, Loans out (lending objects): procedure and standard: https://collectionstrust.org.uk/spectrum/primary-procedures/loans-out-spectrum-5-0-primary-procedures/ , https://collectionstrust.org.uk/resource/loans-out-lending-objects-the-spectrum-standard/
- Collections Trust — Spectrum 5.1, Loans in (borrowing objects): procedure and standard: https://collectionstrust.org.uk/spectrum/primary-procedures/loans-in-spectrum-5-0-primary-procedures/ , https://collectionstrust.org.uk/resource/loans-in-borrowing-objects-the-spectrum-standard/
- CatalogIt Help Center — Managing Loans: https://catalogit.helpjuice.com/en_US/museum-practices/managing-loans
- CollectiveAccess documentation — data model, Loans (ca_loans) and Movements (ca_movements): https://manual.collectiveaccess.org/
- Zetcom — MuseumPlus (Contracts; Exhibition Management): https://www.zetcom.com/en/museumplus-en/
- Gallery Systems — TMS Collections; Software for Registrars: https://www.gallerysystems.com/solutions/collections-management/ , https://www.gallerysystems.com/roles/software-for-registrars/
- Collections Trust software directory — TMS Collections and eMuseum: https://collectionstrust.org.uk/software/tms/
- Lucidea — Argus: https://www.lucidea.com/argus/

> Sourcing limitation: deep operational documentation for the enterprise incumbents (TMS Collections, MuseumPlus) is login-gated; observations for them rest on product pages, the neutral Collections Trust software directory, and sibling-pass evidence, with no screen-level claims. eHive was unreachable from the research environment and was dropped. Exact stage names and product-specific machinery are deliberately not asserted in this document; detailed evidence is recorded in the paired Research Notes.
