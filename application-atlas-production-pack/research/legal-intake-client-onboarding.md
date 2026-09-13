# Research Notes — Legal Intake & Client Onboarding

Research date: 2026-09-07

## Research Goal

Understand how software supports the law-firm-side (and legal-department-side) process of converting an unsolicited legal inquiry into an accepted client with an executed engagement and an opened matter: what objects exist, how the intake workflow moves, what the legal-profession-specific screening and decision steps are, and where this Application Type ends and neighboring Types (Law Practice Management, Legal Conflict Checking, generic Lead Management/CRM, Customer Onboarding) begin.

## Initial Boundary

Working hypothesis before research:

- Core use: capture prospective-client inquiries (web, phone, referral, ads), screen them (conflicts, merits, value), record an accept/decline decision, execute the engagement agreement, and hand the accepted client into the firm's matter system.
- Likely users: intake specialists / new-business teams, intake or marketing coordinators, evaluating attorneys, conflicts/risk teams, firm management.
- Nearest types: Law Practice Management System (downstream system of record), Legal Matter Management (matter container), Legal Conflict Checking Platform (deep conflicts machinery), Lead Management Platform / CRM (commercial analogue), Customer Onboarding Platform (SaaS analogue), Employee Onboarding Platform (HR analogue).
- Main unknowns: whether conflict checking belongs in the defining core of intake or is a separable platform; whether the corporate "new business intake" pattern (risk/AML-driven) and the consumer-law "intake funnel" pattern are one Type or two; whether enterprise legal-department "matter intake" (internal request triage) fits.

## Research Questions

1. How do prospective clients enter the system (capture surfaces)?
2. What is the central object — a lead, a contact, a prospective matter, a "PNC" — and how does it relate to contact and matter records?
3. How is screening organized (conflict check, case evaluation, qualification)?
4. How is the engagement decision recorded, and what happens on decline?
5. What does "onboarding" consist of after acceptance (engagement agreement, retainer, documents, payments)?
6. How does the accepted client land in the firm's client/matter system of record (native vs integration vs sync)?
7. Which roles use which surfaces (intake staff vs attorneys vs conflicts/risk vs the prospective client themselves)?
8. Which variants are strong enough to matter (consumer-law funnel vs large-firm new business vs legal aid vs corporate legal matter intake)?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy / Tier | Role in sample |
|---|---|---|
| Lawmatics | pure-play legal intake CRM for consumer-law firms (PI, immigration, family); marketing-funnel philosophy; SMB/mid-market | standalone pole |
| Clio Grow | intake/onboarding module attached to a practice-management suite (Clio Manage); SMB | suite-embedded pole |
| PracticePanther | all-in-one practice management with native intake; intake as built-in PM function | PM-native pole |
| Intapp Intake | enterprise "new business intake" for large firms; risk/compliance-driven; also sold to accounting/consulting | enterprise risk-gate pole |

## Sources

Primary (fetched 2026-09-07):

- Lawmatics — product page https://www.lawmatics.com/ (Tier 2); help center https://help.lawmatics.com/ structure (Tier 1 index); articles: "Intake Pipeline" (10699827), "Contacts vs. Matters" (10699803), "Conflict Checking" (10699811), "How to Automate Sending Engagement Agreements" (11328508) — Tier 1
- Clio — help center https://help.clio.com/ root + Clio Grow section (52398828497051) + Grow AI section (52131060989083) + Intake Forms section (48844695294875); article "Send, View, and Manage Intake Forms" (9284567246747) — Tier 1. Note: www.clio.com product/marketing pages returned 403 (blocked); clio.com evidence is help-center only.
- PracticePanther — product page https://www.practicepanther.com/ (Tier 2); "Legal client intake software" feature page https://www.practicepanther.com/legal-crm/client-intake-software/ (Tier 2). Help center not directly sampled.
- Intapp — product index https://www.intapp.com/products/intapp-intake/ (nav only); legal new-business-intake solution page https://www.intapp.com/legal/new-business-intake/ (Tier 2, includes feature list, customer quotes, case-study/webinar titles); AML page exists at /legal/new-business-intake/aml-kyc-cdd/ (title/snippet only). Intapp operational docs (support.intapp.com) not fetched.

