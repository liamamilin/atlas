# Research Notes — Supplier Portal

## Research Goal

Understand what a Supplier Portal really is from real products, from the supplier's side of the trading relationship: what the supplier can see and do, how the buyer controls participation, how documents flow in both directions, and where this Type ends and neighboring Types begin — above all Supplier Management Platform (the buyer-side record this surface feeds), Seller Portal (the marketplace-direction look-alike), the buyer-side procurement Types (Procurement Management Platform, Procure-to-pay, Purchase Order Management), EDI Platform, Manufacturing Supplier Collaboration (§16), and Government Procurement Platform (§24).

## Initial Boundary

Hypothesis before research: the supplier-facing interaction surface operated by (or on behalf of) a buying organization — suppliers log in, see the buyer's purchase orders and requests, respond (confirm/decline/bid/invoice), and keep their own data current. Nearest neighbors:

- Supplier Management Platform (§10 sibling, processed 2026-09-08) — buyer-side system of record; its pass held the seam: "portal = supplier-facing interaction surface; SMP = buyer-side system of record." This pass ratifies or adjusts from the portal side.
- Procurement Management Platform / Procure-to-pay / Purchase Order Management (§10, processed) — all three passes flagged "Supplier Portal (external slice)" for joint review; this pass discharges those flags.
- Seller Portal (§05.23, processed 2026-09-07) — shape-adjacent external-party portal; its pass held: procurement direction (PO/ASN semantics, no consumer demand) vs marketplace selling.
- Customer Portal (§07, processed 2026-09-08) — mirror image (sell-side customer self-service).
- EDI Platform (§13) — transport machinery vs human surface.
- Manufacturing Supplier Collaboration (§16, unprocessed) — planning/schedule/fulfillment content.
- Government Procurement Platform (§24, processed) — solicitation/public-rules frame.
- Partner Relationship Management / Dealer portals (§07) — sell-side partner direction.
- Accounts Payable Automation (§08) — invoice-only "vendor portals" lean toward AP tools.
- Portal naming overload: the information-portal pass (2026-09-07) flagged that "portal" spans many distinct Types and recommended later *-portal passes cite the seam (transaction of record vs information access). This pass cites it.

## Research Questions

1. Who is the primary user — the supplier's people or the buyer's people? What exactly does each side do?
2. What documents/objects does the supplier see, and which of them originate from the buyer?
3. What responses can the supplier record, and how do they flow back into the buyer's systems?
4. How is participation established and controlled (invitation, self-registration, per-supplier activation, qualification)?
5. Is money mediated in the portal, or does settlement stay in finance systems?
6. Is the portal the system of record, or a surface in front of one?
7. What is the boundary vs Supplier Management Platform, Seller Portal, EDI, Manufacturing Supplier Collaboration, Government Procurement, and the buyer-side procurement Types?

## Representative Products

| Product | Pole | Tier reached | Customer tier |
|---|---|---|---|
| Microsoft Dynamics 365 Supply Chain Management — Vendor collaboration module | ERP-embedded supplier-facing module | Tier 1 (Learn docs, 2 full pages + search-index metadata) | enterprise |
| Microsoft Dynamics 365 — Supplier Engagement (preview) | dedicated portal app + buyer-side lifecycle app (convergence pole) | Tier 1 (Learn overview) | enterprise |
| Precoro — Supplier Portal | mid-market procurement-platform module | Tier 1 (help center, 2 full pages + section index) | mid-market |
| SAP Business Network — supplier account | multi-buyer network account | Tier 2 (official product page incl. operational FAQ) | enterprise network |

Deliberately different philosophies: ERP module (document-exchange focus, explicitly the non-EDI alternative), mid-market module (PO/RFP/invoice loop with matching), network account (one supplier account serving many buyers, growth/lead extras), and the preview convergence pole (portal + onboarding/qualification in one solution). Coupa Supplier Portal was unreachable in prior sibling passes (403×2 + transport error) and was not retried per network rules; Oracle Fusion supplier-portal chapters sit behind a JS-rendered TOC (book index and toc.html both JS-empty); SPS Commerce 404'd twice (abandoned). These are recorded as market anchors only, with zero operational claims drawn from them.

