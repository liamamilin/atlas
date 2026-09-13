# Research Notes — Government Vendor Management

## Research Goal

Understand what "Government Vendor Management" actually is as an Application Type: what object sits at the center (the vendor record?), what lifecycle the vendor's standing follows, what qualification/compliance machinery attaches to the record over time, who operates it and who uses it, and — above all — how it differs from (a) the Government Procurement Platform (the solicitation cycle), (b) corporate Supplier Management, and (c) the Vendor Management System (contingent labor) whose name collides.

## Initial Boundary

Working hypothesis at start:

- The Type is the government side's system of record for its **vendor population as a standing eligible class**: registration, verification/qualification, compliance documents, standing status (active / lapsed / declined / suspended / excluded), maintained over time and independent of any single solicitation or contract.
- Nearest neighbors: Government Procurement Platform (§24 sibling, processed — which explicitly flagged this leaf), Supplier Management Platform / Supplier Portal (§10 corporate), Vendor Management System / Contingent Workforce Management (§09 — name collision, different thing), Government Grants Management (§24, processed — buy-vs-give), Sanctions Screening (§15), Government Digital Identity (§24 — citizen, not vendor), Accreditation/Certification Management (§25 — certifying-body machinery overlap).
- Prior-pass flag to discharge: government-procurement-platform recorded — "vendor registration, document verification, classifications and performance signals appear inside procurement platforms; that leaf should center on the ongoing vendor relationship (qualification/performance/compliance over time) rather than the solicitation cycle, or it risks aliasing with this Type — joint review recommended."

## Research Questions

1. What is the central object — the vendor/entity record? What does it carry?
2. What lifecycle does the vendor's standing follow (registration → review → active → maintenance → lapse/suspension/reinstatement)?
3. What qualification/evidence machinery exists (documents, declarations, levels, verification)?
4. What government-initiated status changes exist (decline, suspension, debarment/exclusion)? What are their terms and scopes?
5. How does the record connect to solicitations, awards, and payment — without collapsing into the procurement Type?
6. Who operates these systems (government bodies, UN bodies) and who uses them (procurement staff, program offices, finance, vendors themselves)?
7. Is the government qualifier load-bearing vs corporate supplier management?
8. Historical check: does the definition hold for the paper-era vendor file / bidders list / debarment register without software?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies (government-operated system of record vs shared supranational registry vs agency SaaS suite vs network platform), and different customer/geographic levels:

| Product | Pole | Level | Evidence tier reached |
|---|---|---|---|
| SAM.gov — Entity Registration & Exclusions (US GSA) | government-operated national system of record (entity registration + exclusion records) | US federal | Tier 1 (official pages + API documentation) |
| UNGM (United Nations Global Marketplace) | shared supranational vendor registry for 32 organizations | UN system / international | Tier 1 (official site, glossary, code of conduct) |
| Euna Procurement (Bonfire lineage) | agency-side SaaS suite — vendor registration & supplier management modules | NA local/state agencies, education, utilities | Tier 1 (dedicated help center) + Tier 2 (product page) |
| SOVRA (BidNet Direct / Periscope / Vendor Registry lineage) | local/state network platform + suite; supplier qualifications & network | NA local/state (US + Canada) | Tier 2 (product pages) |
| Vendor Registry (vendorregistry.com) | dedicated local-government vendor registration product (sunset — absorbed into SOVRA/Bidnet Direct) | US local government | Tier 2 (sunset notice documenting the category and its absorption) |

Rejected/abandoned samples (per network rules): CPARS (cpars.gov transport error ×2 — cpars.gov and www.cpars.gov), acquisition.gov/CPARS (403), help.ungm.org / ungm.org/Help (transport error + timeout), open.gsa.gov/api/exclusions (404 — correct path /api/exclusions-api/ worked).

## Sources

