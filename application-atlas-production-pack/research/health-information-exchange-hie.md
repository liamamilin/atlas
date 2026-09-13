# Research Notes — Health Information Exchange / HIE

Research date: 2026-09-08

## Research Goal

Understand what a Health Information Exchange (HIE) application is as a software/infrastructure Application Type: what exists inside it, who uses it, how exchange actually works, what rules govern it, and where its boundaries lie against adjacent healthcare Types (EHR, care coordination, patient portal, generic data exchange) and against the HIE *organization/network* sense of the same name.

## Initial Boundary (hypothesis before research)

- Core hypothesis: HIE software enables electronic exchange of patient-anchored clinical information across the boundaries of independent healthcare organizations, under a governed participation framework, with some mechanism for knowing that records from different organizations refer to the same person.
- Likely nearest neighbors: Electronic Health Record (single-org system of record), Care Coordination Platform (workflow), Referral Management (workflow object), Patient Portal (patient-facing single-org), Data Exchange Platform (generic data), clinical integration engines (tooling).
- Known unknowns going in: platform vs network vs service packaging; centralized vs federated architecture; consent machinery; patient-facing services; how much analytics belongs to the Type.

## Research Questions

1. What are the canonical exchange modalities (push / pull / notification) and how are they realized?
2. How does patient identity work across organizations (central MPI vs distributed matching)?
3. What is exchanged (documents vs structured data), in what formats?
4. What governance structure wraps exchange (participation agreements, purposes of use, reciprocity, audit)?
5. How is patient choice (consent / opt-out / individual access) modeled?
6. Who are the users, and what surfaces do they touch (clinician portal, EHR-embedded, API, patient portal)?
7. How do the market poles differ: platform vendor vs API-first network vs connectivity service vs HIE operator?
8. What is NOT part of this Type (analytics depth, care workflow, single-org records)?

## Representative Products

Selected for market representativeness, documentation availability, and distinct product philosophies / market poles:

| Product | Pole | Evidence level |
|---|---|---|
| Orion Health (Amadeus / Communicate) | pure-play HIE platform vendor, national & shared-care-record programs | Tier 2 (product pages; deep docs not public) |
| Health Gorilla | API-first interoperability platform + designated QHIN | Tier 1 (developer documentation, multiple pages) |
| MedAllies | connectivity service provider (HISP / Direct, Carequality, QHIN) | Tier 2 (product/service pages) |
| KONZA Health | regional/state HIE operator turned national QHIN services | Tier 2 (service pages, patient resources) |

Domain-defining official source: ONC (US Office of the National Coordinator for Health IT) — "What is HIE?" page, fetched Tier 1.

## Sources

Fetched 2026-09-08:

- ONC — What is HIE? — https://www.healthit.gov/topic/health-it-and-health-information-exchange-basics/what-hie (Tier 1)
- Health Gorilla developer docs (llms.txt index; Health Gorilla in Action; Network Participation; Patient Matching; Data Contribution; Governance; Patient360 Overview; Clinical Alerts; HIN Document Query; IAS) — https://developer.healthgorilla.com/docs/... (Tier 1)
- Orion Health — homepage; /global/solution/shared-care-record/; /global/product/direct-secure-messaging/ (Tier 2)
- MedAllies — homepage / solutions overview (Tier 2)
- KONZA Health — homepage; /products-services/hie-services/; /patient-resources/ (Tier 2)

Unreachable / abandoned (per source-access limitation rules):

- InterSystems HealthShare documentation — docs.intersystems.com requires login and license (1 timeout + 1 login wall) — platform-suite pole evidenced structurally via other samples only.
- eHealth Exchange (ehealthexchange.org) — 403 ×1.
- Orion Health deep operational documentation — not publicly indexed; product-page evidence only.
- No vendor numeric limits, fees, or exact defaults asserted in the final document beyond what fetched pages directly state.

## Product observations

### Orion Health (Amadeus / Communicate) — platform vendor pole

Evidence layer: A (directly observed, product-page level unless noted).

