# Research Notes — Mortgage Origination Platform

Research date: 2026-09-08
Leaf: Mortgage Origination Platform (DIRECTORY §08 Finance, Banking, Insurance & Investment)
Slug: mortgage-origination-platform

---

## Research Goal

Define the lender-side Mortgage Origination Platform: what it is, who uses it, what its core structure is, how a mortgage application moves through it, which structures are mortgage-specific (as opposed to generic loan-origination machinery), which rules govern it, and where its boundaries sit.

This pass must discharge (from this side) the family flags recorded by prior passes:

1. **mortgage-borrower-portal pass flag** — JOINT REVIEW RECOMMENDED with mortgage-origination-platform and mortgage-servicing-platform: the mortgage family partitions one loan lifecycle across audience axes; borrower portals bundled inside staff-side platforms should be packaging, not identity.
2. **loan-origination-system pass flag (family joint review item 4)** — LOS + LMS + Consumer Lending Platform + Commercial Loan Origination + Mortgage Origination Platform partition one lending lifecycle across two axes (stage vs segment); all five passes agree on keep-both + scope axes + funding seam; this pass supplies the mortgage side's evidence.
3. **loan-origination-system pass boundary finding** — "the Mortgage Origination Platform leaf owns the collateral-regime machinery" (escrow setup, disclosures, investor/GSE workflows were hypothesized; this pass must document what is actually evidenced).
4. **commercial-loan-origination pass boundary finding** — "replace facility/financial-statement machinery with amortizing residential-collateral machinery → mortgage origination."

## Initial Boundary (working hypothesis before research)

- Core use: the lender's staff-side system for carrying a mortgage loan application from intake through processing, underwriting, closing, and funding — the mortgage-scoped sibling of the generic LOS.
- Primary users: the mortgage lender's own staff (loan officers/originators, processors, underwriters, closers/funders, secondary-marketing and post-closing staff); borrowers at the application edge; brokers/TPOs as a channel.
- Nearest neighbors: Loan Origination System (generic), Commercial Loan Origination, Mortgage Servicing Platform (funding/boarding seam), Mortgage Borrower Portal (audience seam), Credit Decisioning Platform (AUS/decision-engine layer), real-estate transaction surfaces (the home sale vs the loan).
- Unknowns: how much of secondary marketing/investor delivery sits inside the Type; whether "escrow setup" is actually documented at origination (the sibling passes hypothesized it); how wholesale/correspondent channel machinery is structured; what regional (non-US) forms look like; whether POS-layer products (no own underwriting/booking) belong inside the Type or beside it.

## Research Questions

1. What is the unit of work, and what does a mortgage case carry that a generic credit case does not?
2. What pipeline/milestone structure does the market use, and who moves the case?
3. How is evaluation structured — borrower evidence (credit, AUS, verifications) vs property evidence (valuation, title), and how do loan programs/eligibility rules shape it?
4. What intake channels exist (borrower POS, staff entry, broker/TPO, correspondent), and how are third-party originators modeled?
5. What happens between approval and funding — conditions, disclosures, closing documents, settlement agents, recording?
6. Where does the Type end: funding? investor delivery? post-closing QC? boarding to servicing?
7. Which machinery is mortgage-specific vs inherited from the generic origination core?
8. How do packaging poles (system of record vs POS-layer products) differ, and do both belong to the Type?
9. What do regional forms look like (UK/other), and does the US agency/secondary-market machinery survive as definitional?
10. What is the seam with servicing (boarding), with the borrower portal, with CRM/lead tools, and with real-estate transaction systems?

## Representative Products

Selection principles: market representation + documentation completeness + different product philosophy + different customer tier. Five products sampled, spanning enterprise system-of-record, digital-POS platform, broker POS/pipeline, cloud-native multi-edition LOS, and a regional (UK) boundary-context pole:

| Product | Pole | Customer tier | Sources reached |
|---|---|---|---|
| ICE Mortgage Technology — Encompass (+ Consumer Connect, TPO Connect, eClose, ICE PPE, Investor Connect) | Enterprise end-to-end "system of record" for mortgage lending; dominant US platform | Banks, credit unions, independent mortgage bankers (enterprise→mid) | Official root + product pages (A) |
| Blend — Home Lending Suite | Digital-origination platform (borrower-experience-first); suite over the lending stack | Banks, credit unions, independent mortgage banks | Official root + suite/originations pages (A) |
| Floify | Point-of-sale + pipeline for loan officers/brokers; document-automation philosophy | Small lenders, brokers, LO teams | Official root + Tier-1 public help center (A) — richest operational evidence in the sample |
| LendingPad | Cloud-native LOS+POS in Broker/Lender/Processing editions; wholesale marketplace | Brokers, small-to-mid lenders, banks, CUs | Official root + solutions pages (A) |
| Mortgage Brain (UK) | Regional boundary-context pole: UK intermediary sourcing/criteria/affordability/submissions stack | UK mortgage intermediaries and lenders | Official root + product pages (A) |

Sibling-pass evidence reused as corroboration (not as primary): loan-origination-system pass (MeridianLink mortgage line; HES), commercial-loan-origination pass (collateral-regime seam), mortgage-borrower-portal pass (borrower-facing portal machinery incl. Floify borrower portal), loan-management-system pass (funding seam / servicing ledger test).

## Sources

Primary (fetched 2026-09-08):

