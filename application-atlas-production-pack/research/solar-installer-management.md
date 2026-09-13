# Research Notes — Solar Installer Management

## Research Goal

Understand what a Solar Installer Management application actually is, from real products: what objects exist inside it, what users do with them, how a solar installation project flows from first contact to permission-to-operate, which structures are solar-specific rather than generic field-service or CRM machinery, and where the Type's boundaries sit against the processed §29 trade-business siblings (Roofing, Plumbing, Restoration), the unprocessed siblings (Small Business Field Service Management, Home Improvement Contractor Management), and the energy-domain neighbor Solar Asset Management (§19).

## Initial Boundary

Hypothesis before research: solar installation sits at the intersection of several neighbors —

- the **field-service family spine** (customer + site → job lifecycle → field execution → billing) shared by the §29 trade leaves;
- the **sale-driven project shape** of Roofing Contractor Management (lead → proposal → signed contract → production → payment);
- a **technical definition of the work** analogous to roofing's measured roof — for solar, the candidate is the *designed PV system* (array layout, equipment, production estimate);
- a **regulatory approval path** (permitting with the authority having jurisdiction + utility interconnection / permission-to-operate) that roofing's pass did not observe as a structure;
- **financing-embedded selling** (loans, leases, PPAs / third-party ownership) that is much deeper in solar than in the sibling trades;
- the **seat seam** with Solar Asset Management (§19): the installer builds and hands over the system; the asset owner/operator then runs it.

Open question: is solar a trade-tuned variant of the generic business-management spine (like plumbing), or does it carry structurally distinct objects (like roofing's measured roof and restoration's loss-driven job)?

## Research Questions

1. What is the unit of record — project, deal, job? What lifecycle does it carry, and what is its terminal event?
2. How does system design enter the product — is the designed system (array layout, equipment, production estimate) a first-class object that drives proposals and procurement?
3. How do permitting and utility interconnection (permission-to-operate) appear — as tracked project states, generated documents, or external services?
4. How does financing work (cash, loan, lease/PPA), and is it definitional or common?
5. How is installation executed and tracked — milestones, tasks, schedules, crews?
6. How does money resolve — contracts, deposits, lender payouts, incentives?
7. What happens after install — monitoring handoff, O&M — and is it part of this Type?
8. Do generic business/FSM tools serve solar installers, and does the market maintain a dedicated solar software ecosystem?
9. Historical check: would a paper-era solar installer's system satisfy the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy | Tier / market | Evidence reached |
|---|---|---|---|
| **Aurora Solar** | design-led platform (sell, design, finance, deliver) | residential + commercial (HelioScope); large installer base | Tier 2 (root, for-installers, plan-sets pages) + Tier 1 (help-center category structure) |
| **OpenSolar** | free all-in-one (leads → design → sell → manage), global SMB | 28,000+ pros, 185+ countries, Australia-origin | Tier 2 (root, project-management-crm, permitting, auto-design pages); help center timed out ×2 |
| **Solargraf** | design + proposal + permitting all-in-one with done-for-you services | residential + C&I; 1,000+ customers | Tier 2 (root, solar-permitting pages) |
| **Enerflo** | ops/OS-led ("operating system for residential solar"), integration-first | US residential; sales orgs, installers/EPCs, financiers | Tier 2 (root page incl. full feature/capability sections) |

