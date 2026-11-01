"""Narrow one sampled project's claims to include its documented pending integrations."""
import copy
import json
from pathlib import Path
import sqlite3
import sys

BASE = Path(__file__).resolve().parent
PACK = BASE.parents[1] / "application-atlas-production-pack"
sys.path.insert(0, str(PACK))
from oss_catalog import CatalogStore, canonical, digest, now
from oss_discovery import PROJECT_REVIEWS, review_card

store = CatalogStore(bootstrap=False)
repo = "330205812/NexusRAG"
card = store.previous(repo, "vector-retrieval-platform")
readme = next(s for s in card["sources"] if s["kind"] == "readme")
reviews = json.loads(PROJECT_REVIEWS.read_text())
reviews[repo.lower()] = {
    "readme_sha256": readme["sha256"],
    "reviewed_at": now(),
    "reason": "人工验收：README 的 Components 表将 Neo4j 和 MinerU 标为 Pending merge，介绍须保留该限制。",
    "fact_overrides": {
        "summary": "NexusRAG 提供知识库管理、文档处理与全文、语义和混合检索；README 列出的 Neo4j 知识图谱与 MinerU 解析器集成尚待合并。",
        "scope": "面向知识检索与 GenAI 应用，依赖 Milvus、Elasticsearch 等组件；Neo4j 与 MinerU 在官方组件表中标为 Pending merge，不能视为已经合入的可用集成。",
    },
}
PROJECT_REVIEWS.write_text(json.dumps(reviews, ensure_ascii=False, indent=2) + "\n")
before = copy.deepcopy(card)
card = review_card(card)
card["features"][0]["text"] = "全文、语义与混合检索；README 列出知识图谱查询，但 Neo4j 集成待合并"
card["features"][1]["text"] = "文档上传与处理；README 列出多模态 OCR，但 MinerU 解析器集成待合并"

def invariant(con):
    return {table: digest(canonical([list(r) for r in con.execute(query)])) for table, query in {
        "memberships": "SELECT * FROM oss_leaf_project ORDER BY leaf,repository_id",
        "matches": "SELECT * FROM oss_match ORDER BY scenario_id,repository_id",
        "favorites": "SELECT repository_id,favorite FROM oss_project ORDER BY repository_id",
    }.items()}

with store.connect() as con:
    saved = invariant(con)
    outcome = store._upsert(con, card, "vector-retrieval-platform")
    assert invariant(con) == saved
    assert card["license"] == before["license"]
    assert card["sources"] == before["sources"]

with sqlite3.connect(store.path) as src, sqlite3.connect("/private/tmp/atlas-100-acceptance-2026-10-25.sqlite") as dst:
    src.backup(dst)
report = {
    "repo": repo, "outcome": outcome, "reviewed_at": now(),
    "source_url": readme["url"], "source_sha256": readme["sha256"],
    "fields_narrowed": ["summary", "scope", "features[0]", "features[1]"],
    "reason": reviews[repo.lower()]["reason"],
    "memberships_matches_favorites_preserved": True,
    "license_and_source_bindings_preserved": True,
}
(BASE / "CORRECTION.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(report, ensure_ascii=False))