## Sources

- Microsoft Learn — Vendor collaboration with external vendors: https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/vendor-collaboration-work-external-vendors (fetched 2026-09-08)
- Microsoft Learn — Vendor collaboration with customers: https://learn.microsoft.com/en-us/dynamics365/supply-chain/procurement/vendor-collaboration-work-customers-dynamics-365-operations (fetched 2026-09-08)
- Microsoft Learn — Supplier Engagement overview (preview): https://learn.microsoft.com/en-us/dynamics365/supply-chain/supplier-engagement/supplier-engagement-overview (fetched 2026-09-08)
- Microsoft Learn search API (located the vendor-collaboration page set; snippets for set-up-maintain-vendor-collaboration, purchase-order-approval-confirmation, manage-vendor-collaboration-users, business events) (fetched 2026-09-08)
- Precoro Help Center — Supplier Portal: https://help.precoro.com/suppliers-portal-1 (fetched 2026-09-08)
- Precoro Help Center — I Am a Supplier. How Do I Use the Supplier Portal?: https://help.precoro.com/i-am-a-supplier.-how-do-i-use-a-suppliers-portal (fetched 2026-09-08)
- Precoro Help Center — How to use Precoro (section index confirming Suppliers Portal + Supplier Registration sections): https://help.precoro.com/how-to-use-precoro (fetched 2026-09-08)
- SAP — SAP Business Network supplier account overview: https://www.sap.com/products/business-network/suppliers/overview.html (reached via https://www.ariba.com/supplier redirect; fetched 2026-09-08)

Failed/abandoned: docs.oracle.com Fusion book TOCs (JS-empty ×2 — abandoned; static EBS-doc guess returned the wrong book, abandoned); spscommerce.com (404 ×2 — abandoned); coupa.com (prior passes 403 — not retried).

## Product Observations

### Microsoft Dynamics 365 SCM — Vendor collaboration module (evidence layer A, Tier 1)

From "Vendor collaboration with external vendors":

- Framing: "The Vendor collaboration module is targeted at vendors who don't have electronic data interchange (EDI) integration with Microsoft Dynamics 365 Supply Chain Management. It lets vendors work with purchase orders (POs), invoices, consignment inventory information, and requests for quotation (RFQs), and also lets them access parts of their vendor master data."
- Buyer-side control: per-vendor **Collaboration activation** field on the vendor account — *Active (PO is auto-confirmed)* vs *Active (PO is not auto-confirmed)*; a scheduled batch job processes auto-confirmations. Buyer option: whether the vendor sees **price information** (unit price, discounts, charges) on POs.
- Buyer-configurable response messaging: "When vendors respond to a PO that you send them, they see one of three message boxes, where they must confirm that they want to accept the PO, reject it, or accept it with changes" — the text of each message is buyer-defined, multi-language.
- PO exchange loop: PO prepared in SCM → status *Approved* → buyer selects **Send for confirmation** → PO status *In external review* → vendor sees it on **Purchase orders for review** → vendor can **accept / reject / accept with changes**, add comments. Line-level changes: dates, quantities, split lines into multiple deliveries, substitute an item (entered as text); "You can't change pricing information or charges, but you can use notes to make suggestions." Buyer processes the response (**Process PO update**); only header changes and line dates/quantities auto-update; other changes manual. Changed POs are sent as **new versions** with a version suffix; **Purchase order vendor confirmation history** tracks all versions and responses. Cancellation is also sent to the vendor to confirm or reject. Attachments marked *External* are visible to the vendor.
- Vendor-side workspaces (from "Vendor collaboration with customers"): **Purchase order confirmation** (lists: *Purchase orders for review* / *Awaiting customer action* / *Open confirmed purchase orders*; pages: review list, confirmation history, open confirmed, all confirmed — "You can use this list to monitor POs that you can send invoices for"); **Vendor bidding** (RFQ invitations, returned bids, bids in progress, awarded bids, lost bids; public-sector published RFQs with self-invitation where enabled; questionnaires may gate bid submission; alternates; recall before expiration); **Vendor information** ("As a vendor, you can access part of the information that the customer maintains in the vendor master record... vendor name, addresses, contact information, contact persons..., identification numbers, tax registration numbers, procurement categories that the vendor is approved to sell to the customer in, and information about certifications" — requires *vendor admin (external)* role); **Invoicing** workspace (separate doc: vendor portal invoicing workspace).
- Consignment inventory: three vendor-visible pages — *Purchase orders consuming consignment inventory*, *Products received from consignment inventory* ("Vendors can use this information to invoice the customer"), *On-hand consignment inventory*.
- Channel pluralism: "Vendors don't have to confirm a PO by using the vendor collaboration interface. They can also send an email or communicate their acceptance of a PO via other channels. You can then manually confirm the order." (Buyer receives a warning when confirming without a portal response.)
- Business events fire on portal actions: "the trigger occurs when the Accept button is clicked on the Purchase order confirmation page in the Vendor collaboration portal."
- User provisioning is buyer-side: "request the provisioning of new vendor collaboration users"; security roles for vendor users; a mobile workspace exists.

