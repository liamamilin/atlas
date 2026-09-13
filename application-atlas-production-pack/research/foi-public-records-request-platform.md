# Research Notes — FOI / Public Records Request Platform

## Research Goal

Understand what a FOI / Public Records Request Platform really is as an Application Type: what the system's world consists of, who uses it, how a request moves from submission to disposition, what rules (statutory, procedural, privacy) shape behavior, and where the boundary lies against records management, open data portals, transparency portals, and generic ticketing/case management.

## Initial Boundary (hypothesis before research)

- A platform used by government agencies / public authorities to receive, log, track, and respond to formal requests for access to records under freedom-of-information / public-records / access-to-information laws.
- Primary users: agency public-records/FOI officers, department coordinators, legal counsel. Secondary: the requesters themselves.
- Confusable neighbors: Government Records Management (lifecycle of the agency's own records), Government Open Data Portal (proactive publication), Government Transparency Portal (publication of performance/agenda info), 311 / Citizen Service Request (service delivery), generic Ticketing / Case Management.
- Unknowns at start: how the requester is modeled (accounts? anonymous?); whether proactive publication is core; whether fee machinery is core; whether the requester-side "make a request to many authorities" model is the same Type or a different one; packaging (module vs standalone).

## Research Questions

1. What is the central object — how is a request defined, and what does its record carry?
2. What is the request lifecycle, end to end? What states does it pass through?
3. How is the requester modeled (identity, accounts, anonymity)?
4. What does the agency-side processing workflow look like (acknowledge, route, collect, review, redact, release)?
5. How are statutory deadlines, extensions, and fee estimates handled?
6. What role does publication play — proactive release of records, public logs of requests, public archives?
7. How do exemption/refusal decisions get recorded and communicated?
8. What reporting/compliance machinery exists (often feeding statutory annual reports)?
9. Where does this Type end and Records Management / Open Data / Transparency / Ticketing begin?

## Representative Products

Selected for market representativeness, documentation quality, product philosophy, and customer-level diversity:

1. **Granicus Records Request Management (GovQA)** — commercial market leader on the agency side; US state/local government, public safety, schools, special districts. Philosophy: compliance automation and deflection at scale.
2. **JustFOIA (MCCi)** — commercial SaaS, US local-government pole. Philosophy: ease of use for the records office; documented feature-by-feature.
3. **Alaveteli / WhatDoTheyKnow (mySociety)** — open-source platform operated by civil-society organizations; requester-side pole; multi-jurisdiction deployments (UK, Kosovo, others). Philosophy: public archive of requests and responses; transparency by default.

Substitution note: NextRequest (open-source-origin city platform) was planned as a fourth sample but all its surfaces (GitHub, product site, live deployments) were unreachable (timeouts / HTTP 403). Abandoned per network-limitation rules; sample stands at three products plus official statutory context.

## Sources

Reached (research date 2026-09-07):

- Granicus — Records Request Management (GovQA) product page: https://granicus.com/product/records-request-management-govqa/ ; Granicus blog on GovQA + Veritone Redact integration: https://granicus.com/blog/govqa-and-veritone-forge-strategic-relationship/ ; public-records solution hub: https://granicus.com/solution/public-records-and-compliance/
- JustFOIA — homepage and Public Portal feature page: https://www.justfoia.com/ , https://www.justfoia.com/product-features/public-portal/ ; feature index (Custom Forms, Correspondence, Workflow Automation, Document Management, Redaction, Payment Portal, Laserfiche Integration, Reporting, SSO, Security)
- Alaveteli (mySociety) — documentation index: https://alaveteli.org/docs/ ; About: https://alaveteli.org/about/ ; Request states: https://alaveteli.org/docs/customising/states/ ; Managing requests: https://alaveteli.org/docs/running/requests/
- FOIA.gov (U.S. DOJ, official context — not a product) — "What is FOIA?": https://www.foia.gov/about.html ; "How to make a FOIA request": https://www.foia.gov/how-to.html

Not reached / limitations:

- NextRequest — github.com and nextrequest.com and live deployment portals all timed out or returned 403. No claims in this research rely on NextRequest.
- GovQA's detailed operator documentation (help center / support portal) was not reachable in this pass; GovQA evidence is from official product/marketing pages, which support capability inventory but not operator workflow precision.
- No precise statutory day counts are asserted anywhere; jurisdiction-specific deadline arithmetic observed in Alaveteli is recorded below as configuration examples only.

## Product Observations

### Granicus Records Request Management (GovQA) — agency-side commercial leader

Evidence layer A (official product page, reached 2026-09-07):

- Positioning: "public records request management" compliance software for state/local governments, public safety organizations, schools, special districts; described as working "across all departments and request types"; part of the Granicus Operations Cloud suite (formerly the standalone GovQA product).
- Customer-centric public portals: intake deflection ("patented predictive intake deflection automatically matches requester searches with 'release-to-all' responses and FAQs"); dynamic intake forms that "collect all needed details (even with anonymous requests)" and "route seamlessly to the correct department for processing."
- Estimates, invoicing, and payments: "automatic estimate conversion creates fully itemized, accounting-aligned invoices and payments with an existing online fee processor or Granicus preferred vendor."
- Secure release: "Secure release with limitable links — deliver responses ... tracking and counting views and downloads with security features that prevent unauthorized, unknown, and expired link-sharing"; release via the public portal to reduce paper/materials costs.
- Duplicate handling: "'Similar Request' alert and link — duplicate requests are automatically identified so staff can work on them together"; "CC Responses" deliver communications and responsive packets to multiple requesters at once.
- Workflow depth: "Request Nesting allows unlimited layers of delegation, collaboration, subrequests, or installments grouped under the original request"; precise assignment and escalation parameters; templates and workflows with individual triggers for notifications, escalations, tracking, oversight reporting; "+Follow" button for trending topics.
- Records processing: "Automatically extract, de-dupe, and search email records" for "any-and-all" requests; "Securely stream, store, redact, transfer, and track video/audio records from inside the solution with no limits in file size or type."
- Security posture (vendor claim): CJIS, HIPAA, NIST, FISMA compliance; redaction "oops!" protection; "full defensible audit trails."
- Success-story framing: e.g. a state patrol agency cited receiving 16,000+ records requests per year; a city cited 500+ requests daily across departments — indicates the volume regime this Type manages (vendor-sourced numbers; product-specific claims).

Evidence layer A (official blog): integration with Veritone Redact for AI redaction of video/audio (PII in body-cam footage); framing of FOIA and "other public record requests"; CJIS-compliant cloud platform.

Layer B (cross-product): intake portal, departmental routing, automation triggers, redaction, release delivery, reporting — shared with JustFOIA.

### JustFOIA (MCCi) — agency-side SaaS, local-government pole

Evidence layer A (official site + Public Portal feature page, reached 2026-09-07):

- Feature inventory: Custom Forms ("paperless process from the start"), Correspondence ("give your inbox a break"), Workflow Automation ("automate tasks and communications"), Any and All Document Management ("extract, review, sort, redact, and respond"), In-App Redaction ("AI-enhanced redaction"), Veritone Redact integration ("never break the chain of custody"), Payment Portal ("invoice and online payments in one interface"), Public Portal ("online portal to submit, track, and search requests"), Laserfiche integration, Security, Single Sign-On, Reporting ("ensure compliance with records request laws"), onboarding/training.
- Public Portal capabilities (requester-facing): submit requests online via agency-configured forms; create an account ("frequent requesters can create an account to see all current and previous requests in one place"); track request statuses; pay invoices by card; download responsive documents ("no more ... thumb drives ... even for the largest of requests"); anonymous requests ("gives anonymous requesters a security key to access their requests"); access previously published records ("publishes high-interest records online proactively so people don't even need to file a request"; "make some or all previous responsive records available online to reduce repetitive requests"); search records by tags (request types such as arrest reports, body cam footage, budgets); legal notices and helpful information; agency branding; ADA compliance (third-party 508 audit of public-facing pages, per company page).
- Problems-the-product-solves list (agency pain points, useful as domain evidence): status phone calls/emails; lack of transparency; large files like body-cam footage; repeated similar requests about high-interest records; high-volume requesters tracking their own requests manually; anonymous requesters unable to check status; accessibility.
- Customer proof (vendor-sourced): city clerk and city-attorney office testimonials about tracking and portal convenience.

Layer B (cross-product): anonymous-with-retrieval-key intake, accounts, proactive publication, payments, redaction, reporting — mirrored in GovQA.

### Alaveteli / WhatDoTheyKnow (mySociety) — requester-side public platform

Evidence layer A (official docs, reached 2026-09-07):

- Model (About page): "citizens use Alaveteli to request information, and the replies are recorded for all to see on the website. Historic requests, along with any resulting correspondence, are archived publicly online." Acts "both as a useful tool for citizens, and as an advocacy tool for right-to-know campaigners." Deployed internationally ("ready to be deployed anywhere in the world"; states "may vary from one jurisdiction to another").
- Request mechanics (Managing requests): a request is automatically created when a user submits and (where necessary) confirms it; Alaveteli sends it to the responsible authority and handles responses. The platform intermediates by email.
- States (Request states page; jurisdiction-dependent, customizable): waiting_response (default initial), waiting_classification (after a response arrives), waiting_response_overdue / very_overdue (automatic when date exceeds request date + holidays + configured day counts — UK example: 20 days, then 40/60 days), waiting_clarification, gone_postal, not_held, rejected, successful, partially_successful, internal_review, error_message, requires_admin, user_withdrawn, attention_requested, vexatious, not_foi, awaiting_description. Overdue transitions trigger user emails and next-step suggestions (e.g., complain).
- Classification: when a response arrives, the original requester is invited to classify the outcome (successful / partially_successful / not_held); after three weeks anyone may classify; administrators can force states.
- Visibility control (Prominence): normal / backpage (URL-visible but unlisted, noindex) / requester_only / hidden — used for privacy problems, vexatious or invalid requests.
- Response intake control: "Allow new responses from…": anybody / authority_only / nobody; old requests auto-restrict (default: 6+ months without activity → authority_only; ~1 year → nobody, effectively closed); rejected responses can bounce, go to a holding pen for admin triage, or be discarded.
- Admin operations: resend request to corrected authority address; move request to a different authority; hide request (not a valid FOI request / vexatious) with or without notifying the requester; delete request entirely (destroys responses) for privacy violations; annotations/comments allowed per request; tags for search.
- Operational reality note (About page): successful deployment "requires constant maintenance" — volunteer/admin moderation is part of the model.

Layer B: the request record with description of records sought, tracked status to a disposition, requester/authority as the two parties, responses of records as the outcome — same skeleton as the agency-side products, seen from the other end of the pipe.

### FOIA.gov (U.S. DOJ) — official statutory context (not a product)

Evidence layer A (official government site, reached 2026-09-07):

- Since 1967, FOIA gives the public the right to request access to records from any federal agency; agencies must disclose unless an exemption applies (nine exemptions protecting interests such as personal privacy, national security, law enforcement).
- Proactive duty: agencies must "proactively post online certain categories of information, including frequently requested records."
- Presumption of openness: withhold only where foreseeable harm to an exemption interest; "take reasonable steps to segregate and release nonexempt information" (partial disclosure duty).
- Request mechanics: request must be in writing and "reasonably describe the records" sought; most agencies accept electronic requests (web form, email, fax); no special form required; requester may specify output format; agencies are not required to create records, conduct research, analyze data, or answer questions.
- Processing: typically in order of receipt; response time varies with complexity and backlog; agencies distinguish simple vs complex requests; requester service centers handle status questions.
- Infrastructure: FOIA.gov aggregates agency FOIA data (annual/quarterly), provides agency contact lookup and a request-letter wizard; agencies report FOIA statistics — compliance reporting is an institutional expectation.

## Cross-product Comparison

| Dimension | GovQA (Granicus RRM) | JustFOIA | Alaveteli |
|---|---|---|---|
| Operator | Agency (state/local, public safety, schools) | Agency (local government pole) | Civil-society intermediary (requests to many authorities) |
| Requester identity | Account or anonymous (dynamic forms) | Account or anonymous with security key | Registered account (site account), public identity by default |
| Intake | Web portal with deflection (matches prior "release-to-all" responses/FAQs) | Web forms (agency-configured) | Web form; platform emails the authority |
| Request record | Yes — logged, nested subrequests/installments | Yes — logged per form | Yes — public page per request with slug URL |
| Status tracking | Yes — triggers, escalations, oversight reporting | Yes — requester self-service tracking | Yes — explicit state ladder incl. overdue arithmetic |
| Correspondence | Yes — CC responses to multiple requesters | Yes — correspondence module | Yes — full thread on the public page |
| Deadline machinery | Escalations/triggers tied to tracking | Compliance reporting against records laws | Overdue states auto-computed (jurisdiction-configured) |
| Fees | Estimates → itemized invoices → online payments | Payment portal (invoices + card payments) | None observed |
| Records gathering | Email extraction/de-dupe/search; video/audio streaming+redaction in-solution | "Any and all" document extraction/review/sort; in-app AI redaction; Veritone Redact integration | Not in scope (authority does the work off-platform) |
| Release delivery | Secure limitable links, view/download tracking | Link to download files, incl. very large files | Published files on the public page |
| Exemption handling | Redaction tooling + audit trails (marketing level) | Redaction (AI-enhanced, chain-of-custody framing) | Authority-side; platform shows redacted/published results |
| Publication posture | Portal releases + "release-to-all" library (records published, requests private) | Proactive publication of high-interest records + tag search (records published, requests private) | Full public archive: requests AND responses by default |
| Duplicates | Automatic similar-request detection, group work | Pain-point framing + published-records deflection | Request history searchable; no auto-dup observed |
| Appeals/internal review | Not directly observed in fetched pages | Not directly observed | internal_review state, first-class |
| Vexatious/abuse handling | Not directly observed | Not directly observed | vexatious / not_foi admin states; prominence controls |
| Reporting | Oversight reporting; automation triggers | Reporting "to ensure compliance with records request laws" | Site-level analytics not observed; institutional reporting outside platform |
| Packaging | Suite member (Operations Cloud) | Standalone SaaS with ECM integration (Laserfiche) | Open-source self-hosted platform |

## L0 / L1 / L2 / L3 Abstraction

### L0 — Defining Invariant (minimal)

A FOI / Public Records Request Platform is recognizable by exactly four properties:

1. **The formal access request as a managed record.** One identified request per submission, carrying the requester's description of the records sought (written, "reasonably describes the records" in the statutory sense), received and logged by the receiving side, persisting through the process. Remove → an email inbox or contact form, not a platform.
2. **An external requester distinct from the processing organization.** The requester is outside the agency's org chart — a citizen, journalist, company, or any party — possibly unidentified; the platform binds the response to the requester and the request, not to an internal employee. Remove → internal case management / ticketing.
3. **A managed processing lifecycle tracked to a formal disposition.** The request is worked through acknowledged → in process → (clarification / extension / fee events) → disposition, with status retained and visible. The statutory clock and its extensions are the characteristic implementation of this tracking, but the invariant is the tracked-until-disposition lifecycle, not any specific day count. Remove → correspondence without memory.
4. **The disposition centers on release of records.** The end state is the provision of records (in full or in part) or a recorded refusal/no-records disposition with reasons. The deliverable is documents/recordings the organization already holds — not a service action, not information created or analyzed anew. Remove → 311 / service request or Q&A.

Historical check (older / regional / platform-native products): the paper-era FOI process — written request, log book or spreadsheet, typed response letter — realizes all four properties without portals, accounts, automated clocks, or redaction software; agencies still accept requests by letter, email, or fax (FOIA.gov). Products that are modules of records-management or ECM suites handle the same four properties inside a broader system. Definition therefore contains no portal, account, link-expiry, fee, or AI machinery — all of that is L1/L2.

### L1 — Common Mature Structure

Very common in current mature products; expected by the market; not definitional:

- Public web portal for intake (forms, guided entry) and requester self-service (status, history, downloads)
- Requester accounts for frequent requesters; anonymous intake with a retrieval key/link for those who decline identity
- Correspondence threads attached to the request record (acknowledgements, clarifications, fee notices, extensions)
- Status ladders with requester-visible states; closed dispositions recorded
- Deadline/extension tracking against the applicable statute (due-date machinery, escalations, compliance reporting feeding statutory statistics)
- Internal routing/assignment to departments; delegation and collaboration on one request (nesting/subrequests in the commercial pole)
- Responsive-records gathering across agency systems (email extraction/de-duplication/search; large video/audio handling)
- Review and redaction tooling (manual, increasingly AI-assisted) with audit trails / chain-of-custody framing
- Fee estimation, invoicing, and payment acceptance
- Release delivery as secure, sometimes expiring, view/download-tracked links
- Deflection: reusable release libraries ("release-to-all"), proactive publication of high-interest records, duplicate/similar-request detection
- Reporting and oversight dashboards (volumes, timeliness, dispositions) aligned to statutory reporting expectations

### L2 — Variant / Optional Structure

- **Operator pole:** agency-side platform (the dominant pole) vs requester-side public platform operated by an intermediary/civil society (Alaveteli family) — the same L0 skeleton viewed from opposite ends; publication posture is the philosophical difference.
- **Publication posture:** records-only publication (proactive release libraries; request threads private) vs full public archive of requests + correspondence + responses (requester-side pole; some agency deployments publish logs).
- **Regime/locale:** FOIA (US federal), state public-records acts, UK FOI/EIR, and other access-to-information regimes — deadline structures, exemption lists, fee rules, and appeal routes differ; state ladders are jurisdiction-configurable (Alaveteli documents per-jurisdiction state sets, e.g., Kosovo's).
- **Scale and segment:** city/county/state/federal agencies, school districts, public safety (high-volume, video-heavy requests, CJIS-class security claims), special districts.
- **Security posture:** CJIS/HIPAA/NIST/FISMA claims and hardened release controls where exempt/sensitive records are routine.
- **AI depth:** AI-assisted redaction, automated email extraction — current-market common, absent in older/open-source generations.
- **Appeals/internal review:** first-class tracked state in the requester-side sample; agency-side handling varies and was not directly observed in the reached pages — treated as optional.
- **Abuse management:** vexatious-requester handling observed directly only in the requester-side sample — optional/variant.
- **Packaging:** standalone SaaS vs suite member vs module of records-management/ECM platforms.

### L3 — Vendor-specific (research notes only)

- GovQA: "Request Nesting", "CC Responses", "+Follow" trending-topic button, "patented predictive intake deflection", "release-to-all" library, redaction "oops!" protection, customer volume claims (16,000/yr state patrol; 500/day city).
- JustFOIA: Veritone Redact integration, Laserfiche integration, "security key" for anonymous requesters (concept may generalize; name is product-specific), llama mascot/brand, 508 third-party audit program.
- Alaveteli: holding pen, prominence ladder (backpage/requester_only/hidden), auto-close timers (6 months authority_only / ~1 year nobody — defaults, configurable), state names (waiting_response_overdue, gone_postal, awaiting_description…), requester-first-then-anyone classification rule (3 weeks), FOI/off-topic determination by admins (not_foi).

## Boundary Findings

- **vs Government Records Management:** RM governs the agency's own records over their lifecycle (classification, retention schedules, disposition, storage). The FOI platform's managed object is the *request*, not the record; records it releases usually live in other systems of record. Remove the external requester and the request machinery → records management. Conversely a records-management module with FOI request tracking (known packaging pattern in some markets) still keeps the request as the worked object — a packaging variant, not a boundary violation.
- **vs Government Open Data Portal:** open data is proactive publication of datasets with no per-request processing, no requester relationship, no deadlines. Remove the request lifecycle → open data portal. The statutory proactive-posting duty connects them (frequently requested records must be posted), which is why release libraries sit comfortably inside this Type.
- **vs Government Transparency Portal:** publishes agendas/performance/finance info; no requester, no per-request processing, no exemptions review. A transparency portal that lets visitors download previously released records is overlapping capability, not the same Type.
- **vs 311 / Citizen Service Request Platform:** service requests seek an action (fix, haul, inspect); FOI requests seek *records that already exist*. The disposition object differs (completed work vs released documents). Remove records-release semantics → 311.
- **vs generic Ticketing / Case Management:** ticketing shares queue/assign/status mechanics, but lacks the statutory frame (deadlines, exemptions, appeal routes), the external-requester identity model (anonymous allowed), and the release-of-records object. Adapted ticketing is a common agency fallback implementation, not this Type.
- **vs Government Service Portal:** the service portal is the citizen's single front door to many government services; a records portal is a single-purpose intake surface. Cross-links exist (records intake embedded in portals) but the processing console is the heart of this Type.
- **vs eDiscovery / Legal Matter tooling:** overlap on search, review, redaction of documents; eDiscovery is matter-scoped litigation work, not standing public access. Adjacent capability donor (review/redaction), not a boundary conflict.
- **"去掉什么就变成另一个 Type"判据汇总:** remove requester-externalness → internal ticketing; remove the request lifecycle → open data/transparency; remove records-release object → 311; remove the agency-processing side but keep everything else → still this Type (requester-side pole).

## Uncertainties

- Agency-side operator workflow precision (exact stage names, deadline configuration UIs, exemption-code libraries) was not verifiable from reached sources; GovQA evidence is marketing-page level. Claims kept at capability level, not workflow level.
- Whether agency-side products universally track internal appeals was not confirmed; only the requester-side sample showed it directly. Kept as optional.
- FOI request handling as a module inside records-management/ECM suites is a known market pattern (JustFOIA's Laserfiche integration hints at it) but was not directly documented in a reached source; recorded as qualified variant, not asserted in the final document.
- Fee regimes vary widely by jurisdiction; only the existence of estimate/invoice/payment machinery is asserted, never fee amounts or triggers.
- The volume figures quoted by vendors (16,000/yr, 500/day) are vendor-sourced and product-specific; not used in the final document.

## Final Synthesis

The Type is best modeled as a **request-lifecycle system of record for statutory access to records**: an external requester (optionally anonymous) files a formal request describing records sought; the platform logs it as an identified record, tracks it through an acknowledged → processed → dispositioned lifecycle (with the statutory clock and extensions as the characteristic timing machinery), coordinates internal search/collection/review/redaction across departments, and ends in a formal disposition that delivers records (full or partial) or a recorded refusal — with a publication layer (release libraries / proactive posting / public archives) as the common modern complement. The requester-side pole (civil-society intermediation with public archives) and the agency-side pole (compliance automation inside the agency) realize the same defining skeleton from opposite ends; publication posture, regime, scale, and packaging are variants. What disqualifies neighbors is structural: no external requester (→ ticketing/RM), no request lifecycle (→ open data/transparency), no records-release disposition (→ 311).
