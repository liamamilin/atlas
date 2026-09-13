# Research Notes — Permit Management (Government)

Research date: 2026-09-09
Leaf: Permit Management (DIRECTORY.md §24 Government, Public Sector & Civic)
Slug: permit-management

## Research Goal

Understand what a government-side Permit Management application really is: the system a public authority (city, county, state/province, special district) uses to receive, review, decide, and issue permits to external applicants, and what happens to the permit afterwards. Produce a vendor-neutral Application Document that a non-user could read and correctly imagine the software's world.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: this is the **agency side** of permitting — the authority manages external applicants' requests. The **permittee side** (an organization managing its own held permits) is already documented as §21 Environmental Permit Management (processed 2026-09-08), which explicitly assigned the agency-side market to this leaf.
- Nearest neighbors expected: Government Licensing Management (§24, processed — joint-review flag owed), Government Inspection Management (§24, processed — seam asserted from their side), Code Enforcement Management (§24, processed — parcel-spine adjacency), Planning & Zoning Management (§24, unprocessed sibling), 311 / Public Sector Case Management (§24), Government Service Portal (§24), Environmental Permit Management (§21, processed — joint-review flag owed).
- Known unknowns: exact internal staff workflow depth (completeness checks, correction cycles); whether conditions-of-approval machinery is definitional; how the permit/license seam behaves for standing environmental authorizations (nuance raised by the §21 pass).

## Research Questions

1. What objects exist inside the system? (application, permit, parcel/property, applicant, review, inspection, fee, certificate, registration…)
2. What is the canonical workflow from application to issued permit to close-out?
3. What does the issuing authority's staff do vs what does the external applicant do?
4. What role do fees/payments play — definitional or standard?
5. How do inspections, plan review, and multi-department routing attach to the permit record?
6. Where is the permit-vs-license seam, and does it hold for standing environmental authorizations?
7. Where is the permit-vs-planning seam (for the unprocessed sibling)?
8. What is configurable per jurisdiction, and what is invariant?
9. Do older / regional / differently-positioned products fit the definition (historical check)?

## Representative Products

Selection rationale: market representation + documentation accessibility + different product philosophies + different customer tiers.

| Product | Vendor | Position | Customer tier | Evidence tier reached |
|---|---|---|---|---|
| Accela (Building / Land Management) | Accela | enterprise platform leader for permitting & land management; city/county/state | large agencies (900+ agencies claimed) | Tier-2 (solution page) |
| SmartGov + AMANDA (Permitting, Compliance & Licensing) | Granicus | suite vendor; SmartGov = cloud local/state; AMANDA = enterprise PCL + FOI, cloud or on-site | small→state; AMANDA at large/international jurisdictions (Canadian base: Vaughan, Oakville, Coquitlam; PBOT) | Tier-2 (product pages) |
| Cloudpermit (Building Permitting) | Cloudpermit | cloud-native community-development suite, building-department focus | small/mid municipalities (1,450 claimed) | Tier-2 (product + product-family pages) |
| GovPilot (Construction / Permitting modules) | GovPilot | modular municipal SaaS priced by population + modules | small municipalities/counties | Tier-2 (product + module pages) |

