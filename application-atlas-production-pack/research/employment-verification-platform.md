# Research Notes — Employment Verification Platform

Research date: 2026-09-06
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1

## Research Goal

Understand what an Employment Verification Platform actually is as an Application Type: what objects exist inside it, who operates it, how a verification request flows from a third party to a confirmed answer, what data model underlies the reports, how fulfillment differs across products, and where its boundaries lie against Background Check Platforms, HRIS, identity verification, and the separately-named "employment eligibility verification" (I-9/E-Verify) domain.

## Initial Boundary (hypothesis before research)

- Core purpose: confirm a person's employment and/or income facts for a third party (lender, landlord, next employer, benefits agency) against employer/payroll-sourced records.
- Likely users: verifiers (underwriters, screeners), employees (data subjects), employers (record sources / outsourcers).
- Likely confusions:
  - Background Check Platform (EV is often one component inside one)
  - HRIS (the system of record that often sources the data)
  - Income verification via bank/tax documents (different record substrate)
  - I-9 / E-Verify "employment eligibility verification" (US name collision; different legal object)
- Unknowns: exact fulfillment models across the market; consent mechanics; whether the dominant database model (The Work Number) is directly researchable.

## Research Questions

1. What objects exist? (employment record, verification request, report, consent, employer directory)
2. Who are the parties and what does each one do in the platform?
3. What data gets verified, and in what report shapes?
4. How does data enter the platform (employer deposit / payroll connection / documents / outreach)?
5. What is the request lifecycle (states, routing, cancellation, pricing)?
6. What authorization/consent machinery is structural?
7. What does the employee/data subject see and control?
8. What industries consume the output, and does packaging change the core?
9. Where exactly is the boundary to Background Check Platform and to HRIS?

## Representative Products

| Product | Model | Tier reached | Notes |
|---|---|---|---|
| Truework (Checkr Group) | Verifier platform; multi-method fulfillment (instant database + consumer payroll credentials + human outreach); API + web app | Tier 1 (help center articles, product pages) | Deep documentation; owned by Checkr (background check group) — boundary evidence |
| Argyle | Consumer-permissioned direct-source verification platform (payroll connections via Link); Console + API + PDF reports | Tier 1/2 (developer docs, product pages, consumer pages) | Strong data-set model; consumer-control layer |
| The Work Number (Equifax) | Dominant incumbent database/deposit model | Not reachable | theworknumber.com and equifax.com returned 403 (2 attempts); attested indirectly by Truework's official docs (partnerships "excluding TWN") |
| Experian Verify | Database-model competitor | Not reachable | experian.com 403 |
| Vault Verify | Employer-outsourced VOE service | Not reachable | vaultverify.com 403 |
| Certree | Employer-direct verification | Not reachable | Geo-blocked / JS-only |

