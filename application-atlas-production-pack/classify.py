#!/usr/bin/env python3
"""bge-m3 top-10 + up to six distinct graph neighbors + model adjudication.
Usage: python3 classify.py "产品描述..."
Database snapshots reload after replacement; each request keeps one snapshot.
"""
import json
import os
import re
import sqlite3
import sys
import threading
import urllib.request
from urllib.error import HTTPError, URLError
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from atlas_runtime import PACK, api_key
from privacy import redact_text

import atlas_model

DB = str(PACK / "atlas" / "atlas.sqlite")
# Empty means "use the configured default model"; an explicit value pins the
# adjudicator to a specific model on the default provider.
ADJUDICATOR = os.environ.get("ATLAS_ADJUDICATOR", "").strip()
POOL_MAX = 16
_cache_lock = threading.Lock()
_snapshot = None
_signature = None


class ClassificationProviderError(RuntimeError):
    """A redacted, stable classification-provider failure."""

    def __init__(self, code: str, message: str, *, status: int | None = None,
                 retryable: bool = False, detail: str = ""):
        super().__init__(message)
        self.code = code
        self.status = status
        self.retryable = retryable
        self.detail = redact_text(detail)[:800]


def _provider_error(error: BaseException) -> ClassificationProviderError:
    # atlas_model already redacts and classifies provider failures; translate
    # its codes into the classification contract the CLI and callers expect.
    if isinstance(error, atlas_model.ModelConfigError):
        mapping = {
            "unauthorized": ("provider_auth", False),
            "no_credential": ("provider_auth", False),
            "not_configured": ("provider_auth", False),
            "no_model": ("model_unavailable", False),
            "model_unavailable": ("model_unavailable", False),
            "rate_limited": ("provider_rate_limited", True),
            "timeout": ("provider_network_error", True),
            "unreachable": ("provider_network_error", True),
            "invalid_response": ("invalid_response", False),
        }
        code, retryable = mapping.get(
            error.code, ("provider_http_error", error.code in {"provider_error"}))
        return ClassificationProviderError(
            code, str(error), status=error.status, retryable=retryable)
    if isinstance(error, HTTPError):
        try:
            detail = error.read(4096).decode("utf-8", "replace")
        except OSError:
            detail = ""
        detail = redact_text(detail)
        lowered = detail.lower()
        status = int(error.code)
        if status in {401, 403}:
            code, retryable = "provider_auth", False
        elif status == 429:
            code, retryable = "provider_rate_limited", True
        elif "model" in lowered and "unavailable" in lowered:
            code, retryable = "model_unavailable", False
        else:
            code, retryable = "provider_http_error", status >= 500
        return ClassificationProviderError(
            code, f"classification provider returned HTTP {status}",
            status=status, retryable=retryable, detail=detail)
    if isinstance(error, URLError):
        return ClassificationProviderError(
            "provider_network_error", "classification provider network request failed",
            retryable=True, detail=str(error.reason))
    if isinstance(error, (TimeoutError, OSError)):
        return ClassificationProviderError(
            "provider_network_error", "classification provider network request failed",
            retryable=True, detail=str(error))
    return ClassificationProviderError(
        "provider_error", "classification provider request failed", detail=str(error))


@dataclass(frozen=True)
class Snapshot:
    slugs: tuple
    matrix: np.ndarray
    leaf_info: dict
    sections: dict
    neighbors: dict
    relations: dict


def snapshot():
    global _snapshot, _signature
    with _cache_lock:
        for _ in range(3):
            stat = os.stat(DB)
            sig = (str(DB), stat.st_ino, stat.st_size, stat.st_mtime_ns)
            if sig == _signature and _snapshot is not None:
                return _snapshot
            con = sqlite3.connect(Path(DB).resolve().as_uri() + "?mode=ro", uri=True)
            try:
                con.execute("BEGIN")
                rows = con.execute("SELECT e.slug, e.vec FROM embedding e JOIN leaf l ON e.slug=l.slug ORDER BY e.slug").fetchall()
                leaves = con.execute("SELECT slug,name_zh,l0_zh,overview,section_id FROM leaf").fetchall()
                rels = con.execute("SELECT from_slug,to_slug,to_name,distinction FROM relation WHERE to_slug IS NOT NULL").fetchall()
            finally:
                con.close()
            now = os.stat(DB)
            if sig != (str(DB), now.st_ino, now.st_size, now.st_mtime_ns):
                continue
            if not rows:
                raise RuntimeError("语料向量为空，请先运行 embed_leaves.py")
            matrix = np.stack([np.frombuffer(r[1], dtype=np.float32) for r in rows])
            matrix /= np.linalg.norm(matrix, axis=1, keepdims=True) + 1e-9
            matrix.flags.writeable = False
            slugs = tuple(r[0] for r in rows)
            available = set(slugs)
            nb, boundaries = {}, {}
            for a, b, name, distinction in rels:
                if a not in available or b not in available:
                    continue
                nb.setdefault(a, set()).add(b)
                nb.setdefault(b, set()).add(a)
                if distinction:
                    boundaries.setdefault((a, b), (name, distinction))
            _snapshot = Snapshot(slugs, matrix,
                {r[0]: (r[1], (r[2] or r[3] or "")[:170]) for r in leaves},
                {r[0]: r[4] for r in leaves}, nb, boundaries)
            _signature = sig
            return _snapshot
        raise RuntimeError("语料正在更新，请稍后重试")


