# Research Notes — Due Diligence Platform

## Research Goal

Understand what a "Due Diligence Platform" actually is as an Application Type: what objects exist inside it, who uses it, how the diligence work flows through it, and where its boundaries sit against the heavily adjacent Virtual Data Room, deal-management, and third-party-risk Types. Special obligation inherited from prior passes: the virtual-data-room pass (2026-09-08) requested a joint review, asking this pass to confirm whether a workflow-centered pole exists as a distinct Type or whether the directory leaf collapses into VDR territory.

## Initial Boundary

- Directory position: §11 Legal, Risk, Compliance & Governance, immediately before Virtual Data Room.
- Hypothesis at start: the market phrase "due diligence software/platform" is dominated by M&A transaction diligence; the center is likely the diligence *workflow* (request lists, tracking, review, findings), not the document repository (VDR) and not the deal pipeline (deal management).
- "Due diligence" is a heavily reused word across the taxonomy: TPRM embeds a due-diligence assessment leg; KYC/KYB centers a due-diligence case file; deal-management-for-PE-VC has due diligence as a pipeline stage; AML ingests customer due-diligence context; environmental-site-assessment is a property-transaction diligence execution. This pass must carve out what is left as this leaf's own center.

## Research Questions

1. What are the core objects of a diligence platform? (exercise/project, workstreams, request list, request, response, Q&A, findings, report)
2. What is the lifecycle of a diligence request, and is the status vocabulary standardized or product-specific?
3. What is the relationship to the data room — host, link, or sync? Is the repository definitional?
4. Who are the parties (inquiring side, responding side, advisors) and how do permissions work across them?
5. Where do findings/issues go and what do they feed (IC memo, closing conditions, price adjustments, integration)?
6. Is the Type M&A-specific, or does the same machinery appear against other subjects (vendor risk, real estate, fundraising)?
7. Does the workflow-centered pole exist standalone, or only bundled with VDR/pipeline suites?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / pole | Tier | Evidence |
|---|---|---|---|
| DealRoom | M&A lifecycle suite with diligence as a named module; explicitly positions against "traditional VDRs" | mid-market M&A teams | Tier-1 product page + FAQ (fetched) |
| Midaxo | Enterprise "M&A Intelligence Platform"; diligence as one phase of a connected lifecycle; publishes its own category glossary | enterprise corporate development | Tier-1 product page + FAQ (fetched) |
| InvestmentBank.com Diligence Tracker | Thin workflow module; links to a separate data room index instead of hosting one | banker/advisor workflow users | Tier-1 product page + FAQ (fetched) |
| Dillien | VDR-centered straddler: "next-generation data room" with the diligence workflow embedded in the room | Nordic market; law firms, brokers, advisors | Tier-1 product page + FAQ (fetched) |
| DD Navigator | AI-native analysis workbench; "No VDR required"; findings/IC-memo production center | PE, advisors, sell-side/VDD, GRC | Tier-1 product page (fetched) |

Additional snapshot evidence (search-result captures, official pages not directly fetchable — degraded to existence-level claims):

- go-diligence.com — standalone PE buy-side DD suite; request tracker with Excel/CSV import, AI auto-matching of documents to open requests, completion dashboard (Satisfied/Partial/Open), native two-way integrations to external VDRs, red-flag detection, IC memo generation. Site is a JS app; content known only via search snapshot.
- Vetting Vault — "request-first intake"; "Your Request List IS Your Data Room"; tasks/files/conversations in one workspace.
- DealTech — data request lists, automatic request-to-response mapping, publish documents to an integrated VDR, VDR-only counterparty access.
- Devaland — AI diligence layer; living model of what the data room should contain generating the next request list automatically.

## Sources

Fetched 2026-09-10 (Tier-1 unless noted):