- SAM.gov — Entity Registration: https://sam.gov/content/entity-registration — fetched 2026-09-08
- SAM.gov Exclusions API (GSA Open Technology): https://open.gsa.gov/api/exclusions-api/ — fetched 2026-09-08
- UNGM homepage: https://www.ungm.org/ — fetched 2026-09-08
- UNGM Site Map: https://www.ungm.org/Public/SiteMap — fetched 2026-09-08
- UNGM Glossary: https://www.ungm.org/Shared/KnowledgeCenter/Pages/UNGMglossary — fetched 2026-09-08
- Euna Procurement Help Center — hub: https://procurement-help.eunasolutions.com/hc/en-us — fetched 2026-09-08
- Euna Procurement Help Center — Vendor Registration section: https://procurement-help.eunasolutions.com/hc/en-us/sections/48366912105235-Vendor-Registration — fetched 2026-09-08
- Euna Procurement Help Center — "Completing Registration Before Documentation Is Verified": https://procurement-help.eunasolutions.com/hc/en-us/articles/48855228986899-Completing-Registration-Before-Documentation-Is-Verified — fetched 2026-09-08
- SOVRA homepage: https://www.sovra.com — fetched 2026-09-08
- SOVRA Source + Network: https://www.sovra.com/government-buyers/solutions/procurement-management/source-network/ — fetched 2026-09-08
- Vendor Registry (sunset notice): https://vendorregistry.com — fetched 2026-09-08
- Prior-pass observations reused: research/government-procurement-platform.md (Euna product page: supplier performance monitoring, insurance/certification tracking; SAM.gov contracting-domain observations) — recorded 2026-09-08

## Product Observations

### SAM.gov — Entity Registration & Exclusions (US GSA) — Tier 1

Evidence layer: A (direct observation).

- **Entity Information is a distinct domain** of the federal award environment, separate from Contract Opportunities (the solicitation domain documented in the procurement pass). Entity Registration's own framing: "Register your entity or get a Unique Entity ID to get started doing business with the federal government."
- **Registration as eligibility gate**: "If you want to apply for federal awards as a prime awardee, you need a registration. A registration allows you to bid on government contracts and apply for federal assistance."
- **Tiered participation**: full registration (bid on contracts, apply for assistance) vs Unique Entity ID only ("If you only conduct certain types of transactions, such as reporting as a sub-awardee, you may not need to complete a registration… If you choose to only get a Unique Entity ID, you cannot apply directly for federal awards."). Standing has degrees.
- **UEI assigned during registration**; entity workspace; "Renew Entity"; "Check Entity Status" status tracker.
- **Renewal clock**: "You must renew your registration every 365 days to keep it active. You can make updates to your registration anytime or during renewal." (precise number = vendor fact, not canonical)
- **Status model & validation**: FAQ entries "What do the different registration statuses mean?", "Why isn't my registration active yet?", "What happens if my registration fails validation?"; "Registration can take up to 10 business days to become active" (vendor fact).
- **Registration data volume**: "For registration, you are required to enter a lot of information about your entity" — checklists/questionnaires; NAICS classification linked (resources: NAICS, SBA Dynamic Small Business Search).
- **Exclusion records (Exclusions API, entity-information domain)** — the federal ineligibility machinery, publicly searchable and machine-readable:
  - Record identity: classification Type (Individual / Firm / Vessel / Special Entity Designation), UEI, CAGE code, NPI, name, addresses, cross-references and "moreLocations" (related entities).
  - exclusionType: "Ineligible (Proceedings Pending)", "Ineligible (Proceedings Completed)", "Prohibition/Restriction", "Voluntary Exclusion".
  - exclusionProgram: "Reciprocal", "NonProcurement", "Procurement" — scope of the exclusion's effect.
  - excludingAgencyCode/Name — the agency that imposed it.
  - Actions lifecycle: createDate, activateDate, terminationDate, terminationType ("Definite" / "Indefinite"), recordStatus ("Active" — only Active records returned). Exclusions therefore have activation and termination semantics — suspension/debarment with defined or indefinite terms.
  - FASCSA order flag; additional comments; public CSV/JSON extracts; rate-limited public API.
- Interpretation: the same system that holds active vendor registrations also holds the government's formal ineligibility records, with both carrying lifecycle dates and statuses. The registry is simultaneously the enablement list and the exclusion list.

### UNGM (United Nations Global Marketplace) — Tier 1

Evidence layer: A.