Selection rationale: Truework and Argyle give maximal documentation depth and two different fulfillment philosophies (orchestrated multi-method verifier platform vs consumer-permissioned direct-source data platform). The Work Number is retained as a market anchor despite inaccessibility (it is named by sampled products' official docs); no TWN-specific operational claims are made.

## Sources

- Truework help center (Tier 1):
  - https://help.truework.com/hc/en-us/articles/14530538028183 — Report Types: VOI vs VOIE vs VOI(only) vs Reverification
  - https://help.truework.com/hc/en-us/articles/4403451853335 — How does Truework complete every verification (3 methods)
  - https://help.truework.com/hc/en-us/articles/10827198639383 — How to submit a new verification request
  - https://help.truework.com/hc/en-us/articles/360049393333 — Status updates guide (full lifecycle)
  - https://help.truework.com/hc/en-us/articles/4408803758615 — Intro for Employees
  - https://help.truework.com/hc/en-us/articles/4403451702935 — Truework 101 (verifiers)
- Truework product site (Tier 2): https://www.truework.com/ (VOIEA platform, orchestration, coverage, reports, visibility; footer: "© 2026 Checkr Group, Inc. d.b.a. Truework")
- Argyle developer docs (Tier 1):
  - https://docs.argyle.com/overview/how-argyle-works
  - https://docs.argyle.com/overview/data-structure/data-sets (Identities, Paystubs, Payroll Documents, Deposit Destinations, Shifts, Gigs, Vehicles, Ratings)
- Argyle product/consumer pages (Tier 2): https://argyle.com/ , https://argyle.com/consumers (Link flow, Passport, delete-data, authorized-agent framing, industries)
- Access limitations: theworknumber.com, equifax.com, experian.com, vaultverify.com → HTTP 403 (2 attempts each before abandonment for the first two; single attempts for others); certree.com geo-blocked; i2verify.com transport error. Per evidence rules, no operational details are asserted for these products from memory.

## Product A — Truework (Evidence Layer A unless noted)

### Positioning
- "Automated income and employment verification"; self-described "unified VOIEA platform" (Verification of Income, Employment, and Assets). Owned by Checkr Group (background check company) — per footer.
- Verifier-side self-service ("Start a Verification" signup) plus enterprise/API integrations (LOS/POS; Encompass named).
- Use cases framed around mortgage, lending, and background checks for new jobs.

### Report objects (the deliverable)
- **VOE** (Verification of Employment): employee name; employment status (Active / Inactive / On leave / Unknown); employment type (Part-time / Full-time / 1099 Contractor / Unknown); title/position; hire date; termination date; on-leave dates; reason for leaving; "probability of continued employment"; additional notes.
- **VOI** (Verification of Income with Employment): everything in VOE plus current gross base pay + pay frequency, gross earnings (current YTD + two prior years), overtime/bonus likelihood, average hours/week, past/next pay increase dates and amounts, off-work remarks. Active vs inactive handling differs (inactive → wage as of termination date).
- **VOI (only)**: net income, estimated gross income, account balances, income source information — explicitly NO employment information (bank-data variant).
- **Reverification (RVOE)**: re-check at a later point (mortgage closing).
- Mortgage lifecycle framing: pre-approval (VOE) → underwriting (VOE/VOI/VOI-only) → closing (reverification). "GSE-ready" report language.

### Fulfillment methods (3)
1. **Instant Network** — pre-existing records: "exclusive relationships with employers and extensive partnerships with HRIS and payroll systems"; claimed 35M+ employee records; immediate verification.
2. **Credentials** — employee logs into their payroll provider to share data (150+ payroll providers claimed; incl. government payroll, gig platforms, custom F500 payroll). Consent screen; 72h timeout then auto-route or cancel.
3. **Smart Outreach** — human specialists contact the employer's HR directly (phone, email, fax); plus partnerships with third-party verification providers ("excluding TWN" per Truework 101); claimed partner-network pool of 5M records.
- Routing: platform picks method(s) per employer ("learned what works for each"); may run methods in parallel; customer pays a single price per completion regardless of method used.

### Request lifecycle (verifier side)
- Submit: verifier account → applicant fields (name, SSN, DOB) + authorization form → employer selection from a searchable directory (multi-employer requests, up to 10 per applicant) → verification type (employment / employment+income) → cart with total price → payment method → permissible purpose selection (editable; tied to the requester's job role).
- Track: "My Requests" dashboard with real-time per-action status updates; additional-information loop ("Respond" flow); email notifications.
- States observed: request received → additional info required/received → searching instant network → not found → partner network search → awaiting employee approval (partner model) → credentials outreach (email sent → consent screen → consent → payroll login → data retrieved / failures with fallback) → outreach (HR matched → specialist called/emailed/faxed → third-party provider submission → info received) → quality review passed/failed → **report ready** or **request canceled** (user cancellation or auto-cancel at 14 days; fee charged only on completions).

### Employee/data-subject side
- Employee is notified when a request is made and can review the employment information being shared ("You will receive the email and have an opportunity to review the employment information Truework has shared with the verifier").
- Four ways data reaches the platform: employer contracted Truework (outsourced VOE handling); HRIS partnership; employee payroll connection (Credentials); Smart Outreach to employer HR.
- Consumer-permissioned self-service exists: employees can obtain verifications for themselves; gig-economy (1099) verification flows; 2FA; payroll reconnection mechanics.
- FCRA page in footer; "Verifier Identity Verification" article exists (verifiers themselves are vetted).

### Employer side
- "Streamline Employment Verifications" employer product line (outsourced handling of incoming verification requests on the employer's behalf). HR product with login mentioned (details behind login).

## Product B — Argyle (Evidence Layer A unless noted)

### Positioning
- "The consumer-permissioned verification platform": direct-source, real-time income/employment/asset data via consumer-directed payroll and bank connections.
- Explicit market framing: the "old way" = verifications by hand (paystubs, W-2s) and "purchased data from databases — outdated data bought and sold … from credit bureau-based databases"; the "Argyle way" = direct payroll connections with consumer direction.

### Connection flow (Link)
- Select employer/payroll provider from network → log in with existing payroll credentials → platform retrieves data ("in a matter of seconds").
- Link is embeddable (in product), sendable as email/SMS invite, or shareable URL.
- Document upload fallback inside Link: W-2s, 1099s, paystubs, proof of identity/address, misc — used when account data is missing.
- Same connection supports re-verification (refresh) and document-processing workflows (VOI from uploaded documents, "AIM Check-approved").

### Data model (data sets)
- **Identities**: name, birthdate, employer, employment status, employment type, job title, hire date, termination date, termination reason.
- **Paystubs**: gross pay, deductions, taxes, net pay, reimbursements, hours worked, base salary, pay frequency (line-by-line pay data).
- **Payroll Documents**: metadata + PDFs + W-2/1099 OCR data.
- **Deposit Destinations**: where pay is allocated.
- **Shifts, Gigs, Vehicles, Ratings**: work-activity and gig-economy data.
- Field availability varies per connection (field_coverage concept); standardization layer over heterogeneous payroll systems.
- Delivery: Console (no-code), API (+ webhooks), or PDF reports "to streamline income and employment verifications".

### Consumer control layer
- "Authorized agent" framing: acts at consumer's direction; never sells data; service provider pays, not the consumer.
- **Passport**: dashboard of all connections made through Argyle — see connected accounts, review records, adjust sharing, withdraw access at any time.
- Delete-data request form; consumer rights page; WCAG 2.1 AA accessibility of Link.

### Industries (packaging)
- Mortgage (incl. Fannie Mae Day 1 Certainty validation, Asset and Income Modeler), personal lending, government benefits, background check (as an industry it serves), tenant screening, gig economy.
- Integration surfaces: POS, LOS, API, Console. Coverage claims (91% of US workforce, 55%+ verification rate, 80%+ cost savings) — marketing figures, Layer A for existence of claims only.

## Cross-product Comparison

| Dimension | Truework | Argyle | Commonality |
|---|---|---|---|
| Central deliverable | Verification report (VOE / VOI / VOI-only / RVOE), PDF/structured, "GSE-ready" | PDF reports + standardized API data sets (Identities, Paystubs, …) | **Both deliver a confirmation artifact built from employment/payroll data** (B) |
| Data substrate | Pre-collected instant network (35M records) + payroll credentials + outreach | Live consumer-permissioned payroll connections (+ doc upload fallback) | **Both anchor to employer/payroll-sourced records, not self-report** (B) |
| Requester | Third-party verifier (lender etc.) submits request with subject identifiers + authorization + purpose | Service provider (lender/property manager/benefits program) initiates flow that the consumer completes by connecting | **Third-party request + subject authorization is structural in both** (B) |
| Subject's role | Notified of inbound request; can review shared info; can connect payroll; can self-verify | Actively authorizes connection; continuous control; revoke/delete | **Data subject is a first-class party with visible control** (B) |
| Fulfillment routing | Waterfall/orchestration across 3 methods, per-employer learning | Direct-source first, doc-processing fallback; re-verification workflows | **Fallback/alternative fulfillment chains exist in both** (B) |
| Identity matching | Name + SSN + DOB required to target the record | Identity via payroll account login | **Request must be matched to a specific person's records** (B) |
| Pricing | Pay per completed verification; auto-cancel at 14 days, no charge on failure | "Only pay for the data you need when you need it"; provider pays | **Per-verification commercial model** (B) |
| Industries served | Mortgage, lending, background checks | Mortgage, lending, background check, tenant screening, benefits, gig | **Verifier industries cluster: lending, housing, hiring, benefits** (B) |
| Self-service surface | Verifier web app (request form, cart, dashboard) | Console (no-code) + embeddable Link | **Both have a no-code operational surface alongside API** (B) |
| Regulatory posture | FCRA page, verifier vetting, permissible-purpose field | Consumer rights, authorized agent, deletion | **Compliance/consent machinery is product-level structural** (B) |
| Report type taxonomy incl. income-only (bank) variant | Yes (VOI-only from bank credentials) | Direct Banking (VOA/VOAI) as separate line | Income-only/bank-data extensions exist but as *adjacent product lines*, not the employment core (B→L2) |
| Gig-economy support | 1099 verification flows | Gigs/Ratings/Vehicles data sets | Gig variant attested in both (B) |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

1. **Employment records attributed to an identified person, sourced from the employment side** (employers, payroll systems, or parties holding employer-originated data) — not self-reported claims.
2. **A third-party verification request**: someone outside the employment relationship asks for specific employment/income facts to be confirmed, carrying (a) subject identifiers to match the record and (b) an authorization/permissible purpose for the disclosure.
3. **A confirmation deliverable**: the platform resolves the request into a report/structured response of the confirmed facts, in a form the requester can use as decision evidence.

Remove #1 → the product is a letter/form generator or a data broker selling self-reported data (not verification). Remove #2 → it is an HRIS/payroll system or a reporting tool. Remove #3 → it is raw payroll data infrastructure without a verification service loop. The triad is the Type.

### L1 — Common Mature Structure

- Employment data model: employer identity, employment status, employment type (incl. contractor), job title, hire/termination dates; income: base pay, pay frequency, gross earnings history.
- Report shapes: employment-only, employment+income, income-only, re-verification of an earlier report.
- Request lifecycle with tracked statuses: received → matched/routed → (subject consent / data retrieval / outreach) → quality review → completed report or canceled.
- Multiple fulfillment methods with fallback ordering; coverage/employer-directory lookup.
- Verifier-facing self-service surface (web app / console) + API and system integrations (LOS/POS/ATS-style).
- Subject-facing surfaces: notification of requests, consent screens, payroll-connection flow, connection dashboard, data deletion.
- Per-verification pricing; fee only on completion in at least one major product (product-specific mechanic).
- Employer-facing participation: record contribution/partnerships or full outsourcing of verification handling.
- Compliance machinery: permissible purpose, verifier vetting, FCRA posture (US-centric sample).

### L2 — Variant / Optional Structure

- **Fulfillment philosophy**: pre-deposited database (bureau incumbents) vs consumer-permissioned direct connections (newer platforms) vs human outreach/service desks vs document-based verification vs government wage data (regional).
- **Scope extensions**: assets (VOA), document processing, gig-economy data (shifts, gigs, ratings), tax documents (W-2/1099).
- **Industry packaging**: mortgage (re-verification at closing, GSE validation programs), consumer lending, tenant screening, background-check embedding, government benefits.
- **Commercial model**: verifier pays per report; provider pays (platform charges the business, consumer free); employer pays for outsourced handling.
- **Ownership/packaging**: standalone platform; API-embedded data product; subsidiary of a background-check group; product line of a credit bureau; HR/payroll-suite add-on.
- **Regional/regulatory regime**: US FCRA-centric in this sample; other markets structure consent and data sources differently (unverified here).
- **Identity substrate for matching**: government ID numbers vs payroll-account authentication.

### L3 — Vendor-specific (Research Notes only)

- Truework: named methods (Instant Network, Credentials, Smart Outreach), 14-day auto-cancellation, 72h credentials timeout, "up to 10 employers per request", single-price-per-completion, Encompass integration, GSE coverage article, 35M/5M record figures.
- Argyle: Link, Passport, Console, AIM Check, Day 1 Certainty / Asset and Income Modeler positioning, named data sets (Deposit Destinations, Shifts, Gigs, Vehicles, Ratings), WCAG 2.1 AA statement of Link, coverage percentage claims.
- The Work Number: no operational details captured (inaccessible); only its existence/role in the ecosystem is attested via Truework's "excluding TWN" partnership note and general market framing of "credit bureau-based databases".

## Vendor-specific Findings

- Checkr Group's ownership of Truework (footer) is direct evidence that background-check groups acquire EV platforms — supports the "EV is consumed by background check platforms" boundary rather than an alias relation.
- Argyle's "old way" narrative (manual documents; bureau databases) is a competitor's characterization — used only as evidence that these older patterns exist and are the market's incumbent strawman, not as a factual description of any specific incumbent.
- Truework's "probability of continued employment" field is a report field, not a platform capability to model.

## Boundary Findings

1. **vs Background Check Platform**: EV platform's world is one fact domain (employment/income) confirmed against payroll/employer records. Background check platforms orchestrate many fact domains (criminal, MVR, education, identity) with adjudication workflow; EV is one input they consume. Evidence: Argyle lists "Background Check" as an industry it serves; Truework is owned by Checkr and described as its verification infrastructure. Test: remove multi-domain orchestration and adjudication — EV remains; add criminal/MVR/education checks — it becomes a background check platform.
2. **vs HRIS**: HRIS is the employer's system of record and may generate self-service verification letters for employees — but it has no external-verifier request loop. EV platforms source FROM HRIS/payroll partnerships. Test: remove the third-party verifier request loop → HRIS capability.
3. **vs Identity Verification / KYC**: those establish *who someone is*; EV confirms *employment/income facts about someone*. EV requests contain identity attributes for record matching, not for identity establishment.
4. **vs Income verification via financial documents / open banking**: different record substrate (bank accounts, tax transcripts vs employer/payroll). Products blend them (VOI-only from bank data; Direct Banking lines), but the employment-anchored confirmation against employer-sourced records is this Type's core; purely financial-document verification without the employment record anchor is a different Type.
5. **vs Employment Eligibility Verification (I-9/E-Verify)**: US name collision. E-Verify confirms work authorization with a government system; this Type confirms employment history/income for third parties. Completely different object, parties, and rules. No directory leaf exists for the eligibility domain, but future work should not merge them.
6. **vs self-reported résumé/candidate data**: EV's defining property is employer-side sourcing and confirmation; a candidate-profile platform with self-reported history is not this Type.

Historical/market-sample check (§24): older and non-digital patterns — HR departments answering phone/fax requests manually (still observable today as the "outreach" fulfillment method), outsourced VOE bureaus, and pre-connected verification letters — all satisfy the L0 triad (records held by the employer/agent, third-party request with authorization, confirmed response letter). HRIS self-service letters and government wage-data programs fit only if the third-party loop and confirmation deliverable exist; otherwise they are capabilities of other Types. The L0 abstracts away the digital substrate (database vs connection vs fax) and the US FCRA framing.

## Uncertainties

- The dominant incumbent (The Work Number) could not be observed directly; its deposit/report mechanics are NOT characterized here. If later research gains access, verify: report shapes, consent model (does the employee see inbound requests?), dispute/freeze features, fee direction.
- Regional (non-US) EV platforms were not sampled; L0's consent framing is calibrated to the US sample.
- Whether "employer pays for outsourced verification handling" is a large distinct segment or a packaging variant of the same platforms (Vault Verify/Certree would have clarified; both inaccessible).
- Exact coverage/record-count figures are marketing claims and were deliberately excluded from the final document.
- The degree to which government benefits verification (Argyle industry page) uses government wage data vs payroll connections is unclear from accessible sources.

## Final Synthesis

An Employment Verification Platform is the system of record for *third-party confirmation of employment facts*: it holds or reaches employer/payroll-sourced employment and income data for identified individuals, accepts verification requests from outside parties (each request carrying subject identifiers and an authorization/purpose), resolves each request through one or more fulfillment methods — pre-collected records, consumer-permissioned payroll connections, documents, or direct outreach to the employer — and delivers the confirmed facts as a report the third party uses as decision evidence. The employee/data subject is a structural party with consent, review, and revocation surfaces. The Type is distinct from background check platforms (which consume it), from HRIS (which feeds it), and from income verification via financial documents (a different record substrate frequently bundled alongside it).