- Markets its HIE platform ("Amadeus") explicitly as a "Health Information Exchange Platform"; the HIE solution page is branded "Shared Care Record" — "Connecting health and wellbeing information across the continuum of care for an integrated, person-centred record."
- Platform consolidates data from disparate systems into a longitudinal person-centric record; modules include Clinical Portal ("secure unified access to all patient data in one clinical view"), Care Pathways, Collaborative Worklists, Medication Management, Reporting and Analytics.
- Sells to shared-care-record / state and national programs globally; cites a US state health information network (North Dakota HIN) as customer.
- Communicate product = Direct Secure Messaging (DSM): encrypted secure webmail requiring no on-premise infrastructure; integrated provider directory ("instantly search, manage, and send messages to verified providers"); XDR cross-enterprise messaging; one-click C-CDA viewing from the inbox; public health reporting via Direct messages; "transfer of care" record sharing between providers, systems, states; messages "encrypted, logged, and reportable"; DirectTrust™ and ONC certified.
- Positioning: "Built on the same Amadeus interoperability foundation" — DSM and the unified record share one interoperability foundation.
- Workflow-extension modules (care pathways, worklists, medication management) are add-ons on top of the exchange/record foundation — evidence that care-workflow tooling is NOT definitional.

### Health Gorilla — API-first network platform pole (Tier 1 documentation)

Evidence layer: A (directly observed, Tier-1 developer docs).

- Self-description: interoperability platform, FHIR-centered, designated QHIN under TEFCA; "centralized integration layer" so organizations "access, contribute, and exchange clinical data without building or maintaining separate connections to each national network."
- **Unified access over many networks**: participates in Carequality, CommonWell, eHealth Exchange, its own HIN, its own QHIN (TEFCA), and state frameworks (California QHIO under DxF). Unified access model "abstracts the complexity of network-specific participation requirements"; framework-specific rules evaluated per transaction.
- **Patient identity (Tier-1 detail)**: demographics are normalized (names, DOB, gender, phone, email, address standardization, 5-digit ZIP) before matching; matching is multi-factor with no single required field (SSN explicitly not required and not sent to networks); the *responding organization* evaluates the query with its own matching logic ("matching methodologies, thresholds, and response behaviors vary by organization and aren't controlled by Health Gorilla"); outcomes: single high-confidence match, multiple candidates, or no match; some networks require exact core demographics + shared contact/address detail; Master Patient Index (MPI) maintains patient links used to route queries; validation differs by intake path (HL7 v2 ADT vs FHIR POST).
- **Record retrieval (pull)**: two patterns — network document query (`/hin/DocumentReference` + `/hin/Binary`: virtual FHIR resources proxying to external networks; returns available documents, typically C-CDA; no normalization, no dedup, not stored) and full retrieval operation (`$p360-retrieve`: asynchronous; retrieves documents, normalizes to structured FHIR, deduplicates/reconciles, stores in tenant, populates a patient chart viewer). Discovery uses record location services (RLS) plus direct routing via MPI patient links; "queries are not broadcast indiscriminately" — routed to systems likely to hold data based on discovery results, MPI links, matching, and responder consent/access controls; results "not guaranteed to be complete."
- **Contribution (push / shareback)**: frameworks "built on reciprocity" — organizations that retrieve are "generally expected to share clinically meaningful data in return"; shareback expectations differ by role (EHR vendors, interoperability platforms, provider organizations); methods: FHIR writes (Patient, Encounter, DocumentReference, Observation, Immunization, MedicationRequest) and C-CDA submission with parsing into FHIR; **responder-only participation** supported (contribute without retrieving) via hosted repository or federated in-place access; participation posture can differ per network.
- **Event notifications**: Clinical Alerts — detection derived from *network document exchange* across care settings; gated by exchange purpose ("detection responds only to a query that another organization submits with the treatment exchange purpose" — payment/operations queries produce no alert); delivery via FHIR Subscription or SFTP; source document available on the chart for licensed organizations; explicitly "does not replace facility-generated HL7 v2 ADT feeds, does not guarantee detection of all encounters, and should not be treated as an authoritative encounter history." Separate ADT Network product delivers facility ADT feeds.
- **Individual access (IAS)**: person-authorized retrieval through QHIN exchange; requires verified identity (signed identity token) + explicit authorization; asynchronous; returns document bundles (C-CDA) or normalized import; "does not generate clinical data, does not modify source records, does not guarantee retrieval of a complete longitudinal history"; deceased-person requests not supported.
- **Governance (Tier-1 detail)**: governance determines who is eligible to participate, which purposes of use are permitted ("most commonly treatment"), how data may be requested/shared/contributed, reciprocity obligations, and compliance monitoring; participation expectations include executing participation agreements, purpose-of-use alignment, HIPAA/TEFCA compliance, contribution where required; oversight: logging/auditability of all exchange activity, periodic or issue-triggered compliance reviews, remediation, suspension/termination, required reporting/attestations to the Recognized Coordinating Entity (RCE); consent management incl. opt-out behavior is part of Patient360.
- Security posture: encryption in transit/at rest, tenant isolation, audit logging; HITRUST / SOC 2 certifications (certifications stated on the overview page).

