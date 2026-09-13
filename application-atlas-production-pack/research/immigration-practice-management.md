# Research Notes — Immigration Practice Management

Research date: 2026-09-07
Slug: immigration-practice-management
Directory leaf: Immigration Practice Management (§11 Legal, Risk, Compliance & Governance)

---

## Research Goal

Understand what Immigration Practice Management software actually is as an Application Type: its core objects, the work loop of an immigration practice, how government-facing mechanics (forms, filings, status) are modeled, who operates it, and where its boundaries sit against general law practice management, government-side immigration case management, and corporate global-mobility platforms.

## Initial Boundary (hypothesis before research)

- Hypothesis: practitioner-side software for immigration law firms/representatives — client (foreign national) records, immigration cases bound to case types, government form preparation, questionnaires, document collection, deadlines, status tracking, billing.
- Neighbors: Law Practice Management System (generic matters), Legal Matter Management, Immigration Case Management (§24 — government side), Legal Document Automation, Legal Docket Management, Legal Intake & Client Onboarding, corporate global-mobility platforms.
- Key risk identified up front: the market label "immigration case management" is used by practitioner-side vendors, while the directory also holds an "Immigration Case Management" leaf under §24 (Government). Naming collision must be handled explicitly.

## Research Questions

1. What is the central object — client, case, or matter — and how do they relate?
2. What is a "case type" and how does it drive the workflow (statuses, tasks, forms)?
3. How does government form preparation work (form library, questionnaire auto-population, packet assembly, e-filing)?
4. How are immigration-critical dates managed (priority dates, expirations, receipt numbers, status durations)?
5. How does the client/employee participate (portal, invitations, messaging, document upload)?
6. How is government status ingested and shared (receipt/notice processing, status updates)?
7. What roles exist (attorney/preparer/paralegal; corporate HR/mobility; regional scoping)?
8. How does billing work and is it definitional?
9. What regional variants exist (US-centric vs Canada/global vs EU mobility)?
10. Where is the boundary vs general law practice management and vs government-side immigration case management?

## Representative Products

| Product | Pole | Tier | Access |
|---|---|---|---|
| 8am DocketWise (Docketwise) | firm-side, SMB, modern cloud, form-first | Tier-1 (product page + help center ×5) | fetched |
| Mitratech INSZoom | firm + corporate enterprise, global (US/Canada/global), configurable | Tier-1 (product page + solution page) | fetched |
| Envoy Global | corporate immigration services-led platform (legal services + tech) | Tier-1 (product + technology pages) | fetched |
| Localyze | EU corporate global-mobility platform (services + software) | Tier-2 (product page) | fetched |

Selection rationale: two pure software poles (modern SMB firm-side vs enterprise configurable firm+corporate), one services-led corporate platform, one EU mobility boundary anchor. Different customer tiers (solo/SMB firm → Fortune 500 enterprise → corporate HR) and different product philosophies (form-automation-first vs workflow-configurability-first vs services-bundled).

Rejected/unreachable:
- LawLogix EDGE — lawlogix.com 403, hyland.com 403 (2 attempts) → abandoned per network rule; limitation recorded. Known market context only (mid-market firm+corporate, I-9 compliance heritage); no claims made.
- Imagility — imagility.co transport error, imagility.com empty output (2 attempts) → abandoned; no claims.
- CaseAid (caseaid.co.uk) — fetched but is UK trade-union employment case management, NOT immigration → product mismatch, excluded.
- General LPM (Clio, MyCase) — not sampled; used only as structural boundary context via Mitratech's own FAQ statement.

## Sources

- Docketwise product page: https://www.docketwise.com/ (fetched 2026-09-07)
- Docketwise Help Center: https://supportcenter.docketwise.com/ (index; collections: Smart Forms 32, Invoicing and Trust Accounting 27, Client Portal 6, Firm Settings 23, Integrations 15, Contacts and Matters 14, Reports 10, Case Tracking 3, Client Communication 10, Files and Documents 5, Docketwise IQ 3, etc.)
- Docketwise — Contacts and Matters collection: https://supportcenter.docketwise.com/en/collections/9474944-contacts-and-matters
- Docketwise — Smart Forms V3 (Packet Assembly, Custom Questions, Templated Intakes): https://supportcenter.docketwise.com/en/articles/9371989
- Docketwise — Workflows with Matter Types and Statuses: https://supportcenter.docketwise.com/en/articles/9372198
- Docketwise — Case Tracking collection (Priority Date Tracking / USCIS Receipt Number Tracking / Tasks and Task Lists): https://supportcenter.docketwise.com/en/collections/9474948-case-tracking
- Docketwise — E-Filing Forms with USCIS: https://supportcenter.docketwise.com/en/articles/9371979
- Mitratech INSZoom product page: https://www.inszoom.com/ (fetched 2026-09-07)
- Mitratech Immigration Case Management solution page (INSZoom): https://mitratech.com/solutions/legal-operations/immigration-case-management/
- Envoy Global home: https://www.envoyglobal.com/ ; Technology: https://www.envoyglobal.com/why-envoy-global/technology/
- Localyze home: https://www.localyze.com/

