# Research Notes — Wastewater Utility Management

## Research Goal

Understand what "Wastewater Utility Management" is as an Application Type: what system (or assembled family of systems) a wastewater utility — a sewer authority, clean-water utility, sanitation district, or the sewer/wastewater line of a municipal utility — runs to manage its service business; what objects live inside it; what work flows through it; who uses it; and where its boundaries lie against the already-processed horizontal utility family (billing, CIS, asset, field service, GIS), the processed §21 sibling (wastewater-compliance-management), the processed commodity vertical (gas-utility-management), and the unprocessed water siblings (water-utility-management, water-network-monitoring, water-quality-management).

## Initial Boundary

The leaf sits in DIRECTORY §19 (Energy, Utilities & Telecommunications) between Water Utility Management and Gas Utility Management. Neighbors:

- Horizontal §19 family (all processed): utility-billing-platform, utility-customer-information-system-cis, utility-asset-management, utility-field-service-management, utility-gis, utility-rate-management, utility-revenue-assurance, AMI, MDMS.
- Commodity verticals: gas-utility-management (processed 2026-09-08 — defined as the gas utility's customer-service business system of record; the utility-billing pass RATIFIED this "vertical-edition framing" and recorded a forward note that water-utility-management is expected to follow the same pattern).
- §21 siblings: wastewater-compliance-management (processed 2026-09-10 — the regulated discharger's discharge-compliance system), water-quality-management, environmental-water-monitoring.
- Unprocessed §19 siblings: water-utility-management, water-network-monitoring.

Prior flags inherited from wastewater-compliance-management (§21):
1. Seam: "utility business/operations center vs discharge-compliance center; WIMS-class products blur the seam by managing plant operations data alongside compliance."
2. "The pretreatment control-authority program (Linko/Locus-IPP pole — a utility-run regulatory program over industrial users: IU permits, inspections, sampling, violation/SNC tracking, enforcement reporting) is structurally closer to government inspection/permitting over external parties — recommend joint review when that leaf is processed."

## Research Questions

1. What does a wastewater utility actually operate and sell? (collection system, treatment works, connected premises, charges)
2. What software does the market sell under the "wastewater utility management" label, and what does each product actually hold?
3. Is the market label ONE coherent Application Type or an umbrella over several software families?
4. Does the ratified commodity-vertical pattern (gas = customer-service business system of record) hold for wastewater, or does wastewater's structure differ (connection-based service, derived charge basis)?
5. How does sewer billing work — metered, derived from water consumption, flat-rated, assessed?
6. Where do the collection system, treatment-plant data, discharge compliance, and the pretreatment program sit relative to this Type?
7. Would older / regional / differently-positioned products still fit the definition?

## Representative Products

Sampled across the poles the market label covers (5 poles, different tiers and product philosophies):

| Product | Pole | Tier | Evidence |
|---|---|---|---|
| Muni-Link | utility billing / CIS for water + wastewater | small/municipal (North America) | official site fetched (home, CIS, billing, water, product pages) |
| OpenGov (Utility Billing + Wastewater Collection) | billing pole AND collection-asset pole, one vendor | municipal | official pages via search snippets (direct fetch 403) |
| Black Mountain Software — Utility Billing | billing/CIS | small municipal/district | official page via search snippet |
| Minol USA — Municipal Sewer Billing | turnkey billing service | municipal, any size | official page via search snippet |
| iWorQ — Sewer Management | collection-system asset/maintenance | small municipal | official page fetched |
| Hach WIMS (Aquatic Informatics) | plant operations data + compliance reporting | mid/large enterprise | official pages + San Diego sole-source doc + Gwinnett County catalog |
| Linko (Aquatic Informatics) | pretreatment / FOG / hauled-waste program | control authorities | official product page + TPO/WaterWorld case studies |
| Sedaru | collection-system field operations | mid-tier | UNREACHABLE (2 fetch failures) — Tier-3 only (Palo Alto staff report, press) |

Tier-3 corroboration: BWSC/Itineris UMAX case (Wastewater Digest), Mount Pleasant Waterworks billing case (Wastewater Digest), SAP Best Practices for Water Utilities (2005, Wastewater Digest), City of Fargo Industrial User Permit application, G2 "Wastewater Pipeline Inspection" category note.

## Sources

- Muni-Link: https://muni-link.com/ , https://muni-link.com/features/customer-information-system/ , https://muni-link.com/features/billing/ , https://muni-link.com/water , http://muni-link.com/products/utility-billing-software (fetched 2026-09-10)
- OpenGov: https://opengov.com/products/utility-billing (403 on direct fetch; content via search snippet), https://opengov.com/products/asset-management/wastewater-collection (search snippet)
- Black Mountain Software: https://blackmountainsoftware.com/utility-billing (search snippet)
- Minol USA: https://minolusa.com/municipal-sewer-billing-services (search snippet)
- iWorQ: https://iworq.com/systems/sewer-management-software (fetched 2026-09-10)
- Hach WIMS: https://www.hach.com/digital-solutions/wims , https://sea.hach.com/digital-solutions/claros/solutions/data-management , https://sea.hach.com/p-hach-wims-water-information-management-solution/WM-MU , https://aquaticinformatics.com/products/hach-wims-water-information-management-solution-platform , WIMS brochure PDF (opssys.com), City of San Diego sole-source certification https://www.sandiego.gov/sites/default/files/58_ss_3939.pdf , Gwinnett County service catalog https://support.gwinnettcounty.com/TDClient/277/Portal/Requests/Service/10858/Hach-WIMS
- Linko: https://aquaticinformatics.com/products/fog-pretreatment-regulatory-software , TPO case https://www.tpomag.com/editorial/2021/05/marlboroughs-linko-software-automates-and-simplifies-data-on-permitted-industries-and-fog-haulers , WaterWorld case https://www.waterworld.com/drinking-water-treatment/potable-water-quality/article/14169157/cleaning-up-compliance , Tracxn profile
- Sedaru: https://www.sedaru.com/ and https://sedaru.com/ both failed (transport error, 2 attempts — abandoned per network rule). Tier-3: City of Palo Alto staff report https://www.paloalto.gov/files/assets/public/v/1/agendas-minutes-reports/reports/city-manager-reports-cmrs/year-archive/2020/id-11314-mini-packet-062220.pdf ; Wastewater Digest press https://www.wwdmag.com/utility-management/news/10931306/colorado-utility-selects-software-platform
- BWSC/Itineris: https://www.wwdmag.com/utility-management/article/11004078/updating-oldest-us-water-sewer-system-with-newest-software
- Mount Pleasant Waterworks: https://www.wwdmag.com/utility-management/article/33010188/new-billing-system-alleviates-bottlenecks-for-a-south-carolina-utility
- SAP: https://www.wwdmag.com/collection-systems/news/10909631/software-streamlines-water-utility-processes-for-more-efficient-implementation-and-faster-return-on
- Fargo IU permit: https://download.fargond.gov/0/industrial_user_permit_application.pdf
- G2 category: https://research.g2.com/insights/wastewater-pipeline-inspection

Research date: 2026-09-10.

## Product Observations

### Muni-Link (billing/CIS pole) — evidence layer A

- "Cloud-based utility billing software for water and wastewater utilities... manage customer accounts, billing, payments, service orders, and customer communications in one system." Customers: "municipal utilities, utility authorities, water districts, and regulated utilities."
- Modules: CIS (Account Central), Billing, Payments, Service Orders, Customer Portal, Customer Notifications, Integrations, Utility Websites.
- Account Central (CIS): one-screen account hub — "account details, usage history, service orders, and notifications"; "balances, transactions, and payment plans"; "usage and meter readings for water, sewer, and stormwater"; "service orders, past or present, associated with a customer account"; "logs, notes, and past interactions". Actions: update account with change log, create/dispatch service orders, set up payment plans, manage delinquency.
- Billing: "tiered and seasonal rates, sewer calculations, minimum charges, adjustments, notices, delinquency workflows, and reporting"; guided billing runs (readings → calculations → reports → billing → ebill notifications); "Generate or Import Meter Readings — automatically pull readings from your meter reading software or import them manually"; billing cycles "monthly, quarterly, or bi-monthly"; delinquency: "Generate shutoff service orders in bulk. System automatically cancels orders if a customer pays and creates orders to restore service when accounts are made current."
- Integrations: "integrating your asset management, accounting, GIS, and AMR/AMI systems with Muni-Link" — the estate lives in OTHER systems; Muni-Link is "both a Utility Billing solution and a full Customer Information System".
- Product page: "supports billing for water, sewer, refuse, and more"; modules list includes Backflow inspection manager, Loans, Stormwater; "built with input from water, sewer, and stormwater utilities" (design partners).
- Security: MFA, role-based user permissions.

### OpenGov (billing pole + collection-asset pole, one vendor) — evidence layer A (snippet-level; direct fetch 403)

- Utility Billing product: "bill water, sewer, trash, and other utilities from one connected system, with rates, meter data, and payments synced directly to your general ledger"; "rates, meter data, billing runs, service tasks, delinquencies, payments, account management, and reporting in one system"; work orders: "shut-offs, turn-ons, and re-reads go straight to field crews and results automatically come back"; rate structures: "tiered water rates, **flat sewer fees**, or seasonal trash pickups"; integrates with OpenGov Financials.
- Wastewater Collection (SEPARATE product): "Manage sewer systems, lift stations, and collection infrastructure. Reduce overflows, track inspections, and stay compliant. Built for wastewater utilities."
- Significance: one vendor ships the billing spine and the collection-estate management as two distinct products — the market itself splits the umbrella.

### Black Mountain Software — Utility Billing (billing pole) — evidence layer A (snippet)

- "Designed for municipalities and special districts like yours that bill for water, sewer, garbage and more." "Manage nearly any type of rate structure, billing cycle, and service." Service Orders module; cash receipting flowing to General Ledger; standalone or integrated.

### Minol USA (turnkey billing-service pole) — evidence layer A (snippet)

- "Turnkey municipal utility billing partner that provides both the billing software and the people and processes to run it — a full back-office operation for your city's sewer billing": bill generation & distribution, payment processing & collections, call center, delinquency management, "work order management — coordinate service events tied to billing", resident/staff portals, "AMI integration — works with your existing meters and AMI systems for accurate consumption data".
- "Minol bills the full range of municipal utilities — water, sewer, stormwater, recycling, and waste — on a single platform."
- Significance: the billing operation itself can be purchased as a service; the software spine is the same family.

### iWorQ — Sewer Management (collection-asset pole) — evidence layer A

- "Track locations and maintenance history for each asset, including lines, manholes, and outlets." Assets: "lateral lines, main lines, force lines, manholes, pumps."
- "Creates an inventory for all your conveyance and collection assets to ensure that inspections and maintenance are up to date." Maintenance history + associated costs per asset; schedule work and inspections; monitor asset conditions; labor hours; interactive GIS map (upload existing GIS data or manually plot); office/field mobile updates; reports on maintenance and costs; integrates with Work Management.
- Customer quote: "A resident with a sewer backup complaint will receive faster response" — service events (backups/complaints) drive work.
- Significance: NO billing. This is the public-works asset-management family (iWorQ also ships pavement, signs, stormwater, water system modules) deployed for the sewer estate. The wastewater-specific content: the asset classes (gravity mains, laterals, force mains, manholes, pumps/lift stations) and the inspection/cleaning/backup-response programs.

### Hach WIMS (plant operations data + compliance pole) — evidence layer A

- "Water Information Management System that replaces Excel, automates reporting"; "Combine field, process, lab, and other data for the complete picture."
- "WIMS gathers and consolidates data from across your water or wastewater system into one secure location": automatic interfaces to SCADA/Historians, LIMS, commercial lab data; manual entry forms; mobile data collection (Rio companion).
- Modules: LAB Cal (lab sample scheduling/tracking), JOB Cal (maintenance tracking/scheduling), BOD Manager (automated data entry/calculations from Hach probes).
- "Over 100 built-in industry-specific formulas"; "Pre-programmed EPA and state report templates create paper and electronic regulatory reports (SWTR, DBR, NPDES, DMR, eDMR, MOR, SDWA, CCR, etc)"; support for NetDMR, CIWQS, SDWIS, E2; user-defined alerts; dashboards; audit trails; defensible-records posture.
- City of San Diego sole-source doc: "WIMS is the management tool used for reporting data to the EPA, state, and other regulatory agencies"; interfaces to DCS and LIMS; used by the Wastewater Treatment and Disposal Division "to maintain compliance with State and Local regulatory agency requirements."
- Gwinnett County: "centralize water and wastewater plant data—from lab results, process instruments, field readings, and SCADA—so teams can analyze trends and generate regulatory and operational reports."
- Significance: serves water AND wastewater plants; the compliance half (limits, DMR-class reports) is the §21 wastewater-compliance-management Type's territory; the plant-data half is the utility's operational data layer. NO billing, NO collection-network assets, NO customer accounts.

### Linko (pretreatment/FOG pole) — evidence layer A (product page) + A- (case studies)

- "Software that provides wastewater pretreatment, fats, oils, and grease (FOG) & liquid hauled waste regulatory compliance. Over 400 customers."
- Modules: LinkoCTS (pretreatment compliance tracking: permit info management, monitoring concentration limits, permit renewals, waste sample tracking, compliance violation detection, EPA-guideline reporting); LinkoFOG (FSE inventory, trap inspection, job planning & scheduling, outreach tracking); LinkoHW (municipal hauled waste: hauler/truck details, disposal tracking); POM Portal (electronic pumpout manifests from establishments or haulers); on-site inspection recording.
- Marlborough case: industrial users "under more stringent regulations through the industrial pretreatment program under the Clean Water Act. Marlborough uses Linko to manage the permitting, sampling and compliance the act requires"; labs submit analytical data electronically; industrial users compile self-monitoring reports and submit online; automated violation notices; inspection/pumpout scheduling; permit renewals.
- SD1 case: LabSync (nightly LIMS→Linko transfer); Compliance Assistant ("determine compliance against rolling quarters and can identify significant non-compliance issues"); Permit Writer ("standardized permit templates... reissue all 55 industry permits at the same time"); "Violations can be issued and tracked along with an enforcement response plan"; state reports queried from the data.
- Significance: the utility here is the CONTROL AUTHORITY regulating external parties (industrial users, food service establishments, waste haulers). Objects: IU/FSE permits, inspections, samples, violations, enforcement responses, manifests. Structurally a regulatory program over external parties — NOT the utility's service business, NOT the utility's own discharge compliance.

### Sedaru (collection-ops pole) — UNREACHABLE; evidence layer C (Tier-3 only)

- Palo Alto staff report (procurement): contract for "Wastewater Collection System Management Software and Implementation" with Sedaru; replaces Redzone ICOM; used by "Utilities Wastewater Operations staff"; "prioritize, plan, schedule, and track Operations planned or unplanned maintenance work"; "linked to the GIS data... to periodically update the wastewater utility information"; "work in conjunction with Wastewater Operations' CCTV system to store images and reports of sewer main and lateral assessment"; mobile field data collection; scheduling hydro-flushing.
- Eagle River press: "real-time solution to connect organizational data, systems and people across the water enterprise... connect its Esri ArcGIS, Cityworks CMMS and hydraulic model in real-time with office and field staff."
- Significance: the collection-operations pole is field-work/GIS-connected operations software over the sewer estate — the horizontal asset/field family's territory with wastewater-specific programs (CCTV, cleaning, overflows). Held at Tier-3 strength only.

### Tier-3 corroboration (billing family serving water+sewer)

- BWSC (Boston Water and Sewer Commission — "the largest retail water and wastewater utility in New England... 1,435 miles of sewer pipe"): replaced its CIS with Itineris UMAX; "65,000 reads were received, 22,000 bills were created, and $11 million in payments were received" in the first week; "2,400 service orders within the first week"; account structure "supports multiple services on one account, such as master accounts, landlord accounts and consolidated billing."
- Mount Pleasant Waterworks (water AND wastewater utility): billing/payments modernization; AMI + portal notify customers of usage issues; paperless billing; self-service.
- SAP Best Practices for Water Utilities (2005): CIS for "small and midsize water and wastewater utilities": "call center management, meter-to-cash operations, integrated work management, customer financial management, consumption data collection, connections and device management and consumption billing"; "invoicing water and sewage and processing connections and disconnections."
- Fargo IU permit application: industrial users report "Total of all flows to the sanitary sewer gpd ☐ estimate ☐ metered" — IU flows may be metered; pretreatment devices enumerated.
- G2: "Wastewater Pipeline Inspection" is its own software category (CCTV/inspection specialists for sewers, storm drains, manholes).

## Cross-product Comparison

| Structure | Muni-Link | OpenGov UB | Black Mountain | Minol | iWorQ Sewer | Hach WIMS | Linko | Sedaru |
|---|---|---|---|---|---|---|---|---|
| Served-premise service account | ✓ (Account Central) | ✓ (account management) | ✓ | ✓ (operated for city) | — | — | — (IU/FSE permits are a different object) | — |
| Charge basis (reads/flat/surcharge) | ✓ (reads import; sewer calculations; minimum charges) | ✓ (meter data; flat sewer fees) | ✓ (rate structures) | ✓ (AMI consumption data) | — | — | — (IU limits/samples, not charges) | — |
| Bill-to-money cycle | ✓ | ✓ (synced to GL) | ✓ (GL) | ✓ (payments/collections) | — | — | — | — |
| Service orders (office↔field) | ✓ | ✓ (shut-offs/turn-ons/re-reads) | ✓ | ✓ (tied to billing) | work orders over assets | JOB Cal (plant maintenance) | inspections/jobs over regulatees | ✓ (field work) |
| Collection-system estate as assets | — (integrated, not held) | separate product | — | — | ✓ (lines/manholes/pumps) | — | — | ✓ (GIS-connected, Tier-3) |
| Plant process/lab data + regulatory reports | — | — | — | — | — | ✓ | — | — |
| Regulatory program over external parties | — | — | — | — | — | — | ✓ | — |

Reading: the billing/CIS pole (Muni-Link, OpenGov UB, Black Mountain, Minol, and the Tier-3 family: Itineris, SAP, SOFTWater, Springbrook) carries ONE coherent structure — the utility customer-service business system — deployed for water+sewer. The other poles carry different structures with no shared L0. The market label "wastewater utility management" is an umbrella over the utility's assembled software estate.

## Canonical Model (four abstraction layers)

### L0 — Defining Invariant

The wastewater utility's customer-service business system of record — the family's three jointly-held structures bound to sewer service:

1. **The connected-premise service account of record** — persistent identified account binding a customer to a served premise's sewer service (the premise connected to the utility's collection system), carrying service state + financial standing, operated open→sustain→close through service actions, accumulating charges/bills/payments/arrears. Remove → CRM contact base / generic billing account.
2. **The charge basis over the served population** — the configured basis converting each served premise's service into charges: commonly measured water consumption (reads imported from the metering population — frequently the water side's meters/AMI where water and sewer are billed together), flat/fixed rates (per-premises/EDU-class), and surcharge structures for regulated industrial dischargers; direct wastewater metering the exception (industrial users). Remove → fee list with no service basis / generic invoicing.
3. **The bill-to-money cycle** — recurring bill production converting the charge basis into charges under configured rates, the bill as the authoritative lifecycle-managed amount-due record, payments/adjustments/deposits/arrears/budget plans/collections tracked on the same account. Remove → meter-reading tool or ad-hoc invoicing.