### MedAllies — connectivity service provider pole

Evidence layer: A (product/service pages, Tier 2).

- Self-description: "connectivity service provider"; operates multiple national networks — a designated QHIN (since 2023), the Carequality network on-ramp ("electronically query records and patient information on demand from Carequality providers"), a Direct Network as an accredited HISP ("accessible, high performance Health Information Services Provider (HISP) platform for seamless and secure communications"), MedAllies Mail (secure provider-to-provider messaging "across the community or across the nation"), and a National Provider Directory ("near real-time updates").
- Combined QHIN + Carequality marketed as one network ("MedAllies Care Enabled Network").
- Serves hospitals/health systems, ambulatory, post-acute/senior living, **health information exchanges themselves**, federal/state government, and health IT vendors — evidence that HIE organizations are customers of connectivity services, not only providers.
- Emphasis: message delivery success ("works directly with other networks and partnering edge systems (e.g., EHRs, HIEs) to ensure messages are delivered, rendered correctly, and actionable"), directory accuracy, certificates, interoperability lab, DirectTrust accreditations (HISP, CA, RA).
- Evidence that a connectivity-service pole exists which is transport- and directory-centric: no repository/record aggregation marketed on its pages — the thin pole of the Type.

### KONZA Health — regional/state HIE operator pole

Evidence layer: A (service pages + patient resources, Tier 2).

- Operates HIE services for eight state/regional health information organizations (e.g., Kansas, South Carolina, Connecticut, New Jersey, Missouri, Louisiana, Mississippi, Georgia) plus national QHIN services ("one of the first Designated QHINs").
- Gateway = "secure online tool … brings together medical records from different sources … creates a comprehensive longitudinal record that unifies data from diverse clinical sources"; Gateway Plus = QHIN access point.
- HIE integration and exchange: HL7 v2 interfaces; CCD exchange ("share and receive CCDs through flexible integrations"); public health reporting routing (electronic case reporting, syndromic surveillance, immunizations, ELR to public health entities, plus disease-specific registries); Query-Based Exchange — "No single network or system contains all health information … pulls data across diverse systems and networks from providers across the nation … connected national and local networks such as eHealth Exchange, Carequality and Designated QHINs."
- Direct Secure Messaging as an HIE basic service ("encrypted email tool").
- RapidAlerts: real-time notifications integrating with clinical/operational workflows (event-notification capability at the operator pole).
- **Patient choice (Tier-2 direct)**: dedicated Patient Resources page — "Participation in HIEs is an individual decision. Opt-Out prevents your information from being available through the HIE. Patients can update their choice at any time and can opt back in." State-specific opt-out instructions (Kansas runs a state opt-out portal; other states via a vendor form).
- Patient portal transition (2026) to a TEFCA QHIN-based system; explains Individual Access Services (IAS): "the specific pathway that lets patients request their records through Qualified Health Information Networks (QHINs), rather than individual hospital portals."
- Analytics (HQ Insights), quality-measure tooling, DAV accreditation services sit beside HIE services — operator value-adds, not exchange core.

### ONC — domain-defining official source

Evidence layer: A (Tier 1, US government).

- Definition: "Electronic health information exchange (HIE) allows doctors, nurses, public health professionals, pharmacists, other healthcare providers, and patients to appropriately access and securely share a patient's vital medical information electronically."
- Standardized data "can seamlessly integrate into the recipient's electronic health record (EHR)".
- Two primary forms currently documented: **Directed Exchange (push)** — send patient information (lab orders/results, referrals, discharge summaries) directly to another care professional, encrypted, among professionals "who already know and trust each other"; also used for immunization data to public health and quality reporting to CMS. **Query-Based Exchange (pull)** — "find and/or request information on a patient from other providers, often used for unplanned care" (ER example: medications, recent radiology images, problem lists).
- TEFCA permitted exchange purposes: Treatment, Payment, Healthcare Operations, Public Health, Government Benefits Determination, Individual Access Services.
- Note: page retains a stray reference to "three forms" while listing two; the historical third form ("consumer-mediated exchange") no longer appears — treated as: current US official framing = two primary exchange forms + patient access realized as IAS under TEFCA.

