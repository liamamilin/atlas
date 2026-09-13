# Research Notes — Real Estate Transaction Management

Research date: 2026-09-09
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a Real Estate Transaction Management application really is, from real products: what the unit of record is, what lives on it, how work moves from accepted offer to closing, who uses it, and where its boundaries sit against the neighboring real-estate Types already processed in §17 (brokerage CRM, listing platform, showing platform, development management, investment management) and adjacent Types outside §17 (mortgage origination, home inspection, title & escrow closing, legal matter management, generic CLM).

## Initial Boundary

Working hypothesis at Understand step:

- This Type is the system of record for **the transaction file itself** — the record of one real-estate deal (sale/purchase, sometimes lease) from accepted offer / executed contract to closing (or fallout).
- It is NOT the client-relationship system (Real Estate Brokerage CRM holds that), NOT the public venue (Property Listing Platform), NOT the viewing schedule (Property Showing Platform), NOT the lender's loan case (Mortgage Origination Platform), NOT the inspection order (Home Inspection Application).
- Nearest confusion risks: (1) post-contract checklists embedded inside brokerage CRMs (packaging question, forward-flagged by the brokerage-CRM pass), (2) title & escrow closing platforms that manage the same transaction from the settlement side, (3) generic contract lifecycle management, (4) e-signature tools (capability, not Type).

## Research Questions

1. What is the unit of record — one file per transaction? Per side (buy/list)? When does it open and when does it end?
2. What content lives on the file: documents, dates, tasks, parties, statuses, money?
3. What are the core workflows: document drafting/filling/signing, checklist/timeline work, compliance review, closing coordination?
4. What roles and permission structures exist (agent, transaction coordinator, broker/admin, clients, service providers)?
5. How do statuses/lifecycle stages work (under contract → pending/escrow → closed / fallen through)?
6. What integrations feed the file (MLS, association forms, CRM, back office/commission, title)?
7. Variants: side of deal, transaction type (sale vs lease), packaging (standalone vs CRM-embedded vs back-office module vs closing-platform), regional regimes (US state/association forms vs UK conveyancing-style legal-side files).
8. Boundaries: vs brokerage CRM (embedded checklists), vs title/escrow closing platforms, vs CLM, vs mortgage origination, vs home inspection.

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| Dotloop (Zillow) | agent/deal-loop, document-centric; SMB + brokerage tiers | self-labels "Real Estate Transaction Management Software"; the loop-as-transaction philosophy; deep official FAQ/buyer's guide |
| Open To Close | transaction-coordinator checklist/automation; team/TC tier | "fully customizable transaction management platform"; tasks/dates/documents/portal philosophy |
| Brokermint (now BoldTrail BackOffice, Inside Real Estate) | back-office suite module; brokerage/enterprise tier | Transaction Management as a named pillar beside Commission Automation/Accounting — the back-office packaging pole |
| Qualia | title & escrow closing-side; settlement-company tier | boundary sample: the same transaction managed from the settlement side (order + closing production) |
| SkySlope | brokerage compliance-centric | intended sample; UNREACHABLE this pass (see Source-access Limitation) |

## Sources

Fetched 2026-09-09:

- Dotloop — https://www.dotloop.com/ (root: page title "Real Estate Transaction Management Software"), https://www.dotloop.com/agents/ , https://www.dotloop.com/brokers/ (positioning + extensive FAQ), https://www.dotloop.com/real-estate-transaction-management/ ("Real Estate Transaction Management Buyer's Guide" — vendor's category framing)
- Open To Close — https://www.opentoclose.com/ , https://www.opentoclose.com/features , https://www.opentoclose.com/portals
- Brokermint / BoldTrail BackOffice — https://www.brokermint.com/ (pillar tiles), https://boldtrail.com/product-comparison-back-office/ (capability matrix)
- Qualia — https://www.qualia.com/ , https://www.qualia.com/title-and-escrow (Core title & escrow production)

Attempted and abandoned (network rule: 1–2 failures then abandon):

- SkySlope — www.skyslope.com 403 (×2 paths), knowledge.skyslope.com transport error, skyslope.zendesk.com "help center no longer exists"
- Open To Close Intercom help article — timeout ×2
- Hoowla (UK conveyancing case management pole) — timeout ×2
- brokermint.com/transaction-management — returned binary video, not usable