## Product Observations

### Docketwise (8am DocketWise) — evidence layer A unless noted

Positioning: "immigration legal case management software… one connected platform for intake, forms, case management, billing, and payments." Audience: small immigration law firms and growing practices. Part of the 8am group (MyCase/LawPay/CasePeer family).

Core objects (help center structure):
- **Contact** — person record; searchable by name, email, phone, **A# (alien registration number)**, unique identifier; related contacts (relations between contacts); custom attributes; merge duplicates; archive; export CSV. (A# search is an immigration-specific identifier surface.)
- **Matter** — created with type + status; Open/Pending/Closed status; archive; link multiple related contacts to one matter; firm/contact/matter activity feeds.
- **Matter Types + Matter Statuses = workflows** — user-configurable per firm: status sequences with optional **duration** per status; automations triggered on entering a status (add task list, send message from template, CC applicant, auto-advance when tasks complete); progress bar green (on time) / red (late) by duration; dashboard/report filters by type/status/late.
- **Smart Forms** — the flagship. A smart form = electronic questionnaire + associated government forms. Tabs: **Assemble** (assign contact/matter/preparer; add forms individually, from smart form collections, or templates; assign form roles Beneficiary/Petitioner; add files; order; table of contents), **Invite** (invite contacts to collaborate via email/text/client portal/shareable link; pre-translated intake; invitation statuses Sent/Accepted/Returner for Review; resend/revoke), **Intake** (questionnaire; hide/flag/comment on questions; @mentions; translate — 11–12 languages incl. Spanish, Portuguese, French, Hindi, Russian, Chinese, Korean, Turkish, Haitian Creole, Arabic, Vietnamese; custom tabs/questions incl. document requests and expiry-date question types; save answers to custom attributes; save intake as template), **Review** (database values vs PDF values views; download single form or whole packet).
- **Case tracking** — Priority Date Tracking; USCIS Receipt Number Tracking; Tasks and Task Lists.
- **E-filing with USCIS** — plan-gated (Pro/Advanced). Available: I-130+G-28, N-400+G-28, I-765+G-28, I-129+G-28(+I-907), H-1B Electronic Registration+G-28; expanding library; also DS-260/DS-160 (DOS) and DOL FLAG e-filing articles. Mechanics: product validates questionnaire → syncs data into the attorney's my.uscis.gov draft using the attorney's USCIS account credentials (email, password, OTP secret from authenticator app) → user completes review/document upload/signing on my.uscis.gov → confirm in Docketwise → G-28 added the same way. Draft cannot be updated after submission. Toggle electronic/paper (N-400+G-28 only). Only attorney/legal-representative USCIS accounts supported.
- **Client portal** — invitations, document sharing, tasks shared to portal.
- **Invoicing and Trust Accounting** — 27 help articles; LawPay integration (IOLTA-compliant payments).
- **CRM/Leads** — capture leads from website, Facebook Messenger, WhatsApp, SMS; follow-up automation.
- **Reporting** — custom reports on case status, revenue, deadlines, tasks, unpaid invoices, lead sources.
- **AI (8am IQ)** — Document Assistant captures client/case data from documents into forms; Writing Assistant edits/refines/translates communications.
- **Integrations** — LawPay, QuickBooks, Google Calendar, Gmail, Outlook, Zapier; Open API.
- Marketing claims (B): "75% less time on admin"; customer quotes. Kept as claims, not facts.

### Mitratech INSZoom — evidence layer A unless noted

Positioning: "Global Immigration Case Manager… U.S., Canadian, and Global Immigration Case Management and Compliance… cloud-based." Audience: "law firms and immigration professionals across the U.S., Canada, and globally"; "solo practitioners to enterprises in the Fortune 500"; 1,500+ immigration practices (vendor claim). Sold under both labels "Immigration Case Management" (product) and "Immigration Practice Management" (law-firm-operations solution category).

