# Research Notes — Greenhouse Gas Accounting

Research date: 2026-09-08
Slug: greenhouse-gas-accounting
Directory leaf: Greenhouse Gas Accounting (§21 Environment, Sustainability & Climate)

## Research Goal

Understand whether "Greenhouse Gas Accounting" is a distinct software Application Type, and if so what its core objects, workflows, and boundaries are. A second, equally important goal is pre-hung from the sibling pass: the carbon-accounting-platform pass (processed 2026-09-07) flagged this leaf as a PROBABLE NEAR-ALIAS — "GHG accounting" naming the methodology, "Carbon Accounting Platform" naming the software that performs it — and recommended joint review when this leaf was processed. This pass is that joint review; it must end in a verdict: merge/alias, or an explicit methodology-vs-software split.

## Initial Boundary

- Hypothesis: "Greenhouse Gas Accounting" names the accounting methodology (the GHG Protocol family: corporate GHG inventory from activity data × emission factors, gases aggregated to CO2e), and the directory leaf is meant to capture the software that performs this accounting. If so, the software population is the same population the sibling pass sampled as "carbon accounting" products.
- Candidate structures that could make it distinct: multi-gas coverage (CO2 + other Kyoto gases, not just "carbon"); public-sector / community-scale GHG inventories (city inventories under community protocols); conformance-and-certification machinery around the GHG Protocol; project-level or product-level accounting (separate GHG Protocol standards exist for both).
- Nearest neighbors: Carbon Accounting Platform (sibling, processed), ESG/Sustainability Management Platform, ESG Reporting Platform, Emissions Monitoring/CEMS, Energy & Carbon Management, Product Carbon Footprint Platform / LCA, Decarbonization Planning Platform, Carbon Credit Management, Climate Risk Management, Scope 3 Management Platform.
- Unknowns: whether any product population labels itself "GHG accounting software" to the exclusion of "carbon accounting"; whether public-sector inventory tools form a separate Type; how deep the certification/conformance layer goes.

## Research Questions

1. What does the methodology itself define as "GHG accounting" (standards body definition, gases, scopes, inventory)?
2. What do products that perform this accounting call themselves, and do the two label populations overlap?
3. Do the products' core structures match the sibling pass's defining core (organizational boundary + activity data + factors + computed inventory + auditability)?
4. Is multi-gas (CO2e) coverage a boundary or common machinery of the same Type?
5. Is the public-sector / community-scale GHG inventory (city-level) a separate Type or a customer-tier/sector variant?
6. What does the conformance/certification layer look like (who certifies, against what)?
7. Where do the methodological boundaries sit (product accounting, project/offset accounting, physical measurement)?
8. Historical check: does pre-platform practice (spreadsheets, earlier tool generations) satisfy the proposed core?

## Representative Products

Selected for a naming-angle spread and tiers different from (but overlapping with) the sibling sample:

| Product | Position | Why sampled |
|---|---|---|
| GHG Protocol (WRI/WBCSD) | the methodology itself, not a product | the standard that defines corporate GHG accounting; anchors terminology and methodological boundaries |
| Watershed | enterprise carbon/sustainability platform (US) | first-hand naming evidence: category page titled "carbon accounting" describing "greenhouse gas emissions" accounting |
| Plan A | mid-market carbon accounting software (DE/FR/UK) | brands as "Carbon Accounting Software" while certifying "GHG Protocol compliant" — both vocabularies on one page |
| Coolset | mid-market ESG & supply-chain compliance platform with carbon module (NL) | carbon management as one module of a compliance suite; methodology certified TÜV/SGS against GHG Protocol; customer story uses "GHG emissions reporting" |
| ICLEI ClearPath 1.0 / 2.0 | public-sector emissions management platform (US local governments) | the "GHG inventory" vocabulary pole; different customer tier (subnational governments); in-sample generational depth (1.0 established → 2.0 relaunched 2025) |
| Emitwise (→ Green Project) | supply-chain carbon platform, acquired 2025 | naming-population persistence evidence only; no longer sold standalone |

## Sources