- ICE Mortgage Technology — https://www.icemortgagetechnology.com/ (root; suite organization: Customer Acquisition / Loan Manufacturing / Settlement & Closing / Capital Markets & Secondary Marketing / Servicing)
- ICE Mortgage Technology — https://www.icemortgagetechnology.com/products/encompass (Encompass platform page)
- ICE Mortgage Technology — https://www.icemortgagetechnology.com/products/encompass-tpo-connect (TPO Connect)
- ICE Mortgage Technology — https://www.icemortgagetechnology.com/products/encompass-investor-connect (Investor Connect)
- Blend — https://blend.com/mortgage/ (Home Lending Suite) and https://blend.com/products/mortgage-suite/originations/ (Mortgage Originations)
- Floify — https://help.floify.com/en/ (help center root; collections: Using Floify [210 articles], Configurations, Integrations, Company Dashboard, Pipeline, Workflows, Disclosure Desk, Borrower Help, Realtor/Partner Help, Settlement Agent Help) — Tier-1
- LendingPad — https://www.lendingpad.com/ (root: Broker/Lender/Processing editions) and https://lendingpad.com/solutions/lenders (Lender Edition page)
- Mortgage Brain — https://www.mortgagebrain.co.uk/ (root; Sourcing/Criteria/Affordability/CRM/Submissions Brain modules)

Unreachable / not attempted / rejected:

- useorigin.com — fetched but is an unrelated personal-finance product ("Origin Financial", US budgeting/investing app); the intended Canadian mortgage-origination sample was NOT verified this pass. Recorded per the network/verification rules; no claim rests on it. Canadian regional forms therefore remain unsampled.
- Encompass help center / ICE client support surfaces — not attempted beyond product pages (login-walled support class, consistent with prior lending passes).
- Blend product documentation (blendhelp.com) — not fetched this pass; claims about Blend rest on its official product pages only.
- Byte Software, Calyx, ARIVE, wemlo, Finastra Mortgagebot — not fetched (sample sufficient per stop conditions; no claims made about them).
- UK lender-side origination systems (the lender half of the UK market) — not sampled; Mortgage Brain evidence covers the intermediary pole only.

Evidence layers: A = directly observed on an official source for a specific product; B = cross-product commonality; C = canonical inference from comparison + boundary reasoning.

---

## Product Observations

### ICE Mortgage Technology — Encompass platform (A)

- Self-positioning: "Mortgage Loan Origination Software… As the industry's system of record"; "connects and accelerates every step of the lending process"; "end-to-end workflows for any lending channel from a single system of record" (platform page).
- The vendor organizes its whole suite by mortgage lifecycle stage — Customer Acquisition → Loan Manufacturing → Settlement & Closing → Capital Markets & Secondary Marketing → Servicing — with Encompass as the core of "Loan Manufacturing" (root page). This is the clearest single statement of the type's stage partition.
- Channel structure is explicit: **Consumer Connect** (borrower POS: "complete an online mortgage application… securely upload and eSign documents"), **TPO Connect** ("receive and manage loans from your Third-Party Originators… in your wholesale and correspondent channels"; TPOs can "view pipeline reports and monitor status; order credit, AUS, submit lock requests; deliver and eSign loan packages; view and manage correspondent trades"), **correspondent lending** ("simplify your loan acquisition process… acquisition pipeline management" — buying loans other lenders closed).
- Closing machinery: **eClose** ("document ordering, borrower engagement, settlement agent collaboration, eSignatures"); companion products Simplifile ("send your documents for recording at county offices") and MERS ("serves as mortgagee of record"). Closing spans pre-close → closing → post-closing "directly from your system of record — from ordering documents, collaborating with partners, collecting borrower signatures, investor delivery, MERS registration and recording."
- Pricing/product machinery: **ICE PPE** — "industry-leading pricing engine, seamlessly integrated into Encompass… quickly access rate sheets"; secondary-marketing section: "streamline pricing and lock policies, trades and loan delivery to investors… sell high-quality loans to a wide network of investors and GSEs."
- Investor delivery: **Investor Connect** — "loan delivery, funding, and purchases — fast"; "deliver complete and accurate loans to investors and warehouse banks"; "preformats documents and data to meet investor requirements"; "notifies you of any missing or required information before delivery." So post-closing/investor-delivery machinery is part of the origination platform family, and **warehouse banks** are a counterparty class.
- Document automation: **Mortgage Analyzers** — "intelligent document recognition and data extraction… interrogate the extracted data from documents against the information in your loan origination system and presents the exceptions for review" (document-vs-data exception handling as a named capability).
- Adjacent home-secured products share the same system: "originate and service home equity loans and lines of credit on the same systems as first mortgage loans" (Home Equity Lending solution).
- Servicing boundary: MSP is marketed as the servicing system "from loan boarding to default" — boarding is the seam.
- CRM/lead tools (Surefire, Velocify) are sold as separate suite products under "Customer Acquisition," not inside the origination core — evidence for the origination-vs-CRM module boundary.

### Blend — Home Lending Suite (A)