Not reachable / not sampled: Clio marketing pages (403 ×2), PracticePanther help-center articles (not attempted after product pages sufficed), Intapp support documentation portal, Lawmatics pricing page. No third-party reviews were needed; vendor docs were sufficient for structure but some precise operational rules remain unverified (see Uncertainties).

## Product A — Lawmatics (pure-play legal intake CRM)

Evidence layer: A (direct observation of official help articles).

Key observations:

- **Matter-centric intake pipeline.** "One of the most important processes you will be managing with pipelines, is your firm's intake… the Intake Pipeline is already created in your account." Firms add their own stages; each stage is a milestone; matters may skip stages that do not apply. [A]
- **The intake unit is the Matter, classified as a PNC.** Contacts are people; Matters are cases. Every matter has one primary contact. Contact-level preset views: "has open matters (PNCs)", "has hired matters", "has lost matters", "no matters" — i.e., prospective-new-client vs hired vs lost is a first-class status split. Pipeline displays only matters. [A]
- **Stage automation as the organizing rhythm.** Sample stages: New Lead (trigger drip campaign), Missed Consultation (auto-send reschedule booking links), Intent to Hire (auto-send fee agreement for e-signature), Fee Agreement Signed (trigger new-client tasks, welcome letter). Automations can move a matter into a stage (e.g., consult booked → "Consult Scheduled") and act on stage entry. [A]
- **Revenue funnel machinery.** Intake pipelines carry financial data: per-matter Estimated Value, stage Total Value, and Expected Value computed from historical conversion (hired ÷ total) — "the goal of an intake pipeline is to convert leads into clients, ultimately bringing revenue into your firm". [A]
- **Conflict checking embedded at intake scale.** Conflict checks search across matter fields/notes/records with approve / deny / flag outcomes; manual or automation-triggered; check history with verification status, search terms, date; term matching exact/contains, AND/OR combinations. This is lightweight screening against the firm's own records — not a full conflicts database product. [A]
- **Engagement agreement automation.** Intake forms carry a "Next Steps" dropdown ("Send Engagement Agreement"), which triggers an automation (Target Type: Matter, Status: Potential New Client (PNC)) that sends the engagement agreement and signing reminders. [A]
- **Capture surfaces.** External custom forms embedded on the firm website; website-lead automation; booking links/appointment scheduling with confirmations/reminders; two-way SMS/MMS; drip email campaigns; marketing source/UTM attribution and ROI tracking; file requests from clients; e-signature on DOCX/PDF; duplicate-avoidance machinery for forms/imports. [A]
- **AI lead qualification (2026-era).** "Merlin Qualify" scores leads instantly (AI agents + QualifyCopilot + lead-score reporting); website chat and voice-agent tooling in the suite. [A]
- **Adjacent suite modules** (time & billing, marketing automation, reporting) exist in the same product but were not treated as intake core. [A]

## Product B — Clio Grow (suite-embedded intake module)

Evidence layer: A (official help-center articles); note clio.com marketing pages unreachable (403), so positioning evidence is help-center-derived.

Key observations:

- **Intake lives on the matter.** Intake forms attach to a matter's "Intake process" section; items can also be grouped via checklist templates and automated workflows/email campaigns. A standalone Forms tab also exists with Pending/Submitted subtabs. [A]
- **Quick Form = the conversion primitive.** "A Quick Form is a combination of an intake form and a new contact with a new matter… Clio Grow will also create a new contact and matter for your prospective client." Matter type and status are entered at creation. [A]
- **Two filling modes.** Staff can fill the form on behalf of the prospect ("Fill out form… if your prospective client is at your office or on the phone with you") or send the form to the client by email/text; the prospect can save progress and return. [A]
- **Managed form lifecycle.** Due dates per form; reminders by email/text; resend on expiry; forms download as PDF; submitted forms are client-edit-locked — administrators can edit, and the edit is saved as a second PDF alongside the original with a Timeline record. [A]
- **Suite handoff is native.** Grow operates on Clio Manage contacts/matters; e-signature, documents (Clio Draft), billing (Clio Manage) are sibling modules. Grow section also covers tasks/checklists and "Strategy and Growth" (marketing channel tracking, reviews). [A]
- **AI lead capture/screen/convert (2026-era).** "Grow AI — AI-powered tools to help your firm capture, screen, and convert leads": lead intake AI, website chat tool, voice agent. [A]