Capabilities (product + solution pages):
- **Configurable workflows and reminders**; **automatic expiration & deadline alerts** ("real-time notifications that protect your clients").
- **Digital questionnaire and forms library** — named in vendor FAQ as a key differentiator; forms list includes I-90, N-400, I-765, I-485, N-565, I-131, I-751, I-821D, I-539, N-600, I-130, I-824, I-129F — "employment-based petitions and family-based sponsorships to travel documents and citizenship matters"; library "constantly evolving"; per-country form lists on request (US, Canada, global).
- **E-filing** of USCIS and DOL forms; "largest library of e-fillable forms" (vendor claim); some forms (I-129/H-1B, DS-160, N-600) are web-based government forms completed on the government site.
- **Automation of data entry from USCIS receipts**; **GovNoticeIDP** — AI intelligent document processor that extracts/categorizes data from scanned USCIS receipt/approval batches and updates case records with a review interface.
- **H-1B Registration Module**; **case phases and milestones for SLA reporting**; **custom & ad-hoc reporting**; **digital file assembly**; **data & document migration**; **invoice generation**.
- **Editions**: Professional vs Enterprise — Enterprise adds HR Portal access for multiple corporate contacts, automated templated emails/reminders, "Advance Case Request" (streamlined case initiation).
- **Integrations**: QuickBooks Online, LawPay, Authorize.net, DocuSign; robust API/developer tools; "integrates with leading solutions for government interactions, HR management, candidate sourcing, payroll".
- **Security posture**: encryption, SSO, MFA, SOC 2 Type 2 (vendor claim).
- Vendor FAQ defines the category and its boundary (A, vendor-stated): "Immigration case management software is a cloud-based legal technology solution that helps immigration attorneys and law firms manage every aspect of the immigration process. It streamlines client intake, case tracking, compliance management, and form preparation…" and "How is immigration case management software different from general legal case management software? Unlike generic legal software, immigration case management platforms are tailored to the needs of immigration law practices. They offer USCIS form libraries, visa-specific workflows, I-94 tracking, and immigration-specific compliance features not found in traditional case management tools."
- Audience span (A): "law firms, corporations and non-profit organizations of all sizes."

### Envoy Global — evidence layer A unless noted

Positioning: "leading corporate immigration services provider" — legal services (via affiliated U.S. law firm) + in-house AI-powered platform; work authorizations, business travel, consular services, program management; 180+ countries (vendor claim). Platform is free with the services (services-led business model).

Platform capabilities (technology page):
- **Case model**: cases with **milestones** and status; "thousands of customized workflows for varying case types in countries around the globe… indicate what is generally required from the outset of a case, allowing mobility teams to continuously track and manage casework… both pre- and post-filing."
- **Smart questionnaires**; auto-import of data from prior cases/user profiles; **AI Quality Sensors** screen forms for potential errors and alert legal teams; built-in data validation "catches errors before they hit a form"; **automated e-filing with USCIS**; automated data capture from trusted sources kept up to date.
- **Employee self-service** (portal + mobile app): communication with legal team, case status tracking (e.g., "when LCA is filed"), document upload into a secure repository.
- **Communications Center** — centralized immigration correspondence; **Case Milestones** set expectations; policy changes trigger direct reports to affected employees.
- **Dashboards & reporting**: work-authorization expiration dates, spend by division/cost center, workforce planning, historical case outcomes incl. **RFE and approval rates**; filter/export/share.
- **Auto-prioritization** of cases by expiration dates, start dates, VIPs.
- **Screening & hiring**: pre-hire candidate eligibility assessment; open cases for accepted offers (ATS integration).
- **Roles**: mobility professionals, employees, regional roles restricting access geographically.
- **Integrations**: HRIS/HCM and ATS (Workday, SAP, Greenhouse), SSO via Okta.
- **Global Deployment Dashboard** — whole workforce across the assignment process.

### Localyze — evidence layer A (product page), boundary anchor