- **One registry, many organizations**: "Register only once to have access to up to 32 organizations"; UN organizations get "a database of more than 500,000 suppliers and individual consultants" (vendor-published figure); UN staff uses listed as: publish opportunities/awards, "Perform due diligence, ensure suppliers are not on sanction lists", share LTAs.
- **Vendor classes**: Company (supplier), Individual consultant ("individual with a specific expertise who provides services… other than as an employee"), Implementing partner (NGO "engaged to carry out technical, development, or humanitarian work with, or on behalf of, a UN agency"). The supplier-vs-implementing-partner split is in-product evidence of the vendor-vs-grantee seam.
- **Terminology**: glossary defines Supplier with alternative terms "Vendor, Company, Business, Business entity" and states "The terms 'supplier' and 'vendor' are considered equivalent and used interchangeably."
- **Registration levels** (glossary):
  - Basic (common level; profile visible to all UN procurement officers "when sourcing for potential suppliers" and in most cases sufficient to participate).
  - Level 1: certificate of incorporation, three references, ownership structure.
  - Level 2: audited financial documents for the last three years, three reference letters.
- **Registration statuses** (glossary; evaluation conducted by UN organizations):
  - "In progress" — being reviewed; form locked.
  - "Submitted" — received; for Levels 1–2 stays Submitted (evaluated as part of tendering).
  - "Registered" — "evaluated and approved… The supplier's profile is now visible to UN staff members when sourcing for potential suppliers. **Registration does not imply pre-qualification.**"
  - "Resubmitted" — re-evaluation.
  - "Declined" — "registration has been declined based on the information provided… in the majority of cases… the supplier's products and/or services do not match those procured by the UN organizations."
  - "Vendor to update" — "reviewed and evaluated… some information is insufficient, incorrect, or obsolete… Once the registration has been amended, the registration needs to be manually re-submitted."
- **Record content classes** (glossary): Certificate of Incorporation; License number ("Business License number, Tax ID number, Official identification number, Fiscal number"); Financial statements; Reference / Reference letters; Ownership (legal form), Publicly-traded / Privately-owned, Parent company, Part of a business conglomerate; Geographical scope ("countries or areas of business"); Declaration of Eligibility ("formal and explicit statement that has to be made on behalf of the supplier").
- **Registry governance**: Duplicate account ("Suppliers are required to only maintain one UNGM account. Duplicate accounts must be deleted"; duplicate "under review" state); Edit/Delete as governed record actions; Activation (email verification) distinct from registration ("The creation of a user account on UNGM does not indicate registration on UNGM").
- **Classification & matching**: UNSPSC codes "used to classify suppliers' products and services on UNGM and to classify the products and services covered by procurement opportunities"; geographical scope; Autosubmissions ("authorizes UNGM to automatically submit my information to new UN organizations with matching registration requirements").
- **Qualification machinery adjacent to registration**: "Request for pre-qualification" defined ("formal method of assessing suppliers… against predetermined qualification criteria"); "Limited international competition" uses "a shortlist of qualified suppliers"; Supplier Code of Conduct is a standing public instrument.
- Account machinery: account creation ≠ registration; dashboard, UNGM number, primary contact, invited contacts, settings.

### Euna Procurement (Bonfire lineage) — agency SaaS suite — Tier 1 help center (+ prior-pass product page)

Evidence layer: A for help-center content; A for prior-pass product-page claims (marketing framing stripped).

- Help center has a dedicated **Vendors** category with a **Vendor Registration** section — registration is a first-class flow of the product: account creation, vendor documents upload during registration, commodity codes, vendor types, diversity certifications, document verification, registration cost (free), multi-portal question.
- **Document verification gate with government discretion**: "In the case where a Buyer requires that documentation needs to be verified, you can still complete your registration, as long as you provide all of the required documents… You can check on the verification status of your documents in the Settings tab. The verification status will be in your **Organization Vendor Record** under Documents. Please note that **it is up to the discretion of the purchasing organization to verify your documents**, however once you upload them, nothing further is required from you unless the purchaser notifies you later on."
  - Note the object name: **Organization Vendor Record** — the vendor record is the organizing object of the vendor-side half of the product.
  - Related article: "How do I update the documents on my vendor profile after registration?" — post-registration document maintenance is an expected flow.
