# Research Notes — Environmental Site Assessment

## Research Goal

Understand what software the "Environmental Site Assessment" (ESA) Application Type actually covers in the market: what the unit of work is, who operates the software, what objects and evidence structures exist inside it, how an assessment flows from trigger to deliverable, and where the boundary lies against the already-processed siblings (Contaminated Site Management, Environmental Impact Assessment Platform, Environmental Compliance Management, Environmental Monitoring Platform, Environmental Laboratory Management) and the unprocessed neighbors (Environmental Data Platform, Environmental Remediation Management).

## Initial Boundary

Working hypothesis before research:

- "Environmental Site Assessment" is the *assessment-execution* application: software supporting a bounded, site-specific investigation of a property's environmental (contamination) condition, producing a formal deliverable.
- The term is a formal term of art in North America (Phase I / Phase II ESA under ASTM E1527 and the US "All Appropriate Inquiries" rule) and has direct analogs elsewhere (UK land contamination risk assessment stages; Canadian Phase I/II ESA; Australian preliminary/detailed site investigation).
- Nearest confusable Types: Contaminated Site Management (processed — site lifecycle record), Environmental Impact Assessment Platform (processed — prospective project gating), Environmental Data Platform (unprocessed, research exists), Environmental Monitoring Platform (processed), Environmental Laboratory Management (processed), plus real-estate-side assessment Types (Building Condition Assessment, processed — flagged this leaf as "contamination due diligence vs physical condition").

## Research Questions

1. What legally/professionally defines an ESA (US ASTM E1527 / AAI; UK LCRM stages; other regimes)?
2. What is the unit of work — the assessment engagement? the evidence report? the property?
3. What evidence classes does the assessment draw on, and which are productized as software?
4. Who are the software users: environmental professionals, commissioning users (buyers/lenders), conveyancers, data suppliers?
5. What does the deliverable look like and where is it produced (report-writing platforms)?
6. How do the intrusive phases (Phase II sampling) relate to the field-data substrate already documented in the Contaminated Site Management pass?
7. Where are the seams: vs contaminated-site record, vs EIA, vs data platform, vs monitoring, vs physical-condition assessment?
8. What is deliberately NOT this Type (remediation execution, compliance obligations, agency site registers, NEPA/EIA report products)?

## Representative Products

| Product | Market | Pole | Customer tier | Why sampled |
|---|---|---|---|---|
| EDR (LightBox) | US | evidence-report supply + report writer (PARCEL) + platform (LightBox Live) | environmental professionals/consultants, lenders, CRE | dominant US Phase I data supplier; explicit ASTM E1527-21 alignment |
| ERIS | US / Canada / Mexico | evidence-report supply + analysis (Xplorer) + report-writing SaaS (Scriva) + mobile field app | environmental professionals/consultants | fullest end-to-end "Power Suite" spanning order → analysis → field → report |
| Envirocheck (Landmark Information Group) | UK | report/data supply + analysis workbench (Envirocheck Analysis) + export to GIS/CAD | environmental and property professionals | UK regime realization; uses the literal term "environmental site assessment" |
| Groundsure | UK (+AU) | due-diligence report products, residential (conveyancing) + commercial + insight/data workspace | conveyancers/homebuyers AND consultants | different customer tier (residential transactions, Law Society guidance) |
| ESdat (EScIS) | AU/US/international | field & laboratory data management for site investigation | consultants, mining, government | cross-reference specimen for the Phase II / intrusive-investigation substrate (already sampled in the Contaminated Site Management pass) |

Standards/regulatory sources examined as products-of-the-domain: ASTM E1527-21 (public standard page), UK LCRM guidance (GOV.UK).

## Sources

Fetched 2026-09-08 unless noted:

- ASTM E1527-21 standard page (Significance and Use, Scope sections publicly displayed): https://www.astm.org/e1527-21.html
- LightBox EDR — Environmental Due Diligence Products page: https://www.lightboxre.com/industries/environmental-due-diligence-products-edr/ (reached via https://www.edrnet.com/ redirect)
- ERIS — root and Scriva pages: https://www.erisinfo.com/ , https://www.erisinfo.com/scriva/
- Envirocheck (Landmark) — root: https://www.envirocheck.co.uk/ (product detail links point to https://www.landmark.co.uk/products/envirocheck and https://www.envirocheck.co.uk/analysis/)
- Groundsure — root: https://www.groundsure.com/
- ESdat — root: https://esdat.net/
- UK LCRM (Environment Agency, GOV.UK): https://www.gov.uk/guidance/land-contamination-how-to-manage-the-risks
- Cross-referenced sibling research (not fetched this pass): research/contaminated-site-management.md (ESdat/EQuIS/Locus EIM/EnFlection observations, 2026-09-07), research/environmental-impact-assessment-platform.md, research/environmental-data-platform.md

Unreachable / limitations:

- US EPA "All Appropriate Inquiries" pages: https://www.epa.gov/all-appropriate-inquiries and https://www.epa.gov/cercla/all-appropriate-inquiries both returned 404 (two attempts, then abandoned per network rule). The US regulatory framing below therefore rests on the ASTM E1527-21 page's own text, which directly cites the AAI Final Rule (40 C.F.R. Part 312), the CERCLA landowner liability protections, and the 2018 BUILD Act. The AAI rule text itself was not directly examined.
- Landmark product-detail pages (landmark.co.uk/products/envirocheck) and Envirocheck Analysis page were not fetched (nav-level evidence only for those subpages).
- Groundsure product pages (Avista/Review/Insight detail) not fetched; root-page product summaries only.
- No standalone "Phase I practice management" system (beyond report writers) was identified and reached; the practice-management layer is evidenced only inside report-writing platforms (Scriva, PARCEL).

## Product Observations

### ASTM E1527-21 — Standard Practice for Environmental Site Assessments: Phase I Environmental Site Assessment Process (evidence layer A)

The authoritative definition of the process the software serves. Directly observed from the public standard page:

- **Purpose**: "define good commercial and customary practice in the United States of America for conducting an environmental site assessment of a parcel of commercial real estate with respect to the range of contaminants within the scope of CERCLA… and petroleum products"; intended to permit the user to satisfy "all appropriate inquiries" for the CERCLA landowner liability protections (innocent landowner, contiguous property owner, bona fide prospective purchaser).
- **Goal**: "identify recognized environmental conditions" (RECs). REC = presence / likely presence of hazardous substances or petroleum products in, on, or at the subject property due to a release or likely release, or presence under conditions posing a material threat of a future release. "A de minimis condition is not a recognized environmental condition." (Appendix X4 offers further examination of the REC definition; the page does not display the HREC/CREC definitions — not directly observed.)
- **Site-specific**: "This practice is site-specific in that it relates to the assessment of environmental conditions for specific commercial real estate." Business-entity/asset purchases and off-site liabilities are out of scope.
- **Who conducts**: "A Phase I Environmental Site Assessment must be performed by an environmental professional as specified in 7.5.1" (definition cross-referenced to the AAI rule, 40 C.F.R. Part 312, Appendix X2). "The professional judgment of an environmental professional is… vital."
- **The user is a distinct role**: Section 6 "User's Responsibilities"; the user may conduct lien searches, provides knowledge, and must satisfy user responsibilities when relying on a prior assessment (4.6.4).
- **Components** (4.6.2): interviews with owners, operators, and occupants; searches for recorded environmental cleanup liens; reviews of federal, tribal, state, and local government records; visual inspections of the subject property and adjoining properties; declaration by the environmental professional.
- **Point-in-time + viability**: "The environmental site assessment is based upon conditions at the time of completion" (4.5.5). Presumed viable when conducted within 180 days prior to acquisition; components (i)–(v) must be conducted/updated within 180 days, other components within one year (4.6.1–4.6.3).
- **Prior assessment usage**: prior ESAs may be reused subject to current investigation of conditions likely to affect RECs (4.7).
- **Uncertainty**: "No environmental site assessment can wholly eliminate uncertainty… intended to reduce, but not eliminate, uncertainty" (4.5.1); "All appropriate inquiries does not mean an exhaustive assessment" (4.5.2); "Not every property will warrant the same level of assessment" (4.5.3).
- **Scope is contractual**: non-scope considerations (Section 13, e.g., business environmental risk) are "additional services… agreed upon between the user and environmental professional" (1.4, 4.4).
- **Documentation**: "sufficient documentation of all sources, records, and resources utilized in conducting the inquiry… must be provided in the written report" (1.1.5); Appendix X5 provides a suggested report table of contents/format.
- **Context**: 2018 BUILD Act extended BFPP to certain commercial tenants/lessees (Note 1).