## Product C — PracticePanther (PM-native intake)

Evidence layer: A (official product + dedicated intake feature page).

Key observations:

- **Intake as a built-in practice-management capability.** "Close prospective clients faster with automated Client Intake… automated Client Intake forms"; intake is listed among core PM responsibilities ("Client Intake and Onboarding" with intake forms + consultation scheduling). [A]
- **Form → CRM contact sync.** "PracticePanther automatically syncs intake form data as Contacts in its CRM database"; custom fields capture case details; unlimited forms per practice area; branded forms; embeddable on website/email signatures; dedicated practice landing pages. [A]
- **Downstream integration is native (same system).** Submitted form alerts attorneys; custom workflows and automated emails for quick consultation calls; eSignature notifies "the moment a client signs, so you can start their case right away". Lead-source captured via custom fields + Tags for reporting. [A]
- **Conflict check positioned as PM responsibility.** "Conflict Checking: … software can quickly perform conflict checks by cross-referencing new client data with existing information" (FAQ on the PM page). [A]
- Note: PracticePanther models the prospect primarily as a **Contact** record (form→Contacts sync), whereas Lawmatics/Clio model the prospect primarily as a **matter/PNC**. Same workflow, different primary record. Recorded as a modeling variation, not a contradiction.

## Product D — Intapp Intake (enterprise new business intake)

Evidence layer: A (official solution pages; feature list and quotes), with the caveat that only Tier-2 surfaces were fetched (no operational docs).

Key observations:

- **Positioning:** "Speed up new client and matter intake using firm-configured questionnaires, workflows, and risk assessments. Powered by firm and third-party data… review the most up-to-date information on your potential client." [A]
- **Screening as the core of the product.** Firm-configured questionnaires; risk and AML scoring ("define risk-based criteria to automatically score and apply approval routing"); centralized review; natively embedded third-party data (corporate tree, industry codes, sanctions lists — Bureau van Dijk, D&B, S&P); AI request summaries; monitoring and alerting on changes to client and matter data (ongoing risk posture, not just at intake). [A]
- **Gatekeeper review.** Customer quote (Osler, Hoskin & Harcourt CKO): "We were able to include more questions relating to conflicts and risk, so that our gatekeepers could review the matter and determine whether it was work that the firm could take on." [A]
- **Engagement letter generation.** "Enforce firm policies through the automated creation and collection of engagement letters." [A]
- **Extended onboarding surfaces.** Secured external forms (collect external info such as AML documentation or lateral-hire data); joint client representation (assign joint clients to a matter — blog title); AML/KYC/CDD as a named sub-capability; lateral-hire onboarding reuses the same questionnaire machinery. [A]
- **Cross-industry packaging.** Same Intake product sold as "client onboarding and continuance" (accounting) and "client onboarding and risk assessments" (consulting). [A]
- **Suite context.** Sits next to Intapp Conflicts (dedicated conflicts product), Intapp Terms (outside-counsel guidelines), Intapp Walls (ethical walls) — i.e., at the enterprise pole, deep conflicts machinery is a separate product that intake feeds. [A]

## Cross-product Comparison

