# Research Notes — Organ Transplant Management

Research date: 2026-09-08

## Research Goal

Understand what "Organ Transplant Management" software actually is as an Application Type: what world it models, who uses it, what workflows it carries, and where its boundaries lie against the EHR, the national organ-allocation systems, donor-side (OPO) software, and generic specialty-care management tools.

## Initial Boundary

Working hypothesis before research:

- Core use: a hospital transplant program (kidney, liver, heart, lung, etc.) manages patients across the whole transplant continuum — referral, evaluation, waiting list, organ offers, the transplant event, and lifelong post-transplant follow-up.
- Primary users: transplant coordinators, transplant surgeons and physicians, program administrators/quality staff, plus multidisciplinary roles (social work, dietitian, financial clearance).
- Nearest neighbors: EHR (general clinical record), national allocation platforms (UNet/COTRS class), donor-side/OPO software, Referral Management, Care Coordination, Patient Scheduling, Blood Bank Management.
- Main boundary risk: confusing the center-side recipient-management system with (a) the national allocation platform and (b) donor-side procurement software. These are distinct systems with different operators and purposes, interconnected through donor/offer/waitlist data.

## Research Questions

1. What are the core objects: candidate, evaluation, listing/waitlist, status, offer, donor/organ, transplant event, graft, follow-up?
2. How does a patient enter and progress (referral → evaluation → selection decision → listing)?
3. What does waiting-list management actually involve (statuses, waiting time, updates, removal, reinstatement)?
4. How do organ offers arrive and get decided? Who runs allocation, and what is the center's role vs the allocation authority's role?
5. What happens at and after the transplant event? What is tracked about the graft and the recipient long-term?
6. What regulatory/compliance duties does the software carry (registry reporting, traceability, quality metrics)?
7. What is the role model (coordinators vs surgeons vs physicians vs quality/admin), and which roles drive which workflow?
8. How do living donors and paired exchange fit? Is donor-side management part of this Type?
9. How does the Type relate to the EHR — embedded module vs standalone system?
10. How do national/regulatory regimes (US OPTN/UNet, China COTRS, etc.) shape what the software must do?

## Representative Products

Selection intended to span product philosophy and customer layer:

| Product | Category | Why selected |
|---|---|---|
| HCL Transplant Management | dedicated standalone transplant-program software | long-standing incumbent category representative for center-side management |
| Transplant Connect (iTransplant) | module-based transplant platform | platform philosophy; known to serve transplant centers and OPOs (both sides of the seam) |
| Epic Transplant | EHR-embedded transplant module | the EHR-native variant; boundary case against the general EHR |
| UNet / DonorNet (UNOS) | national allocation platform | boundary reference: the allocation network the center-side system interconnects with — not itself this Type |
| COTRS (China) | national allocation platform (China) | fetched and evidenced allocation-system structure; regulatory-mandate variant |

## Sources

### Fetched and read (evidence used)

