# Research Notes — Med Spa Management

## Research Goal

Determine what "Med Spa Management" software actually is, from real products: its core operating model, what (if anything) structurally distinguishes it from the generic appointment-based service business software already documented (appointment-based-service-business-management, barbershop-management, massage-practice-management, beauty-professional-business-app — all processed), and where its boundaries sit with Spa Management System (§29 sibling, unprocessed) and §22 healthcare scheduling/practice management.

## Initial Boundary

Working hypothesis at start (per §4 Understand):

- Core use: run a medical-spa (medspa / medical aesthetics) business — booking regulated aesthetic treatments, documenting them compliantly, and monetizing the client relationship.
- Primary users: front desk/reception, treatment providers (injectors, aestheticians, nurses, NPs, MDs), practice managers/owners.
- Nearest neighbors: appointment-based-service-business-management (generic core), spa-management-system (unprocessed sibling), salon-management-system (unprocessed sibling), massage-practice-management (processed), §22 Patient Scheduling / Practice Management System / EHR.
- Potential confusion: is this just "salon/spa software with medical features" (an industry Variant), or a distinct Type with a required clinical core (an EMR with booking bolted on)?
- Prior flags hanging on this leaf: the appointment pass (2026-09-06) flagged med-spa as a probable industry Variant and noted "medspa EMR/charting overlays stay a variant and do not merge with Patient Scheduling / Practice Management (§22)"; the massage pass (2026-09-08) left "med-spa-management" among the unprocessed siblings "probable industry Variants for their own passes."

## Research Questions

1. What objects does the software manage? (catalog, clients, appointments, charts, forms, photos, products, memberships…)
2. Is the appointment/visit economy (catalog + client + appointment + lifecycle + checkout) present at every market pole, including the most clinical one?
3. What exactly is the "medical" layer, and is it definitional or an overlay? (Removal test: can a med spa run the full visit economy with the medical layer absent/optional?)
4. How is the medical layer packaged — built-in, gated setting, or purchasable add-on?
5. What vocabulary and roles appear (client vs patient, provider vs practitioner, medical director)?
6. What state machines and rules matter (form expiry, sign-off/approval, no-show, consent-before-treatment)?
7. Historical check: does a paper-era / regional / differently-positioned medical-aesthetics business satisfy the same definition (avoid overfitting to current US HIPAA + injectables pattern)?
8. Boundary: what distinguishes this from Spa Management System (relaxation/wellness pole) and from §22 practice management/EHR?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Pole | Client tier | Region | Evidence tier reached |
|---|---|---|---|---|
| Zenoti | Enterprise all-in-one "medspa operating platform" (also serves salons/spas/fitness/barbers) | Multi-location chains, franchises, global | US/global | Tier-2 (medspa solution page with detailed product FAQ) |
| Boulevard | Modern mid-market client-experience platform; medspa = named industry; clinical layer sold as add-on | Single + small multi-location self-care businesses | US | Tier-1 (support center: Medspa collection, Forms & Charts articles, Medspa Add-On article) |
| Mangomint | Mid-market salon/spa software with med-spa solution; "HIPAA-compliant booking & EMR" | Boutique salons/spas/med spas | US | Tier-2 (med-spa solution page with FAQ) |
| Pabau | Clinic-first practice management ("Practice Management Software for Clinics & Medical Spas"), full EMR | Clinics of all sizes incl. solo practitioners | UK-origin, US+EU | Tier-2 (site + medspa industry page with FAQ) |