### Microsoft Dynamics 365 — Supplier Engagement (preview) (evidence layer A, Tier 1)

- Three components: **Supplier Engagement app** (buyer-side Power Platform model-driven app: "Registering new suppliers and managing the new-supplier lifecycle from qualification to approval; Recording supplier capabilities and maintaining certificates; Reviewing risks and tracking corrective actions; Managing user accounts that grant access to the supplier portal") + **supplier portal** ("a Microsoft Power Pages site for external supplier representatives. Through the portal, suppliers can: View and respond to requests for quotation; Review purchase orders; Submit invoices; Manage consignment inventory; Update organization details and maintain certificates; Provide compliance information when required. The portal serves as the primary channel of communication between suppliers and your organization.") + **Supply Chain Management** ("stores and processes the data that is exchanged with suppliers through the Supplier Engagement app and the supplier portal").
- Explicit architecture statement: the portal is a surface; SCM is the record. "Supplier Engagement replaces the older vendor collaboration interface with broader capabilities, including global vendor data management, a dedicated Power Pages portal, and lifecycle processes such as qualification and termination."
- Onboarding convergence: self-registration ("a supplier registers themselves through the anonymous registration page on the supplier portal. The registration request is created as a prospect global vendor... review... if approved, the supplier is invited to the supplier portal to complete the onboarding process") or internal registration; guided onboarding form (contact information, addresses, business profile, certificates, capabilities) + final questionnaire; lifecycle *prospect → qualified → disqualified*; qualified global vendors are *released* to legal entities as local vendor accounts, "making the supplier available for transactional processes such as purchase orders and RFQs."

### Precoro — Supplier Portal (evidence layer A, Tier 1)

From "Supplier Portal":

