# Research Notes — Offer Management Platform

## Research Goal

Understand what an Offer Management Platform is in the HR/recruiting sense (the DIRECTORY leaf sits in §09 HR, Workforce & Talent, between Background Check Platform and Employee Onboarding Platform): what objects exist inside it (the offer, its terms, its documents, its approvals), how the offer lifecycle runs from creation through approval to extension and response, who operates it, what rules govern it, and where the boundary sits against the Applicant Tracking System, Employee Onboarding, Compensation Management, Proposal Management (sales), and generic e-signature/approval machinery.

Also required: a naming-collision check. "Offer management" has a second, unrelated meaning in marketing/retail (managing promotional offers/discounts). A prior processed leaf (referral-marketing-platform, STATUS 2026-09-07) even uses the phrase "enterprise offer-management platform" for a growth-space product scope. The DIRECTORY placement (§09) is unambiguous, but the homonym is recorded as a boundary/taxonomy note.

## Initial Boundary (hypothesis before research)

- Core use hypothesis: the system of record for the employment-offer stage of hiring — turning a selected candidate into an extended, approved, accepted (or declined) offer, and handing the accepted offer to the hire/onboarding side.
- Likely users: recruiters/talent acquisition (create/send/track), hiring managers (approve, sometimes send), HR/comp (governance, templates), executives/finance (approvers), candidate (external — receives, signs/accepts/declines).
- Likely realization: predominantly a module/capability inside ATSs and HCM suites rather than standalone products; need to verify whether standalone offer products exist in the reachable market.
- Nearest types: ATS (container/pipeline), Employee Onboarding (post-acceptance), Compensation Management (comp structure that feeds offers), Proposal Management (sales-domain structural analog), CLM (contracts), Approval Workflow Platform (generic approval engine), e-signature (substrate).
- Unknowns: is the internal approval gate definitional or merely common? How deep does comp/band enforcement go? What statuses/exceptions are canonical (decline, rescind/cancel, expire, revise)? Historical (paper-era) fit?

## Research Questions

1. What is an "offer" as a system object — what does it bind (candidate × position × terms) and what does it carry?
2. What is the offer's lifecycle and canonical states (draft → approval → sent → response → outcome; versions/revisions)?
3. Is the internal approval gate definitional, or optional configuration? How are approvers organized (roles, groups, chains, thresholds)?
4. How does the offer document get produced (templates, variables/tokens, uploads) and delivered (email, portal, e-sign)?
5. What response/outcome states exist (accepted, declined with reason, expired, withdrawn/canceled/rescinded) and what side effects do they have (mark hired, requisition reopen)?
6. What permissions separate offer visibility (esp. salary) and actions (create/send/approve/cancel)?
7. What sits around the offer: requisition linkage, budget reporting, offer reports/analytics, onboarding handoff?
8. Where exactly is the boundary vs ATS (pipeline), onboarding (post-acceptance), compensation management (comp structure), and generic e-signature (substrate)?
9. Would paper-era offer practice (typed letter + internal sign-off + mailed response) still fit the definition?
10. Is the "offer management" name stable in the market, or a homonym collision with promotional-offer management?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Why selected |
|---|---|---|
| Greenhouse Recruiting (offer sections of support site) | structured-process ATS; mid-market/enterprise; offers as a first-class pipeline stage with configured approvals, versions, permission separation | the Type's center of gravity; deepest staged offer documentation |
| Workable (E-signature and offer documents section) | self-serve ATS; SMB/mid-market; wizard-driven offer creation, approval groups, requisition/budget linkage | shows offer machinery integrated with requisitions and budget reporting; explicit "offer type" vs "simple type" document separation |
| Breezy HR (Offers and Offer Approvals) | lightweight SMB ATS; template-centric offers with optional approval chains and integrated e-signing | the accessible end; proves the offer-vs-generic-eDocument separation and template+approval model at the SMB tier |
| SmartRecruiters (official site only) | enterprise ATS suite; brands "Offer Management" as a named module under its Hire pillar | market-level evidence that "Offer Management" is a vendor-articulated module name; help center gated so operational detail not evidenced |

Rejected/dropped samples: Lever (help center unreachable: search 401, root JS/CSS error — abandoned after 2 attempts), Ashby (help transport error), Teamtailor (support search 404 ×2), iCIMS/Workday/SAP SuccessFactors (help portals gated or known gated), Oracle Recruiting docs (book index reachable but TOC JS-rendered; PDF binary not machine-readable — abandoned at article level).