### EDR (LightBox) — Environmental Due Diligence Products (evidence layer A)

- Positioning: "EDR is the Industry's Most Trusted Environmental Data Source for 30+ Years… supports environmental due diligence, Phase I ESA workflows, and environmental site assessment research across commercial real estate." "With over 2,000 databases, and the nation's largest collection of historical resources… puts the power of quality data and insight into the hands of the industry's most successful site assessors."
- **Packages table** (Product | Primary Use | Supports Phase I ESA | Data Type):
  - EDR Radius Map — Regulatory search — Yes — Government records
  - SANBORN Map — Historical land use — Yes — Fire insurance maps
  - Historical Aerials — Site history — Yes — Aerial photographs
  - Lien & AUL — Title risk — Yes — Legal records
- **EDR Radius Map Report with GEOCHECK** — "the leading government records report"; searches "over 2,000 databases and layers, from federal, state, tribal, local, and proprietary sources"; delivered "in either PDF format or through LightBox Live."
- **Certified SANBORN Map Report** — fire insurance maps "from 1866… over 1.3 million" maps, ~12,000 cities/towns; "helps assess historical land use, past activities, and potential environmental conditions."
- **City Directory Reports** — digitized directories, searchable, mapped; "visualize City Directory addresses overlaid with Sanborn Maps, historical aerials, tax parcels, and more."
- **Historical Aerial Photographs** — decade packages "typically beginning in the 1930s, '40s or '50s"; geo-referenced; "meet and exceed ASTM E1527-21 requirements."
- **Historical Topographic Maps** — QUADMATCH presentation of USGS quads.
- **PARCEL Report Writer** — "collaborative platform… produce higher quality reports in far less time"; explicitly framed against Word-based report production: "templates, formatting, importing data and images, version control and consistency"; "Create more consistent, accurate Environmental Reports in 40% less time" (vendor claim).
- **Environmental Lien & AUL Search** — "a search of official land title records for environmental liens and activity use limitations"; stand-alone or in packages.
- **NEPASearch Map Report** — NEPA information "for the preparation of environmental impact assessments" — the EIA-adjacent product line sold by the same vendor (boundary specimen).
- Packages: Basic / Standard / Premium / Premium 1980.
- Ordering surface: web.edrnet.com ordering "switchboard" login; LightBox Live platform; "ASTM Resource Center" for the E1527-21 transition; FAQ: "Who uses EDR LightBox? Environmental professionals, consultants, lenders, and commercial real estate stakeholders"; "helps identify recognized environmental conditions, potential contamination, and environmental liability risks."

### ERIS — Environmental Risk Information Services (evidence layer A)

- Positioning: "Your Leading Property Due Diligence Resource… the most current data, historical information and software solutions for environmental and property assessments in the United States, Canada, and Mexico."
- **ERIS Power Suite** — "Advanced technology for every stage of property assessment": Crucial Accuracy (data + historicals "for any property in North America"), Mobile Portability (ERIS Mobile App "take ERIS with you in the field"), Investigative Depth (ERIS Xplorer "powerful visualization and analysis tool"), Advanced Customization (Figure Creator "fast, easy ordering and cutting-edge customization"), Output Efficiency (Scriva "write reports collaboratively and efficiently").
- **Database Reports** — "Key federal, state and proprietary databases are researched to identify environmental concerns associated with your subject property and surrounding area."
- **Custom Area/Corridor Reports** — linear-corridor searches (infrastructure variant).
- **Historical products**: Fire Insurance Maps, Topographic Maps, City Directories, Historical Aerials ("play an essential role in the historical review component of a Phase I ESA"), Environmental Liens, Chain of Titles, Lien & Title bundle, Updated Title Report.
- **Adjacent report lines**: NEPA Report ("evaluate potential effects on natural and cultural resources"), Physical Setting Report, Climate Risk Assessment, Permit Timeline Report, Mexico Package, International Reports.
- **Applications**: ERIS Xplorer ("interactive platform for analyzing and viewing data, map layers, and historical imagery"), Figure Creator, Vapor Screening Tool, Pinpoint, Mobile App.
- **SaaS**: ERIS Direct ("real-time… environmental risk and property data via searchable online subscription"); **Scriva** (below).
- Ordering: order.erisinfo.com order system.

