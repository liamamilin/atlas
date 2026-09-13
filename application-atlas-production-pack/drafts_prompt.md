# Leaf draft prompt template (engine-agnostic)

渲染方式：将 {{KEY}} 占位符替换为实际值后，作为完整 prompt 交给写作引擎。
本文件不含任何引擎特定语法；各引擎 adapter 负责传输方式（CLI 参数 / stdin / API body）。

---

You are a leaf writer for the Application Atlas corpus (a bilingual encyclopedia of
1804+ software application types, each defining what the Type fundamentally is, how
it works, where its boundaries are, and which real products embody it).

Write ONE complete new leaf document.

## The idea (from the human submitter)

- Name (English): {{NAME}}
- Name (Chinese, display hint only — body must be English): {{NAME_ZH}}
- One-line thesis: {{DESC}}
- Research starting link (if provided, fetch it first; if unreachable, work from
  your own knowledge and say so in Sources): {{LINK}}
- Suggested slug: {{SLUG}}

## Identity (settle this FIRST, after initial research, BEFORE writing the body)

The body must be written about the Type as your research establishes it — the
supplied name/thesis may be a shallow guess and MUST yield to evidence.

- If NAME above is "(调研后定名)" (a placeholder), the human did not name the
  Type: after your research, decide the identity yourself — an English Type name
  of 2-5 Title Case words (a category, not a product), a Chinese name (≤12
  characters), and a one-line Chinese thesis (≤60 characters, style:
  「形态+核心机制+边界说明」，e.g. 单机命令行复式记账工具（ledger/hledger 一类：
  纯文本账本、无 GUI）).
- If NAME is a real name, KEEP it unchanged; you may refine the thesis only if
  research proves it factually wrong (explain in Sources/Uncertainties).

Then write `/Users/milin/2026/软件开发/application-atlas/application-atlas-production-pack/drafts/{{SLUG}}.identity.json`
(a third file; JSON object, exactly one of):
1. {"name":"...","name_zh":"...","desc":"..."}   — the settled identity
2. {"verdict":"same","best":"<existing-slug>","reason":"≤80字"}   — proposal duplicates an existing Type
3. {"verdict":"variant","best":"<existing-slug>","reason":"≤80字"} — proposal is a true sub-variant, not a new Type

If you write verdict 2 or 3, write NOTHING else (no body, no research file) and
stop. Otherwise proceed to the body using the final name from case 1.

## Required reading (in order, before writing)

1. `/Users/milin/2026/软件开发/application-atlas/application-atlas-production-pack/WRITING_GUIDE.md`
   — the corpus writing methodology. Follow it exactly (section set, L0 minimal
   definition discipline, evidence grading, boundary analysis).
2. Read these exemplar leaves to calibrate depth, tone, and structure (do NOT copy
   their content): `/Users/milin/2026/软件开发/application-atlas/application-atlas-production-pack/applications/{{EXEMPLAR1}}.md`
   and `/Users/milin/2026/软件开发/application-atlas/application-atlas-production-pack/applications/{{EXEMPLAR2}}.md`
3. Boundary calibration: use the `application-atlas` MCP tools (search_similar /
   get_leaf) to find the 3-5 nearest existing leaf types. Your "Related Application
   Types" table MUST cover these neighbors with concrete, testable distinctions
   (the "remove X → becomes Y" style). Do not write a leaf that duplicates an
   existing one — if research reveals the idea is already covered, stop and report
   that instead of writing.

## Output (exactly three files, nothing else)

The identity JSON from the Identity step above, plus the two files below.
If identity.json was a verdict, it is the ONLY file you write.

## Quality bar (calibrated against the 1804-leaf corpus; a lint gate enforces it)

- Length 16000-22000 characters; ≥15 `###` subsections across the document
  (Interfaces and How It Works carry most of the depth — enumerate concrete
  surfaces, workflows, and capability tiers, not generic prose).
- "Related Application Types" table: ≥8 rows, every row a concrete testable
  distinction ("remove X → becomes Y" style).
- "Representative Products": 4-6 REAL products. **Verify each product's URL by
  fetching it during research.** If a product cannot be verified online, DROP it —
  never invent names, companies, or URLs. A dead or wrong link is a corpus defect.
  Community hubs (e.g. official ecosystem lists) are good sources of real names.
- Sources: cite every URL you actually consulted, with the research date, and
  state explicitly what you could NOT verify.
- English throughout (the corpus source language); the Chinese display layer is
  generated separately by the translation pipeline.

1. `/Users/milin/2026/软件开发/application-atlas/application-atlas-production-pack/drafts/{{SLUG}}.body.md`
   Write the complete leaf body to this NEW file (do NOT touch `{{SLUG}}.md`,
   which holds metadata; and do NOT include any frontmatter or ```yaml). Start with:
   `# {{NAME}}`
   Required H2 sections in order: Overview (with a ```text structure tree),
   Users & Context, Core Model (with "### The Defining Core" subsection, standard
   capabilities, one-structure-many-implementations), How It Works, Interfaces,
   Important Rules / Behaviors, Variants, Related Application Types (table, ≥8
   rows, 2- or 3-column), Representative Products (4-6 verified real products,
   each with a one-line "what it is + which variation it embodies" and a fetched
   URL; drop unverifiable products), Sources.
   Length 16000-22000 characters. English throughout.
2. `/Users/milin/2026/软件开发/application-atlas/application-atlas-production-pack/drafts/{{SLUG}}.research.md`
   Sections: "## Boundary Findings" (each: pair, distinguishing test, evidence
   grade) and "## Uncertainties" (honest unknowns, evidence-grade what you could).

Do not modify any other files. Do not run the atlas pipeline scripts.
When done, reply with a one-paragraph summary: the L0 invariants you settled on,
the 3 nearest neighbors and how the boundaries were drawn, and anything you could
not verify.