## Sources

Fetched 2026-09-08 (official vendor surfaces):

- Greenhouse Support — search index; https://support.greenhouse.io/hc/en-us/articles/200721744-Create-an-offer ; .../201165300-Request-approval-for-a-new-offer ; .../360035625832-Offer-Approval-Overview ; .../200485589-Generate-and-send-offer-document
- Workable Help — search index; https://help.workable.com/hc/en-us/articles/360001165533-E-signature-offer-approval-workflows ; .../360039944893-Sending-offer-and-e-signature-documents
- Breezy HR Help Center — https://help.breezy.hr/en/collections/2949195-manage-communicate-with-candidates ; https://help.breezy.hr/en/articles/8032833-offers-and-offer-approvals ; https://help.breezy.hr/en/articles/8047835-electronic-documents
- SmartRecruiters — https://www.smartrecruiters.com/ (homepage nav lists "Offer Management" module under HIRE); https://www.smartrecruiters.com/recruiting-software/offer-management/ (403 — not fetched)

Unreachable / abandoned (evidence-limitation record):

- Lever — help.lever.co search (401) and root (JS "CSS Error") — abandoned after 2 attempts
- Ashby — help.ashbyhq.com transport error — abandoned
- Teamtailor — support.teamtailor.com search 404 (en-gb, en-us) — abandoned
- SmartRecruiters — help center behind customer login; product page 403 ×2 — marketing-level evidence only
- Oracle Fusion Recruiting — docs.oracle.com books list reachable; "Using Recruiting" TOC JS-rendered; PDF binary unusable — abandoned at article level
- Workday / SAP SuccessFactors / iCIMS — help portals gated (consistent with prior sibling research) — enterprise-suite operational detail kept general

## Product Observations

### Greenhouse Recruiting

Evidence tier: A (official support articles, directly observed).

Key observations:

- Offers are a first-class pipeline stage: "Open the Stages tab … navigate to the Offer stage. Click Create Offer." Offer created from the candidate's profile once the candidate "has progressed to the offer stage."
- The offer is a data record: "Enter your offer details in the pop-up window"; offer details tab; "Offer fields provide a record of a candidate offer and can be used to generate additional documentation like offer documents" (custom offer fields exist; fields populate offer documents).
- Optional approval gate, configurable per job/org: "If your organization has configured an offer approval for the job" → request approval; "newly created offers … need to be submitted for approval before they can be sent to the candidate." Approval status displays as Pending "until all conditions of the job's offer approval process are completed"; once approved, "Greenhouse Recruiting displays the date the offer approval was issued."
- Approver organization: "There can be multiple approvers assigned to an approval flow and can be configured sequentially or non-sequentially. Additionally, approvers can be assigned by office or department." Users configured as offer approvers "will be notified that the new offer is pending approval."
- Without an approval process: users with permission immediately "Generate offer documents / Send offer documents to candidates / Mark candidates as hired" — i.e., the approval gate is explicitly optional configuration ("Offer flow with no offer approval process" is a documented first-class flow).
- Candidate-facing document production: upload an offer document template "with placeholder tokens," tokens populated from "the candidate's personalized offer details" (profile, job, offer details); generation produces .docx + .pdf; token errors surfaced when a value is missing/invalid (fix fields and regenerate, or download/edit/re-upload).
- Delivery: "Send with Greenhouse" (email dialog, offer email template, CC team members, attachments) or via DocuSign / Adobe Acrobat Sign integrations; alternatively "Send an offer document created outside of Greenhouse Recruiting"; signed offer document manually uploaded back ("Upload Signed Offer Document").
- Outcome: "mark the candidate as hired"; offer documents visible in the candidate's Documents panel ("Only the most current version of the offer document will be shown").
- Versions/revision loop: an existing offer with a Refresh trigger creates "a new offer version"; "Creating a new offer version and re-triggering the offer approval process" is a documented flow — revision re-runs the approval gate.
- Bulk creation: "Create offers in bulk" exists (high-volume variant).
- Reporting: "Offer details report" — fields include Recruiter, Offer status, Application date, Offer creation date, Offer sent date, Offer resolved date, Offer approvers.
- Permissions: Site Admin "who can see private notes, salary info, manage offers, request approval, and approve job/offers" and Job Admin "who can view and edit offers and approve/request approval on offers" — salary visibility is explicitly a permission axis.

