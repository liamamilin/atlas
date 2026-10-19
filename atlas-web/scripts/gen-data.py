#!/usr/bin/env python3
"""Generate atlas-web public/data/*.json from atlas.sqlite + classified apps.
Source of truth = markdown corpus; rerun after corpus updates."""
from contextlib import closing, contextmanager
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import sys
import tempfile
import uuid

CODE_PACK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "application-atlas-production-pack"))
sys.path.insert(0, CODE_PACK)
from atlas_runtime import atomic_json, corpus_lock  # noqa: E402
PACK = os.environ.get("ATLAS_PACK", CODE_PACK)
DB = os.path.join(PACK, "atlas", "atlas.sqlite")
OUT = os.environ.get("ATLAS_WEB_OUT", os.path.join(os.path.dirname(__file__), "..", "public", "data"))

TASK_LABELS = {
    "todo": {"zh": "待办", "en": "Tasks"},
    "project": {"zh": "项目", "en": "Projects"},
    "calendar": {"zh": "日历", "en": "Calendar"},
    "habit": {"zh": "习惯", "en": "Habits"},
    "feedback": {"zh": "反馈", "en": "Feedback"},
    "notes": {"zh": "笔记", "en": "Notes"},
    "chat": {"zh": "聊天", "en": "Chat"},
    "booking": {"zh": "预订", "en": "Booking"},
}

RELATION_LABELS = {
    "adjacent": {"zh": "相邻", "en": "Adjacent"},
    "alternative": {"zh": "替代", "en": "Alternative"},
    "authority": {"zh": "权威", "en": "Authority"},
    "broader": {"zh": "更宽", "en": "Broader"},
    "complementary": {"zh": "互补", "en": "Complementary"},
    "contrasts": {"zh": "对照", "en": "Contrasts"},
    "counterpart": {"zh": "对应", "en": "Counterpart"},
    "downstream": {"zh": "下游", "en": "Downstream"},
    "narrower": {"zh": "更窄", "en": "Narrower"},
    "other": {"zh": "其他", "en": "Other"},
    "overlaps": {"zh": "交叠", "en": "Overlaps"},
    "related": {"zh": "相关", "en": "Related"},
    "sibling": {"zh": "同类", "en": "Sibling"},
    "substrate": {"zh": "基础承载", "en": "Substrate"},
    "upstream": {"zh": "上游", "en": "Upstream"},
    "variant_of": {"zh": "变体", "en": "Variant of"},
    "capability_of": {"zh": "内嵌能力", "en": "Capability of"},
    "component_of": {"zh": "组件", "en": "Component of"},
    "parent_of": {"zh": "父类", "en": "Parent of"},
    "child_of": {"zh": "子类", "en": "Child of"},
    "specializes": {"zh": "特化", "en": "Specializes"},
    "generalizes": {"zh": "泛化", "en": "Generalizes"},
    "enabled_by": {"zh": "依托", "en": "Enabled by"},
}


def _contains_cjk(value: str) -> bool:
    return any("\u4e00" <= char <= "\u9fff" for char in value or "")


def _app_name_en(app: dict) -> str:
    name = str(app.get("name") or "")
    if not _contains_cjk(name):
        return name
    for alias in app.get("aliases", []):
        alias = str(alias or "")
        if alias and not _contains_cjk(alias):
            return alias
    return name


def _app_name_zh(app: dict) -> str:
    name = str(app.get("name") or "")
    if _contains_cjk(name):
        return name
    for alias in app.get("aliases", []):
        alias = str(alias or "")
        if _contains_cjk(alias):
            return alias
    return name


def _join_task_labels(labels: list[str]) -> str:
    if not labels:
        return "general software work"
    if len(labels) == 1:
        return labels[0]
    return ", ".join(labels[:-1]) + f" and {labels[-1]}"