## Product Observations

### Dotloop (evidence layer A — direct, official pages)

- Root page title: "Dotloop | Real Estate Transaction Management Software". Self-describes as "PEOPLEWORK, NOT PAPERWORK".
- The **loop** is the container: "Invite as many people as you need to the loop (transaction)" — loop ≡ transaction.
- Document-centric: create, edit, share, eSign, store documents in one place; robust PDF editor; split/rotate PDFs; document scanner; document templates; clause manager (reusable contract clauses); PDF attachments.
- **Forms ecosystem**: partnered with 180–190+ local/state associations and MLSs; association forms "auto-fill with property details so agents can submit offers in seconds"; brokerage proprietary forms made interactive on request.
- **Transaction templates**: "listing and buying real estate transaction templates that contain all the required forms, people and checklists"; templates per transaction type "(listing, buying, renting, etc.)"; placeholders for documents that originate outside the system (e.g., earnest money receipts); required fields for transactional data.
- **Lifecycle/status**: transactions viewed "based on their stage (under contract, in escrow, closed, etc.)"; dashboards include "deals that fell through"; automated workflows keyed on "transaction type or stage" — e.g., "as soon as a transaction goes under contract, set up logic to notify ... to start the review process".
- **Compliance review**: agents "submit documents for review"; transaction coordinators "go through the review process, add notes and request changes"; custom review statuses (e.g., "Awaiting review"); automated compliance notifications; admin mobile oversight (approve, revoke, submit for review).
- **Audit trail / activity log**: "tracks every action taken throughout the entire deal... who did what and when"; eSignature verification; document history incl. version history and field-level changes; downloadable text-message logs; positioned explicitly as audit protection.
- **Acting on behalf**: TCs "share, edit, communicate and modify transactions on behalf of any agent" with the activity log recording who actually acted.
- **Participants**: unlimited participants; invite service providers (lenders, title, inspectors, attorneys, movers) into the transaction; clients; add-to-team access.
- **Offer-stage support**: Easy-Offer Links — secure public links to a set of offer documents for a listing (pre-contract offer handling lives on the same platform).
- **Task management**: task templates; assign tasks with due dates (brokers can "assign tasks and set due dates" on any transaction).
- **Integrations**: 75+ integrations — CRMs (BoomTown, Market Leader, Follow Up Boss, LionDesk, CINC), Earnnest (earnest-money delivery), Notarize, QuickBooks, Google Drive; open API (data export emphasis in buyer's guide).
- **Brokerage reporting**: agent pipeline, transaction status, multi-office views, agent performance, deals per agent, geographic inventory; push transaction data to back office for commissions/financials ("creating 1099s").
- Signup roles include Realtor/Agent, Transaction coordinator, Brokerage manager — plus adjacent service roles (mortgage, escrow/title, attorney, inspection) — corroborates the actor ecosystem.
- Vendor's own category floor (buyer's guide): "A true real estate transaction management software should give you the ability to create, share, eSign and store documents — at the very least"; minimum category expectation = eSignature with autofill + storage + CRM/back-office integration.

### Open To Close (evidence layer A)

- Self-label: "fully customizable transaction management platform for Real Estate professionals"; tagline "organize your tasks, emails, documents and dates all in one place".
- **Transaction record with custom fields**: create any field type (text/description/number/decimal/choice) per transaction; every field becomes a merge field usable in email/text templates — the file carries arbitrary structured deal data.
- **Task templates**: "one of the main powerhouses"; tasks keep transactions on track; completing a task can auto-send emails/texts; past-due notifications.
- **Email/text automation**: smart email templates with merge fields, contact roles, file roles; automated text triggers "set up for several notifications throughout our buy-side and list-side processes" (customer quote on official page) — side-of-deal process separation is first-class ("task templates for both seller and buyer sides").
- **Document tracking**: "Know what's signed, what's missing, and what's fully executed"; documents organized in folders; merge/split; received via email; emailed out; custom buttons.
- **Dates**: "Clear Deadlines — quickly see all important dates. Tracking all important dates in one place" — the deadline layer is a first-class surface.
- **Permissions**: global user permissions, task responsibilities, "assign who is responsible for what inside of the transaction" — per-file responsibility assignment.
- **Client portal**: buyers, sellers, and agents get portal access; view "a timeline of important dates, tasks, documents, contacts"; direct messaging; "set permissions on the client portal so the client will only see what you want them to see"; mobile app portals.
- **Contacts**: contact management (CRM-lite) with transaction history per contact; tables/segments over transactions, listings, contacts with custom filtering and permissions.
- Customer logos: KW, RE/MAX, Compass, eXp, Century 21 — team/brokerage adoption of the TC-led pole.