- Definition: "The **Supplier Portal** in Precoro is a platform where suppliers can view and respond to requests for proposals and purchase orders, submit invoices, and communicate with you about orders. It simplifies collaboration by keeping all order-related activities in one place."
- Key features: "1. Receive and manage POs... such as downloading or invoicing. 2. Send invoices: Create and submit invoices for received orders directly within the portal. 3. Direct communication: Use the built-in communication tools to discuss orders or invoices. 4. Document Management: Upload and manage attachments. 5. Participate in RFPs: Receive, respond to, and track Requests for Proposals. 6. Exchange information: set up Custom Document Fields available to suppliers... such as order tracking numbers."
- Layout: left-side menu — Purchase Orders / Invoices / Requests for Proposals / Configuration. "The Supplier Portal dashboard is similar to Precoro users' accounts."
- Sync: "Precoro and the Supplier Portal have real-time synchronization"; supplier profile changes sync to Precoro; currency is buyer-editable only. Deactivated supplier → buyer edits directly; reactivation syncs back.
- PO actions: export PDF/XLSX; download/upload attachments; comments to buyer; **Create Invoice** from the submitted PO; edit visible custom fields; **Decline Document** with a mandatory reason. Declined PO: status *Declined* in portal, *In Revision* on the buyer side; buyer banner: "This document was declined by supplier. You can take it on revise and make changes, or cancel it." Buyer revises → **Confirm** → "Precoro will automatically send it to the supplier" → supplier notified by email.
- Invoice loop: invoices created from POs go through the buyer's **approval workflow**; routed for **matching** to the PO initiator "if the Invoice includes items that are not listed in the PO" or "the total Invoice amount exceeds the PO sum and the specified Tolerance Limit." Supplier-visible statuses: *Matching/Pending, Rejected/Canceled, Draft, Approved, Partly Paid/Paid*. Comments and email notifications on changes. Optional mandatory Issue Date configuration.
- RFP loop: receive RFPs; reject specific items or the whole proposal (all items rejected → status *Rejected*); enter estimated delivery date; per-item prices; attachments/notes; submit.
- Custom fields: supplier fields viewable/fillable by both sides; document fields flagged "available to suppliers."
- Per-supplier deactivation: buyer unchecks the **Supplier Portal** checkbox on the supplier record; consequences: portal drafts deleted, fully invoiced POs removed from the portal, partially invoiced POs remain for remaining quantities.
- From "I Am a Supplier...": entry by invitation email → accept → register (create password) → profile setup ("primary business and banking information... attachments (e.g., Bank statements, W-9 Forms, tax documents)" — "This data will be available to the company's business account users in Precoro, who invited you"); some fields prefilled by the inviting buyer; add portal users (**User Management → Invite User**); login via credentials or email links (auto-login window documented); invoice tracking via status in the page corner; communication via notes/comments on documents.

### SAP Business Network — supplier account (evidence layer A, Tier 2)

- Positioning: "SAP Business Network supplier account — Manage customer transactions, streamline business processes, and achieve greater visibility and business growth."
- Included: "Electronic order management and e-invoicing; Lead generation; Business insights and analytics; Access to thousands of buyers on the world's largest business network."
- Visibility: "document and payment status updates and turn actionable insights into transactions with KPI analytics."
- Profile: "Searchable company profile" — upload business certifications, share sustainability ratings, human rights information.
- E-invoicing: "automatic network validation processes"; "converting a variety of document formats into e-invoices and rapidly delivering them to your customers"; "Get paid on time with more accurate invoicing."
- Connection model (FAQ): "you need to have both a supplier account and an invitation to transact from your customer. Two scenarios: 1. Receive an invitation to transact (either through a Trading Relationship Request, or from an interactive purchase order), inviting you to create a new account or connect to an existing one. 2. Create a new supplier account from supplier.ariba.com, then share the account number ID with your customer so they can establish the trading relationship."
- Account tiers: standard account free with unlimited documents but limited functionality; enterprise account fully enabled with fees after a transaction-volume threshold. Leads: unlimited public-sector RFIs free; up to three private-sector RFIs free, then a paid subscription.
- Network posture: "managing multiple customers in one place"; browser-only access ("An internet connection and a web browser are the only requirements").

## Cross-product Comparison

