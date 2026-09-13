# Research Notes — Veterinary Practice Management

Research date: 2026-09-09
Slug: veterinary-practice-management
Directory location: §29 Home, Family, Personal & Local Services (siblings: Pet Grooming Management, Pet Boarding Management, Pet Daycare Management, Pet Care Business Management, Pet Adoption Platform, Animal Shelter Management, Pet Health Application, Pet DNA Analysis Platform, Salon Management System; cross-section neighbors: Practice Management System / EHR / Patient Scheduling §22, Livestock Management §20, Research Animal Facility Management §22)

## Research Goal

Understand what "Veterinary Practice Management" software actually is as an Application Type: who operates it, what core objects exist inside it, how the clinical-business loop of a veterinary practice (client/animal records → appointments → consultation and clinical documentation → billing) actually works, and where its boundary sits against the pet-service siblings (§29), Animal Shelter Management, and the human-healthcare practice-software family (§22).

Prior-pass context carried into this pass:

- pet-boarding-management (2026-09-09): "vs veterinary-practice-management — clinical business (appointments, procedures, medical records); boarding products store the veterinarian as a data field, never the clinical workflow."
- pet-care-business-management (2026-09-09): "vet is clinical care (medical records, diagnoses, prescriptions); a 'veterinarian' field here is a contact, not clinical functionality."
- animal-shelter-management (2026-09-09): "ASM additionally ships a separate Clinic module chapter (for shelters running public clinics) — the vendor itself separates the two structures. Flag for joint review when Veterinary Practice Management is processed."
- pet-dna-analysis-platform (2026-09-09): "the seam vs Veterinary Practice Management is caretaker-collected + risk-framing vs clinic-collected + clinical diagnosis."
- practice-management-system (§22 human analog, 2026-09-09): its family note separates the law/massage/immigration practice-management genus by "payer-claim machinery + clinical visit economy". Veterinary was not adjudicated in that pass.

## Initial Boundary

Working hypothesis before research:

1. Core use: the veterinary practice's own operator-side system of record — running appointments, medical records, and billing for a clinic where animals are treated but owned animals are billed to human clients.
2. Primary users: veterinarians, veterinary technicians/nurses, receptionists, practice managers/owners.
3. Nearest neighbors: human Practice Management System / EHR (§22 — same genus), Animal Shelter Management (custody-based care vs client-based clinical business), the pet-service siblings (non-clinical service businesses), Pet Health Application (owner-facing vs practice-facing).
4. Likely seam: the clinical layer (medical records, diagnoses, prescriptions/treatments) is what separates this Type from the non-clinical pet-service family; the client-account billing layer is what separates it from shelter/custody care.
5. Unknowns: is the clinical documentation layer definitional or merely common? How does the market merge/split the human PM/EHR pillars? Is the "PIMS" (Practice Information Management System) name a different Type or the market's name for the same thing? Do equine/production-animal practices share the same core?

## Research Questions

1. What are the core objects? (client, patient/animal, medical record, appointment, estimate/invoice, treatment plan, reminder, inventory…)
2. How does the two-level client↔patient ownership structure work (multiple animals per owner, care delivered to animals billed to owners)?
3. What does the consultation loop look like (SOAP-style documentation, diagnoses, prescriptions, charge capture)?
4. How does the estimate → treatment plan → invoice → payment flow work?
5. What happens with hospitalized/in-patients (whiteboards, treatment sheets, per-administration charging)?
6. What are the standard capabilities around scheduling, reminders/recalls, inventory, communications, portal/online booking, integrations (labs, imaging, payments, insurance)?
7. Which roles participate and what distinguishes them (vet vs tech vs front desk vs manager)?
8. What variants exist (general practice, emergency, specialty/referral, equine/ambulatory, production animal, mobile, corporate groups, universities)?
9. How does the market name itself (PMS vs PIMS) and what does the legacy desktop generation look like?
10. Historical check: would a paper-era or legacy-desktop veterinary practice satisfy the definition?
11. Where are the boundaries against §22 practice software, Animal Shelter Management, and the pet-service family?

## Representative Products

Selection principles applied: market representation, documentation completeness, different product philosophies, different customer tiers, different species/deployment breadth.

