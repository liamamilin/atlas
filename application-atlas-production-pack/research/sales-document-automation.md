# Research Notes — Sales Document Automation

## Research Goal

Understand what "Sales Document Automation" software actually is as an Application Type: what objects exist inside it, what the automation mechanism is, how documents flow from template to buyer to acceptance, what rules govern the process, and where its boundaries lie against neighboring Types (Proposal Management, CPQ, CLM, e-signature platforms, document editors, CCM).

## Initial Boundary

Temporary hypothesis before research:

- What: sales-side software that automates production of buyer-facing deal documents (proposals, quotes, contracts, order forms) from reusable templates plus deal data, and manages the send → view → sign/accept loop.
- Who: account executives / sales reps, sales ops & enablement, proposal/marketing managers, approvers (managers, deal desk), and the buyer as recipient.
- Nearest neighbors: Proposal Management (directory sibling), Configure Price Quote / CPQ, Contract Lifecycle Management, Deal Desk, Sales Order Capture, e-signature platforms, Document Editor, Customer Communication Management.
- Obvious boundary risks: (a) heavy overlap with Proposal Management — the same products market under both labels; (b) e-signature platforms with template features; (c) CRM-embedded document generators (generation-only) that lack the delivery loop.

## Research Questions

1. What document types do these products produce, and which is the center of gravity?
2. What exactly is automated: templates? variables? CRM data merge? content libraries? conditional content?
3. How is the document linked to the deal/customer context (CRM integration)?
4. What is the delivery and tracking loop: send → view → sign/accept → completed copy? What states does a document carry?
5. What pricing/quote machinery exists inside documents (catalogs, pricing tables, recipient-editable options)?
6. What governance exists before send (approvals, locked content, roles, permissions) and after send (reminders, expiry)?
7. What happens at acceptance: e-signature machinery, certificates/audit trails, payment collection, sync-back to CRM?
8. Where does this Type end and CPQ / Proposal Management / CLM / e-signature / CCM begin?

## Representative Products

Selected for market representation, different product philosophies, different customer tiers and geographies:

| Product | Philosophy / position | Tier / geography | Documentation examined |
|---|---|---|---|
| PandaDoc | All-in-one sales document automation: creation + CPQ + approval + tracking + eSign + payments | Mid-market/enterprise, US | Product site (Tier 2) + help center collections & articles (Tier 1) |
| Proposify | Proposal-first, design/brand-forward proposal & quote software | SMB/mid-market, Canada | Product site incl. detailed plan feature matrix and document-automation page (Tier 2 only — KB unreachable) |
| Qwilr | Proposals as interactive web pages ("Qwilr vs. PDF"), quotes, e-sign, payments | Mid-market, Australia | Product site (Tier 2) + help center structure (Tier 1) |
| GetAccept | Digital sales rooms + proposals/quotes + e-signature heritage | SMB→enterprise, Sweden/US (EU e-sign regime) | Product site (Tier 2) + help center incl. step-by-step send article (Tier 1) |

Attempted but abandoned: Conga (CRM-embedded document generation pole) — product page and documentation site both returned HTTP 403. The generation-first pole is therefore **not directly examined**; see Source-access Limitation.

## Sources

Tier 1 (official operational documentation):

- PandaDoc Help Center: https://support.pandadoc.com/en/ — collections "Creating documents, templates, content library items, and forms" (70 articles, incl. sub-collections Editor / Blocks / Fields / Variables / Design / Templates / Documents / Content Library Items / Forms), "Quoting & payments" (47: Catalog / Pricing Table / Quote Builder / CRM Pricing Mapping / Payments), "Sending documents" (39: Recipients / Settings / Sending / Post-Send); article "What's the difference between a template and a document?"
- GetAccept Help Center: https://help.getaccept.com/ — collections Getting Started / Deal Room (57) / Contracts (69) / Editor (20) / Pricing & Products (13) / Integrations (119) / Automation / API; article "Send Your First Contract"
- Qwilr Help Center: https://help.qwilr.com/ — collection structure: Creating & Editing Pages (Branding / Designing / Blocks & Widgets / Templates & Variables / Creating Quotes (19) / The Acceptance Process (8) / Storing & Reusing Content), Sharing & Analyzing Pages (Analytics / Securing), Integrations (CRMs / QwilrPay)

