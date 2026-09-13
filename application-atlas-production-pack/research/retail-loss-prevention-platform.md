# Research Notes — Retail Loss Prevention Platform

Research date: 2026-09-07
Slug: retail-loss-prevention-platform
Directory leaf: Retail Loss Prevention Platform (05.25 Retail Loss Prevention)
Sibling leaf in same group: Retail Shrink Management (not processed here)

---

## Research Goal

Understand what a Retail Loss Prevention Platform actually is as a software Type: what objects exist inside it, what workflows it runs, who uses it, and where its boundaries lie against neighboring Types (Retail Shrink Management, Fraud Detection Platform, Corporate Investigation Management, Retail POS, Video Management Systems, Retail Inventory Management).

## Initial Boundary (hypothesis before research)

- Hypothesis: software used by retail Loss Prevention / Asset Protection (LP/AP) teams to detect loss signals (mostly from POS transaction data), record loss events (theft, fraud, error, waste), manage investigations, and coordinate prevention (audits, coaching, law-enforcement collaboration).
- Likely confusion points:
  - Retail Shrink Management (sibling leaf) — measurement/program layer vs. event/response layer
  - Fraud Detection Platform — payment/card fraud vs. retail loss events
  - Corporate Investigation Management — legal/corporate investigations vs. retail-loss investigations
  - Video Management Systems — cameras vs. loss events
  - Retail POS — transaction creation vs. loss detection over transactions

## Research Questions

1. What are the core objects? (incident, case, exception, alert, subject, evidence, recovery, disposition)
2. How does exception-based reporting (EBR) work over POS data?
3. What is the case/incident lifecycle and what dispositions exist?
4. What roles use the system (LP analyst, investigator, field leader, store manager, executive)?
5. How does law-enforcement and cross-retailer collaboration work?
6. What integrations exist (POS, video/VMS, EAS/alarm, HR, inventory, e-commerce)?
7. Where do audits/compliance fit?
8. What metrics matter (shrink, close rate, time-to-close, recovery)?
9. Where is the boundary vs. shrink management, fraud detection, investigation management, VMS?

## Representative Products

| Product | Philosophy | Segment | Evidence quality |
|---|---|---|---|
| Agilence | Analytics-first (exception reporting) + case management + audits | Mid-to-large retail, grocery, restaurant, convenience, pharmacy | Tier-1/2 product pages, 4 pages fetched |
| ThinkLP | Case-management-first "Loss & Safety Intelligence Platform" (cases + audits + EBR + ORC + HR + safety) | Fortune-100 to mid-market, 120+ countries claimed | Tier-1/2 product pages, 2 pages fetched |
| Auror | Crime-intelligence/network-first (incident capture → connection → investigation → law-enforcement collaboration) | Large enterprise retailers + law-enforcement agencies (AU/NZ/NA/UK/IE) | Tier-1/2 product pages, 2 pages fetched |
| Appriss Retail | "Total Retail Loss" suite (returns/claims + shrink & exception analytics + case & audit management) | Top-100 US enterprise retailers | Root page only — subpages returned 503 (see Sources) |
| Solink | Video-first (AI vision/VMS platform with LP use case) — sampled as boundary/variant evidence | Retail, restaurant, convenience, cannabis | Root page only |

## Sources

Fetched 2026-09-07:

- Agilence — https://www.agilenceinc.com/ (root)
- Agilence — https://www.agilenceinc.com/platform (Analytics)
- Agilence — https://www.agilenceinc.com/platform/case-management
- Agilence — https://www.agilenceinc.com/audit-management
- ThinkLP — https://www.thinklp.com/ (root)
- ThinkLP — https://www.thinklp.com/lp-case-management/
- ThinkLP EBR detail page — https://www.thinklp.com/?page_id=905 → 404 (not fetched; EBR evidence from root page)
- Auror — https://www.auror.co/ (root)
- Auror — https://www.auror.co/product/overview
- Appriss Retail — https://apprissretail.com/ (root) — OK
- Appriss Retail — https://apprissretail.com/incident/ → 503 (×2), https://apprissretail.com/secure/ → 503 (×1) — abandoned per source-access rule
- Solink — https://www.solinkcorp.com/ (root; redirects to solink.com)

