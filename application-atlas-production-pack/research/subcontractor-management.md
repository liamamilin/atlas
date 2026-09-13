# Research Notes — Subcontractor Management

## Research Goal

Understand, from real products, what "Subcontractor Management" is as an Application Type: what the hiring organization (general contractor, owner/hiring client, residential builder) actually manages about its subcontractors, what objects and states exist, how the subcontractor participates, and where the Type's boundary sits against the many neighboring construction Types that touch the same relationship (preconstruction, bidding, cost, labor, safety) and against cross-industry neighbors (supplier management, VMS, third-party risk).

## Initial Boundary

Working hypothesis before research:

- Core use: the hiring organization maintains a managed population of subcontractor companies, keeps each company's qualification/compliance state current, and links each company to the work it is engaged on.
- Primary users: GC prequalification/compliance staff, estimators/bid desks, schedulers, PMs, safety managers; residential builders; owner-side contractor-management programs.
- Nearest neighbors: Preconstruction Management (solicitation/leveling/award), Construction Bidding Platform (multi-party venue), Construction Cost Management (commitments/invoices), Construction Labor Management (worker grain), Construction Safety Management (safety register), Supplier Management Platform (§10 procurement), Vendor Management System (§09 staffing), Third-party Risk Management (§11).
- Main risk: this leaf could be an umbrella over pieces of sibling Types rather than a Type with its own unit of record.
- Unknowns: is the subcontractor-facing portal definitional or a modern realization? Is money machinery part of the core? Is owner-side contractor management (compliance networks) the same Type or a different one?

## Research Questions

1. What is the unit of record — the company, the person, the contract, or the project?
2. What qualification/compliance content is managed per subcontractor, and who supplies it?
3. What lifecycle does the subcontractor relationship pass through (prospect → qualified → invited → awarded → on site → evaluated)?
4. How is engagement with work represented (project membership, schedule assignment, bid participation)?
5. How does money appear (bids, POs, invoices, lien waivers, payment status) and is it definitional?
6. What does the subcontractor itself do in the system?
7. How do performance evaluation and ongoing monitoring work?
8. Which capabilities are Type-defining vs common vs variant vs vendor-specific?
9. Where exactly are the seams to the neighboring Types listed above?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole | Customer tier | Evidence quality |
|---|---|---|---|
| Procore | commercial GC suite; prequalification as formal gated workflow + company directory | enterprise/commercial GC & owners | Tier-1 support docs (fetched) |
| Buildertrend | residential SMB all-in-one; relationship/communication-centric "Sub Portal" | residential builders/remodelers | Tier-2 marketing + help-center content surfaced via search (direct fetch blocked) |
| Buildxact | estimating-first; subcontractor management as RFQ/procurement + schedule assignment | residential/light-commercial SMB | Tier-1 help center + Tier-2 (surfaced via search) |
| Avetta | owner/hiring-client compliance network; verification-as-a-service; multi-tier | industrial/energy/commercial hiring clients + suppliers | Tier-2 product pages (fetched) + solution brief |
| HammerTech | EHS-centric contractor management; site-readiness focus | commercial GCs, EPC, owners | Tier-2 product page with FAQ (fetched) |

## Sources

Research date: 2026-09-10.

Fetched directly (Tier-1/Tier-2):

- Procore — Prequalifications (tool landing page): https://support.procore.com/products/online/user-guide/company-level/prequalifications
- Procore — Prequalification Portal - Workflow Diagrams: https://support.procore.com/products/online/user-guide/company-level/prequalification-portal/workflow
- Procore — Company Directory (tool landing page): https://support.procore.com/products/online/user-guide/company-level/directory
- Avetta — Contractor Prequalification & Monitoring: https://www.avetta.com/clients/solutions/health-and-safety/prequalification
- Avetta — Subcontractor Management (client side): https://www.avetta.com/clients/solutions/health-and-safety/subcontractor-management
- HammerTech — Subcontractor Management: https://www.hammertech.com/en-us/platform/subcontractor-management

Surfaced via web search (content visible in search results; direct fetch blocked or not attempted per network rule):