- DealRoom — https://dealroom.net/product/diligence (also /product/due-diligence-software, /ma-software, /diligenceai via search snapshot)
- Midaxo — https://www.midaxo.com/platform/m-a-due-diligence (also /platform/due-diligence/run-diligence via search snapshot)
- InvestmentBank.com — https://investmentbank.com/transaction-desk/diligence-tracker
- Dillien — https://dillien.com/
- DD Navigator — https://ddnavigator.com/
- go-diligence — https://go-diligence.com/features (search snapshot only; site JS-walled — Tier-2/3, degraded)
- Vetting Vault — https://vettingvault.com/ (search snapshot)
- DealTech — https://www.dealtech.ai/ (search snapshot)
- Devaland — https://devaland.com/diligence-automation (search snapshot)

Prior-pass context: research/virtual-data-room.md §Boundary Findings (joint-review request); research/transaction-legal-management.md; research/third-party-risk-management.md; research/deal-management-for-private-equity-vc.md (STATUS.md entries).

## Product Observations

### DealRoom (Tier-1, A-layer)

- Positions itself as diligence management distinct from VDRs: FAQ states "traditional virtual data rooms (VDRs) primarily focus on document storage and sharing, M&A due diligence software goes beyond by offering comprehensive tools specifically designed to manage the entire due diligence process. Unlike VDRs, which may lack features for request management, collaboration, and workflow automation…"
- Core objects: diligence requests ("create, assign, and track diligence requests"), files linked to requests ("automatically connecting files to relevant diligence requests"), reviewers assigned per request, public and private comment threads, granular permissions, notifications, progress tracking for team and sellers.
- Findings: "Unify deal findings in one tool — effectively track, manage and connect findings directly to the diligence data"; "Generate reports on identified risks within each diligence request."
- Repository: built-in virtual data room as one capability among several ("Use built-in virtual data room… Learn more about virtual data room" — a separate product page).
- Templates: 10+ pre-made playbooks; Excel request-list import ("Quickly import existing diligence request lists from Excel").
- Bundle context: Pipeline and Integration are sibling modules of the same M&A platform; diligence is one module.
- AI-era: document analysis, key-term extraction, prompt templates; "AI Suggested Findings"; checklist builder generating a tailored request list.
- Vendor claims (L3, not promoted): "cut 25+ manual hours", "reduce due diligence time by 50%", "Diligence Risk Tracker with 40+ red flags".

### Midaxo (Tier-1, A-layer)

- Publishes its own category definition: "M&A due diligence software (also called a due diligence platform, intelligent VDR, or M&A diligence platform) is purpose-built software that helps deal teams run structured diligence across legal, financial, operational, and technical workstreams. It centralizes document review, request management, risk tracking, and closing coordination in one secure workspace."
- "A diligence platform combines a virtual data room for documents, reusable diligence checklists and playbooks, task and owner assignment, a risk and issue register, and real-time reporting."
- Repository seam, stated from the VDR side: "A traditional VDR is a secure document repository, it holds, organizes, and controls access to deal documents." Pain-point framing: "The VDR stores files but tracks nothing else."
- Findings machinery: RAID register (risks, assumptions, issues, dependencies) — "captured in a structured register, assessed for severity, assigned an owner, and linked to mitigation steps"; findings "travel into integration planning automatically instead of being re-keyed."
- Workstreams: "Coordinate legal, finance, HR, IT, and operations workstreams in one system without forcing everyone into a generic project tool."
- Closing: "Closing checklists build from live diligence data, not manual re-entry."
- Audit: "Every document access, task, and approval timestamped."
- Parallelism: multiple diligence processes run in parallel with dashboards.
- Q&A handled "in a secure VDR, with every finding tied to an owner."

### InvestmentBank.com Diligence Tracker (Tier-1, A-layer)