Rejected/considered: Sunbase (solar CRM; root returned empty, alternate domain transport error — abandoned per retry rule), Jobber solar industry page (403, consistent with multiple prior passes — trade-agnostic pole not directly evidenced), HelioScope (now Aurora's commercial product; covered under Aurora), ServiceTitan (no solar industry page observed in fetched surfaces).

## Sources

All fetched 2026-09-09:

- Aurora Solar — https://www.aurorasolar.com/ (root; product nav, positioning, testimonials) — Tier 2
- Aurora Solar — https://aurorasolar.com/aurora-for-installers/ (installer page: lead-to-install, AHJ database, dealer accounts) — Tier 2
- Aurora Solar — https://aurorasolar.com/plan-sets/ (Plan Sets Service: AHJ approvals, intake forms, engineering stamps) — Tier 2
- Aurora Solar Help Center — https://help.aurorasolar.com/hc/en-us (category structure: Design, Proposals & Documents, Pricing and Financing incl. Incentives, Utility Rates, Storage, Heat Pumps, Plan Sets, Integrations) — Tier 1
- OpenSolar — https://www.opensolar.com/ (root; product nav: Leads/Design/Sell/Manage/Add-ons) — Tier 2
- OpenSolar — https://www.opensolar.com/project-management-crm/ (projects, workflows/stages, actions, calendar, documents) — Tier 2
- OpenSolar — https://www.opensolar.com/permitting/ (permitting integrations: plan sets, PE stamps, permit applications, interconnection, PTO) — Tier 2
- OpenSolar — https://www.opensolar.com/auto-design/ (auto design, shading analysis, BOM generation) — Tier 2
- OpenSolar Help Center — https://support.opensolar.com/hc/en-us — **unreachable** (timeout ×2; abandoned)
- Solargraf — https://solargraf.com/ (root; design/proposal/permitting pillars, audiences, services) — Tier 2
- Solargraf — https://www.solargraf.com/solar-permitting (AHJ database, SLD generation, permit packages, PE stamps) — Tier 2
- Enerflo — https://enerflo.io/ (root; full OS feature sections: sales process, design integrations, financing, contracting, portals, install tracker, reporting) — Tier 2
- Jobber — https://www.getjobber.com/industries/solar-installation-software/ — **403** (abandoned; consistent with prior passes)
- Sunbase — https://www.sunbase.com/ (empty response), https://sunbase.co/ (transport error) — **abandoned**

## Product A — Aurora Solar (design-led platform)

### Key observations (Tier 2 + Tier 1 category structure)

- Self-positioning: "One platform to **sell, design, finance, and deliver** solar and storage with speed, accuracy, and trust." Product nav splits **Sell** (Sales Mode, Aurora AI, Integrated Financing, Contract Manager) and **Deliver** (Design Mode, Expert Design Services, Plan Sets Service).
- For Installers page: "From **lead to install**, Aurora's end-to-end platform empowers every team"; "solutions for **lead generation, design, and installation** — all in one place — to **prevent change orders at their source**"; "Remote site assessment, LIDAR-based shade analysis, and AI-assisted 3D modeling"; "Aurora's proprietary **AHJ database** and on-demand **Plan Sets Service** let you sell, design, and obtain **AHJ-ready plan sets — including PE stamps** — all within a single platform."
- Dealer/channel: "Bring **dealers** onto the same Aurora account… custom settings for each partner, such as branding, pricing, and equipment" (installer-dealer relationships, channel partners).
- Plan Sets page: "95% first time AHJ approvals"; "collect **site visit information** and request a plan set all within the same platform"; "our team will ensure the project's **AHJ is identified and its prerequisites for approval met** on every plan set"; site-data intake form "**information from your design automatically populates** the intake form"; photo uploads; "post-sales processes."
- Aurora AI: "An address and one month's utility bill are all you need to instantly generate a 3D home solar design."
- Help-center categories (Tier 1 structure): Design (SmartRoof, LIDAR Assisted Modeling, PV System Design and Performance Simulations); Proposals & Documents (Sales Mode); **Pricing and Financing** (Pricing, Custom Financing, Financing Integrations, **Incentives**, Financial Analysis); **Utility Rates & Energy Consumption**; **Storage**; **Heat Pumps**; **Plan Sets**; Integrations.
- Testimonial evidence of the design→install handoff: "build-ready projects to your operations team"; "fewer change orders and smoother handoffs"; "no issues with the AHJ"; "we don't have to take Suneye readings anymore" (legacy shade-measurement device).

## Product B — OpenSolar (free all-in-one, global SMB)

### Key observations (Tier 2 product pages)

- Product nav: **Leads** (PROfile, AI Lead Gen), **Design** (Auto Design, Mounting Designer, Single Line Diagrams), **Sell** (Sales Machine Proposal, CashFlow, Integrated Finance, E-signature), **Manage** (Shop & Bill of Materials, Supplier Assist, Expo, **Project Management CRM**, **Permitting Integrations**, Teams/roles & permissions), Add-ons (Enterprise Services, API, Imagery Marketplace).
- Project Management CRM: "Manage customers and solar projects **from pre-sale through installation**." Projects hold "customer details, workflow stages, actions, notes, documents, and project activity"; table or **Kanban** views (screenshot stages: "Lead," "Design," "Selling"); **custom workflows and stages**; **action management** (assign, due dates, Activity Center, auto-assign by project role); **calendar and scheduling** ("site visits, installs, maintenance"; Google Calendar/Outlook sync); documents (upload/merge/send; "Owner's Manual" per testimonial).
- Permitting Integrations (US): "connect US Pros with **permitting and engineering partners**"; services include "**plan sets, engineering reviews, structural and electrical PE stamps, permit applications, interconnection, and Permission to Operate support**"; request starts from the project ("The system must be **marked as sold** and the project address must be complete"); OpenSolar **prefills project information** and passes it to the partner; partners include SolarAPP+ (automated permitting) and GreenLancer with their own connected workflows; coverage spans "residential, commercial, utility-scale, and EV charging projects."
- Auto Design: "build-ready designs… in seconds"; "Pitch, azimuth and shading calculated automatically"; "**Auto designs automatically generate a bill of materials** for every project"; "Auto designs feed directly into the… customer proposal"; shading analysis "down to the sub-string"; performance engine "based on the trusted System Advisor Model"; multi-panel systems (different panel models per array).
- Root: customer-facing pole ("Find qualified solar professionals near you" — a marketplace-style surface attached to the pro software); 28,000+ pros; 185+ countries; free of charge; blog evidence of Australian incentive machinery (STC claims via an integration) and New Zealand connection requirements.

## Product C — Solargraf (design + proposal + permitting all-in-one with services)

### Key observations (Tier 2)

- Self-positioning: "All-in-one platform for **solar design, proposal, permitting**." "Easy designs. Interactive proposals. Automated permits."
- Audiences: business leaders, contractors, sales team, **operations team** ("Manage multiple projects, control user access, integrate with CRM, and optimize operations"), solar designers.
- Pillars: AI-powered solar design ("From roof to battery"); smart proposals and financing; **automated permitting** ("auto-generating permit packages that meet local compliance standards"); seamless integration ("From fintech to CRM"); simplified user control (roles and permissions).
- Permitting page: "Transform proposals into **AHJ-compliant permits**"; 1M+ permits; 97% AHJ acceptance rate; **auto stringing**; **SLD generation** ("solar and storage systems… whole-home, partial-home backup, grid-tied options, busbar PCS mode"); **electrical validation** before submission; "**preloaded jurisdictional guidelines**"; "**20,000+ AHJs with 200+ data points per AHJ** on electrical and structural details"; customizable permit packages (PDF and DWG; homeowner authorization, compliance letters, roof/array dimensions, stringing layouts, wall elevation, contractor signature); **Permit services** (done-for-you plan sets) and **PE stamps** (certified reviews); "self-service permitting."
- Financing: "Propel and TPO financing"; testimonial: "leading TPO providers built right into the platform… finance-ready proposals."
- Residential + Commercial ("Manage residential and C&I from one platform"); 16 languages.

## Product D — Enerflo (ops/OS-led, integration-first)

### Key observations (Tier 2)

- Self-positioning: "The operating system (OS) for residential solar — connecting your solar CRM, design tools, solar financing, contracting, and project management into one infrastructure layer. **From first knock to Permission to Operate (PTO). One system. One flow.**"
- FAQ topic list includes "What is '**lead to PTO**' in residential solar?" — the industry's own lifecycle phrase.
- Sales process (front end): "Leads & Deals Pipeline, Scheduling, QuickQuote, Virtual Sales Rep (VSR), Solar Design & Proposal, Battery Sizing Tool, **Title Checks, Soft Pulls**, Solar Financing (Loan, TPO, Escrow), Solar Contracting with Solar Signing Packets in Seconds, **Complete Project Handoff**, Project Status Transparency."
- Integrated Solar Design: design executed in integrated tools — "Aurora Solar, Scanifly, Aerialytic, Solargraf, Solo, **Manual Designs**" — "Reps can create complete, customer-ready proposals without switching tools."
- Integrated Solar Financing (Lendflo): "Competitive Loan Products…; **Third Party Owned (TPO) — Lease & PPA** for Solar & Storage; TPO Battery Backup; **Escrow for Cash Deals**"; "deals are routed across lenders."
- Solar Contracting (Docflo): "Generate complete, compliant solar contract packages… Automatically compile all required documents into one signing packet… e-signatures" (email + in-person).
- Solar Customer Portals: "Dedicated Portal for Every Customer (No login required); **Install Tracker with Real-Time Status**; centralize project details & documentation."
- **Solar Install Tracker (backend)**: "Manage solar projects **from contract to PTO**… configurable **milestones**, task management, and automated communications"; "Integrated **Change Orders**."
- Reporting & Analytics powered by Domo; 150+ integrations; "$16B+ Solar Transactions Processed"; "62% Faster Install Timelines"; US-only (all 50 states + Puerto Rico); serves financiers too (Solar Financing OS: originate loans/leases/PPAs).
- Infrastructure framing: "Companies cobbled together a CRM, a design tool, a finance portal, a spreadsheet… Enerflo is the infrastructure layer" — indirect evidence that the market's baseline is fragmented generic tooling.

## Cross-product Comparison

| Structure / capability | Aurora | OpenSolar | Solargraf | Enerflo | Layer |
|---|---|---|---|---|---|
| Customer + project of record bound to the site | ✅ designs/proposals per customer site; "every stage of the project cycle" | ✅ projects "from pre-sale through installation" | ✅ projects managed by operations team | ✅ deals → projects; "complete project handoff" | A×4 |
| Sales pipeline (leads/deals, stages, kanban) | ✅ Sales Mode guided workflows; lead generation | ✅ kanban stages Lead/Design/Selling; custom workflows | ✅ sales team pillar; proposal editing | ✅ Leads & Deals Pipeline | A×4 |
| **Designed system as the project's content basis** | ✅ Design Mode 3D CAD; LIDAR shade; performance simulation; design populates plan-set intake | ✅ Auto Design → BOM → proposal; shading to sub-string; SAM-based engine | ✅ AI design "from roof to battery"; shading/setbacks → yields | ✅ integrated design tools (Aurora/Scanifly/Solargraf/Solo) + Manual Designs; battery sizing | A×4 |
| Proposal with production/savings presentation | ✅ "permit-quality accuracy… just an address and an electric bill"; utility-bill comparison | ✅ Sales Machine proposal fed by auto design; CashFlow | ✅ interactive proposals; savings insights | ✅ customer-ready proposals; QuickQuote | A×4 |
| **External-approval path: permitting (AHJ)** | ✅ proprietary AHJ database; Plan Sets Service; PE stamps; intake forms | ✅ Permitting Integrations: plan sets, PE stamps, permit applications | ✅ automated permitting; 20k+ AHJ database; SLDs; permit packages; permit services | ✅ contract→PTO milestones (permitting inside the tracked path) | A×4 |
| **External-approval path: interconnection / PTO** | (post-plan-set; AHJ focus on fetched pages) | ✅ "interconnection, and Permission to Operate support" | (permit focus on fetched pages) | ✅ "from contract to PTO"; "lead to PTO" | A×2 (+implied ×2) |
| **Financing embedded in the sale** | ✅ Integrated Financing; financing integrations; Incentives category | ✅ Integrated Finance; CashFlow | ✅ TPO/Propel financing; finance-ready proposals | ✅ Lendflo: loans, TPO lease/PPA, escrow; lender routing; title checks/soft pulls | A×4 |
| Contract execution | ✅ Contract Manager | ✅ E-signature | ✅ proposals → contracts (contractor signature pages) | ✅ Docflo signing packets, e-sign | A×4 |
| **Installation execution tracked on the project** | ✅ "lead to install… all in one place"; change-order prevention | ✅ schedule "site visits, installs"; actions; calendar | ✅ "fast-track installs"; operations team; "on time and on budget" | ✅ Install Tracker: contract→PTO, milestones, tasks, change orders | A×4 (depth varies) |
| Bill of materials / equipment purchasing | (equipment in design; not fetched as purchasing) | ✅ Shop & BOM; Supplier Assist; Expo | (equipment in design/permit package) | (via integrations) | A×1 (BOM generation A×2: OpenSolar explicit, Aurora intake) |
| Customer portal / customer-facing surfaces | ✅ Solar for Homeowners (quote site) | ✅ customer quote flow; proposal sharing | ✅ interactive proposals for clients | ✅ dedicated no-login portal, real-time install status | A×4 |
| Lead capture machinery | ✅ Aurora AI (address + bill → 3D design); Lead Capture AI | ✅ AI Lead Gen; PROfile | ✅ agentic AI ("create projects with just a command") | ✅ VSR (white-labeled lead capture, instant quotes) | A×4 |
| Storage / battery | ✅ Storage category; "sell more storage" | ✅ battery in design/SLDs | ✅ storage SLDs; "from roof to battery" | ✅ Battery Sizing Tool; TPO battery | A×4 |
| Incentives machinery | ✅ Incentives help-center category | ✅ STC-claims integration (AU blog) | (not fetched) | (not fetched) | A×2 |
| Change orders | ✅ "prevent change orders at their source"; "fewer change orders" testimonial | (not fetched) | ✅ "reduce proposal revisions" | ✅ Integrated Change Orders | A×3 |
| Roles / permissions | ✅ account configurations; dealer settings | ✅ Teams (roles and permissions) | ✅ roles and permissions | (not fetched) | A×3 |
| Reporting / analytics | (not fetched) | (not fetched) | (not fetched) | ✅ Domo-powered reporting | A×1 |
| Dealer / channel networks | ✅ dealers on same account; channel managers | ✅ Partner program; Expo marketplace | (not fetched) | ✅ network (financiers, installers, sales orgs, distributors) | A×3 |
| Commercial / C&I | ✅ HelioScope (commercial) | ✅ commercial systems; commercial/utility-scale/EV-charging permitting | ✅ residential + C&I from one platform | (residential focus) | A×3 |
| Post-install monitoring / O&M | not observed | not observed | not observed | not observed (ends at PTO) | — (uncertainty) |
| Crew/subcontractor management (roofing-style) | not observed as named structure | ✅ teams, assignment, schedules | (operations team) | (network installers; tasks) | A×1–2 (thin) |
| Job costing / invoicing detail | (not fetched) | (CashFlow observed; invoicing not fetched) | (not fetched) | ✅ escrow, transactions processed | A×1–2 (thin) |

## Canonical Model

### L0 — Defining Invariant (deliberately small)

The solar installation company's project system of record, whose defining core is **five jointly-held structures**:

1. **The solar project of record** — a persistent identified project binding a customer to the installation site, carried from first contact (lead) through the lifecycle to its terminal event, permission-to-operate. Remove → a contact list, or a design/proposal tool with no project memory.
2. **The site's system design as the project's content basis** — the project's equipment and price content derives from a system design for the specific site: array layout on the roof or ground, equipment selection (panels, inverters, batteries), and a production estimate (shading/irradiance analysis, expected output, utility-bill offset). The design feeds the proposal's promise and the bill of materials. Realizations vary: in-product design engines, integrated third-party design tools, done-for-you design services, or manual entry. Remove → a generic pipeline with hand-typed quotes, or a bare design tool with no project.
3. **The external-approval path** — the project carries a tracked path through the approvals that legally gate construction and operation: the construction permit with the authority having jurisdiction (plan sets, engineering stamps, permit applications) and the grid-connection approval with the utility (interconnection, permission-to-operate). Approval documents are generated in-product or procured from permitting/engineering partners; approval states are tracked on the project. Remove → sales/design software that stops at the contract; the job cannot legally be built or turned on.
4. **Installation execution** — the sold project converts into scheduled, tracked installation work (milestones, tasks, site visits, install events, crews/teams) carried through to completion. Remove → a sales/design/permitting pipeline with no build.
5. **The project's commercial resolution** — the project carries its contract (executed via signing packets/e-signature) and its money path: customer payment and/or a financing arrangement (cash, loan, lease/PPA), with pricing carried on the project. Remove → quoting with no money, or contracting tools disconnected from any project.

Jointly-held is load-bearing:

- 1 alone = CRM/project list; 2 without 1 = a design tool; 3 without 1+2 = a permitting service bureau (the permitting partners are exactly this); 4 without 1 = crew scheduling; 5 without 1 = a contracting/e-sign tool.
- 1+2 without 3+4+5 = solar design & sales software (the design-led pole's base layer).
- 1+5 without 2+3+4 = generic CRM with contracts.
- 2+3 without 1+4+5 = design + permitting service bureau.
- 1+3+4+5 without 2 = a generic project tracker with permit tasks (the trade-agnostic pole).
- 1+2+3 without 4+5 = sellable, permittable, but never built or paid.

### L1 — Common Mature Structure (standard capabilities; 3–4/4 observed)

- Sales pipeline with customizable stages/kanban and lead-source tracking.
- Proposals that present the design's outcome: production, savings, utility-bill offset, cash flow.
- Financing integrations at solar depth: loans, third-party ownership (lease/PPA), escrow for cash; lender routing; credit soft pulls/title checks at the ops pole.
- Contract generation and e-signature (signing packets compiling required documents).
- Customer-facing surfaces: interactive proposals, quote flows, customer portals with real-time install status.
- Lead-capture machinery: instant-estimate/AI lead capture, white-labeled quote funnels.
- Storage/battery as a first-class extension of the same design→sell→install flow.
- Bill-of-materials generation from the design; equipment catalogs and supplier purchasing at some products.
- Incentives/rebate machinery (tax credits, regional incentive schemes) inside pricing.
- Change orders when the as-built diverges from the as-sold.
- Roles/permissions; calendars/scheduling; reporting/analytics; CRM/accounting integrations; APIs.
- Dealer/channel-network machinery (dealers on shared accounts, partner settings, marketplaces).

### L2 — Variant / Optional Structure

- Segment: residential-dominant; commercial/C&I at several products (different design tools, permitting coverage); utility-scale appears only as permitting-partner coverage.
- Regulatory regime: US AHJ + utility vocabulary vs Australian/NZ connection and incentive schemes vs European regimes — the approval path is the invariant, the vocabulary is regional.
- Ownership model: customer-owned (cash/loan) vs third-party-owned (lease/PPA) — changes who the contracting counterparty is, not the project structure.
- Design realization: in-product engine vs integrated tool vs done-for-you service vs manual entry.
- Permitting realization: in-product generation with AHJ databases vs partner services vs automated permitting (SolarAPP+).
- Post-install monitoring handoff to the customer/asset owner — suspected, not directly observed (uncertainty).
- Adjacent electrification surfaces: heat pumps, EV charging — era-current expansions at some products.
- Customer-marketplace surfaces attached to pro software (find-an-installer directories).

### L3 — Vendor-specific (Research Notes only)

- Aurora: Sales Mode/Design Mode naming; Aurora AI; Contract Manager; Expert Design Services; Plan Sets Service (95% first-time AHJ approval, 24–48h turnaround claims); LIDAR modeling; irradiance engine; HelioScope (commercial); dealer accounts; NRG/Semper Solaris-class customer logos.
- OpenSolar: free-software model ("100% free of charge"); Ada auto design (beta); Sales Machine proposal; CashFlow; Shop/Expo/Supplier Assist; PROfile; Imagery Marketplace; SAM-based performance engine; 28,000+ pros / 185+ countries; 1% commitment program; Australian STC integration (Bridge Select).
- Solargraf: Sol AI assistant; 20,000+ AHJs with 200+ data points; 97% AHJ acceptance; 1M+ permits; 3M+ proposals; auto stringing; SLD generation modes (whole-home/partial backup, grid-tied, busbar PCS); Propel/TPO financing; permit services + PE stamps; 16 languages; DWG export.
- Enerflo: OS positioning and "infrastructure layer" framing; Lendflo (financing), Docflo (contracting), VSR (virtual sales rep), Install Tracker names; Domo-powered analytics; $16B+ transactions / 62% faster install claims; US-only availability; Solar Financing OS for lenders; SOC 2 posture.

## Vendor-specific Findings

See L3. Packaging observation: the four sampled products represent four philosophies — design-led (Aurora), free-all-in-one (OpenSolar), permitting-led-with-services (Solargraf), ops/OS-integration-led (Enerflo) — yet all four organize the same project arc (lead → design → proposal → contract → approval → install → PTO). The market is a **dedicated solar software ecosystem**, not a configuration of a horizontal FSM vendor: no horizontal trades platform appeared in the fetched surfaces serving solar with a dedicated solar configuration (contrast roofing, where ServiceTitan ships one). Enerflo's own infrastructure framing documents that the market baseline is fragmented generic tooling (CRM + design tool + finance portal + spreadsheet), which is the trade-agnostic pole's real-world form.

## Boundary Findings

1. **vs Small Business Field Service Management (§29 sibling, unprocessed)** — structural sibling-with-additions, NOT a pure trade-tuned variant. The shared spine (customer + site → job → execution → money) is identical, but 4/4 sampled products carry two structures the generic spine lacks: the designed-system content basis and the external-approval path (permit + interconnection/PTO) as tracked project state; and the money leg is financing-dominated (loans/TPO) rather than visit-billing. The trade-agnostic pole (generic CRM/FSM + spreadsheet + point tools) is documented indirectly by Enerflo's own before-state framing. Seam: remove the designed-system basis + the approval path + financing depth → generic business management. Jobber's solar page was unreachable (403), so the generic pole is not directly evidenced — joint review recommended when the FSM leaf is processed, consistent with the roofing/restoration flags.
2. **vs Roofing Contractor Management (§29, processed)** — closest structural sibling in the sale-driven production family. Both: sale-driven job of record, a trade-specific technical definition of the work (measured roof vs designed system), execution behind the sale, money resolved on the job. Seams: solar's content basis is a *designed engineered system with a production promise* (layout + equipment + simulated output), not measured quantities of an existing surface; solar's external-approval path is definitional (permit + interconnection/PTO as tracked project state with generated/procured plan sets), while roofing's pass observed no permit machinery at all; solar's terminal event is permission-to-operate (the system turned on), roofing's is final payment/closeout; solar's money is financing-dominated, roofing's retail/insurance-dominated. Keep-separate; both pass the "remove the trade's technical definition and approval/money shape → the other trade" test.
3. **vs Solar Asset Management (§19, unprocessed)** — the seat seam. This Type is the *installer's* business system: it ends when the system is built, approved, and handed over (PTO). Solar Asset Management is the *asset owner/operator's* system: production monitoring, performance, O&M of the operating asset. The PTO/handoff moment is the seam. Post-install monitoring was not observed in any fetched installer-software surface — consistent with the seam, but recorded as an uncertainty rather than a claim.
4. **vs Home Improvement Contractor Management (§29, unprocessed)** — solar is a trade-specific instantiation of the sale-driven home-improvement shape (lead → proposal → contract → production), but carries structural additions (designed-system basis, approval path, financing depth) analogous to roofing's. Expected keep-separate; forward note for that pass.
5. **vs CRM** — the front half only (leads, pipeline, proposals); the Type is defined by design, approvals, execution, and money behind the sale.
6. **vs Construction Project Management (§17)** — the commercial/C&I pole drifts toward project machinery, but the sampled center is the installer's own business system, not multi-organization contractual coordination.
7. **vs Permit Management (§24) / Environmental Permit Management (§21)** — different seat: those are authority/organization-side permit-office systems; here the permit is one approval state on the installer's project, with the application generated/procured, not adjudicated.
8. **Standalone solar design tools (HelioScope-class) and permitting service bureaus (the permitting partners)** — capability suppliers below the Type: design without the project system; permitting without the project. Both integrate INTO this Type (documented at OpenSolar, Aurora, Enerflo).
9. **vs Local Service Marketplace** — demand-side discovery vs operator-side execution; OpenSolar's consumer "find solar pros" surface is a marketplace-style acquisition layer attached to the pro software, not the Type's center.
10. **vs Electrical Service Management (§29 trade sibling)** — solar installers are often electrical contractors, but this Type's center is the sale→design→approve→install→PTO project arc, not dispatched electrical service visits; the two share the family spine only.

## Historical / Market-Sample Check (§24)

Paper-era solar installer (2000s-era residential boom, and earlier early-adopter installs): customer card file; site visit with tape measure and a shade-measurement device (the SunEye generation — named in Aurora's own testimonial as the displaced legacy); hand-drawn array layout on a roof photo; production estimate from rules of thumb or a spreadsheet; printed proposal; signed contract; paper permit application filed at the building department; interconnection application mailed to the utility; crew calendar on the wall; invoice and payment record; rebate/incentive paperwork. **All five L0 legs are satisfied with zero modern machinery** — no design engines, no AHJ databases, no e-signature, no lender APIs. Regional check: Australian and European installers satisfy the same five legs with their own approval vocabulary (grid-connection applications, incentive accreditation) — the approval path is the invariant, "AHJ/PTO" is the US realization. The design engine, the AHJ database, the lender integration, and the milestone tracker are dominant modern realizations, not the definition.

## Uncertainties

1. **Post-install monitoring/O&M handoff** — suspected (the system must be monitored by someone after PTO) but **not observed in any fetched source**; not claimed; the seam with Solar Asset Management (§19) is drawn at the PTO terminal event.
2. **Crew/subcontractor management depth** — OpenSolar documents teams/assignment/scheduling; roofing-style subcontractor-as-contact patterns were not observed in fetched solar sources; depth unverified.
3. **Equipment procurement depth** — OpenSolar documents Shop/BOM/Supplier Assist; distributor-direct ordering with status sync (roofing-style) was not observed; depth unverified.
4. **Incentive machinery detail** — Aurora's Incentives category and OpenSolar's Australian STC integration observed by name only; mechanics not fetched.
5. **Invoicing/job-costing detail** — thinner than the roofing sample; Enerflo's escrow/transaction processing observed; explicit invoice objects not fetched.
6. **Trade-agnostic pole** — Jobber's solar page 403; no generic-FSM solar configuration directly evidenced; argued structurally and via Enerflo's before-state framing only.
7. **Non-US operational detail** — OpenSolar (185+ countries, AU origin), Aurora (EU sites), Solargraf (16 languages) evidence global reach, but non-US approval-regime mechanics were not fetched; the approval-path abstraction is held at conceptual strength.
8. **Sunbase** — unreachable (empty response + transport error); dropped from the sample; no claims made.
9. **Interconnection/PTO depth at Aurora and Solargraf** — their fetched pages emphasize the permitting leg; interconnection machinery is directly evidenced only at OpenSolar and Enerflo; held as A×2 with implication at the others.

## Final Synthesis

Solar Installer Management is the solar installation company's project system of record. It shares the §29 trade-family spine (customer + site → job → execution → money) but is structurally distinct in three ways. First, the job's content basis is a **designed engineered system**: the array layout, equipment selection, and production estimate for the specific site feed the proposal's promise and the bill of materials — the solar analog of roofing's measured roof, but a design rather than a measurement. Second, the project carries an **external-approval path** as tracked state: construction permitting with the jurisdiction (plan sets, engineering stamps — generated in-product or procured from permitting partners) and grid interconnection with the utility, ending in permission-to-operate — the industry's own terminal event ("lead to PTO"). Third, the money leg is **financing-dominated**: cash, loans, and third-party ownership (lease/PPA) are embedded in the proposal and contract machinery, not bolted on. Around these, mature products add the expected family capabilities — pipelines, proposals, portals, lead capture, storage sales, roles, reporting — and the market maintains a dedicated solar software ecosystem (design-led, free-all-in-one, permitting-led, and ops/OS-led philosophies) rather than a configuration of a horizontal field-service vendor. The historical paper-era installer — card file, shade tool, hand-drawn layout, paper permit and interconnection applications, crew calendar — satisfies all five defining legs without any modern machinery, confirming the abstraction sits above the current market's dominant implementation.