### ERIS Scriva — report-writing SaaS (evidence layer A)

- "The report writer with unlimited users & templates"; "innovative report-writing platform… collaborative tools to elevate productivity, improve quality control and establish a consistent output."
- "its ability to assign, track and collaborate on document production creates a robust project management system that goes beyond report-writing."
- Document types: "letters/proposals to technical reports (Phase I/IIs, PCAs, Asbestos, etc.)."
- Features observed: One-Click Duplication ("copy finalized, delivered, or archived reports… duplicate tables, appendices, and report content"); Integrated City Directory tables ("distance, direction, and listings automatically"); AI Report Assistant ("auto-summarize complex tables/site findings, and instantly draft professional narratives from your raw field notes"); end-to-end workflow ("combine your ERIS data, notes, checklists, photographs, and Figure Creator… graphics"); project dashboard ("manage projects, templates, users, due dates, and metrics"); role-based collaboration with simultaneous editing; confidential projects/restricted access; customized branding/templates.
- **Mobile integration**: photos taken in the ERIS mobile app "automatically uploaded to the Scriva photo log section, and notes on the photos become captions"; "Site checklists are sent to Scriva to review and drop in an appendix"; photos/comments/checklists "push from the mobile app to ERIS Xplorer, Figure Creator and My Orders page."
- PCA adjacency: "cost recommendation tools, automatically create cost tables… generate Fannie Mae and Freddie Mac required outputs" (property condition assessment — adjacent deliverable type on the same rails).
- Vendor-published testimonial: Phase I report writing "around 20 hours… now… about 10 hours" (marketing claim — research notes only).

### Envirocheck (Landmark Information Group, UK) (evidence layer A, nav-level)

- "Powerful data solutions that bring accuracy, speed and confidence to environmental risk assessment"; "environmental reports, mapping products and specialised datasets for environmental and property professionals – backed by our industry-leading digital analysis platform."
- Nav structure: **Reports / Data / Analysis / Projects**.
- Reports: "Designed to effectively support your environmental site assessment" — the literal ESA term used for the UK market.
- Data: "Envirocheck Export service… for use in your own GIS and CAD systems."
- Analysis: "Envirocheck Analysis enables you to assess and analyse our extensive archive of historical maps and environmental data faster and more accurately than ever before, ultimately delivering more enhanced reports to your client, faster."
- Adjacent: Biodiversity Net Gain reports (Landmark product line).

### Groundsure (UK, +Australia) (evidence layer A, root-level)

- "We empower sustainable land and property decisions"; "comprehensive range of due diligence reports for commercial and residential property transactions."
- **Residential tier**: Avista — "our most comprehensive environmental, mining and climate risk report, ensuring maximum compliance with Law Society guidance" (conveyancing-facing; product matrix PDF offered).
- **Commercial tier**: Review — "most comprehensive commercial search… backed by our in house consultancy expertise."
- **Insight tier**: Enviro/Geo/Map Insight reports + "Explorer access included as standard"; free "Insights" access (open-source data, OS mapping, drawing tools, risk alerts, re-access of quoted sites).
- **Groundsure Explorer** — "your environmental data workspace… map and analyse environmental, geological and historical data."
- Mining searches "tailored to the needs of conveyancing, consultancy, and property development… informed by expert interpretation."
- Scale claims (marketing): 1.6M digitized OS maps; ClimateIndex™ used in 1.3M+ property transactions; 40 years mining risk experience. B Corp certified; separate Australian site.

### ESdat (EScIS) — field/laboratory data management (evidence layer A; cross-reference to Contaminated Site Management pass)

