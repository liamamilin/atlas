# Research Notes — Pet DNA Analysis Platform

Directory location: §29 Home, Family, Personal & Local Services (siblings: Veterinary Practice Management, Pet Health Application, Pet Insurance Customer App, pet-care operator siblings)
Research date: 2026-09-09
Slug: pet-dna-analysis-platform

---

## Research Goal

Understand what a "Pet DNA Analysis Platform" actually is as an Application Type: who operates it, what objects exist inside it, how a genetic test moves from purchase to a physically mailed sample to a lab result to an interpreted report, and where its boundary sits against Pet Health Application, Veterinary Practice Management / veterinary diagnostics, human DTC genomics (outside the directory, structural rhyme), and e-commerce.

## Initial Boundary

Working hypothesis at Understand step:

1. Core use: an owner (or breeder) purchases a DNA test for a specific animal, collects a sample at home, mails it to the operator's lab, and receives interpreted genetic results (breed/ancestry, inherited health risk, traits) through an account.
2. Primary users: pet owners; breeders as a large secondary pole; veterinarians as receivers of results and, in some products, orderers/dispensers.
3. Nearest neighbors: Pet Health Application (shared pet-profile vocabulary), Veterinary Practice Management (clinical care context), E-commerce (kit sales), human DTC genomics (same skeleton, different subject).
4. Likely confusions: is this just an e-commerce store for kits? Is it a lab portal? Is it a health app? The center of gravity should determine the answer.
5. Unknowns: results lifecycle (one-time vs evolving), relatives/kinship mechanics, breeder-tooling depth, sample-failure handling, privacy/consent model.

## Research Questions

1. What is the unit of record — the kit, the order, or the tested animal?
2. What is the full lifecycle of a test: purchase → activation → sample → lab → results?
3. What do results consist of, and how are they interpreted (copy state, inheritance, breed relevance)?
4. What happens after results: vet sharing, updates, relatives, breeder tools?
5. How do consumer-owner, breeder, and veterinarian audiences differ in the same product family?
6. Which structures are definitional vs common-mature vs variant vs vendor-specific?
7. What does the software actually manage (vs the wet lab, which the software does not run)?

## Representative Products

Selection logic: market representation + documentation depth + different product philosophies + different customer tiers.

1. **Embark Veterinary** — consumer science-premium pole; dog; deep help center (Tier-1). Health+breed+relatives; separate breeder and vet lines.
2. **Wisdom Panel** (Mars Petcare) — mass-market pole; dogs + cats; large database claims; breeder line is a separate brand (Optimal Selection); vet line exists.
3. **Basepaws** — cat-first species pole + whole-genome-sequencing premium pole; science/research-forward; help center (Tier-1, Gorgias).
4. **Orivet** — breeder/professional pole; store-of-tests model (single-condition tests, parentage verification, multipacks); breeder portal + app; lab turnaround guarantee.
5. DNA My Dog — intended budget-consumer sample; **unreachable (503 ×2 on both domains)**; abandoned per network rules. No claims drawn from it.

## Sources

Embark (Tier-1 unless noted):
- https://embarkvet.com/ (root; product nav, process framing — Tier-2)
- https://help.embarkvet.com/hc/en-us (help center home; categories, promoted articles)
- https://help.embarkvet.com/hc/en-us/categories/360003487374-Your-Dog-s-Test-Results (results category; sections: Understanding Breed Results, Understanding Health Results, Understanding Traits, The Testing Process, Breed and Ancestry, Age Test Results, Clinical Tools, Allergy Risk Scores, Relative Finder)
- https://help.embarkvet.com/hc/en-us/articles/115000237394-How-do-I-activate-my-dog-s-test (activation flow, EM code / swab code, breeder variant)
- https://help.embarkvet.com/hc/en-us/articles/115000245994-How-do-I-interpret-my-dog-s-health-results (copies/MOI/breed relevance/at-risk language, sharing, vet geneticists)
- https://help.embarkvet.com/hc/en-us/articles/17649677460379-Who-can-access-Relative-Finder (kit gating, breeder exclusion, privacy coupling)

Wisdom Panel:
- https://www.wisdompanel.com/en-us (root; product tiers, feature surfaces — Tier-2)
- https://www.wisdompanel.com/en-us/the-process (3-step process, swab instructions, lab QC notification, sample-results link — Tier-2, process-accurate)
- https://kinship-wisdom.kustomer.help/ — help center; JS-rendered, fetch returned only "Knowledge Base" → **unreachable in practice**; account/results mechanics held at product-page depth

