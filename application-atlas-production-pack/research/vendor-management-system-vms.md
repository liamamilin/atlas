# Research Notes — Vendor Management System / VMS

## Research Goal

Understand what a "Vendor Management System (VMS)" actually is as an Application Type — what the "vendor" is, what objects live inside the system, how contingent labor flows through it, which rules and states matter, and — above all — how this leaf relates to its §09 sibling **Contingent Workforce Management**, whose pass (2026-09-07) pre-hung an alias/umbrella flag recommending joint review when this leaf was processed. Secondary goals: verify the boundaries against Staffing Agency Management System (supplier-side mirror), Supplier Management Platform and Government Vendor Management (name collisions), and Services Procurement / Procure-to-pay (SOW overlap).

## Initial Boundary (hypothesis before research)

- Hypothesis (carried from the CWM pass's flag and several prior passes' boundary notes): a VMS is the buyer-side tool for managing the organization's **contingent (non-employee) workforce** — the "vendors" being the staffing suppliers/agencies that provide the workers. If so, this leaf and the Contingent Workforce Management leaf are **one Type under different names** (VMS = classic tool name, CWM = program name, extended workforce platform = modern rebrand).
- Likely confusions:
  - Contingent Workforce Management (§09 sibling) — suspected alias, must be confirmed or refuted from this side.
  - Staffing Agency Management System (§09 sibling) — supplier-side mirror of the same requisition→worker flow.
  - Supplier Management Platform (§10) / Government Vendor Management (§24) — "vendor management" vocabulary collisions with entirely different object models (goods/services suppliers, not staffing vendors).
  - Services Procurement / P2P — SOW modules inside VMS overlap.
- Unknowns going in: can this pass reach any Tier-1 operational documentation (the CWM pass could not)? Is the supplier-side "VMS for staffing firms" a real product form (supports the mirror boundary)? Does the market/analyst category itself carry the "VMS" name?

## Research Questions

