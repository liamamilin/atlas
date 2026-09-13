#!/usr/bin/env python3
"""Draft leaf structural lint.

Validates a leaf document (drafts/<slug>.md or applications/<slug>.md) against
the structure export_atlas.py can parse. Exit 0 = lint clean, 1 = errors.

Usage: python3 leaf_lint.py <file.md> [--json]
"""
import json
from pathlib import Path
import os
import re
import sys

from atlas_runtime import PACK as DATA_PACK
PACK = str(DATA_PACK)
RESEARCH = os.path.join(PACK, "research")

SECTION_RE = re.compile(r"^##\s+(.+)$", re.M)
REL_ROW3_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", re.M)
REL_ROW2_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", re.M)
FRONT_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)

REQUIRED = [
    ("overview", ("overview",)),
    ("users", ("users",)),
    ("core model", ("core model",)),
    ("how it works", ("how it works",)),
    ("interfaces", ("interfaces",)),
    ("rules", ("important rules", "rules")),
    ("variants", ("variants", "one structure")),
    ("related", ("related",)),
    ("products", ("representative products", "products")),
    ("sources", ("sources",)),
]

REQUIRED_FRONT = ["slug", "name", "name_zh", "desc", "source", "status", "created", "engine"]
MIN_BODY = 12000
MIN_PRODUCTS = 4
MIN_RELATED = 6
MIN_H3 = 10


def parse_front(text):
    m = FRONT_RE.match(text)
    if not m:
        return {}, text
    front = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            front[k.strip()] = v.strip()
    return front, text[m.end():]


def lint(path):
    errors, warnings = [], []
    raw = Path(path).read_text(encoding="utf-8")
    front, body = parse_front(raw)

    for k in REQUIRED_FRONT:
        if front and not front.get(k):
            errors.append(f"frontmatter 缺 {k}")

    m1 = re.match(r"^#\s+(.+)$", body.strip(), re.M)
    if not m1:
        errors.append("缺 H1 标题")
    title = m1.group(1).strip() if m1 else ""
    if front.get("name") and title and title.lower() != front["name"].lower():
        errors.append(f"H1「{title}」与 frontmatter name「{front['name']}」不一致")

    parts = SECTION_RE.split(body)
    sections = {}
    for i in range(1, len(parts) - 1, 2):
        sections[parts[i].strip().lower()] = parts[i + 1]

    def grab(*names):
        for n in names:
            for k, v in sections.items():
                if k.startswith(n):
                    return v
        return ""

    for label, names in REQUIRED:
        if not grab(*names).strip():
            errors.append(f"缺 H2 节: {label}")

    core = grab("core model")
    if core:
        has_dc = bool(re.search(r"###\s+.*defining", core, re.I))
        paras = [p for p in core.split("\n\n") if len(p.strip()) > 80]
        if not has_dc:
            if paras:
                warnings.append("Core Model 无「Defining Core」小节（export 将回退首段）")
            else:
                errors.append("Core Model 内缺「The Defining Core」小节且无可回退首段")
    if not re.search(r"```", grab("overview") + "\n" + core):
        errors.append("Overview/Core Model 内缺结构树代码块")

    related = grab("related")
    rows = [r for r in REL_ROW3_RE.finditer(related)
            if r.group(1).strip() not in ("Application Type", "Type", "---", "Distinction")]
    rows += [r for r in REL_ROW2_RE.finditer(related)
             if r.group(1).strip() not in ("Application Type", "Type", "---", "Distinction")
             and r.group(2).strip() != "---"]
    if len(rows) < MIN_RELATED:
        errors.append(f"Related 表仅 {len(rows)} 行 (<{MIN_RELATED})")

    products = grab("representative products", "products")
    items = len(re.findall(r"^\s*[-*]\s+\S", products, re.M))
    if items < MIN_PRODUCTS:
        errors.append(f"Representative Products 仅 {items} 项 (<{MIN_PRODUCTS})")

    n_h3 = len(re.findall(r"^###\s", body, re.M))
    if n_h3 < MIN_H3:
        errors.append(f"仅 {n_h3} 个 H3 小节 (<{MIN_H3})")

    if len(body) < MIN_BODY:
        errors.append(f"正文 {len(body)} 字符 (<{MIN_BODY})")

    slug = front.get("slug") or os.path.basename(path)[:-3]
    rp = next((p for p in (os.path.join(RESEARCH, slug + ".md"),
                           os.path.join(os.path.dirname(path), slug + ".research.md"))
               if os.path.exists(p)), None)
    if not rp:
        warnings.append("无 Boundary Findings/Uncertainties 文件（建议补 research/<slug>.md 或 drafts/<slug>.research.md）")
    else:
        rt = Path(rp).read_text(encoding="utf-8")
        if "Boundary Findings" not in rt:
            warnings.append("research 文件缺 Boundary Findings")
        if "Uncertainties" not in rt:
            warnings.append("research 文件缺 Uncertainties")

    return {"file": os.path.relpath(path, PACK), "ok": not errors,
            "errors": errors, "warnings": warnings,
            "size": len(body), "title": title}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    if "--dir" in sys.argv:
        d = sys.argv[sys.argv.index("--dir") + 1]
        paths = sorted(os.path.join(d, f) for f in os.listdir(d) if f.endswith(".md"))
    else:
        paths = [f for f in sys.argv[1:] if not f.startswith("-")]
    results = [lint(f) for f in paths]
    if "--json" in sys.argv:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for r in results:
            tag = "PASS" if r["ok"] else "FAIL"
            print(f"[{tag}] {r['file']} ({r['size']} 字符)")
            for e in r["errors"]:
                print(f"  ERROR  {e}")
            for w in r["warnings"]:
                print(f"  warn   {w}")
        n_fail = sum(1 for r in results if not r["ok"])
        print(f"--- {len(results)-n_fail} PASS / {n_fail} FAIL")
    sys.exit(0 if all(r["ok"] for r in results) else 1)