- Baidu Baike: 器官移植 (organ transplantation; "科普中国" reviewed entry) — https://baike.baidu.com/item/%E5%99%A8%E5%AE%98%E7%A7%BB%E6%A4%8D — fetched 2026-09-08. Confirms: post-transplant recipients need lifelong vigilance for rejection, regular outpatient follow-up to detect complications (new malignancy, post-transplant diabetes, hyperlipidemia, cardiovascular disease); China had 183 hospitals with organ-transplant qualification as of mid-2023; cross-province medical-insurance direct settlement for post-transplant anti-rejection treatment (Dec 2024).
- Baidu Baike: 中国人体器官分配与共享系统 (China Organ Transplant Response System, COTRS) — https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E4%BA%BA%E4%BD%93%E5%99%A8%E5%AE%98%E5%88%86%E9%85%8D%E4%B8%8E%E5%85%B1%E4%BA%AB%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%B3%BB%E7%BB%9F — fetched 2026-09-08. Confirms: nationally mandated allocation system run under the national health authority; automated organ matching strictly following allocation policy; patients ranked by medical urgency and donor–recipient matching degree; technical exclusion/monitoring of human interference; transparency and traceability as explicit goals; nationwide mandatory use.
- Baidu Baike: 器官获取组织 (Organ Procurement Organizations, OPO) — https://baike.baidu.com/item/%E5%99%A8%E5%AE%98%E8%8E%B7%E5%8F%96%E7%BB%84%E7%BB%87 — fetched 2026-09-08. Confirms (citing 《人体捐献器官获取与分配管理规定》 and related regulations): OPO duties (donor identification/evaluation/maintenance, procurement, transport, handover); OPO enters donor clinical data and legality documents into the allocation system and starts automated allocation there; organs handed over to the transplant hospital holding the matched waiting-list patient; **the regulation explicitly assigns transplant hospitals the duty to maintain the waiting-list (等待者预约名单) in the allocation system**; allocation outside the system is prohibited; full-process traceability (donor chart archive: basic info, evaluation records, informed consent, death determination, ethics approval, procurement record, quality assessment, receipt confirmation); quality metrics include delayed graft function (DGF) and primary non-function (PNF) rates.
- Baidu Baike: 肾移植 (kidney transplantation; "科普中国" reviewed entry) — https://baike.baidu.com/item/%E8%82%BE%E7%A7%BB%E6%A4%8D — fetched 2026-09-08. Confirms: pre-transplant screening classes (contraindications: active hepatitis/cirrhosis, significant coronary disease requiring prior workup, active peptic ulcer, uncontrolled chronic infection, recent/metastatic malignancy — because of immunosuppression); lifelong immunosuppression while the graft functions; post-transplant complication classes (graft non-function, early/late graft function decline, rejection, infection, metabolic complications).

### Not reachable this pass (Source-access Limitation)

Repeated attempts on 2026-09-08 failed: unos.org (403), optn.transplant.hrsa.gov (403), epic.com (403), transplantconnect.com (403), hclsoft.com (empty responses ×2), itransplant.com (transport error), en.wikipedia.org (timeout ×2), web.archive.org (timeout + transport errors), duckduckgo (timeout), r.jina.ai proxy (timeout), bing (index reachable but returns irrelevant results for this topic, both cn and international variants).

Consequences applied:

- No Layer-A (directly observed) vendor product documentation this pass. Vendor module names, precise UI details, numeric limits, status codes, and offer-deadline specifics are NOT asserted anywhere.
- Cross-product Layer-B evidence could not be gathered from product docs. Claims that would normally rest on it are either (a) grounded in the fetched regulatory/clinical sources (Layer A for domain structure), or (b) written as canonical inference (Layer C) with calibrated wording.
- Representative product names are kept as market anchors (category position only); no product-specific capability claims.
- The historical/market-sample check is done structurally (paper-era transplant programs), not via fetched legacy product docs.

## Observations

### O1 — The allocation regime is external, policy-driven, and mandated (Layer A)

Fetched sources (COTRS + OPO entries citing Chinese regulation) establish the structural frame in which this software lives:

- Organ allocation is executed by a designated national allocation system, strictly following written allocation policy; automated matching ranks patients by medical urgency and donor–recipient match criteria; human interference is technically excluded and monitored; allocation outside the system is prohibited.
- The allocation authority (national health administration) mandates system use; OPOs enter donor data and trigger allocation in the system.
- **Transplant hospitals hold the duty to maintain the waiting list (waiting candidates) in/for the allocation system.** The center-side software world therefore includes maintaining allocation-ready waiting-list records.
- The whole chain is designed for traceability (donor chart archive, receipt confirmation, quality metrics).

This frame is stated for China's regime; the same structural frame (an allocation authority operating a mandated matching system; centers maintaining listed candidates; offers decided by centers) is the canonical frame of organ transplantation in jurisdictions with regulated deceased-donor allocation. US-specific parameters (OPTN/UNet specifics) were not fetchable and are NOT asserted at any precision.

### O2 — The center's patient pipeline has a defined shape (Layer A for clinical content; Layer C for software structure)

From the clinical sources (肾移植, 器官移植):