| Structure | D365 Vendor collaboration | D365 Supplier Engagement (preview) | Precoro Supplier Portal | SAP BN supplier account |
|---|---|---|---|---|
| Authenticated external supplier participation under buyer control | ✓ (per-vendor Collaboration activation; buyer provisions users; roles) | ✓ (buyer app manages portal user accounts) | ✓ (invitation + registration; per-supplier checkbox) | ✓ (account + customer invitation / Trading Relationship Request) |
| Buyer-originated documents surfaced for supplier action | ✓ (POs "In external review"; RFQs) | ✓ (POs, RFQs) | ✓ (POs, RFPs) | ✓ (orders; RFIs/leads) |
| Supplier response recorded back into buyer's process | ✓ (accept/reject/accept-with-changes; line changes; bids; profile edits) | ✓ (respond RFQs, review POs, submit invoices, update details) | ✓ (decline with reason; invoice from PO; RFP submission; profile) | ✓ (order management; e-invoices delivered to customers) |
| Confirmation/acceptance workflow on the buyer's order | ✓ (three response types; version suffix; confirmation history; cancellation confirmed) | ✓ (review POs) | ✓ (decline → In Revision → revised re-send) | ✓ (order management; details at Tier 2 only) |
| Invoice submission from the portal | ✓ (Invoicing workspace; separate doc) | ✓ ("Submit invoices") | ✓ (create from PO; approval workflow; matching rules) | ✓ (e-invoicing with network validation) |
| Supplier-visible status of documents/money | ✓ (PO statuses/versions; awaiting-customer-action list) | ✓ (via SCM data) | ✓ (Matching/Pending → Approved → Partly Paid/Paid) | ✓ ("document and payment status updates") |
| Sourcing participation (RFQ/RFP bids) | ✓ (Vendor bidding workspace; public-sector publishing) | ✓ | ✓ (RFPs with per-item pricing) | ✓ (RFI responses; lead generation) |
| Supplier profile / master-data self-service | ✓ (Vendor information workspace; certifications, tax IDs, categories) | ✓ (org details, certificates, compliance info) | ✓ (business + banking info, attachments) | ✓ (searchable company profile, certifications, sustainability) |
| Attachments + comments as the communication channel | ✓ (external attachments; comments) | ✓ ("primary channel of communication") | ✓ (notes/comments; attachments) | ✓ (document exchange) |
| Email notifications as entry points | ✓ (print management email; warnings) | — (not on fetched page) | ✓ (invitation, new-document, action emails; 48h auto-login) | — (not on fetched page) |
| Buyer-side system of record behind the portal | ✓ (SCM) | ✓ (SCM explicitly) | ✓ (Precoro) | ✓ (each customer's SAP Ariba/ERP on the other end) |
| Money mediated in the portal | — (invoices routed to AP; no settlement) | — | — (status shows Partly Paid/Paid; payment executed in finance/banking) | — (payment status visible; settlement outside) |
| Multi-buyer network account | — (single-buyer deployment) | — (single-buyer) | — (single-buyer) | ✓ (one account, many buyers) |
| Onboarding/qualification machinery in/through the portal | partial (buyer provisions; vendor info workspace) | ✓ (self-registration → prospect → qualified → released; onboarding form + questionnaire) | partial (invitation + profile; registration forms are a separate module) | partial (account creation + trading relationship) |
| Inventory/consignment visibility | ✓ (three consignment pages) | ✓ ("Manage consignment inventory") | — | — |
| Business model on the supplier side | included in ERP | included (preview) | included in platform | ✓ (standard free / enterprise fees; lead subscription) |
| Fulfillment notices (ASN/ship) documented in fetched pages | — | — | — | — |

Reading: the first five rows are present in every product that operates a supplier portal; the rows below diverge by packaging and business model. Notably, none of the fetched pages documents ASN/ship-notice creation as a portal feature — the fulfillment-notice association is market folklore for this Type but was not directly evidenced in this sample (see Uncertainties).

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **Buyer-anchored authenticated external participation.** External supplying organizations participate as identified, authenticated parties inside a surface operated under one buying organization's terms (or a network operator's terms acting for its buyers). Access is established and controlled from the buyer side — invitation, per-supplier activation, user provisioning, trading-relationship request — and is scoped to that trading relationship. Remove → the supplier's own back-office system, or a public website/file drop with no relationship frame.
2. **Buyer-originated trading documents surfaced for supplier action.** The buyer's operational documents — purchase orders above all, plus sourcing requests — arrive in the surface as actionable items addressed to the supplier. The supplier does not browse a catalog of opportunities; the documents come from the buyer's own procurement process. Remove → a vendor-registration form, a marketing/contact page, or a generic document exchange.
3. **Supplier-side responses recorded back into the buyer's process.** The supplier's actions — accept/reject/accept-with-changes, decline with reason, invoices created against orders, bids, profile and master-data updates, comments and attachments — are recorded against the buyer's documents and consumed by the buyer's procurement and finance systems. Remove → a one-way notification board or read-only feed.