Source-access limitation: no live help-center / user-guide articles were reachable for any sampled product (Agilence, ThinkLP, and Auror publish marketing/product pages rather than public help centers; Appriss subpages 503'd). All evidence is from official product/marketing pages (Tier 2). Consequence: assertion strength is calibrated to product-page level; no precise operational parameters (numeric thresholds, exact state names, plan gating) are asserted anywhere. Appriss observations are root-page-only and treated as reduced-strength evidence.

---

## Product Observations

### Agilence (evidence layer A unless noted)

Positioning: "Loss Prevention Analytics & Reporting"; "Stop Preventable Loss Before It Reaches Your P&L"; unifies transactional data across channels/locations; AI identifies anomalies/patterns/behaviors.

Platform structure: Analytics (+ "Analytics Plus"), Case Management, Audit Management, AI, Modules, Integrations.

Analytics (exception reporting):
- Integrates "all types of data including POS, customer, eCommerce, inventory, video, RFID, and more".
- Capabilities: custom report builder; alerts & notifications reviewed in a centralized view ("determine whether it's legitimate fraud or a false alarm"); editable dashboards; custom query builder with saved queries.
- Extending modules (each a datasheet): eCommerce, Inventory Adjustments, Direct Store Delivery, Scale Production, Physical Inventory, Expiring Inventory, RFID, Alarm, Cash Over/Short ("monitor and analyze cash handling variances across registers and employees").
- AI: "continuously adapts to the unique patterns, risks, and behaviors specific to your locations, your employees, and your customers"; natural-language queries.

Case Management:
- "Track, document, and analyze all the details surrounding your investigations"; incidents, investigations, and accidents.
- Case creation via Natural Language Queries; create new cases or search for and add to existing ones within Agilence Analytics (exception → case linkage with supporting data auto-included).
- Link cases and identify connections between incidents and investigations; "easily expand investigation scope, see ORC cases more clearly".
- Evidence centralization: "video, photo, or written form, all in one place"; video snippets sendable/reviewable.
- Share case information with local law enforcement.
- Tasks & subtasks with due dates; hours tracked per case; calendar & timeline views; watch list; personalization; complete case history with timestamps ("solid audit trail"); desktop & mobile.
- Reports & dashboards over case data; close rates and time-to-close averages reported to leadership.

Audit Management:
- Audit/compliance tool for multi-location brands: brand standards, health & safety requirements, operational policies → audits executed in the field.
- Form building with question types and scoring (AI/NLQ-assisted); dynamic scoring; unlimited audits; mobile execution; real-time push of audit changes; AI automations create tasks/emails from audit triggers; problem detection & insights; recurring audits.

Industries: retail, restaurants, grocery, convenience, pharmacies (diversion programs, controlled substances), hotels.
Roles addressed: Loss Prevention, Operations, Finance, Marketing, Executive Leadership.

### ThinkLP (evidence layer A)

Positioning: "Loss & Safety Intelligence Platform"; "Run your entire department and centralize your data".

Products: Case Management, Complex Investigations (ORC), Smart Audit, Think360, Reporting & Dashboards, Partners & Integrations. Use cases: LP & AP, ORC, Risk & Safety, HR.

Case Management:
- Enter incidents & accidents: "track all your cases, incidents, investigations, and accidents all in one central location".
- Flexible data capture: "stores, web, mobile, hotlines, exception reporting, text messages, and more".
- Templates or custom case forms; drag-and-drop workflow configuration "from intake to closure. No developer required".
- Investigation: upload photos/documents/videos; notes; anonymous report entry; change tracking on investigation records; task assignment.
- Linking cases: "tying together suspects, vehicles, boosters, fences, and other evidence"; auto-surface potentially related cases on entry; pre-formatted evidence exports for law enforcement.
- Incidents & accidents: injury reports; every location can file directly; auto-import from insurance carriers and TPAs; root-cause-analysis forms triggered by configurable criteria; heat maps and alerts for natural disasters; OSHA regulatory filing module.
- Workflow automation & approvals: centrally managed approval processes; outstanding approvals in one place.
- Civil recovery & restitution: "fully automate and manage an entire recovery and restitution management program"; automatic notices to customers, payment tracking, reminders; restitution tracked on cases (testimonial: "tracks restitution payments").

Smart Audit:
- Compliance audits desktop/mobile "from simple checklists to complex assessments"; dynamic assignment to locations/employees; OSHA compliance; scoring system driving actions based on responses.

EBR & Analytics:
- "Bring Your POS, E-Commerce, Inventory, And Other Big Data to Life"; exception reporting with real-time analysis and alerts "based on our best-in-class AI models"; inventory analytics; POS exceptions ("detect, review, and receive real-time alerts on suspicious patterns in your transaction data"); omnichannel loss data from any source.

Other: HR case management (HR cases, background checks, training); Risk & Safety (multi-site incidents, disaster alerts, business continuity); Seymour AI / Front of Store Insights; marketplace of partners/integrations.

### Auror (evidence layer A)

Positioning: "Retail Crime Intelligence" platform; "turns isolated incidents into positive outcomes"; network of retailers + law enforcement (claims 85,000+ stores, 3,500+ LE agencies — vendor claim, not independently verified).

Auror Core modules:
- Intel: "capture high-quality internal and external incident reports with voice assistance, clear documentation fields".
- Connect the Dots: "AI to responsibly surface connections between people, vehicles, or behavior across stores and over time"; person-of-interest matching with human-in-the-loop verification.
- Investigate: case management — "bring incidents, evidence, and intelligence together in one place, without manual exports or email chains".
- Insights: "surface top offenders, hotspots, and prevention outcomes".
- Audits: "replace spreadsheets and manual workflows… intuitive and comprehensive audit system" (operational gaps).

Risk Detection (add-on):
- Vehicle Recognition (LPR/ANPR): automatic detections/alerts when known vehicles of interest enter a location.
- Subject Recognition (facial recognition): alerts for known high-risk persons of interest linked to past serious behavior.

Collaboration:
- Submit police reports; evidence requests; cross-retailer collaboration; "Collaborate" feature inside Investigate packages structured intelligence for law enforcement; officers get "a dedicated inbox of triaged, evidence-rich reports"; Retail Crime Hub (with Axon) flows packaged evidence into Axon Evidence.

Integrations (per platform diagram): exception-based reporting, license plate recognition, debt recovery, self-checkout AI, VMS integrations, cart pushout detection, APIs/data lake, facial recognition; partner logos include camera/VMS vendors (Axis, Milestone, Avigilon, Verkada, Hanwha, OpenEye…) and Appriss Retail.

Privacy/security posture: privacy-by-design; role-based access; audit trails; customer-controlled data sharing ("retailers stay in full control of their data"; "Event data is controlled by the retailer that collects it, who determines what to share and when"); compliance with global privacy regulations; privacy impact assessments.

Roles: Executives, Investigators, Field Leaders, AP/LP leaders.

Explicit self-positioning vs. the Type: "Traditional loss prevention (LP) tools are built to document crime for reporting purposes only… Auror… connects every incident into a secured intelligence layer that compounds across stores, retailers, and jurisdictions." (vendor framing — useful as evidence that the category baseline is incident documentation + connection + collaboration.)

### Appriss Retail (evidence layer A, root page only — reduced strength)

Positioning: "AI for Total Retail Loss — In-Store + Online"; three products on one platform:
- Appriss Engage — Returns & Claims Management: in-store return authorization; online return & claims authorization/portals; order protection; incentive optimization; returns analytics. Decision intelligence: "Approve, warn, or decline returns in milliseconds".
- Appriss Secure — Shrink & Exception Analytics: "In-store & online exception-based reporting; Inventory exceptions; Coaching tool; Cash over/short tracking; Shrink analytics & insights"; "spotting risk before it compounds across employees, products, locations, and processes".
- Appriss Incident — Case & Audit Management: "centralizing every case type in one system — shoplifting, ORC, audits, and safety"; audit management; quick entry; case linking; civil recovery; incident analytics.
- Sidekick — AI collaborator (workflow intelligence: "Query returns, exceptions, and loss patterns in plain language").
- Cross-retailer data claims (20+ years of transaction history, share of US retail transactions) — vendor claims, not verified.

Note: Appriss explicitly frames the category as spanning loss prevention + operations + finance + CX + ecommerce ("Total loss is no longer one department").

### Solink (boundary/variant evidence, root page only)

Positioning: "Agentic Vision Intelligence for Physical Operations" — video-first platform (AI Cloud VMS, AI Agents, AI Video Alarms, AI Command Center) with LP as one use case.
- LP use case: "AI flags suspicious behavior instantly"; "Video, POS, and transaction data unified for airtight case building"; EBR listed as a use case (solutions/exception-based-reporting).
- 375+ data integrations (POS, HR, access control) giving video "business context".
- Customer quote evidence: cash voids identified via POS-video linkage; after-hours merchandise-exit detection.
- Boundary note: Solink's center of gravity is video security/VMS with LP analytics layered on; it demonstrates that video + POS correlation is a delivery philosophy inside the LP space, and marks the seam toward Video Management System as a separate Type.

---

## Cross-product Comparison

| Capability | Agilence | ThinkLP | Auror | Appriss (root) | Solink (root) | Layer |
|---|---|---|---|---|---|---|
| Loss event records (incidents/cases) | ✓ | ✓ | ✓ | ✓ | partial (case building via video+POS) | B |
| Loss-cause typing (theft/fraud/error/safety) | ✓ (incidents, accidents, fraud) | ✓ (cases, incidents, accidents, injuries) | ✓ (internal & external incidents) | ✓ (shoplifting, ORC, audits, safety) | ✓ (theft/shrink) | B |
| Location-bound events, estate-wide aggregation | ✓ | ✓ | ✓ (across stores/retailers) | ✓ (locations) | ✓ (every location) | B |
| Response workflow → resolution | ✓ (case lifecycle, close rates, time-to-close) | ✓ (intake → closure workflows, approvals) | ✓ (investigate → outcomes) | ✓ (case management) | weaker (alert response) | B |
| Exception-based reporting over POS data | ✓ (core) | ✓ | ✓ (integration) | ✓ (core) | ✓ (use case) | B |
| Alert review (legit vs false positive) | ✓ | ✓ (real-time alerts) | — (not on fetched pages) | ✓ (implied) | ✓ (validated detections) | B |
| Evidence management (video/photos/docs) | ✓ | ✓ | ✓ | ✓ (implied) | ✓ | B |
| Case linking / ORC networks | ✓ | ✓ (suspects/vehicles/boosters/fences) | ✓ (Connect the Dots) | ✓ (case linking) | — | B |
| Law-enforcement collaboration | ✓ (share case info) | ✓ (pre-formatted exports, submission) | ✓ (deep: police reports, inbox, Axon) | — (not on root) | — | B |
| Subjects / persons of interest / watch lists | ✓ (watch list) | ✓ (suspects) | ✓ (POIs, repeat offenders) | — | — | B |
| Audit / compliance management | ✓ | ✓ | ✓ | ✓ | ✓ (compliance use case) | B |
| Civil recovery / restitution | — (not on fetched pages) | ✓ | ✓ (debt recovery integration) | ✓ (civil recovery) | — | B (partial) |
| Dashboards / reports / metrics | ✓ | ✓ | ✓ (Insights) | ✓ (analytics & insights) | ✓ | B |
| Role-based access / audit trail / privacy controls | ✓ (audit trail) | ✓ (change tracking) | ✓ (explicit privacy posture) | — | ✓ (SOC 2) | B |
| Mobile field capture | ✓ | ✓ | ✓ (voice assistance) | ✓ (quick entry) | ✓ (apps) | B |
| Returns/claims fraud decisioning (real-time) | — | — | — | ✓ (Engage) | — | A, single product |
| Cross-retailer intelligence network | — | — | ✓ (core) | ✓ (data claims) | — | A, single product |
| Facial recognition / LPR detection | — | — | ✓ (Risk Detection) | — | — | A, single product |
| Video-first delivery (VMS at center) | — | — | — | — | ✓ (core) | A, single product |
| HR case management | — | ✓ | — | — | — | A, single product |
| Safety/incident (injury, OSHA, disasters) | ✓ (accidents in CM) | ✓ | ✓ (safety framing) | ✓ (safety) | ✓ (safety use case) | B |
| Inventory-loss analytics modules (RFID, expiring, DSD, physical inventory) | ✓ | ✓ (inventory analytics) | — | ✓ (inventory exceptions) | — | B |

## Canonical Model (synthesis)

### L0 — Defining Invariant (minimal)

1. **Loss event records** — discrete recorded events (field-reported incidents and/or system-generated exception alerts), each typed by loss cause (theft, fraud, error, waste, safety), bound to a location and a time.
2. **Managed response workflow** — every event moves through a review/investigation lifecycle to a recorded resolution or disposition (closed, prosecuted, recovered, coached, unfounded…).
3. **Estate-level aggregation** — events aggregate across the retailer's locations and over time to expose patterns (hotspots, repeat subjects, high-loss processes) that prioritize the response. Location is a first-class dimension of every record; the platform operates at the retailer level, not the single-store level.

Historical check: 1990s–2000s exception-based-reporting products (the XBR lineage) already had these three properties — POS-fed exception alerts typed by cause, review/resolution tracking, chain-level aggregation. Field-incident-reporting products (paper-report digitizations) had them too, minus EBR. Therefore EBR is NOT definitional; it is the dominant detection mechanism, not the invariant. Products without case management (pure report generators) fall below the "platform" bar; products without EBR (incident-reporting + investigation tools like early case managers) still fit.

### L1 — Common Mature Structure

- Exception-based reporting (EBR) over POS/transaction data: refunds, voids, discounts/overrides, no-sales, cash over/short — via rules and increasingly ML/AI models; alert queue with legit-vs-false-positive review.
- Case management depth: evidence attachment (video snippets, photos, documents), tasks/subtasks with due dates, case linking, subjects/persons of interest, watch lists, timestamps/audit trail, mobile access.
- Audit & compliance management: configurable audit forms with scoring, mobile field execution, recurring schedules, action triggers.
- Analytics & reporting: dashboards, custom reports/queries, close rate, time-to-close, recovery amounts, loss-cause breakdowns.
- Role structure: LP/AP analysts & investigators (central), field/district leaders, store managers (reporters/auditors), executives (metrics).
- Integrations: POS (essential for EBR), video/VMS (evidence + context), alarm/EAS, HR, inventory, e-commerce.
- Law-enforcement collaboration: case/evidence packages, police report submission.
- Privacy & governance: role-based access, audit trails, customer-controlled sharing (esp. with subject-recognition tech).

### L2 — Variant / Optional

- Returns & claims fraud decisioning (real-time approve/warn/decline at the return boundary — Appriss Engage; drifts toward Fraud Detection).
- Cross-retailer intelligence networks & LE-facing products (Auror Network, Retail Crime Hub/Axon).
- Recognition technology: facial recognition (subject recognition), LPR/ANPR (vehicle recognition) — privacy-regulated.
- Civil recovery & restitution program automation (notices, payment tracking).
- Safety/incident extension: injuries, OSHA filings, disaster alerts, insurance/TPA import.
- HR case management extension.
- Video-first delivery philosophy (Solink: VMS + POS correlation at the center).
- Industry tuning: grocery (perishable/expiring inventory), pharmacy (diversion, controlled substances), restaurants (waste, drive-thru), convenience (fuel), hotels.
- Inventory-loss analytics depth: RFID, physical inventory, DSD, scale production, expiring inventory.
- AI assistance: NLQ case/report building, adaptive anomaly detection, plain-language querying.

### L3 — Vendor-specific (research notes only)

- Agilence: "Analytics Plus" tier; LP Maturity Model whitepaper framing; module datasheet set (Alarm, Scales, DSD…).
- ThinkLP: Seymour AI; Think360; marketplace; OSHA module; insurance-carrier/TPA auto-import; Salesforce-based login.
- Auror: "dots" vocabulary; Retail Crime Hub with Axon Evidence; ORCAs (organized retail crime associations); network statistics (85k stores / 3.5k agencies / "3.5 hrs LE time saved per report" — vendor claims).
- Appriss: Sidekick AI collaborator; TRL (Total Retail Loss) calculator & benchmark report; cross-retailer data-scale claims (40% of US retail transactions etc.).
- Solink: VerifEye Command Center; AI Agents; remote guarding.

## Vendor-specific Findings

See L3 above. None of these entered the canonical model. Appriss's returns-decisioning and Auror's network/recognition tech are real market structures but single-product in this sample → kept as Variant/Optional with product attribution where useful.

## Boundary Findings

1. **vs Retail Shrink Management (sibling leaf)** — LP platforms consume shrink data (inventory counts, cash over/short) and include "shrink analytics" as a capability (Appriss Secure literally named "Shrink & Exception Analytics"; Agilence's stated goal is shrink reduction). The seam proposed: **shrink management = the measurement/program layer** (quantifying shrink by cause/location, inventory accuracy, reduction targets, program governance); **LP platform = the event/response layer** (detect signals, record events, investigate, resolve, recover, prevent). Overlap is real and the sibling leaf needs a joint review; if research shows shrink management is only ever a capability of LP platforms, it may be a Variant rather than an independent Type.
2. **vs Fraud Detection Platform (§15)** — fraud detection centers on payment/card/transaction fraud in real time with decisioning (approve/decline) and financial-crime typologies; LP platforms center on loss events and investigations with retail-specific exception typologies (employee-driven POS abuse, ORC, returns abuse). The seam blurs exactly at returns/claims decisioning (Appriss Engage "approve, warn, or decline returns in milliseconds") — that capability is fraud-decisioning embedded in an LP suite.
3. **vs Corporate Investigation Management (§11)** — corporate investigation management handles legal/HR/compliance investigations with legal holds, matter management; LP case management handles retail-loss investigations with ORC linking, recovery, prosecution support, LE collaboration. ThinkLP's HR module shows the seam: same case machinery, different domain vocabulary.
4. **vs Retail POS** — POS creates transactions; the LP platform consumes POS data as its primary detection input. POS exception reports (built into many POS products) are a lightweight, store-level precursor — the LP platform is the estate-level system of record for the response.
5. **vs Video Management System / physical security** — VMS manages cameras/footage; LP platforms integrate video as evidence and context (POS-video correlation). Solink demonstrates the straddle: a VMS with LP analytics layered on. If video management is the primary object, it's a VMS, not an LP platform.
6. **vs Retail Inventory Management** — inventory systems own stock records; shrink surfaces there as count variance. The LP platform investigates causes of that variance; it does not own the stock record.
7. **vs Insider Risk Management (§15)** — insider risk focuses on digital data exfiltration/employee data risk; LP covers physical/transactional loss including employee theft via POS exceptions. Different evidence domains.
8. **"去掉什么就变成另一个 Type" 判据** — remove the loss-event/case record and response workflow → you have a BI/analytics tool over POS data (or a fraud engine). Remove estate aggregation → store-level exception reporting inside POS. Remove loss-cause typing and investigation semantics → generic corporate investigation management. Remove retail domain (shrink/POS/ORC semantics) → generic case management.

## Uncertainties

- No public help-center/user-guide documentation was reachable for any sampled product; all observations are product-page level (Tier 2). Exact case-state vocabularies, permission models, and workflow defaults are therefore unverified and were not asserted.
- Appriss evidence is root-page-only (subpages 503'd); its module descriptions are accepted at face value but not corroborated in depth.
- Auror's network-scale statistics and Appriss's data-scale claims are vendor marketing numbers, not verified.
- Whether "Retail Shrink Management" can stand as an independent Type (vs. being a capability/variant of this Type) is unresolved — flagged for joint review.
- Regional/legal variation (e.g., facial-recognition legality, civil-recovery statutes by jurisdiction) was not researched in depth; recognition tech is treated as a privacy-regulated variant.
- Restaurant/grocery/pharmacy tuning was observed at page level only; depth of workflow differences per vertical is unverified.

## Final Synthesis

A Retail Loss Prevention Platform is the retailer-side operational system of record for loss events: it detects loss signals (chiefly exception-based reporting over POS/transaction data, plus field reports), records them as typed, location-bound events, moves each through a review/investigation workflow to a recorded disposition, aggregates events across the estate to expose patterns and repeat subjects, and coordinates the response — evidence assembly, audits, coaching, recovery, and law-enforcement collaboration. Its defining core is small (loss-event records + response workflow + estate-level aggregation); everything else — EBR machinery, audit management, ORC networks, recognition tech, returns decisioning, video-first delivery — is common, variant, or vendor-specific structure layered on that core.