Tier 2 (official product pages):

- PandaDoc root + feature pages: https://www.pandadoc.com/
- Proposify root, document-automation page, plan feature matrix: https://www.proposify.com/ , https://www.proposify.com/document-automation
- Qwilr root: https://qwilr.com/
- GetAccept root: https://www.getaccept.com/

Unreachable: https://support.proposify.com/hc/en-us (timeout ×1, transport error ×1 — abandoned); https://conga.com/products/conga-composer and https://documentation.conga.com/ (403 ×2 — abandoned).

Research date: 2026-09-07.

## Product A — PandaDoc

### Key observations (evidence layer A = directly observed on official sources)

- Positioning: "Create, Approve, Track & eSign Docs" — a 360-degree document management flow: Create → Collaborate → Automate → Sign → Analyze → Get paid. Use-case nav: Proposals / Contracts / Quotes / Payments / Forms.
- **Template vs document**: "Templates are used for generic content that you intend on using multiple times, while documents are used for specific information. In order to send a document, you must first create it from an existing template." (help article). Documents can be converted into templates; template roles define signer placeholders.
- **Authoring model**: drag-and-drop editor with blocks (content builder blocks, tables), smart content blocks with conditional content, restricted-editing content blocks, fields (text, date, radio, file upload, inline, conditional fields, field auto-placement, field-tag recognition, text validation), variables (including custom variables), themes/design, image library; .docx/HTML/PDF import and editing.
- **Content Library**: reusable shared content items ("pre-selected content" smart blocks); sharing templates and library items across teams.
- **Quoting machinery**: Product Catalog (CSV import/export, volume-based pricing, volume discounts); Pricing Table (discounts/taxes, optional items, editable quantity, one-time vs recurring fees, product grouping into sections); Quote Builder (custom products, bundles, recipient options, margin/profit calculations, mapping quote columns to CRM fields); CRM Pricing Mapping (Pipedrive / Zoho / Zendesk Sell / SugarCRM product-field → pricing-column mapping); conditional approvals with quotes.
- **Sending loop**: Recipients (add/manage, signing order, recipient groups); Settings (ID check, auto reminders, auto expirations, auto-send completed PDF, notification emails, recipient-view localization, redirect after completion, email code verification, eSign disclosure, approval workflow lives in sending settings); Sending (send & sign, share link, bulk send, send on someone's behalf, send via SMS); Post-Send (in-person signing, recipient guide, decline, signature certificate, document/signature forwarding, recipient inbox).
- **Tracking & analytics**: document tracking ("get insights into how users interact with your document"), audit trail for every document, version history, related documents, document bundling.
- **Negotiation/collaboration**: real-time redlining, comments, approvals, workspaces; AI assistant for editing documents.
- **Payments**: payment gateways embedded in documents (Stripe data merge, recurring payments, installments, pay-by-bank), PCI guidance.
- **CRM integration**: HubSpot, Salesforce, Pipedrive, monday; API + embedded API; automation recipes ("create and send a document from a template" via API).
- Teams nav: sales, HR, marketing, CS, legal — multi-team reuse documented.

## Product B — Proposify

### Key observations (evidence layer A for plan feature matrix & product pages; operational detail not verifiable — KB unreachable)

- Positioning: "Proposal Software to Streamline Your Sales Process" — "create, track, and sign winning proposals". Use cases: Proposals / Quotes / eSignatures / Contracts.
- Document-automation page frames the pipeline explicitly with a hero graphic "stages of a proposal, including **creation, approval, sending, viewing, and signing**".
- **Variables & fields**: "Set up variables once and watch them automatically fill with the right information every time. Client names, project details, pricing, dates — all populated instantly from your CRM data." Custom fields & variables in plans; content pulled from CRM to eliminate manual errors.
- **Governance**: "lock down important proposal elements so reps can't edit them"; roles & permissions; approval workflows — "automatic approval rules based on deal size, discount levels, or custom criteria. Ensure the right eyes see proposals before they reach prospects."
- **Content library**: "Create and share templates, sections, and images that can be pulled into documents"; unlimited templates; brand customization; embedded images/videos; custom domain.
- **Quoting**: interactive quoting — "Allow prospects to alter the quantity or optional add-ons"; client input forms; e-signatures on all plans.
- **Tracking**: notifications when prospects view; "detailed analytics on the time spent on each section"; PDF export matching digital version; reports table of all documents with filtering.
- **Automation**: workflow builder; "trigger actions based on document events"; auto document expiry ("once the time's up, they'll automatically archive"); auto follow-ups/reminders when unopened or about to expire.
- **CRM integration**: Salesforce ("single source of truth" customer quote; managed package; reps work inside Salesforce), HubSpot, Zoho, Pipedrive; SSO; API; workspaces for multi-unit/franchise businesses.
- Sales/marketing/operations role framing; industries: consultants, landscaping, janitorial, construction.

## Product C — Qwilr

### Key observations (evidence layer A for help-center structure; layer A/B for features on product pages)

- Positioning: "Interactive Proposals & Analytics" — "proposal software for modern sales teams"; "Send interactive proposals, generate quotes, secure sign-off and payment"; explicit "Qwilr vs. PDF" comparison — the document medium itself is the differentiator (live web pages, not paginated files).
- Product surfaces: Editor (drag-and-drop online editor); Automation ("automate proposal generation and reduce manual CRM tasks"); Quotes ("interactive quotes tailored for every buyer"); Analytics & Notifications ("track buyer interactions and get notified when they engage"); QwilrPay (payments within proposals); E-sign & Agreements; Smart Proposal Engine ("generate personalized proposals, built with your rules, in minutes").
- Help-center structure confirms the operating model: Templates & Variables; Blocks & Widgets; Creating Quotes (19 articles); **The Acceptance Process** (8 articles — acceptance as a first-class flow); Storing & Reusing Content (saved blocks); Securing Your Pages (password protection); Page Analytics; Pipeline reports; Sharing (16 articles — live link sharing).
- Customer quote (vendor-published): "the ability to track page views on live proposals… make changes on the fly and not have to resend documents" — the live-link edit-after-send behavior of the web-page medium.
- Integrations: HubSpot, Salesforce, Zoho, Pipedrive, Dynamics, QuickBooks, Stripe; AI proposal creator (from website URL); template gallery across sales/marketing/CS/enablement.
- Use-case nav includes: document automation, contracts, digital sales rooms, mutual action plans, customer onboarding.

## Product D — GetAccept

### Key observations (evidence layer A)

- Positioning: "AI-Powered Digital Sales Rooms & Proposal Software" — "turns every signal across your deals into action… moving deals forward". Feature nav: Digital Sales Room / Proposals & Quotes / Electronic Signatures / Tracking & Analytics / Mutual Action Plans / Contract Management / Sales Content Management / Sales Engagement / CPQ / Notifications & Reminders.
- Help-center collections: Deal Room (57), Contracts (69), Editor (20), Pricing & Products (13), Integrations (119), Automation (5), API (6), Mobile App (8), AI (5), Account Settings (34).
- **Send Your First Contract** (step-by-step): 1) start from a ready-made template or upload own PDF ("flat PDF can't offer smart fields and video introductions"); 2) provide basic document info; 3) add recipients — "Assign role next to the 'Signer' placeholder or use Add recipient; enter name and email"; 4) Sending step — review email subject/message, "Prepare for sending", "Sign and send"; 5) recipient "gets an email with a secure link. They can open, review, and sign the document directly in their browser, no login required."
- Pricing & Products collection implies quote machinery inside documents; Sales Content Management ("create personalized content at scale"); e-signature with European legal depth (AdES/QES, eIDAS, GDPR framing).
- CRM integrations incl. Salesforce, HubSpot, Dynamics, Pipedrive, SuperOffice (European CRMs), Chargebee (billing); Automations ("over 500 available connectors"); API (eSign API, document generation, events & webhooks).
- AI layer: AI knowledge base to ground content; meeting-recap generation from transcripts; business-case builder; AI page editor.
- Roles: Account Executive / RevOps / Sales Leader; company-size packaging SMB / mid-market / enterprise.