Plus the family's service-order instrument (office↔field work binding money state to physical service state).

Binding: the service is **sewer service** — conveyance and treatment of wastewater from connected premises through the utility's collection-and-treatment estate. The estate itself is held in adjacent systems and enters this system as the delivery context of served premises (the gas leaf's own exclusion, applied here).

Jointly-held load-bearing: (1 alone = CRM/generic billing; 2 alone = rate calculator; 3 alone = generic billing engine; 1+3 without 2 = fee-based billing with no service basis; 2+3 without 1 = billing over no served population; 1+2 without 3 = meter/charge ops with no revenue loop).

### L1 — Common Mature Structure

- customer portal (balances, usage, bills, payments) and notifications (email/SMS)
- payment machinery (online, autopay, processors); cash receipting
- general-ledger integration
- AMR/AMI integration for reads
- mobile service orders; delinquency workflows (notices → payment arrangements → field action → restoration)
- reporting/dashboards over revenue, arrears, consumption
- role-based permissions / MFA
- multi-service account composition (water + sewer + stormwater + refuse on one account)

### L2 — Variant / Optional Structure

- who operates the billing: municipal department, municipal authority, water/sewer district, regulated utility (Muni-Link's own customer list)
- charge-basis mix: consumption-derived vs flat/fixed (OpenGov "flat sewer fees") vs minimum+usage; EDU-class units
- relationship to water metering: own meter population vs imported reads from another utility's metering/AMI
- industrial-user class: surcharge structures and separate billing arrangements for permitted industrial dischargers (IU flows may be metered — Fargo permit form)
- turnkey billing-service model (Minol: vendor operates the back office)
- sibling service lines on the same platform: stormwater, refuse/recycling (Muni-Link, OpenGov, Minol, Black Mountain)
- loans/lien machinery (Muni-Link Loans module); backflow inspection management (Muni-Link — water-side module present in sewer-serving products)
- scale tier: small municipal packages → enterprise CIS (BWSC/Itineris)
- deployment: cloud vs on-premise

### L3 — Vendor-specific (Research Notes only)

- Muni-Link: Account Central one-screen design; Integration Manager; Backflow inspection manager; Loans; Utility Websites; "Forever Support" packaging.
- OpenGov: OG Assist (AI work-order creation); OpenGov Financials sync.
- Minol: turnkey service model (call center, delinquency managed by vendor); MinolDirect portal; per-bill pricing.
- Black Mountain: BMS PAY; standalone-or-integrated packaging.
- Itineris: One-V (one-version) update methodology; UMAX on Dynamics 365.
- Hach WIMS: LAB Cal / JOB Cal / BOD Manager modules; 100+ formula library; Rio companion; report-template library (NetDMR/CIWQS/SDWIS/E2).
- Linko: POM Portal; Permit Writer; LabSync; Compliance Assistant (rolling quarters, SNC); LinkoCTS/FOG/HW module split.

## Anti-overfit Register

- **The collection system / treatment works as managed objects** — NOT definitional. Held by the horizontal asset/field family (utility-asset-management, utility-field-service-management) deployed for wastewater (iWorQ, OpenGov Wastewater Collection, Sedaru, Cityworks) and by plant-data systems (WIMS-class). Enters this Type only as the delivery context of served premises. (Same exclusion the gas leaf applied to its pipe network.)
- **Direct wastewater metering** — NOT definitional. The charge basis is commonly derived (water-meter reads) or flat; metered IUs the exception.
- **Discharge compliance (DMR-class reporting, effluent limits)** — NOT in this Type; that is the §21 wastewater-compliance-management Type (the utility's discharger hat). WIMS-class products serve it.
- **Pretreatment/control-authority program machinery (IU permits, inspections, violations, enforcement)** — NOT definitional; a regulatory program over external parties (Linko-class), structurally closer to government inspection/permitting. The billing connection is the industrial-user/surcharge class.
- **Portal/payments/notifications/AMI/mobile/GL** — standard mature structure, not definitional (paper-era billing office satisfies the L0).
- **Multi-service breadth (water+sewer+trash+stormwater on one account)** — variant, not definitional; the sampled products are multi-service and the sewer line is the binding.
- **CCTV/inspection specialist tooling (WinCan/PipeLogix-class)** — adjacent specialist category (G2's own "Wastewater Pipeline Inspection"), part of the operations estate.

## Historical / Market-Sample Check (§24)

- **Paper-era sewer billing office** (mid-20th century municipal sewer department): ledger card per connected premise + water-meter read books (or flat-rate rolls) + rate schedule + receipt ledgers + past-due notices + connection/inspection service orders — satisfies all three L0 legs with zero digital machinery. PASS.
- **Regional variant — sewerage undertaker billing on rateable value** (pre-universal-metering UK pattern): flat/derived charge basis, no wastewater meter — fits leg 2's flat/derived forms. PASS (held at moderate strength; not directly sampled).
- **Special district levying assessments via the tax roll**: charge basis = property/EDU-class; money cycle in assessment form. Fits legs 1+2 and the money cycle in levy form; no direct product evidence in-sample — recorded as an uncertainty, not asserted.
- **Enterprise-tier water+sewer CIS** (BWSC/Itineris): same L0 at scale. PASS.
- The L0 names no protocol, no metering technology, no deployment form, no service-order mechanics specific to one era. PASS.

## Boundary Findings

1. **vs water-utility-management (§19, unprocessed)** — same family L0, other commodity binding. Critically, water and sewer are commonly billed on ONE account by the SAME products (Muni-Link, OpenGov, Black Mountain, Minol, Itineris/BWSC, SAP) — the two leaves are co-realized by one product population; the binding differs (drinking-water service vs sewer service). Forward note for that pass: keep the three commodity verticals (gas/water/wastewater) consistent; the wastewater binding's distinct content is the connection-based service, the derived charge basis, and the estate/regulatory context.
2. **vs utility-billing-platform / utility-customer-information-system-cis (§19, processed)** — horizontal family; this leaf is the sewer-service vertical edition (same L0 + domain binding), exactly as the gas pass framed and the billing pass ratified ("vertical-edition framing RATIFIED... water-utility-management expected to follow the same pattern").
3. **vs wastewater-compliance-management (§21, processed) — FLAG DISCHARGED.** The utility wears two hats: service provider (this leaf: connected premises, charges, bills, money) and permitted discharger (that leaf: permitted discharge points, monitoring data, limit evaluation, regulator-facing reports). WIMS-class products serve the discharger hat plus the plant-data layer; they hold no service accounts and no billing. No L0 overlap; the seam holds.
4. **vs the pretreatment/control-authority program (Linko-class) — FLAG DISCHARGED with a recommendation.** The utility's third hat: regulator over industrial users, food service establishments, and waste haulers. Objects (IU/FSE permits, inspections, samples, violations, enforcement responses, manifests) and grammar (permit → inspect → sample → violate → enforce) are a regulatory program over external parties — structurally closer to government inspection/permitting (§24 territory) than to the service business. Adjacent, not core. The connection point to this Type: industrial users are also billing customers under surcharge structures. RECOMMENDATION for STATUS Boundary Issues: joint review when §24 government inspection/permitting leaves are processed; the pretreatment program may deserve its own leaf or an explicit home.
5. **vs utility-asset-management / utility-field-service-management (§19, processed)** — the collection-system estate (sewers, manholes, lift stations) and its work programs (CCTV, cleaning, backup response) are held there (horizontal family deployed for wastewater). The market's procurement phrase "Wastewater Collection System Management Software" (Palo Alto) names exactly that deployment. Observation for the directory: §19 has Water Network Monitoring but no sewer/collection-network leaf; the collection estate is currently absorbed by the horizontal asset family + CCTV specialists. Recorded as an observation, not a demand.
6. **vs SCADA / industrial-historian / plant-data systems** — the treatment-works operational data layer is adjacent (WIMS-class consolidates SCADA/LIMS/lab data for operations + compliance); not this Type's objects.
7. **UMBRELLA FINDING (the pass's central taxonomy observation)** — the market label "wastewater utility management" is used across billing/CIS products (Muni-Link: "utility billing software for water and wastewater utilities"), collection-operations products (Palo Alto: "Wastewater Collection System Management Software"; OpenGov: "Wastewater Collection Asset Management... Built for wastewater utilities"), plant-data/compliance products (Hach WIMS), and pretreatment products (Linko). No sampled product holds the whole estate; OpenGov itself ships the billing spine and the collection estate as two separate products. The leaf is therefore bound to the ratified commodity-vertical pattern (the utility's customer-service business system of record) and the umbrella reality is documented in the final document's Overview and Related Types so the reader is not misled.

## Uncertainties

- Assessment/tax-roll funding for special districts: structurally plausible fit, no direct product evidence in-sample — held at uncertainty.
- Sewer-specific disconnection-for-nonpayment mechanics: NOT asserted. The money↔service-state coupling is evidenced at family strength (Muni-Link/OpenGov service orders: shutoff/restore); whether sewer-only utilities execute physical shutoffs was not researched.
- Industrial surcharge billing structures inside the sampled billing products: not directly documented (the IU metering fact is evidenced via the Fargo permit form; surcharge *billing* held at variant strength).
- Sedaru unreachable: the collection-ops pole is held at Tier-3 strength (procurement document + press).
- OpenGov pages 403 on direct fetch: content taken from official-page search snippets; marked snippet-level.
- Whether any single product integrates billing + collection ops + plant data as one L0: none found in-sample; the assembled-estate reading stands.
- WIMS "TradeWasteMan" module mention (South Gippsland Water 2014 user presentation): single-source, era-old — not generalized.

## Final Synthesis

Wastewater Utility Management is the wastewater utility's own customer-service business system of record: the served-premise service account (customer × connected premise × sewer-service state × financial standing), the charge basis that converts service into charges (commonly water-meter consumption reads or flat/fixed rates rather than a dedicated wastewater meter), and the bill-to-money cycle (recurring bills, payments, arrears, collections) — operated through service orders that bind money state to physical service state. The service being managed is sewer service: conveyance and treatment of wastewater from connected premises through the utility's collection-and-treatment estate, which is held in adjacent systems (asset/field family, plant-data systems) and enters this system as delivery context. The utility's other two hats — permitted discharger (§21 wastewater-compliance-management) and pretreatment control authority (a regulatory program over external parties) — are separate systems with their own Types/grammars. The market label is an umbrella over the assembled estate; this Type is its customer-and-money spine, the third commodity vertical of the ratified utility family pattern (gas → water → wastewater).
