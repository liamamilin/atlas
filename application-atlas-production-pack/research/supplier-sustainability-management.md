# Research Notes — Supplier Sustainability Management

Research date: **2026-09-10**

## Research Goal

Understand what Supplier Sustainability Management software actually is from real products: what sits inside it, who operates it, how sustainability data moves across the buyer–supplier organizational boundary, and what work loops define the Type. Particular duties this pass:

- Ratify the forward flag left by the scope-3-management-platform pass (supplier ESG performance/compliance/ratings vs the emissions account + carbon data collection).
- Answer the joint-review flag left by the supplier-risk-management pass (ESG as centered lens vs ESG as one risk domain; shared due-diligence regimes).
- Leave a forward flag for the unprocessed §21 sibling sustainable-procurement-platform.

## Initial Boundary

Working hypothesis before research:

- Core purpose: the buying organization's (or an assessment scheme's) management of the sustainability/ESG standing of its supplier base — data collection from suppliers, assessment/evaluation, corrective/improvement actions, and feeding procurement/compliance decisions.
- Likely users: sustainability/CSR teams, procurement, compliance; suppliers on the other side.
- Nearest neighbors: Supplier Management Platform (§10), Supplier Risk Management (§10), Supplier Quality Management (§16), Scope 3 Management Platform (§21), ESG Management/Reporting Platforms (§21), Sustainable Procurement Platform (§21, unprocessed), Supplier Portal (§10), Third-party Risk Management (§11).
- Known unknowns: Is there a "standing of record" at the center, or is it a loose bundle of questionnaires? How load-bearing is the corrective-action loop? Is the third-party rating network (EcoVadis) the same Type as buyer-run programs? Where exactly does carbon data collection stop being this Type?

## Research Questions

1. What is the buyer-side center of gravity: a per-supplier record, a campaign engine, or a reporting pipe?
2. What data enters the record, and who supplies it (supplier self-report, third-party assessment, audit, certificates, monitoring signals)?
3. What loops operate over the data: assessment → score → corrective action → re-assessment? Who owns each step?
4. What role do frameworks/standards/regulations play — definitional or variant content?
5. How does the supplier side actually participate (portals, questionnaires, document upload, sharing controls)?
6. How do results connect back to procurement decisions and the commercial relationship?
7. Where is the boundary with supplier risk, scope 3 carbon, supplier management, and ESG reporting?
8. Would older, non-networked, paper-era ethical-trade programs satisfy the definition (historical check)?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer layers:

| Product | Philosophy / pole |
|---|---|
| EcoVadis | Third-party sustainability rating network; assessment performed by the provider, one scorecard shared with many buyers |
| Sedex | Not-for-profit shared data exchange; supplier SAQs + third-party SMETA audits + corrective action reports, shared across buyer relationships |
| Assent | Regulation/program-centered supply chain sustainability & compliance; per-regulation solution packaging, managed supplier engagement |
| IntegrityNext | All-in-one SaaS "supply chain sustainability management": data engine + assessments + risk layer + engagement |
| Prewave | Risk-monitoring-first platform with sustainability/due-diligence as one solution family — the straddle specimen for the supplier-risk seam |

Sedex was originally targeted for direct help-center fetch; the main site and support portals were unreachable (403 / login-gated / transport error ×3). Evidence comes from vendor product pages retrieved via search capture plus a third-party audit-provider page; treated as Tier 2/3 accordingly.

## Sources

- EcoVadis Help Center (Tier 1):
  - What is the EcoVadis assessment process? — https://support.ecovadis.com/hc/en-us/articles/115002653188
  - Setting up a successful sustainability program with EcoVadis — https://support.ecovadis.com/hc/en-us/articles/360015860112
  - Managing My Supplier Network — https://support.ecovadis.com/hc/en-us/articles/14940904327186
  - How to use the Corrective Action Plan feature — https://support.ecovadis.com/hc/en-us/articles/360025780871
  - Help center index (Supplier/Buyer section taxonomy) — https://support.ecovadis.com/hc/en-gb