- **Classification**: "Do I have to enter Commodity Codes when I register for a Vendor account?", "How do I know which commodity code(s) to use?" — commodity codes drive opportunity matching; **Vendor Types** ("How do I edit my Vendor Type(s)?", "How do I complete registration if I don't fall under one of the Vendor types?").
- **Diversity/classification certifications**: "What is the HUB/SWMBE Certification?" — self-identification classes attached to the vendor record (prior pass: DBE self-identification).
- **Multi-portal reality**: "Do I need to register with multiple Euna Procurement portals?" — one vendor maintains registrations on many buyer deployments (prior pass recorded the same finding).
- **Roles**: Vendor, Buyer, Reviewer, Advisor, Observer, Requestor (prior pass) — vendor is a distinct role class from government-side roles.
- From the prior pass (product page): supplier performance monitoring (surveys, scores in the contract record), insurance certificates and certifications tracked in contract records; vendor documents gate opportunity access; registration self-service and free.
- Interpretation: inside the suite, the vendor record + its document/verification state is a distinct working surface from the solicitation project; the suite vendors bundle both, which is exactly the flag the procurement pass raised.

### SOVRA (local/state network + suite) — Tier 2

Evidence layer: A for page claims; structure treated as B (marketing framing).

- Positioning: "Connecting the Ecosystem That Powers Public Procurement… SOVRA powers both sides." Claims: "1 Million active vendors with public service experience", "7,000 public entities using our solutions daily", "$22 Billion solicitations awarded in 2025" (all vendor-claimed figures).
- **Supplier qualifications named as a buyer-side capability**: "Supplier Qualifications: Manage certifications and pre-qualifications" — listed beside solicitation machinery, not inside it.
- **Supplier network as standing population**: "Network: Connect to over 1M+ suppliers"; "10,000+ New Suppliers added every month"; "Free Access for Suppliers to solicitations from 7000+ agencies"; "Bid Alerts: Automate supplier notifications using commodity codes"; "Audit History: Capture who touches what and when".
- Suite around it: Intake, Solicitation Builder, Evaluation (sealed-bid enforcement), Contract — the procurement side is bundled; the vendor population is the connective asset.
- **Vendor Registry lineage**: vendorregistry.com is a sunset page — "We're no longer accepting new purchasers on our platform. Discover our SOVRA solutions… We're no longer accepting new vendors… Find opportunities on Bidnet Direct." The page header still reads "Government Procurement Solutions + **Bid & Vendor Management**" — evidence that (a) standalone local-government vendor registration/bid management was a viable product category, and (b) it has been absorbed into network-platform suites.

## Cross-product Comparison

| Structure | SAM.gov | UNGM | Euna | SOVRA (+ Vendor Registry lineage) | Reading |
|---|---|---|---|---|---|
| Persistent identified vendor/entity record as the supply side | ✔ (entity registration, UEI, workspace) | ✔ (registration, UNGM number, profile) | ✔ (Organization Vendor Record) | ✔ (network supplier accounts; VR registration) | L0 |
| Vendor-submitted information the standing is judged on (identity, classifications, documents, declarations) | ✔ ("a lot of information about your entity", NAICS, checklists) | ✔ (levels 1/2 docs, declarations, ownership, financials) | ✔ (vendor documents, commodity codes, vendor types, HUB/SWMBE) | ✔ (qualifications, certifications) | L0 (as record content class; depth varies) |
| Government-controlled standing with entry gate + evaluated status | ✔ (statuses, validation, UEI-only vs full) | ✔ (In progress/Submitted/Registered/Vendor-to-update/Declined; UN-org evaluation) | ✔ (verification at buyer discretion; registered vendor role) | ◐ (qualification management; network admission) | L0 |
| Government-initiated adverse status change (decline/suspension/exclusion) | ✔ (exclusion records: types, programs, terms) | ✔ (Declined status; sanction screening/due diligence) | — (not evidenced in help center) | — | L1 (strong in government-operated registries) |
| Renewal / currency cycle over time | ✔ (renew every 365 days to stay active) | ◐ (Vendor-to-update for "obsolete" info; resubmission) | ✔ (post-registration document updates; insurance certs tracked per prior pass) | ◐ | L1 (near-universal in modern products; minimal registry can omit) |
| Classification/matching codes (NAICS/UNSPSC/commodity codes) | ✔ (NAICS) | ✔ (UNSPSC) | ✔ (commodity codes) | ✔ (commodity-code bid alerts) | L1 |
| Search/visibility of the population for sourcing | ✔ (searchable registrations; DSBS linkage) | ✔ (profile visible to UN staff when sourcing) | ✔ (vendor network broadcast) | ✔ (network) | L1 |
| One-record governance (duplicates, cross-portal fragmentation) | ◐ (UEI deduplication implied by UEI concept) | ✔ (duplicate account rules) | ✔ (multi-portal question; one record per portal) | ✔ (single network claim) | L1 |
| Performance evaluation of vendors | ✘ (not in entity domain) | ✘ | ✔ (prior pass: surveys/scores in contract record) | ✘ | L1/L2 (weak evidence; CPARS unreachable) |
| Public accountability surface (public exclusion search, open data) | ✔ (public Exclusions API, CSV/JSON) | ◐ (public opportunities/awards; profiles internal) | — | — | L1 |
| Solicitation/response/award machinery | separate domain | present (opportunities) | bundled (suite) | bundled (suite) | NOT this Type's center — procurement Type |

