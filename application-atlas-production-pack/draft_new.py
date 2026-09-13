#!/usr/bin/env python3
"""Create a draft leaf: uniqueness check -> free vector collision check ->
write drafts/<slug>.md (frontmatter + placeholder) -> pluggable engine writes
full body -> leaf_lint gates it.

Usage:
  python3 draft_new.py --name-zh "命令行记账工具" --name "CLI Accounting Tool" \
      --desc "单机命令行复式记账" [--link https://...] [--slug ...] \
      [--engine opencode] [--model provider/model] [--force] [--no-generate]

Exit 0 = draft ready (status: draft), 3 = lint failed (status: failed),
2 = rejected (duplicate slug / high collision without --force).
"""
import argparse
import datetime
import json
import os
import re
import sys

PACK = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PACK)
from leaf_lint import lint

DRAFTS = os.path.join(PACK, "drafts")
PROMPT = os.path.join(PACK, "drafts_prompt.md")
WORKDIR = os.path.dirname(PACK)
ENGINES_CFG = os.path.join(DRAFTS, "engines.json")
HIGH_SIM = 0.80


def slugify(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return re.sub(r"-{2,}", "-", s)


def slug_taken(slug):
    if os.path.exists(os.path.join(DRAFTS, slug + ".md")):
        return "draft"
    if os.path.exists(os.path.join(PACK, "applications", slug + ".md")):
        return "corpus"
    return None


def collision(desc):
    """Free vector top-5 against the corpus (no LLM). Returns [(slug, name_zh, sim)]."""
    try:
        from classify import candidates
        import numpy as np
        pool, sims = candidates(desc, k=10)
        return [(s, float(sims[i])) for i, s in enumerate(pool[:5])]
    except Exception as e:
        print(f"[collision check unavailable: {e}]", file=sys.stderr)
        return []


def write_draft(slug, idea, engine, source):
    now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
    fm = (f"---\nslug: {slug}\nname: {idea['name']}\nname_zh: {idea.get('name_zh', '')}\n"
          f"desc: {idea['desc']}\nlink: {idea.get('link') or ''}\n"
          f"name_source: {idea.get('name_source', 'user')}\n"
          f"source: {source}\nstatus: generating\nengine: {engine}\ncreated: {now}\n---\n")
    open(os.path.join(DRAFTS, slug + ".md"), "w", encoding="utf-8").write(fm)


def unique_slug(base):
    slug, i = base, 2
    while slug_taken(slug):
        slug = f"{base}-{i}"
        i += 1
    return slug


def rename_draft(old, new):
    for suffix in (".md", ".research.md", ".zh.json", ".opencode.log", ".identity.json"):
        p = os.path.join(DRAFTS, old + suffix)
        if os.path.exists(p):
            os.rename(p, os.path.join(DRAFTS, new + suffix))
    p = os.path.join(DRAFTS, new + ".md")
    text = open(p, encoding="utf-8").read()
    open(p, "w", encoding="utf-8").write(
        re.sub(r"^slug: .*$", f"slug: {new}", text, count=1, flags=re.M))


def refresh_front(slug, status, extra=""):
    p = os.path.join(DRAFTS, slug + ".md")
    text = open(p, encoding="utf-8").read()
    text = re.sub(r"^status: .*$", f"status: {status}", text, count=1, flags=re.M)
    if extra:
        text = re.sub(r"^---\n", f"---\n{extra}\n", text, count=1)
    open(p, "w", encoding="utf-8").write(text)


def assemble(slug):
    """Engine wrote drafts/<slug>.body.md: attach it after frontmatter, drop temp file."""
    p = os.path.join(DRAFTS, slug + ".md")
    bp = os.path.join(DRAFTS, slug + ".body.md")
    if not os.path.exists(bp):
        return False
    text = open(p, encoding="utf-8").read()
    m = re.match(r"\A---\n.*?\n---\n", text, re.S)
    body = open(bp, encoding="utf-8").read().strip()
    open(p, "w", encoding="utf-8").write((m.group(0) if m else "") + body + "\n")
    os.remove(bp)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--name-zh", default="")
    ap.add_argument("--desc", required=True)
    ap.add_argument("--link", default="")
    ap.add_argument("--slug", default="")
    ap.add_argument("--engine", default="")
    ap.add_argument("--model", default=None)
    ap.add_argument("--source", default="human")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--no-generate", action="store_true")
    args = ap.parse_args()

    cfg = json.load(open(ENGINES_CFG)) if os.path.exists(ENGINES_CFG) else {}
    engine_name = args.engine or cfg.get("engine", "opencode")
    model = args.model if args.model is not None else cfg.get("model", "")

    slug = args.slug or slugify(args.name)
    if not slug:
        print("无法生成 slug，请用 --slug 指定")
        sys.exit(2)
    taken = slug_taken(slug)
    if taken:
        print(f"拒绝：slug「{slug}」已存在于{ '草稿区' if taken == 'draft' else '正式语料' }")
        sys.exit(2)

    idea = {"slug": slug, "name": args.name, "name_zh": args.name_zh or args.name,
            "desc": args.desc, "link": args.link}

    print("== 撞车检查（向量 top-5，免费）==")
    for s, sim in collision(args.desc):
        flag = "  <-- 高相似" if sim >= HIGH_SIM else ""
        print(f"  {sim:.3f}  {s}{flag}")
    top = collision(args.desc)
    if top and top[0][1] >= HIGH_SIM and not args.force:
        print(f"拒绝：与正式语料最高相似度 {top[0][1]:.3f} ≥ {HIGH_SIM}；如确认要建，加 --force")
        sys.exit(2)

    write_draft(slug, idea, engine_name, args.source)
    print(f"草稿骨架已写入 drafts/{slug}.md (status: generating)")

    if args.no_generate:
        refresh_front(slug, "draft")
        print("跳过生成（--no-generate），status: draft（空正文，待手动填写）")
        return

    from drafts_engines import get_engine
    eng, _ = get_engine(engine_name, model)
    log_path = os.path.join(DRAFTS, slug + ".opencode.log")
    print(f"== 引擎 {eng.name} 生成中（日志: {os.path.relpath(log_path, PACK)}）==")
    ok = eng.generate(idea, PROMPT, WORKDIR, log_path, model=model)
    if not ok or not assemble(slug):
        refresh_front(slug, "failed", extra="lint: engine failed, see .opencode.log")
        print("引擎执行失败，status: failed")
        sys.exit(3)

    r = lint(os.path.join(DRAFTS, slug + ".md"))
    print(f"== lint: {'PASS' if r['ok'] else 'FAIL'} ({r['size']} 字符) ==")
    for e in r["errors"]:
        print(f"  ERROR  {e}")
    for w in r["warnings"]:
        print(f"  warn   {w}")
    refresh_front(slug, "draft" if r["ok"] else "failed",
                  extra=f"lint_errors: {len(r['errors'])}\nlint_warnings: {len(r['warnings'])}")
    sys.exit(0 if r["ok"] else 3)


if __name__ == "__main__":
    main()
