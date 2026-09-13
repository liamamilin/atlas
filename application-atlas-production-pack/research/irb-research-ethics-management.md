# Research Notes — IRB / Research Ethics Management

## Research Goal

Understand what an IRB / Research Ethics Management application really is as an Application Type: what objects exist inside it, who uses it, how a protocol moves from preparation through review to a determination and through its post-approval life, and where its boundary lies against neighboring Types (Research Compliance Management, IACUC platforms, CTMS, Research Administration, Peer Review).

## Initial Boundary

Hypothesis before research:

- Core use: manage the institutional ethics/regulatory review of human-subjects research — protocol preparation, submission, committee review, determination, and post-approval oversight.
- Users: researchers (PI/team), IRB/ethics office staff (analysts/administrators), committee members/reviewers, chairs, organizational approvers (department chairs), compliance leadership.
- Nearest neighbors: Research Compliance Management (broader, multi-board), Animal Research Ethics / IACUC Platform (same machinery, different subject), Research Administration Platform (funding side), CTMS (study operations side), Peer Review Platform (manuscripts, not protocols).
- Unknowns: how much committee/meeting machinery is definitional vs optional; whether UK/EU-style ethics systems (IRAS-based) fit the same model; how single-IRB/reliance changes the model.

## Research Questions

1. What is the unit of record — protocol, study, submission? How do they relate?
2. What submission types exist and why (initial, amendment, continuing review, reportable events, closure)?
3. How does the review workflow work — pre-review, reviewer assignment, exempt/expedited/full-board routes, convened meetings?
4. What determinations exist and how are they communicated (letters, statuses)?
5. What committee machinery exists (agenda, minutes, reviewer comments, decisions)?
6. What happens after approval (modifications, continuing review, adverse events, closure)?
7. What roles exist and what can each see/do?
8. What is vendor-specific vs common?

## Representative Products

Chosen for market representativeness, documentation availability, and different product philosophies/customer layers:

1. **Cayuse Human Ethics (formerly Cayuse IRB)** — commercial SaaS, part of a research-administration suite; higher-ed/healthcare/nonprofit. Strong public user guides (hosted by customer universities).
2. **IRBNet** (Research Dataware / WCG) — standalone web platform, multi-board (IRB/IACUC/IBC/COI), multi-institution; strong public user manual.
3. **RASCAL** (Columbia University, institution-built) — in-house research compliance administration system; shows the same structure without a commercial vendor.
4. **eProtocol** (Key Solutions) — standalone protocol-management system used by universities/health systems (Berkeley, Stanford, Wayne State, Allina Health).
5. **InfoEd Human Studies / IRB & Ethics** — module of a research-administration suite; vendor product page + customer job aids.

Also observed (secondary evidence): OneAegis (formerly IRBManager) at Iowa State and NIH NHLBI; iRIS (iMedRIS) at TTUHSC; RASS-IRB (Cornell, institution-built). UK IRAS-based commercial systems (e.g., rascal.ac.uk) could not be reached — see Sources limitation.

## Sources

- Cayuse Human Ethics product page: https://www.cayuse.com/compliance-management/human-ethics/ (fetched 2026-09-10)
- Cayuse IRB User Guide v1.9.2 (Evisions-era, hosted by Texas Tech University): https://www.depts.ttu.edu/research/responsible-research/irb/assets/pdf/Cayuse-IRB-User-Guide.pdf
- UC Merced Cayuse IRB Researcher Manual & Reviewer Manual: https://cayuse.ucmerced.edu/... , https://rci.ucmerced.edu/...
- William Paterson University Cayuse Human Ethics submission guide: https://ww3.wpunj.edu/osp/Cayuse-Page-Content/Cayuse-User-Guides-Folder/Cayuse%20for%20HE%20-%20Protocol%20Submissions.pdf
- IRBNet product site: https://www.irbnet.org/ (fetched 2026-09-10)
- IRBNet User Manual (Marshall University): https://www.marshall.edu/ori/files/IRBNet-user-manual-072020.pdf
- Columbia RASCAL: https://www.rascal.columbia.edu/help/irbfaq.html , https://www.cuit.columbia.edu/research-compliance , Columbia HRPO "Life Cycle of a Protocol" PDF
- Key Solutions eProtocol guides: Berkeley CPHS reviewer quick guide, Stanford eProtocol Managing Protocols, Wayne State FAQ, Allina Health IRB guide, NEOMED Viewer guide
- InfoEd product page: https://www.infoedglobal.com/products/research-compliance ; Boston College & Boise State InfoEd IRB job aids
- Iowa State OneAegis submission-and-review page: https://compliance.iastate.edu/research-ethics-compliance/irb/submission-and-review
- NIH NHLBI CDS-IRB IRBManager workflow diagram: https://www.nhlbi.nih.gov/sites/default/files/media/docs/CDS_IRB_Review_Process.pdf
- TTUHSC iRIS initial-application guide
- Cornell RASS-IRB guide: https://guide.rass.cornell.edu/institutional-review-board-for-human-participant-research

