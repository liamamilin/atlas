#!/usr/bin/env python3
"""Validate and promote a draft using an isolated corpus copy.
No live corpus writes occur until export, translations, embeddings and the
fixed 52-item gate all pass. Draft IDs remain stable after promotion.
"""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
from contextlib import closing

from atlas_runtime import PACK, atomic_json, atomic_write, corpus_lock, publish_files, recover_publication
from draft_new import slugify
from leaf_lint import lint, parse_front
from review_store import fingerprint, load_review, review_current, review_lock, update_review, valid_slug

CODE = Path(__file__).resolve().parent
WEB_SCRIPT = CODE.parent / "atlas-web/scripts/gen-data.py"
WEB_DATA = CODE.parent / "atlas-web/public/data"
AUX_FILES = ("translations.jsonl", "body-zh.jsonl", "rels-zh.jsonl", "section-zh.json")
STATE_FILES = ("translate-state.json", "bodyzh-state.json", "relszh-state.json")


def validate_promotion(slug, action, target, pack=PACK):
    pack = Path(pack)
    valid_slug(slug)
    path = pack / "drafts" / f"{slug}.md"
    front, body = parse_front(path.read_text())
    review = load_review(pack).get(slug, {})
    if review.get("promoted") or front.get("status") not in ("draft", "promoting"):
        raise ValueError("草稿状态不允许入库")
    result = lint(str(path))
    if result["errors"]:
        raise ValueError("lint 未通过：" + "; ".join(result["errors"]))
    if not review_current(slug, review, pack):
        raise ValueError("请先对当前草稿和当前语料完成查重")
    if action == "new" and review.get("verdict") != "new":
        raise ValueError("查重必须判定为新类型，才能新建正式叶子")
    if action == "merge" and (review.get("verdict") not in ("same", "variant") or review.get("best") != target):
        raise ValueError("合并目标必须与查重裁决一致")
    if action not in ("new", "merge"):
        raise ValueError("action 必须是 new|merge")
    final = slugify(front.get("name", ""))
    if not final:
        raise ValueError("缺少正式英文类型名")
    with closing(sqlite3.connect((pack / "atlas/atlas.sqlite").as_uri() + "?mode=ro", uri=True)) as con:
        if action == "new":
            if not con.execute("SELECT 1 FROM section WHERE id=? AND parent IS NOT NULL AND parent!=''", (target,)).fetchone():
                raise ValueError("目标子域不存在")
            if con.execute("SELECT 1 FROM leaf WHERE slug=?", (final,)).fetchone() or (pack / "applications" / f"{final}.md").exists():
                raise ValueError("正式类型已存在，不能覆盖")
            if not (pack / "drafts" / f"{slug}.research.md").exists():
                raise ValueError("新类型必须有配套研究笔记")
        elif not con.execute("SELECT 1 FROM leaf WHERE slug=?", (target,)).fetchone():
            raise ValueError("合并目标不存在")
    return front, body, final
def insert_bullet(section_id, name, directory):
    """Insert `- Name` alphabetically into the `### NN.MM ...` block of DIRECTORY.md."""
    text = Path(directory).read_text()
    lines = text.split("\n")
    start = None
    for i, l in enumerate(lines):
        if re.match(rf"^###\s+{re.escape(section_id)}\b", l):
            start = i
            break
    if start is None:
        raise RuntimeError(f"DIRECTORY.md 中找不到子域 {section_id}")
    end = start + 1
    while end < len(lines) and not re.match(r"^#{1,3}\s|^---$", lines[end]):
        end += 1
    bullets = [l for l in lines[start + 1 : end] if l.startswith("- ")]
    new = f"- {name}"
    if any(l[2:].lower() == name.lower() for l in bullets):
        return new  # idempotent: bullet already inserted by an earlier attempt
    bullets.append(new)
    bullets.sort(key=lambda s: re.sub(r"^- ", "", s).lower())
    lines[start + 1 : end] = bullets
    atomic_write(directory, "\n".join(lines))
    return new


def append_alias(into_slug, alias_name, directory, canonical_name):
    """Add ` / alias_name` to the DIRECTORY bullet of into_slug (if not present)."""
    text = Path(directory).read_text()
    lines = text.split("\n")
    for i, l in enumerate(lines):
        if l.startswith("- "):
            name = l[2:].strip()
            if name == canonical_name:
                if alias_name.lower() in name.lower():
                    return name
                lines[i] = f"- {name} / {alias_name}"
                atomic_write(directory, "\n".join(lines))
                return lines[i][2:]
    raise RuntimeError(f"DIRECTORY.md 中找不到叶子 {into_slug}")