## Cross-product Comparison

| Structure | Orion Health | Health Gorilla | MedAllies | KONZA |
|---|---|---|---|---|
| Multi-organization participant community | Y (state/national shared-care programs) | Y (multi-network + own QHIN/HIN + state QHIO) | Y (Direct network, Carequality, QHIN; serves HIEs as customers) | Y (8 state/regional HIOs + national) |
| Patient-anchored exchange (documents/records) | Y (C-CDA viewing/sharing; unified record) | Y (C-CDA documents; FHIR resources) | Y (clinical messages/documents between verified addresses) | Y (CCD/HL7 v2/records) |
| Patient identity linkage across orgs | implied (person-centric record; not detail-documented) | Y Tier-1 (normalization, distributed matching, MPI, candidates) | provider-side directory; patient matching not its surface (transport pole) | implied (longitudinal record) |
| Query-based exchange (pull) | (aggregate-centric; query not page-documented) | Y Tier-1 (HIN document query, RLS, targeted routing) | Y (Carequality on-demand query) | Y (explicit, multi-network) |
| Directed exchange (push) | Y (Communicate DSM, XDR, directory) | Y (FHIR writes / C-CDA contribution; shareback) | Y (HISP/Direct core business) | Y (DSM) |
| Aggregated longitudinal record | Y (core of Amadeus offer) | optional (stored/normalized tenant view via retrieve) | N (transport-only pole) | Y (Gateway) |
| Consent / patient choice | not page-documented | Y Tier-1 (opt-out handling; IAS person authorization) | not page-documented | Y (opt-out/opt-in with state specifics) |
| Event notifications | not page-documented | Y Tier-1 (Clinical Alerts + ADT) | not page-documented | Y (RapidAlerts) |
| Public health reporting | Y (via Direct to agencies) | (not core) | not page-documented | Y (eCR/syndromic/imm/ELR) |
| Clinician access surface | Clinical Portal (web) | API + embedded viewer + web access | via EHR/partner edge systems | Gateway web portal |
| Governance / participation framework | implied (trust/standards posture) | Y Tier-1 (agreements, purposes, reciprocity, RCE, suspension) | Y (DirectTrust/TEFCA trust frameworks) | Y (policies; state frameworks) |
| Audit / accountability | Y ("encrypted, logged, reportable") | Y Tier-1 (all exchange logged/auditable) | implied by accreditations | implied by policies |

Reading: all four share the cross-organization participant community, patient-anchored exchange, and a governance/trust wrapper. Identity linkage is explicit and richly documented at the API pole, implied at record-centric poles, and thin/absent at the transport-only pole (where matching happens in the sending/receiving edge systems). Push and pull both appear in three of four; the fourth has push documented. Aggregation, consent surfaces, notifications, and public-health routing vary by pole — strong L1/L2 candidates, not core.

## Canonical Model

### L0 — Defining Invariant (four jointly-held structures)

1. **Cross-organization participant community** — a standing population of independent healthcare organizations (providers, hospitals, labs, HIEs, agencies) connected as participants of one exchange capability. Remove → a within-organization system (EHR territory), not an exchange.
2. **Patient-anchored clinical exchange** — what moves between participants is clinical information about identified patients (documents and/or structured records), not generic messages. Remove → generic secure network / data transport service.
3. **Patient identity linkage across organizations** — the capability maintains, somewhere in the system, the association that records from different participants refer to the same person: via a platform master patient index, via distributed matching at responding organizations, or via the credentialed addressing + provider-directory layer of directed exchange. Remove → records cannot be safely associated with the right person; exchange cannot serve care.
4. **Governed trust framework** — participation is wrapped in enforceable governance: participation agreements, credentialing/identity verification of participants, permitted purposes of use, and auditability of exchange activity. Remove → ad hoc data sharing, not institutional exchange.