Key comparative findings:

1. **The vendor record as a standing object is present in every sampled product**, including where it lives inside a procurement suite — Euna's own help content names the "Organization Vendor Record" as the container of registration state. Evidence layer B.
2. **The standing/status model with a government-controlled gate is universal**: every product has an evaluated state the vendor cannot grant itself. Status vocabularies differ (SAM statuses/Active; UNGM In progress→Registered/Declined/Vendor-to-update; Euna verification pending/complete). Evidence layer B; canonical status set described conceptually only.
3. **Evidence content depth varies enormously** — from SAM's "a lot of information" + NAICS to UNGM's three-level document escalation to Euna's buyer-discretionary verification — but the *class* (vendor-submitted identity/qualification/declaration information on the record) is universal. Evidence layer B.
4. **Exclusion/debarment machinery is strong where government operates the registry** (SAM exclusion records with program scope and definite/indefinite terms; UNGM sanction screening + Declined) and not documented in the agency-suite samples' help content. Common, not defining. Evidence layer A×2 / absent×2 → L1.
5. **Renewal/currency machinery is near-universal but varies**: explicit annual renewal (SAM), obsolete-info resubmission (UNGM), ongoing document updates (Euna). A minimal approved-list registry could exist without expiry clocks, so currency machinery is common mature structure, not the defining core. Evidence layer B.
6. **Performance evaluation is the weakest leg** (Euna only in-sample; CPARS unreachable). Must not enter the defining core; recorded with reduced assertion strength. Evidence layer A×1 → product-supported, L1/L2.
7. **The procurement cycle is present in most sampled systems but is not the center here**: UNGM/Euna/SOVRA bundle solicitations; SAM.gov separates the domains (Entity Information vs Contract Opportunities). The seam is center-of-gravity: vendor population & standing vs solicitation cycle. Evidence layer B + boundary reasoning.
8. Terminology: vendor/supplier equivalence is documented in-product (UNGM glossary); "vendor management" in this Type means administration of the vendor population, not contingent-labor VMS. Evidence layer A.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

A government vendor management application is the government buyer's registry of its vendor population as a standing eligible class. Two structures held jointly:

1. **The vendor record of record** — a persistent, individually identified record for each external organization (or eligible individual) that does or may sell to the government body, carrying vendor-submitted information the government judges eligibility on: legal identity and identifiers, classifications (what they sell), contacts, ownership/financial standing as required, evidence documents, and eligibility declarations. The record outlives any single solicitation, contract, or payment. Remove → a notice board or lead list.
2. **Governed eligibility standing** — the record carries a standing state that only the government body can confer or change: an entry gate (submission → review/verification/validation → approved/registered or declined), in-course changes (updates demanded, amendment → resubmission), and government-initiated adverse changes for cause (decline, suspension, exclusion/debarment — optionally with defined terms and scopes) or lifecycle lapse (unmaintained/expired). The standing is what determines whether the vendor may participate, be awarded, or be paid. Remove → a directory/CRM with self-serve profiles, or a document drop.

Jointly-held is load-bearing: records without governed standing = contact directory; standing without records-as-evidence-base = an approval stamp with nothing behind it. The frame: the object of management is the **population's eligibility over time**, not any transaction — which is the seam against the procurement Type.

### L1 — Common Mature Structure