def prepare_stage(pack, stage):
    """Copy only corpus inputs, not engine logs or unrelated experiment artifacts."""
    for name in ("applications", "research"):
        shutil.copytree(pack / name, stage / name)
    for name in ("DIRECTORY.md", "STATUS.md", "pilot_clean.json", "pilot_synthetic.json",
                 "mvp_apps.json", "mvp_apps_classified.json"):
        shutil.copy2(pack / name, stage / name)
    (stage / "atlas").mkdir()
    (stage / "logs").mkdir()
    with closing(sqlite3.connect(pack / "atlas/atlas.sqlite")) as src:
        with closing(sqlite3.connect(stage / "atlas/atlas.sqlite")) as dst:
            src.backup(dst)
    for name in AUX_FILES:
        if (pack / "atlas" / name).exists():
            shutil.copy2(pack / "atlas" / name, stage / "atlas" / name)
    # Checkpoint files are reproducible from the committed translation records.
    for source, state_name in zip(AUX_FILES[:3], STATE_FILES):
        records = {}
        path = stage / "atlas" / source
        if path.exists():
            for line in path.read_text().splitlines():
                record = json.loads(line)
                if "error" not in record:
                    records[record["slug"]] = record if source == "translations.jsonl" else "v2"
        atomic_json(stage / "atlas" / state_name, {"done": records, "failed": []})


def run_stage(stage, command):
    env = {**os.environ, "ATLAS_PACK": str(stage), "ATLAS_WEB_OUT": str(stage / "web-data")}
    print("$", " ".join(map(str, command)), flush=True)
    result = subprocess.run(command, cwd=CODE, env=env)
    if result.returncode:
        raise RuntimeError(f"{Path(command[1]).name} 执行失败（exit {result.returncode}）")


def validate_stage(stage, final=None):
    with closing(sqlite3.connect(stage / "atlas/atlas.sqlite")) as con:
        if con.execute("PRAGMA quick_check").fetchone()[0] != "ok":
            raise RuntimeError("临时数据库完整性检查失败")
        missing = con.execute("""SELECT l.slug FROM leaf l LEFT JOIN embedding e ON l.slug=e.slug
            LEFT JOIN leaf_zh_body z ON l.slug=z.slug WHERE e.slug IS NULL OR z.slug IS NULL
            OR coalesce(l.name_zh,'')='' OR coalesce(l.l0_zh,'')=''""").fetchall()
        if missing:
            raise RuntimeError(f"临时语料缺少向量或翻译：{missing[:5]}")
        slugs = {r[0] for r in con.execute("SELECT slug FROM leaf")}
        meta = json.loads((stage / "web-data/meta.json").read_text())
        if meta["leafCount"] != len(slugs):
            raise RuntimeError("网页索引数量与数据库不一致")
        if {r["slug"] for r in meta["leafIndex"]} != slugs:
            raise RuntimeError("网页索引类型与数据库不一致")
        for slug in slugs:
            if not (stage / "web-data/leaves" / f"{slug}.json").exists():
                raise RuntimeError(f"网页缺少类型详情：{slug}")
        if final and final not in slugs:
            raise RuntimeError("新类型未写入临时数据库")
        if final:
            missing_relations = con.execute("""SELECT COUNT(*) FROM relation r LEFT JOIN rel_zh z
                ON r.from_slug=z.from_slug AND r.to_name=z.to_name
                WHERE r.from_slug=? AND r.to_slug IS NOT NULL AND r.distinction!=''
                AND coalesce(z.distinction_zh,'')=''""", (final,)).fetchone()[0]
            if missing_relations:
                raise RuntimeError(f"新类型缺少 {missing_relations} 条关系翻译")


def set_status(slug, status, pack):
    path = pack / "drafts" / f"{slug}.md"
    text = re.sub(r"^status: .*$", f"status: {status}", path.read_text(), count=1, flags=re.M)
    atomic_write(path, text)