Jointly-held is load-bearing: 1+2 without 3–4 = raw document transport; 3+4 without 1–2 = an identity/governance registry with nothing exchanged; 2+4 without 1 = point-to-point sharing (a fax-line successor), not a participant community; 1+3 without 2 = a healthcare directory/index network.

### L1 — Common Mature Structure

- **Two primary exchange modalities plus notifications**: directed/push exchange (Direct-class secure messaging, document handoff between known parties), query-based/pull exchange (discover-and-retrieve across networks), and event notifications (facility ADT feeds and/or exchange-derived alerts).
- **Document-centric payload with structured growth**: C-CDA-class clinical documents as the canonical exchanged artifact, increasingly alongside FHIR-class structured resources; retrieved data can be consumed raw (document) or processed (normalized, deduplicated, stored).
- **Central-or-federated data layer** (both postures valid): an aggregated longitudinal record held in the platform, or a virtual/record-locator posture where data stays at sources and queries are routed — products commonly offer both in some mix.
- **Clinician access surfaces**: web portal over the exchanged record, EHR-embedded access, and programmatic API access.
- **Provider/participant directory**: addressable, credentialed endpoints for sending and routing.
- **Patient-choice layer**: opt-in/opt-out administration honored during matching and exchange.
- **Audit & accountability**: exchange activity logged; compliance review and enforcement mechanisms.
- **Onboarding & integration machinery**: participant connection (interfaces, testing, credentials) as an operational workflow of the application.

### L2 — Variant / Optional Structure

- Operator/packaging pole: state or regional HIO platform, national QHIN services, vendor-run national network, API-first interoperability platform, connectivity-service (HISP) pole, EHR-embedded exchange networks.
- Architecture posture: centralized repository vs federated/virtual vs hybrid.
- Data scope breadth: clinical documents vs adding labs/imaging vs claims/payer-adjacent data.
- Consent regime: opt-out (common US regional pattern, one sample documents state-run opt-out portals) vs opt-in vs person-authorized individual access; jurisdiction-specific consent handling (e.g., a Canadian patient-consent page observed at the API pole).
- National framework participation (TEFCA/QHIN, US-specific; QHIO under a state framework).
- Public-health reporting routing (case reporting, syndromic surveillance, immunization, ELR).
- Patient-facing services: patient portal / individual access services.
- Data-quality services: normalization, deduplication, provenance tagging (depth varies; a transport-only pole performs none).
- Analytics/quality-measure modules (operator add-ons).

### L3 — Vendor-specific (kept out of final document)

- Orion Health: Amadeus/Clinical Portal/Care Pathways/Collaborative Worklists/Medication Management/SMARTSuite module branding; Communicate DSM brand.
- Health Gorilla: Patient360, HIN document query path (`/hin/`), `$p360-retrieve`/`$p360-search` operations, HumanGraph, tenant/license-based C-CDA storage, USCDI coverage claims, sandbox mechanics.
- MedAllies: MedAllies Mail, "MedAllies Care Enabled Network" bundle, Network Council.
- KONZA: Gateway / Gateway Plus / RapidAlerts / HQ Insights branding; per-state opt-out portal links.
- All marketing figures (addresses, organizations, users, message volumes).

## Rejected Findings (considered and NOT promoted)

- "HIE = a national TEFCA QHIN" — rejected: TEFCA is a current US framework layer; regional HIOs, Direct-era services, and non-US shared-care programs satisfy the core without it (historical check).
- "HIE = an aggregated central database" — rejected: the federated/virtual posture and the transport-only pole demonstrate the aggregated record is a common implementation, not the invariant.
- "HIE = analytics / population health" — rejected: analytics appears as adjacent operator modules (and Population Health Management is its own Type); Orion positions workflow modules as extensions on top of the exchange foundation.
- "HIE = public health reporting" — rejected: present at two poles but absent as a core claim at others; it is a routed use case of the exchange, not the defining structure.
- "Patient identity matching must be a central EMPI" — rejected: the API sample documents distributed matching at responding organizations; the directed-exchange pole resolves identity through credentialed addressing. The invariant is the linkage, not its locus.
- "HIE software is only the operator's tool" — rejected: the same core is realized as vendor platforms serving single programs, API platforms serving many tenants, and services serving other HIEs.