- Pre-transplant: candidates must be assessed for transplant suitability; the screening classes are documented (contraindications across infection, cardiovascular, malignancy, GI, hepatic domains; cardiovascular workup steps named). This is the evaluation-workup domain the software must organize per organ program.
- Waiting: candidates wait while the allocation system matches donors to listed patients; the hospital maintains its waiting candidates.
- Transplant: the organ is handed over to the hospital holding the matched waiting candidate; surgery follows.
- Post-transplant: immunosuppression is lifelong while the graft functions; rejection requires lifelong vigilance; regular outpatient follow-up is required to catch complications (infection, malignancy, metabolic disease, chronic rejection); graft outcome metrics (DGF, PNF) are official quality indicators; graft failure returns the patient to renal replacement / potential re-listing (structurally implied; the fetched sources document dialysis as the pre-transplant condition and graft loss complications, not the re-listing loop explicitly — re-listing held at Layer C).

### O3 — The donor side is a separate organization with a separate record world (Layer A)

The OPO entry documents the donor-side structure: donor identification, evaluation, maintenance, consent paperwork, procurement, transport, handover confirmation, donor chart archive. The donor record world belongs to the OPO; it enters the transplant hospital's world through the allocation handover (matched organ → waiting candidate). OPO software (donor case management) is therefore a different system-of-record world, even where one vendor serves both.

### O4 — Market product structure (Layer C — canonical inference; vendor docs unreachable)

The category's market structure, kept deliberately coarse:

- Dedicated standalone transplant-program management software (long-standing category; center-side).
- EHR-embedded transplant modules (the transplant lifecycle objects added inside the general EHR).
- Platform vendors serving both transplant centers and OPOs (both sides of the donor/recipient seam).
- The national allocation platform operated by/for the allocation authority (not a center product; the interconnecting counterpart).

No product-specific module names, limits, or workflow parameters are asserted.

### O5 — Roles (Layer A for existence of multidisciplinary frame; Layer C for in-software role model)

The clinical sources document the multidisciplinary nature of transplant care (surgery, medicine, immunosuppression management, infection/malignancy surveillance, nutrition, psychosocial). The transplant program's coordination function (pre- and post-transplant coordinators) is the operational backbone of the waiting-list and follow-up workflows. The in-software role model is held at Layer C: coordinators drive list/offer/follow-up mechanics; surgeons/physicians make clinical selection and offer decisions; program administration and quality staff own compliance reporting.

## Cross-product Comparison

Compared at category level (product-level docs unreachable this pass):

| Dimension | Dedicated transplant software | EHR-embedded module | National allocation platform | Donor-side (OPO) software |
|---|---|---|---|---|
| Operator | hospital transplant program | hospital program (within EHR) | allocation authority/consortium | OPO |
| Managed object center | the program's candidates/recipients and their transplant lifecycle | same, realized as EHR-native objects | allocation-wide waiting lists and donor organs | donor cases and procured organs |
| Offer loop | receives/decides offers against its listed candidates | same, EHR-native | executes policy matching; issues offers | triggers allocation; hands over organs |
| Graft/follow-up | core scope | core scope | outcomes reporting only | not applicable |
| In this Type? | yes (canonical form) | yes (variant) | no — related Type (boundary) | no — adjacent Type (boundary) |

Stable across all frames (evidence: O1/O2/O3 fetched sources + structural reasoning): candidate → evaluation → listing → waiting → offer → transplant event → follow-up; allocation always external-policy-driven; traceability duties throughout.

## Canonical Model

### L0 — Defining Invariant (four jointly-held structures)