- Classification & matching: commodity/industry codes (NAICS, UNSPSC, commodity codes) on the record, used to match vendors to opportunities and route notifications.
- Renewal/currency machinery: expiry clocks and renewal obligations, obsolete-information flags, scheduled re-verification of documents.
- Exclusion/ineligibility records as first-class registry content (type, imposing agency, program scope, activation/termination, definite/indefinite term), searchable/extractable; sanction screening during due diligence.
- Searchable population for sourcing officials; visibility rules (which officials/staff can see profiles; sometimes public surfaces for exclusions and award data).
- Vendor self-service portal: register, maintain profile, upload/update documents, track verification/status, receive notifications.
- One-record governance: duplicate detection, multi-portal fragmentation handling, record activation vs registration distinction.
- Performance evaluation signals attached to the record (evaluations, scores, past-performance reuse) — product-supported in-sample only; weaker evidence.
- Diversity/small-business classifications and program certifications on the record.
- Integrations feeding the record into solicitations, contracts, and payment systems (vendor-master role).

### L2 — Variant / Optional Structure

- Tiered registration levels with escalating evidence requirements (UNGM Basic/1/2; SAM UEI-only vs full registration).
- Multi-organization shared registry (register once, serve many agencies/organizations; auto-submission to new organizations).
- Vendor classes beyond companies: individual consultants, implementing partners (UN).
- Program-certification management for vendor status classes (HUB/SWMBE/DBE self-ID; small-business data) — deep certification-authority machinery straddles toward Accreditation/Certification Management (not directly sampled).
- Performance-evaluation-centric registry (federal past-performance assessment systems — CPARS class; unreachable this pass, unverified).
- Public accountability extensions: public exclusion search, open-data extracts, transparency feeds.
- Payment/vendor-master integration depth (invoicing modules, AP handoff).

### L3 — Vendor-specific (Research Notes only)

- SAM.gov: UEI (12-char), CAGE code, NPI fields; exclusionType vocabulary ("Ineligible (Proceedings Pending/Completed)", "Prohibition/Restriction", "Voluntary Exclusion"); exclusionProgram (Reciprocal/NonProcurement/Procurement); FASCSA order flag; terminationType Definite/Indefinite; 365-day renewal; "up to 10 business days" activation; API rate limits; Login.gov identity; D&B data disclaimer; FPDS award-data linkage (prior pass).
- UNGM: 32 organizations; 500,000+ supplier database (vendor figure); Basic/Level 1/Level 2 requirements; status vocabulary; Autosubmissions; UNGM number; Tender Alert Service subscription; Pro-forma invoice for TAS; ASR statistics.
- Euna: "Organization Vendor Record" object name; Settings→Documents verification status location; HUB/SWMBE article; IonWave/EqualLevel/DemandStar lineage (prior pass).
- SOVRA: 1M+ suppliers claim; 10,000+/month new suppliers; 24-second support response claim; 5.5M+ solicitation library claim; Bidnet Direct/Merx/Ontopical product lines; "0x More Responses" typo on page.
- Vendor Registry: sunset notice text; Bidnet Direct redirection; mdf commerce privacy footer.

## Vendor-specific Findings

See L3. None promoted to the canonical model. The 365-day renewal and 10-business-day activation numbers are recorded as vendor facts and deliberately kept out of the final document.

## Boundary Findings