### Brokermint / BoldTrail BackOffice (evidence layer A — capability level; no help-center depth reached)

- Brokermint root page: "Meet BoldTrail BackOffice: The Next Generation of Brokermint" — five pillars as tiles: **Commission Automation, Transaction Management, Accounting, Agent Management, Reporting & Analytics**. Transaction Management is a named pillar of the brokerage back office.
- Capability matrix (all BackOffice packages): Transaction Management; Commission Automation; eSignature & Templates; Reporting & Analytics; Team Management; QuickBooks Integration; Forms; Agent Management & Onboarding; Multiple Office Locations; **Co-Brokered Sales**; Pipeline.
- Front office product (BoldTrail Platform) lists "Transaction Integration" (not transaction management) among its components — corroborates the front-office/back-office seam: the CRM integrates to the transaction record rather than being it.
- Login domain my.brokermint.com; marketed to enterprise brokerages.

### Qualia (evidence layer A — boundary sample, closing side)

- Self-label: "Digital Real Estate Closing Platform and Settlement Software"; "Real Estate Closing Software". Suite: Core (Title & Escrow Production Software), Connect (secure closing portal for clients/agents), Atlas (enterprise closing system), Shield (wire fraud detection), Marketplace (vendor operations), Assure (title insurer platform), Resware (title production).
- **Order as the file**: "Quickly Open Orders... AI reads your documents and extracts relevant fields to open the order" — a purchase-and-sale contract PDF opens the order; smart tags pull order data into closing documents.
- **Workflow/tasks**: dynamic workflows with task triggers "associated with contacts, transaction types or actions on an order"; task assignment incl. round-robin/equal-load groups; in-app chat/video collaboration.
- **Title production**: title commitment and policy production, underwriter integrations, rate management, policy issuance (CPL + policy jacket) — closing-side content absent from brokerage-side files.
- **Vendor ordering**: order title search / tax search "the moment you open a file" via vendor marketplace.
- **Accounting**: smart balancing (order accounting), bank integrations, three-way reconciliations, aggregate payments — escrow/settlement money machinery.
- **Closing management**: calendar scheduling of closings with all parties, templated emails, documents within the system, eRecording (Simplifile).
- Audience: title & escrow companies; also sells Connect to real estate agents and homebuyer-facing portals. Marketing metrics: order volume, turn time, consolidation of title production/accounting/reporting.

### SkySlope — NOT REACHED

All official surfaces failed (see Sources). No claims are based on SkySlope. Market context only: it is widely known as a brokerage compliance/transaction-file platform; per the evidence rules, this pass does not use it to support any assertion. Its absence is partly compensated by Dotloop's deep compliance-review documentation (submit-for-review, review statuses, notes/request changes) and BoldTrail BackOffice's brokerage back-office capability set.

## Cross-product Comparison