- The cleanest thin pole: a workflow module that does NOT host the data room. "Documents in the Data Room Index can be linked directly to diligence requests in the tracker, creating a connection between the organized data room and the specific questions being asked about it."
- Repository separability, stated explicitly: "Diligence requests are questions about the virtual data room. Nearly every incoming request is either 'produce a document that is not in the VDR' or 'explain a document that is,' which means the tracker and the data room index are two views of one state. Resolving requests by pointing at room files — rather than by emailing attachments — keeps the VDR authoritative and leaves an access record showing exactly what was produced to whom."
- Request lifecycle (7 stages): Receive Request → Categorize → Assign Owner → Link Documents → Respond → Review & Flag → Close or Escalate.
- Status model: "Not Started, In Progress, Submitted, Under Review, Closed, or Flagged."
- Risk flags: "Risk flagging is intentionally integrated into the request workflow rather than a separate tool… the risk register is built automatically from the diligence process rather than maintained as a separate document." Categories: financial, legal, regulatory, operational, environmental, HR. Severity: Informational, Watch, Elevated, Critical. Each flag: description, owner, target-resolution date, linked source document or Q&A record.
- Purpose of findings: "identify, log, and prioritize issues uncovered during diligence — before they surface as closing conditions or price adjustments."
- Q&A: "Log questions from buyers or investors, track response status, and maintain a complete Q&A record linked to the relevant request."
- Multi-counterparty: requests tagged by source party (buyer, investor, lender, legal counsel) — separate request queues per counterparty in one transaction.
- Explicit non-advisory posture: workflow software only; findings require professional review.

### Dillien (Tier-1, A-layer) — VDR-centered straddler

- Self-label: "The next-generation data room and due diligence tool for M&A, real estate transactions, fundraising, and beyond."
- Philosophy: "the data room — where documents stay and collaboration takes place — must be the starting point." Anti-VDR framing still present: "Traditional virtual data rooms have largely served as static storage spaces, offering little support for the process."
- Workflow embedded in the room: "the request list is fully integrated into the platform and directly tied to the file structure… Resolve requests by adding text answers and files or marking applicability directly in the platform."
- Q&A: "questions, answers, and supporting files appear both in request-specific threads and on the Queries page."
- Project management: assign responsibilities/tasks, deadlines, progress tracking, automatic reminders.
- Findings + report: "Review documents, flag issues, note concerns…"; "The built-in report generator then compiles findings and recommendations into a clean, structured due diligence report."
- Export: "complete packages including documents, requests, Q&A, logs, and findings."
- Subject breadth: M&A, real estate, fundraising; also used for "reporting, board work, compliance reviews, litigation."

### DD Navigator (Tier-1, A-layer) — AI-native analysis pole

- "No VDR required · Works alongside one when you have it" — the repository is fully externalized (direct upload or VDR export).
- Objects: DRL (data request list) mapping — "Documents are classified, mapped to the DRL, analyzed across workstreams, and checked for cross-document inconsistencies"; "findings mapped to the data request list, each cited to its source."
- Findings output: "Cited findings, risk heat map, tracked issues, and an IC-memo first draft ready for human review and sign-off."
- Issues list: "surfaced from the target's own documents, tagged by workstream, sorted by priority."
- Sell-side pole: VDD reports, exit-readiness command center, weakness scorecard, objection register.
- Governance: sentence-level provenance, authorship attestation appendix, multi-party sign-off, audit trail.
- Subject extension: "GRC & Vendor Risk — Vendor risk assessments run like M&A diligence. A dedicated Vendor Risk pack with control-gap findings and an annual recertification workflow."

### go-diligence (search snapshot, B-layer at existence level only)

- Standalone PE buy-side DD suite: request tracker (Excel/CSV import of 200–400+ line-item lists — vendor figure, unverified), AI auto-matching of uploaded documents to open requests with confidence scores, completion dashboard (Satisfied/Partial/Open), red-flag detection, QoE first pass, IC memo generation.
- Repository posture: does NOT host the primary room — "Native VDR Integrations: OAuth-native, two-way connections to the four VDRs your deal team actually uses… no copy-paste, no double-uploads." (existence-level; mechanics unverified)

## Cross-product Comparison