- Sedex (Tier 2 via search capture; direct fetch blocked):
  - Sedex Platform — https://www.sedex.com/solutions/sedex-platform
  - SMETA audit — https://www.sedex.com/solutions/smeta.audit
  - Sedex homepage — http://sedex.com/
  - Platform & tools update notes — https://www.sedex.com/knowledge-hub/news/sedex-platform-and-tools-update
  - SMETA Best Practice Guidance (PDF, BSI mirror) — SAQ, CAPR, audit flow
  - TÜV SÜD SMETA page (Tier 3 corroboration of the buyer→supplier→auditor→CAPR flow) — https://www.tuvsud.com/en-us/services/auditing-and-system-certification/sedex-smeta
- Assent (Tier 2):
  - assent.com root + Solutions taxonomy (Product Compliance / Sustainability / Trade Compliance), Supplier Engagement services, Platform capabilities — https://www.assent.com/
- IntegrityNext (Tier 2):
  - Homepage — https://www.integritynext.com/
  - Platform page — https://www.integritynext.com/platform
- Prewave (Tier 2):
  - Homepage — https://prewave.com/
- Processed-neighbor context: research/scope-3-management-platform.md, research/supplier-risk-management.md §Boundary Findings (STATUS.md flags).

## Product Observations

### EcoVadis (evidence layer A — Tier 1 help center)

**Buyer side.**
- Help center has parallel Supplier and Buyer trees. Buyer sections: Program strategy & setup; Onboarding your Partners; Monitoring & risk intelligence; Engaging Partners for improvement; Program administration.
- Program setup article frames a procurement-run "trading partner assessment program": buyer provides clean supplier data and quarterly capacity planning for assessment volumes; informs partners before assessment campaigns; follows up with partners who don't act; "consistently integrate EcoVadis sustainability data in the existing procurement processes"; sets performance targets for partners (e.g. reaching a performance level, working a corrective action plan, continuous improvement).
- Network tab ("Managing My Supplier Network"): view partners' scores, an overview of the network's sustainability performance, and per-partner assessment statuses. Statuses include an "Action Required" state where the platform asks the buyer — "the relationship owner" — to personally nudge the partner (phone call, email, meeting) because the partner has not completed the assessment.
- Per-partner assessment has a scope (parent company vs specific site); the buyer can search a Directory of rated entities and request a scorecard share.
- Duplicate/archived partner entries; contact management for both assessment and corrective action plan.

**Supplier side / assessment object.**
- Assessment process: registration (company identity, scope, country/site, size, industry) → customized questionnaire (tailored to size, industry, location; "material sustainability impacts") + supporting documents (evidence referenced against questions; 55-document limit) → expert analysis (sustainability analysts assess answers + documents + 360° news check; methodology "based on international standards such as the Global Reporting Initiative (GRI), ISO 26000, and the guiding principles of the Global Compact") → results published as a scorecard, valid 12 months.
- Scorecards shared automatically with requesting companies; shareable to additional partners while valid; reassessment produces a new scorecard ("a completely new analysis").
- Medals and badges; sector initiatives.
- Corrective Action Plan (CAP): a dedicated section where rated companies manage corrective actions. Scorecard improvement areas auto-generate corrective actions (status: Not started / In progress / Completed / Archived); "general improvement" corrective actions can be requested by requesting companies (with requested due date and a chat thread) or created by the rated company. Action plan fields: assigned-to, due date, description. Documents can be uploaded and linked; default sharing is private, optionally visible to trading partners. Corrective actions do NOT change the scorecard — only reassessment does.
- Carbon Scorecard exists as a separate scorecard with its own improvement areas (e.g. GHG inventory per GHG Protocol) — carbon is one measured topic, not the center.

### Sedex (evidence layer A− — vendor pages via search capture, plus Tier 3 corroboration)