Basepaws:
- https://basepaws.com/ (root; products, report contents, disclaimer — Tier-2)
- https://basepaws.com/how-it-works (process steps, register kit, report delivery, "life time updates" — Tier-2; note stale-copy discrepancy below)
- https://help.basepaws.com/en-US (help home; per-product article categories; track/cancel order self-service)

Orivet:
- https://www.orivet.com/ (root; How It Works 4 steps, store model, breeder programs, sample tracker, app, FAQ list — Tier-2; single-page depth)

Research limitations:
- DNA My Dog unreachable (503 ×2). Budget pole unsampled.
- Wisdom Panel Kustomer help center JS-unreachable; Wisdom evidence is root + process page depth.
- Orivet evidence is single root page depth (includes its own How It Works + FAQ topics).
- No authenticated product screenshots/walkthroughs observed; all in-app interface claims below are from official descriptive surfaces, not from operating the products.

---

## Product A — Embark Veterinary

### Key observations (Evidence layer A unless noted)

- **Product family**: Breed + Health kit; Breed ID kit; Purebred kit; Age Test ("estimates calendar age and birthday by measuring DNA methylation"); Gut Health Test (microbiome); bundles; supplements (adjacent commerce); "Personalized Games … built from your dog's DNA".
- **Account model**: app.embarkvet.com / my.embarkvet.com account; "How do I add a dog to my account?" — the dog profile is a first-class object; profiles must exist before kit activation.
- **Activation flow (Tier-1 article)**: log in → have a dog profile → activate (app.embarkvet.com/activate or "Activate a kit") → choose kit type → enter 7–8-digit "EM code" from packaging, fallback 14-digit swab-tube code → confirm code → "return the swab as soon as possible". Separate breeder activation flow; separate vet flow ("How do I activate my patient's test?"). Failure mode exists: "I forgot to activate the test. What now?"
- **Sample logistics**: cheek swab; "All Embark tests include a pre-paid mailer for US customers"; separate US / non-US mailing instructions; "Can my dogs contaminate each other's swabs?" — multi-dog contamination guidance; "Have you received my dog's sample?" — sample-status tracking; lab holiday schedules published (lab is a real physical operation).
- **Results surfaces (help taxonomy)**: Understanding Breed Results (incl. "Unresolved", "Supermutt", appearance-mismatch articles); Understanding Health Results (At Risk / At Increased Risk / Carrier / Notable); Understanding Traits (incl. "wolfiness score", trait genotypes, coat colors); The Testing Process; Breed and Ancestry; Age Test Results; Clinical Tools (ALT activity); Allergy Risk Scores (calculated scores with explicit "not a certainty" caveats); Relative Finder.
- **Results are evolving**: "Will you update my dog's results as you add new breeds to your panel?" and pedigree-submission article — the results record is maintained over time, not a static one-shot PDF.
- **Health interpretation (Tier-1 article)**: variant/genotype/phenotype vocabulary; zero copies = "clear"; one copy = "carrier"; two copies; modes of inheritance (autosomal recessive, dominant, codominant/additive, X-linked; X-chromosome inactivation; incomplete penetrance); breed relevance ("this genetic variant is not likely to increase risk… / is associated with increased risk… / we do not know whether…"); "genetic testing is not a clinical diagnosis"; "at-risk" preferred over "affected"; recommend speaking with the veterinarian; results downloadable/printable and shareable; Embark veterinary geneticists available to owner and vet.
- **Relative Finder (Tier-1 article)**: available for Breed + Health / Purebred / Breed ID kits; **breeder kits/accounts excluded**; if breed preferences set private → auto opt-out of Relative Finder (privacy coupling); messaging DNA relatives; relatives list changes over time ("Why did my dog's Relatives list change?"); cross-visibility article ("showing up in another dog's list…"); Matchmaker exists for breeder pairing (related-article evidence).
- **Breeder line**: breeder kits, Litter Package, genetic COI, Coat Color Calculator / Pair Predictor, DNA health summary report; breeder-specific help category.
- **Vet line**: "Embark for Veterinarians" kit product; patient-test activation article.
- **Shelter/rescue program**: wholesale pricing for shelters ("Long Stay, No Longer" initiative).
- **App**: iOS/Android apps.