Research date: 2026-09-10.

**Source-access limitation**: rascal.ac.uk (UK IRAS-oriented vendor) returned transport errors twice and was abandoned. Cayuse's own support portal requires sign-in; evidence for Cayuse comes from vendor product pages plus customer-hosted official user guides (Tier 1-equivalent). Most evidence is US-centric; UK/EU ethics-review systems are under-sampled, so geography-specific claims are avoided.

## Product Observations

### Cayuse Human Ethics (Cayuse IRB) — evidence layer A (vendor page + official user guides)

- **Study as container, submission as unit of work**: a "Study" is created (title), and each review action is a "Submission" inside it — Initial, Modification, Renewal/Continuing Review, Reportable Events (incidents), Closure. All submissions for a study live in one folder-like record.
- **Smart forms**: configurable submission forms with skip logic/conditional branching; drag-and-drop form builder for admins; drafts revertible.
- **Roles**: PI, PC (principal contact), Researcher, Organizational Approver, IRB Analyst, IRB Admin, IRB Member/reviewer. Role-based dashboards; Tasks screen lists what each user must complete; completing a task advances the workflow.
- **Workflow**: complete submission → PI certification (all listed PIs must certify) → departmental/organizational approver chain → IRB analyst pre-review → reviewer(s) or committee. At any point the submission may be returned to the research team to answer comments; comments are threaded per question/section; resubmission requires addressing all comments and re-certification.
- **Determinations/decisions** (reviewer decision types observed): Approved; Requires Changes to the PI; Return to PI; Disapproved; No Engagement in Research; No Human Subjects Research; Not Expedited/Not Exempt (route change); Rely on External IRB; Noted (for incidents). Approval letters generated as formal correspondence, downloadable from the submission's Letters tab.
- **Study statuses** (11 observed in guide): Approved, Closed, Disapproved, plus in-progress states; dashboards show Approved / Expiring / Expired / pending tasks.
- **Meetings**: meeting management for convened review — agendas, minutes preparation, protocol statuses for the meeting.
- **Integrations**: CITI training-record transmission to verify researcher certification; Sponsored Projects (SP) record linking for congruence checks; single sign-on.
- **Continuing review**: automatic reminder notices for expiring approvals.
- Vendor marketing claims (percentages of time saved, "smart forms reduce prep 35%") treated as marketing, not evidence.

### IRBNet — evidence layer A (product site + user manual)

- **Registration & organization binding**: users register and are affiliated with an institution ("Researcher at Marshall University"); email is the official communication channel.
- **Package-based submission**: submissions are "packages" assembled from a Forms and Templates library defined by the institution; a Submission Checklist lists required forms. Submitting **locks** the package; revisions require a new revision package.
- **Submission types**: initial submission, modification/amendment, continuing review/annual update, protocol deviation, adverse event reporting, closure — matching the protocol lifecycle.
- **Multi-board, multi-institution**: one backbone supports IRB, IACUC, IBC, COI and other boards; supports institutions operating multiple IRBs across sites (Nemours DE/FL testimonial).
- **Committee machinery**: electronic submissions, form wizards, agendas, minutes; committee members complete reviews in the system before meetings.
- **Access control**: per-user access levels on a study ("grant each user only the minimum level of access necessary").
- **Notifications**: email notification on submission and on approval to everyone with full access.

### RASCAL (Columbia University) — evidence layer A (university docs)