Jointly-held is load-bearing:

- 1+2 without 3 = a read-only document feed (thin edge; every sampled product has response machinery)
- 2+3 without 1 = EDI-style transport / anonymous document exchange — D365 explicitly positions the portal as the alternative for vendors *without* EDI integration, confirming the account frame is what makes it a portal
- 1+3 without 2 = a supplier data-entry channel only — that is the Supplier Management Platform's self-service intake, not a Supplier Portal
- The portal is **not the system of record**: in every sampled product a buyer-side system (ERP, procurement platform, or the customer's system on the network's far end) holds the documents; the portal is the external surface over it (D365 Supplier Engagement states this as a three-component architecture).

### L1 — Common Mature Structure

- Order-confirmation workflow: accept / reject / accept-with-changes on the buyer's order; line-level changes (dates, quantities, splits, substitutions); change orders re-sent as new versions with history visible to both sides (D365, Precoro's decline→revise→re-send loop).
- Invoice creation and submission from orders, with the buyer's approval/matching machinery behind it and supplier-visible status including payment progress (D365 invoicing workspace, Precoro statuses, SAP BN e-invoicing + payment status).
- Sourcing participation: RFQ/RFP receipt, per-item or whole responses, submission, award/loss visibility (D365 Vendor bidding, Precoro RFPs, SAP BN RFIs/leads).
- Supplier profile / master-data self-service feeding the buyer's vendor record: identity, addresses, contacts, tax/registration numbers, banking details, certifications (D365 Vendor information, Precoro profile, SAP BN company profile, D365 SE onboarding).
- Attachments and comments/notes as the built-in communication channel on documents (all sampled).
- Email notifications as entry points into the portal (Precoro, D365 print-management email).
- Document status and version history visible to the supplier (D365 confirmation history, Precoro revision/status, SAP BN status updates).
- Supplier-side user administration (Precoro invite user; D365 vendor admin external role; D365 SE contact management).
- Buyer-side control switches: per-supplier activation/deactivation, field-visibility options (e.g., price information), buyer-defined response messaging (D365, Precoro).

### L2 — Variant / Optional Structure

- Packaging posture: ERP-embedded module (D365) vs mid-market procurement-platform module (Precoro) vs multi-buyer network account (SAP BN) vs dedicated portal application beside a buyer-side lifecycle app (D365 SE).
- Single-buyer deployment vs multi-buyer network account (one supplier account serving many customers, with subscription tiers and lead-generation extras — SAP BN pole).
- Onboarding/qualification convergence: self-registration, guided onboarding forms, questionnaires, qualification lifecycle gating release into transactional use (D365 SE; partial forms elsewhere) — this is where the portal absorbs Supplier Management Platform intake.
- Inventory/consignment visibility for the supplier (D365 consignment pages).
- Public-sector flavor: published RFQs, anonymous access, self-invitation (D365 public-sector extensions).
- Mobile companion surfaces (D365 mobile workspace).
- Fulfillment-notice and schedule collaboration (ASN/ship notices, forecasts): widely associated with manufacturing supplier portals in the market, but **not directly documented in the fetched sample** — held at the boundary with Manufacturing Supplier Collaboration rather than asserted as a portal capability.

### L3 — Vendor-specific (research notes only)

- D365: exact workspace/list names; *Collaboration activation* auto-confirm batch job; *Process PO update* one-shot semantics; line statuses (*Substituted*, *Split into schedule*); version suffix behavior; *External* attachment classification; business-event trigger on the portal Accept button; consignment page names; public-sector RFQ publishing entities and email tokens.
- Precoro: exact status vocabulary (*Matching/Pending, Rejected/Canceled, Draft, Approved, Partly Paid/Paid*); Decline Document mandatory reason; tolerance-limit matching rule; "available to suppliers" custom-field flag; per-supplier checkbox deactivation consequences; 48-hour email auto-login window; left-menu layout.
- SAP BN: standard vs enterprise account tiers and fee thresholds; promote subscription; three free private-sector RFI responses; UNSPSC category classification; Trading Relationship Request; supplier.ariba.com self-registration.
- D365 SE: global vendor / prospect / qualified / released lifecycle; party model; Power Pages portal; anonymous registration page; onboarding form composition.