## Cross-product Comparison

| Dimension | PandaDoc | Proposify | Qwilr | GetAccept | Layer |
|---|---|---|---|---|---|
| Reusable template system | Yes — templates, template roles, template gallery, doc→template conversion | Yes — unlimited templates, sections as reusable units | Yes — templates & variables, template gallery | Yes — ready-made templates; upload own file also supported | A |
| Data-driven assembly | Variables + fields; CRM product-field → pricing-column mapping; API recipes | Variables auto-filled from CRM data; custom fields | Templates & variables; Smart Proposal Engine "built with your rules"; CRM automation | Template + CRM data; AI drafting from deal context/transcripts | A |
| Document types | Proposals, quotes, contracts, forms, invoices/payments docs | Proposals, quotes, contracts/SOWs | Proposals, quotes, agreements, plus marketing/CS pages | Contracts, proposals, quotes (inside deal rooms) | A |
| Buyer-facing lifecycle w/ tracked state | Yes — send → view → sign/decline → completed PDF + certificate | Yes — send → view → sign; auto-expiry/archive | Yes — share live page → engagement tracking → acceptance process | Yes — send → view → sign in browser → completed | A |
| Engagement tracking | Yes — tracking & analytics, audit trail | Yes — open notifications, per-section time | Yes — page analytics, engagement notifications | Yes — real-time buyer insights, stakeholder tracking | A |
| E-signature | Native, signing order, groups, ID check, certificates, notary | Native, all plans | Native ("E-sign & Agreements", The Acceptance Process) | Native, AdES/QES (EU regime) | A |
| Pricing/quote machinery | Product catalog, pricing table → quote builder, conditional approvals, CRM mapping | Interactive quoting, quantity/add-on options | Creating Quotes (19-articles deep), interactive quotes | Pricing & Products collection; CPQ feature nav | A |
| Content library / approved blocks | Content Library items; restricted-editing blocks | Content library (templates/sections/images); locked elements | Saved blocks ("Storing & Reusing Content"), branding | Sales Content Management | A |
| Internal approval before send | Approval workflow (+ conditional approvals with quotes) | Approval rules by deal size/discount | "streamline approvals" (root page; less operational detail) | Contract room settings (admin control); approval depth not directly observed | A (Qwilr/GetAccept weaker) |
| Reminders / expiry | Auto reminders, auto expirations | Auto follow-ups, auto archive | Engagement notifications (expiry not directly observed) | Notifications & reminders (feature nav) | A/B mixed |
| CRM sync-back | Yes (CRM integrations, API) | Yes ("any activity… is synched with our CRM") | Yes (CRM integrations, automation) | Yes (events & webhooks, CRM integrations) | A |
| Payments inside documents | Yes — gateways embedded | Yes — Stripe integration | Yes — QwilrPay | Yes — Chargebee integration | A |
| Medium | Paginated document (also PDF import) | Paginated, design-forward | Interactive web page | Document + deal-room container | A |
| AI | Editing assistant | AI proposal generator | AI creator (from website), Smart Proposal Engine | AI knowledge base, meeting recaps, business-case builder | A (era-typical, not definitional) |