def _app_tagline_en(app: dict) -> str:
    explicit = str(app.get("tagline_en") or app.get("taglineEn") or "").strip()
    if explicit:
        return explicit
    name = _app_name_en(app) or str(app.get("slug") or "This application")
    labels = [
        TASK_LABELS.get(task, {"en": task.replace("_", " ")})["en"]
        for task in app.get("tasks", [])
    ]
    return f"{name} is cataloged for {_join_task_labels(labels)}."


def _classification_evidence(app_slug: str, classified: dict) -> dict:
    scores = []
    for leaf, score in (classified.get("scores") or {}).items():
        try:
            numeric = float(score)
        except (TypeError, ValueError):
            continue
        scores.append({"leaf": leaf, "score": numeric})
    scores.sort(key=lambda item: (-item["score"], item["leaf"]))
    return {
        "source": "mvp_apps_classified.json",
        "sourceRef": f"mvp_apps_classified.json#{app_slug}",
        "method": "atlas-classification",
        "selectedLeaf": classified.get("leaf", ""),
        "scores": scores[:5],
        "sourceSummary": classified.get("desc", ""),
    }


def _remove_path(path: Path) -> None:
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    else:
        path.unlink(missing_ok=True)


def recover_web_data_publication(output: Path) -> None:
    journal = output.with_name(f".{output.name}.publish.json")
    if not journal.exists():
        return
    state = json.loads(journal.read_text(encoding="utf-8"))
    output = output.resolve()
    stage = Path(state.get("stage", "")).resolve()
    backup = Path(state.get("backup", "")).resolve() if state.get("backup") else None
    for candidate in (stage, backup):
        if candidate and candidate.parent != output.parent:
            raise RuntimeError("invalid web data publication journal")
    if backup and backup.exists() and (not state.get("committed") or not output.exists()):
        _remove_path(output)
        os.replace(backup, output)
    _remove_path(stage)
    if backup:
        _remove_path(backup)
    journal.unlink(missing_ok=True)


@contextmanager
def staged_web_data(output: Path):
    output.parent.mkdir(parents=True, exist_ok=True)
    recover_web_data_publication(output)
    for stale in output.parent.glob(f".{output.name}.staging-*"):
        _remove_path(stale)
    stage = Path(tempfile.mkdtemp(
        prefix=f".{output.name}.staging-", dir=output.parent))
    try:
        yield stage
    finally:
        _remove_path(stage)


