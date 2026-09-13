# Research Notes — SOC Platform

## Research Goal

Understand what a "SOC Platform" actually is as an Application Type: what the market sells under this label (and its synonyms — "security operations platform", "unified SecOps platform"), what objects and layers exist inside it, who uses it, how the SOC's work flows through it, and — critically — where it begins and ends relative to the already-processed §15 siblings: SIEM, SOAR, XDR, Cyber Incident Response Platform, Threat Intelligence Platform, Threat Hunting Platform, Log Management.

This pass also carries three open joint-review flags from sibling passes that explicitly awaited this leaf:
- cyber-incident-response-platform (2026-09-07): joint review with soar and soc-platform on keep-both-with-seam vs variant.
- soar (2026-09-09): "REMAINS OPEN: the third party of the CIRP flag, soc-platform."
- siem (2026-09-09) + extended-detection-response-xdr (2026-09-08): forward notes proposing that SOC Platform = "products centered on process/workforce/metrics across the SOC" — a hypothesis this pass must test against market evidence.

## Initial Boundary

Working hypothesis at start: "SOC Platform" is the umbrella/consolidation category — one product bundling the SOC's functional stack (SIEM analytics + SOAR automation + case management, commonly UEBA/TI) rather than a process/workforce/metrics tool. Nearest neighbors: SIEM (analytics layer), SOAR (automation layer), CIRP (case layer), XDR (cross-domain detection/response product), Log Management, TIP, MDR (service, not product).

## Research Questions