| Structure | DealRoom | Midaxo | InvestmentBank | Dillien | DD Navigator | go-diligence (snap) | Verdict |
|---|---|---|---|---|---|---|---|
| Diligence exercise/project bound to a subject | ✓ (deal) | ✓ (deal) | ✓ (transaction) | ✓ (data room per deal) | ✓ (deal/assessment) | ✓ | Core |
| Workstream/category organization | ✓ (implied) | ✓ explicit (legal/finance/HR/IT/ops) | ✓ (financial/legal/operational/HR/IP/regulatory) | ✓ (parallel workstreams) | ✓ (workstream-tagged) | ✓ | Core |
| Request list as unit of work | ✓ | ✓ | ✓ | ✓ | ✓ (DRL) | ✓ | Core |
| Request status lifecycle | ✓ (track) | ✓ (tasks/owners) | ✓ explicit 7-stage model | ✓ (resolve/mark applicability) | ✓ (coverage mapping) | ✓ (Satisfied/Partial/Open) | Core; labels product-specific |
| Response bound to the specific request | ✓ (link files to requests) | ✓ | ✓ (link from room index) | ✓ (tied to file structure) | ✓ (findings cited to source) | ✓ (auto-matching) | Core |
| Two-party exchange (comments/Q&A) | ✓ (public/private threads) | ✓ (Q&A in VDR) | ✓ (Q&A log) | ✓ (threads + Queries page) | ✓ (follow-ups) | ✓ | Common mature mechanism of the loop |
| Findings/issues/risks register | ✓ | ✓ (RAID) | ✓ (risk flags) | ✓ (flag issues) | ✓ (issues + heat map) | ✓ (red flags) | Core |
| Findings feed a decision artifact | ✓ (reports per request) | ✓ (integration, closing checklists) | ✓ (closing conditions, price adjustments) | ✓ (DD report generator) | ✓ (IC memo, VDD report) | ✓ (IC memo) | Core |
| Built-in VDR | ✓ | ✓ | ✗ (links to separate index) | ✓ (is the room) | ✗ ("No VDR required") | ✗ (two-way sync) | NOT definitional — variant axis |
| Templates/playbooks | ✓ | ✓ | — (request-list resource) | ✓ (best-practice templates) | ✓ (preconfigured agents) | ✓ | Common |
| Excel/CSV import of existing lists | ✓ | — | — | ✓ (Excel/Word/PDF) | ✓ (VDR export) | ✓ | Common |
| Dashboards/progress reporting | ✓ | ✓ | ✓ (14/22 complete view) | ✓ (real-time dashboard) | ✓ (deal dashboard) | ✓ | Common |
| Audit trail | ✓ (FAQ: audit trails) | ✓ (timestamped access/tasks/approvals) | ✓ (access record) | ✓ (activity logged) | ✓ | ✓ (audit trails) | Common |
| AI assistance | ✓ | ✓ | ✓ (adjacent AI tools) | — (legal AI integrations noted) | ✓ (center of product) | ✓ | Era-typical, NOT definitional |
| Deal pipeline / integration modules | ✓ (siblings) | ✓ (same platform) | ✗ | ✗ | ✗ | ✗ | Bundle, NOT core |

## Canonical Model (four abstraction levels)

### L0 — Defining Invariant

Four jointly-held structures:

1. **The diligence exercise of record** — a bounded, identified inquiry into a specific subject (a target company, asset, investment, or counterparty) run by an inquiring party toward a decision; organized into workstreams/categories with owners. Remove → generic project/task management.
2. **The information request list as the unit of work** — structured items, each asking the subject/responding party for a document or an answer; categorized, prioritized, assigned, tracked to completion. Remove → a document repository or a static checklist nobody works.
3. **The tracked request→response→review loop** — each request carries a lifecycle status; the response (document and/or answer) is bound to the specific request; the requesting and responding parties exchange through the platform; gaps and partial responses remain visible. Remove → one-way file sharing.
4. **Findings/issues accumulated against the exercise** — issues, risks, and red flags surfaced during review, logged with severity and owner, linked to the request or document that raised them, feeding the diligence output (report, IC memo, closing conditions, price adjustments). Remove → a request tracker with no assessment output.

Jointly-held is load-bearing: 1 alone = project management; 2 without 1 = a spreadsheet; 3 without 2 = file sharing; 4 without 1–3 = an issues list; 1+2 without 3 = a checklist nobody feeds; 2+3 without 1 = ad-hoc document chasing; 1+4 without 2+3 = a memo without inquiry machinery.

### L1 — Common Mature Structure