## Rejected Findings

- **"Portal = supplier registration form"** — rejected: registration/profile self-service is the intake channel into the buyer's supplier record (SMP territory); the Type's center is the trading-document exchange. A registration-only portal lacks L0 leg 2.
- **"Money mediation as definitional"** — rejected: settlement stays in the buyer's finance systems in every sampled product; the portal shows status (including payment progress) but does not move money. This is the sharpest contrast with Seller Portal, where operator-mediated money is structural.
- **"The portal as system of record"** — rejected: D365 SE states the three-component split explicitly; Precoro syncs the portal against the Precoro record; SAP BN documents belong to each customer's systems. The portal is a surface.
- **"ASN/ship notices as definitional or even common-in-sample"** — rejected for this pass: not documented in any fetched page; held as an uncertainty and pushed to the Manufacturing Supplier Collaboration boundary.
- **"Supplier portal = Supplier Management Platform"** — rejected: the SMP pass held the seam and this pass ratifies it — surface vs record; the portal feeds the record and the record's standing gates the portal.
- **"Lead generation / growth services as definitional"** — rejected: network-pole extras (SAP BN), not part of the document-exchange core.

## Boundary Findings

- **vs Supplier Management Platform** — RATIFIED from this side (SMP pass held the seam first): the portal is the supplier-facing interaction surface; the SMP is the buyer-side system of record for the supplier population. The portal feeds the record (profile updates, registration, certificates); the record's standing gates the portal (Precoro per-supplier checkbox; D365 per-vendor activation; D365 SE qualification gates release). Suites ship both in one product; the test is the primary object: if the system's center is the supplier population's records and standing, it is SMP; if it is the supplier's window onto trading documents, it is the portal.
- **vs Seller Portal (§05.23)** — clean: economic direction. Seller Portal = seller sells inside a marketplace operator's storefront (consumer demand, listings, operator fees, operator-mediated money). Supplier Portal = supplier serves a buyer's procurement (no consumer demand, no listings, no operator fee in the module poles, no money mediation). Same "external party portal" shape, opposite direction.
- **vs Customer Portal (§07)** — mirror image: sell-side self-service over the customer's own account relationship vs buy-side collaboration over the supplier's trading obligations.
- **vs Procurement Management Platform / Procure-to-pay / Purchase Order Management** — DISCHARGES the three passes' "external slice" flags: those Types center the buyer organization's operation, transaction chain, and PO object respectively; the Supplier Portal centers the supplier's window onto that flow. Every sampled portal sits in front of a buyer-side system that holds the record. The seam is the primary user and the direction of authorship: buyers author the documents; suppliers respond to them.
- **vs EDI Platform (§13)** — clean: EDI is the machine-to-machine transport and document-standard machinery; the portal is the human web surface over the same document flows. D365's own framing ("targeted at vendors who don't have EDI integration") shows they are alternatives covering the same exchange; many portals are effectively "web EDI" front-ends (variant posture).
- **vs Manufacturing Supplier Collaboration (§16, unprocessed)** — flagged for joint review: planning/forecast/schedule/fulfillment collaboration content overlaps the portal's variant space. This pass found no direct portal documentation of ASN/schedule exchange in the fetched sample; the boundary is held at the center-of-gravity level (collaboration content vs document-exchange surface) and should be revisited when that leaf is processed.
- **vs Government Procurement Platform (§24)** — held: the government Type centers public solicitations under public rules (publication, equal information, award publication); the supplier portal centers the ongoing trading relationship's documents. D365's public-sector RFQ publishing shows the overlap zone (published opportunities visible to non-provisioned parties), but the portal's core remains the bilateral exchange.
- **vs PRM / Dealer-Distributor Commerce Portal (§07)** — clean: sell-side partner direction (we sell through them) vs buy-side (we procure from them).
- **vs Accounts Payable Automation / invoice-only "vendor portals"** — edge variant: portals whose center is invoice upload/payment status lean toward AP tools; they lack the buyer-originated order document as the actionable center. Recorded as the thin edge, not the Type.
- **vs Employee Portal / Customer Portal / Information Portal (naming overload)** — cites the information-portal pass's seam: a *-portal name does not determine Type; the structural center does. Here the center is the transaction of record (trading documents + responses), not information access or generic self-service.
- **vs VMS (§09)** — clean: contingent-workforce staffing vendors with job-order/submission/assignment objects; vocabulary collision only.