1. What do vendors that market a "SOC platform" / "security operations platform" actually ship? Which layers are native?
2. Is there a market segment of "SOC platform" products centered on process/workforce/metrics (the sibling passes' hypothesis), or is the label carried by converged SIEM+SOAR products?
3. What is the platform's unit of value — the layers, or the unified workflow across them?
4. Where does the platform end relative to SIEM (analytics-only), SOAR (automation-only), CIRP (case-only), XDR (detection/response product)?
5. Which capabilities are era-current (AI agents, UEBA, ATT&CK, MSSP multi-tenancy) vs definitional?
6. Historical check: does the definition over-fit the current consolidation wave?

## Representative Products

| Product | Positioning (vendor's own words) | Why sampled |
|---|---|---|
| Securonix (Unified Defense SIEM; formerly marketed as SOC Platform) | "unifies analytics, threat intelligence, investigation, and response into a single cloud-native platform" | The clearest heritage "SOC Platform" label carrier; enterprise + MSSP |
| Exabeam (New-Scale Fusion Security Operations Platform) | "combines New-Scale SIEM and New-Scale Analytics in a modular, cloud-native platform that applies AI, behavioral analytics, and automation to security operations workflows" | Markets explicitly under "Security Operations Platform"; modular packaging pole |
| Devo (Security Data Platform) | "integrated platform includes data-powered SIEM, SOAR, and UEBA… automated case management, autonomous investigations and threat hunting" | Data-plane-first philosophy; hot-storage differentiation |
| Sumo Logic (SIEM + Cloud SOAR on a shared log-analytics platform) | "unifies SIEM and Logs for Security… autonomous alert triage and guided investigation" | Shared-log-platform pole: security layers as one face of a broader observability platform |

Considered and dropped: Google Security Operations (cloud.google.com/chronicle and /security/products/security-operations both timed out twice — abandoned per the source-access rule; no product claims made from memory); Arctic Wolf (MDR service, not a platform product); Splunk/Microsoft Sentinel (already sampled as SIEM-layer evidence in the siem pass; their convergence is recorded there).

## Sources

- Securonix — root site and product pages: https://www.securonix.com/ , /products/platform-overview/ , /products/siem-solutions/ , /products/sam-the-ai-soc-analyst/ (fetched 2026-09-10)
- Exabeam — New-Scale Fusion platform page: https://www.exabeam.com/product/ , /platform/exabeam-new-scale-fusion-security-operations-platform/ (fetched 2026-09-10); docs portal listed at https://docs.exabeam.com/ (not fetched)
- Devo — root site and platform pages: https://www.devo.com/ , /platform/ (fetched 2026-09-10); docs at https://docs.devo.com (not fetched)
- Sumo Logic — security solutions page: https://www.sumologic.com/solutions/security/ (fetched 2026-09-10)
- Google Security Operations — https://cloud.google.com/security/products/security-operations and https://cloud.google.com/chronicle — both timed out (2 attempts each class); abandoned.

Evidence layers used below: **A** = directly observed on the fetched official page of a named product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison and boundary reasoning.

## Product Observations

### Securonix (Unified Defense SIEM)
- **A** — Markets a single cloud-native platform that "unifies analytics, threat intelligence, investigation, and response" (root page). Product menu: Unified Defense SIEM, UEBA, SOAR, Threat Intelligence Platform (ThreatQ), Data Pipeline Manager, Investigate, AI SOC Analyst ("Sam"), Agentic Mesh.
- **A** — The AI SOC Analyst is "embedded directly into the Unified Defense SIEM and designed to work alongside human analysts": automated alert triage and prioritization, contextual enrichment using identity/behavior/threat intelligence, investigation summaries, case preparation for escalation and response.
- **A** — Positioned for both enterprises and MSSPs ("Built for How You Operate… defending a global enterprise or scaling managed security services"); MSSP multi-tenant economics called out.
- **A** — Gartner MQ for SIEM leadership framing — the market anchors this product family in the SIEM category even when the vendor's own framing is the unified platform.

### Exabeam (New-Scale Fusion Security Operations Platform)
- **A** — "New-Scale Fusion combines New-Scale SIEM and New-Scale Analytics in a modular, cloud-native platform that applies AI, behavioral analytics, and automation to security operations workflows. Detect, investigate, and respond to threats faster."
- **A** — Named capability stack on one platform page: log management (ingest/parse/store/search, normalized via a Common Information Model, enriched at ingestion), SIEM, behavioral analytics with dynamic risk scoring for human and non-human entities, automation ("Automate and streamline TDIR… integrate with 1,000+ tools through low-code automation and standards-based APIs"), AI agents (Nova: threat scoring, investigation, analyst assistant, rule creator, search, advisor, visualization agents), Attack Surface Insights (entity profiles), Outcomes Navigator (coverage mapping to MITRE ATT&CK and OWASP Agentic Top 10).
- **A** — Modular packaging: "Use it to replace your SIEM or augment your current system with advanced analytics and automation." Augmentation path explicitly supports running alongside an existing third-party SIEM.
- **A** — FAQ: "New-Scale Fusion combines log management, SIEM, behavioral analytics, dynamic risk scoring, investigation workflows, automation, and Exabeam Nova agents."

### Devo (Security Data Platform)
- **A** — "Devo's integrated platform includes data-powered SIEM, SOAR, and UEBA. AI and intelligent automation help your SOC make the right decisions in real time."
- **A** — Company boilerplate: "a real-time security data platform that serves as the foundation of your security operations and includes data-powered threat detection, automated case management, autonomous investigations and threat hunting."
- **A** — Data-plane-first philosophy: "Ingest any data source, any format… 100% data source coverage and integrated SIEM, SOAR, and UEBA"; always-hot storage, sub-second query speed as the differentiator.
- **A** — Enterprise + MSSP segments both served (dedicated "Devo for MSSPs" solution page).

### Sumo Logic (SIEM + Cloud SOAR on a shared platform)
- **A** — Security offered as one solution family of a broader log-analytics/observability platform: "Sumo Logic unifies SIEM and Logs for Security with Dojo AI… to deliver answers your team can act on fast."
- **A** — Named security components on the shared data plane: SIEM, Logs for Security, Automation (Cloud SOAR — separate solution page listed), UEBA behavioral baselines, automated investigations, compliance use cases.
- **A** — AI framing: "autonomous alert triage and guided investigation"; natural-language investigation and playbook building.
- **A** — The security operations stack rides a platform that also serves IT observability — the platform-first pole of the sample.

## Cross-product Comparison

| Structure | Securonix | Exabeam | Devo | Sumo Logic | Layer |
|---|---|---|---|---|---|
| Org-wide security event data plane (ingest/normalize/store/search) | A | A | A | A | native in all 4 |
| Continuous security detection over that data (rules/analytics/behavioral) | A | A | A | A | native in all 4 |
| Case / incident management as a first-class layer | A (case preparation; Investigate) | A ("investigation workflows") | A ("automated case management") | A (Cloud SOAR case layer) | native in all 4 |
| Response automation / orchestration (playbooks, integrations) | A (SOAR product line) | A (low-code automation, 1,000+ tools) | A (SOAR included) | A (Cloud SOAR) | native in all 4 |
| UEBA / behavioral analytics | A | A | A | A | common (all 4, but not definitional) |
| Threat intelligence management | A (ThreatQ) | partial (enrichment; Advisor) | B (community TI mentioned) | B | optional |
| Threat hunting | A (ThreatWatch/ATS) | B | A | A | optional/standard |
| AI analyst agents | A (Sam) | A (Nova) | B | A (Dojo) | era-current common, NOT definitional |
| MSSP multi-tenancy | A | B | A | A (SRG case) | variant |
| Cloud-native SaaS | A | A | A | A | dominant form, not definitional |
| Modular augment-or-replace packaging | B | A | B | B (augments existing stacks) | variant |
| Shared platform with IT observability | — | — | — | A | variant (platform-first pole) |

**B — the decisive cross-product finding:** every product marketed under the "SOC platform" / "security operations platform" / unified-defense label natively holds the SAME three machinery layers in ONE product: (1) the org-wide security event data plane with continuous detection, (2) case/incident management, (3) response automation/orchestration. UEBA, TI, hunting, and AI agents are near-universal add-ons; none is the identity.

**Answer to RQ2 (the sibling passes' hypothesis):** No product in the sample (and none surfaced in navigation) is a "SOC platform" centered on process/workforce/metrics. The market label is carried by converged SIEM+SOAR+case products. The siem/xdr passes' "process/workforce/metrics" framing is corrected by this evidence: the whole-operations layer IS the converged platform, and its "whole-operations" character lies in natively holding all layers of the TDIR workflow, not in workforce management.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

The SOC Platform is the **single product that natively unifies the SOC's operational machinery layers** so that the organization's threat detection–investigation–response workflow runs end-to-end in one system:

1. **The security-operations data and detection layer, native** — the platform itself collects the org's security-relevant events and runs continuous detection over them (the SIEM's defining core, held natively, not integrated from a third party). Remove → the product is a SOAR/CIRP combination sitting on someone else's SIEM.
2. **The case/incident management layer, native** — alerts and investigations are worked as managed cases/incidents inside the platform (the CIRP's defining core, held natively). Remove → the product is a SIEM with an alert queue.
3. **The response automation/orchestration layer, native** — playbooks/automation execute response actions across the environment and connected tools from within the platform (the SOAR's defining core, held natively). Remove → the product is a SIEM with a case tool.
4. **The unified workflow as the unit of value** — one product carries the signal from ingestion through detection, triage, investigation, response, and closure/measurement; the layers are designed as one system (shared data, shared entities, shared console), not a bundle of separately-purchased products. Remove the unification → the pre-consolidation SOC toolchain (separate SIEM + SOAR + case tool), which is precisely the sibling Types, not this one.

Jointly-held load-bearing: 1 alone = SIEM; 2 alone = CIRP; 3 alone = SOAR; 1+2 without 3 = SIEM with case management (the SIEM-embedded pole); 1+3 without 2 = automation engine on a data plane without a case layer; 2+3 without 1 = SOAR+CIRP over an external SIEM (the classic pre-convergence stack); all four = the Type.

### L1 — Common Mature Structure
- UEBA / behavioral analytics with risk scoring over entities (all 4 sampled)
- Threat intelligence ingestion and enrichment (native TIP in one; enrichment-level in others)
- Threat hunting over the platform's data
- MITRE ATT&CK mapping of detections/coverage
- Compliance/reporting output from the same data
- Entity/asset context (asset inventories, entity profiles, attack-surface aggregation)

### L2 — Variant / Optional Structure
- AI analyst agents / agentic AI (era-current, near-universal in 2026 marketing, absent from the defining core)
- MSSP multi-tenant operation vs single-org enterprise
- Modular augment-or-replace packaging (run analytics/automation beside an existing third-party SIEM vs full replacement)
- Platform-first pole: security as one face of a broader log-analytics/observability platform
- Deployment economics: hot vs tiered storage, data-pipeline add-ons, third-party storage routing
- Self-hosted vs cloud-native SaaS

### L3 — Vendor-specific
- Securonix "Sam" AI SOC Analyst, Agentic Mesh, ThreatQ acquisition, Snowflake/AWS data-plane options
- Exabeam Nova agent family, Outcomes Navigator, Agent Behavior Analytics for AI agents, LogRhythm self-hosted line
- Devo always-hot storage architecture, "Security Data Platform" naming, Devo+Sentinel augmentation play
- Sumo Logic Dojo AI, shared observability/security data plane, FedRAMP posture

## Vendor-specific Findings
(see L3; none promoted to the canonical core)

## Boundary Findings

1. **vs SIEM (§15, processed)** — The SIEM's three-leg core (data plane + detection + investigation loop) is fully contained in the SOC platform as its native substrate. The seam is the breadth of natively-held layers: a SIEM stands on analytics-over-own-data with the investigation loop; the SOC platform additionally holds case management and response automation as first-class native layers. Bundling, treated as "packaging, not identity" in the SIEM and SOAR passes for SIEM-embedded automation, becomes identity-bearing here only in the specific form of native unification of ALL layers — the platform's unit of value is the whole workflow in one system. Removal test both ways: strip automation+case from the platform → a SIEM; a SIEM cannot become the platform by adding an alert queue alone. **Keep-both RATIFIED; discharges the siem pass's forward note (2).**
2. **vs SOAR (§15, processed)** — The SOAR's center of gravity is orchestration across EXTERNAL tools; it does not own the org's data plane or detection. The SOC platform owns the data plane and detection natively and runs automation as one layer of its own system. The SOAR's tool-connection layer persists inside the platform (Exabeam's "1,000+ tools" integrations) as the automation layer's reach, not as the platform's substrate. **Keep-both RATIFIED; discharges the soar pass's open flag (third party of the CIRP joint review).**
3. **vs Cyber Incident Response Platform (§15, processed)** — The case layer inside the platform is the CIRP core realized natively as one layer among several. CIRP remains the standalone case-management Type (realizable without automation, per its pass). The platform's case layer inherits the same case semantics; embedded realization is packaging at the platform level. **Keep-both RATIFIED; discharges the CIRP pass's joint-review flag from this side.**
4. **vs XDR (§15, processed)** — Confirmed from this side: XDR is the cross-domain detection/response product (vendor-curated telemetry, unified cross-domain incident, actuated response) that FEEDS the operations layer; the SOC platform is the whole-operations system whose substrate is the org's own event plane. Convergence pressure exists (platform vendors sell both), but the cores are distinct. **Keep-both RATIFIED; discharges the xdr pass's SECONDARY forward note.**
5. **vs Threat Intelligence Platform / Threat Hunting Platform** — TI and hunting appear as native layers or integrated modules inside the platform (Securonix ThreatQ; hunting in 3/4 sampled). Consistent with the TIP pass's packaging-drift note and the hunting pass's capability-type note: the platform consumes/integrates these functions; the standalone Types remain distinct.
6. **vs MDR / managed services** — Several sampled vendors sell managed detection/response services ON their platforms (Securonix MDR partner stories; Sumo Logic MSSP cases). The service is a delivery model over the platform, not this Type.
7. **Correction to sibling-pass framing** — the "process/workforce/metrics across the SOC" hypothesis (siem, xdr, CIRP passes) is NOT supported by market evidence: no such product category surfaced. The whole-operations layer is the converged platform. Recorded in STATUS Boundary Issues as a correction.
8. **Alias-risk disclosure** — because the Type's identity rests on consolidation breadth, a skeptic can describe it as "SIEM with bundled SOAR and case management." This pass keeps it as a distinct Type because (a) the market carries a distinct category label ("security operations platform") with products positioned primarily under it, (b) the unit of value is the unified workflow, and (c) the sibling layer-Types remain realizable standalone. If the directory later consolidates, this leaf is the natural umbrella for the converged product family. Recorded in STATUS Boundary Issues.

## Historical / Market-Sample Check (§24)

The Type is consolidation-era by construction: its defining property (native unification of the operational layers) did not exist before the SIEM+SOAR+case convergence wave; the pre-consolidation SOC ran the sibling Types as separate products, which is exactly why those Types exist as separate leaves. The check that matters here is therefore not "would an older product fit" (it would not, and should not — it would be a SIEM or SOAR) but "does the core depend on era-current implementation specifics": it does not — the L0 layers (data plane + detection, case layer, automation layer, unified operation) are all realizable without cloud-native architecture, AI agents, UEBA, or ATT&CK mapping. A hypothetical on-premises converged suite holding all four layers would satisfy the core. Check passed on that basis; the Type's short history is a property of the category, not an over-fit.

## Uncertainties

- Google Security Operations could not be fetched (timeouts ×2 per URL class); its inclusion in the category is asserted only from the Sumo Logic comparison-page reference and general market structure, with no product-behavior claims made from memory.
- Deep documentation portals (docs.exabeam.com, docs.devo.com) were not fetched this pass; observations are Tier-1/Tier-2 official product-page level. Precise operational details (connector counts beyond Exabeam's own "1,000+" claim, retention defaults, pricing models) are deliberately not asserted.
- Whether any standalone "SOC process/workforce management" product exists under a different name was not exhaustively searched; the finding recorded is that nothing under the SOC-platform label centers on workforce/metrics.

## Final Synthesis

The market's "SOC Platform" (security operations platform) is the consolidation-era whole-operations product: one system that natively holds the SOC's three machinery layers — org-wide security event data plane with continuous detection, case/incident management, and response automation/orchestration — so the full detect→triage→investigate→respond→close workflow runs in a single product with shared data, entities, and console. The layer Types (SIEM, SOAR, CIRP) remain realizable standalone and are exactly what the platform unifies. Era-current capabilities (AI agents, UEBA, TI, hunting, ATT&CK, MSSP tenancy, cloud-native form) are standard or variant, not definitional.
