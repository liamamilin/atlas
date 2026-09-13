# Research Notes — Provenance Research Platform

Slug: `provenance-research-platform`
Research date: 2026-09-10
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what "provenance research" software actually is in the art/museum world: what the object of record is, how an artwork's ownership history is structured, what the research workflow looks like, who performs it, how evidence and uncertainty are handled, and where the Type's boundaries run — especially against the §27 museum-cluster siblings that pre-hung flags on this leaf (museum-accession-cataloging, museum-condition-reporting, museum-collections-management) and against adjacent art-market Types (due-diligence screening, gallery management, auction systems).

## Initial Boundary (pre-research hypothesis)

- Core use: investigating and documenting the history of ownership and custody of works of art — who held an object, when, how it transferred, and on what evidence — for scholarship, due diligence, acquisition decisions, and restitution research.
- Users: provenance researchers, curators, registrars, catalogue-raisonné teams, due-diligence staff at auction houses/dealers, restitution researchers, scholars.
- Nearest neighbors: Museum Accession/Cataloging (provenance fields on catalogue records — that pass expects this leaf's core to be "investigation machinery rather than record creation"), Museum Condition Reporting (ownership history vs physical state — pre-agreed clean), Museum Collections Management (container), Art Gallery Management (provenance as archive on artwork records), Due Diligence Platform / stolen-art registries (screening vs history-building), Digital Collection Portal (publication surface).
- Unknowns: do dedicated standalone products exist; how is the ownership event chain structured at field level; is evidence/uncertainty handling definitional or common; how do shared reference corpora (transcribed sales catalogs) relate to the working research environment.

## Research Questions

1. What is the object of record — how are artworks identified and what accumulates on them?
2. How is ownership history structured — free text, typed events, agent records, dates?
3. What event types exist, and how are possession (non-ownership custody) and unlawful transfers represented?
4. How is evidence handled — source documents, catalogs, archives, publications — and how is uncertainty/gap represented?
5. Who uses these systems and for what decisions (scholarship, due diligence, restitution, acquisition)?
6. What is the role of shared reference corpora (sales catalogs, dealer stock books) vs institution-internal research records?
7. Where does provenance research end and record-keeping (cataloguing), screening (due diligence), and publication begin?
8. Historical check: does the paper-era provenance line in a catalogue entry / research file satisfy the minimal core?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole | Why sampled |
|---|---|---|
| **Navigating.art** | dedicated platform for art-historical research teams (catalogue raisonné + provenance research; nonprofit) | the reachable market's purpose-built working-environment pole; fully public field-level help center documenting the provenance event model |
| **Getty Provenance Index** (Getty) | open shared reference corpus of provenance data (dealer stock books, sales catalogs, archival inventories) | the canonical public provenance-research resource; event-based linked-open-data model fully documented in a public user guide |
| **eHive** (Vernon Systems) | mid-market cloud CMS with provenance as a field group on object records | the record-keeping minimal pole; only sampled CMS with fully public field-level docs (consistent with sibling passes) |
| **Art Loss Register** | due-diligence screening service (stolen-art database) | boundary anchor: "checking provenance" in the screening sense vs building ownership history; included to hold the seam, not to define the Type |

TMS Collections / MuseumPlus provenance machinery: login-gated in sibling passes (recorded limitation) — not retried; no screen-level claims. Artory/Verisart-class blockchain registry products and CatalogIt not sampled this pass (noted as boundary context).

## Sources

All fetched 2026-09-10 unless noted.

**Navigating.art (Tier 1 — field-level operational docs):**
- https://navigating.art/ (homepage: positioning, projects)
- https://navigating.art/solution (platform description: database, cataloguing interface, publication; FAQ)
- https://knowledge.navigating.art/en/ (help center home: section structure)
- https://knowledge.navigating.art/en/objects (Objects section: provenance events, art events, reports)
- https://knowledge.navigating.art/en/auctions (Auctions section)
- https://knowledge.navigating.art/en/tutorial/how-to-add-provenance (provenance event entry workflow)
- https://knowledge.navigating.art/en/provenance-transaction-types (full transaction-type table, 25+ types, 3 categories)

**Getty Provenance Index (Tier 1 — operational user guide):**
- https://www.getty.edu/databases-tools-and-technologies/provenance/ (main page: scope, datasets, resources)
- https://www.getty.edu/databases-tools-and-technologies/provenance/gpi-user-guide/ (user guide: data model, search, resource reports)

**eHive (Tier 1 — field-level operational docs):**
- https://help.ehive.com/ (help home)
- https://help.ehive.com/field-help/object/field-help.htm (field help index: Acquisition tab = "provenance and acquisition value")
- https://help.ehive.com/acquisition-fields.htm (Acquisition tab field groups)
- https://help.ehive.com/field-help/object/provenance-details.htm (Provenance details field)

**Art Loss Register (Tier 2 — product pages):**
- https://www.artloss.com/ (homepage: positioning, search/register/recover services)

**Unreachable / limited (recorded per source-access rules):**
- TMS Collections / TMS Conservation Studio, MuseumPlus: operational docs login-gated (consistent with museum-condition-reporting and museum-accession-cataloging passes); no screen-level claims.
- help.ehive.com/field-help/object/provenance.htm 404'd once before the correct path (acquisition-fields.htm) was found.
- Artory, Verisart, CatalogIt, German Provenienzforschung tooling not fetched this pass.

## Product Observations

### Navigating.art — dedicated research platform (evidence layer A)

- Positioning: nonprofit platform that "equips teams with digital tools to create and publish digital catalogues raisonnés and archives"; "supports researchers to record information, organize digitized materials, and publish resources online." Used for Wildenstein Plattner Institute's revised Monet catalogue raisonné, Gauguin catalogue raisonné, Gallen-Kallela, Eva Hesse archives.
- Platform composition: database + cataloguing interface + digital publication. "The database allows researchers to save data in its context, as it relates to other pieces of recorded data."
- Help-center structure: General / Objects / Archive / Publications / Agents / Auctions / Exhibitions / Master Data / Best practices.
- **Provenance events** (dedicated help section): "How to add provenance information" documents the entry workflow:
  1. Select the provenance type — "more than 25 types of provenance events such as acquisition, bequest, gift, and consignment"; the type "defines the set of information that has to be added."
  2. Fill in source-related details — previous owner and other agents chosen from existing agent records or created new; agent properties include address, dealer flag, private-collection flag. "The private collection checkbox will hide all personal agent details such as the name and display 'private collection' instead." "You can add as many agents as necessary to describe the event in its full complexity."
  3. Fill in receiver-related details — receiver agent, date, credit line, reference URL. "The level of certainty can also be documented by checking 'questionable' in the agent settings or marking the whole event as 'possibly.' It is up to you if you want to publish unverified information or keep it internal until further research has been conducted."
  4. Alternative artwork details — alternate title or alternate creation year recorded along the provenance event.
  5. Notes and archival material — notes, resource entries, and media connected to the provenance event, "enables direct linking the information to a primary source or other related material."
- **Provenance transaction types** (full table, evidence layer A): three categories —
  - **Change of ownership** (e.g., Acquisition, Artist's studio, Bequest, By descent, By exchange, Commissioned, Confiscation, Destroyed, Donation, Forced sale, Gift, Inherited, Looting, Restitution, Return, Sale, Seized, Transfer)
  - **Change of possession** (e.g., Consigned, Fractional gift, In possession, Location unknown, On deposit, On loan, Partial gift, Promised gift, Sous réserve d'usufruit, Stolen, Stored) — "All possession events are displayed indented to indicate their relation to the last known owner."
  - **Unlawful ownership changes** (Looting, Forced sale) — "Any provenance events following after this type of event are automatically displayed indented to indicate unlawful exchange, even if they are ownership transactions. The indentation is stopped by adding an event of type 'Restituted' or 'Returned'."
- Purpose statement (from the transaction-types article): "Provenance is an integral part of the history of an artwork, tracing its steps from creation to present day. This documentation creates a comprehensive biography of each piece… Provenance research helps museums and collectors verify the moral and legal validity of ownership chains, particularly given concerns about looted or unlawfully acquired artworks. Today's researchers seek to create provenance records that are as accurate and complete as possible, filling in all gaps to reconstruct the full story of an artwork's journey through time."
- Supporting machinery: Agents section (agent records with roles for provenance events; "how to record an unknown private collection"); Auctions section (auction entries, linking a catalogue to an auction, "documenting no auction catalogue exists", customized auction reports); Exhibitions section (exhibition events); art events (examination events, signatures/inscriptions/markings); artwork changelog; artwork dossier; artwork reports (single and multi-artwork generation); internal vs public rendering comparison ("Previewing public artwork information… compare highlight discrepancies internal vs. public rendering").
- Publication: public/restricted access models; template or API-driven custom site; continuous updating after publication ("living document").

### Getty Provenance Index — shared reference corpus (evidence layer A)

- Positioning: "Providing open access to art provenance data drawn from millions of archival records"; "allows researchers to trace the ownership history of artworks and analyze art market and collecting trends over time."
- Datasets: **Dealer Stock Books** (transactional records from Goupil & Cie./Boussod, Valadon & Cie., M. Knoedler & Co.), **Sales Catalogs** ("auction house and dealer sales catalogs documenting works of art offered for sale in Europe from 1650 to 1945"), **Archival Inventories** ("legal records of objects in European private collections from 1520 to 1880"). Complementary resources: Collectors Files (20,000+ files on collectors), Payments to Artists, Public Collections (provenance records 1500–1990 for artworks in public institutions in GB/US).
- Platform: transitioning to a linked-open-data structure on the **Arches** platform (open-source); legacy datasets remain accessible in a Legacy Index platform.
- Data model (user guide): "In Arches, Getty Provenance Index data is generated through events. Often, but not always, these events are related to historic transfers of ownership." Nine Resource Models based on the Linked.Art profile of CIDOC CRM: **Activity** (auctions, exhibition sales, lotteries, and lot-level parts), **Group**, **Person**, **Physical Object**, **Place**, **Provenance Activity** ("Activities related to ownership, including transfer of ownership, transfer of custody, and inventorying of physical objects"), **Set** (lot/entry groupings), **Textual Work** (text of sales catalogs, inventories, stock books — the source record), **Visual Work**.
- Example event decomposition (from the guide): a sale generates/links a Set (lot + lot identifier), a Provenance Activity (transfer of ownership + valuation), a Physical Object (art object + material), a Person (buyer + name), a Textual Work (record of the sale + page).
- Search machinery: simple keyword search with operators (exact, wildcards, NOT); advanced faceted search over the data model (model/branch/sub-branch/field level; query conditions; Boolean AND/OR between facets); time filter (custom/predefined date ranges, time wheel); saved searches (editor-curated); stable unique URLs per query; export (CSV/JSON/JSON-LD; API docs; SPARQL endpoint; raw datasets on GitHub).
- Results and resources: results as cards; **Related Resources** network graph (interactive, nodes/edges per the semantic data model); **Resource Reports** (branch tables, controlled-vocabulary concepts, resource-instance links, export per resource).
- Corrections workflow: "Users who find incorrect or incomplete information in the Getty Provenance Index are encouraged to submit corrections by emailing the resource URL and supporting documentation."

### eHive — record-keeping field group (evidence layer A)

- Object cataloguing page has an **Acquisition tab**: "You can record information about the credit line, provenance, and valuation on the Acquisition tab of the object cataloguing page. You can also create a separate acquisition record" (linked to the object record).
- **Provenance field group**: Provenance date; Provenance details; Provenance person; Provenance place.
- **Provenance details field**: "records information about the object's history, usually events that happened before you acquired the object." Private field; text field with 1,000-character limit; searchable by field ID (`provenance_details: "founding collection"`).
- Companion fields: Credit line, Named collection; acquisition valuation/price/funder fields.
- Interpretation (calibrated): provenance is carried as record content on the object record — the minimal field-shaped realization. No structured event chain, no agent records, no explicit evidence binding in the fetched field docs; the history is prose in a private field, decomposed by date/person/place companion fields. This matches the accession-cataloging pass's prediction: the CMS carries provenance fields; the research apparatus is elsewhere.

### Art Loss Register — screening service (evidence layer A; boundary anchor)

- Positioning: "the leading due diligence provider for the art market, and maintains the world's largest private database of stolen art, antiques and collectables."
- Three services: **Search** ("Submit the details of an item to be searched against the Art Loss Register database and other databases of stolen art"), **Register** ("Report the theft or loss of an artwork or valuable item… for registration on the database"), **Recover** ("help lost items of art to be reunited with their owners").
- "Experts around the world use our services to check the provenance of items before they buy or handle them." Claims ~450,000 searches conducted annually, ~700,000 items on the database (marketing figures — recorded as vendor claims, not asserted).
- Recovery narratives confirm the market practice: auction houses check items "as part of their standard due diligence process"; art fairs vet works with the ALR "alongside the vetting committees."
- Interpretation (calibrated): this is a **screening/registry service** — it answers "is this item recorded as stolen/lost/disputed?" It does not build or document an object's ownership history. It is the consumer-side complement: due diligence consumes provenance research and adds a risk-screening step. Distinct Type; boundary anchor.

## Cross-product Comparison

| Dimension | Navigating.art | Getty Provenance Index | eHive | Art Loss Register |
|---|---|---|---|---|
| Object of record | artwork records (with dossier, changelog, images, signatures/markings) | Physical Object / Visual Work resources (millions, from historic documents) | object records (Acquisition tab) | items registered as stolen/lost/disputed |
| Ownership history structure | typed provenance events (25+ types; ownership / possession / unlawful categories); agents with roles; dates; credit line; reference URL | event-based LOD: Provenance Activity resources (transfer of ownership, transfer of custody, inventorying) linked to Person/Group/Object/Set/Textual Work | provenance fields (date/details/person/place) as record content; separate acquisition record | not applicable (theft/loss records, not ownership chains) |
| Evidence anchoring | notes, resource entries, media attached to events; "direct linking the information to a primary source"; reference URL | every record derives from a source document (Textual Work: sales catalog, stock book, inventory; page-level) | not explicit in fetched docs (prose field) | registration records (police/insurer/owner reports) |
| Uncertainty / gap handling | "questionable" agent flag; "possibly" event marking; unknown private collection ("private collection" hides identity); "Location unknown" event type; internal vs public publishing decision | corrections workflow for incorrect/incomplete information; controlled vocabularies | not in fetched docs | n/a |
| Unlawful-transfer semantics | dedicated category (Looting, Forced sale, Seized, Confiscation); automatic indentation of subsequent events until Restituted/Returned | historic transfers including forced sales within scope (1650–1945 catalogs) | not in fetched docs | theft/looting registrations (incl. WWII, colonial claims) |
| Search machinery | artwork list/grid search and filtering; multilanguage structured search | simple + advanced faceted search; time filter; saved searches; network graph of related resources; exports/API/SPARQL | field-level search (`provenance_details: …`) | item search against database (service-mediated) |
| Outputs | artwork reports (public and internal); published catalogue raisonné/archive (public/restricted); continuous updates | resource reports; exports; open datasets; APIs | record content for cataloguing/loan workflows | search certificates / recovery services |
| Who uses | research teams (catalogue raisonné projects, museums, institutes) | researchers worldwide (open access) | museums, galleries, collectors (cataloguing) | auction houses, dealers, insurers, police, fairs, buyers |
| Packaging | dedicated standalone platform (nonprofit) | open research database/platform | CMS field group | standalone screening service |

**Cross-product commonalities (evidence layer B):** artworks/objects as individually identified records; ownership history expressed as events linking agents to objects over time; source-document anchoring (transcribed catalogs, stock books, archives) as the evidence base; search over the history data; the history record as something accumulated, corrected, and extended over time.

**Product-specific (evidence layer A, single-product):** Navigating.art's transaction-type taxonomy with possession/unlawful categories and automatic indentation semantics; certainty marking ("questionable"/"possibly"); unknown-private-collection masking; internal-vs-public rendering comparison. Getty's nine-model LOD structure, network graph, SPARQL/API/CSV openness, editor-curated saved searches. eHive's field-group realization and acquisition-record linkage. ALR's search/register/recover service triad.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **Object-anchored ownership history.** Individually identified works of art (or comparable cultural objects) serve as the anchor records, and the system documents the history of ownership and custody *of those objects* — who held them, when, and how possession or title moved. Remove → a person/collector database or a generic event log; the artwork-centered "biography" disappears.
2. **The event-structured chain.** The history is represented as an ordered chain of discrete events (acquisition, sale, gift, bequest, consignment, deposit, loan, looting…) each binding agents (owners, possessors, transferors) to the object at a point in time — not as an undifferentiated prose paragraph. Remove → a static description with a provenance sentence; the traceable, extendable structure disappears.
3. **Evidence-and-gap discipline.** Events and claims are anchored to sources (documents, catalogs, archives, publications) and incomplete knowledge is explicitly represented — unknown holders, uncertain attributions, gaps in the chain — so the history is verifiable research content rather than assertion. Remove → unsourced narrative; the research discipline (and its due-diligence/restitution value) collapses.

Jointly-held is load-bearing: 1+2 without 3 = a dealer's stock list or unverified narrative; 1+3 without 2 = a file of documents with no reconstructed history; 2+3 without 1 = an event database not anchored to objects.

Realization-depth note (recorded honestly): the dedicated platforms (Navigating.art) and the shared corpus (Getty) carry all three legs in full; the CMS field-group realization (eHive) carries legs 1–2 in field form with leg 3 reduced to institutional practice — the record-keeping minimum, consistent with the accession-cataloging pass's prediction that the CMS carries provenance fields while the investigation machinery is this leaf's center.

### L1 — Common Mature Structure

- **Agent records** — people and organizations (collectors, dealers, auction houses, institutions) held as reusable, identified records with roles in events; dealer and private-collection status as agent properties.
- **Typed event vocabulary** — a controlled set of transaction types covering ownership changes, possession changes (loan, deposit, storage, consignment), and unlawful changes (looting, forced sale, seizure), with restitution/return semantics.
- **Source-document corpus** — transcribed/indexed sales catalogs, dealer stock books, archival inventories, and collector files as the evidence base researchers search and cite.
- **Structured search** — keyword and faceted search over objects, agents, events, and sources; date-range filtering.
- **Reports and publication** — per-object provenance reports; publication of research as catalogues raisonnés, databases, or public resources; internal vs public distinction.
- **Accumulation and correction** — records enriched and corrected over time; corrections/feedback workflows on shared corpora.
- **Exhibition and publication events** — documented alongside ownership as part of the object's history (exhibition references, literature citations).

### L2 — Variant / Optional Structure

- **Packaging**: dedicated research platform (Navigating.art) vs open shared corpus (Getty Provenance Index) vs CMS field group/module (eHive; TMS-class per sibling passes). The shared-corpus pole is read-mostly (research resource); the working-platform pole is write-heavy (research environment).
- **Restitution-focus deployments**: Nazi-era (1933–45) research, colonial-context claims, wartime looting — unlawful-transfer semantics become first-class (Navigating.art's indentation machinery; ALR's claim classes).
- **Market-analytics reuse**: the same event data supports art-market and collecting-trend analysis (Getty's stated secondary purpose).
- **Linked-open-data / API exposure**: SPARQL, JSON-LD, CSV downloads, stable URIs (Getty); API-driven custom publication sites (Navigating.art).
- **Certainty granularity**: per-agent vs per-event uncertainty marking (Navigating.art depth; not observed as machinery elsewhere in the sample).
- **Screening integration**: due-diligence checks against stolen-art registries as a separate service consumed alongside provenance research (ALR pole).

### L3 — Vendor-specific (kept here, not in the final document)

- Navigating.art: the exact 25+ transaction-type table and its indentation rules; nonprofit pricing model (€30,800/20-year example budget); premium/standard/legacy editorial modes; data-ownership FAQ; HPF Innovations gGmbH; named projects (Wildenstein Plattner Institute Monet/Gauguin, Gallen-Kallela, Eva Hesse).
- Getty: the nine Resource Model names and Linked.Art/CIDOC CRM basis; Arches platform; Goupil/Knoedler dataset specifics; 1650–1945 and 1520–1880 coverage windows; time-wheel UI; editor-curated saved searches; corrections email address.
- eHive: field IDs (provenance_details…), 1,000-character limit, private-field visibility, search syntax example, acquisition-record linkage mechanics.
- ALR: 450,000-searches/700,000-items vendor claims; service triad branding; named recovery cases; fair-vetting partnerships.

## Vendor-specific vs Type Findings (explicit)

- The **three-category event structure** (ownership / possession / unlawful) is Navigating.art's articulation, but the underlying distinction — ownership vs custody vs unlawful deprivation — is the domain's standard conceptual vocabulary (reflected in Getty's "transfer of ownership, transfer of custody" Provenance Activity definition). The distinction is Type-level; the specific type list and indentation machinery is product-level.
- **Certainty marking** as explicit machinery is Navigating.art-verified at that depth; the underlying practice (marking uncertain attributions, "private collection", "location unknown") is domain-standard provenance convention — held as L1 with the machinery depth marked product-specific.
- **Source anchoring** is Type-level (both Navigating.art and Getty anchor to documents); the LOD graph realization is product-level.
- **Screening** (ALR) is a distinct service Type, not a capability of this one — the market draws the line between building history and checking risk.

## Rejected Findings

- "Provenance research = a provenance field on the catalogue record" — REJECTED as the definition: the field group is the record-keeping minimum; the Type's center is the investigation apparatus (event chains, agents, evidence, uncertainty) over and around those records.
- "Provenance research platforms are due-diligence tools" — REJECTED: screening services check items against risk registries; they do not reconstruct ownership histories. Due diligence *consumes* provenance research.
- "Provenance = only pre-acquisition history" — REJECTED: the event chain runs from creation to the present (Navigating.art's stated scope "from creation to present day"; possession events like promised gifts and loans occur after acquisition).
- "Provenance research is museum-only" — REJECTED: the same structure serves catalogue raisonné projects, collectors, dealers, auction houses, and restitution bodies; the museum is the directory's framing, not the structure's limit.
- "The Getty Provenance Index is the Type" — REJECTED: it is the shared-corpus pole (read-mostly reference data); the working research environment (record, extend, verify) is a different realization of the same object world.
- "Blockchain/registry certificates are this Type" — NOT ASSERTED: registry/certificate products (Artory/Verisart-class) were not sampled; they issue provenance attestations rather than host research; boundary noted, no claim made.

## Boundary Findings

**1. vs Museum Accession/Cataloging (§27 sibling, processed 2026-09-08) — the pre-hung flag, discharged from this side.** That pass recorded: "Catalogue records carry provenance/history fields… but the research apparatus (structured investigation of an object's ownership history, evidence chains) is a different job over the same records. Adjacent; expected to hold as long as that leaf's core is investigation machinery rather than record creation." Confirmed from this side: the accession records the intake event into the collection (source, method, title); provenance research reconstructs the chain of ownership and custody around the object's whole life, with evidence and uncertainty machinery the catalogue record does not carry. The eHive observation directly supports the seam: its Acquisition tab holds both the acquisition record machinery (that leaf) and the provenance field group (this leaf) — adjacent content on one tab, different jobs. Removal tests: strip the investigation apparatus → a catalogue with provenance fields remains (that leaf stands); strip the catalogue records → provenance research platforms maintain their own object records (Navigating.art, Getty both do). **Verdict: distinct sibling Types; boundary holds as pre-agreed.**

**2. vs Museum Condition Reporting (§27 sibling, processed 2026-09-08).** Pre-agreed: "Provenance documents the history of ownership/origin (who held it, how it traveled); condition documents physical state. Both attach to object records; content classes differ." Confirmed — no overlap found in any sampled product's machinery. **Verdict: clean, ratified from this side.**

**3. vs Museum Collections Management (§27 container, processed 2026-09-08).** That pass listed this leaf among unprocessed counterparties. From this side: provenance research operates on object records (the container's register) when module-packaged, and maintains its own object records when standalone (Navigating.art, Getty). The container owns custody accountability and the object register; this Type owns the ownership-history investigation layer. Removal tests both directions hold. **Verdict: keep-both with containment framing, consistent with the accession-cataloging and condition-reporting precedents.**

**4. vs Art Gallery Management (§27 sibling, processed 2026-09-06).** That document records "the record is the archive — provenance, condition, exhibition history and documents accumulate on the artwork record" as gallery-inventory behavior, and notes secondary-market dealers weight provenance more. The gallery's core is the commercial loop (inventory, consignment, sale); provenance research's core is the history investigation. Meeting point: gallery records feed and consume provenance documentation. **Verdict: distinct; adjacent.**

**5. vs Due Diligence Platform (§11) / stolen-art registries (Art Loss Register pole).** Screening answers "is this item recorded as stolen/lost/disputed?" via registry search; provenance research reconstructs and documents the ownership chain. They meet in practice: a due-diligence check combines provenance review with registry screening (ALR's own recovery narratives show auction houses doing both). Removal tests: remove the risk-registry search → provenance research stands; remove the history-building machinery → a screening service remains (ALR is exactly that). **Verdict: distinct Types; the ALR pole is the boundary anchor, not a member of this Type.**

**6. vs Digital Collection Portal (§27 sibling, processed 2026-09-07).** Portal = published public surface over records governed elsewhere; this Type = the research machinery producing provenance content. Navigating.art's publication layer is the output surface, not the core (the platform's database and cataloguing interface precede publication; internal-vs-public distinction is explicit). **Verdict: distinct; publication is downstream.**

**7. vs Auction Management System (§05.18, processed 2026-09-06).** Auction systems run commercial sales (lots, bidding, settlement); provenance research treats historical auctions as *evidence* — Navigating.art holds auction entities (auction entries, linked catalogs, "no auction catalogue exists" documentation) as source records for ownership events, not as transactions to execute. **Verdict: distinct; the auction appears in both worlds with different semantics.**

**8. vs Legal Research Platform / Investment Research Platform (§07/§08).** Different object worlds: legal materials and financial instruments vs artworks and ownership chains. The restitution-research overlap (legal questions about title) is a workflow consumer, not a Type identity. **Verdict: distinct.**

## Historical / Market-Sample Check

Paper-era form of the same discipline: the provenance line in a printed catalogue entry ("Collection of X, London; his sale, Christie's, 15 July 1902, lot 45; … purchased by Y") — an ordered, semi-standardized event chain with sources named; the per-object research file with correspondence, photocopies of sales catalogs, index cards on collectors; the catalogue raisonné's provenance section per entry; museum registration files recording prior ownership at acquisition. All satisfy the three legs: object-anchored history (the entry/file per object), event-structured chain (the semi-standardized provenance line format), evidence-and-gap discipline (sources cited; "private collection", "whereabouts unknown" conventions). The Getty Provenance Index itself is the digitization of exactly this paper corpus (sales catalogs, stock books, inventories), and its pre-Arches form "replicated the tabular structure of the source material" — direct documentation of the paper lineage. The definition therefore names no software surface, no cloud, no LOD graph, no transaction-type list — older, regional, paper-based realizations all fit. Modern machinery (typed event vocabularies, agent databases, network graphs, APIs, publication platforms) is era layering, held outside the core.

## Uncertainties

- TMS Collections / MuseumPlus provenance machinery is login-gated (consistent with sibling passes); their realizations are asserted only at directory/product-page level, and only via the sibling passes' recorded limitations.
- Whether other dedicated standalone provenance-research platforms exist beyond Navigating.art could not be exhaustively excluded; Navigating.art is the clearly reachable dedicated product. German Provenienzforschung tooling (museum-side research environments) was not sampled.
- Registry/certificate products (Artory, Verisart-class) not sampled; their relationship to this Type (attestation vs research) is noted as a boundary, not verified.
- CatalogIt's provenance fields were documented in the accession-cataloging pass but not re-fetched here; the field-group realization rests on eHive this pass.
- The Getty Provenance Index is mid-transition (Legacy Index → Arches LOD); observations mix both platforms as documented in the user guide.
- ALR's search-volume and database-size figures are vendor marketing claims; recorded as claims, not asserted.
- The exact split between "provenance research platform" and "catalogue raisonné platform" for Navigating.art: the platform's positioning is catalogue-raisonné-first, but its provenance-event machinery is a documented, dedicated subsystem; this pass treats the provenance machinery as the Type-relevant core and the publication layer as variant. A vendor might describe the product differently.

## Final Synthesis

The Provenance Research Platform is the art world's **ownership-history investigation layer**: individually identified artworks anchor records whose history of ownership and custody is reconstructed as an ordered chain of typed events binding agents to the object over time, with every claim anchored to sources and every gap or uncertainty explicitly represented — because the record's value (scholarly, commercial, legal, restitution) depends on being verifiable and honest about what is not known. The market realizes the Type as a dedicated research environment (Navigating.art — record, extend, verify, publish), an open shared corpus of transcribed ownership evidence (Getty Provenance Index), and the record-keeping minimum inside collection management systems (eHive's provenance field group; TMS-class per sibling passes). It is deliberately distinct from catalogue record-creation (the accession event vs the life history), from condition documentation (ownership vs physical state), from the collections container (one documentation layer over its object records), from gallery commercial management, and from due-diligence screening services (building history vs checking risk). The paper-era provenance line and research file satisfy the defining core, so the definition names no software surface or era machinery.