## Historical / Market-Sample Check

The core survives the historical check. Pre-portal practice: buyers sent purchase orders by mail/fax and suppliers confirmed by return mail — a bilateral document exchange under a standing trading relationship, with no software at all. The first software generation — web-EDI webform portals of the late 1990s/2000s (supplier logs in, views the buyer's PO, flips an acknowledgment, prints, later generates ship notices and invoices) — satisfies all three L0 structures with no cloud, no AI, no scorecards, no subscription tiers. D365's own positioning ("targeted at vendors who don't have EDI integration") ties the portal to that EDI lineage as its human-surface sibling. The definition does not depend on current network/subscription packaging, and the SAP BN FAQ's "invitation to transact... from an interactive purchase order" shows the old pull-onto-the-network pattern is still the on-ramp. Older regional and platform-native shapes (ERP-embedded vendor portals, government vendor self-service) fit the same core.

## Uncertainties

- **Fulfillment notices (ASN/ship) and schedule collaboration**: widely associated with manufacturing supplier portals, but not documented in any fetched page this pass (SAP help portal, Coupa, Oracle Fusion supplier-portal chapters, and SPS Commerce were unreachable/JS-blocked/404). The final document therefore treats fulfillment/schedule collaboration as adjacent-Type territory with qualified wording, not as a portal capability.
- **SAP evidence is at product-page level (Tier 2)**: order-management mechanics (confirmation flows, ship-notice handling) are not asserted; only the features named on the page (order management, e-invoicing, status updates, profile, leads, account tiers).
- **Enterprise-suite pole rests on D365 (Tier 1) + SAP (Tier 2)**: Coupa CSP, Oracle Fusion Supplier Portal, Zycus, Epicor, Taulia not sampled (unreachable or not attempted per network rules). No precise numeric claims depend on them.
- **Gating formality varies**: per-supplier activation is an explicit switch in Precoro/D365; SAP BN gates via trading-relationship invitation. Whether every product ties portal access to supplier standing (SMP integration) is consistent in direction but varies in formality.
- **Invoice-only vendor portals** (AP-centric) were not sampled; their classification as the thin edge is inferred from the boundary logic, not from product evidence.

## Final Synthesis

A Supplier Portal is the supplier-facing operating surface of a buying organization's procurement. Its defining core is three jointly-held structures: buyer-anchored authenticated external participation (supplier organizations hold accounts under the buyer's — or its network operator's — terms, with access established and controlled from the buyer side); buyer-originated trading documents surfaced for supplier action (purchase orders foremost, plus sourcing requests, arriving as actionable items); and supplier-side responses recorded back into the buyer's process (confirmations, changes, declines, invoices, bids, profile updates — consumed by the buyer's procurement and finance systems). The portal is a surface, not the record: a buyer-side system holds the documents behind it. Money is not mediated — settlement stays in finance systems, with status visible to the supplier. Around that core, mature products add order-confirmation workflows with versioning, invoice-from-order submission with matching and status tracking, sourcing participation, master-data self-service, attachments/comments, notifications, and buyer-side control switches. The Type's center is the supplier's window onto one buyer's procurement flow — the buyer-side Types center the flow itself, the Supplier Management Platform centers the supplier population's record, the Seller Portal mirrors the shape in the marketplace direction, and EDI is the machine-transport sibling of the same exchange.