- **vs Government Procurement Platform (§24, processed — flag DISCHARGED from this side)**: the procurement Type's center is the solicitation → controlled response → recorded/published award cycle; this Type's center is the standing vendor population and its eligibility over time. Registration exists in both, but in procurement platforms it is onboarding-to-bid (a supporting state of the solicitation machine); here it is the organizing object. Remove solicitation/response/award machinery and keep vendor records + standing + qualification → still a complete, marketable product of this Type (SAM.gov's Entity Information domain, UNGM registration, the standalone Vendor Registry lineage). Remove the vendor record and keep the cycle → notice board with an inbox. Keep-both ratified; center-of-gravity test recorded for joint reference.
- **vs Supplier Management Platform / Supplier Portal (§10, corporate)**: the machinery (supplier lifecycle: onboarding, qualification, documents, performance, risk) is shared; the government qualifier shapes it — eligibility standing carries public-law consequences (exclusion/debarment records, award eligibility), registries are often government-operated systems of record, and status surfaces are subject to public accountability (public exclusion search, open data). Same-vendor-different-suite-configuration pattern as ratified for procurement. Keep-both; corporate pass should treat this research as counterparty when processed.
- **vs Vendor Management System / VMS (§09)**: name collision only — VMS manages contingent *labor* procurement (staffing suppliers, work orders, time & billing); no registration/eligibility registry of a general vendor population. Different Type; recorded prominently because "vendor management" vocabulary invites confusion.
- **vs Government Grants Management (§24, processed)**: buy-vs-give seam confirmed in-product — UNGM registers "implementing partners" (NGOs carrying out work on behalf of a UN agency) as a class distinct from suppliers; grants pass recorded the give-vs-buy boundary and the "award" vocabulary collision. A vendor record enables purchase; a recipient record receives funds for public purpose.
- **vs Sanctions Screening Platform (§15)**: screening tools check parties against external lists; this Type holds the government's *own* vendor standing records, including the exclusion records the government itself produces (SAM exclusion records carry the excluding agency). A screening tool may consume this registry's exclusions.
- **vs Government Digital Identity (§24)**: identity of citizens/businesses for authentication vs eligibility records for commerce. Adjacent infrastructure, different object.
- **vs Accreditation / Certification Management (§25)**: programs that *certify* vendor status (diversity certifications, small-business status) run certifying-body machinery that straddles the two Types; the registry here records/references such certifications as record attributes. Not directly sampled (certification-authority pole unreachable); flagged as variant overlap.
- **vs Third-party Risk Management / Supplier Risk (§10/§15)**: risk-specific monitoring vs the whole-population registry. Risk assessments may attach to vendor records as one signal class.

## Uncertainties

- **Performance pole unverified**: CPARS (cpars.gov, www.cpars.gov) and acquisition.gov/CPARS unreachable (transport errors ×2; 403). Federal past-performance assessment machinery is asserted only via Euna's supplier-performance monitoring (single product) — kept at L1/L2 with reduced wording; no evaluation-cycle details (periods, rating scales, reuse rules) are claimed anywhere.
- **Renewal generalization risk**: only SAM.gov documents an explicit renewal clock (365 days, vendor fact). UNGM shows obsolete-info resubmission; Euna shows document updates. The final document states currency maintenance as common structure without universal periods.
- **Decline/suspension criteria** beyond UNGM's documented mismatch reason and SAM's exclusion types are not documented; criteria vary by regime — not asserted.
- **Payment linkage**: registration as precondition to receive/pay federal awards is structurally implied (SAM: registration allows applying for awards) but payment-execution integration was not observed; the vendor-master role is described structurally only.
- **Other national models** (e.g., GeM India vendor side, EU ESPD-based national registries) not sampled; the two-operated-registries + two-suite-vendor sample covers poles but not every regime.
- **Public-visibility posture varies** (SAM exclusions public; UNGM profiles staff-visible; agency suites vary) — recorded as variant axis, not canonical.

## Historical / Market-Sample Check

Paper-era analogues satisfy the two L0 structures without software: the purchasing department's **vendor file** (per-vendor folder with W-9/tax forms, insurance certificates, references, correspondence); the **bidders/plan-holders list** maintained and pruned by the purchasing office; **responsibility determinations** recorded per vendor; **debarment lists** published in official registers/gazettes with stated causes and terms; **renewal chasing** of expiring certificates by clerks. Regional variance (US bidders lists, UN rosters, national registries) does not change the structure. Modern products digitize each element: vendor file → Organization Vendor Record/entity registration; bidders list → searchable classified population; debarment register → exclusion records with activation/termination; certificate chasing → expiry/renewal machinery. The definition does not over-fit the current SaaS generation. Passed.

## Final Synthesis

Government Vendor Management is the government's registry of its vendor population as a standing eligible class. Its world has exactly two load-bearing structures held jointly: the vendor record of record (persistent, identified, carrying the vendor-submitted information eligibility is judged on — identity, classifications, documents, declarations) and governed eligibility standing (a state only the government can confer or change — entry review/verification, demanded amendments, decline, suspension/exclusion with terms and scopes, lapse — which gates participation, award, and payment). Everything else — classification matching, renewal clocks, exclusion records, performance signals, self-service portals, public extracts, tiered levels, multi-organization sharing — is mature machinery layered on that spine, varying by operator (government-operated national system, shared supranational registry, agency SaaS suite, network platform) and by regime. The Type is distinguished from the procurement platform by center of gravity (population standing vs solicitation cycle), from grants by buy-vs-give, and from corporate supplier management by the public-law character of the standing it governs.