- **Institution-built, multi-module compliance system**: protocols, appendices (e.g., Haz Mat module), COI disclosures, HIPAA forms, consent-form module, training certification tests, proposal tracking — research compliance administration beyond IRB alone.
- **Protocol lifecycle statuses** (documented): Creating → Submitted (2-step: personnel + department approvers approve, then PI submits) → HRPO pre-review (assigned staff reviewer; may be returned) → Logged in (accepted, assigned to a specific IRB) → Chair's queue → Distributed (to an IRB member) → Assigned to Meeting → decision; Returned possible at multiple points.
- **Ancillary reviews**: parallel reviews by other committees (cancer center PRMC, IBC/EH&S, radiation, etc.) triggered after IRB submission.
- **Not-human-subjects-research determinations** handled by HRPO staff.
- **Protocol history**: the system logs the submit–return–resubmit history by date — an explicit institutional memory function.
- **Meeting cadence**: IRB meets at least monthly; submission deadlines tied to meetings.

### eProtocol (Key Solutions) — evidence layer A (customer guides)

- **Protocol as record with form types**: New, Amendment, Continuing Review (common to all committees), plus IRB-specific forms (Serious Adverse Event, deviations, final report/closure, miscellaneous).
- **Panels & meeting dates**: every protocol is assigned to a Panel (full-board panels or expedited panels named after the analyst) and a Meeting Date; the Protocol Event column shows current status.
- **Analyst role**: IRB office analyst processes submissions, issues approval letters, handles returns ("Return Notes"); reviewers see action-required events on their home page.
- **Comments/stipulations**: IRB communicates stipulations through a Comments feature ("Comments Received (Cycle X)"); resubmission cycles tracked.
- **Personnel & sign-off**: key personnel listed on protocol; training status (CITI) displayed; all key personnel sign off; authorized signatory (chair/dean) approval chain before IRB office.
- **Clone protocol**: copy an existing protocol to a new IRB number.
- **One submission at a time**: only one pending action per protocol at a time (Wayne State FAQ).
- **Search/archive**: approved documents retrievable; protocol ID as reference key.

### InfoEd Human Studies / IRB & Ethics — evidence layer B (vendor page + customer job aids)

- **eForms with routing**: investigators create submissions and route electronically through signoffs or directly to the IRB office; mandatory questions/uploads; branching logic; institution-configurable forms; reusable templates.
- **Multi-committee linking**: protocols submitted to multiple committees can be linked; each protocol's status managed separately.
- **Committee & meeting management**: agenda generation, distribution of meeting minutes, notifications; reviewer comments captured electronically form the basis of minutes and correspondence.
- **Compliance workflow**: multiple reviews and levels of oversight from intake to full committee review; protocol tracing, conditional alerts, reporting, electronic letters.
- Customer job aids confirm: create protocol, respond to reviewer concerns, modifications, annual renewal, final report, copy protocol, assigned tasks.

### Secondary observations (OneAegis/IRBManager, iRIS, RASS) — evidence layer A per product, used for cross-checks

- OneAegis (Iowa State): application form configured for multiple submission types; reliance requests (external IRB oversight) as a submission type; exempt/expedited applications queued without deadlines while convened-board applications have meeting deadlines; modification and continuing-review submission types.
- NHLBI IRBManager workflow: submission → pre-review (office) → reviewer assignment (chair, by sensitivity/expertise) → member review with worksheets → monthly convened session → determination issued to researcher.
- iRIS (TTUHSC): sectioned submission wizard, signatory authority/chair/dean routing, IRB office prescreen with retraction of incomplete submissions, agenda placement notices, submission-status tracking.
- Cornell RASS: auto-determined review-type (exempt/expedited/full-board) from questionnaire answers, subject to change by the IRB; PI/faculty-advisor attestations; reviewer comments bound to specific form sections/fields; side-by-side version comparison on resubmission; protocol development/prescreening protocols as a distinct early-phase type.

## Cross-product Comparison

