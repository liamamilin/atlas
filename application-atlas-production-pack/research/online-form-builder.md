# Research Notes — Online Form Builder

Date: 2026-09-08
Slug: `online-form-builder`
Directory leaf: Online Form Builder (§03.11 Forms & Data Collection)

## Research Goal

Understand what an Online Form Builder actually is as an Application Type: what the "form" is as an object, how it is built and by whom, how it reaches respondents, what happens to a completed submission, how the form owner works with collected data, and where the boundary sits — above all against the §03.11 siblings (Survey Platform, Polling Application, Questionnaire Application) and the many processed neighbors that define themselves partly against this leaf (lead capture, event registration, approval workflow, digital waiver, EDC, employee survey, admissions).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: software for assembling web forms interactively (no code), publishing them as fillable pages, and collecting each completed submission as a structured record the owner can view, manage, export, and route.
- Likely confusions:
  - Survey Platform (§03.11 sibling, unprocessed) — same instrument machinery; suspected seam is measurement/analysis as the center
  - Polling Application (§03.11 sibling, unprocessed) — single-question / live aggregate vs persisted per-submission records
  - Questionnaire Application (§03.11 sibling, unprocessed) — possibly near-alias
  - Lead Capture Platform (processed) — form machinery subordinated to revenue-intent semantics
  - Event Registration Platform (processed) — form machinery subordinated to an event offer + roster
  - Approval Workflow Platform (processed) — "ends at collecting structured data"
  - Electronic Data Capture (processed) — protocol/participant/visit structure + regulated record
  - Digital Waiver Management (processed) — release instrument + signer binding
  - Structured Table / Lightweight Database Application (§03.03) — table/data-model center vs respondent-intake center
- Unknowns: whether respondent identity (accounts, verified email) is definitional or variant; whether payments are definitional; how strong the workflow/approval extension is across the category; whether "builder" is a defining leg or merely universal.

## Research Questions

1. What is a form inside these products — a document? a field list? a configuration object?
2. How is the form built (drag-and-drop, templates, AI)? Who builds it — developer or non-specialist?
3. What field types, validation, and logic exist? Are they definitional or common?
4. How is the form published and distributed (link, embed, QR, email)?
5. Who fills the form — do respondents need accounts? What identity options exist?
6. What exactly is a submission/entry/response? What metadata and status does it carry?
7. How does the owner work with collected data (table views, edit, export, notifications, integrations)?
8. Which capabilities are market-standard but not defining (payments, files, logic, workflows, AI)?
9. What do vendor product families reveal about boundaries (Microsoft's own upsell line, Formstack's suite packaging)?
10. Where does this Type end and Survey Platform / Polling / database-app territory begin?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| Jotform | standalone pure-play leader, individual→SMB→enterprise | deepest public user guide; the category's center of gravity |
| Microsoft Forms | platform-native (Microsoft 365), education + org tier | different philosophy (simplicity, suite-native output); free tier; quiz variant |
| Formstack | business-process suite pole (Forms + Documents + Sign) | forms as data-capture layer of a no-code automation suite; enterprise security posture |
| Cognito Forms | mid-market pure-play, calculation/payment strength | rich user-guide evidence on entries/lifecycle; different packaging |

Rejected/abandoned samples:
- Google Forms — canonical free/platform-native pole, but all Google properties unreachable this pass (support.google.com timeout ×2, google.com/forms/about timeout ×1). Recorded as a sampling limitation; used only as positional market context (Jotform ships dedicated "Google Forms Alternative" comparison pages, corroborating its category centrality), never for operational claims.
- Wufoo (historical check candidate) — docs not fetched this pass; historical check reasoned structurally instead (early form services stored submissions and emailed them to the owner — that shape satisfies the core without any modern capability).
- Typeform — already covered contextually by the lead-capture pass; conversational pole noted but not re-sampled.

## Sources