- Buildertrend — Subcontractor Management Overview (help article): https://helpcenter.buildertrend.net/s/article/Subcontractor-Overview (help center is JS-rendered; direct fetch failed with CSS error)
- Buildertrend — Manage Subs with Subcontractor Software: https://buildertrend.com/communication/subcontractor-software/ (help-article mirror returned 403)
- Buildertrend — Benefits of Subcontractor Management Software (blog): https://buildertrend.com/blog/subcontractor-management-software/
- Buildxact — General FAQs: https://help.buildxact.com/en/articles/8733540-general-faqs
- Buildxact — Understanding the Buildxact navigation menu: https://help.buildxact.com/en/articles/5168138-understanding-the-buildxact-navigation-menu
- Buildxact — Construction Quoting Software: https://www.buildxact.com/us/features/construction-quoting-software/
- Buildxact — Estimate phase RFQ video transcript: https://www.youtube.com/watch?v=hfwm6a_zYjE
- Avetta — Prequalification Solution Brief (PDF): https://pages.avetta.com/rs/752-BVH-753/images/Prequalification-Solution-Brief.pdf
- Avetta — Company prequalification (supplier side, AU): https://www.avetta.com/en-au/suppliers-contractors/products/company-prequalification
- Avetta — Subcontractor management (supplier side): https://www.avetta.com/suppliers-contractors/products/subcontractor-management
- HammerTech — General Contractors segment page: https://www.hammertech.com/en-us/solutions/segments/general-contractors
- HammerTech — Subcontractors segment page: https://www.hammertech.com/en-us/solutions/segments/subcontractors

Source-access limitations:

- Buildertrend's help center could not be fetched (Salesforce JS site); its evidence is calibrated to marketing/blog pages plus help-article content surfaced through search. No precise defaults or limits are asserted from Buildertrend.
- Buildxact evidence is help-center + marketing content surfaced through search; no precise limits asserted.
- Avetta and HammerTech are Tier-2 (product marketing with FAQ); no operational manuals were reachable. Claims from these two are held at marketing-level strength.
- Procore is the only sample with fully fetched Tier-1 operational documentation.
- No precise numeric limits, default settings, or exact status vocabularies are asserted anywhere in the final document except where directly observed and materially useful.

## Product A — Procore (commercial GC suite)

### Key observations

- **Prequalifications tool (company level)** — "designed to allow General Contractors or Owners to set up, manage, and extensively evaluate potential bidders." Setup/review actions: configure the prequalification form; invite companies to prequalify; review and comment on a submitted form; create a change request; prequalify a company; view the form and its change history; view/filter the prequalification company list. (A)
- **Two-sided structure** — "Subcontractors or other collaborators access the Prequalification Portal to view, submit, and manage their prequalification materials." The subcontractor side is a separate tool with its own permissions; users must first exist in the Company Directory, and invited companies automatically get Read-Only access to the portal. (A)
- **Directory as the company population of record** — the Company Directory holds collaborator companies and people; tutorials include: add a company to the directory; add a company to a project; **add insurance to a company record**; **update expiring insurance for a vendor**; remove company insurance; deactivate/reactivate a company; merge companies; set bidder information at the company level; designate an insurance manager. Release notes show: "New 'Additional Insured' Field for Companies", "Save Companies from the Procore Construction Network to your Directory", "Manage Bid Contacts for a Connected Company", "improved company association accuracy for Procore Pay". (A)
- **Engagement linkage** — companies are added to projects (project directory); bidder information and bid contacts live on the company record; a Bidding tool integration exists ("About the Bidding + COMPASS Integration" referenced from Prequalifications). (A)
- **Form-driven evaluation** — configurable prequalification form with custom questions; category response data (Standard users can view all categories "except for Financials" — financials are a distinct, more sensitive category); status setting on forms; change requests back to the subcontractor. (A)
- Positioning: prequalification protects the GC/owner's "best interests" and minimizes financial risk before bidding. (A)

## Product B — Buildertrend (residential SMB all-in-one)

### Key observations