| Structure | Cayuse | IRBNet | RASCAL | eProtocol | InfoEd | Reading |
|---|---|---|---|---|---|---|
| Persistent protocol/study record accumulating submissions | ✔ (Study folder) | ✔ (study + packages) | ✔ (protocol + history log) | ✔ (protocol + form types) | ✔ (protocol record) | Core |
| Submission types: initial / amendment / continuing review / reportable event / closure | ✔ | ✔ | ✔ | ✔ | ✔ | Core |
| Configurable institution-defined forms | ✔ smart forms | ✔ own forms/library | ✔ (built for one institution) | ✔ | ✔ eForm tool | Core (the institution owns the form) |
| Routed workflow with organizational approvers before IRB office | ✔ (dept approver chain + PI certification) | ✔ (access + submit) | ✔ (personnel + dept approvers) | ✔ (signatory chain) | ✔ (signoffs) | Core-ish; depth varies |
| Staff pre-review / analyst role | ✔ | ✔ (office) | ✔ (HRPO) | ✔ (analyst) | ✔ (intake) | Core |
| Review routes: exempt / expedited(designated member) / convened full board | ✔ | ✔ | ✔ | ✔ (panels) | ✔ | Core |
| Committee meeting machinery (agenda, reviewer assignment, minutes, decisions) | ✔ | ✔ | ✔ | ✔ | ✔ | Core |
| Recorded determination + formal letter/correspondence | ✔ | ✔ | ✔ | ✔ | ✔ | Core |
| Post-approval oversight: modifications, continuing review + reminders, adverse events/deviations, closure | ✔ | ✔ | ✔ | ✔ | ✔ | Core |
| Comment threads bound to form sections; version comparison | ✔ | (revision packages) | (return + resubmit) | ✔ (stips) | ✔ | Common |
| Training verification (CITI) integration | ✔ | — | ✔ (cert tests) | ✔ (displayed) | — | Common (US-specific) |
| Ancillary/parallel committee reviews | — | (multi-board) | ✔ | ✔ (admin approvals) | ✔ (multi-committee linking) | Common |
| Multi-board (IRB/IACUC/IBC/COI) on one backbone | ✔ (suite) | ✔ | ✔ (modules) | ✔ | ✔ (suite) | Common packaging, not definitional |
| Multi-institution / external-IRB reliance | — | ✔ | — | — | — | Variant |
| Single sign-on, dashboards, reporting | ✔ | ✔ | ✔ | ✔ | ✔ | Common |
| Institution-built (no vendor) | — | — | ✔ | — | — | Deployment variant |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The smallest structure without which the system stops being an IRB/research-ethics management application:

1. **The protocol as unit of record** — a persistent, identified record of one research study subject to ethics review, carrying the research team (PI + personnel) and accumulating every submission, review, decision, and correspondence over the study's life. Remove → a grant tracker or document store.
2. **Submission-driven review workflow to a recorded determination** — structured submissions (at minimum initial review, amendment/modification, continuing review, and reportable-event reporting) routed through a configured path (staff pre-review → designated reviewer or convened committee) that ends in a recorded determination (approved / modifications required / returned / disapproved / not-human-subjects-research / reliance) issued as formal correspondence. Remove → generic e-form workflow or file share.
3. **The committee as reviewing actor** — the ethics board's review machinery: reviewer assignment, review materials, reviewer comments, convened-meeting handling (agenda/minutes), and decisions attributed to the board. Remove → single-approver sign-off tool.
4. **Post-approval oversight lifecycle** — an approved protocol remains under management: amendments, continuing review with expiry/reminders, reportable events, and closure; the protocol record is the institution's compliance memory. Remove → one-shot application form.

**Binding**: human-subjects research ethics semantics — the review is conducted against participant-protection criteria (risk/benefit, consent, subject population) under the institution's research-ethics obligations. Remove the binding → generic committee review / approval workflow.

Jointly held: 1 alone = protocol registry; 2 without 1+3 = bare workflow; 3 without 1+2 = meeting scheduler; 4 without 1–3 = reminder calendar; 1+2 without 3 = staff-processed queue with no board; 1+3 without 2 = committee with no structured submissions; 2+3 without 1 = anonymous form processing.

### L1 — Common Mature Structure

- Configurable smart/e-forms with branching logic and mandatory fields; institution owns its form templates.
- Comment threads bound to specific form sections/questions; side-by-side version comparison on resubmission.
- Role-based dashboards and task lists; email notifications at workflow transitions.
- Determination letters as generated formal correspondence; approval documents archived and retrievable.
- Training/certification verification (CITI-style) surfaced on the protocol.
- Ancillary/parallel reviews (biosafety, radiation, scientific review) triggered alongside IRB review.
- Reporting/analytics for compliance leadership; audit trails.
- Meeting management: agendas, minutes, member review worksheets.

### L2 — Variant / Optional

- Multi-board consolidation (IRB + IACUC + IBC + COI in one system) — packaging variant.
- Multi-institution operation, external-IRB reliance / single-IRB arrangements — common in US multi-site research but structurally variant.
- Regulatory-grade features (21 CFR Part 11 compliance, e-signatures) — regulated-context variant.
- Protocol development/prescreening protocols (pre-approval phase records) — product-specific variant (Cornell).
- UK/EU IRAS-style national submission integration — regional variant (under-sampled; not asserted in detail).
- Institution-built vs commercial SaaS — deployment variant.
- AI assistance, integration with CTMS/sponsored-projects systems — emerging/optional.