## Boundary Findings

- **vs Electronic Health Record (EHR)**: the EHR is one organization's internal system of record and the common source/destination of exchanged data; the HIE is the cross-organization exchange layer. ONC's own framing: standardized exchanged data "integrates into the recipient's EHR." Test: remove cross-organization reach → EHR. EHR-embedded exchange networks (EHR-vendor-run) straddle at packaging level, not structure.
- **vs Care Coordination Platform**: coordination owns workflow (tasks, plans, team communication) around care; the HIE owns the data-exchange substrate. Orion's care-workflow modules are explicitly extensions on top of its exchange foundation — supporting evidence.
- **vs Referral Management**: a referral is a managed workflow object; directed exchange may carry referral documents, but the HIE does not manage the referral lifecycle.
- **vs Patient Portal**: single-organization patient-facing records vs cross-organization exchange. Drift zone: TEFCA Individual Access Services makes cross-organization personal record access a patient-facing HIE service (documented at two samples); when the patient-facing aggregate becomes the product's center, it is patient-portal territory.
- **vs Data Exchange Platform (§13)**: generic any-data exchange vs healthcare-specific semantics — patient identity linkage, clinical document formats, permitted purposes of use, consent, and health-regulatory audit obligations. A generic data exchange has none of these as structures.
- **vs clinical integration engines (message/transport tooling)**: an engine transforms and routes messages; the HIE carries the participant community, identity linkage, governance, and exchange semantics. Engines are components inside realizations.
- **vs the HIE organization / network sense of the name**: "HIE" also names the operator organization and the network frameworks (state HIOs, QHINs, Carequality/eHealth Exchange). The Application Type documented here is the software/infrastructure capability; operator organizations are participants/customers (one sample's own market page lists "Health Information Exchanges (HIEs)" among the customers it serves). Taxonomy note recorded.
- **Standalone Direct/HISP services**: a bare transport service without identity linkage or participant-community machinery is a component/service, at the thin edge of this Type; the connectivity pole sampled here stays in-type because it operates within the network trust frameworks and carries patient-anchored exchange as its business, but its thinness is the Type's lower boundary.

## Historical / market-sample check

- Pre-FHIR/pre-cloud realizations satisfy the core: 1990s community health information networks, HITECH-era (2009–2015) statewide HIEs running Direct + IHE-style document exchange with opt-out consent, and today's shared-care-record programs — all show the four-part core without modern APIs, cloud, or AI.
- The "two primary forms" framing itself shifted over time (an older three-form framing including consumer-mediated exchange is echoed by a stray phrase on the current page); the core does not depend on any specific modality mix — push/pull are modalities of the same exchange core, and patient access appears in every era in some form.
- Regional and jurisdictional variety (US state opt-out regimes, Canadian consent handling noted at one vendor) confirms the consent *regime* is variant-level, while patient *choice* being honored is common-mature.

## Uncertainties

- Orion Health and KONZA evidence is product-page level; their deeper operational behavior (matching depth, consent machinery, audit detail) could not be verified from public sources — assertions kept conceptual for them.
- InterSystems HealthShare (platform-suite pole) documentation sits behind a login/license wall — that pole is evidenced structurally through other samples only.
- MedAllies' consent handling and notification capabilities were not page-documented; not asserted.
- Exact reciprocity rules, purpose-of-use lists, and per-network matching thresholds vary by framework and product; only the TEFCA purpose list (official) and Health Gorilla's treatment-gating (Tier-1) are asserted specifically.
- The market's center of gravity (API-first platforms vs operator platforms) is shifting; the document describes both poles without claiming which dominates.

## Final Synthesis

A Health Information Exchange application is the governed, cross-organizational exchange layer for patient-anchored clinical data. Its defining core is four jointly-held structures: a standing community of independent participant organizations; exchange of clinical information about identified patients between them; linkage of patient identity across those organizations (centralized, distributed, or address-based); and an enforceable trust framework of participation, permitted purposes, and auditability. Around that core, mature products add push/pull/notification modalities, document-and-FHIR payloads, central-or-federated data layers, clinician/patient/API surfaces, directories, consent administration, and audit machinery. The market realizes the Type as platform vendors serving state/national programs, API-first network platforms, connectivity services, and operator-run regional/national HIEs — poles of one Type, not different Types.