PROMPT = """你是软件类型分类器。对下列每个候选类型，独立打 0-10 分表示与产品描述的匹配度（互不比较，仅看各自定义）。
产品描述: {desc}
候选:
{cands}
{bounds}
输出 JSON 数组: [{{"slug":"...","score":0-10,"brief":"≤12字"}}] 然后输出 {{"choice":"最高分slug或none"}}。"""


def _embed(texts):
    body = json.dumps({"model": "bge-m3", "input": texts}).encode()
    req = urllib.request.Request("http://localhost:11434/api/embed", body,
                                 {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as response:
        return [np.array(e, dtype=np.float32) for e in json.load(response)["embeddings"]]


def _pairwise(slugs, state=None):
    state = state or snapshot()
    lines = []
    for i, a in enumerate(slugs):
        for b in slugs[i + 1:]:
            relation = state.relations.get((a, b)) or state.relations.get((b, a))
            if relation:
                lines.append(f"{a} vs {b}: {relation[1][:140]}")
    return "\n".join(lines[:8])


def candidates(qtext, k=10, state=None):
    """Return ordered slugs and similarity keyed by slug, never by row position."""
    if not 1 <= k <= POOL_MAX:
        raise ValueError(f"k must be between 1 and {POOL_MAX}")
    state = state or snapshot()
    vector = _embed([qtext])[0]
    vector /= np.linalg.norm(vector) + 1e-9
    values = state.matrix @ vector
    scores = dict(zip(state.slugs, map(float, values)))
    order = sorted(state.slugs, key=lambda s: (-scores[s], s))
    pool = order[:k]
    seen = set(pool)
    neighbors = set().union(*(state.neighbors.get(s, set()) for s in pool[:5])) - seen
    neighbors.intersection_update(scores)
    pool.extend(sorted(neighbors, key=lambda s: (-scores[s], s))[:POOL_MAX - len(pool)])
    return pool, scores


def classify(desc, model=None):
    # An explicit model (argument or ATLAS_ADJUDICATOR) pins the model; empty
    # means "use the configured default for the adjudicator role".
    raw = ADJUDICATOR if model is None else model
    if raw is None:
        raw = ""
    if not isinstance(raw, str):
        raise ValueError("classification model must be text")
    model_name = raw.strip()
    state = snapshot()
    pool, similarities = candidates(desc, state=state)
    cands = [f"- {s}（{state.leaf_info[s][0]}）: {state.leaf_info[s][1]}" for s in pool]
    bounds = _pairwise(pool, state)
    prompt = PROMPT.format(
        desc=desc, cands="\n".join(cands),
        bounds=("\n分界记录:\n" + bounds if bounds else ""))
    try:
        result = atlas_model.complete(
            [{"role": "user", "content": prompt}],
            model=model_name or None, role="adjudicator",
            temperature=0.1, max_tokens=3000, timeout=300)
    except atlas_model.ModelConfigError as error:
        raise _provider_error(error) from error
    except (HTTPError, URLError, TimeoutError, OSError, KeyError,
            FileNotFoundError) as error:
        raise _provider_error(error) from error
    text = result["text"]
    served_model = result["model"] or model_name
    if not text:
        raise ClassificationProviderError(
            "invalid_response", "classification provider response shape is invalid")
    match = re.search(r"\[.*?\]", text, re.S)
    scores = {}
    if match:
        try:
            scored_items = json.loads(match.group(0))
        except json.JSONDecodeError as error:
            raise ClassificationProviderError(
                "invalid_response", "classification provider score payload is invalid",
                detail=str(error)) from error
        if not isinstance(scored_items, list):
            raise ClassificationProviderError(
                "invalid_response", "classification provider score payload is invalid")
        for item in scored_items:
            if not isinstance(item, dict):
                continue
            slug, score = item.get("slug"), item.get("score")
            if slug in pool and isinstance(score, (int, float)) and 0 <= score <= 10:
                scores[slug] = score
    match = re.search(r'\{[^{]*"choice"[^}]*\}', text, re.S)
    try:
        choice = json.loads(match.group(0)).get("choice") if match else None
    except (json.JSONDecodeError, AttributeError) as error:
        raise ClassificationProviderError(
            "invalid_response", "classification provider choice payload is invalid",
            detail=str(error)) from error
    if choice not in pool and choice != "none":
        raise ValueError("分类器没有返回有效候选类型")
    return {"choice": choice, "scores": scores, "pool": pool,
            "model": served_model,
            "detail": [{"slug": s, "name_zh": state.leaf_info[s][0]} for s in pool]}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    result = classify(" ".join(sys.argv[1:]))
    print(f"判定: {result['choice']}")
    names = {r["slug"]: r["name_zh"] for r in result["detail"]}
    for slug, score in sorted(result["scores"].items(), key=lambda item: -item[1])[:5]:
        print(f"  {score:>4} {slug}（{names.get(slug, '?')}）")