- "helps scientists and engineers import, manage, analyze and report data from laboratories, field programs, data loggers, sensors, historical sources, and regulatory standards"; "for scientists, engineers, and managers who need to understand environmental, hydrogeological and related site investigation, monitoring, and compliance data."
- Laboratory integration (labs upload validated deliverables), Field Programs ("plan, execute and report all stages of large or recurring field programs"), Bore Logging, exceedance tables vs pre-loaded regulatory standards (US/CA/AU/NZ/UK), QA indicators (holding times, RPD, blanks, ionic balance), statistics, maps, Power BI/ArcGIS/Excel/API feeds, public portal.
- Industries: consultants, mining, government, energy, industry, landfills. Client logos include the major global consultancies.
- This is the substrate the intrusive (Phase II-class) assessment phase runs on — the same product family the Contaminated Site Management pass sampled as its consultant-workbench pole.

### UK LCRM — Land Contamination Risk Management (GOV.UK, Environment Agency) (evidence layer A)

- "How to assess and manage the risks from historic land contamination"; expected practice for England (and, per updates, NI/Scotland/Wales with local notes).
- Three-stage structure: **Stage 1 risk assessment → Stage 2 options appraisal → Stage 3 remediation and verification**.
- Terminology: "historic contamination"; "competent person" requirement; rapid measurement techniques protocol for intrusive investigation.
- The UK process analog of the US Phase I/II/III ladder: risk assessment (desk study + investigation) is the assessment act; options appraisal and remediation belong to the contaminated-site/remediation Types.

## Cross-product Comparison

| Dimension | EDR (US) | ERIS (US/CA/MX) | Envirocheck (UK) | Groundsure (UK/AU) | ESdat (cross-ref) |
|---|---|---|---|---|---|
| Subject anchor | subject property | subject property (+ corridors) | property/site | property (residential & commercial) | site/project locations |
| Evidence reports as products | Radius Map, Sanborn, Aerials, City Directories, Topo, Lien & AUL, NEPASearch | Database Reports, FIM, Topo, City Directories, Aerials, Liens, Chain of Title, PSR, NEPA, Climate | environmental reports + mapping data + export | Avista/Review/Insight report products, mining searches | — (data management, not report products) |
| Search geometry around property | radius search | radius + custom area/corridor | report-defined coverage | report-defined coverage | sampling locations |
| Historical evidence classes | fire insurance maps, aerials, city directories, topo | same classes | historical map archive | historical OS maps | historical sources as data import |
| Title/legal evidence | lien & AUL searches | liens, chain of title, updated title | — (not observed at nav level) | — (not observed at root) | — |
| Analysis workbench | LightBox Live viewer | Xplorer | Envirocheck Analysis | Groundsure Explorer / Insights | maps, graphs, exceedance tables |
| Report production | PARCEL Report Writer | Scriva (+ mobile photo log/checklists) | "delivering more enhanced reports to your client" (analysis→report framing) | report products are the deliverable | data analysis & reporting outputs |
| Field capture | — (not observed) | ERIS Mobile App | — (not observed) | — (not observed) | field programs, bore logging |
| Ordering machinery | ordering switchboard, packages | order system, packages | register/order (implied by account nav) | sign-in/order (implied) | — |
| Standards alignment marketed | ASTM E1527-21 resource center | Phase I ESA component framing | "environmental site assessment" support | Law Society guidance (residential) | pre-loaded regulatory standards |
| Customer tier | consultants, lenders, CRE | consultants | environmental & property professionals | conveyancers/homebuyers + consultants + developers | consultants, mining, government |
| Adjacent lines on same rails | NEPA, PZR zoning | NEPA, climate, permit timeline, PCA outputs | biodiversity (BNG) | climate, mining/geo, ecology | compliance monitoring data |

Stable across the sample (B-layer cross-product commonality):

1. The **subject property** anchors everything: every report, map set, and deliverable is scoped to a defined property plus a defined surrounding area.
2. **Standardized evidence reports about a property** are the market's productized unit: regulatory/database searches, historical maps (fire insurance / OS), historical aerials, historical topography, city directories, and title/liens records — the desk-study evidence classes of the assessment process.
3. **Ordering and delivery machinery** wraps the evidence reports (order systems, packages/bundles, account logins).
4. **Map/analysis workbenches** let the practitioner view, overlay, and analyze the evidence (historical imagery, layers, drawing, alerts).
5. **Report production** is a distinct, productized layer (PARCEL, Scriva): templates, data-table insertion, photo logs, checklists, figures, collaboration, project dashboards, delivery states — explicitly aimed at Phase I/II-class technical reports.
6. **Field capture** feeds the report (mobile photos → photo log with captions; site checklists → appendices) where offered.
7. The same platforms sell **adjacent report lines** (NEPA, climate, mining, biodiversity, PCA) on the same property-anchored rails — evidence that the *environmental contamination* assessment is one product family member, not the whole platform.