Stable across all four (evidence layer B, cross-product commonality):

1. Template → document-instance as the production mechanism.
2. Personalization from deal/customer data (variables/fields/CRM mapping).
3. Buyer-facing delivery with tracked state through to a buyer acceptance act (signature/accept), and a completed record (certificate/completed copy/archive).
4. Engagement tracking of the sent document.
5. Native e-signature/acceptance machinery.
6. Quote/pricing content as a document block with catalog linkage.
7. Reusable approved content library and brand/lock-down controls.
8. CRM integration both directions.
9. Internal review/approval somewhere before the buyer sees the document (strongest in PandaDoc/Proposify).
10. Reminders/expiry behaviors (variable depth).

Era-typical but not definitional: AI assistance, digital deal rooms, mutual action plans, embedded payments, SMS/bulk delivery, multi-team (HR/marketing) reuse.

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

1. **Reusable sales document templates** — a stored blueprint (structure, content, design, placeholder roles/fields) for a buyer-facing sales document.
2. **Data-driven assembly of a specific document instance** — the template is populated with deal/customer/product data (variables, fields, CRM mapping, conditional or AI-drafted content) to produce a personalized document for a specific buyer; documents are created *from* templates, not from a blank page.
3. **The buyer-facing document as a stateful, tracked record with a managed lifecycle** — created → (internally approved) → delivered to the buyer → tracked (viewed/engaged) → terminal buyer act (signature/acceptance or decline) → completed record retained. The document instance is the unit of record; its progression is system-visible state.