Tier 1 (official operational documentation):
- Jotform User Guide hub — https://www.jotform.com/help/
  - "How to Create Your First Web Form" — https://www.jotform.com/help/2-how-to-create-your-first-web-form/
  - "How to View Form Submissions" (Jotform Tables) — https://www.jotform.com/help/269-how-to-view-form-submissions/
  - Chapter titles read from hub: Create Forms; Share Forms; Payment Forms; Reports; Jotform Tables; Custom Domains; Accessible Forms; HIPAA Compliance Forms; Integrations; Widgets; Conditional Logic guide title ("What is Conditional Logic?...")
- Microsoft Forms help & learning — https://support.microsoft.com/en-us/forms
  - "Create a form with Microsoft Forms" — https://support.microsoft.com/en-us/forms/create-a-form-with-microsoft-forms
  - "Adjust your form or quiz settings in Microsoft Forms" — https://support.microsoft.com/en-us/forms/adjust-your-form-or-quiz-settings-in-microsoft-forms
- Formstack Help Center — https://help.formstack.com/
  - Forms category — https://help.formstack.com/hc/en-us/categories/43680297224723-Forms
  - Getting Started with Forms section (Form Types; Manage Forms and Permissions; Forms Account Overview)
  - Trending articles read as titles: Export Submission Data; Data Encryption; Password Protecting Your Form; Using SSO to Password Protect a Form; WCAG 2.1 AA audit article
- Cognito Forms Support — https://www.cognitoforms.com/support
  - "Entries" guide — https://www.cognitoforms.com/support/6/entries
  - "Working with entries" — https://www.cognitoforms.com/support/81/entries/working-with-entries
  - Guide-section titles: Building Forms; Style & Publish; Managing Entries; Workflow; Guest Access; Collecting Payments; Calculations; Data Integration; Document Generation; Account & Organizations
  - Product pillars page titles: Data Collection ("gather, format, and validate data through different field types"); Workflow Automation; Data Management; Security & Compliance (HIPAA, GDPR, CCPA); Online Payment (Cognito Pay)

Tier 2 (official product surfaces, contextual only):
- Jotform root/features menus (products, features, industries, template categories) — https://www.jotform.com/
- Formstack suite menus — https://www.formstack.com/
- Cognito Forms template/industry taxonomy — https://www.cognitoforms.com/templates/type

Unreachable / limited:
- support.google.com (×2 timeout), google.com/forms/about (×1 timeout) — abandoned per the one-to-two-failure rule; Google Forms not used for any operational claim.

## Product Observations

### Jotform (evidence layer A — official user guide, fetched 2026-09-08)

**Form creation**
- Start from Workspace → Create → Form; choose Start from Scratch or Template ("over 20,000 premade forms" — vendor claim, L3).
- Layout choice at creation: **Classic Form** ("displays all questions on a single page") vs **Card Form** ("shows one question per page for a guided experience").
- Builder is drag-and-drop; positioning statement: "create web forms without any coding ... intuitive drag-and-drop builder".

**Form elements (the field palette)**
- Add Element menu with tabs: **Basic** (Name, Email, Short & Long Text, Multiple Choice, Dropdown, Date Picker), **Payments** (PayPal, Stripe, Square gateways as elements), **Widgets** (e-signatures, file uploads, rating scales, progress bars — plus widget marketplace incl. Likert variants, configurable lists, remote-data dropdowns).
- Form Designer (paint-roller): Colors / Styles / Themes / Layout tabs; custom CSS injection documented as the beyond-the-designer option.

**Notifications**
- A notification email is **auto-generated by default** when a form is created; owners add recipients; autoresponder emails to respondents are a separate configured email ("reassure users that their submission was received").

**Publishing / distribution**
- Publish tab: Copy link ("send it directly to your users via email or social media"); guides for sending via email; embedding (guide titled "Adding a Contact Form to Your Facebook Page"); custom domains as a separate chapter; enable/disable form is a named feature; assign forms; prefill forms; translate forms.

**Testing**
- Preview toggle → fill and submit a test entry → check notification email and Table Submissions.