## Canonical Abstraction

### L0 — Defining Invariant (three jointly-held structures)

```text
1. The assessment engagement of record on a defined subject property
   (a specific parcel/site + an identified purpose/trigger + a defined scope or
   standard + an environmental professional performing it for a commissioning user)

2. Structured evidence collection about the property's environmental condition
   (records/desk study at minimum — regulatory records, historical maps/aerials/
   directories, title & lien records; site reconnaissance; intrusive sampling and
   laboratory analysis where the scope includes it)

3. The formal assessment deliverable
   (findings — identified conditions/concerns, classified — compiled with the
   documented evidence trail into a report delivered to the commissioning user
   for their decision)
```

Jointly-held is load-bearing:

- 1 alone = a property file / project folder
- 2 without 1 = environmental data research (data-platform territory)
- 3 without 1+2 = an opinion letter / empty template
- 1+2 without 3 = evidence gathering with no deliverable (a data service, not an assessment)
- 2+3 without 1 = a report with no property anchor (not a site assessment)
- 1+3 without 2 = an opinion without evidence (not an assessment)

The scope/standard discipline (ASTM E1527-class practice, LCRM stages, or an agreed scope) is what shapes legs 2 and 3 — it defines which evidence classes are required and what the report must contain. The professional-judgment requirement (environmental professional / competent person) is part of leg 1's engagement structure.

### L1 — Common Mature Structure

- Standardized evidence-report products for the desk study: regulatory/database searches with defined search geometry around the property; historical fire-insurance/OS maps; historical aerial photography; historical topographic maps; city directories; environmental lien & activity-use-limitation / chain-of-title searches; physical-setting reports
- Ordering & delivery machinery: order systems, packaged bundles, account/order management, turnaround as a competitive dimension
- Map/analysis workbenches over the evidence: layer viewing, historical-imagery overlay, drawing tools, risk alerts
- Report-production platforms: templates & branding, evidence-table insertion, photo logs, site checklists → appendices, figure creation, version control, role-based collaboration, project dashboards (users, due dates, metrics), delivery states (finalized/delivered/archived), one-click reuse
- Mobile field capture feeding the report (photos with captions, checklists)
- Portfolio/multi-site screening for transaction programs (lender/CRE tier)
- Standards-alignment as a marketed feature (E1527-21 transition support; Law Society guidance compliance)
- Vapor encroachment screening tools

### L2 — Variant / Optional Structure

- Jurisdiction packaging: US ASTM E1527/AAI; UK LCRM stages; Canada; Mexico; Australia
- Customer-tier packaging: consultant-facing tooling vs residential/conveyancing report products vs lender/portfolio programs
- Tiered assessment depth: non-intrusive (Phase I-class) vs intrusive investigation (Phase II-class, running on the field/lab data substrate) vs further assessment/remediation phases (belonging to neighboring Types)
- Adjacent report lines on the same rails: NEPA/EIA-support reports, climate risk, mining/geo stability, biodiversity, property condition assessment, permit timelines
- Corridor/linear reports for infrastructure
- Free/self-serve data tiers; AI report drafting (era-current)

### L3 — Vendor-specific (research notes only)

- EDR: "2,000+ databases" claim; Sanborn library figures (1866, 1.3M maps, ~12,000 towns); GEOCHECK/QUADMATCH/PARCEL product names; Basic/Standard/Premium/Premium 1980 package names; "40% less time" claim
- ERIS: Scriva/Xplorer/Figure Creator/Pinpoint product names; testimonial "20 hours → 10 hours" claim; unlimited users/templates pricing posture; Fannie Mae/Freddie Mac PCA outputs
- Groundsure: 1.6M OS maps; ClimateIndex™ 1.3M transactions; Avista/Review/Insight names; B Corp posture; Australian sister site
- Envirocheck: Analysis/Export product names; Landmark brand family
- ASTM: committee E50/E50.02, 59-page document, version lineage E1527-97→05→13→21