Remove (1)+(2) → generic editor or pure e-sign platform. Remove (3) → a document-generation/mail-merge utility (adjacent capability family, not the sales application). Remove the sales/deal context → CCM or general document management.

### L1 — Common Mature Structure (cross-product, not definitional)

- CRM integration: pull deal/contact/product data in; push document status/events back.
- Engagement tracking: view notifications, per-section/per-page time, recipient identification.
- E-signature machinery: recipient roles, signing order, identity checks, certificates/audit trails.
- Pricing/quote blocks: pricing tables / quote builders backed by a product catalog; discounts, taxes, recurring fees, optional items, recipient-editable quantities.
- Content library of pre-approved reusable blocks/sections; brand themes; restricted-editing/lock-down of protected content.
- Internal approval workflows (often rule-gated: deal size, discount).
- Reminders, auto-expiry/archival of offers.
- PDF export / white-labeled delivery (custom domains, branded emails).
- Team collaboration: comments, collaborator/approver seats, roles & permissions, workspaces.
- Embedded payments (variable by plan).
- Mobile apps; bulk send; send-on-behalf; SMS delivery (product-dependent).
- Template galleries with signer-role placeholders.

### L2 — Variant / Optional Structure

- Document medium: paginated documents vs interactive web pages vs deal-room containers (all three realizations coexist in the market).
- Packaging: standalone SaaS vs CRM-embedded generation (Conga-class; not directly examined) vs suite-module.
- Segment packaging: self-serve SMB → enterprise (SSO, workspaces, API, security certifications).
- Regional e-signature regimes: US E-SIGN/UETA framing vs EU eIDAS AdES/QES.
- Use-case breadth: sales-focused vs multi-team reuse (HR/marketing/CS using the same machinery).
- Adjacent extensions: digital sales rooms, mutual action plans, forms/intake, notary, CPQ modules.
- AI posture: editing assistant vs generator (from prompts/website) vs knowledge-base-grounded drafting from conversations.

### L3 — Vendor-specific (research notes only)

- PandaDoc: Quote Builder replacing Pricing Tables, product catalog CSV/volume pricing, Stripe data merge, notary, document bundling, related documents, Inbox, Admin Hub, 2FA.
- Proposify: workspaces for franchises, Aspire integration, professional design services, collaborator-seat tiers, custom-domain mapping.
- Qwilr: QwilrPay, Springboard, pipeline velocity reports, page password protection, website-to-template AI creator, live-link edit-after-send behavior.
- GetAccept: digital sales rooms, AI knowledge base, meeting-recap/business-case AI agents, mutual action plans, SuperOffice integration, AdES/QES depth.

## Vendor-specific / Rejected Findings

- Rejected as definitional: embedded payments (present in all four but plan-gated and not what makes the Type), AI anything, deal rooms, notary, SMS delivery.
- Rejected: "43% of proposals won within 24 hours of opening" and similar vendor marketing statistics (Proposify homepage) — marketing claims, not operational structure.
- Rejected: precise numeric limits (document counts, seat tiers, expiry windows) — plan-dependent and not researched across the sample.
- PandaDoc's "CPQ" self-labeling is a product-feature framing; it does not make CPQ's configuration-rules engine part of this Type's core (center-of-gravity test).

## Boundary Findings