- **Sub/Vendor record** — "Buildertrend enables seamless collaboration with your subcontractors, trades, and vendors through the Sub/Vendor profile feature. You can invite them to join you on Buildertrend with tailored access to features and job details, or simply store their contact information for easy internal reference." One record type covers subs and vendors; subs are added individually or by import; adding a sub to a job triggers a Permission Wizard. (B — help article surfaced via search)
- **External-party permissions** — "Unlike internal users, subs and vendors have default permissions that cannot be customized… ensuring they can only view information relevant to their role as external partners." Some adjustments possible per profile/job. (B)
- **Engagement linkage** — subs are added to jobs; "Assign subcontractor work to scheduled items within your project timeline"; each sub logs in and sees "when they're needed and if they're approved to start work"; subs can be assigned to Warranty service appointments and confirm/reschedule. (B)
- **Communication hub** — in-platform messages; job comments available on Bids, Change Orders, Daily Logs, Files, Bills, Purchase Orders, Scheduling; subs can answer RFIs via comments. (B)
- **Fitness state** — "Store that information and other important agreements for each sub in our system, then elect to receive notifications prior to when certificates expire" (insurance tracking with expiry notifications). (B)
- **Bid solicitation** — "create, compare, send and store bids… notifies subs when a bid package is ready and communicates deadlines." (B)
- **Money status** — "Reference any outstanding POs or lien waivers awaiting sign-off to ensure subs are being paid on time and accurately"; Bill Pay "streamlines the entire subcontractor payment process"; PO tool sends electronic agreements to subs for sign-off on scope and payment. (B)
- Positioning: subcontractor management is one named capability inside a platform that spans sales→project→financial management. (B)

## Product C — Buildxact (estimating-first SMB)

### Key observations

- **Contacts book** — suppliers and subcontractor contacts held in a contacts book; new suppliers/contacts can be added from the RFQ screen. (B)
- **RFQ machinery to the "labor network"** — "Save time when you send RFQ invitations to multiple subcontractors in your labor network"; "Track who's accepted your invitations, compare quotes based on consistent responses, and pick the most suitable one"; RFQs are sent per trade/line from estimates and jobs; the Request for Quotes section aggregates all RFQs across estimates and jobs (Pro/Teams subscription). (B)
- **Two-sided response** — recipients (trade suppliers/subcontractors) respond through a link: interested yes/no/yes-later; open/submitted/pending/rejected statuses visible to the sender; recipients can reopen and resubmit until a winner is picked; the builder can enter a reply on the recipient's behalf; subcontractors "do not need to subscribe to Buildxact to open and submit quotes" (freemium response accounts). (B)
- **Award → estimate/budget** — picking a winner ("chosen") updates the price in the estimate; the winning quote can convert into a purchase order. (B)
- **Schedule assignment** — tasks in the job schedule carry assigned contacts; bulk emails can be sent to contacts assigned to tasks in the schedule. (B)
- Positioning: subcontractor management is realized through procurement (RFQ) and scheduling rather than through a compliance workflow. (B)

## Product D — Avetta (owner/hiring-client compliance network)

### Key observations

- **Prequalification & monitoring** — "Collect, review and monitor safety performance, audits, certifications, documents and more to better manage risk and compliance in one place." Questionnaires (PQFs), performance indicators, supporting documents; Avetta's own compliance specialists verify and continuously update supplier data (verification-as-a-service). (A — fetched)
- **Subcontractor Management as tier extension** — dedicated client-side solution: "Extend your compliance programs to all contractor tiers"; "Prime contractors can easily discover, invite and connect with new subcontractors for projects"; "Subcontractors undergo the same prequalification process as prime contractors"; analytics "at the contractor, subcontractor and workers levels". The solution brief has a literal "Subcontractor Management" section: "Extend prequalification to both contractors and subcontractors, applying consistent standards across all tiers for a unified view of third-party risk." (A — fetched)
- **Sourcing from a network** — "Tap into our network of 130,000+ prequalified contractors"; search filters by location, trade, diversity; prequalification indicators. (A — fetched; number is vendor-specific, not asserted in final doc)
- **Two-sided structure** — supplier side: "Upload documents once and share the information across multiple clients"; "Ensure that your company stays on your customers' approved vendor list by gaining visibility into their expectations… monitoring expiry dates and renewal processes"; OCR-assisted PQF completion; supplier-side product literally named "Subcontractor management": "Find and manage subcontractors while ensuring they comply with client requirements" — i.e., a subcontractor that itself subcontracts uses the same machinery downward. (A — fetched)
- **Scope beyond construction** — hiring clients include industrial/energy/facilities operators; risk domains span health & safety, financial viability, diversity, workforce risk, cyber; regional schemes (e.g., Tōtika in New Zealand). (A — fetched)
- Positioning: subcontractor management = extending the client's compliance program to lower tiers of the contracted-work population. (A)

