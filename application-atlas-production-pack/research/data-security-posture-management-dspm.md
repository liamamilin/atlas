# Research Notes — Data Security Posture Management / DSPM

Research date: **2026-09-07**
Methodology: WORKFLOW_v1.1 (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

---

## Research Goal

Understand what a Data Security Posture Management (DSPM) application actually is as a Type: its defining structure, its canonical workflow, who operates it, and how it is distinguished from the crowded neighborhood of posture/discovery/governance Types (CSPM, SSPM, CNAPP, DLP, Data Access Governance, Data Catalog, Data Observability, Data Governance Platform).

## Initial Boundary

Initial hypothesis before research:

- DSPM is a **security-team management plane over the organization's data estate**: it discovers where data lives (primarily cloud stores, extending to SaaS/warehouses/on-prem), classifies what data is sensitive, evaluates the security state of that data (exposure, access, protection), and turns the combination into prioritized findings the security team works.
- Nearest neighbors and suspected seams:
  - **CSPM** — same loop (connect → inventory → evaluate → findings), but the assessed object is infrastructure *configuration*, not data content/sensitivity. Already processed; its doc records "DSPM = object-domain sibling; DSPM's assessed object is data stores and data sensitivity; often shipped as a module inside CSPM products."
  - **SSPM** — SaaS tenant *configuration* posture (not data content). Not yet processed; noted as unprocessed sibling.
  - **DLP** — enforces policy on data *movement/use*; DSPM discovers/grades data *at rest*. Already processed; its doc records this seam.
  - **Data Access Governance** — operates the access-decision loop on the permission layer; DSPM assesses posture. Already processed; its doc records the seam ("discovers and classifies data and flags configuration weaknesses… DAG operates the access-decision loop").
  - **Data Catalog / Data Observability / Data Quality** — non-security lenses over the same external data estate; must be separated from the security lens.
  - **CNAPP** — umbrella platform whose pillars include DSPM; already processed with a platform-composition flag.
- Unknown points going in: risk-taxonomy depth, remediation depth, whether activity monitoring (DDR) is inside or outside the Type, hyperscaler realizations, deployment topology (SaaS vs in-environment scanning).

## Research Questions

1. What does a DSPM connect to, and how (agentless/read-only vs agents vs in-environment scanners)? Where does the data of record live?
2. What is the central object model — data stores? data objects? findings? classifications?
3. What exactly does "posture" evaluation mean for data: which risk families appear across products?
4. How is risk prioritized (sensitivity × exposure × access)? Is there a posture score?
5. What happens after a finding: alerting, tickets, remediation guidance, native actions, owner routing?
6. How does classification work (patterns vs ML/LLM; structured vs unstructured)?
7. Where does DSPM end and Data Detection & Response (DDR) begin?
8. Which estate scope is definitional (cloud-only? SaaS? warehouses? on-prem)?
9. Packaging: standalone Type or module of CNAPP / data-security platforms?
10. Historical check: would pre-DSPM-era data discovery/classification tools (DLP-at-rest discovery, enterprise data classification scanners) fit the definition?

## Representative Products

Selection principles: market representation (category leaders across analyst-recognized DSPM names), documentation completeness, different product philosophies, different packaging tiers.

| Product | Pole | Evidence tier reached |
|---|---|---|
| Prisma Cloud DSPM (Palo Alto Networks) | CNAPP-embedded DSPM module (Dig Security acquisition) | **Tier 1** — full operational docs (GitBook markdown, fetched directly) |
| Sentra | DSPM pure-play, cloud-data-estate focus | Tier 2 — official product pages + official category guide |
| BigID | Data discovery/classification platform heritage, DSPM as one use case | Tier 2 — official DSPM product page + official FAQ |
| Cyera | AI-era data security platform with DSPM as core product | Tier 2 — official product/platform pages |
| IBM (Guardium Data Security Center) | Enterprise data-security suite heritage | Tier 2 (suite-level page only) — market context, no DSPM-specific operational claims |

Rejected/abandoned samples: Wiz (docs auth-gated in the prior CSPM pass; not retried), Varonis/Securiti/Orca/Microsoft Purview DSPM-for-AI (not fetched — budget; recorded as unverified realizations), IBM DSPM-specific docs (403).

## Sources

Fetched 2026-09-07:

- Prisma Cloud DSPM docs (GitBook, `.md` versions):
  - https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome.md
  - .../welcome/system-components.md
  - .../welcome/platform-overview/overview.md
  - .../welcome/platform-overview/risks.md
  - .../welcome/platform-overview/ddr-policies.md
  - sitemap.md (DSPM section: deployment per cloud, how-to articles, integrations, API, troubleshooting)
- Sentra:
  - https://www.sentra.io/ (product positioning)
  - https://www.sentra.io/resources/guides/data-security-posture-management-dspm-a-complete-guide (official category guide, by Sentra CTO)
- BigID:
  - https://bigid.com/ (platform positioning)
  - https://bigid.com/data-security-posture-management/ (DSPM product page + official FAQ)
- Cyera:
  - https://www.cyera.io/ (platform + product navigation, capabilities, remediation/stewardship claims)
- IBM:
  - https://www.ibm.com/products/guardium-data-security-center (suite-level)

Source-access limitations (recorded per rules):

- `docs.prismacloud.io` GitBook `ask`-query interface timed out twice → abandoned that interface; direct page fetches used instead (successful).
- `ibm.com/docs/en/dspm` returned 403 → IBM restricted to suite-level marketing page; **no DSPM-specific operational claims drawn from IBM**.
- Microsoft Purview "DSPM for AI", Varonis, Securiti, Orca not fetched — hyperscaler and additional poles unverified this pass; not used for any claim.
- Vendor precision numbers (PB-scanned benchmarks, classifier counts, precision %, staleness-day thresholds) are marketing claims on official pages; kept in Research Notes only, none promoted to the final document.

---

## Product Observations

### Prisma Cloud DSPM (Palo Alto Networks) — Evidence Layer A

From official operational documentation (the strongest source in this pass):

- Self-positioning: "agentless, multi-cloud, data security platform that **discovers, classifies, protects, and governs sensitive data**… complete visibility and real-time control over potential security risks to their data."
- **Deployment architecture** (System Components page): native/built-in per-cloud deployment; three components:
  - *Orchestrator* — runs the compute (e.g., EC2/VM) that scans and analyzes customer accounts; installable in a dedicated security-tooling account or per-account (configurable).
  - *Read-only permissions* — read-only access for asset **metadata** (size, name, region) and log collection for DDR.
  - *Scanner permissions* — enable discovery/scan for analysis and classification; "cannot be used outside the client's environment. This ensures that all sensitive data discovered, scanned, and classified… **never leaves the client's environment**."
  - Positioning: "real-time monitoring… without affecting the monitored environment's performance, making it a completely **out-of-band** solution."
- **Deployment scope** (sitemap): onboarding per AWS / Azure / GCP / OCI / Alibaba; **Snowflake**; **Microsoft 365**; **on-premise file shares**. Offboarding per cloud is documented.
- **Platform surfaces** (Platform Overview page):
  1. assets automatically discovered, breakdown per platform;
  2. **data security posture score** + top risks;
  3. **exposed issues** count + description of exposed sensitive records;
  4. assets with **data footprint issues**;
  5. sensitive records with **DDR protection**;
  6. **open alerts** + alert history;
  7. top assets most at risk;
  8. activity log.
- **Risks page**: risks sorted by **risk type, category and severity**; per-risk **Findings** (assets detected in, labels); full risk info includes **which compliance regulations it violates**; clicking an asset → **Asset Page**; filtering + saved Views.
- **DDR Policies page**: out-of-the-box DDR policy set maintained by vendor's data researchers; policy categories: **First Move / Attack / Compliance**; per-policy open-alert counts; enable/disable per policy.
- **How-to articles** (from sitemap — titles are direct evidence of supported operations):
  - custom **risk rules** ("Create and edit custom risk rules");
  - **labels** to files; **key:value tagging** of assets;
  - **exclude projects** from alerts and risks (scoping);
  - **scanning settings per supported service**;
  - **data-asset access information** exploration;
  - **monitor AWS activities**;
  - assets **not accessed or modified for 90 days** (staleness monitoring — the number is a product default, kept here);
  - **custom data types** creation (incl. from email examples);
  - asset/file-level filters; findings-by-file views; ignoring non-sensitive-asset findings;
  - email notifications; amount-of-assets calculation.
- **Integrations** (from sitemap): Amazon SNS, Torq, PagerDuty, Jira, Slack, webhooks, XSOAR (remediation), WildFire.
- **API documentation**: API keys, first API call — programmatic access is a documented surface.
- Notable: data-sensitivity context also feeds the CNAPP's broader inventory (Data Inventory page exists in the Prisma Cloud docs corpus).

### Sentra — Evidence Layer A (self-description) / B (category claims)

From official site and official category guide (authored by co-founder/CTO):

- Positioning: data security that "lives in your environment — not ours"; classification signals flow into existing Agentic AI, DLP, IAM, ITSM, SIEM, SOAR, and cloud platforms ("no parallel stack required").
- Official definition of DSPM (guide): "securing cloud data by ensuring that data assets always have the correct security posture, regardless of where it's been duplicated or moved to"; does this by: (1) discovering all data in the public cloud including **shadow data** ("created but isn't used or monitored"); (2) "understanding the right security measures needed for different types of data"; (3) "prioritizing alerts by how sensitive the data is and providing practical solutions."
- Key example (guide, product-agnostic framing): a discovery tool finding PII with proper posture should **not** alert — sensitivity alone isn't risk; posture context decides.
- Key features (guide): data discovery & classification (structured + unstructured; ML for IP-like types; data-catalog integration for ownership); **exposure & risk assessment** ("data that moves can lose the protections it once had"); **access governance** (authorization gap, least privilege); incident response & remediation (SIEM integration, NIST SP 800-61 framing); compliance & audit management (automated checks, reports, audit logs); continuous monitoring.
- Classification method (guide): **statistical analysis at column level for structured data; LLMs and ML for unstructured**; rationale: resource consumption + accuracy/false-positive reduction.
- Data movement detection listed as a selection criterion ("tracks data movements and changes").
- CSPM-vs-DSPM table (guide): CSPM = infrastructure vulnerabilities (VMs/VPC networks), "lacks data sensitivity prioritization"; DSPM = "overexposure, access controls, and anomalies, bridging data with infrastructure security"; DSPM coverage "beyond IaaS to cover data security in PaaS and SaaS".
- Implementation steps (guide): **Discovery → Assessment → Remediation** (encryption, access-control refinement, etc.).
- When to adopt (guide): multi-cloud with varying security; frequent replication/movement (test, backup, DR); large user base/complex access; strict regulation.
- AI-era additions (site): Copilot/Bedrock data governance, shadow-AI protection, agent access — the current flagship pitch.

### BigID — Evidence Layer A (self-description) / B (FAQ risk list)

From official DSPM product page and platform page:

- Positioning: "DSPM that goes beyond visibility" — discover → prioritize → remediate; "most DSPM tools stop at mapping your cloud data" (explicit category framing).
- Discover/Understand/Prioritize/Remediate model: identify sensitive/regulated/high-value data across **structured, unstructured, semi-structured** sources; connect data to **exposure, access, ownership, and business context**; prioritize by sensitivity/exposure/access/impact; remediate via "automated workflows, access controls, retention enforcement, and policy-driven actions".
- Coverage claims: cloud, SaaS, IaaS, PaaS, hybrid, **on-prem**, dev environments, AI systems; "agentless & cloud native… run locally when needed — no backhaul or cloud copying".
- **Official FAQ — what risks DSPM identifies**: "**overexposed data, excessive permissions, stale data, duplicated data, and policy violations**" (direct product-anchored risk list).
- FAQ — DSPM vs CSPM: "CSPM focuses on securing cloud infrastructure and configurations, while DSPM focuses on securing the data itself… visibility into sensitive data, access permissions, data exposure, and data risk regardless of where the data resides."
- Remediation claims (native actions): "revoke access, delete toxic data, redact secrets, enforce retention, or delegate tasks to owners — natively from BigID".
- Heritage: data discovery & classification platform first (DSPM one of several marketed use cases alongside DAG, DLP, insider risk, privacy); identity-aware discovery ("links data risk to real identities — not just buckets and blobs").
- AI-era additions: AI training-data governance, shadow AI detection, vector-database scanning, AISPM.

### Cyera — Evidence Layer A (self-description)

From official site/platform pages:

- Positioning: DSPM as "the most intelligent **data security control plane**" inside a broader AI-security platform (DSPM, DLP, Agent Guardian, Privacy products).
- Capability set: **enriched classification** (AI-native, "learns your business", combines "classification, context, identities, usage & movement into actionable intelligence"); **remediation** ("predefined rules that trigger native actions or automation workflows teams already rely on in platforms such as Tines and Torq"; "built-in guardrails such as **previews, blast-radius insights, and audit trails**"); **Access Trail** (data-access detective for humans and AI — activity dimension); **Identities** (identity enrichment); **Data Subject Request** (privacy seam).
- Stewardship: "routing high-risk data exposures to **data owners** via custom notifications and a **dedicated portal**"; "turn business users into data security stewards".
- Compliance: "instantly generate **auditor-ready evidence** from continuously classified data and access trails, mapped to regulatory controls across cloud, SaaS, and on-prem data stores."
- Solution framings: public exposure, data minimization, compliance readiness, insider threat, secure M365.
- Marketing numbers (kept here only): 74 PB in 7 days, 95%+ precision, "80% less risk in 3 months", "<1 day to value" — deployment-speed claims, not structure.

### IBM (Guardium Data Security Center) — Evidence Layer A (suite-level only), used as market context

- Suite spans data activity monitoring (Guardium Data Protection), vulnerability assessment of data stores, DDR, cryptography management — an enterprise **data-security suite** heritage into which data-security posture use cases fold.
- DSPM-specific operational documentation not publicly reachable this pass (403). **No DSPM-specific structural claims drawn from IBM.** Used only to confirm the "enterprise data-security suite" packaging pole exists.

---

## Cross-product Comparison

| Dimension | Prisma Cloud DSPM | Sentra | BigID | Cyera | IBM (context) |
|---|---|---|---|---|---|
| Connection posture | native per-cloud; read-only + scanner permissions; scanning compute runs **in customer environment**; "out-of-band" | "lives in your environment — not ours" | agentless; "run locally… no backhaul or cloud copying" | in-environment scanning claims (speed/scale marketing) | (unverified) |
| Data of record | stays in customer stores; sensitive content never leaves client environment | stays in place | stays in place | stays in place | — |
| Estate scope | AWS/Azure/GCP/OCI/Alibaba + Snowflake + M365 + on-prem file shares | cloud + data warehouses + M365/Slack/AI surfaces | cloud, SaaS, IaaS/PaaS, hybrid, on-prem, dev, AI | cloud, SaaS, on-prem, AI surfaces | hybrid, on-prem + cloud |
| Discovery incl. unknown data | auto-discovery of assets per platform | shadow data (named concept) | sprawl / "see what others miss" | "secure the unknown" framing | — |
| Classification | documented capability; custom data types; data-type taxonomy | statistical (structured) + ML/LLM (unstructured) | classifier-led heritage; identity-aware | AI-native "enriched" classification | — |
| Posture evaluation | posture score; exposed issues; data-footprint issues; custom risk rules; risk type/category/severity | exposure & risk assessment; movement detection | overexposure, excessive permissions, stale, duplicated, policy violations | public-exposure solution framing; risk reduction | — |
| Access/identity dimension | data-asset access information; AWS activity monitoring | access governance section | identity-aware discovery; DAG companion | Identities + Access Trail | — |
| Prioritization | top risks; severity; top assets at risk | "prioritizing alerts by how sensitive the data is" | prioritize by sensitivity × exposure × access × impact | actionable intelligence; guardrailed one-click actions | — |
| Remediation | integrations (XSOAR remediation, SNS, PagerDuty, Jira, Slack, webhooks); custom risk rules | "practical solutions"; remediation step | native actions (revoke/delete/redact/retain/delegate) | native actions + automation + guardrails; owner portal | — |
| Activity/DDR | DDR policies inside the product (First Move/Attack/Compliance); monitor activities | DDR as separate marketed guide | DDR as separate use-case/product line | Access Trail as platform capability | Guardium DDR suite member |
| Compliance | regulations violated per risk; compliance overview page | compliance & audit management | GDPR/CPRA/HIPAA/AI-Act alignment claims | auditor-ready evidence mapping | suite-level compliance heritage |
| Stewardship/owners | labels/tagging; project exclusion | data-catalog integration for ownership | delegate tasks to owners | data-owner routing + dedicated portal | — |
| Packaging pole | CNAPP module | standalone pure-play | data-security platform use case | AI-security platform core | data-security suite |

### Stable commonalities (Layer B)

Across the researched sample, every product:

1. connects to the customer's data stores via **read-authorized, non-inline** mechanisms (agentless/native roles or in-environment scanners); none replaces the store's own security model; the data of record stays in place.
2. **discovers** data stores/objects including previously unknown ones, maintaining a continuously refreshed **data inventory**.
3. **classifies data content** for sensitivity (patterns and/or ML/LLM; structured and unstructured) — the inventory is a *sensitivity-bearing* inventory.
4. evaluates the **security state of each data asset** — exposure (public/internet), access (over-permission, identity context), protection (encryption/protection controls), hygiene (staleness, duplication, footprint) — and produces **risk findings**.
5. **prioritizes findings by combining sensitivity with exposure/access context** — sensitivity alone is explicitly not the alerting criterion (Sentra's own example; Prisma's posture-score design; BigID's "prioritize" leg).
6. **routes findings to security operations**: alert surfaces, ticketing/ITSM, chat, SOAR, SIEM, APIs.
7. supports **compliance mapping** of findings to regulations/standards.
8. offers **remediation** on a spectrum: guidance → one-click/native actions → automated rules → owner-delegated tasks.
9. labels/tagging, scoping/exclusion, custom risk rules and custom data types appear repeatedly as *operator configuration* surfaces.
10. AI-era extensions (copilot/agent/LLM data surfaces) are now standard marketing territory in all four DSPM-specific samples.

### Variances (Layer B/C)

- **Remediation depth** varies most: Prisma documents remediation via integrations/SOAR and custom rules; BigID/Cyera document native in-product actions; Sentra's public material emphasizes signal feeding into existing stacks.
- **DDR (activity/behavioral detection on data)**: inside the product (Prisma), separate product line (BigID), platform capability (Cyera Access Trail), suite member (IBM Guardium DDR). Not uniform → treat as variant/adjacent capability.
- **Estate scope**: cloud-first everywhere; SaaS (M365), warehouses (Snowflake), and on-prem file shares are extensions present in the strongest-documented product and claimed by others — breadth is a variant axis, not the definition.
- **Classification philosophy**: statistical column-level + LLM for unstructured (Sentra), classifier-library heritage (BigID), AI-native adaptive (Cyera) — method varies, the *classified inventory* is constant.
- **Deployment topology**: SaaS metadata plane vs in-environment scanning compute vs hybrid — varies; "agentless" is a marketing posture, not an invariant (Prisma explicitly deploys in-environment scanner compute while calling the platform agentless).

---

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant (deliberately small)

The DSPM Type is recognizable only with all three of:

```text
Connected external data estate          (read-authorized connections into data stores
                                          the platform does NOT own; the platform is a lens,
                                          data of record stays in place)
└── Sensitive-data inventory            (discovered stores/objects + what data they hold,
                                          classified by sensitivity — a data map)
    └── Data-exposure findings loop     (the security state of each data asset — exposure,
                                          access, protection — evaluated against risk,
                                          producing prioritized findings that security
                                          operators work: alert → triage → remediate/close)
```

Removal tests:

- Remove the connection/lens posture → an offline advisory service or a scanner over exported copies — not DSPM.
- Remove sensitivity classification of data content → infrastructure posture management (CSPM) or a bare asset inventory — the "Data" in DSPM is gone.
- Remove the exposure-evaluation → pure discovery/classification — i.e., a data catalog / classification engine, not posture management.
- Remove the findings/management loop → a one-shot scan report — not a management system.

### L1 — Common Mature Structure

- agentless/read-only connector posture; in-environment scanning so content stays in the customer's environment (both documented as the common deployment shape)
- shadow/unknown-data discovery; continuous refresh of the inventory
- ML/LLM + pattern classification spanning structured and unstructured data; custom data types
- data security posture score / top-risk dashboards; asset detail pages with risk roll-ups
- access analysis: effective access/identities on data assets; activity monitoring hooks
- movement/replication awareness (data that moved/copied loses protections); cross-region awareness
- staleness/duplication/data-footprint findings
- custom risk rules; labels/tagging; scoping/exclusions
- compliance mapping (findings ↔ regulations/standards); auditor evidence
- alert routing: SIEM, SOAR, ticketing/ITSM, chat, webhooks; reports; APIs/CLI
- owner routing / stewardship surfaces
- remediation: guidance → native one-click actions → automated workflows

### L2 — Variant / Optional Structure

- packaging pole: standalone pure-play vs CNAPP module vs data-security platform use case vs suite member (main market-structure axis; structure of the core loop identical across poles)
- estate scope: cloud-only vs +SaaS vs +warehouses vs +on-prem file shares
- DDR / data detection & response (behavioral detection on data access/use): inside the product, separate line, or absent
- remediation enforcement depth (observe/advise vs native enforce vs automated with guardrails)
- identity enrichment depth; privacy machinery (DSR, consent) overlap
- AI-era extensions: AI readiness, shadow AI, copilot/agent data governance, vector-store scanning
- deployment: SaaS-hosted metadata plane vs in-environment deployment vs hybrid

### L3 — Vendor-specific (research notes only)

- Prisma: Orchestrator/Read-Only/Scanner component names; "First Move / Attack / Compliance" DDR policy categories; posture-score composition; 90-day staleness article default; WildFire/XSOAR integration specifics.
- Sentra: benchmark claims (9 PB scanned <72 h, >98% accuracy, ROI tables); statistical-column-level + LLM split rationale.
- BigID: classifier-count claims (1,000s/1,500+); "only platform" framing; free assessment funnel.
- Cyera: 74 PB/7 days, 95%+ precision, "<1 day to value", "80% less risk in 3 months"; Oasis acquisition/Agent Guardian positioning.
- IBM: Guardium suite component names; KuppingerCole/IDC quotes.

### Anti-overfitting check (per abstraction rules)

- "Agentless" is **not** definitional: the best-documented product deploys in-environment scanner compute while marketing itself as agentless. Canonical form: *non-inline, read-authorized access; data of record stays in place*.
- "Cloud-only" is **not** definitional: on-prem file shares / hybrid are documented (Prisma) and claimed (BigID/Cyera). Canonical form: *the organization's data estate, cloud-first*.
- ML/LLM classification is **not** definitional: pattern/classifier approaches exist. Canonical form: *classified sensitivity inventory*.
- Sensitivity-only alerting is explicitly rejected by a vendor's own explanation — the sensitivity × exposure *combination* is the invariant.

---

## Boundary Findings

| Neighboring Type | Seam | "Remove what → becomes the other" test |
|---|---|---|
| **CSPM** | assessed object: data content/sensitivity + data-store exposure vs infrastructure configuration state | Remove the data-sensitivity inventory (keep config evaluation) → CSPM. Remove config-evaluation breadth (keep data content) → DSPM. Products literally ship DSPM as a CSPM-platform module — sibling Types, same loop, different object. |
| **SSPM** (unprocessed sibling) | SaaS tenant *application settings* posture vs *data* posture inside SaaS | Assessed object test: tenant configuration of a SaaS app vs the data it holds. Recorded for the future SSPM pass. |
| **DLP** | at-rest discovery/grading + remediation vs enforcement on movement/use | Remove enforcement-on-movement → DLP becomes discovery (DSPM-adjacent). Add movement enforcement to DSPM → you have built DLP. DLP doc records: "DSPM discovers/grades data at rest in cloud stores; DLP enforces on movement/use." |
| **Data Access Governance** | posture assessment + risk findings vs the access-decision loop (reviews/approvals/revocations as recurring governance) | Remove the risk-findings lens → permission reports. Add certify/approve/request loops → DAG. DAG doc records the same seam from its side. |
| **Data Catalog** | security risk lens (findings, exposure, remediation) vs descriptive lens (understand/evaluate/trust for use) | Both harvest metadata and classify. Remove risk findings & remediation → catalog. Add glossary/trust/consumption surfaces → catalog. Data-catalog pass's core ("describes data, never holds it") overlaps the connector posture but not the findings loop. |
| **Data Observability / Data Quality** | security posture vs operational health/fitness | Object of evaluation differs: exposure/risk vs freshness/volume/quality rules. Same "lens over external estate" architecture — different question asked. |
| **CNAPP** | umbrella platform composed of CSPM/CWPP/CIEM/DSPM pillars | Remove platform unification → the pillar Types stand alone. DSPM often appears as a pillar; the pillar's own core loop is what this document defines. (CNAPP pass already recorded the platform-composition flag.) |
| **DDR / Data Detection & Response** | posture (standing state) vs behavioral detection/response (events) | DDR appears inside DSPM products (Prisma), as separate lines (BigID), as platform capability (Cyera). Not uniform → treat as variant/adjacent capability, not a defining element. |
| **Data Governance Platform** | security-risk framing vs normative rules/accountability/governed processes | Governance pass recorded catalog-vs-governance seam; DSPM sits even further from governance: findings/remediation vs policy/accountability. |

Drift markers (what would make a DSPM stop being DSPM): if the product's primary object becomes infrastructure configuration (→ CSPM), a SaaS tenant's app settings (→ SSPM), movement/use enforcement (→ DLP), the access-decision loop (→ DAG), or descriptive understanding for consumers (→ Data Catalog).

## Historical / Market-Sample Check (§24 discipline)

The DSPM category is young (market-coined early 2020s), so the "older product" test must use ancestors:

- **Pre-cloud enterprise data discovery/classification scanners** (on-prem DLP-at-rest discovery modules, data classification appliances): they connect to stores and classify content — they satisfy L0's first two structures but **lack the exposure-evaluation findings loop** (they report where data is, not the security state of it). They are ancestors, not members; the exposure-evaluation leg is what the market added when data moved to elastic cloud stores. This supports keeping the findings loop inside the invariant rather than treating classification as sufficient.
- **Cloud-native ancestors**: CSPM products added bucket/public-access checks — configuration-only, no data-content sensitivity. They lack the classified inventory. Also supports the two-part object (data content + security state).
- **Regional/smaller products**: nothing in the definition assumes a specific cloud provider, deployment model, language, or jurisdiction; compliance mappings are generic ("regulations the finding violates").
- Conclusion: the L0 generalizes across the young category's poles and its ancestors. No historical contradiction found. One caveat recorded: the category's *flagship marketing* is currently AI-era (copilots/agents); the definition deliberately does **not** include AI surfaces (they are L2 extensions).

## Uncertainties

1. **Exact risk taxonomies** per product are only partially public (BigID's FAQ list and Prisma's risk-type/category/severity surfaces observed; full catalogs are behind consoles). The final document therefore describes risk *families* with examples, not exhaustive taxonomies.
2. **Posture-score methodology** is vendor-specific and undocumented publicly — mentioned as common capability, never explained numerically.
3. **Hyperscaler realization** (Microsoft Purview "DSPM for AI", AWS/GCP native options) unverified this pass — recorded as unverified, no claims.
4. **DSPM vs DDR seam** is still forming in the market; classification of DDR as variant/adjacent reflects current packaging variance, not a settled taxonomy.
5. **IBM/Varonis/Securiti poles** thin evidence; packaging-variant conclusions about "suite members" rest on suite-level pages + market structure, marked accordingly.
6. **Deployment topologies** (SaaS metadata plane vs in-environment) vary and are not fully documented for all sampled products; final document states the invariant (data of record stays in place; access is non-inline read-authorized) and presents topologies as variants.

## Final Synthesis

DSPM is a **security operations lens over the organization's own data estate**. Its world model:

```text
Connected data estate (cloud stores, warehouses, SaaS, on-prem shares — data of record in place)
  → Data inventory (stores/objects discovered, incl. unknown ones)
      → carrying sensitivity classification (what data is where)
          → evaluated for security state (exposure / access / protection / hygiene)
              → risk findings, prioritized by sensitivity × exposure × access
                  → worked by security operators (alerts, tickets, SOAR, owner routing)
                      → remediation (guidance → native actions → automation)
                          → compliance evidence + posture metrics (score, trends)
```

The Type is defined by the *combination*: a data map **with** a security-state evaluation **with** a findings loop. Discovery without evaluation is a catalog; evaluation without data content is CSPM; findings without the data lens are generic asset security. The management loop (findings worked by security operators toward remediation) is what "Posture Management" contributes beyond discovery/classification.

Packaging (pure-play vs CNAPP pillar vs platform use case vs suite member) is the market's main structural variant axis and does not change the core loop. DDR, identity enrichment, AI-era surfaces, estate breadth, and remediation enforcement depth are variant axes.

Taxonomy note for Boundary Issues: DSPM ships as a module of CNAPP/data-security platforms in several sampled products, but standalone pure-plays exist, and the market treats DSPM as an externally validated category (analyst radars/vendor-neutral usage across all samples). Type stands; packaging recorded as variant axis; recommend the future SSPM pass adopt the same "assessed object" discriminator (data content vs tenant configuration).