def promote(slug, action, target, pack=PACK, web_data=None, runner=None):
    pack = Path(pack)
    runner = runner or run_stage
    web_data = Path(web_data) if web_data is not None else WEB_DATA
    with corpus_lock(pack):
        recover_publication(pack)
        front, body, final = validate_promotion(slug, action, target, pack)
        original_fingerprint = fingerprint(slug, pack)
        set_status(slug, "promoting", pack)
        try:
            with tempfile.TemporaryDirectory(prefix=".staging-", dir=pack / "atlas") as temp:
                stage = Path(temp)
                prepare_stage(pack, stage)
                if action == "new":
                    (stage / "applications" / f"{final}.md").write_text(body.rstrip() + "\n")
                    shutil.copy2(pack / "drafts" / f"{slug}.research.md", stage / "research" / f"{final}.md")
                    insert_bullet(target, front["name"], stage / "DIRECTORY.md")
                else:
                    with closing(sqlite3.connect(stage / "atlas/atlas.sqlite")) as con:
                        canonical = con.execute("SELECT name FROM leaf WHERE slug=?", (target,)).fetchone()[0]
                    append_alias(target, front["name"], stage / "DIRECTORY.md", canonical)
                commands = [(CODE / "export_atlas.py",), (CODE / "translate_zh.py",),
                            (CODE / "export_atlas.py",),
                            (CODE / "translate_bodies.py", "--engine", "api"),
                            (CODE / "translate_rels.py", "--engine", "api"),
                            (CODE / "import_zh.py",), (CODE / "embed_leaves.py",), (WEB_SCRIPT,)]
                for command in commands:
                    runner(stage, [sys.executable, *map(str, command)])
                validate_stage(stage, final if action == "new" else target)
                try:
                    runner(stage, [sys.executable, str(CODE / "gate_check.py")])
                finally:
                    report = stage / "atlas/gate_summary.json"
                    if report.exists():
                        summary = json.loads(report.read_text())
                        update_review(slug, {"gate": f"{summary['accuracy']:.1%}",
                                             "gate_ok": summary["passed"]}, pack)
                # Validate the raw result ourselves; never trust an exit code or summary alone.
                from gate_check import score_rows
                items = json.loads((stage / "pilot_clean.json").read_text()) + json.loads((stage / "pilot_synthetic.json").read_text())
                _, summary = score_rows(json.loads((stage / "atlas/gate_regression.json").read_text()), items)
                update_review(slug, {"gate": f"{summary['accuracy']:.1%}", "gate_ok": summary["passed"]}, pack)
                if not summary["passed"]:
                    raise RuntimeError(f"回归未达标：{summary['accuracy']:.1%}，要求至少 90%；正式语料保持不变")
                if fingerprint(slug, pack) != original_fingerprint:
                    raise RuntimeError("入库期间草稿被修改，已停止发布")
                mapping = [(stage / "DIRECTORY.md", pack / "DIRECTORY.md")]
                if action == "new":
                    mapping += [(stage / kind / f"{final}.md", pack / kind / f"{final}.md")
                                for kind in ("applications", "research")]
                for name in (*AUX_FILES, *STATE_FILES, "atlas.json", "gate_regression.json", "gate_summary.json"):
                    if (stage / "atlas" / name).exists():
                        mapping.append((stage / "atlas" / name, pack / "atlas" / name))
                mapping += [(path, web_data / path.relative_to(stage / "web-data"))
                            for path in sorted((stage / "web-data").rglob("*.json")) if path.name != "meta.json"]
                mapping.append((stage / "web-data/meta.json", web_data / "meta.json"))
                # Persist success and draft status in the same rollback transaction.
                with review_lock(pack):
                    current = load_review(pack)
                    current[slug] = {**current.get(slug, {}), "promoted": True, "action": action,
                        "section": target if action == "new" else None, "into": target if action == "merge" else None,
                        "final_slug": final if action == "new" else target, "gate": f"{summary['accuracy']:.1%}",
                        "gate_ok": True, "promote_error": None}
                    atomic_json(stage / "review.json", current)
                    draft_text = re.sub(r"^status: .*$", "status: promoted",
                                        (pack / "drafts" / f"{slug}.md").read_text(), count=1, flags=re.M)
                    atomic_write(stage / "promoted.md", draft_text)
                    mapping += [(stage / "review.json", pack / "drafts/review.json"),
                                (stage / "promoted.md", pack / "drafts" / f"{slug}.md"),
                                (stage / "atlas/atlas.sqlite", pack / "atlas/atlas.sqlite")]
                    publish_files(mapping, pack)
                    return current[slug]

        except Exception as error:
            set_status(slug, "draft", pack)
            update_review(slug, {"promoted": False, "gate_ok": False, "promote_error": str(error)}, pack)
            raise


def promote_new(slug, section_id):
    return promote(slug, "new", section_id)


def promote_merge(slug, into_slug):
    return promote(slug, "merge", into_slug)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug")
    parser.add_argument("action", choices=["new", "merge"])
    parser.add_argument("--section")
    parser.add_argument("--into")
    args = parser.parse_args()
    try:
        promote(args.slug, args.action, args.section if args.action == "new" else args.into)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