## Product B — Wisdom Panel

### Key observations

- **Product family (Tier-2)**: Premium / Essential / Breed Discovery (dogs); Complete for Cats. Tiers differ by scope: breed-only vs breed + health vs + behavior; "Genetic consult for 'at risk' health findings" included in higher tiers.
- **Result domains (product pages)**: Breed Mix (430+ breeds claimed); Relatives ("message them, compare DNA results, view photos"); Health (265+ health tests claimed); Traits & Behavior (behavior tendencies: anxiety, sociability, weight management).
- **Process (Tier-2 "The Process")**: 1) swab cheek ≥15s, avoid debris, dry ≥5 min, wait ≥2h after meal; 2) prepaid mailer → lab: genotyping, screen against breed database, build results breakdown; 3) results in 2–3 weeks ("DNA reveal party"). **Sample-failure state explicit**: "our lab performs quality checks on every sample prior to analysis… in the unlikely event that yours don't have enough high-quality DNA for processing, we'll let you know."
- **Account**: "Activate Kit" at /app/activate; "Create an Account" — same code-linking model as Embark. Demo "View Sample Results" link exists (public sample account).
- **Research framing**: "over 5 million pets tested… largest pet health database… Every sample in our database contributes to research" — sample donation as default behavior with research framing.
- **Vet line**: "Wisdom Panel for Veterinarians" (dispenser-style packaging shown). **Breeder line**: Optimal Selection (separate brand/site, dog + cat). **Business line**: business.wisdompanel.com.
- **Breed library**: browsable dog/cat breed encyclopedia pages (weight/height/lifespan/breed group) — content layer adjacent to results.
- **Help center**: kinship-wisdom.kustomer.help — JS-rendered; not readable in this environment (limitation recorded).

## Product C — Basepaws

### Key observations

- **Species pole**: cat-first ("we care about cats so much"); now also dogs. Products: Breed + Health Cat DNA Test (21 breeds, 64 health markers, 50 trait markers, Oral Health report, blood type); Breed + Health Dog DNA Test (330+ breeds, 280+ health markers, 30+ traits); Oral Health Test for Cats (microbiome-based dental risk); **Whole Genome Sequencing** ("100% DNA decoded", "support from genetics specialists") — the sequencing-premium pole.
- **Process (Tier-2)**: Sign up → create account and register kit online → swab ("5–10 seconds… both gums and teeth") → send (free US shipping) → "results are sent straight to your inbox in 9 to 12 weeks". Report by email + account.
- **"Life Time Updates"** listed as a benefit (reports gain content as science develops).
- **Report contents**: breed mix, health markers ("genetically predisposed to disease"), dental/oral health, traits; personalized insights.
- **Content layer**: Cat/Dog libraries (breeds, diseases, traits encyclopedias); blog; research program page.
- **Vet line**: "For Veterinarians" page.
- **Disclaimer**: "provided for educational purposes only… not intended to replace discussions with an animal healthcare professional."
- **Help center (Gorgias)**: per-product article categories (Cat DNA test 10 articles; WGS; Oral; More FAQs); self-service: track order, cancel order, report issue; my.basepaws.com login.
- **Data-quality note**: the how-it-works page's "What will I find out" block contains copy that contradicts the product pages (says "350+ breeds" and lists "Relatives" — textually near-identical to Wisdom Panel's marketing copy; cat product page says 21 breeds and does not list relatives). Treated as **stale template copy**: relatives matching NOT counted as confirmed for Basepaws. Recorded as uncertainty.

## Product D — Orivet

### Key observations

