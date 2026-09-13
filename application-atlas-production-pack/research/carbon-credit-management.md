# Research Notes — Carbon Credit Management

Research date: 2026-09-07
Slug: carbon-credit-management
Directory leaf: Carbon Credit Management (§21 Environment, Sustainability & Climate)

## Research Goal

Understand what "Carbon Credit Management" software actually is as an Application Type: what objects exist inside it, who uses it, what workflows it supports, and where its boundary lies against Carbon Accounting Platform, Carbon Trading Platform, and Renewable Energy Certificate Management.

## Initial Boundary Hypothesis

- Hypothesis: software that treats carbon credits / offsets as managed assets — an inventory/portfolio of credits with identity (project, standard, vintage), custody, acquisition and disposition transactions (including retirement/cancellation against emissions claims), and an evidence trail for audit and reporting.
- Likely confusions:
  - Carbon Accounting Platform (measures the organization's own emissions — different object)
  - Carbon Trading Platform (market execution/exchange — different job)
  - Renewable Energy Certificate Management (same structural pattern, different instrument)
  - ESG Reporting Platform (consumes credit data; does not manage credits)
  - Registry systems (Verra/Gold Standard-class) — authoritative issuance/retirement infrastructure operated by standards bodies, not organization-side management software

## Research Questions

1. What is the core object (the credit) and what identity attributes does it carry?
2. What lifecycle states do credits move through (forecast/issued/held/retired; forecast→measured→verified→issued on the supplier side)?
3. Who are the actors (corporate buyers, project developers/suppliers, brokers, advisors)?
4. What does "management" concretely mean: inventory, procurement, retirement, delivery risk, reporting?
5. How do registries and retirement records appear in the product?
6. What interfaces exist (portfolio dashboard, project catalog, procurement workspace, supplier consoles, API)?
7. Where is the boundary vs Carbon Accounting, Carbon Trading, and REC Management?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer levels:

| Product | Philosophy / pole | Customer level |
|---|---|---|
| Patch | buyer-side procurement + portfolio platform (strategy→sourcing→diligence→purchase→manage) | enterprise |
| Cloverly | dual-sided: buyer API/storefront + supplier-side commerce software (Catalyst) | SMB→enterprise + project developers |
| Carbon Direct | science-led buyer-side carbon management (curated/bespoke portfolios + platform) | enterprise / Fortune 500 |
| Watershed | broad sustainability suite with Marketplace as one module | enterprise |

Market context (not primary samples; credit modules not directly observed on current public surfaces): Persefoni (carbon accounting; lists Patch as partner), Sweep (carbon accounting/ESG; current carbon page is measurement-focused).

## Sources

All fetched 2026-09-07 (Tier 1/2 official product pages):

- Patch — https://www.patch.io/ , https://www.patch.io/how-it-works , https://www.patch.io/rfp , https://www.patch.io/purchase (docs.patch.io is JS-rendered; root/how-it-works/rfp fetched successfully)
- Cloverly — https://www.cloverly.com/ , https://www.cloverly.com/catalyst/commercial-credit-operations , https://www.cloverly.com/buyers
- Carbon Direct — https://www.carbon-direct.com/ , https://www.carbon-direct.com/solutions/remove
- Watershed — https://www.watershed.com/ , https://www.watershed.com/platform/marketplace
- Sweep — https://www.sweep.net/ , https://www.sweep.net/carbon-management (context: accounting-focused)
- Persefoni — https://www.persefoni.com/ , https://www.persefoni.com/business/decarbonization-management (context: accounting/reduction-focused)

Source-access limitations: Patch's developer docs (docs.patch.io) returned a JS shell — no API-level detail claimed. Watershed Marketplace FAQ answers were truncated in fetch; retirement mechanics for Watershed not directly observed. No help-center-level operational documentation was reachable for any sampled product; all observations are from official product/marketing pages (Tier 2). Assertion strength calibrated accordingly; no numeric limits, prices, or default settings asserted in the final document.

## Product Observations

### Patch (buyer-side enterprise platform) — Evidence Layer A

From /how-it-works, /rfp, /purchase:

- Positioning: "AI-native services company"; "The Patch System" platform for environmental markets (carbon credits primary; also SAFc, RECs mentioned in strategy copy).
- Five-step process: **Strategy → Sourcing → Diligence → Purchase → Manage**.
  - Strategy: embedded climate strategists; align company goals to climate goals; define purchase criteria (types of environmental resources, volumes, portfolio mix, budget); spot purchases and offtake agreements.
  - Sourcing: access to a broad range of environmental resources; "every project type — from avoidance to removal, nature-based to engineered"; can source from specific preferred suppliers; "neutral criteria matching" (Patch states it does not own credits); actionable insights: project details, indicative inventory available from suppliers, price trends based on real transaction data.
  - Diligence: strict criteria "based on the latest science, standards, and methodologies"; platform centralizes and standardizes "hundreds of disparate project attributes"; AI-assisted diligence evaluations.
  - Purchase: "We take care of delivery and retirement"; collect and negotiate offers from multiple suppliers for the same project; multiple projects, one contract and payment; manage retirement; spot purchasing or complex multi-year offtake agreements; lock in tonnage and pricing.
  - Manage: "real-time visibility into every credit you own — including those purchased outside the platform, so you can audit the past and plan for the future"; "Every credit includes its registry ID, delivery status, and a registry-linked retirement record so it's audit-ready on demand, whether for CSRD, AB 1305, or internal sign-off"; protection against credit defaults (replace credits at no additional fee if a project fails to deliver a future vintage).
- RFP page: procurement workflow productized — on-demand market pulse (inventory availability, project data, diligence analyses, pricing insights); multi-vendor sourcing in one place; offer review and management moved "out of your inbox and into a streamlined platform"; expert negotiation; transparent offer tracking.
- Demo form interest areas mirror the workflow: Strategy (claims, budgeting), Sourcing, Diligence, Purchasing (spot vs multi-year), Management (monitoring, reporting, risk).
- Vendor claims kept out of final doc: "200+ suppliers", "save 10-20% on price of credits", named customers.

### Cloverly (dual-sided: buyer API/storefront + supplier commerce software) — Evidence Layer A

From /, /catalyst/commercial-credit-operations, /buyers:

- **Buyer side**: vetted high-quality projects; spot, forward, or offtake agreements; single project or curated portfolios; "streamlined contracts, payments, and retirement management"; buyers get "curated carbon removal projects and data without worrying about tracking down the certificates and retirement information yourself"; API with real-time project information, structured and queryable metadata, real-time dashboard; branded storefront option; in-house climate science team for vetting/consultation.
- **Supplier side (Catalyst)**: "The Commercial Operating System for Carbon Credit Project Developers" — "end-to-end software platform for carbon credit project developers to centralize inventory, streamline operations, and grow revenue."
  - **Inventory Management**: "Manage credits through forecast, measure, verified and issued stages" (vendor stage names).
  - **Pricing Management**: default prices per batch of credits in inventory; update pricing across all channels in one place.
  - **Content Management**: project content across all sales channels from one single source of truth.
  - **Payments & Invoicing**: capture information needed to plan and track credit deliveries.
  - **Delivery Management**: "facilitate secure and accurate transactions."
  - **Data & Reporting**: reliable information hub; integrate with other systems.
  - **Direct Sales Tools**: branded buyer portal, proposal builder, automated RFP responses.
  - **Omnichannel Distribution**: reach several demand channels from one source of truth.
  - Audience: nature-based solutions, tech-based solutions, early-stage developers.
- Case-study language: "a source of truth for their carbon credits" (Bioforestal); "manage our inventory and the operational backbone to scale our commercialization efforts" (Three Oaks Carbon).

### Carbon Direct (science-led buyer-side carbon management) — Evidence Layer A

From / and /solutions/remove:

- Positioning: "Measure, reduce, and remove" — Measure / Reduce / Remove / Report solutions + Advisory + Platform.
- Remove (credit side):
  - **Curated carbon removal portfolios**: pre-vetted portfolios matched to budget, diverse projects and benefits.
  - **Bespoke procurement**: custom portfolio development — project sourcing, due diligence, forward offtake agreements, delivery support.
  - **Scientific vetting**: deep scientific diligence by 60+ scientists; projects evaluated against published "Criteria for High-Quality Carbon Dioxide Removal" (co-authored with Microsoft); multi-stage review.
  - **Beyond-carbon benefits**: criteria for environmental/social harms, benefits, environmental justice.
  - **Flexible purchasing and contracting**: contracts directly with projects; in-year purchasing for annual goals; multi-year forward offtake to secure future supply and lock pricing.
  - **De-risked delivery with credit protections**: multi-project sourcing, monitoring at key stages of project development, early notification of delays, offtake structures weighted towards payment on delivery, replacement options vetted by Carbon Direct.
- **Platform**: "Easily track and manage carbon credit purchases and retirements… manage and monitor the status of the credits in your portfolio… automatically get updates… track and report on the impact of your carbon removal purchases."
- Market framing: scarcity of high-quality credits; greenwashing risk; complexity of VCM as the problems the product solves.

### Watershed (sustainability suite with Marketplace module) — Evidence Layer A (retirement mechanics not observed)

From / and /platform/marketplace:

- Broad platform: Measure (2.3M emission factors library — vendor claim), Report (disclosures/CSRD/SB 253), Act (decarbonization), **Marketplace**.
- Marketplace: "Climate projects with proven impact" — carbon removal, clean power, SAFc; vetted supplier list (Frontier AMC, SAF certificates, wind VPPA, DAC, reforestation, enhanced weathering, bio-oil, EACs, SABA).
- Vetting methodology: six considerations — additionality, verification, permanence, leakage, catalytic nature, co-benefits.
- Portfolio + integration: "Build a diverse portfolio aligned with your business priorities, commitments and reduction plans, then manage projects together with your key stakeholders. Centralize purchase records, scale supplier engagement, and see the impact on your overall carbon footprint, all on one platform."
- Combined buying power framing (access to projects historically requiring eight-figure investments).
- FAQ questions exist on monitoring impact of Marketplace purchases (answers truncated in fetch — retirement mechanics not directly observed).

### Context products (not primary samples)

- **Sweep**: current carbon-management page is entirely emissions accounting (Scopes 1–3, emission factors, PCF, targets). Offsetting appears only as narrative ("purchasing carbon credits to offset" unavoidable emissions). No credit-management module observed on fetched surfaces.
- **Persefoni**: carbon accounting + reporting + decarbonization planning; Patch listed as a partner. No credit-management module observed on fetched surfaces.

## Cross-product Comparison

| Dimension | Patch | Cloverly | Carbon Direct | Watershed | Layer |
|---|---|---|---|---|---|
| Credit as identified object tied to project/registry | registry ID per credit, registry-linked retirement record | batches in inventory with stages; certificates | credits in portfolio with status; project contracts | vetted projects; purchase records | B |
| Portfolio/inventory as managed unit | portfolio incl. credits bought off-platform | inventory (supplier) / curated portfolios (buyer) | curated + bespoke portfolios | "build your portfolio" | B |
| Acquisition transactions | spot + multi-year offtake; offers/negotiation | spot, forward, offtake; contracts, payments | in-year + multi-year forward offtake | purchases via Marketplace | B |
| Retirement / disposition | registry-linked retirement record; "we take care of… retirement" | "retirement management"; certificates tracked | "track and manage carbon credit purchases and retirements" | not directly observed (purchase records only) | B (3/4) |
| Quality vetting / diligence layer | criteria + AI diligence evaluations | in-house climate scientists vet projects | scientific criteria + 60+ scientists | six-consideration methodology | B |
| Delivery risk management | default protection with replacement | delivery planning/management (supplier side) | delivery protections, replacement options, payment-on-delivery weighting | not observed | B (2/4) |
| Procurement machinery | RFP workspace, offer management, negotiation | proposal builder, automated RFP responses, buyer portal | bespoke procurement service | purchase records centralization | B |
| Reporting / audit posture | audit-ready (CSRD, AB 1305 naming) | data & reporting hub | track and report impact | integrated with disclosures platform | B |
| Human expertise layer | embedded climate strategists | in-house climate science team | 60+ scientists, advisory | science advisory board | B |
| Supplier-side commerce | not observed | Catalyst (inventory stages, pricing, content, delivery, omnichannel) | supplier program (supply scaling) | not observed | A (Cloverly-specific pole) |
| API / embedded integration | not observed on current pages | API + storefront + queryable metadata | not observed | not observed | A (Cloverly-specific) |
| Integration with emissions accounting | claims/budgeting in strategy; audit frameworks | ESG goals framing | Measure/Reduce/Report siblings | same platform as footprint | B |
| Instrument scope beyond carbon | SAFc, RECs mentioned | carbon credits | carbon removal focus (+ SAF service) | removal, clean power, SAFc, EACs, VPPAs | B |

## Canonical Model (abstraction)

### L0 — Defining Invariant

The smallest structure without which the software stops being carbon credit management:

1. **Credit as identified tracked object** — a unit of verified climate benefit bound to an identified source (project, standard/registry, vintage) and carried with identity attributes. Without identity, credits are indistinguishable from generic commodity units and integrity/anti-double-counting collapses.
2. **Portfolio / inventory custody** — the organization's holdings of credits as a managed, persistent collection (who holds what, how much, in what state).
3. **Transactional movement with recorded state** — credits enter (purchase/agreement/issuance), move (transfer, delivery), and exit (retirement/cancellation against claims; sale/delivery on the supplier side), and each movement is recorded against the credit.
4. **Evidence trail binding credits to provenance and use** — registry references, retirement/delivery records, certificates, purchase records — because the credit's value depends on verifiable, non-double-counted provenance and defensible claims.

Test: remove (1) → generic inventory system; remove (2) → a marketplace/listing site without custody; remove (3) → a static registry mirror; remove (4) → a trading blotter without claim support. Any removal stops the product from being carbon credit management.

### L1 — Common Mature Structure

Present across the sample (evidence layer B):

- project catalog with rich attributes (type, location, methodology, co-benefits, price signals)
- quality vetting / diligence layer (criteria, scientific review, ratings-style evaluation)
- procurement machinery (RFPs, offers, negotiation, contracts; spot vs forward/offtake)
- retirement management with registry-linked records / certificates
- delivery risk management (monitoring, delay notification, replacement protections)
- reporting and audit-ready exports (framework alignment, claims support)
- portfolio dashboards (status, impact, spend)
- human expertise layer (strategists / climate scientists / advisory)

### L2 — Variant / Optional Structure

- **Side of market**: buyer-side only (Patch, Carbon Direct), supplier-side only (Cloverly Catalyst as a distinct product), or both (Cloverly overall)
- **Instrument scope**: carbon-only vs broader environmental attributes (RECs, SAFc, EACs, clean power/VPPA)
- **Voluntary vs compliance market posture**
- **API/embedded integration** vs console-only
- **Marketplace vs curated portfolio vs bespoke procurement** acquisition models
- **Suite membership**: standalone vs module of a sustainability platform (Watershed) or accounting suite
- **AI-assisted diligence** (era-current; present in Patch, framed in others)
- **Default/replacement guarantees** (Patch, Carbon Direct — two of four)

### L3 — Vendor-specific (research notes only)

- Patch: "200+ suppliers", "10–20% savings" claims, AB 1305/CSRD naming, default-replacement-at-no-fee, "Patch doesn't own credits" neutrality stance, Embedded Climate Strategists branding, Radius/Offtake product names.
- Cloverly: Catalyst stage names (forecast/measure/verified/issued), omnichannel distribution, branded storefront, proposal builder, monthly-shipments/tons-offset stats, CEEZER partnership.
- Carbon Direct: Criteria for High-Quality CDR (Microsoft co-authorship), 60+ scientists, "only 4% of credits are removal" market stat, payment-on-delivery offtake weighting, Carbon Direct Capital.
- Watershed: six vetting considerations, Frontier AMC / SABA listings, 2.3M emission factors, 30+ projects claim, Verdantix/CDP badges.

## Vendor-specific Findings

See L3 above. None promoted to the canonical model.

## Boundary Findings

- **vs Carbon Accounting Platform**: accounting measures the organization's own emissions (Scopes 1–3, activity data, emission factors). Credit management tracks offset instruments as assets. Watershed and Carbon Direct span both — the credit module is distinct from the measurement module. Test: remove credits → still carbon accounting (Sweep, Persefoni prove this); remove emissions measurement → still credit management (Patch and Cloverly Catalyst have no measurement module).
- **vs Carbon Trading Platform**: trading is market execution (price discovery, exchange/order-book mechanics, speculation). Credit management is custody + lifecycle + claims evidence. Overlap exists at procurement, but the defining object differs: trade execution vs managed holding. The directory carries both leaves; the seam is custody/claims vs market execution.
- **vs Renewable Energy Certificate Management**: identical structural pattern (tracked environmental attribute units, retirement against claims, registry linkage) with a different instrument (energy attributes vs carbon). Sibling Type; REC management is not a variant of carbon credit management because the instrument, registries, and claim semantics differ.
- **vs ESG Reporting Platform**: reporting consumes credit data as one input among many; credit management produces and maintains that data with registry-grade provenance.
- **vs Registry systems** (Verra/Gold Standard-class): registries are the authoritative issuance/retirement infrastructure operated by standards bodies; credit management is the organization-side system of record that references registries and holds mirror records.
- **"去掉什么就变成另一个 Type" 判据**: remove the credit object and custody (keep measurement) → Carbon Accounting Platform; remove custody/claims (keep market execution) → Carbon Trading Platform; swap the instrument → Renewable Energy Certificate Management; remove the asset layer entirely (keep disclosure) → ESG Reporting Platform.

## Historical / Market-Sample Check (§24)

- Would older, regional, or platform-native products fit the L0? Yes: compliance-market participants (e.g., EU ETS operator holding accounts) hold, transfer, and surrender units with registry evidence — the same four invariants, without any marketplace, AI diligence, or API. Early voluntary-market buyers tracked credits in spreadsheets plus registry accounts — still the same invariants (tracked credit objects, custody, recorded transactions, evidence).
- Therefore marketplace, AI diligence, advisory services, and framework-specific reporting (CSRD/AB 1305) are era-current implementations, not definitional.

## Uncertainties

- Watershed retirement mechanics not directly observed (FAQ answers truncated); only purchase records and portfolio integration observed.
- Patch developer docs unreachable (JS shell); no API-level claims made for any product.
- Exact retirement semantics (initiation, timing, cancellation vs retirement terminology across registries) not directly observed; kept generic in the final document.
- Cloverly Catalyst stage names are vendor-specific; the general issuance pipeline (forecast → measured → verified → issued) is inferred as a common supplier-side pattern from a single product — marked as such.
- Sweep and Persefoni credit modules not observed on current public surfaces; excluded from the sample.
- No help-center-level operational documentation was reachable for any sampled product; all claims are calibrated to product-page evidence.

## Final Synthesis

Carbon Credit Management is the organization-side system of record for carbon credits as managed assets. Its defining core is small: identified credits (project/standard/vintage), a portfolio/inventory holding them, recorded transactions that move them (acquire → hold → transfer/deliver → retire/cancel or sell), and an evidence trail (registry references, retirement records, certificates) that makes each credit's provenance and use defensible. Around that core, mature products add project catalogs, quality vetting, procurement machinery, delivery-risk protections, reporting, dashboards, and human expertise. The market splits into buyer-side portfolio management (Patch, Carbon Direct, Watershed Marketplace) and supplier-side credit commerce (Cloverly Catalyst), with some products covering both. The Type is distinct from Carbon Accounting (measures own emissions), Carbon Trading (market execution), REC Management (different instrument), and ESG Reporting (consumes the data).