1. **The transplant candidate of record.** A patient carried by the program as an individually managed candidacy: referral into the program, an organ-specific evaluation workup (clinical screening classes, testing, consults), culminating in an explicit selection/listing decision. Remove → generic patient record / referral log.
2. **The allocation-context waiting list.** Accepted candidates are held as listed waiting patients — with waiting-state management (activation changes, updates, removal/reinstatement) and waiting-time meaning — under the jurisdiction's mandated allocation regime; the program maintains this list as its interface to allocation. Remove → clinic roster with no allocation interface.
3. **The organ-offer loop.** Donor-organ data enters a policy-driven allocation; ranked offers arrive against the program's listed candidates; the program makes and records time-critical accept/decline decisions (with reasons); an accepted offer converts into the transplant event that binds a specific donor organ to a specific candidate (the candidate becomes a recipient). Remove → waitlist clinic tool; the defining allocation interaction is gone.
4. **Post-transplant graft-and-patient continuity.** The transplant event does not close the record: the recipient and graft remain managed — surveillance visits/labs, immunosuppression-era management, complications (rejection, infection, malignancy, metabolic), outcome metrics — and graft failure re-enters the candidacy/waitlist world. Remove → pre-transplant offer tool; "management" ends at surgery.

Jointly-held load-bearing:

- 1 alone = specialty clinic tracker; 2 without 1 = bare waiting-list register; 3 without 1+2 = the allocation platform's own world (or OPO-side); 1+2 without 3 = waitlist clinic management without the allocation interaction; 1+3 without 2 = offers without a maintained list (incoherent); 2+3 without 1 = allocation interface with no care context; 1+2+3 without 4 = pre-transplant system, the continuum broken.

### L1 — Common Mature Structure

- Referral intake/triage and referral-source tracking
- Structured evaluation workup checklists per organ program; multidisciplinary selection-committee meeting records
- Waiting-list data elements for allocation compatibility (blood type, size, tissue-typing/sensitization attributes — exact elements jurisdiction-dependent)
- Offer-management tooling: offer notification/tracking, decline-reason capture, offer logs/audit
- Center-specific organ-acceptance criteria configuration (which offers this program will consider)
- Post-transplant visit/lab schedules, graft-function tracking, rejection episode records, immunosuppression regimen tracking
- Registry/compliance reporting to the allocation authority and regulator; quality-metric dashboards; audit/traceability support
- Financial/insurance clearance steps in the evaluation and listing pipeline (market-dependent prominence)
- Living-donor pathway: living donor evaluation and living-donor→recipient linkage (organ-mix dependent)
- Program role model: pre-transplant coordinator, post-transplant coordinator, transplant surgeon, transplant physician, financial coordinator, social worker, dietitian, quality/program administrator

### L2 — Variant / Optional Structure

