# Research Animal Facility Management

## Overview

A **Research Animal Facility Management** application is the operational system of record for a facility that keeps laboratory animals for research — the vivarium and the colonies it hosts. Its job is to answer, at any moment and for any animal: *what is it* (species, strain or line, genotype), *where is it* (room, rack, cage or tank), *under which approved protocol does it live and get used*, *what has happened to it* (breeding, health, procedures, movements), and *what does keeping it cost*. It replaces paper cage cards, census books, breeding logs, and per-diem ledgers with a governed animal population that is continuously current.

The defining core is small:

```text
Identified animals in the facility's care
└── Housing locations with tracked occupancy (rooms / racks / cages / tanks)
    └── Census-and-disposition loop
        (arrive → house → move / breed / treat → use → disposition)
        └── Research-use linkage
            (animals held and used under approved protocols, with usage tracked)
```

Everything else commonly associated with this software — breeding and colony machinery, genotyping, cage-card printing, per-diem billing, health records, ordering, regulatory statistical reports — is standard capability that mature products add to make the facility operable. The same core also describes the lighter lab-level "colony management" tools used by individual research groups, which run the core with a smaller subset of that machinery.

## Users & Context

Primary users are the people who operate the facility and the colonies in it:

- **Animal caretakers / vivarium technicians** — the daily operators: check and change cages, move and wean animals, record health observations, print cage cards, execute work requests.
- **Vivarium / facility managers** — own occupancy and capacity, staffing and work requests, billing, and the facility's operational statistics.
- **Veterinarians and veterinary staff** — health records, treatments, colony health surveillance (in facility-oriented products).

Secondary users act on the animals from the research side:

- **Principal investigators and lab members** — maintain their own colonies: plan matings, track litters, record genotypes, select animals for experiments, and keep their protocol usage within approved numbers.
- **Breeding core staff** — produce and maintain lines/strains on behalf of research groups as a service.
- **Compliance / quality staff** — monitor protocol usage against approved numbers, audit trails, training and competence records, and prepare regulatory statistical reports.
- **Billing / finance staff** — consume per-diem cost records and invoice research groups or grant accounts.

The work environment is the animal facility itself: cage-changing rooms, procedure rooms, and offices around them. The software is used at desks, on mobile devices inside the facility next to the racks, and through printed cage cards that carry the record's identity back to the physical cage.

## Core Model

### The Defining Core

Four structures. Remove any one and the product stops being recognizable as this Type:

- **The animal as the managed unit of care.** The central object is the individually identified animal (or colony unit) held in the facility's custody. It carries species, strain or line identity, genotype where relevant, ownership (the investigator or group responsible for it), and a life-stage state that advances with events — newborn, weaned, adult, in-breeding, ended. Exact state vocabularies vary by product; the pattern of an automatically advancing life-stage state is common.
- **Housing location with tracked occupancy.** The facility's physical housing is modeled as a structure — rooms, racks, cages for terrestrial facilities; racks and tanks for aquatic ones — with capacities and occupancy. Every animal's current location is recorded, and the recorded location is expected to match physical reality. Facility-oriented products render this estate graphically (rack and tank displays with occupancy).
- **The census-and-disposition loop.** The population is kept current through recorded life events: animals arrive (born into the colony, ordered from a vendor and received, transferred in), move between locations, breed, receive health events and procedures, and leave custody (euthanasia, transfer out, export, death). Because every event is recorded, counts — how many animals are alive on a given day, how many cages are active, how many were born, weaned, or ended — are computable for any date. This census is the facility's operating picture and the basis of its billing and reporting.
- **Research-use linkage.** Animals are held and used under a governing research authorization — an approved animal-use protocol or study. The system tracks which animals belong to which protocol (assignment to animals or, in some products, to whole cages), and keeps usage accounts against the approved numbers: how many animals were approved, how many used, how many remain, with amendments raising the approved count. In some regimes the authorization is the regulated project license; in others the institutional protocol; in preclinical settings, the study. The common structure is that holding and using animals traces to a tracked authorization.

### Standard Capabilities of Mature Products

These capabilities appear across the researched products and make the core operable at scale. They are expected in the market but do not define the Type:

- **Breeding and colony machinery** — mating setup (pairs, harems, male rotations), plug-date tracking, litters (birth, fostering, parent records), weaning workflows (tag, sex, genotype, wean — with due-date alerts), breeder retirement and remating, pending matings, pregnant females.
- **Lines, strains, and pedigrees** — a registry of lines/strains with gene, strain, and protocol associations; generation tracking; family/pedigree trees spanning many generations, navigable in both directions.
- **Genotyping workflows** — gene/allele nomenclature lists, queues of animals awaiting genotyping, well-plate management, tube and plate labels, and import of results from external genotyping services.
- **Cage cards and labels** — customizable card/label printing (paper, card stock, stickers), QR/barcodes, and scan-based identification, so the physical cage carries the record's identity.
- **Protocol compliance machinery** — approved-number accounting with amendments, protocol permissions, training and competence tracking, SOP management, and severity assessment for genetically modified lines (facility-oriented products).
- **Health and veterinary records** — per-animal health records and treatments in facility-oriented products; medication management (drug registers, expiry tracking, administration via procedures) appears as an extension.
- **Ordering and transfers** — vendor orders for animals and supplies with receipt states (confirm, pre-receive, receive), standing and multi-orders, supplier catalogs, special-service ordering, and transfers of animals between owners or groups.
- **Per-diem billing and cost recovery** — per-diem rates assigned to cages, costs accumulating per owner, cost visualization, and export or invoicing for billing purposes; budgeting information for housing, orders, procedures, and services.
- **Statistics and reporting** — census at any date, born/weaned/ended counts, occupancy reports, breeding productivity, per-line pup counts, data export; regime-specific statistical reports (for example, the European statistical reports generated by one European vendor).
- **Work requests and task management** — a request system connecting scientists, caretakers, and managers, with full request history.
- **Ownership, roles, and permissions** — group accounts (centralized or decentralized strategies), owner-based data segregation, transfers of animals between owners, and granular permissions (view, edit, create, assign, field-level).
- **Audit trail and notifications** — date/time-stamped, user-attributed change history; email alerts for due events (weaning, plug dates, breeder replacement, expiries).
- **Integration surface** — APIs, genotyping-service integrations, electronic lab notebook integrations, housing-hardware interfaces (for example, automated cage-monitoring systems), electronic cage-card exchange, and single-sign-on.

### One Structure, Many Implementations

```text
Concept:   Managed animal unit
Realizations:  individually tracked rodents in cages; fish tracked per tank; colony units in lab-level tools

Concept:   Housing location
Realizations:  room → rack → cage (terrestrial); rack → tank (aquatic); capacity and density limits

Concept:   Research authorization
Realizations:  institutional animal-use protocol with approved-number accounting; regulated project license (EU directive framing); preclinical study

Concept:   Census
Realizations:  alive-on-a-date counts, active-cage counts, occupancy reports, per-diem snapshots

Concept:   Disposition
Realizations:  euthanasia, transfer out, export, death — recorded as the end of custody
```

A reader who has only seen one product should be able to recognize any other from this structure: the vocabulary (mice vs fish, cages vs tanks, protocols vs project licenses) changes, the structure does not.

## How It Works

### Animals enter the population

```text
Ordered from a vendor:  create order → confirm → (pre-)receive → assign to owner and protocol → house in a cage
Born into the colony:   mating set up → plug date tracked → litter born → pups recorded in the litter
Transferred in:         transfer record moves ownership and location
```

Every entry path ends the same way: an identified animal exists, in a recorded location, under an owner, linked to a protocol.

### Operate the daily loop

```text
Check the colony/cage lists and due-date alerts
→ perform husbandry (cage changes, health checks, feeding records where kept)
→ record movements between cages
→ wean litters that fall due (tag, sex, genotype, split into new cages)
→ print fresh cage cards
→ work requests from researchers are executed and closed
```

The loop is alert-driven: wean dates, plug dates, and breeder-replacement dates generate reminders, because missed husbandry events have welfare and cost consequences.

### Breed and maintain lines

```text
Select breeders → set up the mating (pair, harem, rotation)
→ track plug dates → litter born → record litter size and parents
→ at wean age: tag, sex, genotype, wean
→ genotyping results imported from the external service
→ select the next breeders; retire or remate the old ones
→ pedigrees and generation counts update automatically
```

### Use animals under the protocol

```text
Animals assigned to a protocol (automatically by line, or manually)
→ protocol usage account updates (used vs approved)
→ animals may join experiments or studies (cohorts, time points, measurements)
→ procedures and treatments recorded against the animal
→ amendment needed? approved count is raised through a recorded amendment
```

### End custody

```text
Euthanize / sacrifice / transfer out / export
→ animal state becomes ended; cage may be closed
→ census and occupancy update; the history remains
```

### Recover costs

```text
Per-diem rates configured and assigned to cages
→ costs accumulate daily per owner as long as animals occupy cages
→ researchers and managers visualize colony costs
→ costs exported or invoiced to the owner's account/grant
```

### Stay compliant

```text
Protocol usage tracked against approved numbers (with alerts as usage approaches limits)
→ every change attributed in the audit trail
→ training/competence and SOP records maintained (facility-oriented products)
→ statistical reports generated for the governing regime
```

### Capability tiers