1. **Shepherd** (shepherd.vet) — modern cloud PIMS built by practicing vets, US, independent-practice pole; SOAP-first workflow philosophy. Product site + feature pages (Tier-2, moderately deep).
2. **Provet / Provet Cloud** (provetcloud.com / provet.com, Nordhealth) — cloud PIMS, Finland-origin, international (45 countries claimed), spans independent clinics to the largest corporate groups and referral hospitals; strongest category-level self-definition. Product site + FAQ + feature pages (Tier-2).
3. **ezyVet** (IDEXX) — cloud PIMS, global, enterprise/university/equine/production-animal breadth; integration-ecosystem philosophy. Product site + feature page (Tier-2).
4. **Legacy desktop generation — AVImark, Cornerstone (ImproMed, Robovet, Teleos)** — no direct documentation reachable this pass; evidenced indirectly by Provet's own FAQ (naming them as the pre-cloud legacy generation its migrations replace) and by ezyVet's published market-comparison table listing Avimark. Treated as the legacy-desktop pole with reduced assertion strength.

Rejected/considered: Digitail (not fetched; sample saturated per stop conditions), Hippo Manager (appears in ezyVet's comparison table only), IDEXX Cornerstone support site (transport error ×1 + idexx.com path 404 ×1 — abandoned per network rules), AVImark root (empty response ×1 — abandoned).

## Sources

Fetched 2026-09-09:

- Shepherd root: https://www.shepherd.vet/
- Shepherd — Features: https://www.shepherd.vet/features/
- Shepherd — Clinical tools / Automation: https://www.shepherd.vet/clinical-tools/automation/
- Provet root: https://provetcloud.com/
- ezyVet root: https://www.ezyvet.com/
- ezyVet — Invoicing & Payments: https://www.ezyvet.com/features/invoicing-and-transactions

Source-access limitations:

- **No Tier-1 operational documentation was reached this pass.** help.ezyvet.com returned an empty response; cornerstonesupport.idexx.com transport-errored; www.idexx.com/en/veterinary-services/practice-management-software/ returned 404; docs.provetcloud.com transport-errored; www.avimark.net returned empty. All product evidence is Tier-2 (official product/feature/FAQ pages).
- Consequence: precise operational details (exact state names, numeric limits, default settings, record-retention rules, controlled-substance logging mechanics, vaccination-reminder timing defaults) are NOT stated anywhere in this research or the final document. The legacy-desktop pole (AVImark/Cornerstone generation) is evidenced only indirectly (Provet's FAQ naming them as legacy; ezyVet's comparison table). Claims that would require Tier-1 depth are marked below.

Evidence layers used: **A** = directly observed on an official vendor page for a specific product; **B** = cross-product commonality across the sampled products; **C** = canonical inference from cross-product comparison and boundary reasoning.

## Product A — Shepherd

Positioning: cloud-based veterinary practice management software "built by vets"; independent-practice pole; SOAP-first philosophy.

Key observations (all Layer A unless noted):

- Medical records are **SOAP-based** (Subjective/Objective/Assessment/Plan structure named explicitly). "Completing your SOAP automatically updates the medical record and invoice, and generates discharge instructions."
- **Charge capture as a core promise**: "If it's on the medical record, it's on the invoice." Administering treatments automatically adds them to the invoice. This is presented as the reason the record and the financial side are one product.
- **Estimate → treatment plan → invoice chain**: services added to an estimate (individually or as bundles), adjustable when a client declines a service, client signature captured from any device, "with one click the estimate becomes the treatment plan. One more click, and it's all on the invoice." Approved estimates are "pushed to treatment plans before the patient even leaves the room."
- **Digital whiteboard**: "at-a-glance view of current treatments," sortable/searchable/filterable, one click opens the patient record for treatment administration.
- **Dashboard**: real-time view of patients' SOAP status and location, patients currently in the practice and which doctor they are seeing, upcoming appointments, pending lab work, and pet-portal requests.
- **Scheduling**: appointment types tied to provider availability; blocked provider time slots for non-patient activities.
- **Client communication**: Messaging Center + pet portal; clients request appointments and Rx refills, view medical history, access vaccine certificates; reminders can be tied to any product/treatment and "automatically add them to the queue."
- **Inventory tracking** with automatic updates after product administration; tracks treatments, prescriptions, PPE, medical supplies, sellable items; re-order scheduling.
- **Reporting**: end-of-day, commissions, treatments, patients, inactive clients; framed for "administration and compliance."
- **Payment processing** (Shepherd Pay) built in: USB terminal, stored cards, online pet-portal payments.
- **AI tools** (TranscribeAI auto-generating SOAP notes; DiagnoseAI treatment/differential suggestions) — era-current, vendor-specific productization.
- Unlimited users/workstations included; multi-location edition exists.
- Testimonial evidence of the paper→software transition: a practice "100% on paper for over 40 years" migrated in phases (indicates the paper-era predecessor workflow the software replaces).
- Testimonial from a mobile veterinary service (Vista Paws Mobile) — ambulatory use exists at the small-practice pole.

## Product B — Provet / Provet Cloud

Positioning: "all-in-one veterinary PIMS"; Finland-origin (Nordhealth), international; independent clinics through the largest corporate groups (CVS Group, IVC Evidensia, Altano, Pets at Home, Linnaeus named); referral hospitals and universities.

Key observations (all Layer A unless noted):

- **The vendor's own category definition**: "A veterinary PIMS is the operational backbone of a clinic. It runs your schedule, holds your medical records, generates invoices, processes payments, sends reminders, books appointments online, and connects to your lab and imaging equipment." — Tier-2 but category-shaping evidence for the Type's scope.
- **Naming history**: "The category has historically been called PMS (practice management software). We use PIMS because the system holds your information (medical, clinical, financial, client) as much as it runs your operations." — direct vendor evidence that PMS and PIMS name the same product population from two angles (operations vs information).
- **Health records**: "One place for history, notes, labs, imaging, and estimates" — the record is the container across clinical and financial artifacts.
- **Payments flow**: "Estimates to invoices to payment, all in one flow."
- **All-in-one scope claim**: "PIMS, scribe, payments, messaging, reporting, health plans, inpatient treatment sheets, online booking, and client engagement all in one unified workspace." — evidence for in-patient treatment sheets and health plans as in-product structures.
- **Communication**: appointment confirmations and reminders via SMS and email.
- **Online booking**: clients book, confirm, and create a profile without calling.
- **Multi-location/enterprise**: central oversight + local flexibility; centralized reporting, role-based access; group-level quality-assurance tracking quote from IVC Evidensia's Country Medical Director.
- **Specialty/emergency**: "general practice, specialty referrals, and emergency workflows in one workspace"; a referral-hospital manager quote describes following "every step of the clinical and economic route of the patient from the appointment to discharge."
- **Ambulatory/equine**: equine customer (Brazil Cheltenham Equine Vets) describes house/farm calls, records and accounts "on the road," part-time vets writing up from home — the field-visit overlay on the same core.
- **Integrations (150+)**: labs (IDEXX, Antech, Laboklin, Axiom), insurers (Agria, If Insurance), pharmacies/suppliers (MWI, NVS, Vetcove, Covetrus), imaging, telemedicine, payments — the PIMS as the practice's integration hub.
- **Charity use**: RSPCA is a named customer ("Provet does drive compliance. It does drive workflow.") — a charity operating the same client-based clinical-business structure for its clinics.
- **Legacy naming**: "Legacy systems like AVImark, Cornerstone, ImproMed, and Robovet were built before the cloud, before mobile, before AI." — indirect evidence for the legacy-desktop pole (Layer A for Provet's claim; Layer B for the pole itself via ezyVet's table).
- Pricing model is per practicing veterinarian (front desk/nurses uncharged) — vendor business-model detail (Layer A; vendor-specific, not structural).
- AI agents (Clinical Agent/Scribe, Ask Provet, Provet MCP) — era-current vendor-specific productization.

## Product C — ezyVet

Positioning: cloud PIMS owned by IDEXX (diagnostics company); global; breadth across general practice, specialty, emergency, equine, corporate groups, universities, production animal, mobile.

Key observations (all Layer A unless noted):

- **Feature pillars** (site navigation): Scheduling, Client Communication, Invoicing & Payments, Task Automation, Business Reporting, Cloud-based.
- **Invoicing depth**: product bundles; mark-up and fixed pricing; **remote payments** via secure payment link sent by SMS or email; **integrated pet-insurance electronic claims** ("send an insurance claim at the touch of a button"); customizable financial documents — Statements, Invoices, Payment Receipts, Estimates — auto-personalized from client details.
- **Solutions breadth** (site structure): General Practice / Specialty / Emergency / Equine ("visiting stables or making farm calls") / Corporate Groups / Universities / Production Animal ("plan for your farm and lifestyle visits") / Mobile (dedicated mobile feature set). — the species/practice-type variants are vendor-acknowledged market segments of one product.
- **Integration ecosystem**: Vet Radar (in-hospital treatment/workflow companion), CareCredit, payments, insurance, imaging, diagnostics, product suppliers — IDEXX-aligned diagnostics integration as a distinguishing posture.
- **Market-population evidence**: the site publishes a Capterra-based comparison table including ezyVet, Pulse (Covetrus), Avimark, Hippo Manager, Provet Cloud — five PIMS brands named on one official page (supports the sample's market representativeness).
- Enterprise posture: corporate groups named as a solution; a customer story describes building on ezyVet's API.

## Cross-product Comparison

| Structure / capability | Shepherd | Provet | ezyVet | Layer | Verdict |
|---|---|---|---|---|---|
| Client (owner) account as the billing-responsible party | ✓ (pet portal, client comms) | ✓ (client information in record; data ownership FAQ) | ✓ (financial docs auto-personalized by client; remote payment links) | B | definitional context |
| Individually identified animal patient records under the client | ✓ (patient records, patient health tracking) | ✓ ("20M+ pets"; health records per patient) | ✓ (patient care; solutions per species) | B | definitional |
| Appointment book binding patient × provider × time | ✓ (appointment types tied to provider availability; blocked slots) | ✓ (schedule; online booking into it) | ✓ (Scheduling pillar) | B | definitional-adjacent (see L0 note) |
| Clinical documentation as the consult's output (SOAP named in ≥1 product) | ✓ (SOAP explicitly; SOAP status on dashboard) | ✓ (notes, history, labs, imaging in one record) | ✓ (patient-care framing; AI blog on clinical decision support) | B | definitional |
| Diagnoses/treatments/prescriptions recorded and tied to products/services | ✓ (treatments administered → charged; prescription tracking in inventory) | ✓ (AI Actions matches "diagnoses recorded, medications administered, treatments performed" to PIMS items) | ✓ (bundles, mark-up pricing on products/services) | B | definitional-adjacent |
| Estimate → (approval) → treatment plan/procedure → invoice → payment | ✓ (one-click chain, client signature) | ✓ ("estimates to invoices to payment, all in one flow") | ✓ (Estimates as financial doc; remote payment) | B | definitional |
| Hospitalized/in-patient workflow (whiteboard / treatment sheets) | ✓ (digital whiteboard) | ✓ (inpatient treatment sheets named) | ✓ (Vet Radar companion integration) | B | standard (L1) |
| Reminders/recalls tied to products/treatments | ✓ (reminders tied to any product/treatment) | ✓ (reminders via SMS/email) | ✓ (client communication pillar; reports incl. vaccinations) | B | standard (L1) |
| Inventory of medical products/supplies with usage decrement | ✓ (auto-update on administration) | ✓ (suppliers/pharmacy integrations; not directly named as core) | ✓ (product bundles/suppliers; pricing on products) | B | standard (L1) |
| Client-facing surfaces (portal, online booking, messaging) | ✓ (pet portal, messaging center) | ✓ (online booking, client engagement) | ✓ (client communication; remote payments) | B | standard (L1) |
| Payment processing inside the product | ✓ (Shepherd Pay) | ✓ (Provet Pay) | ✓ (payments integration; remote payments) | B | standard (L1) |
| Insurance claims handling | — (not observed this pass) | ✓ (insurer integrations named) | ✓ (electronic claims) | A (2/3) | variant/optional (region-dependent) |
| Health/wellness plans (recurring client plans) | — (not observed) | ✓ (health plans named) | — (not observed) | A (1/3) | optional, single-source → not promoted |
| Reporting (financial/production/compliance) | ✓ (end-of-day, commissions, treatments) | ✓ (dashboards; Ask Provet analytics) | ✓ (business reporting pillar) | B | standard (L1) |
| Labs/imaging integrations | ✓ (pending lab work on dashboard) | ✓ (labs, imaging named; IDEXX/Antech integrations) | ✓ (diagnostics/imaging partner categories) | B | standard (L1) |
| Multi-location / group operation | ✓ (multi-location edition) | ✓ (enterprise, group reporting, role-based access) | ✓ (corporate groups solution) | B | variant axis (scale) |
| Species/practice-type variants (companion, emergency, specialty, equine, production animal, mobile) | ✓ (independent + mobile evidence) | ✓ (GP/ER/specialty/hospital/university; equine customer) | ✓ (full solutions taxonomy) | B | variant axis |
| AI documentation/decision tools | ✓ (TranscribeAI, DiagnoseAI) | ✓ (Clinical Agent, Scribe, Ask Provet, MCP) | ✓ (AI blog positioning) | B | era-current, not definitional |
| Cloud delivery | ✓ | ✓ | ✓ | B | dominant-but-variant (legacy desktop generation exists) |
| Per-vet pricing / unlimited users | ✓ (unlimited users) | ✓ (per-vet pricing) | — | A (2/3) | vendor business-model detail (L3) |

## Canonical Abstraction

### L0 — Defining Invariant

Minimal structure without which the product is not a veterinary practice management system:

1. **The client-and-patient two-level record** — an identified client (owner) account that holds individually identified animal patient records; care is delivered to patients but owned and billed through the client. Remove the patient level → a client CRM; remove the client level → custody-based care (shelter territory) or anonymous clinical notes.
2. **The clinical encounter loop on the animal's medical record** — appointments/consultations produce attributed clinical documentation (exam findings, diagnoses/problems, treatments/prescriptions) that accumulates as the animal's longitudinal medical record. Remove → appointment-booking + invoicing machinery with no clinical core (non-clinical service management).
3. **The client-account billing loop** — clinical services and medical products carry configured prices, are charged to the client account (estimate → invoice), and resolve into payments. Remove → a clinical documentation tool with no business loop.

Jointly-held load-bearing test:

- 1 alone = client/pet CRM (pet-service family territory)
- 2 alone = clinical notes tool (no practice business)
- 3 alone = invoicing shell
- 1+2 without 3 = custody-style clinical records (shelter clinic territory, no client billing)
- 2+3 without 1 = an anonymous clinic (no identified owners/animals)
- 1+3 without 2 = a non-clinical pet-service business (grooming/boarding territory)

What is deliberately NOT in L0 (anti-overfit):

- **SOAP structure NOT definitional** — SOAP is named explicitly by Shepherd and reflected in Provet's AI wording, but the invariant is "attributed clinical documentation accumulating on the animal's record," not a specific note format. Paper-era and legacy-desktop records were not uniformly SOAP.
- **Vaccination/reminders NOT definitional** — standard (L1).
- **Inventory NOT definitional** — standard (L1).
- **Estimates NOT definitional as a separate object** — the estimate is a common realization of the billing loop's pre-approval step; the invariant is charge → invoice → payment on the client account.
- **Whiteboard/treatment sheets NOT definitional** — in-patient workflow machinery, standard (L1).
- **Online booking / client portal NOT definitional** — modern access layer (L1); the client can be booked by staff.
- **Insurance claims NOT definitional** — region/payer-model dependent (2/3 products only; absent from the Shepherd observations).
- **Payment processing, health plans, AI tools, cloud delivery NOT definitional** — era/market machinery.
- **Species set NOT definitional** — the animal patient can be companion, equine, production animal; the two-level client↔patient structure holds across all sampled variants.

Historical/market-sample check: a paper-era veterinary practice (appointment book + client/patient paper cards + handwritten records + day sheets and receipt book) satisfies all three L0 legs with no modern machinery; the legacy desktop generation (AVImark/Cornerstone/ImproMed/Robovet, named by Provet as pre-cloud) satisfies them with desktop software. The definition is not fitted to the modern cloud-AI implementation.

### L1 — Common Mature Structure

Present in most mature products (Layer B across the sample): appointment book with provider availability; reminders/recalls; estimates and estimate approval; discharge instructions; whiteboard/in-patient treatment views; inventory with usage decrement; reporting (financial, production, compliance); client communications (SMS/email); client portal / online booking; payment processing; lab/imaging integrations; role-based access; multi-location support at the upper end.

### L2 — Variant / Optional Structure

Practice-type variants (companion GP, emergency, specialty/referral, equine/ambulatory, production animal, mobile); scale variants (single clinic → corporate group → university teaching hospital); deployment (cloud dominant, legacy desktop still in market); region/payer variants (pet-insurance claim assistance in some markets; direct-pay elsewhere); health/wellness plans; AI documentation/decision support (era-current).

### L3 — Vendor-specific

Shepherd's TranscribeAI/DiagnoseAI/Shepherd Pay; Provet's AI Agents/MCP/per-vet pricing/ISO-uptime claims; ezyVet's Vet Radar companion, IDEXX-aligned diagnostics posture, remote-payments framing; CVS Group's 350-clinic migration claim. These stay out of the final document.

## Boundary Findings

1. **vs Practice Management System (§22, human ambulatory analog)** — same genus: an ambulatory practice's administrative-financial system of record with a registered patient of record + scheduled visit + visit-to-money loop. Seams: (a) the veterinary market norm **merges the clinical record and the business system into one product** (PIMS), while the human market sells PM and EHR as separable pillars (the human pass documented vendors selling EHR and PM separately); (b) the patient is an animal under an identified human client — every charge routes to the client, no third-party payer sits at the loop's center (insurance appears as claim-assistance integration, not as the billing counterparty); (c) species/mobility variants (equine farm calls, production-animal herd visits) reshape scheduling and location semantics. Keep-both ratified from this side; the human pass's family note ("same genus; payer-claim machinery + clinical visit economy distinctive") extends to veterinary with the merge/separate seam added.
2. **vs Animal Shelter Management** — custody-based care (animals taken into the organization's custody; intake → in-care → outcome; no client billing) vs client-based clinical business (owners own the animals and pay for services). The ASM pass recorded that a shelter vendor ships a public-facing **Clinic module as a separate optional chapter** — vendor-confirmed structural separation. Provet counting the RSPCA as a customer does not blur the seam: a charity running public clinics uses the clinical-business structure; the operator's nonprofit identity is orthogonal. **Joint-review flag from the ASM pass DISCHARGED this pass.**
3. **vs the pet-service family (boarding/daycare/grooming/training/pet-care-business)** — non-clinical service delivery vs clinical care; across four prior passes the veterinarian/vaccination appear only as data fields on the pet record, never as a clinical workflow. The clinical documentation + treatment layer is this Type's defining seam.
4. **vs Pet Health Application / Pet DNA Analysis Platform** — owner-facing consumer record of the animal's day-to-day health or lab-derived findings vs practice-operated clinical system of record; clinic-collected, clinician-attributed, diagnosis-bearing (carried from the DNA pass).
5. **vs generic Appointment Scheduling / Appointment-based Service Business Management** — the appointment book exists here but is one component feeding the clinical encounter loop and the billing loop; scheduling-only products lack the record and the money loop.
6. **Taxonomy observation (no rewrite)** — the leaf sits in §29 (Home, Family, Personal & Local Services) among pet services, while the product population is structurally closest to §22 ambulatory practice software. The placement is defensible (the practice is a local service business whose clients are pet/horse/livestock owners), and the market itself names the products PMS/PIMS interchangeably. Recorded as an observation only.
7. **Naming observation** — PMS (Practice Management System) vs PIMS (Practice Information Management System) is a vendor naming axis over one product population, evidenced by Provet's own FAQ; the directory leaf name ("Veterinary Practice Management") covers both.

## Uncertainties

1. No Tier-1 operational documentation reached; all assertions calibrated to product-page strength. Precise state machines (appointment statuses, invoice states), default settings, retention rules, and controlled-substance logging are deliberately absent.
2. Legacy-desktop pole (AVImark/Cornerstone) evidenced only indirectly (Provet's legacy naming; ezyVet's comparison table). No direct feature claims about those products are made.
3. Insurance-claims machinery depth (claim status tracking, direct insurer settlement vs client-pays-then-claim) could not be verified; asserted only as "claim submission assistance exists in some markets."
4. Health/wellness plans observed in one product (Provet) — kept optional, single-source.
5. The exact composition of in-patient workflow across products (whiteboard vs treatment sheets vs companion module) varies; asserted at class level only.
6. Equine/production-animal field-visit workflows (route planning, herd-level billing) are inferred from vendor solution pages and one customer quote; asserted as variant existence, not workflow depth.

## Final Synthesis

Veterinary Practice Management software is the veterinary practice's operator-side system of record — the market calls it PMS or PIMS. Its defining core is three jointly-held structures: a two-level client-and-patient record (identified owner account holding individually identified animal patients), a clinical encounter loop that turns appointments/consultations into attributed, accumulating medical records for animals (exam findings, diagnoses, treatments, prescriptions), and a client-account billing loop that prices clinical services and medical products, charges them to the client account as estimates/invoices, and resolves them into payments. Around this core, mature products add the appointment book with provider availability, reminders and recalls, estimates and discharge instructions, in-patient whiteboards/treatment sheets, inventory decrementing, reporting, client communications and portals, payment processing, and lab/imaging integrations. The Type varies by practice type (companion GP, emergency, specialty/referral, equine/ambulatory, production animal, mobile), by scale (independent clinic → corporate group → university), and by deployment (cloud dominant, legacy desktop persisting). Its boundaries are sharpest against the human practice-software family (merged vs split clinical/business pillars; animal patients under paying owners), Animal Shelter Management (custody vs client-based clinical business), and the non-clinical pet-service family (service delivery vs clinical care).