- Organ-program mix (kidney / liver / heart / lung / multi-organ; program scale)
- Standalone system vs EHR-embedded module vs suite module
- National regime differences (which allocation system, which policy parameters; mandated-system shapes like COTRS's prohibited-off-system allocation)
- Dual donor+recipient coverage (vendor serving OPOs and centers from one platform)
- Living-donor and paired-exchange depth
- Bridge-therapy status (e.g., mechanical circulatory support in heart programs)
- Patient-facing surfaces (portal access for waitlisted/transplanted patients)

### L3 — Vendor-specific Structure (Research Notes only)

Not asserted this pass beyond category position: specific module names (e.g., waitlist/offer/compliance module branding), exact status code schemes, numeric offer-response windows, specific integrations (lab/paging), branded quality-reporting products. All such detail requires vendor documentation that was unreachable; nothing from memory is promoted into the model.

## Vendor-specific Findings

- None asserted at precision. Category-level positions only (see O4).

## Boundary Findings

- **vs National allocation platform (UNet/COTRS class).** The allocation platform is operated by/for the allocation authority to execute policy matching across all centers and OPOs. The transplant-program system is operated by one hospital program for its own candidates/recipients. The regulation-cited evidence is clean: the hospital's duty is to *maintain the waiting list* and *execute the allocation result* (accept, take handover); the automated matching itself is the authority's system. Remove the center's care-management objects (evaluation, follow-up, graft) and you drift to the allocation platform; remove the allocation-matching execution and you are at this Type. A center product that merely embeds an allocation-system interface is still this Type; the allocation platform itself is not.
- **vs Donor-side (OPO) management.** Donor case management (identification → consent → maintenance → procurement → handover) is a separate record world with a different operator. The two worlds interlock at the handover/allocation result. Some vendors serve both sides from one platform — a coverage variant, not evidence that donor case management belongs to this Type's core.
- **vs EHR.** The general EHR holds the patient's overall clinical record; this Type holds the transplant-lifecycle objects a generic EHR does not natively model: candidacy with evaluation workup, allocation-context listing, offers and their decisions, the graft as a tracked object. EHR-embedded variants exist (transplant module inside the EHR); the seam is whether transplant-lifecycle objects exist as first-class managed records.
- **vs Referral Management / Care Coordination / Patient Scheduling.** Those Types carry generic workflows (referral routing, task coordination, bookings). This Type is defined by allocation-bound candidacy/waitlist/offer/graft semantics; generic workflow support inside it is standard capability, not the identity.
- **vs Blood Bank Management.** Both manage scarce human-derived therapeutic resources under strict regulation. Blood bank = inventory model (pooled, stored products dispensed on request); transplant = unique per-donor organs allocated through policy matching to waiting patients (no inventory shelf; each organ arrives as a one-off matched offer). The allocation object differs fundamentally.
- **vs Clinical Trial Management.** Both carry regulatory reporting and protocolized workflows, but CTMS manages research protocols/subjects; this Type manages care under an allocation regime. Outcome reporting to a registry is a compliance duty here, not a study.

### "去掉什么就变成另一个 Type" 判据

- Remove evaluation/candidacy and follow-up/graft structures, keep list+matching → the allocation platform's own Type.
- Remove allocation-context (listing vs authority, offers) → waitlist-annotated specialty clinic management (falls into generic care coordination/EHR territory).
- Swap the donor-organ offer loop for product inventory dispensing → Blood Bank Management.
- Swap the patient lifecycle for research protocol subjects → CTMS.

## Historical / Market-Sample Check

Paper-era and early-digital transplant programs satisfy the L0 without any modern machinery: candidate chart with typed workup results; a maintained waiting-list ledger (name, blood type, waiting time, status notes); offers arriving by phone/pager and accepted/declined with reasons written down; a transplant event binding donor organ to recipient in the operative record; post-transplant clinic charts with lab schedules and immunosuppression notes; registry report cards. Therefore the definition must NOT include: specific status code schemes, numeric offer-response windows, specific allocation-policy parameters, cloud/AI machinery, or any particular national system's names. These are era/regime machinery. The historical check passes.

## Uncertainties

1. Product-level verification of the named market anchors (HCL, Transplant Connect, Epic Transplant) was impossible this pass; their category positions are stated as market anchors, not as verified capability claims. A future pass with vendor-doc access should verify module structure, role models, and offer-workflow mechanics.
2. US/EU regime specifics (OPTN policy structure, Eurotransplant mechanics) were not fetched; all regime-specific claims in the final document are limited to what the fetched Chinese regulatory frame evidences, generalized only at structural level.
3. Whether every mature product models the "transplant event" as a distinct first-class object vs an EHR surgical encounter — unverifiable this pass; the final document describes it conceptually (binding donor organ to candidate) without claiming implementation form.
4. Depth of living-donor support in dedicated products (core module vs optional pathway) — unverifiable this pass; held at L1/variant strength.
5. Patient-facing surfaces (portal) — held at L2; no evidence gathered.

## Final Synthesis

Organ Transplant Management is the transplant program's recipient-side system of record for the whole transplant continuum. Its identity rests on four jointly-held structures: the managed candidacy (referral → evaluation → selection), the allocation-context waiting list the program must maintain, the organ-offer loop where policy-driven allocation meets time-critical center decisions and the accepted organ becomes a transplant event binding donor organ to candidate, and the post-transplant graft-and-patient continuity (immunosuppression-era management, surveillance, outcomes, re-listing loop). The allocation machinery itself belongs to a different Type (the national allocation platform); the donor case world belongs to OPO-side software; the two interlock with this Type at the offer and the handover. Everything else — checklists, financial clearance, reporting tooling, patient portals, living-donor depth — is common or variant structure, not identity.