| Dimension | Lawmatics | Clio Grow | PracticePanther | Intapp Intake |
|---|---|---|---|---|
| Primary record for a prospect | Matter flagged as PNC | Matter (created with contact via Quick Form) | Contact (form syncs to CRM), matter created downstream | Intake request / prospective client + matter record |
| Capture surfaces | Web-embedded forms, website-lead automation, booking links, SMS | Sent intake forms (email/text), Quick Form, embedded forms; AI chat/voice | Embedded intake forms, landing pages, alerts | Firm-configured questionnaires; secured external forms |
| Screening | Conflict check (approve/deny/flag) vs own records; AI lead scoring | AI "screen" leads (Grow AI); conflicts handled in suite ecosystem | Conflict check cross-referencing new client data | Questionnaires + risk/AML scoring + approval routing + third-party data + sanctions |
| Consultation scheduling | Booking links, confirmations/reminders, no-show handling | Appointment scheduling in suite (Clio Scheduler) | Automated emails for consult calls; workflows | Not emphasized (enterprise new-business flow is less consult-driven) |
| Decision expression | PNC → hired / lost matter views; stage milestones | Matter status at creation; workflow stages in suite | Start case after signature | Approval routing on risk scores; gatekeeper review |
| Engagement execution | Auto-send engagement agreement (fee agreement) for e-signature on "Intent to Hire" | e-signature module; forms→PDF; admin edits versioned | Native eSignature; "start their case" after signing | Automated engagement letter generation and collection |
| Onboarding after acceptance | New-client tasks, welcome letters, file requests | Intake-process checklist continues; portal; payments in suite | Workflows, tasks, reminders, payments | Engagement letters; ongoing monitoring/alerting; walls/terms downstream |
| System of record handoff | Integration to PM systems (Clio/MyCase/Filevine integrations) or own suite | Native into Clio Manage | Native (same system) | Feeds firm systems; sits beside Conflicts/Terms/Walls |
| Revenue/marketing machinery | Estimated/Expected Value funnel; source ROI/UTM | Marketing-channel tracking (Strategy & Growth) | Lead source via fields/tags | Not a marketing tool; risk/compliance posture |
| Customer tier | SMB/mid consumer-law firms | SMB, all practice areas | Solo→large, all practice areas | Large firms (also accounting/consulting) |

Layer B (cross-product commonality, observed across ≥3 of 4):

- Capture of the prospective client as a managed record distinct from an accepted client. [B]
- A screening step before commitment — conflict screening against the firm's existing records appears in all four samples, in lightweight form. [B]
- A recorded accept/decline (hire/lost) outcome that changes the record's status class. [B]
- The engagement agreement (engagement letter / fee agreement / retainer) as the acceptance artifact, executed via e-signature in modern products. [B]
- Handoff of the accepted client into a matter (and client) record in a practice-management/matter system — native when integrated, via sync/integration when standalone. [B]
- Automated communication with the prospective client during intake (text/email confirmations, reminders, follow-up). [B]
- Intake forms with per-practice-area or per-matter-type configuration; duplicate-prevention when a prospect already exists in the system. [B]

## Canonical Model (synthesis, layer C inference)

The Type can be modeled as a gated conversion pipeline whose center of gravity is the prospective-client record:

```text
Prospective client (person/org + matter inquiry) — managed record, NOT yet a client
  ↓ capture (forms, web, phone, referral, marketing)
Screening gate — conflict screening + case evaluation/qualification (firm-defined)
  ↓ recorded outcome
Engagement decision — accept as client / decline (recorded, reportable)
  ↓ on acceptance
Onboarding closure — engagement agreement executed (e-signature) + client/matter opened in the firm's system of record
```

Four-part defining core (see Final Synthesis below): prospective-client record · screening gate · recorded engagement decision · onboarding closure into representation.

## Abstraction Levels

### L0 — Defining Invariant (minimal)

1. **Prospective-client record of record** — an identified person/organization with a legal matter inquiry captured and tracked as a managed record that is explicitly *not yet* a client (prospect/PNC/intake matter). Remove → a contact form / bare CRM; nothing legal remains.
2. **Screening gate before commitment** — the firm evaluates the inquiry through firm-defined checks before any obligation arises; conflict screening against the firm's own client/adverse-party records is the legal-signature instance. Remove → marketing lead capture, not intake.
3. **Recorded engagement decision** — an explicit accept-as-client / decline outcome recorded against the prospective record (declined representation stays reportable). Remove → a lead tracker with no professional gate; the Type collapses into generic Lead Management.
4. **Onboarding closure into representation** — on acceptance, the relationship is formalized (engagement agreement executed) and the client/matter enters the firm's client-matter system of record. Remove → a decision list; the "client onboarding" half of the Type disappears.

