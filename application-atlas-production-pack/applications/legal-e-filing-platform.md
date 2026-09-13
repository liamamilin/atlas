# Legal E-filing Platform

## Overview

A **Legal E-filing Platform** is a filer-facing application through which legal documents are submitted electronically to a court and tracked through the court's acceptance decision. It is the filer's side of the filing transaction: the platform assembles a filing, submits it into the court's system, conveys the clerk's accept/reject decision back to the filer, handles the fees the filing triggers, and returns the officially filed (file-stamped) copies.

It solves a specific operational problem: getting documents on file with a court is not a simple upload. A filing must be bound to the right case, name the right parties, use the court's own document classifications, satisfy court-specific formatting rules, carry the correct fees, and — decisively — it is not "filed" until a court clerk reviews and accepts it. Rejections are routine, and a rejected filing must be corrected and resubmitted without losing what was already accepted.

The boundary of the Type: the platform is filer-facing. The court's own case management system — the system of record that receives, reviews, and dockets filings — sits on the opposite side of the transaction and is a different Application Type. The platform is also not a document drafting tool (that happens upstream) and not a courier service (physical delivery is a peripheral channel, not the core).

## Users & Context

**Primary users:**

- **Attorneys** — the filer of record; filings are made on behalf of a represented party under the attorney's name.
- **Paralegals and legal assistants** — the hands-on daily users who prepare filings, attach documents, select document types, manage service contacts, and submit.
- **Firm administrators** — manage the firm account, payment methods, attorney and staff accounts, and reporting.

**Secondary users:**

- **Self-represented litigants (pro se)** — a distinct account tier in most products, with simplified flows and limited support; in many jurisdictions they are exempt from mandatory e-filing but encouraged to use it.
- **Support staff at the platform provider** — a first-class human layer; providers position live chat and phone support as a core differentiator because a failed filing can mean a missed deadline.

The work context is litigation practice under court deadlines. In a growing number of jurisdictions, e-filing is mandatory for attorneys in most case types, so the platform is not optional infrastructure — it is the only way to file. The accept/reject loop is high-stakes: a rejection consumes part of the time available before a deadline.

## Core Model

### The Defining Core

```text
Court case (existing, from court records — or new, initiated here)
└── Filing submission (documents + case/party context, one case per submission)
    └── Clerk adjudication loop
        ├── accepted → filed (file stamp, conformed copies returned)
        ├── partially accepted → accepted documents stay; rejected documents re-filed
        └── rejected → reasons conveyed back → correct → resubmit
```

Three structures, held together:

- **The filing submission** — the unit of work: one or more documents plus case and party context, submitted as a single transaction to one court case. A submission may contain multiple documents, but they must all pertain to the same case. The submission receives a confirmation number and an official receipt timestamp from the court. (Without the submission as a managed unit, the product is just document delivery.)
- **Case binding** — every submission is bound to a court case. Either the case already exists and is retrieved from the court's records by case number, or the filing initiates a new case by selecting the court and case type and supplying the parties in the roles the court requires. (Without case binding, the product is a generic government form submission.)
- **The clerk adjudication loop** — the submission crosses into the court's system and comes back with a decision: accepted, partially accepted, or rejected. The clerk's rejection reasons are conveyed back through the platform. Acceptance is what constitutes filing — the court's receipt timestamp becomes the official file stamp, and file-stamped copies flow back to the filer. Rejections feed a correct-and-resubmit loop. (Without this loop, the product is a one-way upload portal, and the filing semantics disappear.)

### Standard Capabilities

Mature products commonly add the following. They make the platform practical; they are not what makes it an e-filing platform.