- Self-positioning: "Digital Origination: Blend Home Lending"; "Blend brings speed and simplicity to mortgage loan origination"; the suite covers "mortgage and home equity" (root).
- **Mortgage Originations** components: application intake ("borrower loan app with educational, dynamic questioning and self-serve capabilities"); purchase affordability ("loan scenario simulator and soft credit pulls" — pre-application qualification); "intelligent follow-up engine… identify up to 65% of conditions upfront with triggered, automated follow-up notifications"; soft-credit pre-qualification; "upfront rates… instant rate quotes"; "disclosures… deliver digital disclosure packages to borrowers throughout the process in a single platform"; SMS notifications; borrower co-pilot assistance.
- Suite siblings: **Verifications** ("instant, automated verifications — sourced directly from leading data providers — to speed up the loan lifecycle"), **Lender Tools** (mobile app for loan officers), **Close** ("hybrid, hybrid with eNote, and Remote Online Notary options"), **Rapid Home Refi**, **Rapid Home Equity**.
- Platform layer: process automation, intelligence, branding/theming, "consumer and banker interfaces," customizable workflows, integration management, reporting, **compliance management** — i.e., the vendor sells the origination experience layer and workflow machinery; the underlying LOS of record for many clients is an external system (the vendor's own materials describe integration management; no servicing-ledger or investor-delivery claims are made on the fetched pages).
- Home equity (HELOC) is a first-class product line of the same platform — consistent with ICE's home-equity-on-the-same-system statement.

### Floify (A, Tier-1 help center)

- The lender-side world model, from the help-center collections (Pipeline, Company Dashboard, Disclosure Desk, Workflows, Realtor/Partner Help, Settlement Agent Help):
  - **Prospect → Loan Flow**: pipeline holds prospects (pre-application leads) that convert into live loan flows; loan flows can be started, edited, archived, unarchived, deleted, transferred between teams; owner/reassignment machinery; pipeline filter/search and status tab.
  - **The 1003 as the application object**: "Continuing to Edit the 1003 Application," "Import an 1003 XML File," "Download a MISMO 3.4 Version of My Borrower's Loan Application" — the standardized URLA (1003) and MISMO as the interchange formats; loan flows connect to Encompass loan file numbers ("Connect a Loan Flow to a New Encompass Loan File Number with Co-Mortgagors Enabled") — POS-to-LOS synchronization is explicit machinery.
  - **Milestones as configuration**: "Company Milestone Sets," "Create Company Level Milestones," "Set Up or Edit Company Milestones," "Set Up or Edit the Milestone LOS Synced Fields," "Update a Borrower's Milestones" — the milestone sequence is company-configurable and syncs to the LOS; borrowers and realtor partners can review milestone updates.
  - **Document requests / needs list**: "Add a New Document Request," "Resend Needs List Email to My Borrower," "Accept or Reject a Document," "Loan Flow Document Status Column," borrower-side "Declare a Document Request Not Applicable"; LOS conditions can be converted into document requests ("Enable Encompass Conditions to Floify Document Requests").
  - **Credit + verification pulls**: "Manually Pull a Hard Credit Report," "Reissue a Credit Report," "Enabling Soft Credit Pulls," "Manually Pull a VOA, VOE, or VOI Request" (verification of assets/employment/income via The Work Number / AccountChek integrations), "Edit Authorization to Run Credit Check," "Consent to a Credit Check on Borrower's Behalf" (e-consent machinery).
  - **AUS findings**: "Running Dual AUS Findings" — automated-underwriting-system findings are consumed inside the platform.
  - **Disclosure workbench**: the "Disclosure Desk" collection — "How to Order Disclosures Using Disclosures Desk 2.0," "Lender Disclosure Signing Process," "Borrower Disclosure Signing Process," "Automated Floify Disclosure Emails," Encompass disclosure plugin — disclosure generation/ordering/delivery is a distinct workbench with its own permission ("Enable the Disclosure Desk Permission").
  - **Closing machinery**: "Ordering Closing Documents — Floify Hybrid eClosing," "Viewing Closing Documents in Floify," "Floify and ICE eClose Setup," and a **Settlement Agent Portal** ("Hybrid E-Closing: Settlement Agent Portal") — third-party settlement collaborators have their own surface; "Update the Loan Deadline, Expected Closing Date, or Actual Closing Date" tracks the case to closing.
  - **Pre-approval letters**: "Sending a Pre-Approval Letter," "Floify Pre-Approval Letter Hub," realtor-side "Generate a Pre-Approval Letter in My Realtor Account" — LO-generated borrower qualification letters are a first-class output.
  - **Party model**: borrowers + co-mortgagors ("Set Up Borrower Pairs," "Split Co-Mortgagors"), realtor/partner portals (invite to loan flow, milestone review, document upload), settlement agents.
  - **Organization/roles**: Company Dashboard, Organization Dashboard, teams and users, user permissions, SuperUsers vs regular users, support users, audit log, session timeouts, password controls, SSO, white-label.
  - **Regulatory/compliance surfaces**: "Mortgage Call Reports" (NMLS reporting), "Update the Company NMLS ID," state-specific form generation ("Texas Conditional Qualification and Conditional Approval Forms," "Arizona Pre-Qualification and Loan Status Forms"), "Configure E-Consent," SMS compliance, audit-log events.
  - **Pricing adjacency**: "Enable Rate Calculators via Optimal Blue" — third-party product/pricing engines integrate at the POS.
  - **Data hygiene**: "Edit the Timeline in Which Floify Automatically Deletes Old Loans," auto-delete loans, loan archiving.
- Floify carries the case, pipeline, evidence collection, and closing-document machinery, but the underwriting decision and funding/booking live in the connected LOS (loan-file-number sync, conditions/eFolder sync) — the POS-layer pole.

### LendingPad (A)

- Self-positioning: "The Modern LOS… web-based, end-to-end innovative LOS for residential mortgage lending."
- Edition structure maps the market: **Broker Edition** (brokers who submit to wholesale lenders: "Direct wholesale integration," "Complementary POS facilitating a seamless borrower experience," multi-user processing, real-time notifications); **Lender Edition** (adds "Secondary, funding and post closing functions," "Capability to perform banking functions and warehousing activities," "Administration of third-party channels, and complete secondary tasks with institutional investors," enterprise API); **Processing Centers** (outsourced processing: "Multiple role definitions including processor, manager, closer, funder and post closer").
- Lender Edition page: "For the independent Lender — retail, wholesale and correspondent"; "customized pricing and eligibility, automated underwriting, and real-time pipeline monitoring"; "Secondary, QC, Closing, Warehousing and Post Closing Functions"; "Direct and Third-party (Wholesale & Correspondent) Channels."
- Channel machinery: integrated wholesalers displayed in a "Wholesale Marketplace" (major wholesale lenders named as integrations); GSE integrations displayed (Fannie Mae, Freddie Mac logos among partners, alongside doc-prep and compliance vendors — DocMagic, ComplianceEase — and data vendors).
- A customer quote on the official page describes the working loop: "you can send the requests through LendingPad, title requests, VOE, Hazard Insurance and more… you can balance your closing disclosure on the platform, and it even helps you calculate some of the fees" — title/insurance/VOE requests and closing-disclosure balancing as in-product work.

### Mortgage Brain (UK) (A — regional boundary-context pole)

- Self-positioning: "at the forefront of mortgage technology in the UK for four decades. Backed by some of the largest lenders — Barclays, Lloyds Bank, Nationwide Building Society, NatWest, and Santander."
- The UK intermediary stack decomposes origination differently: **Sourcing Brain** ("source products from 100+ lenders… 98% of the industry"; inbuilt AVM; browse/compare/graph product analysis); **Criteria Brain** ("criteria verified by up to 90 lenders directly in real time daily"; searches through 75,000+ individual criteria for residential and buy-to-let); **Affordability Brain** (lender-specific affordability results "supplied for full audit purposes"); **CRM Brain** (fact find, client portal with document upload, secure messages, case progress; workflows/tasks/roles/permissions); **Submissions Brain** ("a single journey that is identical for all lenders"; "Alternate Lender Submission journey allows ReDIP without rekeying"; data dictionary); Hub = one login over all modules.
- Lender-side products exist in the same vendor's portfolio (Distribution Brain, Insights Brain, Services Brain) but were not fetched — the intermediary pole is what this pass observed.
- Structural reading: in the UK regime the *advice-and-submission* work is carried by intermediary systems, the *decision-and-funding* work by lender systems; there is no US-style GSE delivery, dual-AUS, or rate-lock machinery in evidence. The same market function (broker-initiated origination) that the US realizes as a channel portal inside the lender's platform is realized here as a separate intermediary system talking to lender systems.

---

## Cross-product Comparison

| Structure | ICE Encompass | Blend | Floify | LendingPad | Mortgage Brain (UK) | Layer |
|---|---|---|---|---|---|---|
| Loan application as persistent case (prospect/loan flow/loan file) | A (loan files; system of record) | A (application journey) | A (prospect → loan flow) | A (pipeline of loans) | A (cases/fact find) | B — core |
| Subject property + collateral evidence in the case | A (valuations suite; title; eClose) | A (property intake form; affordability on property price) | B (document requests incl. insurance; closing dates) | A (title requests; insurance; user quote) | A (inbuilt AVM; affordability) | B — core (mortgage invariant) |
| Milestone/stage pipeline with per-party visibility | A (TPO pipeline views) | B (process automation) | A (configurable milestones, borrower/realtor views) | A ("real-time pipeline monitoring") | A (case progress tracking) | B — core |
| Borrower evidence: credit reports, verifications (VOE/VOA/VOI), e-consent | A ("order credit" via TPO Connect) | A (verifications; soft pulls) | A (hard/soft pulls; VOA/VOE/VOI; e-consent) | A (VOE requests) | — (not observed) | B — core |
| AUS findings consumed in the pipeline | A ("order… AUS") | — | A ("Running Dual AUS Findings") | B ("automated underwriting") | — | B — core (US-shaped, see L2) |
| Loan programs / pricing / eligibility machinery | A (ICE PPE; "pricing and lock policies") | A (upfront rates; scenario simulator) | B (Optimal Blue rate calculators) | A ("customized pricing and eligibility") | A (sourcing across 100+ lenders; criteria verification) | B — core (form varies by regime) |
| Human underwriting inside the system | A (Loan Manufacturing) | B (lender tools; workflows) | — (decision in connected LOS) | A (Lender Edition underwriting) | — | B — core, packaging-dependent |
| Recorded approval / decline with reasons | A (loan manufacturing workflow) | B | B (pre-approval + state conditional-approval forms) | A (underwriting + pipeline) | — | B — core |
| Conditions tracking to clearance | A (Mortgage Analyzers exceptions; TPO) | A ("65% of conditions upfront"; follow-up engine) | A (document requests; Encompass conditions sync; accept/reject) | B (requests machinery) | — | B — core |
| Disclosure delivery machinery (US regime) | B (Consumer Connect eSign; ecosystem) | A ("digital disclosure packages") | A (Disclosure Desk; lender/borrower disclosure signing) | A (closing-disclosure balancing — user quote) | — | B — L1, US-specific |
| Closing documents + settlement-agent collaboration + e-closing/eNote/RON + recording | A (eClose; Simplifile; MERS) | A (Close: hybrid/eNote/RON) | A (hybrid eClosing; Settlement Agent Portal) | A (closing functions) | — | B — core-ish (modern form; see historical check) |
| Funding + booking handoff to loan record | A (Investor Connect "funding") | — | — (LOS-synced; closing dates tracked) | A (funding functions) | — | B — core |
| Third-party originator channel (broker/TPO portal; wholesale/correspondent) | A (TPO Connect; correspondent lending) | — | B (realtor/partner portals ride the flow) | A (wholesale marketplace; TPO administration) | A (submissions to lenders — as separate system) | B — L1/L2 (channel-dependent) |
| Secondary marketing / investor delivery / warehouse banking | A (secondary marketing; Investor Connect; GSEs; warehouse banks) | — | — | A (Lender Edition secondary/warehousing; institutional investors) | — | L2 (scale/channel-dependent) |
| Post-closing QC / trailing docs | B (post-closing in lifecycle language) | — | — | A ("Post Closing Functions"; QC) | — | L2 |
| Borrower-facing POS as bundled surface | A (Consumer Connect) | A (whole product) | A (whole product) | A ("complementary POS") | A (CRM Brain client portal) | B — standard |
| Organization/roles/permissions/audit | A (enterprise platform) | B (platform layer) | A (teams, permissions, audit log) | A (role definitions incl. closer/funder/post-closer) | A (roles/permissions) | B — standard |
| Regulatory reporting (NMLS call reports) | — | B (compliance management) | A (mortgage call reports) | — | — | product-specific/L2 |
| CRM/lead-generation adjacency (separate products or landing pages) | A (Surefire/Velocify as separate suite products) | B (top-of-funnel affordability tools) | B (prospects; landing pages; lead-source tracking) | — | — | L1/L2 — adjacency, not core |

Key comparison reads:

1. **The generic origination core survives intact** — case, pipeline, policy-governed evaluation, decision-to-funding — exactly as the LOS pass defined it. Nothing mortgage-specific replaces those legs.
2. **What the mortgage population adds structurally is the property**: every sampled product binds the case to a subject property whose value (AVM/appraisal/valuation) and encumbrance (title) are evidenced as part of the case, and every product carries program/pricing/eligibility machinery that prices the loan against the property + borrower profile. This is the load-bearing mortgage invariant.
3. **The party web is wider than the generic LOS**: borrower(s)/co-borrowers, loan officer, processor, underwriter, closer, funder, post-closer, broker/TPO, realtor partners, settlement agents — multiple sampled products give third parties dedicated portal surfaces (Floify realtor + settlement-agent portals; ICE TPO Connect; LendingPad wholesale marketplace).
4. **US agency/secondary-market machinery (AUS, GSE delivery, warehouse banking, rate locks, TRID-style disclosures) is common but channel- and regime-dependent** — absent from the UK pole, absent from broker-pole products (Floify), optional-edition at LendingPad (Lender edition only). L2.
5. **Packaging splits the market into (a) full systems of record and (b) POS/experience layers over a system of record** — both marketed as mortgage origination platforms; the POS layer carries legs 1–2 fully and shares legs 3–4 with a connected LOS.

---

## Canonical Model

### L0 — Defining Invariant

A Mortgage Origination Platform is the lender-side origination system for real-estate-secured residential lending (first mortgages and home-secured lines), defined by four jointly-held structures — the generic origination core scoped to property-anchored collateral:

```text
1. The mortgage application as property-anchored case of record
   one persistent, individually identified case per loan request, carrying the
   borrower party set, the requested loan, AND the subject property with its
   collateral evidence (valuation, title/encumbrance, insurance) — reachable
   from every intake channel (borrower POS, staff/LO entry, broker/TPO submission)
   [remove the property anchoring → generic Loan Origination System;
    remove the case → disconnected point tools]

2. The lender-side origination pipeline with per-party milestone visibility
   the case advances through the lender's own defined stages from intake toward
   funding; the system is the record of in-flight work (stage, ownership,
   history), and milestone state is visible to the parties riding the case
   (staff roles, borrower, channel partners)
   [remove → decision service or form tool]

3. Borrower-and-property evaluation under program eligibility rules
   borrower evidence (identity, credit history, income/assets — verified via
   credit reports and verification services) is assessed TOGETHER WITH the
   property's collateral evidence (valuation, title) against the lender's loan
   programs and eligibility criteria, through configurable machinery: automated
   rules/findings, human underwriting, or hybrid routing
   [remove the property leg → generic consumer credit evaluation;
    remove policy machinery → generic workflow tracker]

4. The recorded decision executed through conditions and closing to funding
   approve with final terms / decline with reasons / refer — recorded with
   basis and actor as an audit-ready institutional act; approved cases clear
   tracked conditions, produce and execute closing documents with settlement
   counterparties, and reach funding, ending in a booking/boarding handoff to
   the loan's servicing-side record; decline/withdrawal/cancellation are
   recorded terminal outcomes
   [remove the decision leg → paperwork software;
    remove execution-to-funding → standalone decisioning/experience layer]
```

Jointly-held is load-bearing:

- 1 alone = a property/lead data collector. 2 without 1 = workflow machinery with nothing case-bound. 3 without 2 = a decisioning service (Credit Decisioning Platform seam). 1+2 without 3 = a generic CRM-shaped tracker around loans. 1–3 without 4 = an application experience layer, not an origination system of record.
- The **property anchoring** (leg 1 + leg 3) is what makes this a sector Type rather than an alias of the generic LOS: in a generic LOS collateral handling is optional machinery for secured products; here the subject property is a mandatory, evidenced component of every case, and evaluation is jointly borrower-and-property.
- The definition is stated so that it does NOT require: POS portals, AUS findings, GSE/investor delivery, rate locks, US disclosure machinery, MISMO interchange, or any specific milestone vocabulary — all are implementations (see L1/L2).

### L1 — Common Mature Structure (widespread; not definitional)

- **Borrower-facing POS** bundled with the platform: guided application (the standardized 1003/URLA in US products), document upload, e-consent and credit authorization, e-signature, milestone/status updates, notifications (SMS/email), co-borrower accounts.
- **Milestone/task machinery**: configurable milestone sets synced across surfaces; task management; document-request/needs-list machinery with review states (submitted/accepted/rejected/not-applicable).
- **Verification services consumed in-pipeline**: credit reports (hard/soft, reissue), employment/income/asset verifications (VOE/VOI/VOA) via external data providers.
- **AUS findings** consumed at decision points (US market).
- **Program/pricing machinery**: product & pricing engines, rate quotes, eligibility engines, rate-lock requests/policies (US form: lock + lock policies).
- **Pre-approval letters** as LO outputs, including partner-generated letters.
- **Closing machinery**: closing-document generation/ordering, settlement-agent collaboration portals, hybrid e-closing / eNote / RON options, e-recording, closing-disclosure balancing (US), closing-date tracking.
- **Channel portals**: TPO/broker portals (submission, pipeline visibility, credit/AUS ordering, lock requests); realtor/partner portals riding the loan flow.
- **Conditions tracking** to clearance, with LOS↔POS condition synchronization.
- **Multi-role organization**: loan officer, processor, underwriter, closer, funder, post-closer; team/user/permission administration; audit logs.
- **Integration spine**: credit bureaus, verification providers, AUS, valuation/title/appraisal vendors, doc-prep and e-sign vendors, GSE systems, POS↔LOS sync (MISMO/1003 interchange in the US), e-recording registries.
- **Compliance surfaces**: disclosure delivery, e-consent, audit trails, jurisdiction-specific forms, regulatory reporting (product-specific where observed).
- **Reporting/analytics**: pipeline throughput, cycle times, conversion.

### L2 — Variant / Optional Structure

- **Channel mix**: retail/consumer-direct vs wholesale/TPO vs correspondent acquisition; broker editions vs lender editions vs processing-center editions.
- **Packaging**: full system of record (origination through funding and into secondary) vs POS/experience layer over an external LOS (case + pipeline + evidence + closing docs, with the decision/booking in the connected system) vs POS as a module of a suite.
- **Secondary-market machinery** (US lender tier): investor delivery packages, warehouse-bank submissions, correspondent trade management, post-closing QC/trailing-doc machinery. Present where the lender sells loans; absent from portfolio/broker forms.
- **Regime forms**: US agency machinery (GSE eligibility, dual-AUS, TRID-style disclosures, MERS/e-recording) vs UK intermediary regime (sourcing engines across lenders, criteria verification, affordability engines, lender submissions) vs other regional regimes (unsampled). The UK form splits the four legs between intermediary systems (legs 1–2, channel-side) and lender systems (legs 3–4) — a boundary case, not a counterexample.
- **Asset scope**: first mortgages vs home equity/HELOC vs refinance-specific flows on the same platform.
- **Deployment**: cloud SaaS dominant; long-lived installed/desktop heritage forms persist in the market.
- **Adjacency modules**: CRM/lead capture, marketing, consumer-banking/deposit flows (platform suites), call reports.

### L3 — Vendor-specific (research notes only)

- ICE/Encompass: "system of record" positioning; Consumer Connect / TPO Connect / eClose / ICE PPE / Investor Connect / Data Connect product names; Mortgage Analyzers document-vs-data exception machinery; ROI study figures ($1,154/loan, 15.5% more closings, 3.75 days, 7.53x) — marketing claims; Simplifile (county recording) and MERS (mortgagee-of-record registry) as companion products; suite organized as Customer Acquisition / Loan Manufacturing / Settlement & Closing / Capital Markets & Secondary Marketing / Servicing.
- Blend: Home Lending Suite naming; Autopilot / Co-pilot / Navigator AI features; "65% of conditions upfront" claim; "10x ROI baked in" marketing; Rapid Home Refi / Rapid Home Equity product names; customer-story metrics (BMO, KeyBank, BOK, Affinity, UWCU).
- Floify: Prospect vs Loan Flow object naming; "Needs List"; Disclosure Desk 2.0; Stack and Send; co-mortgagor split; company milestone sets + LOS-synced fields; Optimal Blue / The Work Number / AccountChek integrations; TX/AZ state form packages; auto-delete loan retention timeline; white-label; NMLS call reports; Settlement Agent Portal.
- LendingPad: Broker/Lender/Processing edition names; wholesale marketplace with named wholesalers (UWM et al.); "10 Questions to Ask Your LOS Vendor" content marketing; SSAE16/SOC 2 trust claims; enterprise API.
- Mortgage Brain: module names (Hub, Sourcing/Criteria/Affordability/CRM/Submissions Brain); "98% of the industry" / "100+ lenders" / "75,000 criteria" / "90 lenders verified in real time daily" claims; ReDIP alternate-lender submission journey; Lender Service Report; lender-shareholder backing (Barclays, Lloyds, Nationwide, NatWest, Santander).

## Rejected Findings (considered and not promoted)

- **"Escrow setup" as origination machinery** — hypothesized by prior sibling passes; NOT verified in any sampled product's reachable documentation this pass. Escrow *administration* is documented in the servicing/borrower-portal passes. Held out of the definition; recorded as an uncertainty.
- **Rate locks as definitional** — lock requests/lock policies appear at ICE (TPO + secondary) and are absent from the UK pole and Floify-class POS documentation; the UK regime prices differently. L1/L2 only.
- **GSE/investor delivery as definitional** — channel- and regime-dependent (see comparison row 14). L2.
- **Milestones as a fixed universal sequence** — milestone sets are company-configurable at the one product with Tier-1 evidence; exact stage vocabularies vary. Held as configurable machinery, not a standard state list.
- **Dual-AUS / specific agency program names** — observed (Floify "Dual AUS"; ICE "AUS"; GSE logos at LendingPad) but regime-specific; kept generic ("automated-underwriting-system findings").
- **Mortgage Brain as a representative product of the Type proper** — the UK intermediary pole fails L0 legs 3–4 (no lender-side decision/funding machinery of its own); retained as boundary context, not a sample member for the core.

---

## Historical / Market-Sample Check

- **Paper-era check**: a mid-20th-century savings-and-loan or mortgage bank runs the four legs without software: the standard paper application form (the 1003's ancestor) as the identified case carrying borrower + property (1); the loan file moving across desks — intake, processing, appraisal, title, underwriting, closing (2); the underwriter applying the institution's lending policy to credit reports, appraisals, and title searches (3); a minuted approval, note and deed-of-trust executed at closing, funds disbursed, loan booked to the ledger (4). No POS, no AUS, no GSE delivery, no MISMO. The L0 passes.
- **Regional check**: the UK intermediary pole shows the case-carrying work split from the decision-and-funding work across two systems — the L0 is scoped so that the *lender-side* system satisfies it while the intermediary system is documented as the channel realization. The definition does not require US agency machinery, so non-US regimes are not excluded by construction. Canadian, EU, and APAC lender-side forms were not sampled (recorded as uncertainty; the attempted Canadian fetch landed on an unrelated product).
- **Platform-native check**: bank-embedded origination modules and suite-internal mortgage modules (e.g., a multi-line bank platform originating mortgages beside consumer/commercial lines — MeridianLink's mortgage line per the LOS pass) satisfy the core as platform modules. Home-secured lines (HELOC) ride the same systems per two sampled vendors — included in scope without changing the core.
- **Scale check**: a single-LO brokerage running a POS+pipeline over a wholesale lender's platform and a national lender running an end-to-end system of record both satisfy the core at different leg depths — the packaging axis is documented, not hidden.
- **Anti-overfitting check**: consumer-grade digital POS, AI assistance, instant verifications, and e-closing are the current dominant implementations, not the definition; the paper-era and desktop-era forms satisfy the same four legs.

---

## Boundary Findings

| Neighboring Type | Seam | Test ("remove what → becomes the other Type") |
|---|---|---|
| Loan Origination System (processed) | Sector seam inside the origination family: generic LOS = segment-agnostic pre-funding case pipeline; this leaf = the same core scoped to real-estate-secured residential lending with the property as a mandatory evidenced case component and borrower-and-property evaluation under program eligibility. Population logic from the LOS pass (narrowing the sector doesn't change the generic core) + this pass (the sector adds the collateral regime) → keep-both as sector siblings | remove the property anchoring and program-eligibility machinery → generic LOS; add them → this leaf |
| Commercial Loan Origination (processed) | Collateral-regime seam (per that pass): residential/home-secured amortizing machinery vs business-facility machinery (commitments, financial statements, covenants). Commercial CRE lending stays a variant of the commercial leaf | replace the residential property/collateral regime with facility/financial-statement machinery → commercial leaf |
| Mortgage Servicing Platform (unprocessed) | Funding/boarding seam: origination ends when the funded loan is boarded to the servicing record. Investor delivery, warehouse-bank submission, and post-closing QC are origination-side money machinery (the loan sale), NOT a servicing ledger (no payment application, escrow administration, or default machinery observed in origination documentation) | add the payment/escrow/default ledger → servicing; strip the pipeline, keep the ledger → servicing |
| Mortgage Borrower Portal (processed) | Audience seam: this leaf is staff-side + channel-side; the portal is borrower-operated standing self-service. Every sampled origination platform bundles a borrower-facing POS — packaging, not identity (discharges the portal pass's flag) | swap the audience back (borrower as direct user over a standing account space) → borrower portal |
| Credit Decisioning Platform (processed) | Layer seam, corroborated: AUS/rules/eligibility engines are invoked at decision points inside the case pipeline; standalone decisioning has no case, conditions, or closing machinery | strip everything but evaluation machinery → decisioning platform |
| UK-style intermediary sourcing/submission systems (no directory leaf) | Regime-shaped sibling: carries the case + sourcing + submission (legs 1–2, channel-side) but not the lender's decision/funding machinery (legs 3–4 live on lender systems); flagged as a potential future leaf or variant note, not silently merged | move legs 3–4 onto the intermediary system (it becomes a lender) → this leaf |
| Marketing/CRM platforms (mortgage CRM) | Module seam: lead/relationship work is sold as separate products or modules ("Customer Acquisition" vs "Loan Manufacturing" at one sampled vendor; prospects/landing pages at the POS pole); the origination core starts at the loan case | strip the loan-case/pipeline/decision machinery, keep lead nurturing → CRM |
| Real Estate Transaction Management / Property Listing / Showing platforms | Domain-object seam: realtor portals ride the loan flow, but this Type's object is the credit+collateral case, not the home transaction or listing | swap the loan case for the listing/transaction object → real-estate Types |
| Underwriting Workbench (insurance, §15) | Same word, different domain — insurance risk selection vs credit+collateral approval | swap credit/collateral machinery for insurance risk machinery → insurance workbench |
| Consumer Lending Platform (processed) | Scope seam: consumer platform = individual-borrower lifecycle (origination→servicing→collections); this leaf = property-secured residential lending's origination stage (HELOC overlap noted by that pass — home-secured lines sit in both neighborhoods; the property anchoring is this leaf's discriminator) | remove the property regime and add the funded lifecycle → consumer platform |

**Joint-review discharges and flags for STATUS.md:**

1. **Discharge (origination side) of the mortgage-borrower-portal pass flag**: confirmed from the origination side that borrower-facing POS surfaces are standard bundled packaging of the origination platform (4/5 sampled products document a borrower POS or client portal as part of/beside the origination core); the portal leaf's "one Type spanning two phase poles" definition stands; family partition (staff-side origination / staff-side servicing / borrower-side portal) corroborated.
2. **Contribution to the LOS-pass family joint review (item 4)**: this pass agrees — keep-both with scope axes (stage vs sector) and the funding seam; the five-leaf partition (LOS, LMS, Consumer Lending, Commercial Origination, Mortgage Origination) is corroborated from the mortgage side; directory-level family joint review still recommended, now including Mortgage Servicing Platform once processed.
3. **Correction to prior hypotheses**: "escrow setup" as origination machinery was NOT evidenced this pass (see Rejected Findings); the collateral regime evidenced is property + valuation/title + program eligibility. The LOS/commercial passes' boundary wording should be read with this narrowing.
4. **New flag — UK intermediary sourcing/submission systems**: a real market family (sourcing/criteria/affordability/submission for intermediaries) that carries the origination case channel-side without lender decision/funding machinery; no directory leaf exists. Recorded as a boundary case; no directory change made.
5. **New flag — POS-layer vs system-of-record packaging tension**: both poles are marketed as mortgage origination platforms; the POS layer shares legs 3–4 with a connected LOS. Membership test adopted (consistent with the LOS pass): documented pre-funding case pipeline = this Type; the decision/booking may live in a connected system of record (POS-layer variant) or in the same product (full-system variant).

---

## Uncertainties

1. **Encompass/LendingPad/Blend operational depth**: evidence is product pages (+ Floify Tier-1). Milestone vocabularies, lock-workflow states, field-level data models, and configuration mechanics are not asserted; Floify's help center is the only Tier-1 anchor in this pass.
2. **Escrow setup at origination** — unverified (see Rejected Findings).
3. **Correspondent machinery depth** — evidenced at marketing level (ICE correspondent lending; LendingPad correspondent channel); operational detail not documented.
4. **Regional breadth** — Canadian/EU/APAC lender-side origination platforms not sampled; the intended Canadian fetch returned an unrelated product. The UK pole is intermediary-side only; UK lender-side systems unsampled.
5. **HELOC breadth** — home-equity-on-the-same-platform documented at two vendors (ICE, Blend); breadth across the market not verified.
6. **Post-closing QC/trailing docs** — evidenced mainly at LendingPad and implied by ICE lifecycle language; treated as L2 without deeper claims.
7. **Precise regulatory machinery** (TRID timing, disclosure rules, NMLS reporting scope) — deliberately not characterized beyond what sampled documentation states; no regulatory specifics asserted.

---

## Final Synthesis

A Mortgage Origination Platform is the lender-side system of work for originating real-estate-secured residential loans. Its defining core is the generic origination structure — application case, lender-side pipeline, policy-governed evaluation, recorded decision executed to funding — scoped by one sector invariant: **every case is anchored to a subject property whose value and title are evidenced as part of the case, and every decision rests jointly on the borrower's verified capacity and the property's collateral standing, assessed against the lender's loan-program eligibility rules.** Around that core, mature products add the borrower POS, milestone machinery with per-party visibility, verification and AUS consumption, program/pricing/eligibility engines, disclosure and closing machinery with settlement-agent collaboration, channel portals (broker/TPO), and — at the lender tier that sells its loans — secondary-market, warehouse-banking, and post-closing machinery ending in investor delivery.

The type's market splits by packaging (full systems of record vs POS/experience layers over a connected LOS) and by channel mix (retail, wholesale/TPO, correspondent), and its machinery is regime-shaped: US products carry agency/AUS/disclosure/lock machinery that regional forms replace with their own sourcing/submission machinery. The funding/boarding seam separates this leaf from mortgage servicing; the audience seam separates it from the borrower portal; the collateral-regime seam separates it from commercial origination; the property anchoring separates it from the generic LOS. The paper-era mortgage desk — paper 1003, loan file, appraisal and title in the folder, policy-manual underwriting, minuted approval, closing table, booked loan — satisfies the core unchanged.