Positioning: "the platform for employee cross-border moves" — relocations, business trips, work abroad, workations, destination services; immigration & visa services delivered with immigration experts. Audience: corporate HR ("People Teams"), employees. EU-based (Germany), UK entity OISC-registered (F202100378), ISO 27001, GDPR.
- "Self-serve or managed relocation and immigration case management" — case management exists as a platform capability but is bundled with destination/settling-in services, workation/business-trip compliance, and a services marketplace.
- 2-way HRIS integration; relocation budget/cost tracking and reporting.
- Interpretation: the immigration case-management core is present, but the product's center of gravity is broader global mobility program management — used here as the boundary anchor for the corporate-mobility pole, not as a core sample.

## Cross-product Comparison

| Structure | Docketwise | INSZoom | Envoy Global | Localyze | Strength |
|---|---|---|---|---|---|
| Client/foreign-national person record (with immigration identifiers) | Contact (A# search, relations, custom attributes, merge) | foreign nationals/clients central repository | sponsored employees (HRIS-fed) | employees/talents | A×4 — core |
| Case/matter as the unit of work | Matter (type+status, open/pending/closed) | Case (phases/milestones, SLA) | Case (milestones, status, pre/post-filing) | case (self-serve or managed) | A×4 — core |
| Case bound to an immigration process type that shapes the work | Matter Types + status sequences (user-configurable) | configurable workflows; forms per process | thousands of country/case-type workflows (pre-built) | country/process workflows | A×4 — core |
| Questionnaire → form population | Smart Form intake (invite/translate/custom questions) | digital questionnaire + forms library | smart questionnaires + auto-import | employee self-serve flows | A×4 — core |
| Official form/filing production from case data | Smart Forms, packet assembly, e-file USCIS/DOL/DOS | forms library, e-filing USCIS/DOL | data validation before filing; automated e-filing | services-led (experts + platform) | A×3 strong + A×1 services-led — core |
| Deadline/date machinery | expiry reminders, priority dates, status durations | expiration & deadline alerts | expiration tracking, auto-prioritization | compliance tracking | A×4 — common |
| Government status ingestion | USCIS receipt tracking; auto-share USCIS updates | USCIS receipt data entry automation; GovNoticeIDP AI | automated data capture; case status visibility | — | A×3 — common |
| Client/employee participation surface | client portal, invitations, tasks to portal | client portal; Enterprise HR portal | employee portal + mobile app | employee app | A×4 — common |
| Workflow automation | status-triggered tasks/messages/auto-advance | configurable workflows/reminders; templated emails | automated collaborative workflows | — | A×4 — common |
| Billing/invoicing | invoicing + trust accounting + LawPay | invoice generation; QuickBooks/LawPay | (services-led; spend reporting only) | budget/cost reporting | A×2 full + A×2 partial — common, NOT definitional |
| Reporting/dashboards | custom reports | custom & ad-hoc | dashboards incl. RFE/approval rates | budget reports | A×4 — common |
| Roles & permissions | firm staff, preparer | attorney/HR; Enterprise HR portal | mobility/employee/regional roles | HR teams | A×4 — common |
| Integrations | payments/accounting/calendar/email/Zapier/API | accounting/payments/e-sign/API; HR/payroll | HRIS/ATS/SSO | HRIS 2-way | A×4 — common |
| E-filing support | yes (USCIS/DOL/DOS; plan-gated) | yes (USCIS/DOL) | yes (automated e-filing USCIS) | not evidenced | A×3 — common |
| AI assistance | 8am IQ (doc→form capture, writing) | GovNoticeIDP (notice extraction), virtual assistant | validation, data capture, quality sensors | (era positioning) | A×3 — era-common |
| CRM/lead management | Leads CRM (web/Messenger/WhatsApp/SMS) | — (not observed) | pre-hire screening via ATS | — | A×1 — optional |
| Compliance adjacency (I-9/E-Verify) | — | Mitratech sibling product (Tracker I-9) | — | — | structural — optional/adjacent |
| Destination/travel services | — | — | business travel/consular services | destination services, workations | A×2 — services-led pole only |

## Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

1. **Client (foreign national) record** — an identified person whose immigration status/permission is the subject of the work; carries immigration-relevant identity (in US practice commonly the A-number; conceptually: the person's immigration identity data).
2. **Immigration case bound to a case type** — the case is an instance of a defined immigration process (a visa/petition/application/benefit category); the type shapes what the case requires (statuses, forms, documents). Configurable-by-firm vs pre-built-by-vendor is a variant; the concept is invariant.
3. **Filing preparation from case data** — questionnaires collect case data; official immigration forms and supporting-document packets are produced from that data; the case is worked toward a government filing. (This is the immigration-specific work product; generic matter management has no such fixed output shape.)
4. **Persistent case record with tracked progression** — the case's state, history, and progression live in the system across a process that runs months-to-years; the record outlives any single session and accumulates the filing trail.

Historical check: pre-cloud/desktop-era immigration form-and-case software, Canadian/UK/Australian practitioner tools, and non-lawyer representative practices all satisfy these four without USCIS specifics, portals, e-filing, or billing. US-specific identifiers (A#, priority dates, receipt numbers) are regional realizations, not invariants.

### L1 — Common Mature Structure

- Client-facing questionnaires with invitations (email/SMS/portal/link), multilingual intake, question-level collaboration (hide/flag/comment)
- Client/employee portal (self-service status, documents, tasks, messaging)
- Document collection & checklists; secure document repository; packet assembly (forms + supporting documents + table of contents)
- Deadline/date machinery: expiration reminders, priority-date tracking, receipt-number tracking, per-status durations with late indicators
- Government status ingestion: receipt/notice data capture (increasingly AI-extracted), status updates shared to clients
- Workflow automation: status-triggered task lists, message templates, auto-advance
- E-filing / electronic submission support on government platforms (plan- or edition-gated)
- Billing/invoicing (flat-fee oriented; trust accounting in the US firm pole) — common but not definitional (services-led pole lacks it)
- Reporting/dashboards (case status, deadlines, revenue/spend, cycle outcomes)
- Roles & permissions (attorney/preparer/paralegal; corporate: mobility/HR roles, regional scoping)
- Integrations: payments, accounting, e-signature, calendar/email; corporate pole: HRIS/ATS/SSO
- Templates: form collections, intake templates, message/letter templates
- AI assistance (era-common): document→form data capture, notice extraction, writing assistance, form-error screening

### L2 — Variant / Optional Structure

- Operator pole: law-firm/practitioner-side vs corporate (employer HR/global-mobility) side vs services-led hybrid (platform bundled with legal services — Envoy; platform + managed mobility services — Localyze)
- Regional scope: US-centric (USCIS/DOL/DOS forms, A#, priority dates, receipt tracking) vs multi-country (INSZoom US/Canada/global; Envoy 180+ countries claim) vs EU mobility framing (Localyze)
- Practice mix: family-based/humanitarian vs employment-based/corporate mobility caseload
- Edition/plan gating: e-filing on higher plans (Docketwise Pro/Advanced); Professional vs Enterprise (INSZoom); free-platform-with-services (Envoy)
- CRM/lead management for client acquisition (firm pole)
- Compliance adjacency: I-9/E-Verify employment-verification modules (LawLogix heritage; Mitratech Tracker sibling)
- Corporate program depth: HR portals for corporate contacts, advance case request, SLA reporting, workforce/deployment dashboards, spend analytics
- Identity/regulatory posture of the operator: attorneys vs accredited representatives/consultants (OISC registration visible at Localyze UK; product supports "preparer" role distinct from attorney)
- Mobile apps; desktop app (Docketwise)
- AI depth (from extraction to quality sensors to writing)

### L3 — Vendor-specific (research notes only)

- Docketwise: Smart Forms V3 tab model (Assemble/Invite/Intake/Review); 11–12 intake languages list; A#-based contact search; USCIS OTP-secret sync mechanics (attorney credentials + authenticator app); "DocketWise cannot update an e-filing draft after submission"; electronic/paper toggle (N-400+G-28 only); 8am IQ Document/Writing Assistant; Leads CRM channel list; IOLTA-compliant LawPay; "75% less admin" claim.
- INSZoom: H-1B Registration Module; Advance Case Request; GovNoticeIDP; Professional vs Enterprise split; named forms list (I-90…I-129F); "largest library of e-fillable forms" and "1,500+ practices" claims; SOC 2 Type 2 claim; account setup 2–5 business days claim.
- Envoy Global: Global Deployment Dashboard; Communications Center; Case Milestones; AI Quality Sensors; RFE/approval-rate analytics; auto-prioritization (expiration/start date/VIP); free platform + free implementation; Okta SSO; "50% reduction in admin time" claim; U.S. legal services via affiliated law firm (Corporate Immigration Partners).
- Localyze: destination/settling-in services marketplace; workations/business-trip compliance; OISC registration number; ISO 27001; YC S2019; 10,000+ relocations claim.

## Vendor-specific Findings

See L3. None promoted to the canonical document except as named-product examples where useful.

## Boundary Findings

1. **vs Law Practice Management System (§11 sibling)** — sharpest seam. General LPM manages matters generically (any practice area) with generic document/calendar/billing machinery; it has no immigration form library, no case-type-driven immigration workflows, no questionnaire→form population, no government status ingestion. Mitratech's own FAQ states the difference (USCIS form libraries, visa-specific workflows, I-94 tracking, immigration-specific compliance "not found in traditional case management tools"). Test: remove the immigration-specific case model + form machinery → general LPM. Many firms reportedly run both side by side (Docketwise markets integrations with general tools rather than replacing them).
2. **vs Immigration Case Management (§24, Government)** — same market words, different operator and different object state. §24 leaf sits under Government/Public Sector: the government agency is the operator, cases are adjudicated/decided by the state. Practitioner-side products prepare and track filings on behalf of a client; the case's "outcome" is the government's decision, recorded and communicated, not adjudicated. The naming collision is real: Mitratech brands INSZoom "Immigration Case Management" while the directory's §24 leaf uses the same name for the government-side Type. Flag for joint review / disambiguation note.
3. **vs Legal Matter Management** — generic matter container vs domain-instantiated case; immigration PM is the domain instantiation with fixed output shape (the filing). Consistent with how other domain instantiations (e.g., creator CRM vs CRM) were treated.
4. **vs Legal Document Automation** — form/document automation is one capability inside immigration PM; document-automation products are general-purpose assembly engines without the immigration case model.
5. **vs Legal Docket Management** — deadline/docket machinery is one layer; docket management is court-calendar-centered, not case-preparation-centered.
6. **vs Legal Intake & Client Onboarding** — intake is the front end of the loop; immigration PM carries the case through preparation, filing, tracking, and resolution.
7. **vs corporate global-mobility platforms (Envoy, Localyze)** — these bundle immigration case management with destination services, business travel, workations, program management, and deliver it as a service. The immigration case-management core is shared; the mobility platform's scope is wider and services-led. Test: remove destination/travel/program services and the practitioner operates the filings → immigration practice management; keep them → global mobility platform (a different, services-led Type; no dedicated directory leaf — noted, not silently created).
8. **vs I-9 / E-Verify employment verification (HR side)** — adjacent compliance domain over the employment-eligibility lifecycle; some vendors span both (LawLogix heritage; Mitratech sells both). Different object (the employment verification record) and different operator moment (hiring/onboarding vs status maintenance).

## Uncertainties

- LawLogix EDGE unreachable (403 ×2) — the third historical US leader could not be directly verified; its known positioning (firm+corporate, I-9 compliance heritage) is market context only, no claims made.
- Imagility unreachable — newer AI-era entrant unverified.
- UK/regional standalone practitioner tools (e.g., for OISC advisers) not directly sampled; the regional check rests on INSZoom's Canadian/global support, Localyze's UK OISC registration, and structural reasoning. Assertion strength for non-US regional mechanics kept low.
- Billing depth at the corporate pole (Envoy/Localyze) not directly observed — treated as services-led absence, not as a claim that corporate tools never bill.
- Exact e-filing form coverage changes frequently (both vendors say libraries are expanding) — no stable counts asserted in the final document.
- Government-side §24 leaf unprocessed — boundary stated structurally; joint review recommended.

## Final Synthesis

Immigration Practice Management is the practitioner-side system of record for an immigration practice's caseload. Its world is built from four load-bearing structures: the client (foreign national) record; the immigration case bound to a case type that encodes a government process; filing preparation that turns case data — collected through questionnaires — into official forms and supporting-document packets; and a persistent case record whose progression is tracked across a months-to-years process, including against government-issued status (receipts, notices, decisions). Around this core, mature products add the operational loop of a practice: client participation surfaces (portals, multilingual intakes), deadline machinery (expirations, priority dates, status durations), workflow automation, e-filing support, billing, reporting, roles, and integrations. The Type splits into three market poles — firm-side software (Docketwise), enterprise configurable platforms serving firms and corporate immigration programs (INSZoom), and services-led corporate platforms where the software is bundled with legal services (Envoy, Localyze) — all sharing the same core. The defining difference from general law practice management is the immigration-specific case model and its form/filing machinery; the defining difference from government-side immigration case management is who operates the system and what happens to the case (preparation and tracking on behalf of a client vs adjudication by the state).