**Defining core** — identified animals in care; housing occupancy; the census-and-disposition loop; research-use linkage with usage accounting.

**Standard capabilities** — breeding/colony machinery; lines/strains and pedigrees; genotyping workflows; cage cards and labels; protocol compliance machinery; ordering and transfers; per-diem billing (institutional facilities); statistics and reports; work requests; ownership and permissions; audit trail and alerts.

**Common variants / optional** — health and veterinary records (facility-oriented products); graphical rack/tank maps; transgenic machinery (cryopreservation, rederivation); medication/pharmacy management; regime-specific statistical reporting; study/experiment management depth; hardware integrations.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Colony / animal lists

The primary working surface for finding animals and cages.

- lists animals or cages with identity, state, location, owner, line, and genotype
- filters and saved filters; totals and counts (per cage type, per line, alive on a date)
- primary actions: open a record, build a worklist, move/wean/end animals, export

### Cage / rack / tank map

The spatial surface of the facility (facility-oriented products).

- graphical rack and tank displays with occupancy and capacity
- primary actions: locate an animal's cage, check occupancy, place or relocate animals

### Animal record

The full record of one animal.

- identity, strain/line, genotype, life-stage state, owner, protocol assignment, physical tag, complete event history, lineage links
- primary actions: edit attributes, move, assign to protocol/experiment, record health event, end custody

### Mating and litter records

The breeding surfaces.

- mating: breeders, set-up date, plug dates, status (active, disbanded, retired); litter: parents, birth date, pup count and states, weaning status
- primary actions: set up or disband a mating, record a plug date or litter, foster, wean, end

### Protocol list and detail

The research-governance surface.

- protocols with approved numbers, used numbers, remaining numbers, amendments, attached files, permissions
- primary actions: create or amend a protocol, assign animals or cages, check usage, print the protocol onto cage cards

### Census and statistics dashboards

The management surface.

- alive/active counts at any date, born/weaned/ended counts, occupancy, breeding productivity, cost views
- primary actions: filter, drill in, export, generate regime-specific statistical reports

### Work requests

The communication surface between researchers and facility staff.

- requests bound to colony records or free-standing, with status and full history
- primary actions: create a request, execute and close it, view completed work

### Cage card printing

The physical bridge to the cage.

- customizable cards/labels carrying identity, protocol, owner, and codes; printed per cage or in batches

## Important Rules / Behaviors

- **Life-stage states advance with events.** An animal's state (newborn → weaned → adult → in-breeding → ended) changes automatically as husbandry events are recorded; only animals past weaning can enter breeding. Exact vocabularies and age thresholds are configurable and vary by product.
- **Protocol usage is accounted, not assumed.** The system keeps a running account of animals used against the number approved on each protocol, with amendments recorded when the approved count changes. Whether over-assignment is blocked or merely surfaced varies by product; the accounting itself is the common structure.
- **Location fidelity is the core discipline.** The recorded cage must match the physical cage; cage cards and scans exist to reconcile the two, and movements are recorded events.
- **Ownership gates visibility.** Animals belong to owners (investigators or groups); other users see an owner's data only through granted permissions, and transfers of animals move ownership explicitly. Facilities shared between organizations run under separated authorization contexts.
- **Capacity and density guard welfare.** Cage capacities and housing-density limits are modeled so overcrowding is surfaced or prevented; exact limits follow each facility's standards.
- **Every change is attributed.** Because the record is the facility's compliance evidence, changes carry user and timestamp in an audit trail.
- **Disposition is terminal but correctable.** Ending an animal or cage closes its custody; some products allow reversing an ended state to fix errors, with the correction itself recorded.
- **Due dates drive the daily rhythm.** Weaning, plug checks, and breeder replacement generate alerts; missed husbandry events carry welfare and cost consequences (overdue weaning and extra cages are commonly cited cost drivers).

## Variants

Common shapes of the same Type:

- **Institutional vivarium management** — the facility operator's system: census, occupancy, compliance machinery, health records, ordering, per-diem billing, statistical reporting; role separation between caretakers, managers, veterinarians, and researchers.
- **Lab-level colony management** — the research group's system: breeding, genotyping, lines, and protocol usage for the group's own animals; lighter on billing, health, and facility machinery; commonly SaaS with free or per-lab pricing.
- **Aquatic facility management** — tank-based realization: stock vs experiment tanks, crossings instead of matings, larva/juvenile/adult age levels, survival and death statistics, Petri-dish and tank labels.
- **Transgenic and cryopreservation operations** — embryo and sperm freezing with cryotank maps, revitalization, rederivation through embryo transfer, donor ordering; often an extension of the core system.
- **Preclinical / pharma in vivo facilities** — animals managed in linkage to GLP-style studies rather than academic protocols; the study takes the authorization role.
- **Species variants** — rodents (cages, matings, litters, ear tags), fish (tanks, crossings), and large animals (unverified in this research pass, expected to fit the core with husbandry-scale adaptations).