### L3 — Vendor-specific (Research Notes only)

- Cayuse: "Smart forms" branding, 11 named study statuses, SP/CITI integrations, specific decision-type vocabulary.
- IRBNet: package locking model, Forms & Templates library naming.
- RASCAL: named statuses (Creating/Submitted/Logged in/Distributed/Assigned to Meeting), Haz Mat module, certification tests.
- eProtocol: Panel/Meeting Date model, "stips" (stipulations) vocabulary, clone protocol.
- InfoEd: eForm tool, multi-committee protocol linking.
- Marketing metrics (45% faster, 35% prep reduction, 80% decision-time decrease) — vendor claims only.

## Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit? Yes: the paper-era IRB office — paper protocol forms, routing slips for department chair sign-off, staff pre-review, typed reviewer assignments, convened monthly meetings with agendas and minutes, stamped approval letters, manila protocol files holding amendments and continuing reviews — satisfies all four L0 structures without any electronic workflow, smart forms, dashboards, or training integrations. The definition therefore abstracts the workflow, not the electronic implementation. UK/EU systems could not be directly sampled (rascal.ac.uk unreachable), but the same structural pattern (protocol record → submission → committee determination → oversight) is the recognizable shape of research-ethics review there as well; geography-specific claims avoided.

## Vendor-specific Findings

See L3 above. None promoted to the canonical core.

## Boundary Findings

| Neighbor | Distinction | "Remove what → becomes the other" |
|---|---|---|
| Animal Research Ethics / IACUC Platform | Same machinery (protocol, submission types, committee, determination, oversight); different subject domain (animal use vs human subjects) | Remove human-subjects semantics, add animal-use semantics → IACUC platform. Sibling Type sharing the L0 shape |
| Research Compliance Management | Broader: multi-board compliance program management (COI, export control, training programs, audits) beyond the protocol-review loop | Remove the protocol-review center of gravity, keep program-level compliance → Research Compliance Management |
| Research Administration Platform / Grants Management | Governs funding lifecycle (proposals, awards), not ethics review; linkage (congruence checks) is integration, not identity | Remove ethics-review semantics, keep funding → Research Administration |
| Clinical Trial Management System / CTMS | Manages study operations (sites, subjects, visits, data) after approval; IRB system governs the review/overship of the protocol | Remove review/oversight, keep operations → CTMS |
| Peer Review Platform | Reviews manuscripts/publications for quality; not participant-protection review of a protocol with a compliance lifecycle | Remove regulatory/participant-protection semantics → Peer Review |
| Ethics & Conduct Management (corporate) | Organizational ethics hotline/policy/case management; not research-protocol review | Remove research-protocol object → corporate ethics management |
| eDiscovery / Legal Hold | Litigation evidence processes; not prospective ethics review | — |
| Approval Workflow Platform | Generic routed approvals; lacks protocol record, committee machinery, ethics determinations, oversight lifecycle | Remove all four L0 structures → generic approval workflow |

## Uncertainties

- UK/EU and other regional ethics-review systems under-sampled (rascal.ac.uk unreachable); whether national-portal integration changes the model is unverified — treated as regional variant, not asserted.
- Exact status vocabularies, review-time claims, and numeric limits are vendor-specific; no canonical numeric claims made.
- Degree to which consent-form management is definitional vs common: observed in several products (RASCAL consent module, eProtocol consent forms, InfoEd) but treated as L1 common, not L0.
- Whether single-IRB/reliance management is growing into a definitional expectation — currently variant.

## Final Synthesis

An IRB / Research Ethics Management application is the research institution's system of record for the ethical and regulatory review of human-subjects research. Its defining core is four jointly-held structures around one object: the protocol as persistent unit of record; structured submissions routed through configured review paths to recorded committee determinations issued as formal correspondence; the ethics board's review machinery (reviewer assignment, comments, convened meetings, minutes); and the post-approval oversight lifecycle (amendments, continuing review, reportable events, closure) that makes the protocol record the institution's compliance memory. Everything else — smart forms, training integration, dashboards, multi-board consolidation, reliance agreements, regulatory-grade e-signatures — is common mature structure or variant, not definition.