- **Fee machinery** — the platform computes the fees a filing triggers (statutory court fees driven by case and document types, court technology fees, provider service fees, payment-processing costs, and in some jurisdictions sales tax), presents the itemized breakdown before submission, collects payment, and handles fee waivers as a distinct payment type. Payment is typically pre-authorized at submission and settled only on acceptance; rejected filings release the hold. Refunds and itemized receipts/invoicing round out the loop.
- **Filing status tracking** — a status screen listing every submission with its current state (pending, processing, accepted, partially accepted, rejected), searchable by submission number, case number, or internal matter reference, with printable receipts for accepted filings and email notifications at each transition.
- **Returned artifacts** — file-stamped documents and conformed copies delivered back to the filer once the court accepts.
- **Document preparation aids** — automatic conversion of word-processing and image files into the court-required PDF format (usually text-searchable), plus validation and warnings for conditions that would cause the court to reject the file.
- **Case-centric organization** — a case summary view (parties, judge assignment, register of filings) and a per-case history of filings, documents, and costs; some products organize everything by the firm's internal matter.
- **Service of documents** — electronic service to designated service contacts with delivery tracking (some products also show whether each served party has opened the documents), and paid physical mail service (certified or first class) as a complement. Process serving is a common adjacent bundle.
- **Organization accounts** — firm-level accounts with attorneys, staff, and support roles; client matter numbers carried on filings for internal cost tracking; party address books.
- **Court-specific rule encoding** — the court's document-type lists, formatting requirements, file-size limits, fee schedules, and procedural quirks, maintained by the provider as configuration and help content, often organized court by court.
- **Human support** — live chat, phone, and email support, plus per-court help libraries.

### One Structure, Many Implementations

```text
Concept:   Filing submission
Realized as: "filing envelope" (the term many courts use), an "order", a submission batch

Concept:   Case binding
Realized as: case-number retrieval from the court's system, case initiation,
             a firm-side case/matter portfolio linked to court cases

Concept:   Adjudication outcome
Realized as: status labels that vary by product and court
             (pending / processing / accepted / partially accepted / rejected)

Concept:   Fee settlement
Realized as: pay-per-submission, monthly invoicing, or provider-pays-then-invoices
```

A reader who has only seen one implementation — say, a law firm filing through a standalone provider — should still be able to recognize a state-run court portal or a practice-management suite with embedded filing as the same Type.

## How It Works

There are two fundamental flows, which share the same skeleton and differ only in how the case is established.

### File on an existing case

```text
Select the case (from the account's linked cases, or retrieve it
                 from the court's system by case number)
→ add documents (choose court-maintained document type,
                 enter the exact document title, upload files
                 — auto-converted to court-required PDF)
→ set per-document security and add any additional services or fees
→ confirm the filing party (the party the filing is made on behalf of)
→ add service contacts for electronic service and/or mail service
→ review the computed fee breakdown and choose a payment method
→ review everything and submit
→ submission crosses to the court; a confirmation number and
  receipt timestamp are issued
→ status: pending
→ clerk decision:
     accepted → file-stamped copies returned; fees settled
     partially accepted → accepted documents stay in the case;
                          rejected documents corrected and re-filed
     rejected → clerk's reasons displayed; correct and resubmit
```

### Initiate a new case

```text
Select the court and case type
→ add documents (the initiating pleadings)
→ enter the parties in the roles the court requires
   (with representing attorneys; unknown addresses permitted)
→ then the same skeleton as above: security, filing party,
   service contacts, fees, review, submit
```

A partially accepted case initiation is a special moment: the court has created the case, so the rejected remainder is re-filed as a subsequent filing on the now-existing case — the two flows hand off to each other.

### The rejection loop

Rejections are a designed-for state, not an exception path. The platform preserves everything entered in the rejected submission and lets the filer correct and resubmit without re-entering data. Two rules govern the loop:

- **Full rejection** — the entire submission was rejected; correct anything (party names, documents, fees) and resubmit the whole filing.
- **Partial rejection** — at least one document was accepted and at least one rejected. The accepted documents are already part of the case record; only the rejected documents are corrected and re-filed. Re-uploading the accepted documents would itself be rejected as duplicates.

Some products disable the resubmission path once a rejected filing has been successfully re-filed, to prevent accidental duplicates.

### The fee flow

Fees are computed from what the filing is, not entered by hand: the case type, the selected document types, and any additional services determine the amount. The filer reviews the itemized breakdown before submitting. Payment is pre-authorized at submission and finalized only when the filing is accepted; a rejection releases the hold. Court-approved fee waivers replace payment where applicable. Some providers pay court fees on the filer's behalf and invoice afterward; others bill per submission or invoice monthly.