A variant remains a variant of this Type as long as the defining core — identified animals in care, housing occupancy, the census-and-disposition loop, and research-use linkage — still describes it.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Animal Research Ethics / IACUC Platform | adjacent, heavily integrated | the ethics platform's central object is the protocol under committee review (submission → review → recorded decision); here the protocol is a usage-tracking reference and the animals are the central object. The approved protocol functions as the authorization this Type's operations check against. |
| Biobank Management | adjacent | manages preserved specimen inventory (custody-centric, inert material, consent governance); this Type manages living animals that breed, age, and must be housed daily. |
| Laboratory Information Management System / LIMS | adjacent | LIMS is test/assay-centric — samples flow through processing to results; this Type is care/census-centric — the population itself is the managed asset. |
| Scientific Core Facility Management | adjacent | both may bill principal investigators, but core-facility systems manage bookable services and instruments; this Type manages animals and husbandry. Per-diem billing is the animal-facility realization of cost recovery, not a service catalog. |
| Electronic Lab Notebook / Scientific Data Management | adjacent | documents experiments and data; this Type operates the animal population that experiments consume. Experiment membership here is animal-to-study linkage, not protocol documentation. |
| Livestock Management | structurally nearest outsider | production-economics context (herds, yields, feed, market) vs research-governance context (authorized protocols, strains/lines, experiments). Remove the research-use linkage and this Type drifts toward livestock-shaped husbandry inventory — that is the boundary. |
| Animal Shelter Management | adjacent outsider | shelter context is custody transfer and adoption (intake → outcome, adopter-facing welfare); research facilities retain custody under research authorizations and animals are consumed by studies. |
| Practice Management System (veterinary) | adjacent outsider | client-facing clinical care (appointments, encounters, claims); a vivarium's veterinary function is internal colony health management. |
| Clinical Trial Management / preclinical Study Management | downstream consumer | study-centric systems plan and report studies; they consume animals from, or interoperate with, the facility system. The coupling is integration, not identity. |

The two boundaries that matter most in practice: **against the IACUC platform** the discriminator is the central object (the animals in care vs the protocol under review); **against livestock management** the discriminator is the research-use linkage (authorized protocols and experiments vs production economics).

## Representative Products

- **PyRAT** (Scionics Computer Innovation, Germany) — web-based animal facility management software, established since 2003, positioned as the leading such product in Europe; SaaS or self-hosted; strong compliance framing (authorization management under EU directive 2010/63/EU), graphical rack displays, breeding and pedigree machinery, budgeting/invoicing, EU statistical reports; aquatic sibling product (PyRAT Aquatic) and add-ons (Transgenic, Pharmacy, Integration).
- **SoftMouse.NET** (Iseehear, Canada) — cloud colony-management platform for labs, breeding cores, and institutions; deep breeding/genotyping/pedigree machinery, protocol usage accounting, per-diem cost tracking, free and premium tiers; documented through an extensive official online manual.
- **JCMS — JAX Colony Management System** (The Jackson Laboratory, US) — historical open-source, multi-user mouse colony database (Access/MySQL, web and mobile surfaces, cage cards, pedigree trees); no longer developed or supported; included as the older-generation anchor of the lab-level pole.

## Sources

Research date: **2026-09-09**

- SoftMouse.NET (Iseehear) — homepage: https://www.softmouse.net/ ; official online manual (FAQ): http://www.softmousefaq.com/ (including "Mouse States Explained" and "Track No. of Animals Used")
- PyRAT (Scionics Computer Innovation) — product page: https://www.scionics.com/pyrat ; PyRAT Aquatic: https://www.scionics.com/pyrat_aquatic ; Add-ons: https://www.scionics.com/pyrat_add_ons
- JCMS (The Jackson Laboratory) — product page: https://www.jax.org/jcms ; source repository: https://github.com/jaxcs/JCMS-root
- Boundary check only: AniLog (animal-welfare-sector software) — https://www.anilog.co.uk/

> Sourcing limitation: several major US institutional vivarium vendors (Topaz Technologies, eSirius, Mosaic Vivarium) were not reachable from the research environment during this pass, so the US institutional pole is under-sampled. US-specific regulatory machinery (for example USDA reporting) is intentionally not asserted in this document; billing and compliance findings rest on the European facility product and the per-diem capabilities documented by the colony-management product. The historical open-source product is evidenced at positioning and structure level only. Precise numeric limits (rates, capacities, age thresholds beyond one product's documented defaults) are intentionally not stated. Product-by-product observations and evidence calibration are recorded in the paired Research Notes.