| Structure | Dotloop | Open To Close | BoldTrail BackOffice (Brokermint) | Qualia (Core) |
|---|---|---|---|---|
| Unit of record | loop (transaction) | transaction (fully customizable) | transaction (named pillar) | order (title & escrow) |
| Anchored to property + parties | yes (property autofill, parties invited) | yes (transaction details, contacts with roles) | yes (implied; co-brokered sales) | yes (order from purchase contract) |
| Document set on the file | create/edit/share/eSign/store; association forms; clause library | documents in folders; signed/missing/fully-executed tracking | eSignature & Templates; Forms | contract → closing documents; title commitment/policy |
| E-signature on the file | yes (core philosophy) | tracks signature state (external execution common) | yes (eSignature & Templates pillar) | closing-side eClosing products (separate suite members) |
| Dates/deadline layer | stage-triggered workflows; due dates on tasks | first-class "Clear Deadlines" surface | pipeline | closing calendar; workflow triggers |
| Task/checklist layer | task templates; required fields | task templates = core philosophy | team management | dynamic workflows + task management |
| Status lifecycle | under contract → in escrow → closed; fell-through | transaction tables/segments (customizable) | pipeline | order open → close |
| Compliance review | submit-for-review; review statuses; notes/request changes | permissions/responsibility per file | brokerage back-office oversight | settlement-company compliance posture (security framing) |
| Audit trail | every action; e-sign verification; field-level history | activity via templates/automation | not directly evidenced | audit-ready reconciliations; in-system communication |
| Participant sharing | unlimited participants; service providers; acting-on-behalf | contact roles; client portal with scoped permissions | co-brokered sales | Connect portal for clients/agents |
| Money content | earnest-money receipt placeholders; commission push to back office | custom fields (arbitrary) | commission automation pillar beside transaction management | full settlement accounting (balancing, reconciliation) |
| Feeds/integrations | MLS + association forms; CRM integrations; QuickBooks | API; forms product | QuickBooks; CRM/contact sync; front-office transaction integration | underwriters; banks; eRecording; marketplace vendors |
| Primary actor | agent + TC + broker | TC/team | brokerage back office | title & escrow company |

Reading of the comparison:

- The **file-per-transaction anchored to property + parties, carrying its document set, its dates, its tasks, and a status toward close** is present in every sampled product including the closing-side boundary sample — this is the Type's stable skeleton (evidence layer B→C).
- **How the money, the compliance gate, and the actor are weighted differs by pole**: agent/document pole (Dotloop), TC/automation pole (Open To Close), back-office pole (BoldTrail), settlement pole (Qualia).
- Compliance review machinery is deepest at the document/brokerage pole (Dotloop explicit; SkySlope known-unreached). At the back-office pole the compliance gate is implied by suite content rather than directly evidenced on fetched pages — held common-at-brokerage-pole, not definitional.
- E-signature: definitional-adjacent capability. Dotloop treats eSign as core; Open To Close tracks executed/signed/missing states and commonly receives externally-executed documents; BoldTrail bundles eSignature as a pillar capability. The invariant is **the executed document set held on the file**, with in-product e-signature as the dominant modern implementation. (This distinction matters for the historical check.)

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The transaction file of record** — a persistent identified record for one real-estate transaction, anchored to a specific property and its parties (buyers, sellers, and their representing side), opened around the deal (commonly at offer/contract formation) and carried to its terminal event (closing, or termination/fall-through), then retained.
   - Remove → a checklist app or document store with no deal memory; a deal list = CRM/deal-board territory.
2. **The transaction's document set on the file** — the executed contract and the required accompanying documents (forms, disclosures, amendments, addenda, receipts) held together on the file with their execution/state (draft → out for signature → fully executed; versions; who signed what when).
   - Remove → a date tracker with no content; standalone e-sign tool territory.
3. **The contract-to-close timeline worked on the file** — the transaction's key dates, contingencies, and required steps tracked and worked toward closing, with the file's overall status visible (in progress → closed / fallen through).
   - Remove → a document archive nobody works from.

Jointly-held load-bearing:

- 1 alone = bare deal registry
- 2 without 1 = loose document/e-sign collection
- 3 without 1+2 = generic deadline tracker
- 1+2 without 3 = archive without motion
- 1+3 without 2 = deal tracker with no file content
- 2+3 without 1 = documents and dates with nothing binding them to one deal

### L1 — Common Mature Structure

- E-signature and interactive document filling on the file (dominant modern implementation of "executed document set"; historically wet-ink)
- Transaction templates per transaction type (listing / buyer / lease) that auto-create the required documents, participants, and tasks; required fields; clause libraries
- Task/checklist layer per file with owners, due dates, and automated notifications (email/text triggers on task completion, stage change, or approaching deadlines)
- Compliance/oversight review on the brokerage side: submit-for-review → reviewer approves or requests changes; review statuses; activity log/audit trail (who did what when, e-sign verification, version and field-level history) framed as audit protection
- Participant model: agent(s), transaction coordinator (with acting-on-behalf), broker/admin oversight, clients via permission-scoped portals (timeline, documents, messaging), invited service providers (title/escrow, lender, inspector, attorney)
- Status/pipeline surfaces: transactions by stage, fallout visibility, brokerage-level reporting (agent productivity, offices, geographic mix)
- Feeds: MLS/listing data and association/state form libraries feeding property and form content; CRM handoff upstream; back-office/commission handoff downstream