**Submissions (Jotform Tables)**
- Jotform Tables is "the central workspace for your submission data", reachable from Workspace, Form Builder, Inbox, Workflow Builder, PDF Editor, Report Builder.
- Capabilities documented on the submissions page: search, filter, add formulas, edit submissions, request submission updates, direct emailing, share/collaborate, add/change views, export to Excel/CSV/PDF, download uploaded files, print entries.
- Related-article titles corroborate: Submission ID ("Where to Find the Submission ID"), Incomplete submissions exist (user comment confirms a save-and-continue feature with an Incomplete-submissions tab), approval statuses exist ("Approve"/"Awaiting Approval").
- Suite modules around the core (all named products, L3): Inbox, Workflows (approvals), Apps, Boards, Report Builder, Smart PDF Forms, PDF Editor, Sign, Store Builder, Appointments, Tables.
- Features list (named, L3-ish but category-typical): conditional logic, conversational forms, HIPAA forms, secure forms, teams, white labeling, multiple users, embeddable form builder.
- Footer positioning: "online form builder ... data collection, payments, and workflows ... without coding."

### Microsoft Forms (evidence layer A — official support articles, fetched 2026-09-08)

**Creation**
- "With Microsoft Forms, you can create surveys, quizzes, and polls, and easily see results as they come in."
- Sign-in with Microsoft 365 school/work credentials or a personal Microsoft account (platform identity for the owner).
- New Form → title (≤90 chars) + description; **"Your form is saved automatically while you create it."**
- Question types: Choice, Text, Rating, Date; More question types: Ranking, Likert, File upload, Net Promoter Score; **Section** to organize pages.
- Text formatting in titles/questions (bold/italic/underline/color/size/lists).
- Preview on computer or mobile; test submit; Back to editing.
- Embedding surfaces: standalone; **Forms for Excel** (work/school — responses collected to an Excel workbook; also Insert > Forms inside Excel); **OneNote** embed (education).
- Branching logic named as a follow-on resource; themes; pictures in questions.

**Settings (per form/quiz)**
- **Who can fill out this form**: "Anyone can respond" / "Only people in my organization can respond" (with **Record name** and **One response per person**) / "Specific people in my organization can respond" (org-only tiers; Education/business licensing required — exact limits L3).
- **Accept responses** toggle with customizable closed message; **Start date / End date** for the collection window; **time duration** (timed form; auto-submit at expiry).
- Shuffle questions (all vs lock-question; not available with sections); disable question numbers; progress bar (multi-section only); hide "Submit another response"; custom thank-you message.
- **Response receipts**: respondent can save/print a PDF of their own answers; internal respondents can request email receipt; owner "Get email notification of each response"; smart reminder emails; org classification labels.

**Important structural rule**
- "If you delete a question, it will be **permanently deleted along with any response data that's been collected for it**." (Form definition and collected responses are structurally coupled per field.)

**Quiz variant (education pole)**
- Quiz-only settings: practice mode, show results automatically (per-question correct/incorrect), show answer explanations (Copilot-generated, editable), "Open with Windows 10 Take a Test" (secure testing environment), points/grading machinery (quiz guide title).