## Product E — HammerTech (EHS-centric contractor management)

### Key observations

- **Employers tab as the population** — "Within the 'Employers' tab in HammerTech, you can easily add new subcontractors, who will then be sent a welcome email." Per-subcontractor information: "the subcontractor's name, whether they are active within your account, how many and which projects they are active on, their address, insurance information, and any additional prequalification questions you add related to general safety statistics." (A — fetched)
- **Self-service compliance** — "Subcontractors can use self-service portals to upload insurance certificates, safety documents, and worker information directly"; "Stop chasing paperwork and put documentation in subcontractors' hands"; configurable templates "to ensure consistency across all projects". (A — fetched)
- **Cross-project compliance dashboard** — "a centralized dashboard where you can view subcontractor compliance across all active projects. Easily track insurance, safety documentation, and approval status in real time"; "tracking document expiration dates and highlighting gaps in coverage or missing information". (A — fetched)
- **Engagement = active projects + site readiness** — engagement is expressed as which projects the sub is active on, plus worker-level onboarding (orientations/inductions, JHAs/RAMS, site access). Unlimited subcontractor access without per-seat fees. (A — fetched)
- **Subcontractor-side value proposition** — "Your safety record determines which GCs want to work with you and which projects you can bid on"; "Stand out in prequalification with comprehensive safety data". (A — fetched)
- Positioning: subcontractor management is the "Mobilize" phase of a safety platform — before preconstruction kickoff, ensuring every company and worker is compliant and ready. (A — fetched)

## Cross-product Comparison

| Dimension | Procore | Buildertrend | Buildxact | Avetta | HammerTech |
|---|---|---|---|---|---|
| Unit of record | company (Directory) + prequal form | Sub/Vendor profile | contact (supplier/sub) | company in network | employer (company) |
| Population scope | GC's collaborators across projects | builder's subs & vendors | builder's labor/supplier network | hiring client's contractor+sub tiers | GC's employers across projects |
| Fitness state | prequal form + review + status; insurance on company record w/ expiry | insurance + agreements w/ expiry notifications | (not evidenced) | PQF + docs + verification service + performance indicators | insurance + safety docs + prequal questions w/ expiry + approval status |
| Data supplied by subcontractor | yes — Prequalification Portal | yes — Sub Portal | yes — quote response link | yes — supplier platform | yes — self-service portals |
| Hiring-side review/verification | review, comment, change request, prequalify decision | storage + notifications (light review) | quote comparison + winner pick | specialist verification service | required fields + approval status + gap highlighting |
| Engagement linkage | company→project; bidder info; Bidding integration | sub→job; schedule items; warranty appointments | contact→schedule tasks; RFQs per estimate/job | sub invited/engaged for projects; site programs | sub active on projects; worker onboarding per project |
| Bid/RFQ solicitation | Bidding integration; bidder info | bid packages (create/compare/send/store) | RFQs (core of the product) | discover/invite/connect | not evidenced |
| Money machinery | (lives in Commitments/Pay — sibling modules) | POs, lien waivers, Bill Pay, invoices | winning quote→PO; budget | not evidenced | not evidenced |
| Performance evaluation | pre-award evaluation focus | not evidenced | not evidenced | performance indicators, analytics | compliance scoring (segment page) |
| Worker-level data | (Resource Planning — sibling) | not evidenced | not evidenced | worker level in analytics | deep (orientations, certs) — labor-adjacent |
| Subcontractor-facing surface | Prequalification Portal (Read-Only default) | Sub Portal + mobile app | quote-response link, free account | supplier platform | self-service portals, QR, no-login workers |
| Tier-N subcontracting | not evidenced | not evidenced | not evidenced | yes — supplier-side product | not evidenced |
| Network/sourcing | Procore Construction Network | not evidenced | not evidenced | network sourcing | not evidenced |