- **Audience pole**: breeder-first ("Your Breeding Program"), with Pet Owner and Veterinarian segments; tagline "Predict & Protect".
- **Store model (differs from boxed-kit retailers)**: 414+ tests; single-condition tests; Health & Trait Panels (Full Breed Profiles); **Parentage Verification** ("DNA Fingerprint / Profile… compares your litter's DNA directly against the dam and sire… meeting kennel club and registry requirements"); multipacks (10-pack); vet SKUs (Genopet VET / VET+).
- **Process (root-page How It Works)**: 1) order kit online (arrives ≤5 business days); 2) **activate**: "Log in to your Orivet account and activate your kit by linking the swab barcode to your chosen test"; 3) collect sample per guide, post with reply-paid envelope; 4) results "in your breeder portal" — lab turnaround guarantee: results within 28 business days of sample receipt or money back.
- **Sample tracking**: dedicated "Track Your Samples" tool; live tracking of kit delivery and sample progress (web + app).
- **App**: manage animals + results + breeding records anywhere.
- **Breeder ecosystem**: Responsible Breeder Program (verified badge + global breeders directory listing), Breeder Loyalty Program (points per test).
- **Results sharing**: FAQ topic "Can I share my results with my vet, pet owner or fellow breeder?" — sharing across audiences.
- **Consolidation**: "Paw Print Genetics merger" notice — the professional-genetics pole is consolidating.
- FAQ topics confirming scale operation: "Can I test multiple dogs from my breeding program? Yes… order tests in bulk, manage multiple animals from a single account, access all results in one place through the Orivet app or online portal."

## Product E — DNA My Dog

- Unreachable (503 ×2 on dnamydog.com and www.dnamydog.com). **No observations. No claims.** Known in-market as a budget consumer breed-test brand; absence from this sample is a recorded limitation only.

---

## Cross-product Comparison

| Aspect | Embark | Wisdom Panel | Basepaws | Orivet |
|---|---|---|---|---|
| Primary audience | consumer owners (breeder/vet as separate lines) | consumer owners (breeder brand separate; vet line) | cat-first consumers (+dogs) | breeders first; owners/vets second |
| Species | dogs | dogs + cats | cats (dogs second) | dogs + cats |
| Purchase model | boxed kits, tiered | boxed kits, tiered | boxed kits incl. WGS premium | store of individual tests, panels, multipacks |
| Account + tested-animal profile | yes (dog profile required pre-activation) | yes (activate/create account) | yes (sign up → register kit) | yes (account links barcode to test) |
| Kit activation | code entry (EM code / swab code) | code activation page | register kit online | swab barcode → chosen test |
| Sample type | cheek swab | cheek swab | oral swab (gums + teeth) | swab (per collection guide) |
| Mail-in | prepaid mailer (US) | prepaid mailer | free US shipping | reply-paid envelope |
| Lab QC / sample failure | contamination guidance; status tracking | QC every sample; notify on insufficiency | implied by per-product help | turnaround guarantee implies standard flow |
| Results delivery | account dashboard (+app) | account + app | email + account | breeder portal + app |
| Breed/ancestry results | yes | yes | yes | yes |
| Health-risk results | yes, deep interpretation model | yes, tiered depth | yes (markers) | yes (panels/single tests) |
| Traits | yes | yes | yes | yes |
| Relatives / kinship | yes (kit-gated, privacy-coupled) | yes (message/compare/photos) | unconfirmed (stale copy) | no (parentage testing instead) |
| Parentage verification | FAQ exists (related-article) | no evidence | no | yes, registry-oriented core |
| Results updated over time | yes (panel expansion, pedigree submission) | implied (database/research framing) | "life time updates" | research programs |
| Vet handoff | download/share + vet geneticists | genetic consult (tiered) | disclaimer + vet page | share with vet; vet SKUs |
| Extra test types | age (methylation), gut microbiome, allergy risk | behavior tests | oral microbiome, WGS, blood type | single-condition tests, parentage |
| Adjacent commerce | supplements, games, insurance | — | merchandise, fitness plan | loyalty program |
| Help center | Zendesk (Tier-1) | Kustomer (JS-unreachable) | Gorgias (Tier-1 home) | FAQ on root page |

Stable cross-product commonalities (Evidence B): account + tested-animal profile; kit activation linking physical code to animal + test; owner-collected at-home sample; mail-in to operator's lab; lab QC with a failure/notify state; digital results attached to the animal; breed + health + traits result domains; results usable/sharable for veterinary care; results/content evolving over time; multi-audience structure (owner / breeder / vet).

---

## Canonical Model (four-level abstraction)

### L0 — Defining Invariant

Four jointly-held structures. Remove any one and the product stops being a Pet DNA Analysis Platform:

1. **The tested pet as the unit of record** — an individually identified animal (profile) under a customer account; the test and all findings attach to that animal, not to an anonymous order. Remove → anonymous lab-order tracking or a pet CRM.
2. **The owner-collected at-home sample loop** — a purchaseable test kit, activation linking a physical code to the animal, collection by the animal's caretaker at home, mail-in to the operator's lab, lab analysis. The software tracks this physical lifecycle. Remove (vet collects in clinic) → veterinary/clinical diagnostics territory.
3. **The genetic results of record for the animal** — a persistent record of the animal's DNA-derived findings held in the platform and attached to the animal's profile; delivered to the customer; not a one-time consumable. Remove → kit commerce with no deliverable.
4. **Interpretation of raw genotype into owner-actionable findings in the animal's context** — breed/ancestry composition, inherited health risk (copy state + inheritance mode + breed relevance), trait findings; risk-framed, explicitly not a clinical diagnosis. Remove → raw sequencing data service.

Jointly-held load-bearing checks:
- 1 alone = pet profile/CRM
- 2 without 1 = anonymous lab order tracking
- 3 without 1+2 = genetics content site
- 4 without 1–3 = genetic encyclopedia/advice content
- 1+2 without 3+4 = paid sample mailing with no deliverable
- 1+3 without 2 = clinical-genetics results portal (vet-collected territory)
- 2+3 without 1 = anonymous sequencing service

### L1 — Common Mature Structure (evidence B unless noted)

- Customer account + pet profile (photo, name, breed guess, age/weight as declared) as the container
- Interactive breed-composition breakdown (percentages, breed detail pages)
- Health-result cards with per-variant state (clear / carrier / at-risk) and explanation
- Trait reports (coat, physical features)
- Kit code activation step (distinct, user-performed, failure modes documented)
- Sample status tracking (registered → sample received → in lab → results ready)
- Downloadable / printable / shareable results (PDF) for veterinary use
- Mobile app companion
- Email/notification on milestones (sample received, results ready)
- Breed/condition/trait reference libraries (encyclopedic content)
- Upgrade path between test tiers (add health/traits post-hoc)
- Re-test / resample path when QC fails
- Help center / support
- Research-participation framing (samples feeding a growing database)

### L2 — Variant / Optional Structure

- Species focus (dog / cat / multi-species lines)
- Audience pole (consumer-first vs breeder-first vs dual; separate breeder brands)
- Relatives/kinship matching + owner-to-owner messaging (2/4 confirmed; Basepaws unconfirmed; Orivet replaces with parentage)
- Parentage verification + registry/kennel-club documentation (breeder pole)
- Breeder tooling depth: litter packages, genetic COI, pair prediction/matchmaking, breeder directories, loyalty programs
- Extra test types: age estimation (methylation), gut/oral microbiome, allergy-risk scores, blood type, behavior tendency
- Genetic consult services (bundled or available)
- Region structure (separate US/UK storefronts; shipping/consent differences)
- Turnaround guarantees (money-back)
- Shelter/rescue program pricing
- Adjacent commerce (supplements, insurance referral, merchandise, games, fitness plans) — drift surface, not identity
- Results delivered as physical mail in earlier generations (digital/account is the current common form, not the invariant)

### L3 — Vendor-specific (kept out of the final document)

Embark: EM codes / swab codes, "Supermutt", "Unresolved", "wolfiness score", Matchmaker, ALT Activity clinical tool, "Long Stay, No Longer", personalized games.
Wisdom Panel: tier names (Premium/Essential/Breed Discovery/Complete), 430+/265+/5M+ claims, Banfield collaboration framing, Optimal Selection brand, Kustomer help stack.
Basepaws: oral-health microbiome test framing, WGS "100% decoded", genetics-specialist support, stale how-it-works copy, Gorgias help stack.
Orivet: Geno Pet / Genopet VET / My CatScan product names, 28-business-day guarantee, Responsible Breeder Program, loyalty points math, Paw Print Genetics merger, breeder-portal terminology.

### Anti-overfitting notes

- **Cheek swab is NOT definitional** — Basepaws samples gums+teeth; microbiome tests sample differently. Invariant is "owner-collected at-home sample"; swab is the common implementation.
- **Breed identification is NOT definitional** — Orivet sells single-condition health tests and parentage-only DNA fingerprints in-type; the invariant is "DNA-derived findings", of which breed composition is the most common content.
- **Relatives matching is NOT definitional** — confirmed at 2/4, unconfirmed at 1/4, explicitly absent/replaced at the breeder pole.
- **Digital-first results delivery is NOT definitional** — earlier generations delivered paper reports; the invariant is a persistent results record delivered to the customer.
- **The modern e-commerce shop is NOT definitional** — order-by-form/mail generations satisfy the core without a web store.