## Vendor-specific Findings

- The report-writer layer is productized by the data suppliers themselves (EDR's PARCEL, ERIS's Scriva) rather than by independent vendors in the reached sample — a market-structure observation, not a definitional one.
- Scriva's PCA support (Fannie Mae/Freddie Mac outputs) shows the same production machinery serving the property-condition-assessment deliverable — the rails are deliverable-generic; the ESA is the contamination-class member.
- Groundsure's residential tier is the only sampled product explicitly facing homebuyers/conveyancers (Law Society guidance compliance); the US sample is consultant/lender-facing.
- ERIS's corridor reports and vapor screening tool are single-vendor observations (product-specific until corroborated).

## Rejected Findings

- **"Environmental Site Assessment = database report products"** — rejected as the definition: it over-fits to the current data-supplier market. The evidence-report layer is the dominant software realization of the desk study, but the paper-era assessment and the report-production layer both exist without it; the L0 is the engagement structure, and evidence-report supply is documented as the standard capability it sits on.
- **"REC (recognized environmental condition) terminology as definitional"** — rejected: REC and de minimis are US-standard (ASTM E1527) vocabulary; UK LCRM's risk-assessment stages and the competent-person requirement are the analogs. The canonical finding structure is "classified conditions/concerns", not the US label.
- **"Report-writing platforms as definitional"** — rejected: they are a productized production layer; the deliverable itself (a documented report with classified findings) is definitional, its production tooling is not.
- **"Phase I/II/III ladder as definitional"** — rejected: the ladder is US-practice vocabulary; the canonical depth axis is non-intrusive vs intrusive vs further assessment, which other regimes express differently.
- **"NEPA/climate/mining/biodiversity/PCA report lines as part of this Type"** — rejected: adjacent deliverable classes sold on the same property-anchored rails by the same vendors; they are boundary specimens, not members of the Type.

## Boundary Findings

1. **vs Contaminated Site Management (processed)** — CSM holds the *site's standing record* across its lifecycle (investigation → remediation → monitoring → closure, retained after closure); ESA holds the *bounded assessment engagement* that produces a deliverable. The handoff is designed: the ESA report and its data become evidence attached to the site record (sibling pass: "an assessment is a record attached to the site and its results are ingested as evidence. Remove the assessment-execution machinery and what remains is this Type's record; remove the site-centered record and what remains is ESA"). The Phase II intrusive phase runs on the same field/lab substrate CSM's consultant pole uses — shared substrate, different center.
2. **vs Environmental Impact Assessment Platform (processed)** — EIA assesses *predicted future effects of a proposed project* under an authority's legally defined gate; ESA assesses the *existing environmental condition of a specific property* for a commissioning user's decision, with no authority gate (the standard is contractual/voluntary; CERCLA liability protection is a legal *consequence* of doing it, not an approval instrument). Boundary specimen: the same vendors (EDR NEPASearch, ERIS NEPA Report) sell NEPA/EIA-support reports as a separate product line from their Phase I ESA lines.
3. **vs Environmental Data Platform (unprocessed; research exists)** — the data platform holds a cross-program environmental data corpus; ESA's evidence reports are per-property, per-engagement products consumed by the assessment. The corpus is the supplier's asset; the assessment is the practitioner's bounded work. Sibling pass confirms handoff ("assessment execution… outputs are ingested as corpus inputs here").
4. **vs Environmental Monitoring Platform (processed)** — monitoring is ongoing observation of operating facilities/parameters; the ESA is explicitly point-in-time (ASTM 4.5.5) with defined viability windows.
5. **vs Environmental Laboratory Management (processed)** — the lab processes samples into validated results; the ESA consumes results as one evidence class among several (records, maps, reconnaissance).
6. **vs Building Condition Assessment (processed)** — that pass flagged the seam: contamination due diligence vs physical condition of buildings. Different object (environmental media vs building fabric), same transactional trigger.
7. **vs Environmental Compliance Management (processed)** — compliance manages standing legal obligations of an operating organization; the ESA is a one-time (per-transaction/per-trigger) condition determination whose output may *create* obligations but is not itself the obligation register.
8. **vs Site Selection / property search surfaces** — screening many candidate locations for fit vs determining one property's environmental condition in depth; different question, different evidence depth.
9. **Removal tests**: remove the property anchor → environmental research/data platform; remove the evidence structure → opinion letter; remove the deliverable → data service; remove the bounded-engagement frame → contaminated-site record; remove the existing-condition frame → EIA.