### Cross-product findings (evidence layers)

**Layer B (cross-product commonality, 4–5 of 5):**

1. The subcontractor is held as a **company record** in a hiring-organization-owned directory (5/5).
2. A **fitness-to-work state** is maintained per company — qualification questionnaires, insurance/licensing documents with expiry, safety performance — and kept current (4/5 direct; Buildxact not evidenced).
3. The fitness data is **supplied by the subcontractor itself** and **reviewed/verified by the hiring side** — a two-sided data-maintenance structure across the organizational boundary (5/5).
4. **Engagement linkage**: each company is linked to the projects/work it is engaged on, visible per company and per project (5/5).
5. **Expiry-driven renewal**: documents carry expiry dates and the system surfaces expiring/gap states (4/5).
6. **Subcontractor-facing surface** with limited external permissions (5/5; portal form varies).
7. **Bid/RFQ solicitation to subcontractors** as an engagement mechanism (4/5; absent in the EHS-centric pole).

**Layer A (single-product, held product-specific):**

- Verification-as-a-service by the platform's own specialists (Avetta).
- Tier-N subcontracting (a sub manages its own subs against client requirements) (Avetta supplier-side product).
- Network sourcing of new subcontractors (Avetta, Procore Construction Network).
- Unlimited free subcontractor access (HammerTech).
- Financials as a restricted prequalification category (Procore).
- Lien-waiver sign-off tracking on the sub relationship (Buildertrend).
- Freemium response accounts for subcontractors (Buildxact).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **The subcontractor company population of record.** External companies engaged to perform contracted construction work, held as persistent identified records (identity, trade/specialty, contact, active status) in the hiring organization's own directory. Remove → a generic contact list; the Type loses its subject.

2. **The fitness-to-work state maintained per company.** The hiring organization's current judgment of each subcontractor's qualification and compliance — prequalification questionnaires, insurance certificates/licenses with expiry, safety performance — fed by the subcontractor's own submissions and reviewed/verified by the hiring side, kept current through expiry-driven renewal. Remove → an address book; keep only the hiring-side assessment without the subcontractor's own submission → third-party-risk assessment territory.

3. **The engagement linkage between companies and work.** Each subcontractor is linked to the projects/work it is engaged on — invited to bid, awarded, scheduled, active on site — with engagement state visible per company and per project, and outcomes (performance, incidents, payment standing) recorded back onto the company record. Remove → a vendor registry with no work relationship, or project scheduling with no company population.

Jointly-held load-bearing:

- 1 alone = contact list
- 2 alone = prequalification/compliance database (third-party risk territory)
- 3 alone = project commitments/scheduling
- 1+2 without 3 = qualified-vendor database with no work linkage
- 1+3 without 2 = directory + assignments with no fitness gate
- 2+3 without 1 = per-project compliance tracking with no standing population

### L1 — Common Mature Structure

- Prequalification questionnaires with configurable forms, custom questions, review/comment/change-request loops, and qualification decisions (3/5 direct).
- Insurance/licensing certificate tracking with expiry notifications and gap highlighting (4/5).
- Bid/RFQ solicitation to subcontractors with response tracking and comparison (4/5).
- Scheduling assignment of subcontractors to work items (2/5 direct; implied in suite poles).
- Subcontractor-facing portal/app with limited external permissions (5/5).
- Cross-project compliance dashboards and status roll-ups (3/5).
- Performance evaluation / scorecards / safety indicators (2/5 direct).
- Money status on the relationship (POs, invoices, lien waivers, payment standing) (2/5 direct; in suite products it lives in sibling modules).
- Communication hub between hiring org and subs (2/5 direct; implied elsewhere).

### L2 — Variant / Optional Structure