### L2 — Variant / Optional Structure

- **Side of deal**: listing-side vs buyer-side files, tracked as separate processes/templates (explicit at Open To Close; templates per type at Dotloop)
- **Transaction type coverage**: sale (buy/list) is the center; leases/rentals commonly included (Dotloop "listing, buying, renting")
- **Actor center**: agent-led vs TC-led vs brokerage-compliance-led vs settlement-company-led — a market-structure axis, not a Type boundary within the documented population
- **Packaging**: standalone product vs checklist/timeline embedded in a brokerage CRM vs module of a back-office suite (beside commission/accounting) vs closing platform of a title/escrow company
- **Money content on the file**: from receipt placeholders and custom fields (light) to commission worksheets/disbursement (back-office pole) to full settlement accounting (closing pole — boundary)
- **Regional regime**: US state/association form + escrow pattern documented; UK conveyancing-style legal-side files inferred as the regional analog (UNVERIFIED this pass — see Boundary Findings)
- Mobile-first vs desktop posture; client-portal depth; AI extraction/automation (era-current)

### L3 — Vendor-specific (research notes only)

- Dotloop: "loop" terminology; Easy-Offer Links; Business+ success managers; specific integration roster (Earnnest, Notarize)
- Open To Close: automation recipes (task-completion-triggered texts), fully custom field engine, Boise framing
- BoldTrail: Co-Brokered Sales machinery; white label; package tiers
- Qualia: Smart Tags; CPL/policy jackets; Clear agentic AI; Shield wire-fraud; marketplace vendor network
- (SkySlope compliance file tiers: known market context, UNREACHED — no claims)

## Vendor-specific Findings

See L3 above. Additional notes:

- Dotloop's buyer's guide is a vendor-authored category definition ("at a minimum, an eSignature platform with autofill, maybe some storage... possibly integration with CRM/back-office"). Used here only as evidence of market framing (the category floor per a leading vendor), not as the canonical definition.
- Dotloop's "190+ associations/MLSs" and "75+ integrations" are product-specific marketing numbers — recorded, not generalized.
- BoldTrail's front office lists "Transaction Integration" while BackOffice lists "Transaction Management" — vendor-published confirmation of the CRM↔transaction-file seam.

## Boundary Findings

1. **vs Real Estate Brokerage CRM (forward flag RATIFIED from this side).** The brokerage-CRM pass held that sampled CRMs embed post-contract checklist/timeline layers at varying depth (in-product at SMB pole, integrations at open-CRM pole, separate back-office product at enterprise pole) and flagged the transaction file's own system of record for this pass. This pass confirms: the defining center of this Type is the transaction file (documents + executed contract set + contract-to-close timeline + file status). CRM-embedded checklists are packaging, not the Type: they ride on the CRM's relationship record, whereas the transaction file is its own record with its own document set, review machinery, and lifecycle. Removal tests: strip the relationship/pipeline from a brokerage CRM → the transaction file product still stands (Dotloop, Open To Close exist without any CRM record); strip the file/documents/timeline from this Type → only a relationship pipeline remains = CRM territory. Corroboration: BoldTrail itself splits front office (CRM with "Transaction Integration") from BackOffice ("Transaction Management") — the vendor keeps the two as separately named structures.
2. **vs Property Listing Platform** — the venue holds public expiring offers and routes interest; this Type holds one deal's private file after interest matures into a contract. Strip the public venue → this Type unaffected; strip the per-deal file → listing venue unaffected.
3. **vs Property Showing Platform** — viewings/schedule-of-record vs deal file; showing outcomes appear on the transaction file at most as context.
4. **vs Mortgage Origination Platform** — lender-side case: borrower + loan + subject property under program eligibility; the transaction file tracks the financing contingency as one timeline item, not the loan. Different professional actor (lender vs brokerage), different record content (loan case vs deal file).
5. **vs Title & Escrow Closing Platform (Qualia pole)** — same transaction, settlement-side realization: the order file is opened from the purchase contract but carries title production (commitment/policy), escrow/settlement accounting (balancing, reconciliation), vendor ordering, and eRecording. The brokerage-side file does not produce title commitments or balance escrow ledgers. Sampled evidence: Qualia self-labels as title & escrow production/closing software and markets to title & escrow companies — a distinct product population sharing one seam (the closing event). Keep-both: brokerage transaction file vs settlement closing platform.
6. **vs Legal Matter Management / conveyancing case management (regional legal-side actor)** — in jurisdictions where the transaction is legally driven (e.g., UK conveyancing), the deal file is held by the conveyancer/law firm as a matter. UNVERIFIED this pass (Hoowla unreachable ×2; structural inference only): flagged as a boundary issue for future review — likely seam = the matter-of-record (legal) vs the deal file of the selling side's professionals (this Type), with the transaction timeline shared.
7. **vs Generic Contract Lifecycle Management** — CLM centers the contract artifact and its lifecycle across a business generally; this Type centers the property deal file with real-estate-specific timeline semantics (contingencies, escrow/closing), an association-forms ecosystem, brokerage compliance review, and participant roles. A CLM lacks the property/transaction substrate; a transaction file lacks enterprise CLM's clause negotiation/approval generality.
8. **vs Home Inspection Application** — per that pass, "transaction fields attach to the order; the order remains the container." Reversed here: the whole transaction is the container; the inspection appears as a tracked contingency/step and its report as a document on the file.
9. **vs E-signature Application** — e-signature is a capability of the document layer (dominant implementation), not the defining structure: the invariant is the executed document set on the file, historically satisfied with wet-ink signatures.
10. **vs Transaction Legal Management (§11)** — that leaf serves legal teams managing transactional legal work; this Type serves the selling side's real-estate professionals on the deal itself. Name proximity only; no evidence of population overlap this pass.