- Self-description: "One platform for human rights & environmental due diligence." Flow: map supply chain → risk screening + targeted questionnaires → verify with SMETA/recognized audits → corrective actions → report.
- Per supplier site: risk rating, audit results, and open corrective actions in one view ("For each factory, farm or facility you can see risk rating, audit results and open corrective actions").
- Self-Assessment Questionnaire (SAQ): standardized disclosure structure completed by the site/supplier; feeds the risk assessment tool; recommended updated at least annually and before audits.
- SMETA audit: third-party audit by approved affiliate audit companies against the ETI Base Code + ILO conventions + local law; 2-Pillar / 4-Pillar scopes; outputs an audit report and a Corrective Action Plan Report (CAPR) uploaded to the platform; non-compliances tracked to closure with owner, due date, evidence upload, possible follow-up audit.
- Sharing across relationships: suppliers link to customers ("request to link"), share SAQ + audit data with multiple buyers, "avoid duplicate audits and carry corrective actions across customers"; 115,000+ supplier sites registered on the platform; buyer can match its supplier list against existing platform data.
- Supplier Directory for finding credible new suppliers by product/country/sector/certification; Site Compliance Report (SAQ completion, membership, audit status, non-compliances, risk scores); customer API to push non-compliance/audit/SAQ data into buyer systems (SAP, Oracle, Ariba, Coupa).
- Sedex is not a certification body — a data platform storing audit reports, corrective actions, self-assessments, risk assessments.

### Assent (evidence layer A− — Tier 2 product pages)

- Self-description: "Product Intelligence for Compliance and Sustainability"; the "Assent Network" connects manufacturers with suppliers for product material compliance, product sustainability, and responsible sourcing.
- Packaging axis is per-regulation/per-program: conflict minerals, extended minerals (cobalt/mica), forced labor, supplier code of conduct, supplier diversity, LkSG/SCDDA, CSRD, CBAM, EUDR, EPR/PPWR, product carbon footprint, ESG reporting — plus product-material compliance (REACH/RoHS/TSCA/PFAS) and trade compliance as sibling families.
- Supplier engagement as an explicit service: "Education, data collection, and technical support for suppliers" — the vendor operates supplier outreach on the buyer's behalf; program management as managed services.
- Data machinery: AI extraction/standardization of supply chain data with human-in-the-loop validation; "audit-ready data" posture; supplier screening; reporting; integrations (SAP, PTC Windchill, APIs).
- Buyer industries: electronics, automotive, aerospace & defense, industrial equipment, medical devices — complex manufacturers.

### IntegrityNext (evidence layer A− — Tier 2)

- Self-description: "All-in-one Supply Chain Sustainability Management"; "supply chain sustainability intelligence & orchestration platform."
- Platform architecture: data & intelligence engine (millions of supplier profiles, auto-enrichment), automated workflows ("collect, validate, and act on risk and sustainability data"), embedded services (supplier onboarding resources; certificate & data validation by expert review + automated checks; capacity building/education to raise supplier ESG maturity).
- Capability set: supplier data collection, assessments, compliance checks; a governed risk layer (continuous evaluation of supplier/product signals → alerts, assessments, actions "with humans in control"); automated follow-up & remediation triggers; news sentiment analysis; AI multi-tier supply chain mapping; smart supplier prioritization.
- Solutions sold from the same platform: supply chain due diligence (CSDDD, LkSG, Norwegian Transparency Act, Swiss act), product compliance (REACH, RoHS, EUDR, conflict minerals…), sustainable procurement, forced labor prevention (UFLPA/EUFLR), carbon emissions (corporate carbon footprint, CBAM), sustainability reporting (CSRD/ESRS), supply chain visibility (multi-tier).
- Integration layer: real-time bi-directional APIs into ERP, SRM, sourcing, risk systems; pre-built connectors (SAP Ariba, Coupa, Ivalua, Celonis).

### Prewave (evidence layer A− — Tier 2)

- Self-description: "Supply Chain Superintelligence"; risk events across languages/networks condensed "into focused, actionable alerts."
- Center: monitoring & alerting (200+ risk types, millions of data points/day), scoring, scoping & rapid onboarding, actions & partners, tier-N transparency, integrations.
- Solutions menu groups: Sustainability (due diligence, product & environmental compliance, forced labour) and Resilience (fast time-to-response, proactive resilience, multi-tier management).
- Market recognition: named a Leader in the 2026 Gartner Magic Quadrant for **Supplier Risk Management Solutions** AND an Innovator in the Verdantix Green Quadrant **Supply Chain Sustainability Software** — a live specimen of the risk/sustainability straddle, packaged with sustainability as one solution family inside a risk platform.

## Cross-product Comparison