Jointly-held is load-bearing: 1+3 without 2+4 is a CRM; 2+3 without 4 is a screening register, not onboarding.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Intake form builder (per practice area/matter type), website embedding, landing pages
- Automated first response and nurture: email/SMS confirmations, reminders, drip campaigns, booking links, consultation scheduling, no-show handling
- Intake pipeline with firm-defined stages and stage-triggered automations
- E-signature of engagement agreements/retainers with templates and reminders
- Document/file requests from the prospective client
- Payment/retainer collection during intake (in several products)
- Lead-source tracking and marketing attribution/ROI reporting; conversion-rate reporting
- Conflict-check records with history (verification status, terms, dates) in lightweight in-product form
- Client portal access for the prospective/new client
- Bi-directional sync or native linkage with practice management / matter systems
- Role model separating intake staff, attorneys, conflicts/risk reviewers, admins
- Reporting/dashboards on intake funnel performance

### L2 — Variant / Optional Structure

- Market pole: consumer-law high-volume funnel (PI/immigration/family; marketing-led, speed-to-response philosophy) vs corporate large-firm new business intake (questionnaire- and risk-led; AML/KYC; gatekeeper committees; approval routing; third-party firmographic/sanctions data; ongoing monitoring after acceptance)
- Segment: legal aid / nonprofit intake with eligibility screening (not directly sampled — recorded as variant from market knowledge, low confidence)
- Audience: corporate legal department "matter intake" (internal employees requesting legal help) — adjacent, likely separate Type; recorded as boundary issue, not folded into this Type
- Packaging: standalone pure-play vs suite-embedded module vs PM-native feature vs enterprise risk-suite product
- Geography/regulation: AML/KYC obligations shape intake in some jurisdictions (directly observed as a product capability; jurisdictional mapping not verified)
- Current-market common additions: AI lead scoring, AI website chat / voice agents, AI request summaries

### L3 — Vendor-specific (research notes only)

- Lawmatics: "PNC" (Potential New Client) terminology; intake-pipeline toggle with Estimated Value / Expected Value formula (Total Estimated Value × historical hire rate); "Intent to Hire" / "Fee Agreement Signed" example stages; Merlin Qualify/Engage branded AI suite; "Show All Matters" pipeline toggle.
- Clio Grow: "Quick Form" primitive; intake-form link validity windows (14 days, refreshable to 30 days, then permanent expiry); admin-edited forms saved as second PDF with Timeline record; "Intake process" section per matter; Grow AI product naming.
- PracticePanther: intake forms sync to Contacts (contact-primary model); Tags for lead-source reporting; practice landing pages; "PantherPayments"/OneLink payment specifics.
- Intapp Intake: risk/AML scoring with automatic approval routing; engagement letter generation; joint client representation feature; Intapp Data firmographic enrichment; named data partners (Bureau van Dijk, D&B, S&P); monitoring/alerting on client/matter data changes; cross-industry packaging (accounting "client onboarding and continuance", consulting "client onboarding and risk assessments"); Osler gatekeeper quote.

## Vendor-specific Findings

See L3. Additionally: the **primary-record split** (prospect as Matter/PNC vs prospect as Contact) is a genuine modeling divergence between vendors. It does not change the workflow (capture → screen → decide → formalize → matter) but affects where intake state lives. The canonical model deliberately states the record conceptually ("prospective-client record") without committing to contact-primary vs matter-primary.

## Rejected Findings

- "Intake = marketing automation": Lawmatics bundles marketing automation deeply, but Clio/PracticePanther/Intapp do not define intake by marketing. Marketing attribution is L1 at most.
- "Intake requires conflict-check *deep search* engines": the deep conflicts machinery (firmwide full-text search, ethical walls, clearance workflows) is a separate directory Type (Legal Conflict Checking Platform); intake only requires that a screening step can be performed and recorded (Intapp ships Conflicts as a separate product; Lawmatics ships a lightweight in-product check).
- "Intake requires payment collection at signing": observed in suite products but not in the enterprise pole's core description; variant/optional.
- "Corporate legal matter intake (internal request triage) is this Type": different audience (employees, not external prospective clients), different object (service request, not client engagement). Boundary issue recorded.

## Boundary Findings