**Boundary marker (vendor's own)**
- "Want more advanced branding, question types, and data analysis? Try **Dynamics 365 Customer Voice**." — the vendor positions the simple form product below the enterprise experience-management product on the analysis axis.

### Formstack (evidence layer A at category/section level — fetched 2026-09-08)

**Positioning (suite pole)**
- Forms category blurb: "Create custom online forms, collect data, and automate processes with our **drag-and-drop form builder**. **No coding required**."
- Suite context: Formstack = Forms + Documents + Sign (+ Salesforce flavor, + Workflows product); "workplace productivity suite ... digitize ... automate workflows ... without code" — forms are the data-capture layer of a process-automation suite.
- Footer notes the suite serves "25,000+ organizations" (vendor claim, L3).

**Documented machinery (titles/sections)**
- Getting Started sections: **Form Types**, **Manage Forms and Permissions**, Forms Account Overview — permission machinery is a first-class help area.
- Security section (18 articles): Password Protecting Your Form; **Using SSO to Password Protect a Form**; SSL/embedding security; Content-Security-Policy headers; DPA opt-in; phishing-flag remediation ("My Form was flagged for Phishing").
- Trending articles: **Export Submission Data**; **Data Encryption**; Mobile Signing.
- Forms audited for WCAG 2.1 AA compliance (accessibility posture).
- Integrations section: 99 articles incl. PayPal connected path, Power Automate large-file upload, Documents integration, prefill-via-API, respondent incentives.

### Cognito Forms (evidence layer A — official user guide, fetched 2026-09-08)

**Product pillars (menu self-description)**
- Data Collection: "Easily gather, format, and **validate data** through different **field types**."
- Workflow Automation; Data Management ("organize, configure and transfer data, and create reports and documents"); Security & Compliance (HIPAA, GDPR, CCPA); Online Payment (Cognito Pay).

**Guide taxonomy (what the product is made of)**
- Building Forms ("use the builder. Set up notifications. Manage forms."); Style & Publish ("customize styles. Add logos and images. **Embed forms**."); **Managing Entries**; Workflow ("create actions. **Manage entry statuses**. Share role-based links."); **Guest Access** ("create secure, self-service portals for clients, members, patients, students"); Collecting Payments; **Calculations** ("use conditional logic. Hide and show fields. Example calculations."); Data Integration ("create webhooks. Prefill fields. Integrate with third-party apps."); Document Generation ("generate PDF and Word documents from your form entry data"); Account & Organizations.

**Entries — the submission object (deep evidence)**
- Framing: "Creating your form and sharing it with your customers is just step one — what happens to all that data after it gets submitted?"
- Entries page per form: default view named **All Entries**; owners create **saved entry views** (customized filtered data sets); sort/filter/hide columns; each entry shows **submission date** and **entry status**; newest first; expand entry details (repeating sections/table fields open inside the entry).
- **Owner-side entry operations**: create entries manually (Grid/Task/Form views with "Allow New Entries" control); **edit existing entries** (click into fields, save or discard changes); **change entry status** (single or bulk; statuses include **Incomplete** and **Submitted** plus custom statuses); **delete entries (permanent)**; print entries; **Read/Unread** marking (submitted entries start Unread/bold, auto-flip on open; independent of workflow status; Incomplete entries excluded); **bulk actions** (status changes, emails, integrations; run in batches of 100; conditional-logic rules still apply, entries under those rules are skipped); **entry numbers** (unique sequential ID assigned at first save/submit, "never changes, and it will never be reused; even after the entry is deleted"; referenceable in calculations, confirmation pages, and notification emails; custom ID codes derivable via calculation; payment entries get a separate transaction number).
- Entry-level articles: importing entries; exporting entries; downloading files (uploads); downloading documents; **auditing entries**; **encrypting entries**; sharing entries; HIPAA compliance; data security.

**Template/industry taxonomy (use-case breadth)**
- Template families: Application, Contact, Portal, Customer Service, Patient Intake, Order, Event Registration, Reporting, Survey & Quiz.
- Industries: accounting, churches, education, government, healthcare, home services, HR, IT, insurance, legal, manufacturing, marketing, nonprofits, travel, real estate, restaurants, retail.

## Cross-product Comparison

| Dimension | Jotform | Microsoft Forms | Formstack | Cognito Forms | Layer |
|---|---|---|---|---|---|
| Interactive builder assembling typed fields (no coding) | Yes (drag-and-drop, element tabs) | Yes (Add new → question types) | Yes (category blurb) | Yes (builder guide) | B |
| Form as stored, re-editable configuration object | Yes (workspace asset, preview, re-edit) | Yes (auto-saved form in My Forms list) | Yes (managed forms + permissions) | Yes (form sidebar, builder) | B |
| Published fill-and-submit surface (link; embed) | Yes (copy link; embed guides; custom domains) | Yes (share/send; Excel/OneNote embed) | Yes (embed/SSL articles) | Yes (Style & Publish: embed) | B |
| Respondents need no account by default | Yes (link-based collection) | Configurable: anyone vs org-only vs specific people | Configurable (password/SSO gating options) | Yes (link-based; Guest Access is optional portal layer) | A/B — mixed; default-open common, identity optional |
| Submission persisted as individual structured record | Yes (Tables rows; Submission ID) | Yes ("see results as they come in") | Yes (Export Submission Data article) | Yes (entries with number, date, status) | B |
| Owner-side collection view (table/entries) | Yes (Jotform Tables: filter/search/views) | Yes (Results pages; Excel sync) | Yes (submissions + export) | Yes (Entries page, saved views) | B |
| Submission metadata: ID + timestamp + status | Yes (ID article; Incomplete + approval statuses) | Partial (per-response email notification; results view not fetched) | Implied (export) | Yes (explicit: number never reused, date, status classes) | A/B |
| Owner can edit stored submissions | Yes (edit submissions in Tables; request updates) | Not observed (deleting question deletes its data instead) | Not observed directly | Yes (edit entry fields; save/discard) | A (2/4) — common, not definitional |
| Notifications: owner alert + respondent confirmation | Yes (auto notification; autoresponder) | Yes (email per response; receipts) | Implied (category: automate) | Yes (notifications in Building Forms) | B |
| Export collected data | Yes (Excel/CSV/PDF; files; print) | Yes (Excel sync is native output) | Yes (Export Submission Data) | Yes (export entries; download files/documents) | B |
| Templates library | Yes (20,000+ claim) | Yes (create.microsoft.com templates linked) | Yes (templates site section) | Yes (template families) | B |
| Branding/design themes | Yes (Form Designer: colors/styles/themes) | Yes (themes) | Implied | Yes (Style & Publish) | B |
| Conditional logic / branching | Yes (guide title; named feature) | Yes (branching logic) | Not fetched (implied by automation positioning) | Yes (Calculations: conditional logic, hide/show) | B (3/4 direct) |
| Multi-page / sections | Yes (Card form; Classic) | Yes (Sections; progress bar) | Not observed | Not observed directly (repeating sections) | B (2/4 direct) |
| File upload | Yes (widget) | Yes (question type) | Yes (Power Automate large-file article) | Yes (download files article) | B |
| Payments | Yes (payment element tab; gateways) | No (not in question types) | Yes (PayPal connected path) | Yes (pillar; Cognito Pay; transaction numbers) | B (3/4) — optional capability |
| Calculated/computed fields | Widgets/formulas in Tables | Not observed | Not observed | Yes (Calculations engine; Entry.Number expressions) | A (1/4) — product-strength variant |
| Quiz/grading mode | Not observed | Yes (deep: grading, practice mode, secure browser) | Not observed | Not observed (Survey & Quiz templates only) | A (1/4) — education variant |
| Approval/status workflow over submissions | Yes (Workflows product; approval statuses) | Not observed | Yes (Workflows product) | Yes (Workflow guide; statuses; role-based links) | B (3/4) — adjacent module, not core |
| Document generation from entries | Yes (PDF products) | Not observed | Yes (Documents product) | Yes (Document Generation guide) | B — adjacent module |
| Portal/guest access for respondents | Not observed | Not observed | Not observed | Yes (Guest Access) | A (1/4) — variant |
| AI assistance | Yes (AI agents, Claude/ChatGPT form builders) | Yes (Copilot in Forms; generated explanations) | Not observed | Yes (support chatbot; blog) | B — era-current |
| Suite/module packaging | Yes (Inbox/Boards/Apps/Store...) | Yes (M365-native; Customer Voice upsell) | Yes (Documents+Sign+Salesforce) | Yes (portals, documents) | B |
| Respondent identity recording (verified) | Not observed as default | Yes (org-only modes: record name, one response per person) | Password/SSO gating | Not observed as default | A/B — variant per product |
| Accessibility program | Yes (accessible-forms chapter) | Not observed | Yes (WCAG 2.1 AA audit) | Not observed | A/B |
| Compliance modes (HIPAA etc.) | Yes (HIPAA chapter) | Org classification labels | Yes (DPA, encryption) | Yes (HIPAA/GDPR/CCPA pillar; entry encryption) | B — enterprise posture |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures:

1. **The builder-authored form definition** — a form assembled interactively in a design surface from configurable typed fields/questions (labels, answer types, ordering, required/format constraints, layout/pages), held as a named, stored, re-editable configuration object owned by the form owner — not hand-coded software. Remove it → hand-coded HTML forms or a PDF/PDF-form designer (what this Type replaces), not a form builder application.
2. **The provisioned respondent surface** — the definition is published as a fill-and-submit page that respondents open (hosted link, embed, QR, or generated/embedded markup) without writing code, and without the respondent needing an account in the default case. Remove it → a form *design* tool (a questionnaire document), not a collector.
3. **The submission as a persisted, owner-retrievable record** — each completed fill is captured as an individual structured record (field values, timestamp, identifier, status) held in the owner's collection, retrievable and workable later (view, export, notify, route). Remove it → a static questionnaire or a live poll with no per-submission records.

Jointly-held is load-bearing:
- 1+2 without 3 = form design/publishing with no collection (a document).
- 1+3 without 2 = a data-entry tool for the owner only (no respondents).
- 2+3 without 1 = hand-coded web forms with a mail handler — the thin ancestor, not the application.
- 1 alone = a form designer; 2 alone = a web page; 3 alone = a database.

Historical / market-sample check (§24): early web form services (builder + hosted page + stored entries + email to the owner) satisfy all three without payments, logic, portals, AI, or even tables views; suite-native and education-tier products satisfy; platform-native products (Microsoft Forms) satisfy; kiosk/offline data-entry variants satisfy (records sync later). Paper forms are pre-history — the Type *is* the digitization of the fill-in form. Hand-coded HTML forms fail leg 1 by design — they are what the builder replaces. The core therefore does not depend on cloud delivery, drag-and-drop specifically, respondent accounts, or any specific distribution channel.

### L1 — Common Mature Structure (cross-product, not definitional)

- Template libraries (thousands of ready forms per vendor) + themes/branding (form designer: colors, fonts, logos, layouts).
- Broad field palette: short/long text, choice/dropdown, date, rating, file upload, e-signature widget; per-field required/format validation with entry-time error messages.
- Conditional logic / branching (show/hide fields, section jumps); multi-page forms with sections and progress.
- Distribution machinery: link, email, website embed, QR, social; enable/disable collection; response windows (start/end); custom closed/thank-you messages.
- Submission management view: table/grid with filter, sort, saved views, column control; per-entry detail; entry IDs; Read/Unread; statuses; bulk actions.
- Notifications: owner alert per submission (often auto-configured at creation); confirmation/autoresponder to respondents; respondent receipts of own answers.
- Export: Excel/CSV/PDF, uploaded-file download, print.
- Integrations spine: spreadsheets, CRM, storage, webhooks, automation platforms, API; prefill via URL/API.
- Collaboration: teams, shared form editing, permissions, sharing entries; admin/user management.
- Security/compliance posture: encryption, password/SSO-gated forms, abuse/phishing controls, HIPAA/GDPR/CCPA tooling at the enterprise pole, accessibility programs.
- Basic reporting/analytics over collected data (aggregates, charts) — light by design; depth belongs to survey/analysis Types.

### L2 — Variant / Optional Structure

- Payments (order/donation forms; payment elements/gateways; per-entry transaction numbers) — 3/4 sampled, absent in the free platform-native pole.
- Calculation engines (computed fields, pricing, custom ID generation) — product-strength variant.
- Quiz/grading mode with secure-testing integrations — education variant.
- Presentation pole: one-question-per-page / conversational (card) forms.
- Owner- or staff-side entry creation; kiosk/mobile offline data entry (field data collection).
- Guest portals for repeat respondents (clients/patients/members).
- Document generation from entry data (PDF/Word).
- Approval/workflow routing over submissions (status chains, role-based links) — boundary-adjacent; products ship it as an adjacent module (see Boundary Findings).
- Respondent identity enforcement (org sign-in, record name, one-response-per-person, specific-people lists).
- Multi-language forms; prefill; respondent incentives; AI form generation/assistance (era-current).

### L3 — Vendor-specific (research notes only)

- Jotform: Jotform Tables/Inbox/Boards/Apps/Store Builder/Sign/PDF Editor as named sibling products; Classic vs Card layouts; 20,000+ template and 40M-user claims; Claude/ChatGPT builder integrations; prefill forms; enable/disable form; assign forms.
- Microsoft Forms: Forms for Excel workbook sync; OneNote embed; Take a Test secure browser; org classification labels; Dynamics 365 Customer Voice upsell line; 90-character title limit; Copilot in Forms.
- Formstack: Forms+Documents+Sign suite; Salesforce-native flavor; WCAG 2.1 AA audit; phishing-flag remediation flow; webmerge Documents API.
- Cognito Forms: "Entries" vocabulary; entry numbers "never reused"; `=Entry.Number + 1000` voucher-code pattern; Guest Access portals; Cognito Pay; support chatbot.

## Vendor-specific Findings

- **Analysis ceiling is vendor-marked**: the platform-native sample explicitly redirects "advanced data analysis" to a separate enterprise product (Customer Voice) — market-internal confirmation that deep analysis is outside this Type's center and inside the survey/experience-management family.
- **Suite packaging is the norm, not the exception**: all four sampled products sit beside workflow/document/sign/report modules. The form core remains separable; modules are packaging.
- **Owner-side data authority differs**: two products document owner editing of stored submissions; the platform-native sample instead couples question deletion to data deletion (definition-edit affects collected data). Do not generalize either behavior as the Type's rule.
- **Respondent identity posture differs**: default-open link collection is common, but verified/recorded respondent identity is a first-class mode in the org-tier product and gating (password/SSO) is a first-class topic at the business tier — identity is a settings axis, not a defining property.
- **Vocabulary differs**: submissions (Jotform) / responses (Microsoft) / submissions+entries (Formstack/Cognito) — same conceptual object.

## Boundary Findings

1. **vs Survey Platform (§03.11 sibling, unprocessed) — sharpest seam, JOINT REVIEW RECOMMENDED.** Both author question instruments and collect responses. Proposed discriminator: this Type's center is the **per-submission record produced for downstream use** (the owner processes, exports, routes, or integrates each entry); the survey Type's center is **measurement** (instruments tuned to opinion/scales, aggregate analysis and reporting as the deliverable). Supporting evidence: the enterprise experience-product upsell line sits on "advanced data analysis" (market's own gradient); the employee-survey pass already framed surveys as "measure attitudes through scales and aggregate analysis" vs forms capturing "structured submissions into record/table output"; the research-panel pass framed survey platforms as "instrument authoring/fielding to non-persistent respondents." The instrument machinery is shared; the output object and analysis depth differ. Straddle zone is wide (one sampled product sells both Survey & Quiz templates beside order forms).
2. **vs Questionnaire Application (§03.11 sibling, unprocessed)** — likely near-alias of Survey Platform or of this Type's instrument layer; flagged for that pass with this document as counterparty.
3. **vs Polling Application (§03.11 sibling, unprocessed)** — a poll is one question (or a small set) with instant aggregate display; a form is a multi-field instrument whose defining output is persisted per-submission records. The audience-response pass already held the session-instrument test for live polls; async poll tools that persist records drift toward this Type; this Type's forms never center the live-aggregate loop.
4. **vs Lead Capture Platform (§06, processed)** — consistent with that pass: "neutral data collection for any purpose" vs revenue-intent semantics (identity + attribution + handoff). Form machinery is capability inside that Type, never its definition.
5. **vs Event Registration Platform (§26, processed)** — consistent with that pass: intake-without-event-machinery vs event offer + take-up state + roster. Form-builder RSVP = the boundary case that pass named.
6. **vs Event Management Platform (§26, processed)** — consistent: a form collects responses; the event platform anchors them to an event lifecycle.
7. **vs Approval Workflow Platform (§10, processed)** — consistent with that pass's line ("ends at collecting structured data"). Cross-evidence: sampled products ship approval/workflow routing as *adjacent modules* (named workflow products in two suites; status machinery in the fourth) — the collection core and the routing layer remain separable.
8. **vs Electronic Data Capture (§22, processed)** — consistent: that Type's protocol/participant/visit structure, site-scoped roles, and regulated record posture are absent here; that pass's own removal test ("remove the participant×visit protocol structure → generic form builder") terminates at this leaf.
9. **vs Digital Waiver Management (§26, processed)** — consistent: no release instrument, no signer binding, no evidentiary archive; that pass's removal test terminates here ("remove the release document → form builder").
10. **vs Employee Survey Platform (§09, processed)** — consistent: workforce population + confidentiality machinery define that Type; remove the workforce orientation and the generic instrument remains — this leaf is that generic instrument's record-capture pole.
11. **vs Structured Table / Lightweight Database Application (§03.03, unprocessed)** — table-centric data model the owner works vs respondent-intake front-end producing per-form record sets. Watch: one sampled vendor ships a Tables product beside its builder (adjacent capability, not the form core); database products ship form views (reverse direction). Seam = center of gravity; flag noted for that pass.
12. **vs Landing Page Builder (§04.16) / Website builders** — page/experience center vs form/instrument center; forms embed into pages as capability.
13. **Removal tests** ("去掉什么就变成另一个 Type"):
    - Remove the builder leg → hand-coded web forms (not an application in this directory).
    - Remove the respondent surface → form design tool / PDF designer.
    - Remove persisted per-submission records → static questionnaire or live poll (Polling territory).
    - Add measurement/analysis as the center → Survey Platform territory.
    - Add revenue-intent identity/attribution/handoff → Lead Capture Platform.
    - Add event offer + roster → Event Registration Platform.
    - Add decision-routing chains as the center → Approval Workflow Platform.
    - Add the release instrument + signer binding → Digital Waiver Management.

## Uncertainties

- Google Forms (the free/platform-native consumer pole) was unreachable this pass (3 failures across Google properties); it is used only as positional context, not evidence. Its inclusion in Representative Products reflects market centrality (competitor comparison pages) rather than studied documentation.
- Wufoo and other legacy form services were not fetched; the historical check is structural (builder + hosted page + stored entries + notification satisfies the core), not source-verified against a specific legacy product.
- Exact default notification behavior, response-volume limits, storage quotas, and retention defaults were deliberately not asserted — pricing-tier-dependent (L3) and not systematically researched.
- Formstack evidence is category/section-level (help-center structure and article titles); no deep workflow page was fetched, so its submission-management details are held at lower strength than Jotform's/Cognito's.
- Whether "owner editing of stored submissions" is universal is unresolved (documented in 2/4; the counter-behavior — question deletion destroying collected data — documented in 1/4).
- Microsoft Forms results-view mechanics (aggregate charts vs itemized responses) were not fetched; "see results as they come in" is the only claim carried.

## Final Synthesis

An Online Form Builder is an owner-side instrument tool built around one object (the form definition), one act (a respondent filling and submitting the provisioned surface), and one output (the persisted per-submission record the owner collects and works). Its defining loop: assemble the form interactively from typed fields → publish it as an open-to-respondents fill-and-submit surface (no respondent account by default) → capture each completed fill as an identified, time-stamped record in the owner's collection → work the collection (view, filter, edit where supported, notify, export, integrate). Everything else — templates, themes, conditional logic, file upload, payments, calculations, quizzes, portals, workflow routing, document generation, AI — is mature market structure, packaging variant, or adjacent module, not the definition. The Type stands independently of the survey family by output object and analysis depth (per-submission record for downstream use vs measurement deliverable), and every processed neighbor that borders it has independently defined itself against exactly this neutral-capture core.