| Dimension | EcoVadis | Sedex | Assent | IntegrityNext | Prewave |
|---|---|---|---|---|---|
| Per-supplier standing of record | Scorecard(s) + CAP + document library on platform | Site record: SAQ + audits + CAPR + risk rating | Program records per supplier per regulation/declaration + screening | Supplier profile: assessments, certificates, risk data, actions | Supplier/partner records + scores + event/alert history |
| Supplier-supplied content | Questionnaire + evidence documents | SAQ + audit access + corrective action evidence | Declarations (e.g. CMRT-class), documents, data via campaigns | Questionnaires, certificates, responses | Responses; mostly supplier-registered network |
| Verification posture | Expert analyst review + 360° news check | Third-party audit (SMETA) + risk tool | AI extraction + human-in-the-loop + managed services | Automated checks + expert certificate validation | Continuous AI monitoring + scoring |
| Evaluation output | Scorecard w/ themes+indicators, medals, improvement areas | Risk rating + audit non-compliances | Program/compliance status per regulation | Risk level + assessment results | Supplier risk scores + alerts |
| Corrective/improvement loop | CAP w/ statuses, partner requests, chat, due dates | CAPR actions: owner, due date, proof, closure, follow-up audit | Supplier engagement services + program management | Improvement plans, automated remediation triggers, capacity building | Actions & partners workflow |
| Relationship integration | "Integrate data into existing procurement processes"; buyer-run campaigns w/ targets | Linking, sharing, buyer APIs into procurement systems | Integrations (SAP/Windchill) | Bi-directional APIs into ERP/SRM/sourcing | Integrations into procurement ecosystems |
| Sharing/network posture | One assessment shared with many buyers | Multi-buyer data exchange; avoid duplicate audits | Buyer-private network (vendor-operated outreach) | Buyer programs over a shared supplier data pool | Buyer programs over registered supplier network |
| Carbon content | Separate Carbon Scorecard | Environment pillar in SAQ/audit | PCF/CBAM solutions | Carbon Emissions solution (CCF/CBAM) | — (not core) |

**Stable across the sample (cross-product commonality, evidence layer B):** per-supplier (or per-site) sustainability record; supplier-supplied structured content; some verification/validation of that content; evaluation of the standing against defined criteria; a supplier-owned corrective/improvement loop with deadlines and evidence; buyer-side program management surface; connection of outcomes to procurement processes; sharing/reuse of one supplier's data across multiple buyer relationships.

**Varying (implementation space):** who verifies (analyst vs auditor vs software vs managed service); what is evaluated (composite ESG score vs per-regulation compliance status vs risk rating); network vs private posture; which ESG domains and regulations are packaged in; whether monitoring is continuous (Prewave/IntegrityNext) or assessment-cycle-based (EcoVadis/Sedex).

## Abstraction Levels

### L0 — Defining Invariant

Three jointly-held structures:

1. **The supplier sustainability standing of record.** A persistent, per-supplying-company (or per-site) record maintained on the requesting side's behalf — assessment results/scores, supplier-supplied disclosures, certificates, audit findings, declarations, statuses — that accumulates across assessment cycles and outlives any single request. Remove → a pile of one-off questionnaires/documents (no record).
2. **The two-sided sustainability data/assessment loop across the organizational boundary.** The requesting side structures and initiates sustainability requests (assessment invitations, questionnaires/SAQs, disclosure campaigns, document/certificate requests, audit arrangements); the supplier itself supplies the content; entries are validated or verified (expert review, third-party audit, certificate checks, automated validation) and written onto the standing, refreshed in recurring cycles. Remove → static registry or a survey nobody feeds.
3. **The evaluation → corrective-action loop tied to the commercial relationship.** The standing is evaluated against defined sustainability criteria (scores, ratings, compliance statuses); identified gaps, non-conformances, and improvement areas become supplier-owned corrective/improvement actions with deadlines and evidence-based closure, visible to both sides; outcomes feed the requesting side's decisions about the business relationship (requirements, incentives, escalation, continued business). Remove → a data archive, or a survey tool, or a generic task tracker.