### Service alongside filing

Electronic service is usually attached to the filing itself: the filer designates service contacts, and accepted documents are served to them, with delivery tracked per recipient (some products show whether each served party has opened the documents). Physical mail service (certified or first class) is a paid complement. Process serving — the formal service of summons and complaints — is commonly bundled as a separate but linked service with its own fulfillment tracking.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Dashboard

The entry surface. Primary actions: start a new-case filing, start a filing on an existing case, open the filing status screen. Often shows recent cases and filings.

### Filing workflow

A guided multi-step sequence (case → documents → security and services → parties → filing party → service contacts → fees → review and submit). Each step validates against the court's requirements; the fee step shows the itemized, court-computed breakdown; the final step requires an accuracy verification before submission.

### Filing status screen

The filer's worklist of submissions. Typical information: submission number, status, last change, case number, confirmation number, lead document. Primary actions: open a submission for detail, filter by status/case/matter, print receipts for accepted filings, and — after a rejection — re-enter the corrected filing. Service indicators show whether served parties have opened their documents.

### Case summary

The per-case view: case and party information, judge assignment, and a register of all filings on the case. Primary actions: view filings, start the next filing on the case.

### Account settings

Payment accounts and payment methods, attorney and staff user management, service contacts, party address books, client matter number policies, defaults (court, case type, screen).

### Notifications

Email at each transition: submission confirmation with the receipt timestamp, acceptance with file-stamped copies attached, rejection with the clerk's message, service receipts.

## Important Rules / Behaviors

- **A filing is not filed until the clerk accepts it.** The platform can only submit; the court's review is the constitutive act. The receipt timestamp issued at submission becomes the official file stamp if the filing is accepted. Submissions made after the court's cutoff — or on weekends and court holidays — commonly receive the next court business day as their file stamp; exact cutoffs vary by court.
- **Rejection reasons flow one way, from the court.** The clerk may attach a reason at the filing level or per document; the platform displays it but did not generate it. Sometimes no reason is provided at all, and the filer must contact the court directly, quoting the confirmation number.
- **Accepted content is immutable in the loop.** On partial rejection, accepted documents remain part of the case record and must not be resubmitted; only the rejected documents are corrected and re-filed.
- **Document types belong to the court.** The list of types is maintained by the court, and the filer — not the platform — is responsible for choosing the right one; the platform's role ends at presenting the court's list. The document description should be the document's exact title.
- **Security settings and service interact dangerously.** Documents carry a security level (commonly public or confidential, options vary by court). Electronic service sends *all* documents in the filing to *all* selected parties regardless of per-document security — a filer who wants a confidential document kept from a party must not e-serve that party.
- **Fees are the court's rules made arithmetic.** The computed fee set follows from case type, document types, and additional services; some fees are triggered automatically by document selection while others must be added by the filer's own knowledge. Incorrect document-type selection therefore produces incorrect fees.
- **Court-specific rules permeate everything.** Formatting requirements, file-size limits, field character limits, hearing-date procedures, courtesy-copy rules, and under-seal procedures all vary court by court; the platform encodes them as configuration and help content rather than as uniform product behavior.
- **Deadlines give the loop its urgency.** In mandatory-e-filing jurisdictions, a filing rejected late in the day may lose its filed-that-day status; providers staff live support precisely because a technical failure near a deadline is an emergency.

## Variants

- **Standalone e-filing service provider** — the dominant market form in US state courts: independent providers certified by courts or states, competing on price, usability, and support, often operating across many states with per-state configuration.
- **Court-technology-vendor provider** — the vendor that operates the court's back-end receiving system also operates a filer-facing service; the same company sits on both sides of the technical seam.
- **State-run single portal** — the state operates the filer-facing service itself (sometimes on vendor infrastructure); one official channel instead of a competitive market.
- **Practice-management-embedded filing** — law-firm practice-management suites deliver e-filing through an integration: case and client data flow from the suite into the filing order, and filed documents, service records, and expenses sync back to the firm's matter record.
- **Concierge / full-service filing** — a human-mediated pole where the provider's team prepares and submits filings (including physical filing for documents exempt from e-filing), blurring into litigation-support services.
- **User-tier variants** — firm accounts with unlimited users, solo-attorney accounts, and restricted self-represented-litigant accounts with limited support.
- **Service-bundle variants** — filing bundled with process serving, courtesy-copy delivery, court delivery, or document retrieval.