Rejected/abandoned samples:
- **Tyler Technologies (Enterprise Permitting & Licensing / EnerGov)** — tylertech.com returned 403 twice; abandoned per network rules. Tyler remains a major market product but is NOT used as evidence this pass.
- **OpenGov (Permitting & Licensing, ViewPoint heritage)** — opengov.com returned 403 twice; abandoned. Noted as sourcing limitation.
- **CentralSquare** — 404 on first URL; not pursued (sample already sufficient).
- **Cloudpermit us.cloudpermit.com** — login redirect, then transport error on www.cloudpermit.us; main cloudpermit.com succeeded (the abandoned URLs were the same vendor's regional portal).

## Sources

All fetched 2026-09-09 (Tier-2 official product/solution pages; no authenticated help-center articles reached):

- Accela — Government Permitting / Building: https://www.accela.com/solutions/land-management/ (served building-permitting content)
- Granicus — SmartGov: https://granicus.com/product/permitting-compliance-licensing-smartgov/
- Granicus — AMANDA: https://granicus.com/product/permitting-compliance-licensing-amanda/
- Granicus — govService (boundary specimen, service-request sibling): https://granicus.com/solutions/govservice/
- Cloudpermit — home / product family: https://www.cloudpermit.com/
- Cloudpermit — Building Permitting: https://cloudpermit.com/products/building-permitting
- GovPilot — home: https://www.govpilot.com/
- GovPilot — Construction Permitting: https://www.govpilot.com/building-and-construction-permitting-software

Prior-pass counterparty records consulted (STATUS.md / research files): government-licensing-management, government-inspection-management, code-enforcement-management, environmental-permit-management, land-records-cadastre-system.

## Product Observations

### Accela (Building / Land Management) — evidence layer A

- Positions itself as "the only end-to-end platform for the entire building permit lifecycle"; "connect intake, plan review, inspections, and permit issuance in one workflow. Handoffs, duplicate data entry, and status chasing are eliminated."
- **Concurrent multi-department plan review**: "Fire, planning, public works, and utilities all review in one shared system at the same time. Every reviewer works from the same record, with annotations and approvals tracked in real time. Building Officials see exactly where each application stands."
- AI at intake: "AI will guide applicants to the right permit type at intake, reviews plans for errors before formal submission, and surfaces relevant issues during review."
- Inspections: "Field inspections and back-office tracking in one system. Inspectors work paperless from assignment to close."
- Applicant experience: "Applicants get real-time visibility into application status and consolidated feedback from all reviewing departments. Fewer status calls and resubmissions."
- Lifecycle diagram: citizen idea → initial engagement → application submission **and payment** → back office reviews → plan review → **permit/license issuance** → inspection and/or renewals.
- Product family separates: Building, Planning, Business Licensing, Occupational Licensing, Alcohol Beverage Control, Short Term Rental, Cannabis Regulation, Environmental Health, Fire Prevention, Service Request Management, Plan Review (ePermitHub), Asset Management. → permitting vs licensing vs planning vs service-request are **separate applications** on one platform.
- Serves city / county / state agencies.

### Granicus SmartGov — evidence layer A

- "A cloud-based license and permit management software that helps governments … manage permitting, licensing, code enforcement, inspections and more."
- "Customize plan reviews and permit routing flows and forms"; "Customize unlimited permit types, forms and requirements."
- "Automated permit flow and approval processes."
- Citizen portal: "submit applications, track permit status and review real-time inspection results 24/7 on any device."
- GIS: ArcGIS integration — "Visualize GIS layers alongside permits, projects, inspections and code enforcement cases."
- Real-time reports on "permit lifecycle, licenses and enforcement cases."
- Mobile: on-site inspections and code enforcement on mobile devices.

### Granicus AMANDA (Permitting, Compliance & Licensing Enterprise) — evidence layer A

- "Hundreds of government agencies rely on [it] as their case management solution"; "manage all business processes (workflows, fees, inspections, reporting, integrations) necessary to successfully operate their regulatory programs"; "deployed in the cloud or on-site."
- Scope: "modernize Permitting Compliance and Licensing (PCL) and Freedom of Information (FOI) processes, including land and construction management and professional and business regulation."
- Inspections digitized for: law and code enforcement, fire prevention and safety, building code, food safety, environmental protection, audit and investigation.
- Licenses/registrations for: businesses, residents, vehicles, animals. Land development and planning activities handled.
- FOI request lifecycle machinery (intake, correspondence, document management, consultations, review and redaction, fee calculations and payment) — bundled into the same enterprise product (Canadian ATIP/FOIPP vocabulary → international/regional pole).
- Success stories: City of Vaughan (permits & licensing), PBOT Portland (right-of-way permits, −60% processing time), Oakville, Coquitlam.

### Cloudpermit (Building Permitting) — evidence layer A

- Product family: Building Permitting / Licensing / Land Use Permitting / Planning & Zoning / Inspections / Code Enforcement / Property Management / Public Works Permitting / Work Orders — **separate products**; "Permitting" groups Building, Land Use, Public Works permitting.
- Building permits: "Accept complete building permit applications and issue permits as soon as payment is processed"; mandatory input fields force complete applications; "Automatically issue eligible permit types after required information and payment are received for routine applications"; track processing times; filter/organize by property, property owner, property ID, parcel ID.
- Application wizard: guided steps — property, party, form, attachment requirements; automatic document-type identification; optional estimated-fee display; "Reduce incomplete applications and unnecessary follow-up."
- Inspections: mobile on-site (phone/laptop/tablet), deficiencies/orders, checklists, schedule additional inspections, dispatch multiple inspectors, "View status of all inspections on a multi-permit site"; offline-capable app; recurring/periodic inspections.
- **Contractor registrations**: online registration showing "up to date on their licensing and insurance"; automatic license renewals; expiry notifications; "Decide which applications must have a contractor before a permit can be submitted" — the license→permit gate, in-product.
- API: "workspaces" (the application record), attachments, inspections data, "bills and fee items", GIS property attributes.
- Configuration: "Change and modify workflows; Manage requirements, including forms, drawings, reviews, and inspections for each type of application; Use templates to create permits, reports, certificates, and other documents in PDF format; Add stakeholders to review and approval processes."
- Municipal portal: branded; "submit permit applications, search records"; public search of permits/projects/records; complaints; sign-in with email/Google/Microsoft.
- Payments: online and over-the-counter; PCI-compliant gateways; escrow account for funds.
- Plan review integrations: Bluebeam, DigEplan. ICC Code Connect integration. GIS integrated maps. Multi-language (EN/ES/FR).

### GovPilot (Construction / Permitting modules) — evidence layer A

- Module catalog under Construction: Building Permit, Construction Permit, Crane, Demolition, Dumpster, Electrical, Elevator, Fence, Floodplain Development, Mechanical/HVAC, Plumbing, Roofing, Septic System, Sign/Banner, Well Construction permits — plus **Certificate of Continued Occupancy, Rental/Resale Certificate, Smoke Detector Certificate** (certificates) and **Contractor Registration, Landlord Registration, Vacant Property Registration** (registrations) sold in the same department module.
- "Enables property owners and contractors to apply for permitting … directly through your government's website"; automated updates "by text message and email, notifying them of the status of applications, reviews, inspections, and permits."
- "Automatically schedule fee collection and inspections"; "Review, inspect, and approve plans."
- Parcel spine: PropertyProfile "displaying parcel level detail including cross departmental records"; "View the status of in-progress permit and registration applications as well as all historical records related to individual properties"; "Cross-reference data with the Planning and Zoning Department in real time."
- Integrations: ICC Code Connect API, General Code eCode360.
- Case study: Bexar County TX septic permits — paper review/approval 30 days → 3 days.

## Cross-product Comparison

| Structure / capability | Accela | Granicus SmartGov | Granicus AMANDA | Cloudpermit | GovPilot | Layer |
|---|---|---|---|---|---|---|
| External applicant submits application of record | ✓ | ✓ | ✓ | ✓ | ✓ | A→B |
| Authority review/routing process ending in official decision | ✓ (multi-dept concurrent review) | ✓ (permit routing flows) | ✓ (workflows) | ✓ (workflows, stakeholders in review/approval) | ✓ (review, inspect, approve) | A→B |
| Issued permit as persistent authorization record | ✓ (issuance in lifecycle) | ✓ (permit lifecycle) | ✓ (PCL case management) | ✓ (issue permits; PDF templates) | ✓ (permits issued/tracked) | A→B |
| Public self-service portal (apply / status / pay) | ✓ | ✓ (24/7 portal) | ✓ (public portal) | ✓ (municipal portal, public search) | ✓ (apply via gov website) | B |
| Fees & payments | ✓ (submission and payment) | ✓ (implied: revenue growth) | ✓ (fees in business processes) | ✓ (online + counter, escrow, fee items) | ✓ (automatic fee collection) | B |
| Inspections attached to permit record | ✓ | ✓ | ✓ | ✓ (dispatch, multi-permit site) | ✓ (scheduling + GovInspect) | B |
| Plan/document review (electronic, markup) | ✓ (concurrent, annotations) | ✓ (customize plan reviews) | ✓ | ✓ (Bluebeam/DigEplan integrations) | ✓ (review/approve plans) | B |
| Configurable permit types / forms / workflows | ✓ | ✓ (unlimited permit types) | ✓ | ✓ (per application type) | ✓ (module catalog) | B |
| Parcel/property/GIS anchor | (implied; not explicit on page) | ✓ (ArcGIS) | ✓ (land management) | ✓ (GIS maps, parcel IDs) | ✓ (PropertyProfile, GIS) | B (3/4 explicit) |
| Status notifications to applicant | ✓ | ✓ | ✓ | ✓ (automatic updates) | ✓ (text/email) | B |
| Contractor/licensing gate on permit applications | — | — | ✓ (licenses & registrations) | ✓ (explicit) | ✓ (contractor registration module) | A (2/4 explicit) |
| Certificates / registrations sold alongside permits | — (separate applications) | — | ✓ (licenses & registrations) | ✓ (certificates via templates; contractor registration) | ✓ (CCO, smoke detector, landlord registration) | A |
| Auto-issuance of routine permits | — | — | — | ✓ (explicit) | — | A (single product) |
| Bundled FOI/public-records machinery | — | — | ✓ (FOI/ATIP module) | ✓ (public records search) | — | A |
| AI intake/review assistance | ✓ (CivicAI) | — | — | ✓ (NoVa assistant) | — | A |
| On-prem deployment option | ✓ (enterprise deployment) | — | ✓ (cloud or on-site) | — (cloud) | — (cloud) | A |

Reading: the first three rows are jointly held across all sampled products (layer B, approaching definitional). Portal, fees, inspections, plan review, configurability are universal-but-standard (layer B). Auto-issuance, FOI bundling, AI are product-specific (layer A, single/dual product).

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

Three structures, jointly held:

1. **The application of record from an external applicant.** A party outside the issuing authority (resident, contractor, builder, business, event organizer) submits a request for authorization to perform a specific regulated activity — construction work, land use, an event, use of a right-of-way, a regulated operation — tied to a specific subject (property, facility, right-of-way, event). The authority holds it as a persistent, individually identified record with applicant, subject, permit type, status. Remove → an online form / generic request tracker; the regulatory-authorization purpose is gone.
2. **The authority's review-and-decision process.** The application is routed through configured review steps — completeness screening, plan/document review, multi-department or multi-reviewer circulation — and ends in an official approve/deny decision made by the authority, not by the system. Remove → a submission inbox; the exercise of regulatory judgment is gone.
3. **The issued permit as the authorization instrument of record.** On approval the system issues the permit — numbered, fee-bearing, commonly carrying conditions and validity terms — and retains it as the persistent record that legally authorizes the activity and anchors everything that follows (inspections, amendments, extensions, close-out, public record). Remove → a decision memo in a ticket system; the "permit" is gone and the product becomes generic approval workflow machinery.

Jointly-held load-bearing tests:
- 1 alone = form builder / request tracker
- 2 without 1 = internal approval workflow (Approval Workflow Platform territory)
- 3 without 1+2 = permit registry / document library
- 1+2 without 3 = request/case management with decisions but no issued authorization instrument (311 / public-sector case management territory)
- 2+3 without 1 = internal permit-to-work (construction safety territory) — no external applicant

The **agency posture** (applicant external to the issuing organization; the system manages the applicants' pipeline, not the organization's own held permits) is part of the Type identity — the discriminator against §21 Environmental Permit Management.

### L1 — Common Mature Structure (standard, not definitional)

- public self-service portal: apply online, track status, pay, upload documents
- fee calculation and payment (online + over-the-counter), receipts
- inspection scheduling and mobile field inspections tied to the permit record
- electronic plan/document review with markup; concurrent multi-department review
- configurable permit types, forms, requirements, workflows per jurisdiction
- automatic status notifications to applicants and involved parties
- parcel/property/GIS integration as the locational spine
- reporting (processing times, volumes, revenue)
- public search of permit records
- contractor registration and license gating of applications
- certificates and occupancy documents issued from the same record

### L2 — Variant / Optional Structure

- department scope: building-only vs multi-department land management vs environmental health vs fire prevention vs public-works/right-of-way vs special events
- jurisdiction scale: small town → city → county → state/province
- deployment: cloud SaaS vs on-prem enterprise
- digital depth: fully digital plan review vs paper-plus; auto-issuance of routine permits (single-product evidence)
- bundled adjacent machinery: FOI/public-records requests (one enterprise product), code enforcement, service requests
- multi-language portals; regional statutory vocabularies (US ICC-based vs Canadian ATIP/FOIPP vs European practice)

### L3 — Vendor-specific (research notes only)

- Cloudpermit: "workspace" as the application-record term; NoVa AI assistant; escrow accounts; estimated-fee display in wizard
- Accela: CivicAI; OpenCounter (guided applicant intake); ePermitHub (plan review); Civic Platform branding
- GovPilot: PropertyProfile; GovAlert/GovInspect apps; population+module pricing
- Granicus: SmartGov "Enhanced" packaging; AMANDA's FOI/ATIP module; Government Experience Cloud framing
- Marketing metrics (900+ agencies, 1,450 municipalities, −60% processing time) — vendor claims, not structural facts

### Rejected Findings (anti-overfit)

- **Fees/payments are NOT definitional.** Universal in the sample, but a fee-free permit office (or a jurisdiction with waived fees) is still permit management; the authorization function does not require payment machinery. Historical check supports: paper-era permit ledgers recorded fee stamps where applicable, not always.
- **Inspections are NOT definitional.** Permit-required inspections are the dominant pattern, but the inspection object stands alone (standalone inspection poles run non-permit programs — corroborates the government-inspection-management pass). A permit product without integrated inspection scheduling still exists in the market.
- **GIS/parcel anchoring is NOT definitional.** Dominant for land-use/building permits, but event permits, right-of-way permits, and facility operating permits anchor to other subjects. The abstract concept is "a specific regulated subject," of which parcel is the most common realization.
- **Public portal is NOT definitional.** Counter-based paper intake satisfies the Type (historical check); the portal is the modern delivery channel.
- **Auto-issuance is NOT definitional** (single-product evidence; held as variant).
- **"Permitting, Compliance & Licensing" as one bundle is NOT definitional** — it is Granicus's packaging; Accela and Cloudpermit ship licensing separately.

## Historical / Market-Sample Check

- **Paper-era permit counter**: application form completed at the counter → routing slip through plan-review desks (building, fire, engineering) → approval signature → fee stamp → permit card written and filed in the permit ledger → inspection records attached → final/close-out. Satisfies all three L0 legs with no cloud, GIS, portal, AI, or payment gateway. The definition holds.
- **Regional/international poles**: AMANDA's Canadian base (ATIP/FOIPP vocabulary; Vaughan/Oakville/Coquitlam) and Cloudpermit's Nordic-origin cloud product fit without US-specific vocabulary. The definition names no statute, code family, or national program.
- **Platform-native**: permitting run inside broader government ERP/GIS suites still realizes the three legs.
- Conclusion: the L0 is era- and region-neutral. No overfit to the current US SaaS pattern.

## Boundary Findings

1. **vs Government Licensing Management (§24, processed — joint-review flag DISCHARGED from this side).** The prior pass recorded the structural test: authorization spent on one job/event = permit; persists as holder standing kept alive by renewals = license. This pass **ratifies the test** with fresh evidence: Accela ships Building (permitting) and Business/Occupational Licensing as separate applications; Cloudpermit ships Building Permitting and Licensing as separate products ("Review and issue licenses, manage renewals" vs "issue building permits"); GovPilot's construction module mixes permits with certificates (CCO — transaction-anchored, permit-like) and registrations (landlord, contractor — standing, license-like), showing the market bundles the patterns under one umbrella while the structural test still separates them. **Interlock documented in-product**: Cloudpermit lets jurisdictions "decide which applications must have a contractor before a permit can be submitted" and runs contractor license renewals — the license gates the permit. **Nuance recorded for the §21 flag**: standing environmental operating permits (renewal-kept authorizations) map imperfectly onto the consumed-by-completion test; on the agency side, environmental-health permits for facilities (Accela Environmental Health application) often recur annually and behave license-like. The seam is the structural test, not vendor packaging; boundary language in the market ("permitting & licensing") is deliberately blurry.
2. **vs Environmental Permit Management (§21, processed — joint-review flag DISCHARGED from this side).** Discriminator confirmed = **whose permits/applications the system manages**: the agency-side platform runs the external applicants' pipeline (this leaf); the permittee-side system manages the organization's own held permit portfolio (§21). Accela's Environmental Health application (agency-side: operators apply/pay/upload/check status on the agency's platform) belongs here, as the §21 pass anticipated. The §21 pass's nuance about standing environmental authorizations is recorded in Finding 1 — it softens the permit/license test at the edges but does not blur the permittee/agency seam, which is clean.
3. **vs Government Inspection Management (§24, processed — seam corroborated).** Permits authorize proposed work; inspections verify actual conditions and record results. Permit-required inspections are a step inside the permit lifecycle here (all sampled products integrate inspection scheduling), but the inspection object stands alone (standalone poles run parks/roads/fire programs with no permit context — prior pass evidence). Vendors ship them as separate products (Cloudpermit Inspections; Accela's inspection machinery inside Building; GovPilot GovInspect app). Corroborated; no conflict.
4. **vs Code Enforcement Management (§24, processed — seam corroborated).** Authorized work (permit) vs violations of rules (enforcement case); shared parcel spine; separate products at all sampled vendors (Cloudpermit Code Enforcement; Accela Service Request/Code products; GovPilot Code Enforcement module). Cloudpermit explicitly links them ("view past building permits on a property" from code enforcement). Consistent with the code-enforcement pass.
5. **vs Planning & Zoning Management (§24, UNPROCESSED sibling — seam recorded for that pass).** Planning & zoning decides land-use entitlements (zoning approvals, subdivisions, variances) — the upstream policy layer; permits authorize and control the execution of approved work. Interlock: zoning/entitlement approval commonly precedes building permits; GovPilot cross-references the Planning & Zoning department in real time; Cloudpermit and Accela ship Planning & Zoning as separate products/applications; AMANDA handles "land development and planning activities" inside the enterprise PCL product (packaging straddle noted). Structural test for the sibling's pass: the managed object is the land-use/entitlement decision vs the work/activity authorization. Some products straddle (AMANDA); the seam rests on the object, not packaging.
6. **vs 311 / Public Sector Case Management (§24).** A service request asks the government to fix something; a permit application asks the government for permission to do something. The decision output differs: service fulfillment vs a legal authorization instrument. Accela ships Service Request Management as a separate application; Granicus ships govService separately from SmartGov/AMANDA. Boundary clean.
7. **vs Government Service Portal (§24).** The portal is the front door (often a module of the permit product — Cloudpermit Municipal Portal, SmartGov citizen portal); permit management is the system of record and decision machinery behind it. Portal without the record/decision machinery = website/forms platform (Granicus OpenForms-class).
8. **vs Approval Workflow Platform / Enterprise Request Management (§10).** Generic approval machinery routes internal requests; permit management adds the regulatory-authorization semantics: external applicants, legal instrument issuance, fee schedules, statutory review steps, public-record status. The L0 test "2 without 1 = internal approval workflow" marks this seam.
9. **vs Construction Safety Management (permit-to-work) (§16).** Internal operational authorization of hazardous work by an employer vs regulatory authorization issued by a public authority to external parties. Same word "permit," different object and posture.
10. **vs Land Records / Cadastre System (§17, processed).** The parcel record is the shared locational spine; the land-records system owns the parcel as its object of record, while permit management references it. Adjacent, not overlapping.

## Uncertainties

- **Conditions-of-approval machinery**: direct product-page evidence is thin (Cloudpermit PDF permit templates; AMANDA clause-pick illustration). Conditions are certainly common in the domain, but this pass could not verify depth (condition tracking, condition-linked inspections) at official-document level. Held as common capability with qualified wording; not definitional.
- **Internal staff workflow depth** (completeness/correction cycles, resubmittal handling): evidenced indirectly (application wizard "reduce incomplete applications"; Accela "fewer resubmissions"; consolidated feedback). Exact stage vocabularies not verified — no authenticated help-center reached.
- **Tyler Technologies and OpenGov** (both major market vendors) could not be fetched (403 ×2 each). Market-coverage claims are weakened accordingly; no memory-filled details were used for them.
- **Fee-rule engines** (fee calculation formulas): referenced by all products but not documented in fetched pages; not stated precisely anywhere in the final document.
- **State/province-level deployments**: Accela claims state agencies; AMANDA claims state jurisdictions; no state-specific workflow evidence fetched.

## Final Synthesis

A government Permit Management application is the issuing authority's system of record for regulatory permits: external applicants submit applications of record for specific proposed activities; the authority routes them through configured review and makes the official decision; the issued permit — numbered, fee-bearing, condition-carrying — is retained as the persistent authorization instrument that anchors inspections, amendments, close-out, and the public record. The defining core is exactly three jointly-held structures (application of record from an external applicant; authority review-and-decision; issued permit as instrument of record) under an agency posture. Portal, fees, inspections, plan review, GIS, configurability, and notifications are the standard mature layer; department scope, scale, deployment, and digital depth are variants; auto-issuance, FOI bundling, and AI assistance are product-specific. The permit/license seam is the consumed-by-completion vs holder-standing structural test (ratified with fresh evidence, with a recorded nuance for standing environmental authorizations); the permittee/agency seam against §21 is the whose-permits discriminator (discharged); the planning/inspection/enforcement seams rest on the managed object, corroborating the prior §24 passes.