## Historical / Market-Sample Check (§24)

- Paper-era brokerage transaction file: a folder per deal holding the executed contract, counteroffers, disclosures, receipts; a key-date sheet (contingency deadlines, closing date); a checklist of documents to collect; the broker's review sign-off before closing/commission. This satisfies all three L0 structures with no software, no e-signature, no portals, no MLS feed. E-signature, task automation, client portals, forms autofill, and CRM/back-office integrations are all era-current layers, not definitional.
- Regional/actor check: the closing-side settlement file (Qualia) shares the skeleton (file + documents + dates + tasks) but adds title/escrow production — held as a neighboring Type sharing the closing seam, consistent with the vendor's own category labeling. The legal-side conveyancing file is presumed to share the skeleton too but was not verifiable — recorded as a boundary issue, not folded silently into the definition.
- The definition does not depend on US-specific machinery: no MLS, escrow, or state-form requirement is in the core; the forms ecosystem is a common implementation of "document set".

## Uncertainties

- SkySlope (the brokerage-compliance pure-play) was unreachable; the compliance-review leg rests on Dotloop's explicit documentation plus the brokerage-CRM pass's independent observation that enterprise poles pair "separate back-office products". Compliance review is held common-at-brokerage-pole, not definitional.
- UK/AU/regional legal-side files (conveyancing case management) not fetched; the regional-regime variant and boundary 6 are structural inference.
- BoldTrail BackOffice evidence is at capability-matrix depth (no help-center); internal mechanics of its transaction records not asserted.
- Open To Close's exact status vocabulary is customizable; no canonical status list is claimed beyond what products document (Dotloop's "under contract, in escrow, closed" is product-documented phrasing, held as an example, not a standard).
- Whether lease/rental files constitute a variant or an occasional second population: Dotloop documents "renting" templates; other samples silent — held variant.

## Final Synthesis

A Real Estate Transaction Management application is the deal file's system of record: one persistent file per real-estate transaction, anchored to the property and its parties, holding the transaction's executed document set together with its contract-to-close timeline and a visible status toward closing or fallout, worked by the selling side's professionals (agents, transaction coordinators, brokerage staff) with scoped access for clients and invited service providers. Mature products add e-signature/filling, per-transaction-type templates, task/checklist automation with deadline triggers, brokerage compliance review with audit trails, participant portals, forms/MLS feeds, and hand-offs to CRM upstream and commission/back-office downstream. The Type is bounded by the brokerage CRM (relationship record), the listing platform (public venue), the showing platform (schedule), the lender's origination case, the settlement company's closing order, and legal-side matter files — same transaction, different records, different professionals.