- Q&A threading between parties (request-specific threads plus a consolidated queries view)
- Templates/playbooks/request-list libraries per deal type; import of existing Excel/Word/PDF lists
- Progress dashboards, status reporting, exportable status updates
- Granular permissions and cross-party access control (buyer/seller/advisors/counterparties)
- Audit trail (document access, task, approval timestamps)
- Data-room integration in some posture (built-in room, link to a room index, or two-way sync)
- Reviewer assignment per request; notifications and reminders
- Closing checklists built from live diligence state
- AI assistance: document classification, auto-matching documents to requests, key-term extraction, red-flag ranking, summary and memo drafting

### L2 — Variant / Optional Structure

- Repository posture: built-in VDR (DealRoom, Midaxo, Dillien) vs link-to-external-room (InvestmentBank.com) vs two-way sync with external VDRs (go-diligence) vs no room at all (DD Navigator)
- Packaging: standalone diligence workbench (DD Navigator, go-diligence) vs module of an M&A lifecycle suite (DealRoom, Midaxo) vs data-room-first product with embedded workflow (Dillien) vs workflow module of a transaction platform (InvestmentBank.com)
- Side: buy-side operation vs sell-side operation (VDD reports, exit readiness, objection registers)
- Subject context: M&A/PE (dominant), real estate transactions, fundraising, vendor-risk assessments — machinery identical, subject varies
- AI depth: none → matching → analysis → memo drafting
- Geography: Nordic pole (Dillien), US mid-market, etc.

### L3 — Vendor-specific (research notes only)

- DealRoom: "Buyer-Led M&A" framework branding; Diligence Risk Tracker with "40+ red flags"; time/cost saving claims (25+ hours, 50%, 80%, 60%); 4-level permissions claim.
- Midaxo: "RAID register" naming; "M&A Intelligence Platform" branding; IDC MarketScape Leader citation; "500+ M&A teams" claim.
- InvestmentBank.com: exact status vocabulary (Not Started/In Progress/Submitted/Under Review/Closed/Flagged); severity vocabulary (Informational/Watch/Elevated/Critical); "7 request status stages" framing.
- DD Navigator: sentence-level provenance overlay; Authorship Attestation Appendix; per-deal pricing ($2,500–$7,500) and VDR cost comparisons ($25K–$190K); "PE Top 20" style analysis packs (go-diligence).
- Dillien: fixed monthly price per data room; Norwegian market anchoring.
- go-diligence: 200–400+ line-item request lists; "11 standard folders"; one-click purge.

## Vendor-specific Findings

See L3 above. None promoted to the canonical core. The most tempting over-fits, rejected:

- **Built-in VDR is NOT definitional** — three of six sampled products run diligence without hosting the room (link, sync, or none). This is the decisive anti-overfit finding and directly answers the VDR pass's question.
- **AI auto-matching/analysis is NOT definitional** — the spreadsheet-era practice (Excel tracker + email + VDR) that every sampled product markets against satisfies the same core.
- **RAID vocabulary is NOT definitional** — InvestmentBank uses "risk flags", Dillien "flag issues", DD Navigator "issues"; the register concept is shared, the labels are not.

## Boundary Findings

1. **vs Virtual Data Room — JOINT REVIEW DISCHARGED, keep-both RATIFIED.** The VDR pass's provisional seam is confirmed from this side with direct evidence in both directions: (a) the workflow pole exists without hosting the repository — InvestmentBank.com's tracker links to a separate data room index and states "the tracker and the data room index are two views of one state… keeps the VDR authoritative"; DD Navigator states "No VDR required"; go-diligence two-way syncs external VDRs; (b) the repository pole exists without the workflow — all sampled workflow products characterize traditional VDRs as "static storage" that "stores files but tracks nothing else." The seam: **VDR = disclosure repository of record (corpus + party access + disclosure record); Due Diligence Platform = inquiry workflow of record (requests → responses → review → findings).** Market straddling is real and packaged (DealRoom and Midaxo bundle both; Dillien embeds the workflow in the room; HighQ ships both per the TLM pass) — bundling does not dissolve the seam.