Jointly-held load-bearing checks:
- 1 alone = ESG data/document archive; 2 alone = questionnaire tooling; 3 alone = corrective-action tracker.
- 1+2 without 3 = a collection archive nobody improves against; 1+3 without 2 = stale scoring with no evidence refresh; 2+3 without 1 = scattered requests and actions with no standing.
- All three together are exactly what every sampled product is built around.

### L1 — Common Mature Structure

- Supplier-facing participation surface (assessment portal: questionnaire, document upload, action plan workspace, sharing controls).
- Scoring/rating of the standing with comparative output (scores, medals, risk ratings, compliance statuses).
- Program/campaign management for the requesting side (onboarding partners, batches/campaigns, status tracking, follow-up management).
- Monitoring inputs (news/signal monitoring, certificate expiry, re-assessment reminders).
- Reporting/analytics over the network (coverage, performance distribution, remediation progress, audit-ready outputs).
- Integration into procurement systems (ERP/SRM/sourcing connectors, APIs) so standing data enters sourcing decisions.
- Supplier support/education services (capacity building, onboarding help — in-house or vendor-operated).

### L2 — Variant / Optional Structure

- Verification instrument: third-party expert analysis (EcoVadis) vs third-party audit methodology (SMETA) vs automated/expert certificate validation (IntegrityNext) vs AI extraction with human oversight (Assent) vs managed-service outreach (Assent).
- Network posture: shared third-party rating/data network (one supplier assessment shared by many buyers — EcoVadis, Sedex) vs buyer-private programs (Assent, Prewave, IntegrityNext deployments).
- Regulatory regime content as packaged solutions: LkSG/SCDDA, CSDDD, UFLPA/EUFLR, CBAM, EUDR, CSRD, conflict minerals, PPWR — current realizations, not definitional.
- Carbon/emissions content: Carbon Scorecard (EcoVadis), PCF/CBAM solutions (Assent, IntegrityNext) — one topic among several on the supplier-standing lens; the emissions account itself is the Scope 3 Type.
- Assessment grain: company-level vs site-level (both exist in-sample; both supported by EcoVadis scopes and Sedex site records).
- Multi-tier mapping beyond direct suppliers (IntegrityNext AI mapping, Prewave tier-N) — extension, not core.
- Industry verticals (electronics, automotive, apparel-class schemes) and topic emphasis (human-rights-first vs broad ESG).

### L3 — Vendor-specific Structure

- EcoVadis: 12-month scorecard validity; 55-document evidence limit; medals/badges; "Action Required" partner status; Eva assistant; Select subscription fast-track; sector initiatives; the four-theme scorecard vocabulary.
- Sedex: SMETA 2-Pillar/4-Pillar methodology; ETI Base Code anchor; CAPR as a distinct auditor-produced artifact; affiliate audit company scheme; "Carry corrective actions across customers" phrasing; Site Compliance Report.
- Assent: per-regulation "solution" packaging; "Assent Network"/"Request Manager" branding; Assent University; distributor-experience module.
- IntegrityNext: "intelligence & orchestration layer" phrasing; AI Intelligence Layer with sentiment analysis; Academy; 2M+ supplier profile pool; Verdantix VVD ROI claims.
- Prewave: "superintelligence" framing; 200+ risk types; situation reports; Gartner MQ/Verdantix dual positioning.

## Vendor-specific Findings

(Consolidated from L3 above — none of these enter the canonical document as definitional.)

- EcoVadis's CAP separates "scorecard-based" corrective actions (auto-generated from improvement areas) from "general improvement" requests created by either side — a two-sided action-request mechanism with per-partner privacy of requests.
- Sedex's audit workflow assigns artifact ownership to the auditor (report + CAPR uploaded by the audit company, QC-reviewed), while corrective-action follow-up "sits outside the remit of a social audit" and belongs to the linked buyer–supplier pair — direct vendor-authored evidence that the improvement loop is a relationship structure, not an audit artifact.
- IntegrityNext markets "Sustainable Procurement" as one solution inside the platform — evidence for the seam against the unprocessed sustainable-procurement-platform leaf.
- Prewave carries both risk and sustainability analyst-category recognitions simultaneously — the straddle is packaged, not accidental.

## Rejected Findings