Deliberately excluded: Fresha/Booksy (known unreachable from this environment per prior passes); AestheticsPro/PatientNow/Remedly/Symplast (named by Zenoti's own comparison content as clinical-EMR-first competitors — used as category vocabulary, not as researched products).

## Sources

All fetched 2026-09-08.

- Zenoti — https://www.zenoti.com/ (site nav: /platform/forms-and-charting, /platform/photo-manager, /medical-spa-software/* sub-pages) ; https://www.zenoti.com/medical-spa-software
- Boulevard — https://www.joinblvd.com/ ; https://www.joinblvd.com/medical-spa-software ; support center https://support.boulevard.io/en/ (Tier-1): article 8038055 "Forms and Charts in the Professional App", article 10723276 "Product Tracking", article 9586002 "Medspa Training Checklist", article 9084775 "Medspa Add-On", Medspa collection (9811066)
- Mangomint — https://www.mangomint.com/ ; https://www.mangomint.com/solutions/medical-spa-software/
- Pabau — https://pabau.com/ ; https://pabau.com/industry/medical-spa-software/

Sourcing limitation: Tier-1 help-center evidence was reached for Boulevard only; Zenoti, Mangomint and Pabau claims rest on their official product/industry pages (Tier-2). Zenoti's help center (help.zenoti.com) was not fetched this pass. Marketing numbers (benchmark percentages, rating claims) are NOT carried into the final document. Prior-pass Tier-1 knowledge reused from the family file where noted (Vagaro/Zenoti API-doc observations from the appointment and massage passes).

## Product A — Zenoti (enterprise operating-platform pole)

### Key observations (evidence: A=direct from fetched pages, Tier-2)

- Positioning: "Medical Spa Software: Purpose-Built for Growing Medspas"; tagline mixes the two registers: "Effortless Operations. Clinical Excellence. Exponential Growth." Customer logos are medspa/laser/weight-loss chains.
- Zenoti's own category FAQ (A, quotable semantics): "Medical spa software is an all-in-one operating platform built specifically for the intersection of clinical medicine and retail wellness… A traditional day spa can run adequately on generic booking and payment tools. A medspa cannot…" Clinical side listed: "HIPAA-compliant patient charting, before/after photo documentation with comparison overlays, digital intake and consent forms, e-prescription integration, injectable and controlled substance tracking, and treatment protocol management." Business side: "online booking… point of sale and integrated payment processing, staff scheduling and commission tracking, product inventory management, membership and package programs, gift cards, automated marketing campaigns, and multi-location reporting."
- Charting: AI charting with templates, auto-filled summaries, conditional fields, previous-chart copying; SOAP-note AI scribe module; "HIPAA-ready documentation for medspa providers."
- Photography: before/after photos in every client profile, guided overlays and sequences, organize by body area/treatment type, side-by-side comparison; "HIPAA-Compliant Photo Management."
- Compliance: real-time form-completion monitoring, "enforce custom compliance rules by center or role," review of forms in real time (supervisor review loop).
- e-Prescribe via Surescripts integration (from patient profile) — optional capability layer.
- Inventory: injectables tracked "by syringe and batch," per-unit usage monitoring; AI inventory example uses "Wrinkle Relaxer (50u)", "Hyaluronic Filler" — unit-dose economics.
- Visit economy: online booking, appointment book, kiosk/POS, memberships & packages ("beauty banks" — recurring programs for injectables/facials/IV/laser), gift cards, loyalty, marketing automation from clinical data (segment by skin type, past treatments), pre/post-care communication, telehealth for consults/follow-ups, BNPL, payroll & tipping, franchise/multi-location.
- Vocabulary: "patients" and "guests" used interchangeably; "providers" for staff.
- Zenoti's own competitive framing (A): AestheticsPro "was built as a clinical EMR first. Its capabilities include charting… Its limitations are on the business operations side…" vs Zenoti "built as a complete medspa operating platform." Names AestheticsPro, PatientNow, Vagaro, Pabau, Remedly as the medspa-software competitive set.
- Sub-industry pages for the same product: injectables & filler clinics, skin & derma, medical weight loss, laser treatments, wellness & IV therapy — same machinery, different treatment taxonomies.

## Product B — Boulevard (client-experience pole, clinical layer as purchasable add-on)

### Key observations (evidence: A on all help-center articles, Tier-1)

- Positioning: "Medical Spa EMR Software for Scheduling, Booking & Patient Management" — but the pitch is explicitly anti-EMR: "Clients expect a personalized, luxurious experience. EMRs aren't built to support that — our HIPAA-compliant med spa software platform is." Site footer carries HIPAA / SOC 2 / PCI Level 1 compliance badges.
- **Medspa Add-On (Tier-1, article 9084775) — decisive packaging evidence.** The add-on bundles: (1) unlimited photo markup and sign-off ("mark up images to indicate treatment points… submit forms and charts to designated reviewers for them to add comments, approve or reject documents"), (2) HIPAA Coverage: signed BAA in the dashboard, "additional security settings" (e.g., "Service details hidden from patient communications by default"), "a clinical section of the patient profile that centralizes allergy, medication, and prescriptions," HIPAA configuration guidance, access to purchase ePrescribe, HIPAA-trained support. ⇒ The clinical layer is an optional, purchasable module on the generic appointment platform. (List price observed; vendor detail, not carried to final doc.)
- **Forms vs Charts — two document classes (Tier-1, article 8038055):** forms are client-facing (sent to clients, reminders to complete, "Charts are not sent to clients"); charts are provider-facing treatment documentation completed in the Professional App from the appointment or client profile; both have statuses (Not started / In progress / Completed / Expired) and **expiry semantics bound to appointments** ("If a form has an 'Expired' status… The client will be asked to resubmit that form for their first appointment after the expiration date"). Draft saving, offline submission marking, blank-PDF export, notes on completed forms, sign-off feature, photo upload + photo markup inside forms/charts.
- Medspa Training Checklist (Tier-1, article 9586002) — the vendor's own medspa configuration recipe: services + add-on services + resources; **product tracking** (products linked to services, usage-based pricing, prepaid units); custom payment types; packages; memberships (creating, selling in-store/online, updating, billing management, tracking); **Forms & Charts** (building, connected fields that write answers back into the client profile, photo upload, notes, sign-off, example forms); **Security & Access** (HIPAA security requirements for HIPAA-enabled accounts, automatic staff logout, permission groups).
- Product Tracking (Tier-1, article 10723276): products attached to services with price and quantity per service; report fields "Service Product Usage Name / Quantity / Unit Price"; usage-based pricing and prepaid-units reporting — the per-unit injectables economy implemented on the generic service machinery.
- Visit economy present throughout: Precision Scheduling, all-in-one POS, memberships & packages, loyalty, marketing/messages, BNPL, dispute resolution center, reporting.
- Vocabulary: "clients" and "patients" both used; "Boulevard Professional" app for providers.

## Product C — Mangomint (mid-market salon/spa software with med-spa solution)

### Key observations (evidence: A, Tier-2 solution page)

- Positioning: "Med Spa Software: HIPAA-Compliant Booking & EMR." EMR framing deliberately de-hospitalized: "our EMR is a comprehensive solution—just without the cluttered, clunky interface… captures all the essential client information medical spas need without turning your dashboard into a hospital system" (paraphrase from page; exact wording on page).
- Forms & Charting feature "meets the intake and charting needs of medical spas (including maintaining HIPAA compliance, with a signed BAA, once enabled)" ⇒ HIPAA posture is a **gated setting** on the generic platform, not the platform's default identity.
- Charting mechanics: "intake forms and SOAP notes, upload visual templates or client photos, and annotate images"; workflow "from consent forms to completing outcome notes."
- **Med-spa-specific booking behavior (A, single-product):** "many medical spas using Mangomint prefer to limit online booking to consultations and require clients to call for booking additional services. You can direct clients to call to book…" — booking-gating as a configured posture; supports the observation that medspa businesses adapt the generic booking machinery to clinical screening norms.
- Virtual meeting rooms ("HIPAA-compliant virtual meeting rooms… linked to any med spa appointment") — telehealth as appointment-typed surface.
- Customer quote (A): "keep appointment information and HIPAA protected health information all in one place… removing the need for a separate software."
- Full generic feature set on the same page: Calendar & Scheduling, Payments & POS, Online Booking, Express Booking, Mobile Apps, Client Management, Memberships & Packages, Forms & Charting, Gift Cards, Automated Flows, Campaigns, Offers & Discounts, Virtual Waiting Room, retail & inventory, reporting.
- Mangomint serves Med Spas as ONE industry among ~12 solutions (hair salons, IV therapy, skincare studios, massage, tattoo & piercing, nail salons, barbershops, wellness centers, spas…) — same platform, industry configuration.

## Product D — Pabau (clinic-first pole)

### Key observations (evidence: A, Tier-2 site + industry page)

- Positioning: "Practice Management Software for Clinics & Medical Spas"; medspa is one named specialty among many (GP, wellness, longevity, IV therapy, weight loss, dermatology, cosmetic surgery, mental health, physio…). A separate "Spa" specialty page also exists — same product sells to both.
- **The visit economy is the operating spine even at the most clinical pole:** "Keep your appointment book full and payments flowing — let clients book online 24/7, reduce no-shows with smart reminders, and get paid instantly"; deposits collected at booking; waitlist auto-fill; client portal (view treatment history, book follow-ups, pay balances, access before/after photos); integrated POS; memberships & packages ("turn one-off treatments into predictable recurring revenue"); quotes; commissions per practitioner; marketing campaigns/loyalty/gift vouchers; multi-location; reporting.
- Clinical depth (deepest of the sample): "full in-built EMR… A single client card acts as a hub"; structured clinical notes; before/after photos with integrated photography tools; **injection plotting** ("Map every injection point with injection details on the client record… support multi-session treatments"); AI scribe (voice → structured notes); pre- and post-care instructions auto-sent on booking confirmation ("Whatever treatment clients book, Pabau automatically sends them that specific online consent form and precare" — customer quote); labs (request/result workflow); prescriptions; telehealth; vaccines; measurement-based care; consent workflows; compliance surface (role-based permissions, 2FA, encryption, audit trails, HIPAA+GDPR posture).
- Optional capability observed here only: Insurance Billing (claims management) — single-product in this sample.
- Vocabulary: "patients", "practitioners", "treatment providers", "front of house staff".

## Cross-product Comparison

| Structure / capability | Zenoti | Boulevard | Mangomint | Pabau | Evidence layer |
|---|---|---|---|---|---|
| Bookable treatment catalog (duration+price) | ✓ | ✓ | ✓ | ✓ | B |
| Identified client/patient records with history | ✓ | ✓ | ✓ | ✓ | B |
| Appointment binding client×treatment×provider×time | ✓ | ✓ | ✓ | ✓ | B |
| Visit lifecycle through delivery; cancel/no-show handling | ✓ | ✓ | ✓ | ✓ (deposits/no-show protection) | B |
| Checkout / POS resolving visit into payment | ✓ | ✓ | ✓ | ✓ | B |
| Client-facing intake/consent forms (appointment-bound, expiry) | ✓ | ✓ (Tier-1) | ✓ | ✓ | B |
| Provider-facing charts/notes (SOAP-class), saved to client record | ✓ | ✓ (Tier-1) | ✓ | ✓ (EMR hub) | B |
| Form/chart review — sign-off / approve-reject by reviewer | ✓ (compliance monitoring) | ✓ (Tier-1, add-on) | — (not observed) | ✓ (compliance) | B (partial) |
| Before/after photography + markup/treatment-point annotation | ✓ | ✓ (Tier-1, add-on) | ✓ | ✓ (+injection plotting) | B |
| HIPAA/GDPR compliance posture (BAA, PHI handling, audit) | ✓ | ✓ (Tier-1, add-on) | ✓ (gated setting) | ✓ (GDPR+HIPAA) | B |
| Product/service unit-usage tracking & usage-based pricing | ✓ (syringe/batch) | ✓ (Tier-1) | — (retail/inventory present; unit pricing not observed) | ✓ (stock + usage logging) | B (partial) |
| Memberships / packages / prepaid ("beauty bank") | ✓ | ✓ | ✓ | ✓ | B |
| Self-booking, reminders, waitlist, deposits | ✓ | ✓ | ✓ | ✓ | B |
| e-Prescribing | ✓ (Surescripts) | ✓ (add-on) | — | ✓ | B (partial) |
| Telehealth consults | ✓ | — (not observed) | ✓ (virtual rooms) | ✓ | B (partial) |
| Quotes/consultation flow with treatment plans | ✓ | — (not observed) | — | ✓ | partial |
| Marketing/loyalty/gift cards/reviews | ✓ | ✓ | ✓ | ✓ | B |
| Staff schedules, commissions, (payroll) | ✓ (payroll) | ✓ (schedules) | ✓ | ✓ (commissions, timesheets) | B |
| Multi-location | ✓ | ✓ | ✓ | ✓ | B |
| Insurance billing | — | — | — | ✓ (single-product) | A (product-specific) |
| AI documentation (scribe) | ✓ | — | — | ✓ | partial |

Reading: the visit economy is unanimous (B-layer) at every pole including the most clinical. The clinical-compliance layer is also common, but its **packaging varies wildly** — purchasable add-on (Boulevard), gated setting (Mangomint), built-in deep module (Zenoti), EMR core (Pabau) — which is the signature of a variant-defining overlay, not a definitional structure.

## Canonical Model (four abstraction levels)

### L0 — Defining Invariant

Same jointly-held core the family passes already established (appointment-business core), realized for the medical-aesthetics trade:

1. **Bookable treatment catalog** — services with duration and price (treatments: injectables, laser, skin, IV, weight-loss consults; catalog typed by treatment, not by relaxation therapy).
2. **Identified client records** — persistent per-person records carrying history (health-adjacent content commonly attached).
3. **Appointment** — binding client × treatment × provider × time; rooms/equipment as common resource constraints.
4. **Visit lifecycle through service delivery** — with cancellation and no-show as named outcomes (deposits/no-show protection common but not invariant).
5. **Checkout resolving the visit into recorded payment** — the visit becomes revenue in the same system.

Remove any leg → not this Type (remove catalog/appointment → generic CRM; remove checkout → scheduler; remove appointment → retail POS).

### L1 — Common Mature Structure

Present in essentially all mature modern products; expected, not definitional:

- Self-booking portal + reminders + waitlist + deposits/no-show protection
- Client-facing intake & consent forms; provider-facing treatment charts/notes; both saved against the client record
- Before/after photography with markup/comparison
- Memberships, packages/prepaid series, gift cards
- Product usage tracking (per-unit pricing on services) and retail/inventory
- Marketing automation, campaigns, loyalty, reviews, lead capture
- Staff scheduling, commissions, (in some suites payroll), multi-location management, reporting
- Permission groups / role-based access (front desk vs provider vs manager)
- Consultation/quote flows, treatment plans, pre/post-care communication
- Compliance surfaces: form-completion monitoring, audit trails

### L2 — Variant / Optional Structure

- **Packaging pole of the clinical layer**: purchasable add-on (Boulevard) ↔ gated setting (Mangomint) ↔ built-in module (Zenoti) ↔ EMR-first core (Pabau)
- Regulatory regime: HIPAA (US) vs GDPR (UK/EU); consent vocabulary follows the regime
- e-Prescribing (product-specific integrations), telehealth consults, AI scribe
- Booking-gating posture (consultation-only online booking — observed in one product's docs as a common customer preference)
- Insurance billing (single product in sample)
- Sub-industry emphasis: injectables clinics / laser / skin & derma / medical weight loss / IV therapy (same machinery, different catalog taxonomy)
- BNPL/financing, retail depth, franchise/multi-brand operations

### L3 — Vendor-specific (research notes only)

- Boulevard: Medspa Add-On list price; Duo hardware app; Offset (surcharge product); "Precision Scheduling™"; Dispute Resolution Center
- Zenoti: AI Workforce family (Receptionist, Scribe, Concierge, Lead Manager, Marketer, Dispute Manager); benchmark-report claims (33% revenue/guest, 35% call recovery); Surescripts "95% of U.S. pharmacies" claim
- Mangomint: Express Booking™; Virtual Waiting Room; "4.9 stars" marketing claims
- Pabau: Pabau GO mobile app; Scribe/Prescribing/Letters AI agents; Insights/Marketing/Care "Plus" bundles; Healthcode (UK private-insurance) integration

## Vendor-specific Findings

- Boulevard's "Medspa Add-On" (Tier-1) is the cleanest natural experiment in the family: the entire medspa clinical layer — markup, sign-off, HIPAA coverage, clinical profile section, ePrescribe access — is a separately purchasable module. A medspa business demonstrably runs the visit economy without it (Boulevard still sells the base platform to med spas; the checklist walks them through generic machinery + the add-on).
- Mangomint's "HIPAA compliance… once enabled" (Tier-2) shows the same from the settings side.
- Zenoti's own FAQ defines the category as two-sided (clinical + business) — but its competitive framing (AestheticsPro = "clinical EMR first… limitations on the business operations side") shows the market itself distinguishing EMR-first products from operating platforms, i.e., acknowledging a packaging gradient within one category.
- Boulevard's "service details hidden from patient communications by default" (Tier-1) is a concrete example of compliance-driven defaults reshaping generic behavior (appointment confirmations must not leak treatment names).

## Boundary Findings

1. **vs appointment-based-service-business-management (generic, §29)** — keep-both, industry-variant resolution per barbershop/massage precedent. The L0 is identical; the med-spa differences concentrate in the overlay (compliance documentation layer, photography discipline, unit-based product economics, regulated vocabulary/roles, compliance posture). Removal test passed in BOTH directions: (a) generic platforms (Boulevard, Mangomint) serve med spas with the same core machinery, clinical layer sold/gated separately; (b) no sampled product lacks the visit economy, not even the EMR-first pole. ⇒ This pass DISCHARGES the appointment pass's sibling flag for med-spa-management.
2. **vs spa-management-system (§29 sibling, unprocessed)** — removal test recorded for that pass: remove the regulated-treatment layer (medical intake/consents, provider-facing charts, compliance posture, unit-usage economics) and the treatments revert to relaxation/wellness therapies delivered in rooms by therapists → Spa Management System on the same visit economy. The spa pole's emphasis is room/therapy/multi-service itineraries; the med-spa pole's emphasis is provider-typed regulated treatments + clinical documentation + compliance. Same L0 family; probable industry Variant (flagged for the spa pass's own joint review).
3. **vs §22 Patient Scheduling / Practice Management / EHR** — the clinical pole (Pabau) carries EMR-class depth (labs, prescriptions, vaccines) yet keeps booking/deposits/POS/memberships as the operating spine and retains retail vocabulary absent from hospital-grade systems. Documentation depth alone does not merge the Types — RATIFIES the appointment pass's variant-not-merge note and the massage pass's seam note from this side. Where insurance claims processing, physician-led care programs, referral networks, or encounter-based clinical billing dominate, the product drifts to §22. Pabau's insurance-billing feature is the observed straddling marker (single-product).
4. **vs beauty-service-marketplace (§29)** — consumer-side discovery across providers vs operator-side management of one business (already established family seam; medspa software is operator-side; client portals are service surfaces, not marketplaces).
5. **Leaf-name note** — the market calls this category "med spa software / medical spa software"; the directory leaf name "Med Spa Management" describes the same operator-side system of record. No alias problem: no separate "med spa software" leaf exists in DIRECTORY.md.

## Historical / Market-Sample Check (§24)

- **Paper-era analog check (conceptual, passed):** a physician-supervised aesthetic clinic before this software category — appointment book; client card with medical history; signed paper consent forms; treatment chart cards (per-visit notes, injection sites hand-marked on face charts); printed before/after photos filed in the client's chart; product stock ledger with lot/batch notes; invoices/cash. Satisfies the L0 at analog level AND shows the overlay (consents, charts, photos, lot tracking) predates the software — the overlay is the digitized clinic paperwork, not a software-era invention. The software-era additions (HIPAA machinery, e-prescribing, AI scribe, BNPL) are correctly NOT in the core.
- **Regional check:** the sample includes a UK/GDPR-origin product (Pabau) whose regime vocabulary differs but whose structure is identical — so the definition must not name HIPAA (named as regime variant instead). European "medical spa" traditions (Kur/spa-with-medical-services) differ in business model but still reduce to the visit economy if run as appointment businesses; they are not separately evidenced in this pass and are recorded as an uncertainty rather than a claim.
- **Era check:** the definition names no AI, no cloud, no telehealth, no e-prescribing, no specific treatment type (no "Botox"/"injectables" in L0), no US-specific compliance regime.

## Uncertainties

- No Tier-1 help-center evidence for Zenoti, Mangomint, Pabau this pass; their structural claims rest on official product/industry pages (Tier-2). Structure-level assertions only; no operational minutiae asserted from them.
- Single-product observations: insurance billing (Pabau), booking-gating preference (Mangomint), form-compliance monitoring with per-center/role rules (Zenoti). Held at product-specific/variant level.
- The med-spa-specific pricing dimensions (per-unit pricing, beauty-bank memberships) were observed in 2–3 of 4 products; L1 placement chosen conservatively.
- Whether any product positions itself as a pure "medical spa EMR" with NO booking economy (the extreme clinical pole) is unverified — Zenoti's comparison content describes AestheticsPro that way but AestheticsPro was not directly researched. If such products exist, they would sit ON the §22 seam, not change this Type's core.
- Zenoti help center and Pabau knowledge base (support.pabau.com) not fetched; Pabau's "single client card as hub" claim rests on its own FAQ.

## Final Synthesis

Med Spa Management software is the med-spa industry's expression of the appointment-business core: a bookable regulated-treatment catalog, identified client records, the appointment binding client×treatment×provider×time, the visit lifecycle through delivery, and checkout into recorded payment — with a characteristic (not definitional) medical-compliance overlay: client-facing intake/consent forms and provider-facing treatment documentation saved to the client record, before/after photography with treatment-point annotation, regulated-data handling posture (BAA/PHI/audit), per-unit product economics, and clinical-role permissions. The market realizes one Type across a packaging gradient — from generic platforms with the clinical layer sold as an add-on, to EMR-first clinic software with the booking economy built in — and the visit economy remains the operating spine at every point on that gradient.