2. **vs Deal Management for Private Equity / VC — keep-both.** That Type is the firm's front-office deal-flow CRM (pipeline stages, counterparty records, deal history); "due diligence" appears there as a pipeline stage. This Type is the execution workbench for the diligence exercise itself. Suites bundle both (DealRoom Pipeline+Diligence; Midaxo pipeline+diligence+integration) — packaging, not identity.

3. **vs Third-party Risk Management — keep-both.** TPRM is the standing relationship program (inventory + per-relationship evaluation + governed decision loop across the relationship lifecycle). This Type is the bounded exercise toward a transaction decision. Convergence zone is real: DD Navigator sells a "Vendor Risk pack" that runs "like M&A diligence" with an annual recertification workflow — the exercise machinery is reusable for vendor assessments, but the standing third-party program remains TPRM's center. TPRM's own core includes a due-diligence assessment leg; that leg is the standing-program realization, not this Type.

4. **vs KYC/KYB Platform — distinct.** KYC/KYB centers the customer-onboarding compliance program (accumulated due-diligence case file, risk-based relationship decision, standing regulator-facing maintenance). Subject and regime differ: regulated customer relationships vs transaction subjects; the terminal artifact is a relationship decision under a compliance regime, not a deal decision.

5. **vs Transaction Legal Management — keep-both (consistent with that pass).** TLM centers whole-deal execution; diligence is one workstream inside it. HighQ ships both — module packaging.

6. **vs Investment Research Platform — distinct (that pass's recorded seam confirmed).** Public-domain issuer material vs deal-confidential document sets; research interrogation vs inquiry workflow.

7. **vs eDiscovery / Corporate Investigation / Environmental Site Assessment — adjacent, distinct.** eDiscovery: evidentiary review with legal hold/production machinery. Corporate investigation: internal wrongdoing cases. ESA: the closest "assessment" sibling (bounded engagement + evidence + report) but its subject is a property's environmental condition under practice standards, not a multi-workstream transaction inquiry. Contract analytics: analysis machinery over documents vs the deal process (that pass recorded the same seam).

8. **Open question (not resolved this pass):** the allocator→fund-manager DDQ exchange pole (questionnaire-based investment diligence) was not directly sampled. If a distinct questionnaire-exchange Type exists there, it is adjacent; recorded for future passes.

## Historical / Market-Sample Check

Paper-era M&A diligence satisfies all four L0 legs with zero software machinery: a numbered request list (typed or spreadsheet), responses assembled against a data-room index or mailed/faxed documents, a Q&A log, the legal team's issues list, and the final diligence report feeding the closing. The spreadsheet-era practice (Excel tracker + email + traditional VDR) — the exact "old way" every sampled product markets against — also satisfies the core. Therefore no modern implement (built-in VDR, AI matching, dashboards, provenance tooling) is definitional. Historical check **passed**.

## Uncertainties

- go-diligence evidence is search-snapshot only (JS-walled site); its external-VDR integration mechanics and dashboard states are held at existence level.
- Help-center-level operational documentation was not crawled (DealRoom's support center exists but was not fetched); no status vocabulary or permission scheme is claimed as industry-standard — documented status models are product-specific realizations of one conceptual lifecycle.
- The sell-side pole is under-sampled (only DD Navigator's sell-side/VDD surfaces).
- The DDQ/questionnaire-exchange pole (allocator diligence) remains unsampled — open question recorded above.
- Vendor figures (line-item counts, pricing, savings claims) are marketing figures, kept here and excluded from the final document.

## Final Synthesis

The Due Diligence Platform is the deal team's inquiry workbench: a bounded diligence exercise against a subject, organized into workstreams, run through an information request list whose items are tracked from issue through response and review to closure, with the responses bound to their requests, the parties exchanging through the platform, and the findings accumulated into the diligence output that feeds the transaction decision. The document repository is a separable companion (hosted, linked, synced, or absent); the deal pipeline is an upstream sibling; the standing third-party program is a different Type. The workflow-centered pole exists as a distinct Application Type — the directory leaf does not collapse into VDR territory.