- "Supplier sustainability = a questionnaire tool" — rejected; questionnaires are one collection instrument; the standing + loops are the Type.
- "Supplier sustainability = supplier risk management with an ESG flavor" — rejected; see Boundary Findings (risk lens vs standing/performance lens; Prewave packages them as separate solution families).
- "Supplier sustainability = carbon data collection" — rejected; carbon is one topic here and one account there (Scope 3 pass).
- "Continuous monitoring is definitional" — rejected; EcoVadis/Sedex are assessment-cycle-based and remain canonical.
- "Multi-tier mapping is definitional" — rejected; Tier-1-first is the default in most sampled products; multi-tier is an extension.
- "The supplier portal is the Type" — rejected; the portal is one surface of the loop; the record and loops define it.
- "Data-foundation services (entity resolution/enrichment, Supplier.io-class)" — outside this Type per the supplier-management-platform pass's standing test; recorded as adjacent substrate.

## Boundary Findings

**vs Supplier Management Platform (§10, processed) — keep-both.** SMP centers the supplier population's commercial lifecycle and information standing (entry → qualification → in-life change → exit). Here the centered object is the sustainability standing and its loops; sustainability appears there (if at all) as one qualification domain. Structural corroboration: sampled products here are sold and operated as sustainability programs (dedicated buyer-side program roles, supplier assessment campaigns), not as supplier-record lifecycle machinery.

**vs Supplier Risk Management (§10, processed) — flag RATIFIED from this side; keep-both.** Seam = the centered lens. Risk products center threat evaluation over the supplier base: risk events, likelihood/impact, continuous disruption monitoring, disposition/response. This Type centers the supplier's sustainability standing and its improvement: evidence-based assessment, scores/statuses, corrective actions, supplier development. The overlap zone is real and packaged: due-diligence regimes (LkSG/CSDDD-class) and forced-labor monitoring are sold from both seats (the risk pass recorded Prewave and Sphera; this pass adds Assent and IntegrityNext selling the same regimes from the sustainability seat), and Prewave holds analyst recognitions in both categories simultaneously. But within Prewave the sustainability/due-diligence content is one solution family beside the risk-monitoring center — the market itself separates the seats. Ratified as proposed by that pass: ESG lens as center here vs ESG as one risk domain there.

**vs Supplier Quality Management (§16, processed) — keep-both, parallel structure.** Both Types share the abstract shape "supplier standing of record + two-sided loop + evidence base." The seam is the regime object and its authority: quality standing is conformance of supplied material (approvals gate use of the material; complaints/SCARs attribute product defects); sustainability standing is the supplier organization's ESG performance/compliance (scores/statuses gate relationship and regulatory exposure; corrective actions address organizational practices, not material lots). Vendor packaging corroborates: Assent and IntegrityNext ship sustainability beside quality/compliance as separate solution families.

**vs Scope 3 Management Platform (§21, processed) — flag RATIFIED from this side; keep-both.** Seam = object of work, exactly as that pass proposed. Scope 3 centers the value-chain emissions account: counterpart data collected to compute and improve the organization's tonnage inventory (estimate → primary-data progression), engagement tracked in service of the account. This Type centers the supplier's own sustainability standing: assessments, scores, certificates, audit findings, corrective actions across ESG topics, improvement of the supplier as a counterparty. Overlap confirmed as predicted: supplier data requests and supplier scorecards exist in both. Corroboration from this sample: carbon appears here as one measured topic (EcoVadis Carbon Scorecard; IntegrityNext/Assent carbon solutions), while the account-of-record framing is absent from every sampled product here. Removal tests hold both directions: strip the account and keep supplier programs → this Type remains; strip the supplier-program framing and keep the account → Scope 3 remains.

**vs ESG Management / Sustainability Management / ESG Reporting Platforms (§21) — keep-both.** Those Types center the organization's OWN program data and disclosures; this Type centers external suppliers' sustainability standing collected across the org boundary. Supplier data feeds the buyer's disclosures (CSRD value-chain, due-diligence reporting) as an output capability here, not as the center. Consistent with the esg-reporting pass's cluster note: this leaf is not a fourth name in that naming cluster.