1. What does "vendor" mean in a VMS? (Workday's definitional FAQ was the target for this.)
2. What is the core object model — requisition/work order, supplier, candidate submission, worker/engagement record, timesheet, invoice?
3. What is the canonical end-to-end workflow, and where does the system start and stop (does it pay? does it employ?)
4. Who operates it (program office/PMO, hiring managers, procurement, MSP) and what surfaces do suppliers and workers get?
5. Which compliance/risk machinery is structural (background checks, certifications, security IDs, tenure, rehire eligibility)?
6. How does money close (rates, time/expense approval, consolidated invoicing) and where does payment execution land?
7. **Joint-review question:** is this leaf the same Type as Contingent Workforce Management? What do vendors themselves call this product class?
8. What variants exist (SOW/services procurement, direct sourcing, AOR/EOR, shift-based, mid-market vs enterprise, suite module vs standalone)?
9. Historical check: does a pre-cloud, pre-AI VMS generation satisfy the same definition?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Why sampled |
|---|---|---|
| SAP Fieldglass Contingent Workforce Management | Enterprise ERP-integrated; market leader | Vendor self-identifies the product class as VMS (cites its rank in the "VMS landscape"); deep product + features pages fetched this pass |
| Beeline (Enterprise / Professional / Extended Workforce Platform) | Longest-standing independent VMS family | Own nav carries "Vendor management systems (VMS)" as the category; product lines literally named "VMS for enterprises", "VMS for mid-sized companies", "VMS reimagined for staffing firms" |
| VectorVMS | Mid-market; brand contains "VMS" | Full VMS product page fetched; support portal attempted (Tier 1, failed) |
| Workday VNDLY | HCM-suite module pole | Product page literally titled "VENDOR MANAGEMENT SYSTEM — Your contingent workforce system of record"; dedicated "What is a vendor management system?" definitional FAQ |
| Magnit (VMS) | Services-led pole (MSP+VMS unified) | VMS page fetched; legacy login surfaces (Wand VMS, Workforce Logiq VMS) evidence multi-generation VMS product lines |

## Sources

All fetched 2026-09-08 by this pass. Tier 2 (official product/definitional pages); no Tier 1 operational help-center content was reachable (see Source-access Limitation).

- SAP — SAP Fieldglass Contingent Workforce Management product page: https://www.sap.com/products/hcm/contingent-workforce-management.html
- SAP — SAP Fieldglass Contingent Workforce Management features page: https://www.sap.com/products/hcm/contingent-workforce-management/features.html
- Beeline — Extended Workforce Platform (category/product overview incl. "Vendor management systems (VMS)" nav category): https://www.beeline.com/solutions/extended-workforce-platform
- VectorVMS — Vendor Management System product page: https://vectorvms.com/vendor-management-system/
- Workday VNDLY — VMS overview: https://www.workday.com/en-us/products/vndly-vms/overview.html
- Workday VNDLY — "What is a vendor management system?": https://www.workday.com/en-us/products/vndly-vms/what-is-a-vendor-management-system.html
- Magnit — VMS page: https://magnitglobal.com/vendor-management-system

Failed fetches (1 attempt each, then abandoned per network rules):
- SAP Help Portal (https://help.sap.com/docs/SAP_Fieldglass) — served a JS-shell page with no content.
- VectorVMS support portal (https://support.vectorvms.com) — request timed out.

Source-access Limitation: no vendor help center / user guide / operational manual was reachable in this environment (same limitation as the sibling CWM pass on 2026-09-07). Consequently: no exact state-machine labels, no numeric limits, and no UI field lists are asserted in the final document; all cross-product claims are kept at "commonly/typically" strength and derived from official product and definitional pages. Vendor marketing numbers observed (190 countries, 180 countries [SAP uses both on different pages], 120+ reports, 1,800+ integrations, 30-day deployment, 90% automated onboarding adoption, savings percentages) were noted but excluded from the final document.

## Product Observations

### SAP Fieldglass Contingent Workforce Management (evidence layer: A — direct vendor pages)

- Product page + features page both fetched. The vendor's own analyst-recognition block cites the "Ardent VMS Tech Advisor 2025" report ("ranked Market Leader in the VMS landscape") — SAP's own page names the category **VMS** while the product carries the CWM name. Direct same-product/two-names evidence from this side.
- Lifecycle framing: "Manage the complete lifecycle of your contingent workforce from requisition and engagement to offboarding and evaluation." Automation bullet: "Automated work orders, time sheets, expenses, approvals, and payments."
- FAQ: three stated purposes — (1) create workforce capacity on demand (talent pools, side-by-side comparison with benchmarked rates); (2) manage for results (streamline requisitions and approval flows); (3) proactive risk/compliance control (automated labor-rate and tenure tracking, invoice accuracy, "airtight" on/offboarding).
- Features detail (this pass): AI-assisted job descriptions and translations; decision wizards for sourcing-channel selection and **worker classification**; custom templates specifying "job descriptions, qualifications, pay rates"; **configurable distribution and tiered positioning targeting preferred MSPs and suppliers**; ML side-by-side candidate comparison; **compliant offer/pay-rate negotiation inside the application**; verification of licenses/certifications/training **before the job starts**; background checks, security IDs, access restrictions; asset tracking (gate passes, laptops); **pro forma invoices aligned with defined terms** for reconciliation/settlement; integrated evaluation/feedback; ERP/HRIS unification.
- Distinctive vendor detail (stays out of canonical model): per-worker **security ID** linking onboarding/offboarding/history and rehire-eligibility status; **crew/gang (team-based) staffing** with group worksheet approval (railroad repair crews, consulting teams); field-level visibility suppression by line of business; pay parity; invoice-format compliance.
- Worker dashboard shown in product hero: spend information, tenure, engagement duration, documents attached to the worker.

### Beeline (evidence layer: A)

- Site nav (this pass): Solutions list carries BOTH "**Extended workforce platform** — an end-to-end platform for all types of external workforce engagement" AND "**Vendor management systems (VMS)** — simplify external workforce management" as the category label; Products list names "**Beeline Enterprise** — VMS to support large, global, complex external workforce programs" and "**Beeline Professional** — VMS for mid-sized companies". The word VMS is used as the product-class noun throughout.
- Positioning: "a modern, cloud-based platform built entirely to manage the external workforce"; benefits framing across Visibility / Efficiency / Cost saving / Compliance.
- Enterprise VMS attributes: custom processes, longer implementation, "a centralized team manages your contingent workers", per-country fiscal/legal/cultural/language requirements. Professional VMS: best-practice templates, rapid deployment, one-or-more-country reporting.
- **Supplier-side VMS confirmed** (this pass): "Beeline Professional for staffing suppliers — VMS reimagined for staffing firms… a powerful and easy-to-deploy VMS to help staffing agencies and master vendor providers" — plus Beeline Supplier Network (supplier profiles, ATS integration) and JoinedUp (shift/roster management for high-volume frontline labor). Strong boundary evidence: the same software class exists on the staffing firm's side of the transaction.
- AOR/EOR variant present (MBO Partners by Beeline) for independent contractors/freelancers.
- Era evidence: "backed by decades of intelligence, experience, and innovation" — multi-decade VMS heritage.

### VectorVMS (evidence layer: A)

- Product page: "Get end-to-end visibility and control over your contingent workforce with a flexible VMS that's quick to implement and easy to use."
- Three talent types in one platform: **Staff Augmentation** ("distribute, review and manage contingent workers in one place"), **Services Procurement** ("sole source or competitively bid… milestone, and time & material projects"), **Extended Workforce** ("gig workers, independent contractors and more with talent pooling, compliance management and shift scheduling").
- Platform capability groups: **Compliance** (track by position and location; NDAs, certifications, drug screening, security access; workflows/alerts for pre-engagement, onboarding, offboarding; "ensure that compliance doesn't expire during the lifetime of your candidate"); **Spend** (timesheets, volume discounts, overtime rates; approve contractor time online; "pay a single invoice for all your contingent labor"; real-time budget alerts); **Lifecycle** ("single source of record" for staff augmentation, services procurement, and other resources; procure/track temps and hourly workers; SOW via milestones/resources/fees; "track IDs for security, cafeteria, landscaping, janitorial, and other nonemployees on premises"); **Quality** (candidate comparison; performance tracked by role/manager/department/vendor; flag poor performers to prevent re-engagement; vendor performance ranking); **Efficiency** (requisitions → candidate review → timesheets → evaluation in a single system; mobile timesheet approval); **Metrics** (spend, tenure, diversity, time-to-fill, false starts; dashboards per stakeholder for procurement, HR, hiring managers).
- Delivery models: license only / Shared Managed Services (hybrid) / MSP-run.

### Workday VNDLY (evidence layer: A)

- **Overview page title: "VENDOR MANAGEMENT SYSTEM"** with the line "**Your contingent workforce system of record.**" — "our industry-leading vendor management system (VMS) that can pair with Workday Human Capital Management (HCM) to support total workforce optimization." The leaf's exact name is the product's own headline.
- Efficiency bullets: "extensive configurability, approval workflows, full-service statement of work (SOW), consolidated invoicing, vendor portal access." Visibility: "contingent worker headcount, assignments, spend, vendor performance." Compliance: configurable to local requirements, role-based data access. Global: "one global instance… local compliance, in-country invoicing, tax management."
- Products: Extended Workforce Management ("every step of your contingent labor lifecycle, from requisition to offboarding"), Statement of Work, Worker Profile Management.
- Lifecycle roles: **Program Teams** (rule-based configuration, approval workflows, vendor oversight), **Hiring Managers** (automated requisition creation, candidate shortlisting, interview management, vendor collaboration), **Vendors and Contractors** (clear assignment details, simple time entry, timely approvals).
- FAQ (on the overview page): "What is a vendor management system? A vendor management system is a web-based software application that centralizes the end-to-end lifecycle management of extended workers and statement of work needs." "What key features are found in a vendor management system? Core VMS capabilities typically include **vendor portal access, sourcing, tenure and rate management, invoicing, worker tracking, SOW, and reporting**." "What are the benefits…? manage contingent workforce cost, efficiency, quality, and risk in a single platform."
- Category-name evidence: "Workday VNDLY named a Leader in Everest Group's **VMS** PEAK Matrix® Assessment 2026" — the analyst category is named VMS.
- Definitional FAQ page (fetched this pass): "A vendor management system (VMS) is a software solution that helps you manage the entire lifecycle of your contingent workers—from sourcing, engaging, managing, and invoicing through reporting and offboarding." "**Vendor**: … those who are supported by VMS technology—which includes contract employment agencies, service providers, and the contingent workers themselves." "Contingent worker: anyone who works on behalf of your organization but is not a direct employee." Typical features: "supplier management, order distribution, consolidated billing, risk mitigation, headcount tracking, and significant improvements in reporting." Usage: "most often used by the program management office (PMO) team to help with daily management tasks," data leveraged by HR, finance, IT. Global compliance: global invoicing, in-country tax structures, local currency billing, complex rate calculations, local employment laws. Security: systems "record and store personal worker information" and are held to high standards with third-party-validated controls. VMS+HCM connection for total workforce. Components: Extended Workforce Management, SOW, Worker Profile Management. AI/ML for applicant identification. Notes: "you may find VMS vendors who use the term 'extended workforce system' or 'extended workforce platform'."
- Workday main nav (this pass) lists "**Vendor Management System**" as a product under HR.

### Magnit (evidence layer: A)

- Page title: "**Vendor Management System (VMS) for Smarter Contingent Workforce Management**" — the two names paired again.
- Positioning: "All Your Workforce Management in One Platform… real-time visibility and control to source faster, stay compliant, and achieve measurable savings"; "The Only Vendor-Neutral VMS Software That Manages 100% of the Contingent Workforce Lifecycle"; unified MSP + VMS.
- Capabilities: end-to-end workforce visibility and analytics (sourcing, spend, worker status, vendor performance); AI matching and workflow automation; integrated pay intelligence (rate benchmarking, OT/DT tracking); compliance rules engine; global architecture.
- Ecosystem: MSP, EOR ("hire and pay global talent"), Direct Sourcing ("build private talent pools"), Services Procurement, Shift-Based Workforce Management.
- **Multi-generation evidence (this pass):** the client-login area lists the legacy product surfaces — "**Wand VMS** (PRO Unlimited lineage)" and "**Workforce Logiq VMS**" — alongside Magnit Shift and Pay Intel. The "VMS" tool name survives brand consolidation as the login/product surface name.
- FAQ: "A Vendor Management System (VMS) streamlines how you manage your contingent workforce from sourcing and onboarding to time tracking and invoicing." "A VMS centralizes and automates how organizations manage contingent workers by improving visibility, compliance, and cost control."

## Cross-product Comparison

| Dimension | SAP Fieldglass | Beeline | VectorVMS | Workday VNDLY | Magnit VMS |
|---|---|---|---|---|---|
| Uses "VMS" as the class name | Yes (cites "VMS landscape" rank on own page) | Yes (nav category "Vendor management systems (VMS)"; "VMS for enterprises/mid-sized") | Yes (brand + page) | Yes (page title "VENDOR MANAGEMENT SYSTEM"; Everest "VMS PEAK Matrix") | Yes (page title; legacy Wand VMS/Workforce Logiq VMS logins) |
| Subject population | contingent workers: contractors, consultants, freelancers, service providers | external/contingent workforce; + ICs via AOR/EOR; + shift-based (JoinedUp) | staff augmentation + services procurement + gig/IC extended workforce | contingent workers + SOW (external workforce) | contingent workforce; + EOR, direct sourcing, shift-based |
| Entry object | requisition / work order | requisition (VMS class) | requisition ("submit requisitions") | job requisition (automated creation) | sourcing request |
| Fulfillment | suppliers with tiered posting, MSP targeting | suppliers via Supplier Network; staffing-firm VMS | suppliers; competitive or sole source | vendors via portal | suppliers + direct-sourcing pools |
| Worker/engagement record | worker dashboard: spend, tenure, engagement duration, documents; security ID | worker tracking (VMS class) | single source of record; on-prem nonemployee IDs | Worker Profile Management product | worker status in analytics |
| Compliance machinery | background checks, security IDs, access restrictions, tenure automation, pre-start verification | compliance benefit axis; audit | NDAs, certifications, drug screening, security access; expiry during lifetime; pre-engagement/onboarding/offboarding workflows | tenure management, rehire eligibility, role-based access | compliance rules engine |
| Time/expense | automated timesheets, expenses | Time/Expense/Billing area | timesheets, OT rates, online + mobile approval | time and expense tracking; approvals | time tracking |
| Financial closure | pro forma invoices aligned to terms | billing area | single consolidated invoice for all contingent labor | global digital invoicing; invoice template generator | invoicing (in definition) |
| SOW/services | sibling product (Services Procurement) | in scope | milestones/resources/fees; T&M projects | separate SOW product | Services Procurement solution |
| Program ops | ERP integration; centralized processes | MSP partners; enterprise/professional tiers | license / hybrid managed services / MSP | program teams; MSP partners | unified MSP+VMS |
| Roles | hiring managers, suppliers, program teams | program + suppliers | procurement, HR, hiring managers, vendors | program teams, hiring managers, vendors & contractors | program + suppliers |
| AI | Joule (job descriptions, screening, reporting) | positioning | (not prominent on fetched page) | AI insights for matching | Maggi AI matching/automation |

### Stable cross-product commonalities (layer B — observed across all 5 sampled products)

1. The managed subject is the organization's **contingent (non-employee) workforce** — temps, contractors, consultants, freelancers; gig/IC in several.
2. The system is operated **buyer-side** (the organization using the workers); staffing suppliers/vendors and workers participate through portals.
3. Work enters as a **request** (requisition/job posting; SOW project as the second form) defining role, skills, dates, rate.
4. Fulfillment runs through **managed external sources** — staffing suppliers/agencies ("vendors") classically; talent pools/direct sourcing as modern extensions.
5. A tracked **worker engagement lifecycle**: request → source/select → onboard (compliance gate) → work (time/expense) → offboard.
6. **Compliance machinery** attached to the worker/engagement: background checks, certifications/credentials verified before start, NDAs, security/site access, tenure tracking, rehire eligibility.
7. **Rate management and enforcement**: agreed rates/rate cards; only approved spend becomes invoicable.
8. **Time/expense capture in-system, buyer approval, invoicing** — commonly consolidated across suppliers; payment execution stays downstream (AP/ERP).
9. **Program visibility as the raison d'être**: who is working, where, how long, at what cost; spend/headcount/tenure/vendor-performance reporting.
10. **Multi-party roles**: program office/PMO, hiring managers, procurement, suppliers, workers, (often) an MSP operating the program.
11. Integration with **HCM and ERP/AP** systems (total-workforce view; finance handoff).
12. Vendor/supplier performance tracking and rehire flags.

### Joint-review finding (this leaf's central taxonomy question)

**Alias confirmed from this side, with independent naming evidence gathered this pass (all layer A):**

- Workday's VNDLY product page is literally titled "**VENDOR MANAGEMENT SYSTEM**" and subtitled "**Your contingent workforce system of record**" — the leaf name and the sibling's definition are the same product, in one headline.
- Workday's nav lists "Vendor Management System" as a product; its FAQ defines the VMS as managing "the entire lifecycle of your contingent workers."
- Beeline's nav carries "**Vendor management systems (VMS)**" as the category and "Extended workforce platform" as the umbrella, with products literally named "VMS for enterprises," "VMS for mid-sized companies."
- SAP's CWM page cites its own "Market Leader" rank in the "**VMS landscape**" (Ardent VMS Tech Advisor 2025); Workday cites Everest Group's "**VMS** PEAK Matrix Assessment" — the analyst category itself is named VMS.
- Magnit titles its page "VMS for Smarter Contingent Workforce Management" and its login surfaces carry the legacy tool names (Wand VMS, Workforce Logiq VMS).
- VectorVMS's brand and page use VMS for a contingent-workforce product whose own page says "end-to-end visibility and control over your contingent workforce."

Conclusion: one Application Type, three market labels. **"VMS" is the classic tool name** (the vendors being the staffing suppliers), "contingent workforce management" is the program/function name, "extended workforce platform/system" is the modern rebrand (Workday's own FAQ documents the rebrand). This pass therefore adopts the sibling CWM pass's canonical core, deliberately structure-compatible, and documents the Type from the VMS leaf's named perspective. The CWM pass's pre-hung flag is discharged from this side; resolution = **keep both directory leaves as aliases of one Type** (no merge, no taxonomy rewrite).

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small; structure-compatible with the CWM pass)

A Vendor Management System is the **buyer organization's system of record for managing its contingent (non-employee) workforce as a governed program** — the "vendors" being the external staffing sources that provide the workers. Four jointly-held structures, each load-bearing:

1. **The contingent worker record** — a persistent, identified record per non-employee person (or team) engaged to work for the organization, carrying engagement context rather than employment terms: role/assignment, start/end dates and accumulated tenure, rate and cost, location, documents, compliance state. Remove → an employee HRIS or a procurement catalog; the Type disappears.
2. **The work request fulfilled through managed external sources** — a requisition/job posting (or SOW project request) raised in the system and distributed to enrolled external fulfillment sources (staffing suppliers, agencies, talent pools) that respond with candidates/proposals, from which the hiring manager selects. Remove → hiring happens in an ATS (ends in employment) or a procurement tool (buys goods); no contingent program.
3. **The governed engagement lifecycle with a compliance gate** — the engagement moves through managed states (requested → sourced/selected → onboarded → working → offboarded); onboarding is gated on required checks/documents; compliance state is tracked during the engagement; offboarding is a managed event. Remove → a placement list or spreadsheet, not a management system.
4. **The financial closure loop** — time/expense (or milestone) capture in-system, buyer approval, and invoicing reconciled against agreed rates, commonly consolidated across suppliers; payment execution remains downstream in AP/ERP. Remove → an applicant/candidate tracker; the "manage and pay the supplier for the work" half is gone.

The visibility claim every vendor states — who is working for us, where, how long, at what cost, under what compliance standing — is what these four records add up to, not a fifth structure.

Historical check: the classic pre-cloud VMS generation (the tool name itself dates from that era; Beeline cites decades of VMS heritage; Magnit still operates two acquired legacy VMS products as login surfaces) already ran requisition distribution, timesheet approval, and consolidated invoicing for temp/contract labor — satisfying this L0 with none of today's AI, direct sourcing, or global tax machinery. The definition is independent of cloud delivery, of any specific worker subtype, and of supplier-mediated vs pool-based sourcing. No older/regional/platform-native product class fails the definition; the phrase "vendor management" itself is the era artifact (the vendors are the staffing agencies — before modern rebranding reframed the subject as the workforce).

### L1 — Common Mature Structure (very common; not definitional)

- Rate machinery: rate cards, negotiated bill rates, markups, rate thresholds, overtime rules; enforced at invoicing.
- Candidate workflow: submissions, shortlists, side-by-side comparison, interview scheduling; AI/ML ranking increasingly common.
- Approval workflows at every gate (requisition, selection, onboarding, timesheet, invoice).
- Supplier and worker performance tracking; rehire-eligibility flags.
- Reporting/analytics: spend, tenure, headcount, time-to-fill, diversity; stakeholder-specific dashboards.
- Consolidated invoicing across suppliers; invoice templates; country-specific invoice formats in global programs.
- Budget visibility and alerts.
- Mobile apps (manager approvals; worker time entry).
- MSP operating-model support.
- Integration spine: HCM, ERP/AP, SSO, e-signature.
- AI assistance (job-description drafting, candidate matching, workflow automation) — current-generation common.

### L2 — Variant / Optional Structure

- SOW / services-procurement module (milestone-, deliverable-, resource-, fee-based projects) — packaged as built-in (VectorVMS), separate product (SAP, VNDLY), or functional area (Beeline).
- Independent-contractor engagement via AOR/EOR services.
- Direct sourcing / private talent pools under the buyer's brand.
- Shift-based frontline workforce management (drifts toward Employee Scheduling semantics).
- On-premises physical security integration (badge/security IDs for nonemployees, asset tracking).
- Crew/gang (team-based) engagement with group worksheets (observed at one product; qualified).
- Regional compliance engines (local tax tables, invoicing formats, pay parity).
- Delivery model: pure license vs vendor-run hybrid managed services vs MSP-operated.
- Tier: enterprise global programs vs mid-market rapid-deploy templates.

### L3 — Vendor-specific (kept out of the final document)

- SAP: per-worker security ID linked to onboarding/offboarding/history/rehire eligibility; crew/gang worksheets (railroad/consulting framing); field-level visibility suppression by line of business; Joule assistant; intelligent configuration manager (five components); 190/180-country and 99%-invoice-accuracy claims (inconsistent across SAP's own pages); 2% rate-savings claim.
- Beeline: Supplier Network; Professional-for-staffing-suppliers packaging; 30-day deployment claim; 400+ companies claim; MBO Partners AOR/EOR.
- Magnit: Maggi AI; Pay Intelligence; 1,800+ integrations; BYOK; C5 certification; vendor-neutral positioning; legacy Wand/Workforce Logiq login surfaces.
- VectorVMS: 120+ standard reports; Shared Managed Services hybrid; support portal (unreachable).
- Workday VNDLY: conditional custom fields; invoice template generator; Workday HCM pairing specifics; Everest PEAK Matrix Leader claim.

## Vendor-specific Findings

See L3. None promoted to the canonical model. The SAP security-ID mechanic and VectorVMS's on-premises nonemployee ID tracking together suggest site-access tracking is a common-in-site-based-segments capability (2/5), not a core structure.

## Rejected Findings

- "VMS = Supplier Management Platform" — rejected. Despite the word "vendor," the VMS's vendors are staffing sources for human labor under a requisition→worker flow; Supplier Management manages a goods/services supplier population with records, standing, and information currency. Vocabulary collision only.
- "VMS = Government Vendor Management" — rejected. Same vocabulary collision; the government Type is a registry/eligibility-standing system over a vendor population, not a labor-program tool.
- "A VMS pays the workers" — rejected as definitional. Workers are paid by their staffing supplier (or an EOR); the VMS produces approved, rate-checked invoices toward AP/ERP.
- "A VMS employs the workers" — rejected. The triangular relationship is structural: supplier employs/pays, buyer directs/approves.
- "VMS = MSP" — rejected. The MSP is an operating model for running the program on the platform, not the software Type; license-only delivery exists in the sample.
- "Shift scheduling is part of the VMS" — rejected as definitional; it appears as a distinct product line (JoinedUp; Magnit Shift) and as an extended-workforce scope bullet in one mid-market product.

## Boundary Findings

| Neighboring Type | Relationship | Discriminator ("remove what → becomes the other Type") |
|---|---|---|
| Contingent Workforce Management (§09 sibling) | **Alias — same Type** | None. One product population, three labels (VMS / CWM / extended workforce platform); confirmed independently this pass via Workday page title, Beeline nav, SAP analyst citations, Magnit legacy logins. Remove nothing — the names differ, the Type does not. |
| Staffing Agency Management System (§09 sibling) | Mirror image (supplier side) | The operator. Beeline explicitly sells a VMS "for staffing suppliers" — same software class, opposite transaction side. Hand the record to the staffing firm → agency-side Type. |
| Human Capital Management / HRIS (§09) | Complementary population split | Employees (employment records, payroll) vs non-employees (engagements via external sources). Remove "non-employee via external source" → HCM. |
| Applicant Tracking System / Recruiting (§09) | Flow-similar, outcome-different | Both run requisition→candidate→selection; the VMS ends in a supplier-engaged non-employee engagement with billing closure, the ATS ends in an employment hire. Remove external fulfillment + invoicing → ATS. |
| Supplier Management Platform (§10) | Vocabulary collision only | Its "vendor" is a goods/services supplier with records and standing; the VMS's "vendor" is a staffing source in a requisition→worker flow. Different object models entirely. |
| Government Vendor Management (§24) | Vocabulary collision only | Registry + eligibility standing of a government's vendor population; no requisition→worker flow, no time/billing. |
| Services Procurement / Procure-to-pay (§10) | Adjacent; variant module here | SOW projects inside a VMS are workforce-flavored services procurement; generic services procurement covers non-labor services. SAP ships them as sibling products. |
| Employee Scheduling / WFM scheduling (§09) | Adjacent at the shift-based pole | High-volume contingent shift filling borrows scheduling semantics; classic VMS governs engagements and billing, not rosters. |

## Uncertainties

- No Tier 1 operational documentation (help centers/user guides) was reachable for any sampled product (SAP Help Portal JS shell; VectorVMS support portal timeout; others not attempted beyond product surfaces). Interface and rule descriptions in the final document are kept at "commonly/typically" strength, derived from official product/definitional pages.
- Exact state names/counts for requisitions, engagements, timesheets, and invoices were not observed; conceptual states only.
- Whether any VMS executes actual payment (vs producing approved invoices) was not confirmed; all sampled descriptions end at invoicing/consolidated billing, so "payment execution remains downstream" is stated at that strength.
- The supplier-side VMS (Beeline Professional for staffing suppliers) is documented only at product-page depth; its internal structure was not examined and belongs to the Staffing Agency Management System pass.
- Market-share and segment-size claims are absent by design (no reliable source in this environment).

## Final Synthesis

The Vendor Management System leaf and the Contingent Workforce Management leaf denote **one Application Type**. Its defining core is small and buyer-side: contingent worker records + request-driven fulfillment through managed external sources (the staffing "vendors" that give the Type its name) + a governed engagement lifecycle with a compliance gate + a time/expense-to-invoice financial closure — all operated as a program with multi-party roles (program office, hiring managers, procurement, suppliers, workers, often an MSP). Everything else — rate cards, AI matching, SOW modules, direct sourcing, AOR/EOR, shift scheduling, global tax engines, physical-security integration — is common mature structure or variant structure. The joint-review flag from the CWM pass is discharged: keep both leaves, documented as aliases of the same Type, with each document written from its own name's perspective. The vocabulary collisions with Supplier Management Platform and Government Vendor Management are recorded so cross-reference work does not confuse "vendor management" meanings across the directory.