Fetched 2026-09-08 (Tier 1/2 mix; no product's help center was reachable this pass):

- GHG Protocol — Corporate Standard page: https://ghgprotocol.org/corporate-standard
- Watershed — carbon accounting page: https://www.watershed.com/platform/measure/carbon-accounting
- Plan A — root: https://www.plana.earth/
- Coolset — root: https://www.coolset.com/
- ICLEI USA — ClearPath page: https://icleiusa.org/clearpath/
- Emitwise — acquisition/transition page: https://www.emitwise.com/

Source-access limitations:

- Sweep (sweep.com root and /product) returned empty responses twice — abandoned per network rules; not sampled.
- Carbon+Alt+Delete (carbonaltdelete.eu/en/) returned 403 — abandoned; not sampled.
- No public help center / operational documentation was fetched for any sampled product this pass (Plan A, Coolset, ClearPath, Watershed are evidenced from official product/marketing pages only). Operational claims are kept at the level those pages support.
- Community-scale inventory protocol documents (e.g., GPC) were not fetched; ClearPath claims kept at page level.
- Sibling pass evidence (Watershed, Persefoni, Microsoft Sustainability Manager, IBM Envizi, Greenly; Microsoft's operational docs) is recorded in research/carbon-accounting-platform.md and is used for the joint-review verdict as the repo's shared record, not re-fetched here.

## Product Observations

### GHG Protocol — Corporate Standard page (methodology anchor, evidence layer A)

- "The GHG Protocol Corporate Accounting and Reporting Standard provides requirements and guidance for companies and other organizations preparing a corporate-level GHG emissions inventory."
- Covers "the accounting and reporting of seven greenhouse gases covered by the Kyoto Protocol" — CO2, CH4, N2O, HFCs, PFCs, SF6, NF3; updated 2015 with the Scope 2 Guidance (purchased or acquired electricity, steam, heat, and cooling).
- Stated objectives: a "true and fair account" via "standardized approaches and principles"; "simplify and reduce the costs of compiling a GHG inventory"; "increase consistency and transparency in GHG accounting and reporting among various companies and GHG programs."
- Applies "equally to other types of organizations... e.g., NGOs, government agencies, and universities."
- Boundary: "It should not be used to quantify the reductions associated with GHG mitigation projects for use as offsets or credits; the GHG Protocol for Project Accounting provides requirements and guidance for this purpose."
- Calculation Tools: "cross-sector and sector-specific calculation tools... provide step-by-step guidance and electronic worksheets to help users calculate GHG emissions from specific sources or industries." — the methodology itself ships spreadsheet-era tooling; historical anchor.
- Standards family: Corporate Standard, Scope 2 Guidance, Corporate Value Chain (Scope 3) Standard, Product Standard, Project Protocol, Land Sector and Removals Standard/Guidance, "Actions and Market Instruments Standard" (under development).
- "Built On GHG Protocol" review service with a "Tools Built on GHG Protocol" register — the standards body's own mechanism recognizing software tools built on the methodology.
- Adoption claim: in 2016, 92% of Fortune 500 companies responding to CDP used GHG Protocol directly or indirectly; it "provides the accounting platform for virtually every corporate GHG reporting program in the world."

### Watershed — carbon accounting page (evidence layer A for the page; operational depth limited)

- Page title "Getting started with carbon accounting": "Carbon accounting is the first step in accurately measuring, reporting, and reducing your company's greenhouse gas emissions."
- Definition: "Carbon accounting is the process of assessing an organization's impact on the environment by calculating its emissions of carbon-based greenhouse gases. In general, emissions are calculated by multiplying business data (such as an employee travel budget or an office electric bill) by an 'emissions factor,' or average emissions generated by that activity."
- Software-buying framing: "How to choose the right carbon accounting software for your business" — the product category is named "carbon accounting software," while the object is "greenhouse gas emissions."
- Small vs large company must-haves: small = manual upload, single-region models (US EEIO), 1–2 measurements/year, manual export; large = automated integrations + upload, Scope 1–3, multi-region models (CEDA), multiple measurements/year, reporting, benchmarking, target-setting, simulations, audit trail and data governance.
- Machinery described: 60+ pre-built integrations and flexible file upload; embedded project management for departmental data collection; "proprietary carbon data engine" with anomaly detection and gap filling; granular science-based factors from "tens of thousands of benchmarks and emissions models" incl. multi-region CEDA; integrated supplier engagement for Scope 3; Disclosures toolset that "automatically formats your data to match disclosure requirements"; target-setting and reductions modeling; enterprise data management with "complete audit trails for all carbon data" and visibility into "how each number was calculated."
- Vendor claim (noted, not generalized): "When audited, 100 percent of Watershed customer footprints have passed."

### Plan A — root page (evidence layer A for the page)

- Page title: "Carbon Accounting Software by Plan A."
- Product nav: Carbon Accounting (Emissions measurement; Data collection) / Reporting (Carbon reporting) / Decarbonisation (Emissions reduction; Target setting) — a measure → report → reduce journey.
- Positioning: "Your certified software for reliable emissions intelligence to measure, report and reduce your carbon footprint." Badge: "Certified GHG Protocol compliant" (TÜV Rheinland); B Corp; "Developed by scientific experts"; "AI-enhanced interface" (Gaia AI assistant).
- "Measure and analyse your corporate carbon footprint with precision"; "Disclose your sustainability progress with integrated carbon footprint reports"; "Achieve emission reductions through targeted actions and accurate forecasts."
- Supplier engagement: "uncover opportunities by engaging your suppliers."
- Marketing metrics (vendor claims, research only): 70% faster data management, "130+ days saved on carbon accounting," "20x reporting speed."
- Customers: mid-market/enterprise European mix (software, mobility, finance, fashion logos).

### Coolset — root page (evidence layer A for the page incl. structured data)

- Self-description: "ESG & Supply Chain Compliance Platform" helping "ESG, procurement, and compliance teams manage emissions and meet CSRD, EUDR, and CBAM requirements - all in one audit-ready platform" (mid-market enterprises, 500+ customers claimed).
- Modules: ESG compliance; **Carbon management — "Measure and reduce Scope 1-3 emissions."** Reporting card: "Report on scope 1 - 3 — Extract carbon footprint data for seamless reporting."
- Guided product tours include "GHG Scope 1-3" alongside CSRD, EUDR, PPWR, VSME, EU Taxonomy, EcoVadis.
- Conformance layer (page footer + structured data): badges "Compliant with GHG Protocol" — TÜV Rheinland test mark (TR-Testmark 0000086794) described as "Carbon measurement methodology independently certified by TÜV Rheinland for Scope 1-3 emissions per the GHG Protocol"; plus "SGS GHG Protocol Methodology" audit approval.
- Case-study headline uses the other vocabulary: "Alpina Group professionalises GHG emissions reporting with Coolset."
- Base platform: "Auditable reporting, Cross-team collaboration, On-demand analytics"; customer-success manager, in-house sustainability researchers, accelerator programs, and an "auditor network" of "vetted auditors for streamlined limited assurance."
- Note: here the accounting core (Scope 1–3 measure/report/reduce) is one module inside a broader compliance platform — the ESG-suite-membership posture the sibling pass also observed.

### ICLEI ClearPath — page (evidence layer A for the page)

- "ClearPath 1.0 was ICLEI USA's established emissions management platform for completing greenhouse gas inventories, forecasts, climate action plans, and monitoring at the community-wide or government-operations scale."
- ClearPath 2.0 — "launched in spring 2025," "powered by ClimateView": "the revamped industry-standard emissions management platform" / "a revamped climate action planning and implementation platform... to help U.S. subnational governments make data-driven decisions, engage stakeholders, and drive transparent climate action."
- Related ICLEI tools on the same site: "GHG Contribution Analysis — Drivers of community emissions analysis tool"; "GHG Protocols — Guidance for communities to account for carbon emissions."
- Observations: the public-sector pole uses "greenhouse gas inventories" / "emissions management" vocabulary, not "carbon accounting"; the measured inventory remains the anchor (inventories, monitoring) with forecasts and action plans as planning extensions; the accounting unit is the community or government operations rather than the company — but the structure (bounded organization + emitting activities + computed inventory over a period) is the same accounting core.

### Emitwise → Green Project Technologies (naming-population note, evidence layer A, thin)

- Emitwise is "no longer sold as a standalone product or brand" (acquired July 2025); the technology continues inside Green Project's "suite50, which combines supplier engagement, carbon accounting, and renewable energy procurement in one platform."
- Use: the acquired technology's accounting capability is still described with the category label "carbon accounting" — the label persists across ownership changes.

## Cross-product Comparison

| Structure | GHG Protocol (methodology) | Watershed | Plan A | Coolset | ICLEI ClearPath | Layer |
|---|---|---|---|---|---|---|
| Bounded organization as unit of account (company OR other org / community) | ✓ (companies "and other organizations"; communities via community protocols) | ✓ | ✓ (corporate footprint) | ✓ (Scope 1–3 for the enterprise) | ✓ (community-wide or government operations) | Core (A/B) |
| Activity/business data as records to account | ✓ (calculation tools per source/industry) | ✓ (travel budget, electric bill; integrations/upload) | ✓ (data collection) | ✓ (extract footprint data) | ✓ (inventories from community data) | Core (A/B) |
| Emission factors converting activity → emissions | ✓ (calculation tools embody factors) | ✓ ("multiplying business data by an emissions factor") | ✓ (certified methodology) | ✓ (certified per GHG Protocol) | ✓ (protocol guidance) | Core (A/B) |
| Computed GHG inventory over a period | ✓ ("preparing a corporate-level GHG emissions inventory") | ✓ (Scope 1–3 footprints, 1-2×/yr small, multiple large) | ✓ (carbon accounting step 1) | ✓ (Scope 1–3 report) | ✓ (GHG inventories; monitoring) | Core (A/B) |
| Multi-gas coverage → CO2e | ✓ (seven Kyoto gases) | ✓ ("carbon-based greenhouse gases"; gas handling in sibling pass) | ✓ (GHG Protocol-conformant) | ✓ ("per the GHG Protocol", Scope 1–3) | ✓ (GHG inventories) | Core (A) — methodology-defined |
| Traceability/auditability of results | ✓ (standard designed for verifiable inventory; verification itself out of scope of the standard) | ✓ (audit trails, per-number calculation visibility) | ✓ (auditable reporting posture) | ✓ (audit-ready platform; auditor network) | ✓ (transparent climate action posture) | Core (A/B) |
| "Carbon accounting" as the software category label | — | ✓ (page title; "carbon accounting software") | ✓ (page title) | (module named "Carbon management") | — (uses "emissions management / GHG inventories") | A: market's dominant product label |
| "GHG" vocabulary for the same work | ✓ (the standard's own name) | ✓ ("greenhouse gas emissions" as object) | ✓ ("Certified GHG Protocol compliant") | ✓ ("GHG Scope 1-3"; "GHG emissions reporting" case study) | ✓ ("greenhouse gas inventories") | A: methodology's label, mixed freely |
| Scope organization (1/2/3) | ✓ (Scope 2 Guidance; Scope 3 Standard) | ✓ (Scopes 1–3) | ✓ (GHG Protocol conformant; sibling pass) | ✓ (Scope 1–3) | — (community-scale protocol instead) | Common mature (B) — dominant implementation |
| Conformance/certification layer | ✓ (Built On GHG Protocol register) | ✓ (assured methodologies claim) | ✓ (TÜV mark) | ✓ (TÜV + SGS marks) | ✓ (protocol-guided tool lineage) | Common (B) — trust machinery, not structure |
| Disclosure outputs | — (standard is program-neutral) | ✓ (Disclosures toolset) | ✓ (carbon reporting) | ✓ (CSRD-class compliance) | ✓ (public climate action reporting) | Common mature (B) |
| Targets + reduction planning | — (out of the accounting standard) | ✓ (target modeling, reductions) | ✓ (decarbonisation module) | ✓ ("measure and reduce") | ✓ (forecasts, climate action plans) | Common mature (B) — extension, not core |
| Supplier/value-chain engagement | — (Scope 3 Standard covers method) | ✓ (integrated supplier engagement) | ✓ (supplier engagement) | ✓ (supply-chain compliance posture) | — | Common mature (B) |
| Suite embedding (accounting as module of ESG/compliance platform) | — | — (standalone platform) | — (focused product) | ✓ (module of compliance platform) | ✓ (tool of a membership org's program) | Variant (delivery posture) |
| Public-sector / community-scale unit | — (separate standards exist for communities via programs) | — | — | — | ✓ | Variant (customer tier / sector) |

Joint-review note: the sibling pass's sample (Watershed, Persefoni, Microsoft Sustainability Manager, IBM Envizi, Greenly — research/carbon-accounting-platform.md) lands in the same population and shows the same double vocabulary (Envizi's engine "built on the GHG Protocol"; Microsoft's docs speak of "GHG emissions"). Two independent passes sampling different pages of the same population strengthens the alias verdict.

## Canonical Model (abstraction)

### L0 — Defining Invariant (minimal)

The software type recognizable as "GHG accounting" / "carbon accounting" requires all of:

1. **A bounded organization as the unit of account** — a company, institution, agency, or community whose emissions are being accounted (not a product, not an individual).
2. **Activity data records** — quantified records of the organization's emitting activities (energy purchased, fuel burned, materials bought, travel, waste), each bound to the organization's units and a time period.
3. **Documented emission factors** — coefficients converting activity into greenhouse gas emissions, with traceable sources/methodology.
4. **A computed inventory** — emissions calculated (activity × factor, per gas, aggregated to CO2e via global warming potentials) and assembled into an inventory of the organization over a reporting period.
5. **Auditability** — the path from each reported figure back to activity data, factor, and method is recorded and inspectable.

Remove the organizational unit of account → product footprint/LCA; remove factors and computation → raw data collection or disclosure formatting; remove the inventory-over-period → ad-hoc calculators; remove multi-gas CO2e accounting → not what any sampled tool means by the term; remove auditability → the output cannot serve the disclosure and verification purposes that motivate the accounting.

### L1 — Common Mature Structure

- Scope organization (Scope 1 direct, Scope 2 purchased energy, Scope 3 value chain with categories) per the GHG Protocol — the dominant implementation of organized emission categories; alternative category schemes exist (ISO-style, community protocols).
- Organizational hierarchy (sites, business units, regions) as the attribution and roll-up dimension.
- Data ingestion machinery: system integrations, file upload, manual entry, supplier surveys/portals.
- Emission factor libraries from published sources, versioned; factor mappings; custom and estimation factors.
- Calculation method choices (spend vs activity-based; location vs market-based energy accounting; distance/fuel/spend for transport; attribution for financed emissions), recorded with results.
- Data-quality machinery: anomaly detection, completeness checks, approval staging, period closing/locking.
- Disclosure outputs aligned to climate frameworks and regulations.
- Analytics, hotspot identification, year-over-year comparison.
- Reduction targets and progress tracking; reduction planning as a common extension.
- Supplier engagement to improve value-chain data.
- Conformance/certification signaling against the GHG Protocol (including third-party certification marks and the standards body's own tools register).

### L2 — Variant / Optional Structure

- Customer-tier/sector variants: public-sector and community-scale inventories (city/community protocols; government-operations vs community-wide scales), financial-services financed-emissions specializations, consultancy-served accounting.
- Delivery postures: standalone product vs module of an ESG/compliance/sustainability suite vs platform-ecosystem module; self-serve SMB vs enterprise sales-led.
- Extended environmental metrics (water, waste), product-footprint extensions, decarbonization roadmaps/scenario modeling — common extensions that drift toward neighboring Types when they become the center of gravity.
- Regional factor regimes and languages; AI assistance throughout current products.
- Forecasting and climate action planning attached to the inventory (public-sector pole).

### L3 — Vendor-specific (research notes only)

- Watershed: CEDA multi-region model, "60+ pre-built integrations", "tens of thousands of benchmarks and emissions models" claim, footprint-pass audit claim, Disclosures toolset naming.
- Plan A: TÜV Rheinland mark, B Corp, Gaia AI assistant, marketing metrics (70% / 130+ days / 20x), Scientific Advisory Board.
- Coolset: TÜV test mark TR-Testmark 0000086794 + SGS methodology approval, MCP integration ("Explore Coolset in your favourite AI assistant"), auditor network for limited assurance, CSM + researchers + accelerator programs bundle.
- ICLEI ClearPath: 1.0 → 2.0 transition (2.0 launched spring 2025, powered by ClimateView); sibling tools "GHG Contribution Analysis" and "LEARN" (forest/tree emissions mapping); membership-org delivery model.
- Emitwise/Green Project: suite50 bundling (supplier engagement + carbon accounting + renewable energy procurement).

## Vendor-specific Findings

All L3 items above. None enter the canonical document except as neutral examples where useful.

## Boundary Findings

- **vs Carbon Accounting Platform (sibling leaf) — ALIAS VERDICT.** The two leaves name one software Type from two naming angles. Evidence: (1) the methodology's own name is "GHG accounting" — the GHG Protocol Corporate **Accounting** and Reporting Standard for a corporate-level GHG emissions inventory; (2) the market's product-category label is "carbon accounting software" (two of this pass's sampled vendors title themselves exactly that; the acquired Emitwise technology is still described as "carbon accounting" inside its new owner's suite); (3) every sampled product mixes both vocabularies on the same page — Watershed's "carbon accounting" page defines the work as measuring "greenhouse gas emissions"; Plan A brands as carbon accounting software while certifying "GHG Protocol compliant"; Coolset sells "Carbon management" with "GHG Scope 1-3" tours and a customer story titled "GHG emissions reporting"; ClearPath's public-sector pole says "greenhouse gas inventories" where a commercial vendor would say carbon accounting; (4) this pass's independently derived defining core is identical to the sibling pass's (boundary + activity data + factors + computed inventory + auditability); (5) no product population was found that calls itself "GHG accounting software" to the exclusion of "carbon accounting." Verdict per precedent (recruiting-management-platform/ATS; online-marketplace/multi-vendor-marketplace): alias — keep both leaves documented and cross-referenced, recommend consolidation to the taxonomy owner; do not treat as two Types. The methodology is not a separate Type either: it is the standard the software implements, and the standards body itself maintains a register of "Tools Built on GHG Protocol."
- **Multi-gas coverage is not a boundary.** "GHG" points at the seven Kyoto gases vs the "carbon" metonym, but all sampled tools in both passes account for multiple gases and aggregate to CO2e; the GHG Protocol defines the gases. Common machinery of the same Type.
- **vs Product Carbon Footprint Platform / LCA.** The methodology itself separates levels of account: the GHG Protocol ships a separate Product Standard for product-level accounting; the corporate standard is written for the organization. Same seam the sibling pass observed.
- **vs Carbon Credit Management / project accounting.** Methodology-anchored: the Corporate Standard "should not be used to quantify the reductions associated with GHG mitigation projects for use as offsets or credits; the GHG Protocol for Project Accounting provides requirements and guidance for this purpose." Offset/credit accounting is a different methodology and the instruments belong to the credit-management Type.
- **vs Emissions Monitoring / CEMS.** Computed from activity data × factors vs physically measured at sources with instruments (sibling pass's seam; not re-researched).
- **vs ESG/Sustainability Management suites.** Coolset demonstrates the seam from the suite side: the accounting core (Scope 1–3 measure/report/reduce) is one module; when compliance/regulatory breadth (CSRD/EUDR/CBAM, policies, due diligence) becomes the center of gravity, the product is an ESG/sustainability platform carrying an accounting module, not an accounting system of record.
- **vs Decarbonization Planning / public-sector climate action planning.** ClearPath adds forecasts and climate action plans on top of inventories — planning extensions; the measured inventory remains the anchor in all sampled products.
- **Remove-tests:** remove the organizational boundary → Product Carbon Footprint/LCA; remove factors/computation → data collection or disclosure tooling; remove inventory-over-period → calculator; remove auditability → internal estimates that cannot survive external scrutiny; swap the unit to a project → project/offset accounting (Carbon Credit territory); swap the unit to a product → PCF/LCA.

## Uncertainties

- Absence-of-evidence risk on the alias verdict: Sweep (empty ×2) and Carbon+Alt+Delete (403) could not be sampled; no help-center documentation was fetched this pass. A product that markets itself strictly as "GHG accounting" software excluding "carbon accounting" was not found, but the search breadth was moderate (five fetches plus the sibling's five-product record).
- Regional label preference (e.g., non-English markets preferring "GHG" or "treibhausgasbilanz"-class terms) unverified.
- ClearPath's operational structure (community-scale protocol categories, inventory data model) not directly fetched; community-scale variance kept at variant strength.
- Certification depth: test-mark descriptions come from vendor pages/structured data; the certification schemes themselves were not investigated. Kept as trust machinery (L1) with vendor specifics in notes.
- The "GHG accounting" leaf could in principle have been intended as the *methodology* node (a knowledge artifact, not software). The directory's own convention (Application Types are software) and the sibling flag's candidate outcomes both indicate software; resolved as software alias.

## Final Synthesis

"Greenhouse Gas Accounting" is the methodology's name for the accounting that "Carbon Accounting Platform" names as a product category — one software Type, two labels. The GHG Protocol defines the methodology: a bounded organization compiles a GHG emissions inventory from activity data multiplied by documented emission factors, covering the Kyoto gases aggregated to CO2e, over reporting periods, designed for verification. The software that performs it — titled "carbon accounting software" by the market, certified "GHG Protocol compliant" by its vendors, described in "greenhouse gas inventories" terms by its public-sector implementations — has exactly the defining core the sibling pass derived: organizational boundary + activity data records + emission factors + computed auditable inventory. Both passes sampling different pages of the same product population converge on the same structure and the same double vocabulary. Verdict: alias; keep both documents standing and cross-referenced (this document written from the methodology-naming angle: conformance, multi-gas CO2e, the inventory as deliverable, the public-sector pole); recommend consolidation at a taxonomy pass.