**vs Sustainable Procurement Platform (§21, unprocessed) — forward flag.** Candidate seam: sourcing-decision orientation (sustainability criteria embedded in tenders, sourcing events, supplier selection/contracting decisions) vs this Type's standing-program orientation (data collection, assessment, improvement over the supplier base as such). Evidence touching the seam: IntegrityNext sells "Sustainable Procurement" as a distinct solution inside its platform ("embed sustainability into every decision", "integrate sustainability into sourcing, contracting, and supplier management"); EcoVadis program guidance stresses integrating ratings "into existing procurement processes" and procurement decisions. Joint review recommended at that pass.

**vs Supplier Portal (§10, processed) — consistent.** The portal is the supplier-facing document-exchange surface in front of buyer-side records; here supplier-facing surfaces (questionnaire, CAP workspace, sharing controls) are the operational half of the standing loop, not a generic exchange surface. Overlap of surfaces acknowledged; centers differ.

**vs Third-party Risk Management (§11, processed) — consistent with both processed passes.** Subject universe: any third party under GRC engagement cycles (there) vs the supplying company under sustainability assessment cycles (here). Cyber-led vendor posture belongs to §15.

**vs generic survey/questionnaire platforms (§03.11) — clean.** Generic survey machinery can host a supplier ESG questionnaire but carries no standing of record, no validation/verification posture, no corrective-action-to-relationship loop, no program machinery.

**Adjacency note — product compliance:** Assent and IntegrityNext ship product-material-compliance solutions (REACH/RoHS/substance data) beside supplier sustainability. Supplier-facing declaration collection is shared machinery; the substance-level product-compliance domain is its own territory. Recorded for the taxonomy owner; no directory conflict with this leaf.

## Historical / Market-Sample Check

Paper-era ethical-trade practice satisfies the core: a buyer adopting a supplier code of conduct; supplier questionnaires filled on paper; on-site social audits by second or third parties; audit findings and corrective action plans tracked in supplier files; certificates (SA8000-class) on file; periodic re-audits; purchasing decisions informed by the file. That is: standing of record (the supplier file) + two-sided collection (questionnaire, audit visit, evidence) + evaluation → corrective action → relationship decision. No cloud, no networks, no AI. Shared-rating networks, continuous monitoring, multi-tier AI mapping, and named regulatory regimes are modern additions; the definition does not depend on them. The check passes.

## Uncertainties

- Sedex evidence is vendor-product-page level retrieved via search capture (direct fetches blocked); operational details of Sedex Advance screens are not directly observed. No precise Sedex workflow claims beyond what its pages and the auditor-side documents state.
- No Tier-1 help-center depth for Assent, IntegrityNext, Prewave — product-page level only. Exact workflow states, limits, and defaults asserted nowhere for these three.
- The buyer-side "program" layer (policies, category strategies, incentives) is documented for EcoVadis (Tier 1) and implied elsewhere; its depth in other products is unverified.
- Whether a supplier-sustainability product can fully lack the corrective-action loop (pure rating feed) exists at the data-service edge (rejected finding) but was not deeply sampled.
- Industry-scheme platforms (apparel Higg-class, electronics RBA-class) were not sampled; expected to satisfy the core but unverified.

## Final Synthesis

Supplier Sustainability Management is the requesting organization's system for managing the sustainability standing of its supplier base. The Type stands on three jointly-held structures: the supplier sustainability standing of record (per-supplier/per-site assessment results, disclosures, certificates, audit findings, statuses, accumulating across cycles); the two-sided data/assessment loop across the organizational boundary (structured requests, supplier-supplied evidence, validation/verification, recurring refresh); and the evaluation → corrective-action loop tied to the commercial relationship (scores/statuses against defined criteria, supplier-owned actions with deadlines and evidence-based closure, outcomes feeding procurement and relationship decisions). Mature products add supplier portals, scoring vocabularies, program/campaign management, monitoring inputs, reporting, procurement-system integration, and supplier support services. Verification instruments, network vs private posture, regulatory content, carbon topics, and multi-tier mapping are variant space, not definition. The seams to supplier risk (lens), scope 3 (object of work), supplier management (lifecycle), quality (regime), and ESG management/reporting (whose program) all hold on the object-and-loop structure derived here.
