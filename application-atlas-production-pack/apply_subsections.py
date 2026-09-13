#!/usr/bin/env python3
"""Apply subsection proposals to DIRECTORY.md (domains 06-29).
Inserts ### NN.MM subsection blocks under each ## NN domain, regrouping leaves.
Leaf order within each subsection preserved from original order."""
import json, os, re, sys

PACK = os.path.dirname(os.path.abspath(__file__))
DIR_PATH = os.path.join(PACK, "DIRECTORY.md")
PROPOSAL = json.load(open(os.path.join(PACK, "atlas", "subsections-proposal.json")))

text = open(DIR_PATH, encoding="utf-8").read()
lines = text.splitlines(keepends=False)

top_re = re.compile(r"^##\s+(\d+)\s+(.+)$")

# pass 1: locate domain blocks (start index of "## NN", end before next "## " or "---")
blocks = []  # (top_id, start_idx, end_idx_exclusive)
for i, ln in enumerate(lines):
    m = top_re.match(ln)
    if m:
        blocks.append([m.group(1), i, None])
for j, b in enumerate(blocks):
    end = len(lines)
    for k in range(b[1] + 1, len(lines)):
        if top_re.match(lines[k]) or lines[k].strip() == "---":
            end = k
            break
    b[2] = end

by_top = {b[0]: (b[1], b[2]) for b in blocks}
missing = [t for t in PROPOSAL if t not in by_top]
if missing:
    sys.exit(f"domains not found in DIRECTORY.md: {missing}")

# pass 2: rewrite each domain block (process in reverse to keep indices valid)
for top in sorted(PROPOSAL, key=lambda t: -int(t)):
    start, end = by_top[top]
    header = lines[start]
    body = lines[start + 1:end]
    # collect leaf lines with original order; keep other lines (prose) in header area
    leaf_names = []
    leaf_lines = []
    for ln in body:
        if ln.startswith("- ") and not ln.startswith("- ["):
            leaf_names.append(ln[2:].strip())
            leaf_lines.append(ln)
    all_names = [ln[2:].strip() for ln in leaf_lines]
    proposed = [n for s in PROPOSAL[top]["subsections"] for n in s["leaves"]]
    if sorted(proposed) != sorted(all_names):
        miss = set(all_names) - set(proposed)
        extra = set(proposed) - set(all_names)
        sys.exit(f"{top}: MECE fail missing={list(miss)[:3]} extra={list(extra)[:3]}")
    # interleave: rebuild body as prose-preface + subsection blocks
    # find where leaves start in body (first leaf line)
    first_leaf = next(i for i, ln in enumerate(body) if ln in leaf_lines)
    pre = body[:first_leaf]
    # build sub blocks with original member order
    new_body = list(pre)
    for i, sub in enumerate(PROPOSAL[top]["subsections"], 1):
        new_body.append(f"### {top}.{i:02d} {sub['name']}")
        pos_of = {ln[2:].strip(): p for p, ln in enumerate(leaf_lines)}
        members = sorted((pos_of[x], x) for x in sub["leaves"] if x in pos_of)
        for p, _ in members:
            new_body.append(leaf_lines[p])
        new_body.append("")
    # trim trailing blank inside block, keep one before separator
    while new_body and new_body[-1] == "":
        new_body.pop()
    lines[start + 1:end] = new_body + [""]

open(DIR_PATH, "w", encoding="utf-8").write("\n".join(lines) + "\n")
n_subs = sum(len(PROPOSAL[t]["subsections"]) for t in PROPOSAL)
print(f"DIRECTORY.md updated: {len(PROPOSAL)} domains, {n_subs} subsections")