| Neighbor Type | Distinction | Removal test |
|---|---|---|
| Law Practice Management System | PM is the firm's system of record for accepted clients and active matters; intake covers the pre-acceptance record and the conversion into PM. In integrated products intake appears as a section/stage inside PM, but the intake surface (forms, pipeline, screening, engagement execution) remains the distinctive unit. | Strip prospective-client records + screening + decision gate from a PM and it still is a PM (active-matter system of record); strip active-matter management from intake and it still is intake. |
| Legal Matter Management | Matter is the downstream container this Type feeds; intake's object of record exists *before* the matter is accepted. | — |
| Legal Conflict Checking Platform | Intake *runs* a conflict screening step and records outcomes; the dedicated platform provides deep firmwide conflicts search, clearance workflows, walls. Enterprise vendor splits these into two products — vendor-internal evidence for separability. | Keep only screening → intake still stands with a recorded check; keep only deep search → conflicts platform, no conversion loop. |
| Lead Management Platform / CRM (generic) | Generic CRM captures and nurtures leads but lacks the professional gate: conflict screening, recorded accept/decline with non-engagement significance, engagement-agreement execution, matter creation. | A CRM re-labeled for lawyers without the gate is still lead management, not this Type. |
| Customer Onboarding Platform (§07) | Post-sale activation of a paying SaaS customer; legal client onboarding is the *pre*-representation acceptance step with professional-responsibility semantics. | — |
| Employee Onboarding Platform (§09) | HR object (employee record) vs legal object (client + matter). | — |
| Corporate legal "matter intake"/request triage | Audience = internal employees; object = service request routed to legal; no engagement decision with a prospective external client. Recorded as a likely separate Type / alias risk for future review. | — |

"去掉什么就变成另一个 Type" 判据（removal tests, canonical statement): remove the screening gate → Lead Management Platform; remove the recorded engagement decision → marketing capture; remove onboarding closure (engagement + matter handoff) → screening register; remove the prospective-client record entirely → practice management only.

## Historical / Market-Sample Check

- Pre-SaaS practice: paper intake forms, phone intake, a conflicts department checking index cards/early databases, engagement letters typed and mailed, matter opened in a paper register. All four L0 properties hold in this paper-era realization (record, screen, decide, formalize). The core is not an artifact of the SaaS intake-funnel era.
- Large-firm "new business intake" has been a named process since well before modern SaaS (Intapp's category dates to the 2000s); its realization (questionnaires, risk assessment, gatekeepers) satisfies the same core with a heavier screening gate.
- Older/simpler products (solo-practice paper intake; minimal practice-management with a simple intake form) satisfy L0 with only a form + a decision — no pipeline, no e-signature, no automation. Therefore pipelines, automation, e-signature, AI scoring are correctly L1/L2, not definitional.
- Regional check: UK/EU AML-regulated intake (Intapp AML page observed) adds compliance weight to the screening gate but does not change the structure.

## Uncertainties

1. Legal aid / nonprofit eligibility intake was not directly sampled (e.g., legal-aid case-management products). The variant is recorded with low confidence.
2. Intapp evidence is Tier-2 (solution pages). Operational details of questionnaires, approval routing, and matter handoff are asserted only at the strength of the vendor's own feature descriptions; no workflow precision claimed.
3. Clio marketing pages were unreachable (403); Clio positioning is inferred from its help center, which documents Grow thoroughly but may understate marketing-side capabilities.
4. Whether the market treats "Legal Intake CRM" and "Legal Client Intake software" as one category — sample strongly suggests yes (same workflow, different packaging), but no category-level source (e.g., analyst taxonomy) was fetched.
5. Payment collection during intake is common in the SMB suite sample but its universality is unverified.
6. Corporate legal department matter intake (internal request triage) is recorded as a boundary issue for taxonomy review; it may deserve its own Type or be folded elsewhere.

## Final Synthesis

Legal Intake & Client Onboarding is the law-firm-side conversion system whose defining core is four jointly-held structures: the prospective-client record (an identified person/organization with a matter inquiry, tracked as explicitly not-yet-a-client), the screening gate before commitment (firm-defined checks, with conflict screening against the firm's own records as the legal-signature instance), the recorded engagement decision (accept as client / decline, with declined representation remaining reportable), and onboarding closure into representation (engagement agreement executed, client/matter opened in the firm's system of record). Around this core, mature products standardize capture forms, automated communication and scheduling, intake pipelines, e-signature, file requests, conflict-check records, source attribution, and PM sync; the market splits into a consumer-law marketing-funnel pole and an enterprise risk-gate pole (with suite-embedded and PM-native packaging between), and the corporate-legal internal-request-triage pattern is a likely separate Type.