- Operator posture: GC-side vs owner/hiring-client-side vs residential builder vs the subcontractor itself (tier-N).
- Fitness regime formality: formal gated prequalification workflow vs lightweight document storage vs specialist-verified compliance.
- Network sourcing (discover new subs from a shared network) vs closed private directories.
- Worker-level depth (inductions, certifications, site access) — deep in EHS-centric poles, absent elsewhere.
- Money machinery depth: from payment status visibility to full PO/invoice/lien-waiver handling.
- Regional compliance schemes and regulatory prequalification standards.
- Engagement grain: project membership vs schedule-task assignment vs site/facility approval.

### L3 — Vendor-specific Detail (research notes only)

- Procore: Prequalifications/Prequalification Portal as separate tools with permission tables; Directory insurance records with "Additional Insured" field; Insurance Manager designation; Procore Construction Network company saving; Bidding + COMPASS integration; Financials as restricted prequal category; Procore Pay company association.
- Buildertrend: Sub/Vendor as one record type; Permission Wizard; default non-customizable external permissions; Warranty appointment assignment; Bill Pay + AI Bill Capture; bid package notifications.
- Buildxact: RFQ per trade/line; yes/no/yes-later interest states; reopen-and-resubmit until winner picked; enter-reply-on-behalf; freemium sub accounts; unique quote numbers per project; winner→estimate price update.
- Avetta: verification specialists; OCR PQF population; network size claim; Tōtika NZ scheme; FMCSA motor carrier data; supplier-side "upload once, share across clients"; AskAva AI assistant.
- HammerTech: "Employers" tab naming; welcome-email onboarding workflow; QR-code no-login worker participation; unlimited-access pricing posture; "Mobilize" phase framing.

### Anti-overfitting notes

- The subcontractor **portal** is not definitional: it is the modern realization of the two-sided data structure. A paper-era GC receiving certificates and quotes by mail and filing them satisfies the same structure.
- **Prequalification questionnaires** are the dominant realization of the fitness leg but not the leg itself — document-and-expiry tracking without questionnaires (Buildertrend) still qualifies.
- **Money machinery** is not definitional: suite products realize it in sibling modules (commitments/billing); the EHS/compliance poles omit it entirely.
- **Scheduling** is a realization of the engagement leg, not the leg itself.
- **Safety content** is dominant in some poles but the fitness leg is domain-neutral in structure (financial viability, diversity, cyber risk also appear as fitness content in the owner-side pole).

### Historical / market-sample check

- Paper-era practice: a GC's card file of subcontractors organized by trade, a filing cabinet of insurance certificates with expiry dates, a bid list per project, a subcontract log, and handwritten performance notes — satisfies all three L0 structures with no modern machinery. Passes.
- Public-agency prequalified-bidder lists (regional/regulatory variant): a standing list of qualified contractors eligible to bid — population + fitness state + engagement (bid eligibility). Passes.
- Owner-side contractor management in industrial/energy (the Avetta pole) predates modern construction SaaS and satisfies the same structure with site/facility-level engagement. Passes.
- The check confirms the L0 must not include: portals, questionnaires, cloud delivery, network sourcing, or any specific document type beyond "fitness evidence maintained current".

## Vendor-specific Findings

See L3 above. None of these enter the canonical core.

## Rejected Findings

- "Subcontractor management = prequalification" — rejected: two of five samples carry no formal prequalification workflow; the fitness leg is broader than its questionnaire realization.
- "Subcontractor management = bid management" — rejected: solicitation is one engagement mechanism; the EHS-centric pole manages subs with no bidding at all.
- "Subcontractor management = vendor management (generic)" — rejected as an identity claim: the construction realization is anchored in contracted work on projects (site presence, safety, progress payment), not in procurement transactions for goods/services. The generic supplier-management Type remains a distinct neighbor.
- "Subcontractor management = labor management" — rejected: different record grain (company vs person). Products that span both (HammerTech, Avetta) keep the two populations distinct (employers vs workers).
- "The subcontractor portal is the defining structure" — rejected by the historical check; the two-sided data responsibility is the invariant, the portal is its current surface.
- "Payment/lien machinery is definitional" — rejected: absent from the compliance poles; owned by sibling Types in suites.

## Boundary Findings