A variant remains a variant as long as the defining core — submission bound to a case, clerk adjudication loop — is intact. A product that loses the adjudication loop (one-way submission with no accept/reject semantics) has left the Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Court Case Management System | opposite side of the same transaction | court-side system of record that receives, reviews, and dockets filings; the e-filing platform is filer-facing and holds no authoritative case record |
| Court E-filing Platform | sibling directory leaf | the researched market has one filer-side category; this leaf is most plausibly the same Type framed from the government/court side — flagged for joint review rather than treated as a separate Type here |
| Law Practice Management System | embedding host | manages clients, matters, documents, billing, calendar; e-filing enters as an integrated capability that syncs orders and filed documents back to matters |
| Legal Docket Management | adjacent | centers on the court's register of case events and deadlines; the e-filing platform centers on the submission transaction |
| Legal Document Automation | upstream | produces the documents to be filed; has no submission or adjudication loop |
| Government Service Portal | adjacent | general citizen-facing service delivery; e-filing is a specialized filing transaction with clerk adjudication and fee machinery |
| E-signature Application | upstream | signing is part of document preparation; the e-filing platform documents acceptable signing approaches but does not center on them |
| Managed File Transfer / Document Delivery | looks similar, is not | one-way delivery with confirmation; no case binding, no adjudication loop, no filing semantics |

The sharpest boundary is with the court-side systems. The same filing transaction has two sides: the filer's platform (assemble, submit, track, pay, receive) and the court's system (receive, review, docket, record). When a court operates its own single portal, both sides live in one system — the Type boundary then follows the filer-facing surface, not the operator.

## Representative Products

- **Green Filing** — independent standalone provider operating across multiple US states; documented the reference filing workflow, fee layering, and status model
- **One Legal** — provider combining e-filing with process serving and litigation support (California/Nevada focus); documented rejection handling and the provider-pays fee model
- **FileTime** — independent standalone provider; documented the shared court-back-end identity layer and document conversion
- **MyCase (with InfoTrack)** — practice-management suite delivering e-filing through integration; documented the embedded pole
- **Tyler Technologies (Odyssey File & Serve)** — the dominant court-technology vendor, operating both court back-end systems and a filer-facing service; included as a market anchor on the basis of state-portal listings and competitor documentation (see Sources)

## Sources

Research date: **2026-09-07**

- Green Filing — homepage and Texas state page (https://www.greenfiling.com/, https://www.greenfiling.com/texas/); support center: "File on an Existing Case", "Initiate a New Case", "Filing Status Screen" (https://support.greenfiling.com/)
- One Legal — homepage and Court Filing product page (https://www.onelegal.com/, https://www.onelegal.com/products/filing/); support center: "How to Use Re-File to Resubmit Rejected Filings", "Why did the court reject my filing?", "What fees should I expect to pay when eFiling?", "What is eFileCA?" (https://support.onelegal.com/)
- FileTime — homepage (https://www.filetime.com/)
- eFileTexas.gov — official state e-filing portal (https://efiletexas.gov/)
- MyCase — "Integrating InfoTrack with MyCase" (https://supportcenter.mycase.com/en/articles/9370184-integrating-infotrack-with-mycase)

> Sourcing limitation: official Tyler Technologies product documentation was not reachable from the research environment (HTTP 403 on tylertech.com; transport errors on its filer portals). Tyler's market role is therefore established indirectly — through the official Texas EFSP listing, competitor documentation organized around Tyler's court systems, and customer comparisons — and no product-level operational claims about Tyler's filer service are made in this document. Clio's e-filing offering was likewise not directly verifiable; the practice-management-embedded pole is evidenced by the MyCase integration instead. Precise numeric details (file-size limits, fee percentages, retention periods, review-time ranges) are court-, state-, and product-specific and are intentionally not stated here; they are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