## Historical / Market-Sample Check (§24)

- Paper-era Phase I ESA: a consultant reviews paper Sanborn maps, aerial prints, city directories and title records, walks the site, interviews occupants, and issues a typed report with findings — satisfies all three L0 structures with no software at all. The sampled products digitize the records hunt (evidence platforms) and the report production (report writers); they do not define the practice.
- UK pre-digital desk studies (manual map and archive orders) satisfy the same structure; LCRM's stage framing is process law, not software.
- The REC concept and the environmental-professional requirement are US-standard specifics; the canonical structure (property + evidence + findings + deliverable) holds without them (UK "competent person," LCRM stages are the analogs).
- The data-supply platforms are the current market's dominant *software* realization; treating "database report products" as the definition would over-fit to the current supplier market — the L0 is the engagement structure, and the evidence-report layer is documented as the standard capability it sits on.

## Uncertainties

- US EPA AAI pages unreachable (404 ×2); the US regulatory framing rests on the ASTM page's own citations of 40 C.F.R. Part 312 and the LLPs. AAI-rule-specific details (e.g., exact component definitions beyond those quoted) are not independently verified.
- HREC/CREC condition classes and the "data failure" concept are named in the standard's structure but not displayed on the fetched page — not asserted in the final document beyond REC and de minimis.
- The standalone practice-management layer (beyond report writers' project dashboards) was not directly evidenced; claims kept at "report-production platforms include project-management machinery."
- The Phase II/intrusive pole is evidenced through ESdat (cross-referenced from the Contaminated Site Management pass) rather than an independently sampled Phase II-specific product; the shared-substrate finding is solid, the Phase II tooling market depth is not independently profiled.
- Canada/Mexico/Australia regime packaging observed at navigation level only (ERIS country nav, Groundsure AU site); no regime process documents fetched.
- Landmark product-detail pages and Groundsure product pages not fetched; those products documented at nav/root level (evidence strength noted per claim).
- Vendor-published numeric claims (database counts, library sizes, time savings, transaction counts) are marketing figures — excluded from the final document.
- The residential/conveyancing workflow (order-by-solicitor → report to homebuyer) is observed at product-page level; the workflow itself was not examined.

## Final Synthesis

The Environmental Site Assessment Application Type is the **assessment-execution application for a specific property's environmental condition**. Its unit of work is a bounded assessment engagement: a defined subject property, an identified trigger (typically a property transaction, redevelopment, financing, or regulatory/suspected-contamination concern), a defined scope or standard, and an environmental professional performing the assessment for a commissioning user. The engagement's substance is structured evidence — records/desk study (regulatory database searches, historical maps, aerials, directories, title/liens), site reconnaissance, and intrusive sampling where in scope — and its output is the formal assessment deliverable: a report that compiles the documented evidence trail with classified findings (recognized conditions/concerns) and feeds the user's decision.

The market realizes the Type on two productized layers wrapped around that engagement: (1) **standardized evidence-report supply** about a subject property — the dominant product category (regulatory database searches with defined search geometry, historical fire-insurance/OS maps, historical aerials, topographic maps, city directories, lien/title searches), sold through ordering systems with analysis workbenches over the data; and (2) **assessment production tooling** — report-writing platforms (templates, evidence-table insertion, photo logs, checklists, figures, collaboration, project dashboards, delivery states) and mobile field capture feeding them. The intrusive (Phase II-class) phase runs on the field/laboratory data substrate shared with Contaminated Site Management.

The Type's identity is held by the engagement structure, not by any evidence class or tool: remove the property anchor and it becomes environmental data research; remove the evidence structure and it becomes an opinion; remove the deliverable and it becomes a data service; widen the frame to the site's standing lifecycle record and it becomes Contaminated Site Management; re-point it at the future effects of a proposed project under an authority gate and it becomes Environmental Impact Assessment.