1. **vs Preconstruction Management** — precon centers on the pursuit (a prospective undertaking) with solicitation→leveling→award and handoff to execution; Subcontractor Management centers on the standing company population and its fitness + engagement across the whole relationship. Prequalification appears in both: as pursuit-scoped supply-chain solicitation in precon, as company-level fitness state here. Remove test: strip the pursuit record + award handoff → subcontractor management remains; strip the standing population + fitness state → precon remains.
2. **vs Construction Bidding Platform** — the multi-party solicitation venue (bid boards, ITB distribution, sub-side bid tracking) vs the hiring organization's population management. RFQ machinery here is one engagement mechanism, not the venue.
3. **vs Construction Cost Management** — cost management owns the money objects (commitments with SOV, invoices, retainage); this Type holds the relationship view (who is engaged, fit, scheduled, performing). Money appears here as status on the relationship, not as the cost baseline.
4. **vs Construction Labor Management** — record grain: companies (this Type) vs individual workers (labor management). EHS-centric products span both; the seam is the grain and the center (employer fitness vs worker readiness/placement).
5. **vs Supplier Management Platform (§10)** — procurement-side supplier lifecycle for goods/services enterprise-wide vs construction subcontracted work on projects with site/safety/progress-payment semantics. The owner-side compliance pole (Avetta) straddles: it is marketed as contractor/supplier management but its subcontractor-management extension carries the same population+fitness+engagement structure. Recorded as a straddle, not a merge.
6. **vs Third-party Risk Management (§11)** — TPRM assesses risk across all third parties; this Type operationally manages the contracted-work relationship. The fitness leg overlaps TPRM's assessment; the engagement leg and the subcontractor's own participation distinguish.
7. **vs Vendor Management System / VMS (§09)** — VMS manages contingent staffing (people placed through suppliers); here the unit is the contracted company performing work. Different grain, different object.
8. **vs Government Vendor Management (§24)** — industry-shaped analog (public-agency vendor/prequalification programs); same structure, different regime.
9. **vs Manufacturing Supplier Collaboration (§16)** — industry sibling (manufacturing supply chain vs construction subcontracting).
10. **vs Construction Safety Management** — safety management owns the event/finding register; this Type owns the company fitness state. Linked via employer attribution on safety records; the safety register's existence is not this Type's center.

**Remove test for the Type as a whole:** strip the fitness state → a directory plus work assignment (not this Type's center); strip the engagement linkage → a prequalification/compliance database (third-party-risk-shaped); strip the company population → scattered per-project records with no standing relationship. All three legs are jointly required.

## Uncertainties

- Buildertrend and Buildxact evidence rests on marketing pages plus search-surfaced help content; operational details (exact permission models, exact status vocabularies) were not verified from Tier-1 manuals. No precise claims from these two enter the final document.
- Avetta and HammerTech documentation is Tier-2; the exact mechanics of their approval states and verification workflows are not documented publicly. Claims held at marketing strength.
- Procore's ongoing (post-award) performance evaluation of subcontractors was not evidenced this pass — the sampled evidence covers pre-award evaluation; ongoing scorecards may exist in other Procore tools but were not fetched.
- The relative market weight of the owner-side compliance-network pole vs the GC-side suite pole could not be quantified from public sources; both are treated as first-class poles.
- Whether public-agency prequalification systems (DOT-style) are served by the same commercial products could not be confirmed; the historical/regional check treats them as a class-level variant only.

## Final Synthesis

Subcontractor Management is the **hiring organization's system of record for its subcontractor population**: the external companies it engages to perform contracted construction work. Its defining structure is three jointly-held legs — the company population of record, the fitness-to-work state maintained per company (subcontractor-supplied, hiring-side reviewed, expiry-driven), and the engagement linkage between companies and the work they perform — with the subcontractor participating as a limited external party that supplies and maintains its own data. Bid solicitation, scheduling assignment, money status, performance evaluation, portals, networks, and worker-level onboarding are common mature capabilities or variants, not the definition. The Type is distinct from preconstruction (pursuit-centered), bidding (venue-centered), cost (money-centered), labor (person-centered), and from cross-industry supplier management, VMS, and third-party risk by its grain (company), its anchor (contracted work on projects), and its two-sided data structure.