def publish_web_data(stage: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    recover_web_data_publication(output)
    backup = output.with_name(f".{output.name}.backup-{uuid.uuid4().hex}")
    journal = output.with_name(f".{output.name}.publish.json")
    state = {
        "stage": str(stage.resolve()),
        "backup": str(backup.resolve()) if output.exists() else "",
        "committed": False,
    }
    atomic_json(journal, state)
    try:
        if output.exists():
            os.replace(output, backup)
        os.replace(stage, output)
        state["committed"] = True
        atomic_json(journal, state)
    except BaseException:
        recover_web_data_publication(output)
        raise
    recover_web_data_publication(output)


def _write_json(path: Path, value) -> None:
    with path.open("w", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False)


def main():
    output_root = Path(globals()["OUT"]).resolve()
    with corpus_lock(PACK), staged_web_data(output_root) as OUT, closing(sqlite3.connect(DB)) as con:
        sec_cols = [r[1] for r in con.execute("PRAGMA table_info(section)")]
        has_sec_zh = "name_zh" in sec_cols
        sections = {}
        for sid, name, parent, path, kind in con.execute("SELECT id, name, parent, path, kind FROM section"):
            sections[sid] = {"id": sid, "name": name, "parent": parent, "path": path}
        if has_sec_zh:
            for sid, name_zh in con.execute("SELECT id, name_zh FROM section WHERE name_zh != ''"):
                sections[sid]["name_zh"] = name_zh
        leaves = {}
        for row in con.execute("SELECT slug, name, name_zh, aliases_zh, section_id, section_name, overview, defining_core, how_it_works, rules, variants, products_md, l0_zh, sources_md, full_md FROM leaf"):
            leaves[row[0]] = {
                "slug": row[0], "name": row[1], "name_zh": row[2] or "",
                "aliases_zh": [a for a in (row[3] or "").split("\n") if a.strip()],
                "section_id": row[4], "section_name": row[5],
                "overview": (row[6] or ""), "dc": (row[7] or ""),
                "how": (row[8] or ""), "rules": (row[9] or ""),
                "variants": (row[10] or ""), "products": (row[11] or ""),
                "dc_zh": (row[12] or ""),
                "sources": row[13] or "", "full_md": row[14] or "",
            }
        # body zh from translation table
        try:
            for row in con.execute("SELECT slug, overview_zh, how_zh, rules_zh, variants_zh, products_zh FROM leaf_zh_body"):
                if row[0] in leaves:
                    leaves[row[0]].update({
                        "overview_zh": (row[1] or ""), "how_zh": (row[2] or ""),
                        "rules_zh": (row[3] or ""), "variants_zh": (row[4] or ""),
                        "products_zh": (row[5] or ""),
                    })
        except sqlite3.OperationalError:
            pass
        relations = {}
        rel_zh = {}
        try:
            rel_zh = {(a, tn): d for a, tn, d in con.execute("SELECT from_slug, to_name, distinction_zh FROM rel_zh")}
        except sqlite3.OperationalError:
            pass
        for a, b, tn, k, d in con.execute("SELECT from_slug, to_slug, to_name, rel_kind, distinction FROM relation WHERE to_slug IS NOT NULL"):
            target = leaves.get(b, {})
            labels = RELATION_LABELS.get(k, {
                "zh": k.replace("_", " "),
                "en": k.replace("_", " "),
            })
            item = {"id": f"{a}:{k}:{b}:{len(relations.get(a, []))}",
                    "to": b, "toName": tn,
                    "toNameZh": target.get("name_zh", "") or tn,
                    "toNameEn": target.get("name", "") or tn,
                    "kind": k, "kindLabelZh": labels["zh"],
                    "kindLabelEn": labels["en"], "distinction": (d or "")}
            z = rel_zh.get((a, tn))
            if z:
                item["distinction_zh"] = z
            relations.setdefault(a, []).append(item)

        apps = json.load(open(os.path.join(PACK, "mvp_apps.json")))
        classified = {c["slug"]: c for c in json.load(open(os.path.join(PACK, "mvp_apps_classified.json")))}
        app_entries = []
        app_by_leaf = {}
        for a in apps:
            c = classified.get(a["slug"], {})
            leaf = c.get("leaf") or ""
            leaf_data = leaves.get(leaf, {})
            task_values = [str(task) for task in a.get("tasks", [])]
            task_labels = {
                lang: [TASK_LABELS.get(task, {"zh": task, "en": task})[lang] for task in task_values]
                for lang in ("zh", "en")
            }
            e = {
                "slug": a["slug"], "name": a["name"],
                "nameZh": _app_name_zh(a), "nameEn": _app_name_en(a),
                "aliases": a.get("aliases", []),
                "vendor": a.get("vendor", ""), "tagline": a.get("tagline", ""),
                "taglineEn": _app_tagline_en(a), "tasks": task_values,
                "taskLabels": task_labels, "leaf": leaf,
                "leafName": leaf_data.get("name_zh", "") or leaf_data.get("name", ""),
                "leafNameZh": leaf_data.get("name_zh", "") or leaf_data.get("name", ""),
                "leafNameEn": leaf_data.get("name", "") or leaf_data.get("name_zh", ""),
                "classificationEvidence": _classification_evidence(a["slug"], c),
            }
            app_entries.append(e)
            if leaf:
                app_by_leaf.setdefault(leaf, []).append({"slug": e["slug"], "name": e["name"]})

        os.makedirs(os.path.join(OUT, "sections"), exist_ok=True)
        os.makedirs(os.path.join(OUT, "leaves"), exist_ok=True)

        # meta + search index
        def summ(md, n):
            md = re.sub(r"```[\s\S]*?```", " ", md)
            prose = []
            for ln in md.splitlines():
                s = ln.strip()
                if not s or s[0] in "│├└┌#" :
                    continue
                s = re.sub(r"^[-*+]\s+", "", s)
                s = re.sub(r"(\*\*|__)(.*?)\1", r"\2", s)
                s = re.sub(r"`([^`]*)`", r"\1", s)
                prose.append(s)
            if len(prose) > 1 and prose[1].startswith(prose[0]):
                prose = prose[1:]
            txt = re.sub(r"\s+", " ", " ".join(prose)).strip()
            return txt[:n]

        def summ_zh(lf, n):
            c1 = summ(lf.get("dc_zh", ""), 400)
            c2 = summ(lf.get("overview_zh", ""), 400)
            return (c1 if len(c1) >= 40 or len(c1) >= len(c2) else c2)[:n]

        leaf_index = []
        for slug, lf in sorted(leaves.items(), key=lambda kv: (kv[1]["section_id"], kv[1]["name"])):
            leaf_index.append({"slug": slug, "name": lf["name"], "name_zh": lf["name_zh"],
                               "aliases_zh": lf.get("aliases_zh", []),
                               "sec": lf["section_id"], "dc": summ(lf["dc"], 160), "dc_zh": summ_zh(lf, 160)})
        l0s = []
        for sid, s in sorted(sections.items(), key=lambda kv: kv[0]):
            if s["parent"]:
                continue
            subs = []
            for sid2, s2 in sorted(sections.items(), key=lambda kv: kv[0]):
                if s2["parent"] == sid:
                    subs.append({"id": sid2, "name": s2["name"], "name_zh": s2.get("name_zh", ""), "path": s2["path"]})
            if not subs and any(lf["section_id"] == sid for lf in leaves.values()):
                n_leaves = sum(1 for lf in leaves.values() if lf["section_id"] == sid)
                subs.append({"id": sid, "name": f"All Types ({n_leaves})", "name_zh": f"全部类型 ({n_leaves})",
                             "path": s["path"]})
            l0s.append({"id": sid, "name": s["name"], "name_zh": s.get("name_zh", ""), "subs": subs})
        meta = {"leafCount": len(leaves), "sectionCount": len(sections), "l0Count": len(l0s),
                "appCount": len(app_entries), "generated": "gen-data.py", "l0s": l0s, "leafIndex": leaf_index}
        _write_json(Path(OUT) / "meta.json", meta)

        # per-section leaf cards
        sec_leaves = {}
        for slug, lf in leaves.items():
            sec_leaves.setdefault(lf["section_id"], []).append(
                {"slug": slug, "name": lf["name"], "name_zh": lf["name_zh"], "l0": summ(lf["dc"], 260), "l0_zh": summ_zh(lf, 260)})
        for sid, lst in sec_leaves.items():
            _write_json(Path(OUT) / "sections" / f"{sid}.json", {
                "id": sid, "name": sections[sid]["name"],
                "name_zh": sections[sid].get("name_zh", ""),
                "path": sections[sid]["path"],
                "leaves": sorted(lst, key=lambda x: x["name"]),
            })
        stale = set(os.listdir(os.path.join(OUT, "sections"))) - {f"{sid}.json" for sid in sec_leaves}
        for f in stale:
            os.remove(os.path.join(OUT, "sections", f))

        # per-leaf full detail
        for slug, lf in leaves.items():
            detail = dict(lf)
            detail["section_name_zh"] = sections.get(lf["section_id"], {}).get("name_zh", "")
            detail["relations"] = sorted(relations.get(slug, []), key=lambda r: (r["kind"], r["toName"]))
            detail["apps"] = app_by_leaf.get(slug, [])
            _write_json(Path(OUT) / "leaves" / f"{slug}.json", detail)

        _write_json(Path(OUT) / "apps.json", app_entries)
        publish_web_data(Path(OUT), output_root)
        print(f"generated: {len(leaves)} leaves, {len(sections)} sections, {len(app_entries)} apps")


if __name__ == "__main__":
    main()