---

## Boundary Findings

1. **vs Pet Health Application (unprocessed sibling)** — shared vocabulary (pet profile, health), different center of gravity: DNA platform's unit of record is lab-derived genetic findings for the animal, produced once and maintained; Pet Health Application's unit of record is the animal's ongoing health state (logs, reminders, vet records) with no lab. DNA platforms drift toward health content (fitness plans, games); health apps do not run a lab loop. **JOINT-REVIEW FLAG for the pet-health-application pass** (expected clean, mirroring the pet-adoption pass's flag).
2. **vs Veterinary Practice Management / veterinary diagnostics** — clinic-operated, vet-collected samples, clinical diagnosis vs consumer at-home risk assessment; DNA platforms explicitly disclaim clinical diagnosis and route follow-up to the vet. A vet-ordered patient test (Embark vet line) still uses the owner-collected kit loop — the platform part stays in-type; the clinic system does not.
3. **vs E-commerce Platform** — kit sales are the acquisition surface; the world's center is the test lifecycle + results record. A store without the sample→lab→results loop is just a store.
4. **vs human DTC genomics (outside directory)** — same skeleton (kit → lab → interpreted genome), different subject; the pet subject + caretaker collection + veterinary handoff + breeder/registry semantics are the discriminators. Recorded because the structural rhyme is strong enough to cause confusion.
5. **vs Animal Shelter Management / adoption** — some DNA products run shelter programs (bulk pricing), but no custody or placement structures exist in the DNA platform; the shelter relationship is a pricing/distribution channel.
6. **Removal tests**: remove the lab/sample loop → pet content + profile app; remove the animal-of-record → human genomics or anonymous lab; remove interpretation → raw data service; remove results persistence → one-shot report email (thin ancestor, still recognizable — the persistence is what makes it a platform).

## Historical / Market-Sample Check

- **Early-2000s DTC dog breed tests** (the DNA My Dog / BioPet generation): order form or early web store, kit mailed, owner swabs, results as a mailed/paper breed report — satisfies all four legs at analog level (results record was paper; no health panels, no relatives, no apps). Confirms breed-only + paper results still in-type.
- **Kennel-club parentage DNA programs** (registry DNA profiling): kit mailed to breeder/owner, swab, mail to lab, parentage-qualified result recorded against the animal's registration — satisfies the four legs with parentage as the finding. Confirms the breeder/registry pole is not a new invention.
- **Vet-collected genetic diagnostics** — correctly excluded (fails leg 2): sample collected by a professional in a clinical context.
- **Human DTC genomics** — correctly excluded (fails leg 1).
- Check passed: the definition is not over-fitted to the modern app-era, US-market, health-panel-rich implementation.

## Uncertainties

- Basepaws relatives feature: unconfirmed; site copy contradicts itself (stale template copy suspected). Held at "common in some products", not asserted for Basepaws.
- Wisdom Panel account/results mechanics: help center unreachable; held at product-page depth. No precise claims about its in-app states.
- Orivet breeder portal internals (sample tracker UX, portal structure): root-page depth only.
- Precise numeric claims (breed counts, marker counts, turnaround windows, database sizes) are vendor-claimed and vary; they are recorded here but NOT carried into the final document.
- DNA My Dog (budget pole) unsampled; price-segment spread is asserted only from the sampled four.
- Relative-finder cross-visibility mechanics (why a dog appears in another's list) not fully evidenced from the fetched article.

## Final Synthesis

A Pet DNA Analysis Platform is the owner-facing system of record for at-home pet genetic testing: the tested animal is the unit of record; the platform sells/registers test kits, links each kit to an animal via activation, tracks the owner-collected sample through mail-in and lab analysis, and delivers a persistent, interpreted genetic results record — breed/ancestry, inherited health risk, traits — that the owner can act on, share with a veterinarian, and that evolves as the science and reference databases grow. Breeder-facing tooling (parentage, pairing, registries), extra test types (age, microbiome), relatives matching, and adjacent commerce are common but variant structures. The defining seam is the owner-collected-sample + lab loop (vs health apps, which have no lab) and the animal-of-record (vs human genomics) and risk-not-diagnosis framing (vs clinical diagnostics).