1. **vs Proposal Management (adjacent leaf)** — the heaviest seam. All sampled products self-market as "proposal software" (PandaDoc, Proposify, Qwilr; GetAccept "proposal software" in its title). The distinguishing structure of this leaf: (a) document-type breadth — quotes, contracts, order forms, proposals as instances of one template→instance machinery; (b) automation mechanism as center of gravity (template + data merge + delivery lifecycle). Proposal Management presumably centers the proposal-specific workflow. Because the products are the same, this leaf pair needs joint review; the boundary recorded here is center-of-gravity, not product populations.
2. **vs CPQ** — CPQ centers on product configuration rules and pricing logic; its output can be a quote document. This Type centers on document production/delivery; quote content appears as catalog-backed document blocks. PandaDoc ships a "CPQ" feature — evidence that vendors blur the seam, not that the Types are identical.
3. **vs Contract Lifecycle Management** — CLM manages contracts after signature (clause libraries, negotiation across parties, obligations, renewals). This Type's contract handling ends at completion/certificate/archive. PandaDoc has a small CLM collection (8 articles) — light-touch overlap.
4. **vs e-signature platforms** — pure e-sign products sign arbitrary uploaded documents without sales-document assembly (template+deal data, pricing content, CRM linkage). E-sign machinery is embedded here as the acceptance mechanism. Template-based e-sign platforms approach this Type from the other side; the sales-assembly layer is the discriminator.
5. **vs Document Editor / word processor** — general-purpose authoring from blank pages, no buyer-facing lifecycle, no deal-data merge, no tracked delivery.
6. **vs Customer Communication Management** — CCM produces high-volume operational/compliance communications (statements, bills) from enterprise systems of record; different users, volume profile, and document semantics.
7. **vs Sales Order Capture / Contract-to-order** — after acceptance, converting the signed quote/contract into an order is the downstream neighbor's job; some products hand off to CRM for this.
8. **Generation-only pole** — mail-merge / CRM-embedded document generators produce documents but do not manage the buyer-facing tracked lifecycle; treated here as an adjacent capability family (and a boundary of this L0), not as the same Type. Not directly examined (Conga unreachable) — flagged in Uncertainties.

### Historical / market-sample check

- Would older products fit? Pre-web proposal practice (print/PDF + email) is the pre-digital baseline, not a software Type. Early-2010s web proposal tools already had template→send→track→e-sign — the L0 above matches them. A pure offline quote generator (Word mail merge + CRM) lacks the tracked buyer-facing lifecycle and is better classified as document generation — the L0 holds by excluding it.
- Multi-era media check: paginated documents (dominant), web-page documents (Qwilr), and room containers (GetAccept) all satisfy L0; the L0 does not assume any specific medium.
- Regional check: US products (E-SIGN/UETA framing) and EU products (eIDAS AdES/QES) satisfy the same core; signature legal regime is a variant.
- Team-reuse check: HR/marketing/CS reuse of the same machinery (PandaDoc team nav; Qwilr roles) still satisfies the core with the deal context replaced by another agreement context — recorded as a variant, with sales/deal documents remaining the canonical center (directory placement).

## Uncertainties

1. Conga (and the CRM-embedded generation pole generally) could not be examined (403 ×2). The claim that generation-only tools sit outside this Type rests on structural reasoning + market framing, not direct examination of that pole's current products.
2. Proposify's operational documentation was unreachable; its observations are Tier-2 (product pages + plan matrix). Proposify-specific behavior details (exact expiry mechanics, workflow-builder events) are deliberately not asserted.
3. Qwilr's and GetAccept's approval workflow depth is weakly evidenced (root-page claim / admin settings only) — approval machinery is written as common with moderate confidence, not as uniformly deep.
4. The exact relationship between this leaf and the Proposal Management leaf needs a joint review pass; this research records the seam but does not resolve whether the directory should eventually merge or re-scope either leaf.
5. Sync-back depth (what exactly is written back to CRM on completion) varies by product and was observed only at the level of existence, not mechanics.

## Final Synthesis

Sales Document Automation is the sales team's document-production-and-delivery application. Its world has one central production mechanism — reusable templates assembled with deal data into specific buyer-facing document instances — and one central lifecycle — internal approval, delivery, tracked buyer engagement, and a terminal acceptance act (signature/accept) that completes the record. Everything else the market expects (CRM sync, engagement analytics, quote machinery, content governance, reminders, payments, AI drafting) accumulates around that spine as standard or optional capability. The Type ends where configuration rules (CPQ), post-signature obligation management (CLM), order creation (Sales Order Capture), and high-volume operational communications (CCM) begin.