### Workable

Evidence tier: A (official help articles).

Key observations:

- Offers live at the pipeline's Offer stage: "Move the candidate to the Offer stage … Click the pen tip icon … to select an offer template." Requisition linkage: with Hiring Plan, users "will be asked to open or select a requisition before choosing an offer template."
- The market itself separates the offer object from generic signing: templates are typed "offer" vs "simple"; "job offers are always sent in offer stages, feed into budget reporting, and can have approval workflows and internal signatures" — simple documents can be requested at any stage.
- Offer details as structured data: wizard step "Add details" fills fields "such as salary, start date, and direct manager"; prefills for Candidate/Job/Company/Sender/Signatory; "today's date" auto-populated; internal-only reference fields exist ("The candidate will not see these details").
- Approval workflow (Premier/Enterprise feature; optional): approval groups in succession — "One person from each group must approve the offer before it can be sent"; groups can be Admin, Recruiter, Hiring Manager (job-assigned), or a named person; "Group 1 must approve before Group 2 is notified, and so on."
- Sender auto-approval rule: "If the sender of an offer qualifies as an approver in any approval group, then those groups will approve the offer automatically."
- Approver experience: notification (inbox + email) with full offer details ("including things like salary, vacation time, etc."), approve (checkmark) or reject (X); "If a user rejects the offer, they will be asked to note a reason, and the person who initially set up the offer will be notified. Any necessary updates should be made, and the offer can be set up again."
- Approval trail on the record: "The entire approval process is recorded on the candidate's profile so the team can see which stakeholders need to provide their approval or why a hiring manager rejected the offer details." Approvers marked with green checkmarks in offer details.
- Company signatory: an internal signer signs the offer "before it's sent to the candidate" ([company_signature] variable required in the document).
- Candidate loop: email with link; candidate e-signs in Dropbox Sign (vendor-specific integration); candidates "can only fill in the [candidate_signature] variable"; after signature → status "Offer accepted"; signed PDF emailed to candidate and downloadable from Offer/Files tabs. Declining: three-dots decline in the signing surface → reason "added to their Timeline" → status "Offer declined."
- Expiration: offers carry an Offer Expiration Date; "the candidate can no longer sign the document after the Offer Expiration Date passes. If they need more time, you'll need to send another offer." (Vendor FAQ pins expiry to end-of-day in the creator's timezone — product-specific detail, kept out of the canonical document.)
- Cancel/withdraw: available across states — pending approval, pending candidate answer, and even "Accepted by the candidate"; canceling updates status to "Offer canceled," notifies followers, and — with Hiring Plan — "canceling an offer associated with a requisition will reopen the reserved or filled requisition." If pending candidate signature, the candidate is informed by email; if already accepted, not notified.
- Revise/resend: "If you made an error in the unsigned offer or if the offer expired, you can send a revised offer document"; recommended to cancel the old one first; "the previous offer document will become inactive and overwritten by the new one."
- Record/archival: Offer tab on the candidate profile shows status, offer details, unsigned PDF link, per-document links; signed copy archived.
- Reporting side effect: offers "feed into budget reporting."

### Breezy HR

Evidence tier: A (official help articles).

Key observations:

- Offer = template + email + document + optional approval flow: "The offer template includes an email message and an attached offer document"; templates created in Recruiting Preferences as eDocuments with Document Type "Offer."
- Variable/merge model: document contains "[[variable]]" placeholders; [[company_name]], [[position_title]], [[candidate_name]], [[sender_name]] auto-detected; custom variables ([[salary]], [[start_date]], [[work_location]], etc.) "fill them in when you generate an offer."
- Approval machinery optional and template-bound: "With optional offer approvals, you can require approval from one or more people before sending an offer"; two shapes — "approval from any Admin" (any one of them can approve) or an ordered approval chain ("Approvals will be requested in this order"); each offer template picks its approval flow.
- Offer creation from the candidate profile: Send Offer → choose template → review signature document → "Review and add offer details, then click Generate" → extra signers → review email → if approval required, "Request Approval" with optional message/attachment for approvers.
- Approval tracking as per-approver state: status of the offer approval viewable; per-approver status list; cancel or resend the approval request.
- Post-approval send: "Once approved, the offer will be sent to the candidate, the offer status will be updated to Sent. Waiting For Response," and the offer email appears in conversation history.
- Candidate loop: email with link → digital sign and return; signing completion can auto-move the candidate to a chosen pipeline stage ("Move on completion").
- Outcome and archival: notification on signature; status "Accepted"; signed offer PDF viewable/downloadable from the profile's Documents section.
- Expiration: templates can enable expiration ("the number of days the offer will be available for signing"); product default 7 days (vendor-specific; not canonical). Offers already sent expire at the original setting.
- Plan/permission gating: Offers/Offer Approvals on Business and Pro plans; Admin creates templates and approval flows; Hiring Manager or Admin sends and approves.
- Explicit separation from generic e-signature: Electronic Documents page splits "eSignatures" (general signature requests: NDAs, contracts) from "Offers" (offer letter machinery) — the market distinguishes the offer document type from generic signing even at the SMB tier.

### SmartRecruiters (Tier-2, marketing-level only)

Evidence tier: B/C — vendor names an "Offer Management" module under the Hire pillar of its platform nav (homepage fetched); the module's product page was unreachable (403) and the help center is customer-gated, so operational structure is NOT evidenced from this vendor and is not relied on for canonical claims. Its value here is market-naming evidence: "Offer Management" is a vendor-articulated module name in the enterprise ATS segment, consistent with the Type being predominantly a suite module.

## Cross-product Comparison

| Dimension | Greenhouse | Workable | Breezy | Reading |
|---|---|---|---|---|
| Offer as record bound to candidate × position, with structured terms | yes — offer details on Offer stage, custom offer fields | yes — details form (salary, start date, manager), internal-only fields | yes — "Review and add offer details" at generation | L0 candidate: the offer of record |
| Candidate-facing extension + response recorded | yes — send doc (email/Docusign/Adobe), upload signed, mark hired | yes — email + e-sign, accepted/declined statuses | yes — email + e-sign, Sent→Accepted, stage move | L0 candidate: extend-and-respond loop |
| Approval gate | optional per job/org; sequential/non-sequential approvers; scoped by office/department | optional (Premier/Enterprise); sequential approval groups; sender auto-approval | optional per template; any-admin or ordered chain | Common mature structure — explicitly optional in all three |
| Document production | template + tokens (docx+pdf), external docs uploadable | template + variables, wizard | template (.docx) + [[variables]] | Common; production substrate varies |
| Delivery substrate | native email; DocuSign / Adobe Sign integrations | Dropbox Sign signing surface | built-in e-signature fields | Substrate varies; not definitional |
| Response/outcome states | offer resolved (report), mark hired | Offer accepted / Offer declined (reason on timeline) / Offer canceled | Sent. Waiting For Response / Accepted; expiration | Canonical conceptual states: awaiting → accepted / declined / withdrawn / expired |
| Revision loop | new offer version, re-triggers approval | resend — new offer overwrites, old inactive | (not directly evidenced) | Common: supersede + re-gate |
| Withdrawal/cancel | (not directly evidenced) | cancel incl. post-acceptance; requisition reopens | cancel approval request; cancel offer from Documents | Common exception handling |
| Expiration | (not directly evidenced) | Offer Expiration Date blocks signing | configurable expiration window | Common variant, timing product-specific |
| Requisition/budget linkage | job-scoped approvals | requisition selection before offer; budget reporting feed; requisition reopen on cancel | (not evidenced) | Common in requisition-driven products; suite-dependent |
| Permissions around offers | Site/Job Admin split; salary-info permission | role-based ("Hiring Managers and above"); access-level comparison doc | Admin vs Hiring Manager split; plan gating | Common: visibility (esp. comp) and action rights are governed |
| Bulk/high-volume | bulk offer creation | (not evidenced) | (not evidenced) | Optional/high-volume variant |
| Analytics | Offer details report (status, sent/resolved dates, approvers) | budget reporting feed | (not evidenced) | Common: offer funnel/status reporting |

## Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

Two jointly-held structures. Remove either and the Type stops being recognizable:

1. **The offer of record** — a persistent, individually identified employment offer binding a specific candidate to a specific position, carrying its proposed terms (role, compensation, start, location/conditions as configured) and a lifecycle state. The offer accumulates its documents and history.
   - Remove → a merge/e-sign utility or an approval log; nothing "offer" remains.
2. **The extend-and-respond loop** — the approved offer is extended to the candidate as a candidate-facing offer document, and the candidate's response (accept/sign, decline, or non-response) is recorded back as the offer's outcome, driving the hire forward or closing the offer.
   - Remove → an internal requisition-approval workflow (no candidate), or a document generator (no tracked outcome).

Jointly-held is load-bearing:
- 1 alone = offer log/spreadsheet
- 2 without 1 = an e-sign/send workflow with no standing offer object
- 1+2 without governance depth = the thin end of the market (letter generator + tracker) — still in-type but below the mature pole

Deliberately NOT in L0 (tested per the historical/market-sample check):

- **Internal approval gate** — in all three deep samples the approval flow is *optional configuration* (Greenhouse: jobs can have no approval process, documented as a first-class flow; Workable: Premier/Enterprise feature; Breezy: "optional offer approvals"). It is the most emphasized common governance layer, but a product that only creates/extends/tracks offers is still clearly this Type. → L1. (Paper-era check: the typed letter + mailed response loop satisfies L0 with sign-off as practice, not machinery.)
- **E-signature / specific delivery channel** — Greenhouse supports email + manual upload of signed docs; delivery is substrate. → L1 implementation.
- **Templates/variables, offer versions, expiration windows, bulk offers, requisition/budget integration, offer reports** — common or variant capabilities, not defining. → L1/L2.
- **Comp-band enforcement / comp benchmarks** — not evidenced in the sample as enforcement inside offer creation; comp data appears as fields, not as a governed structure. → L2 (and a Compensation Management boundary).

### L1 — Common Mature Structure

- offer document production from templates with variables/tokens (docx/pdf), token-error handling
- internal approval machinery when used: approver roles/groups, sequential or parallel chains, per-approver status, notifications, approve/reject with reason, approval trail on the record, revision re-triggering approval
- response/outcome statuses: awaiting response → accepted / declined (reason recorded) / withdrawn (cancel, incl. post-acceptance at one product) / expired
- archival of signed offer documents on the candidate record
- permission separation: who can view offer details (esp. salary), create, send, approve, cancel
- offer reporting: status, created/sent/resolved dates, approvers
- handoff at acceptance: mark hired / auto-move stage (→ onboarding)

### L2 — Variant / Optional Structure

- approval gating by org attributes (office/department), comp-threshold-driven routing (implied by scoped approvals; not directly evidenced as thresholds — unverified)
- requisition linkage and budget reporting feed; requisition reopen on withdrawal
- expiration windows (timing product-specific), resend/overwrite semantics
- bulk offer creation (high-volume hiring)
- company signatory signing before send
- multi-language offer documents (one product's language-kit doc mentions offer letters)
- verbal-offer-first workflows (ATS pipeline convention in the market; not directly evidenced in fetched pages — unverified, excluded from canonical doc)

### L3 — Vendor-specific (research notes only)

- Greenhouse: "Send with Greenhouse" dialog, Refresh icon versioning, offer email templates with CC, "Offer stage" interview-plan framing, Core/Plus/Pro tier language, specific salary-comma parsing quirk
- Workable: pen-tip/stamp icons, three-step wizard, "An offer from [company] for [job]" fixed subject line, Dropbox Sign integration, expiry at 23:59 creator timezone, green-checkmark approver marks, plan names Premier/Enterprise
- Breezy: default 7-day expiration, max 100 approval flows, max 300 eDocument templates, [[double-bracket]] variable syntax, font whitelist, "Move on completion" stage picker, Business/Pro plan gating
- SmartRecruiters: "Offer Management" module branding under HIRE; Winston AI context (marketing)

## Vendor-specific Findings

See L3 above. None promoted to the canonical document.

## Rejected Findings

- "Offer Management = approval workflow software" — rejected: approvals are optional configuration in every deep sample; without the offer record + candidate loop, approval machinery alone is a different Type (generic approval engine).
- "Offer Management = e-signature for HR" — rejected: the market itself splits generic e-signature requests from offer documents (Workable "offer type" vs "simple type"; Breezy eDocuments vs Offers); signing is substrate.
- "Approval thresholds against comp bands are definitional" — rejected: not directly evidenced in fetched pages; comp-band enforcement belongs to Compensation Management territory unless evidenced.
- "Offers always live in an ATS pipeline" — rejected as a definitional claim (it is the dominant packaging, not the definition); the offer object and loop can exist in suite or thin-tool form.
- "Offer ≈ job ad" — rejected as a meaning collision: some recruiting tools use "offer" for the vacancy advertisement itself (flagged from prior knowledge of the Recruitee/Teamtailor naming convention; not directly evidenced in fetched pages — unverified caution, excluded from canonical doc).

## Boundary Findings

- **vs Applicant Tracking System / ATS**: the ATS owns the candidate pipeline from sourcing through stages; offer management owns the offer artifact's lifecycle at the Offer stage. Remove the pipeline (sourcing, screening, interview stages) and keep the offer lifecycle → still offer management. Remove the offer record/loop and keep the pipeline → still an ATS. In the sampled market, offer management ships inside ATSs as a stage/section — packaging, not identity.
- **vs Employee Onboarding Platform**: onboarding starts at acceptance (new hire preparing/starting); offer management ends at acceptance (mark hired, stage move, document handoff). The seam is the accepted offer.
- **vs Compensation Management Platform**: comp management governs org-wide compensation structure (bands, cycles, budgets, benchmarks); offer management consumes comp-relevant fields for one hire's offer. A salary field in an offer form is not comp management.
- **vs Proposal Management (sales) / Sales Document Automation**: structural analog (internal approval → external document → acceptance), but different domain objects (CRM opportunity vs candidate/position), different terms (commercial vs employment), different downstream (contract/revenue vs hire/onboarding).
- **vs Contract Lifecycle Management (legal)**: CLM is generic contract machinery (clauses, repositories, legal review); the offer letter is an employment-specific pre-hire artifact produced and consumed inside the hiring loop. Employment contracts may follow acceptance — that path belongs to onboarding/HR document flows.
- **vs Approval Workflow Platform**: generic approval engines route arbitrary requests; offer approval is a hiring-specific instantiation whose subject is the offer's terms and whose outcome gates an external communication.
- **vs e-signature products**: substrate capability. Distinguished above.
- **Homonym (taxonomy note)**: "offer management" in marketing/retail means managing promotional offers/discounts — a different domain with no shared objects. The DIRECTORY leaf (§09) is the employment sense. No employment-vs-promotional conflict exists inside §09, but the name is collision-prone; recorded for Boundary Issues.

## Uncertainties

- Enterprise HCM offer mechanics (Workday, SAP SuccessFactors, Oracle, iCIMS) were not directly observed (gated/JS-rendered docs). Claims about the enterprise pole are held general: suite modules exist (SmartRecruiters module naming is evidenced; the suites' internal structure is not).
- Whether comp-threshold/band enforcement inside offer approvals is common in the enterprise pole: unverified; excluded from canonical claims.
- Verbal-offer/verbal-acceptance tracking: widely believed ATS convention, not directly evidenced in fetched pages; excluded.
- Post-acceptance rescission (offer withdrawal after acceptance) evidenced at one product only (Workable cancel across states incl. accepted) → kept as a qualified "some products" statement.
- Standalone offer-only products (not embedded in an ATS): none surfaced in the reachable sample; the thin end realized as offer-document features inside lighter tools. Held as an open market-shape uncertainty rather than an assertion that none exist.

## Final Synthesis

An Offer Management Platform (HR sense) is the system of record for employment offers at the end of the hiring funnel. Its defining core is two jointly-held structures: (1) the offer of record — a persistent, identified binding of a specific candidate to a specific position with proposed terms and a lifecycle state, accumulating its documents and history; and (2) the extend-and-respond loop — the offer is extended to the candidate as a candidate-facing document, and the candidate's response is recorded back as the offer's outcome (accepted → hire handoff; declined/withdrawn/expired → close). Around this core, mature products add the governance layer (optional-but-ubiquitous internal approval gates with approver roles, chains, per-approver status, reject-with-reason, re-approval on revision), template-driven document production, permission separation (especially salary visibility), offer reporting, and requisition/budget linkage. The market predominantly packages this Type as a stage/section inside ATSs and as a named module in enterprise suites, with the same structure visible from SMB to enterprise; paper-era practice (typed letter, internal sign-off, mailed response) satisfies the core without any of the modern machinery. E-signature and email are replaceable substrate; the offer object and its loop are the Type.
