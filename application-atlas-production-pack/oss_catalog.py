"""Scenario-indexed repository catalog, isolated from the historical factory.

python3 oss_catalog.py refresh | export | inspect
Curated PKM updates, open-taxonomy discovery and persistent batch progress.
"""
from __future__ import annotations

import argparse
import base64
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
from functools import lru_cache
import hashlib
from html import unescape
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import sqlite3
import threading
import time
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlencode
from urllib.request import HTTPRedirectHandler, Request, build_opener
import uuid

from atlas_runtime import PACK, atomic_json

DATA = Path(__file__).resolve().parent / "oss_catalog_data"
PILOT_LEAF = "personal-knowledge-management-application"
AUTO_LEAVES = {"feed-reader": "阅读器", "diagramming-application": "图表应用", "password-manager": "密码管理器"}
OSI_LICENSES = {"MIT", "BSD-2-Clause", "BSD-3-Clause", "Apache-2.0", "GPL-2.0", "GPL-3.0", "AGPL-3.0", "MPL-2.0"}


@lru_cache(maxsize=1)
def available_leaves():
    """The existing Atlas taxonomy is the authority, not a pilot allowlist."""
    source = DATA.parent / "atlas/atlas.json"
    leaves = json.loads(source.read_text())["leaves"]
    return {slug: AUTO_LEAVES.get(slug, "个人知识管理应用" if slug == PILOT_LEAF else row["name"])
            for slug, row in leaves.items()}


def validate_leaf(leaf):
    if not isinstance(leaf, str) or leaf not in available_leaves():
        raise CatalogError("叶子不在 Atlas 现有分类中", 404)
    return leaf


class CatalogError(ValueError):
    def __init__(self, message, status=400):
        super().__init__(message)
        self.status = status


class ServiceUnavailable(CatalogError):
    """A shared service outage must preserve unfinished work for recovery."""
    component = "service"

    def __init__(self, message, status=502, *, retryable=False, retry_after=None,
                 code="model_unavailable", upstream_status=None):
        super().__init__(message, status)
        self.retryable = retryable
        self.retry_after = retry_after
        self.code = code
        self.upstream_status = upstream_status


class ModelServiceUnavailable(ServiceUnavailable):
    component = "model"


class GitHubServiceUnavailable(ServiceUnavailable):
    component = "github"


class GitHubResponseTooLarge(CatalogError):
    """A bounded response exceeded the read limit; search pages can be split."""


class WorkflowInterrupted(ServiceUnavailable):
    """An aborted coordinator must not turn untouched candidates into failures."""
    component = "workflow"

    def __init__(self, exception_type, phase):
        super().__init__(f"本批执行中断（{exception_type}），未完成候选保留，将自动重试",
                         retryable=True, code="workflow_interrupted")
        self.exception_type = exception_type
        self.phase = phase


def now():
    return datetime.now(timezone.utc).isoformat()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


def repository_metadata(value):
    # Keep public catalog facts only, excluding authenticated account permissions
    # or repository security settings returned by GitHub.
    fields = ("id", "name", "full_name", "private", "disabled", "visibility", "archived", "fork", "pushed_at",
              "default_branch", "language", "url", "html_url", "description", "stargazers_count", "license", "topics")
    return {key: value[key] for key in fields if key in value}


def manifest():
    return json.loads((DATA / "pilot.json").read_text())


def curation_digest(candidate):
    reviews = json.loads((DATA / "license-reviews.json").read_text())
    return digest(canonical({"candidate": candidate, "license_review": reviews.get(candidate["repo"].lower())}))


class _Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def plain_text(value):
    parser = _Text()
    try:
        parser.feed(value)
        text = " ".join(parser.parts)
    except AssertionError:
        # Markdown/code can contain a literal '<![' (e.g. regex lookbehind),
        # which HTMLParser treats as a broken declaration. Keep its text;
        # only remove ordinary HTML tags, never discard the whole repository.
        text = unescape(re.sub(r"</?[A-Za-z][^>]*>", " ", value))
    return re.sub(r"\s+", " ", text).strip()


def decode_file(value):
    if value.get("encoding") != "base64" or not value.get("content"):
        raise CatalogError("GitHub 未返回完整的文本文件", 502)
    return base64.b64decode(value["content"]).decode("utf-8-sig")


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class GitHub:
    """Read-only, bounded public GitHub API client; tokens never reach catalog data."""
    _search_lock = threading.Lock()
    _last_search = 0.0

    @staticmethod
    def retry_delay(headers):
        from email.utils import parsedate_to_datetime
        import math
        value = headers.get("Retry-After", "")
        if value:
            try:
                delay = float(value)
            except ValueError:
                try:
                    delay = parsedate_to_datetime(value).timestamp() - time.time()
                except (ValueError, TypeError, OverflowError):
                    delay = float("nan")
            if math.isfinite(delay):
                return max(0, delay)
        reset = headers.get("X-RateLimit-Reset", "")
        if reset.isdigit() and headers.get("X-RateLimit-Remaining") == "0":
            return max(2, float(reset) - time.time() + 1)
        return None

    def get(self, path):
        for attempt in range(2):
            try:
                return self._get(path)
            except GitHubResponseTooLarge:
                if not path.startswith("/search/repositories?"):
                    raise
                options = {k: v[-1] for k, v in parse_qs(path.split("?", 1)[1]).items()}
                size, page = int(options.get("per_page", 30)), int(options.get("page", 1))
                # Keep the same result window and 3 MiB per-response bound.
                # At most 100 -> 50 -> 25: no unbounded pagination/retries.
                if size not in {100, 50}:
                    raise
                smaller = size // 2
                parts = [self.get("/search/repositories?" + urlencode({**options, "per_page": smaller,
                         "page": (page - 1) * 2 + offset})) for offset in (1, 2)]
                items = {item["id"]: item for part in parts for item in part.get("items", [])}
                return {"items": list(items.values()), "total_count": max(p.get("total_count", 0) for p in parts),
                        "incomplete_results": any(p.get("incomplete_results", False) for p in parts),
                        "search_request_count": 1 + sum(p.get("search_request_count", 1) for p in parts),
                        "split_pages": [entry for offset, part in enumerate(parts, 1)
                                        for entry in part.get("split_pages", [{"page": (page - 1) * 2 + offset,
                                                                              "per_page": smaller}])]}
            except CatalogError as error:
                if attempt == 0 and (not isinstance(error, ServiceUnavailable) or error.retryable and (error.retry_after or 0) <= 2) and ("无法连接或读取" in str(error) or re.search(r"HTTP 5\d\d", str(error))):
                    time.sleep(2)
                    continue
                raise

    def _get(self, path):
        if (not path.startswith(("/repos/", "/repositories/", "/search/repositories?")) and path != "/rate_limit") or ".." in path:
            raise CatalogError("不支持的 GitHub 资源")
        if path.startswith("/search/repositories?"):
            # Public repository search has a separate small quota. Pace cached
            # reruns too: those still perform real searches, without a model wait.
            with self._search_lock:
                delay = max(0, 6.1 - (time.monotonic() - GitHub._last_search))
                if delay:
                    time.sleep(delay)
                GitHub._last_search = time.monotonic()
        headers = {"User-Agent": "Application-Atlas-OSS/1", "Accept": "application/vnd.github+json"}
        from github_settings import token as github_token
        token = github_token()
        if token:
            headers["Authorization"] = "Bearer " + token
        try:
            # Repository transfers use a numeric repository resource redirect.
            url = "https://api.github.com" + path
            for _ in range(4):
                try:
                    with build_opener(_NoRedirect()).open(Request(url, headers=headers), timeout=25) as response:
                        data = response.read(3 * 1024 * 1024 + 1)
                        if len(data) > 3 * 1024 * 1024:
                            raise GitHubResponseTooLarge("GitHub 资源超过采集大小限制", 502)
                        return json.loads(data)
                except HTTPError as error:
                    target = error.headers.get("Location", "")
                    if error.code in (301, 302, 307, 308) and re.fullmatch(
                        r"https://api\.github\.com/(?:repos|repositories)/[^?#]+(?:\?[^#]*)?", target
                    ):
                        url = target
                        continue
                    if error.code == 404:
                        raise CatalogError("GitHub 资源不存在或不再公开", 502) from None
                    if error.code == 401:
                        raise GitHubServiceUnavailable("GitHub Token 无效或已过期，请在设置中更新", 401,
                                                       code="github_unauthorized", upstream_status=401) from None
                    if error.code in (403, 429):
                        retry_after = error.headers.get("Retry-After", "")
                        detail = error.read(4096).decode("utf-8", "replace").lower()
                        if error.code == 429 or retry_after or error.headers.get("X-RateLimit-Remaining") == "0" or "rate limit" in detail:
                            delay = self.retry_delay(error.headers)
                            raise GitHubServiceUnavailable("GitHub 暂时限流，将按恢复时间自动继续", retryable=True,
                                                           retry_after=delay if delay is not None else 60,
                                                           code="github_rate_limited", upstream_status=error.code) from None
                        raise CatalogError("GitHub 当前资源无访问权限（HTTP 403）", 502) from None
                    if 500 <= error.code < 600 or error.code in {408, 425}:
                        raise GitHubServiceUnavailable(f"GitHub 请求暂时失败（HTTP {error.code}）", retryable=True,
                                                       retry_after=self.retry_delay(error.headers),
                                                       code="github_unavailable", upstream_status=error.code) from None
                    raise CatalogError(f"GitHub 请求失败（HTTP {error.code}）", 502) from None
            raise CatalogError("GitHub 重定向次数过多", 502)
        except (URLError, TimeoutError, OSError, json.JSONDecodeError) as error:
            raise GitHubServiceUnavailable("无法连接或读取 GitHub；已保存的资料仍可浏览", retryable=True,
                                           code="github_unreachable") from error

    def collect(self, candidate, previous=None):
        repo = candidate["repo"]
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
            raise CatalogError("仓库名称无效")
        path = "/repos/" + repo
        meta = self.get(path)
        if meta.get("private") or meta.get("disabled"):
            raise CatalogError("仓库不再公开可用", 502)
        # A fresh repository metadata check is sufficient while the default
        # branch and pushed_at remain unchanged. License and README digests are
        # retained, rather than claimed to have been fetched again.
        if previous and previous.get("repository_id") == meta["id"] and all(
            previous.get(key) == meta.get(key) for key in ("pushed_at", "default_branch")
        ) and previous.get("curation_digest") == curation_digest(candidate):
            result = dict(previous)
            result.update(full_name=meta["full_name"], github_url=meta["html_url"],
                          archived=meta.get("archived", False), checked_at=now())
            return result
        readme = self.get(path + "/readme")
        try:
            license_file = self.get(path + "/license")
        except CatalogError as error:
            # An absent license must downgrade classification, not preserve an
            # obsolete open-source label. Other failures preserve the last card.
            if "不存在" not in str(error):
                raise
            license_file = None
        languages = self.get(path + "/languages")
        return build_card(candidate, meta, readme, license_file, languages)

    def discover(self, query):
        if not isinstance(query, str) or not 1 <= len(query.strip()) <= 200:
            raise CatalogError("发现关键词必须在 1–200 字符之间")
        response = self.get("/search/repositories?" + urlencode({"q": query, "per_page": 15, "sort": "stars"}))
        return {"query": query, "source_url": "https://github.com/search?" + urlencode({"q": query, "type": "repositories"}),
                "retrieved_at": now(), "status": "candidates_need_review", "total_count": response["total_count"],
                "items": [{key: item.get(key) for key in ("id", "full_name", "html_url", "description", "license", "archived")}
                          for item in response["items"]]}


def source_file(repo, kind, file, text):
    # Keep both a readable file URL and the immutable Git blob resource.
    return {"kind": kind, "url": file["html_url"],
            "immutable_url": file["git_url"],
            "path": file["path"], "blob_sha": file["sha"], "sha256": digest(text),
            "retrieved_at": now()}


def license_info(repo, meta, file):
    detected = (meta.get("license") or {}).get("spdx_id")
    result = {"spdx": None, "detected_spdx": detected, "status": "pending",
              "note": "许可证尚未核验", "source": None}
    if not file:
        result["note"] = "未发现许可证文件；公开仓库不等于开源授权"
        return result
    body = decode_file(file)
    result["source"] = source_file(repo, "license", file, body)
    reviews = json.loads((DATA / "license-reviews.json").read_text())
    review = reviews.get(repo.lower())
    if review and review["sha256"] == digest(body):
        spdx = review["spdx"]
        result.update(spdx=spdx, status="open_source" if spdx in OSI_LICENSES else "source_available",
                      note=review["note"], reviewed_at=review["reviewed_at"])
    else:
        result["note"] = "许可证文件新增或发生变化，需要重新核验；GitHub 自动识别仅供参考"
    return result


def build_card(candidate, meta, readme, license_file, languages):
    if meta.get("private") or meta.get("disabled"):
        raise CatalogError("不能收录非公开仓库")
    body = decode_file(readme)
    searchable = plain_text(body)
    source = source_file(meta["full_name"], "readme", readme, body)

    def evidence(needle):
        position = searchable.casefold().find(needle.casefold())
        if position < 0:
            raise CatalogError(f"{candidate['repo']} 的 README 不再支持已整理的资料，需要复核：{needle}", 422)
        return {"source_url": source["url"], "immutable_url": source["immutable_url"], "source_sha256": source["sha256"],
                "excerpt": searchable[max(0, position - 50):position + len(needle) + 90]}

    facts = [{"text": fact["text"], "evidence": evidence(fact["anchor"])} for fact in candidate["features"]]
    matches = [{"scenario_id": match["scenario_id"], "reason": match["reason"],
                "evidence": evidence(match["anchor"])} for match in candidate["matches"]]
    return {
        "repository_id": meta["id"], "name": candidate["name"], "full_name": meta["full_name"],
        "github_url": meta["html_url"], "positioning": candidate["positioning"],
        "summary": candidate["summary"], "summary_evidence": evidence(candidate["summary_anchor"]),
        "scope": candidate["scope"], "scope_evidence": evidence(candidate["scope_anchor"]),
        "features": facts, "matches": matches, "languages": list(languages)[:5],
        "license": license_info(meta["full_name"], meta, license_file),
        "sources": [source, {"kind": "repository", "url": meta["url"], "retrieved_at": now()},
                    {"kind": "languages", "url": meta["languages_url"], "retrieved_at": now()}],
        "pushed_at": meta["pushed_at"], "default_branch": meta["default_branch"],
        "archived": meta.get("archived", False), "checked_at": now(),
        "curation_digest": curation_digest(candidate),
        "editorial_method": "试点编辑整理；逐项依据官方仓库资料核验，未做部署实测",
    }


def content_digest(card):
    def stable(value):
        if isinstance(value, dict):
            return {key: stable(item) for key, item in value.items() if key not in {"checked_at", "retrieved_at"}}
        if isinstance(value, list):
            return [stable(item) for item in value]
        return value
    return digest(canonical(stable(card)))


class CatalogStore:
    def __init__(self, path=None, bootstrap=True):
        self.path = Path(path or os.environ.get("ATLAS_OSS_STORE", PACK / "atlas/oss-catalog.sqlite"))
        self.path.parent.mkdir(parents=True, exist_ok=True)
        # The API builds a store per request; schema checks, association backfill
        # and snapshot bootstrap only need to run once per database file.
        ready = (_file_key(self.path), bool(bootstrap and os.environ.get("ATLAS_OSS_BOOTSTRAP") != "0"))
        if ready[0] and ready in _READY:
            return
        self._initialize(bootstrap)
        _READY.add((_file_key(self.path), ready[1]))

    def _initialize(self, bootstrap):
        with self.connect() as con:
            con.execute("PRAGMA journal_mode=WAL")
            con.executescript("""
                CREATE TABLE IF NOT EXISTS oss_scenario (
                  id TEXT PRIMARY KEY, leaf TEXT NOT NULL, position INTEGER NOT NULL, data TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS oss_project (
                  repository_id INTEGER PRIMARY KEY, full_name TEXT NOT NULL COLLATE NOCASE UNIQUE,
                  data TEXT NOT NULL, content_digest TEXT NOT NULL, checked_at TEXT NOT NULL,
                  favorite INTEGER NOT NULL DEFAULT 0);
                CREATE TABLE IF NOT EXISTS oss_match (
                  scenario_id TEXT NOT NULL REFERENCES oss_scenario(id),
                  repository_id INTEGER NOT NULL REFERENCES oss_project(repository_id), data TEXT NOT NULL,
                  PRIMARY KEY(scenario_id,repository_id));
                CREATE TABLE IF NOT EXISTS oss_run (
                  id TEXT PRIMARY KEY, leaf TEXT NOT NULL, status TEXT NOT NULL, data TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS oss_meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS oss_candidate (
                  leaf TEXT NOT NULL, repository_id INTEGER NOT NULL, status TEXT NOT NULL,
                  reason TEXT NOT NULL, data TEXT NOT NULL, PRIMARY KEY(leaf, repository_id));
                CREATE TABLE IF NOT EXISTS oss_leaf_project (
                  leaf TEXT NOT NULL, repository_id INTEGER NOT NULL REFERENCES oss_project(repository_id),
                  PRIMARY KEY(leaf,repository_id));
                CREATE TABLE IF NOT EXISTS oss_batch_job (
                  id TEXT PRIMARY KEY, status TEXT NOT NULL, data TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS oss_batch_target (
                  job_id TEXT NOT NULL, leaf TEXT NOT NULL, repository_id INTEGER NOT NULL,
                  full_name TEXT NOT NULL, status TEXT NOT NULL, reason TEXT,
                  priority TEXT NOT NULL, finished_at TEXT,
                  PRIMARY KEY(job_id,leaf,repository_id));
                CREATE INDEX IF NOT EXISTS oss_batch_target_status ON oss_batch_target(job_id,status);
                CREATE TABLE IF NOT EXISTS oss_batch_leaf (
                  job_id TEXT NOT NULL, leaf TEXT NOT NULL, position INTEGER NOT NULL,
                  selected_count INTEGER NOT NULL, candidate_total INTEGER NOT NULL,
                  deferred_count INTEGER NOT NULL, state TEXT NOT NULL, data TEXT NOT NULL,
                  PRIMARY KEY(job_id,leaf));
                CREATE INDEX IF NOT EXISTS oss_project_favorite ON oss_project(favorite);
            """)
            con.execute("INSERT OR IGNORE INTO oss_leaf_project SELECT DISTINCT s.leaf,m.repository_id FROM oss_match m JOIN oss_scenario s ON s.id=m.scenario_id")
        if bootstrap and os.environ.get("ATLAS_OSS_BOOTSTRAP") != "0" and (DATA / "pilot.snapshot.json").exists():
            self.bootstrap()
            self.bootstrap_batch()

    @contextmanager
    def connect(self):
        con = sqlite3.connect(self.path, timeout=10)
        con.row_factory = sqlite3.Row
        con.execute("PRAGMA foreign_keys=ON")
        try:
            with con:
                yield con
        finally:
            con.close()

    def bootstrap(self):
        with self.connect() as con:
            con.execute("BEGIN IMMEDIATE")
            if con.execute("SELECT 1 FROM oss_meta WHERE key='bootstrap'").fetchone():
                return
            bundle = json.loads((DATA / "pilot.snapshot.json").read_text())
            self._scenarios(con, bundle["scenarios"])
            for card in bundle["projects"]:
                if not con.execute("SELECT 1 FROM oss_project WHERE repository_id=?", (card["repository_id"],)).fetchone():
                    self._upsert(con, card)
            con.execute("INSERT INTO oss_meta VALUES ('bootstrap',?)", (bundle["exported_at"],))

    def bootstrap_batch(self):
        path = DATA / "batch.snapshot.json"
        if not path.exists():
            return
        with self.connect() as con:
            con.execute("BEGIN IMMEDIATE")
            bundle = json.loads(path.read_text())
            bundle["scenarios"] = [{**s, "leaf": s.get("leaf", PILOT_LEAF)} for s in bundle["scenarios"]]
            revision = digest(canonical({k: bundle.get(k) for k in ("scenarios", "projects", "candidates")}))
            previous = con.execute("SELECT value FROM oss_meta WHERE key='batch_bootstrap_revision'").fetchone()
            if previous and previous[0] == revision:
                return
            for leaf in sorted({s["leaf"] for s in bundle["scenarios"]}):
                self._scenarios(con, [s for s in bundle["scenarios"] if s["leaf"] == leaf
                                     and not con.execute("SELECT 1 FROM oss_scenario WHERE id=?", (s["id"],)).fetchone()], leaf, prune=False)
                ids = {s["id"] for s in bundle["scenarios"] if s["leaf"] == leaf}
                for card in bundle["projects"]:
                    matches = [m for m in card["matches"] if m["scenario_id"] in ids]
                    if matches or leaf in card.get("leaves", []):
                        old = con.execute("SELECT data FROM oss_project WHERE repository_id=?", (card["repository_id"],)).fetchone()
                        if old and json.loads(old[0])["checked_at"] > card["checked_at"]:
                            continue
                        self._upsert(con, {**card, "matches": matches}, leaf)
            for item in bundle.get("candidates", []):
                previous_candidate = con.execute("SELECT data FROM oss_candidate WHERE leaf=? AND repository_id=?", (item["leaf"], item["repository_id"])).fetchone()
                if previous_candidate:
                    local = json.loads(previous_candidate[0])
                    incoming = item["data"]
                    newer_attempt = incoming.get("last_attempt_at", "") > local.get("last_attempt_at", "")
                    newer_change = incoming.get("source_changed") and incoming.get("last_seen_at", "") > local.get("last_seen_at", "")
                    if not newer_attempt and not newer_change:
                        continue
                con.execute("INSERT INTO oss_candidate VALUES (?,?,?,?,?) ON CONFLICT(leaf,repository_id) DO UPDATE SET status=excluded.status,reason=excluded.reason,data=excluded.data",
                            (item["leaf"], item["repository_id"], item["status"], item["reason"], canonical(item["data"])))
            con.execute("INSERT INTO oss_meta VALUES ('batch_bootstrap_revision',?) ON CONFLICT(key) DO UPDATE SET value=excluded.value", (revision,))

    def record_candidates(self, leaf, metadata, version, discovery=None):
        with self.connect() as con:
            for position, meta in enumerate(metadata, 1):
                meta = repository_metadata(meta)
                row = con.execute("SELECT status,reason,data FROM oss_candidate WHERE leaf=? AND repository_id=?", (leaf, meta["id"])).fetchone()
                old = json.loads(row["data"]) if row else {}
                changed = not row or old.get("version") != version or old.get("meta", {}).get("pushed_at") != meta.get("pushed_at")
                data = {**old, "meta": meta, "version": version, "discovered_at": old.get("discovered_at", now()), "last_seen_at": now(),
                        "source_changed": bool(row) and changed or old.get("source_changed", False)}
                if discovery is not None:
                    hit = {**discovery, "position": (discovery.get("page", 1) - 1) * 100 + position, "searched_at": now()}
                    previous_hits = [h for h in old.get("search_hits", [])
                                     if (h.get("query"), h.get("page")) != (hit.get("query"), hit.get("page"))]
                    data["search_hits"] = (previous_hits + [hit])[-40:]
                    data["search_verified_at"] = hit["searched_at"]
                con.execute("INSERT INTO oss_candidate VALUES (?,?,?,?,?) ON CONFLICT(leaf,repository_id) DO UPDATE SET status=excluded.status,reason=excluded.reason,data=excluded.data",
                            (leaf, meta["id"], "pending" if changed else row["status"], "等待分批读取官方资料" if changed else row["reason"], canonical(data)))

    def candidates(self, leaf=""):
        with self.connect() as con:
            return [{**dict(row), "data": json.loads(row["data"])} for row in con.execute(
                "SELECT * FROM oss_candidate WHERE (?='' OR leaf=?) ORDER BY repository_id", (leaf, leaf))]

    def scenarios(self, leaf):
        with self.connect() as con:
            return [{**json.loads(row["data"]), "leaf": row["leaf"]} for row in con.execute(
                "SELECT leaf,data FROM oss_scenario WHERE leaf=? ORDER BY position,id", (leaf,))]

    def candidate_counts(self, leaf):
        with self.connect() as con:
            return dict(con.execute("SELECT status,COUNT(*) FROM oss_candidate WHERE leaf=? GROUP BY status", (leaf,)))

    def candidate_result(self, leaf, repo_id, status, reason, metadata=None):
        with self.connect() as con:
            row = con.execute("SELECT data FROM oss_candidate WHERE leaf=? AND repository_id=?", (leaf, repo_id)).fetchone()
            data = json.loads(row[0])
            data.update(last_attempt_at=now(), attempts=data.get("attempts", 0) + 1, source_changed=False)
            if metadata:
                data["meta"] = repository_metadata(metadata)
            con.execute("UPDATE oss_candidate SET status=?,reason=?,data=? WHERE leaf=? AND repository_id=?",
                        (status, reason, canonical(data), leaf, repo_id))

    def _scenarios(self, con, scenarios, leaf=PILOT_LEAF, prune=True):
        current = {s["id"] for s in scenarios}
        for row in con.execute("SELECT id FROM oss_scenario WHERE leaf=?", (leaf,)).fetchall():
            if prune and row[0] not in current:
                con.execute("DELETE FROM oss_match WHERE scenario_id=?", (row[0],))
                con.execute("DELETE FROM oss_scenario WHERE id=?", (row[0],))
        for position, scenario in enumerate(scenarios):
            owner = con.execute("SELECT leaf FROM oss_scenario WHERE id=?", (scenario["id"],)).fetchone()
            if owner and owner[0] != leaf:
                raise CatalogError("场景 ID 已属于另一叶子")
            con.execute("INSERT INTO oss_scenario VALUES (?,?,?,?) ON CONFLICT(id) DO UPDATE SET data=excluded.data, position=excluded.position",
                        (scenario["id"], leaf, position, canonical({**scenario, "leaf": leaf})))

    def _upsert(self, con, card, leaf=PILOT_LEAF):
        card = {key: value for key, value in card.items() if key not in {"favorite", "leaves"}}
        key = card["repository_id"]
        old = con.execute("SELECT data FROM oss_project WHERE repository_id=?", (key,)).fetchone()
        for match in card["matches"]:
            owner = con.execute("SELECT leaf FROM oss_scenario WHERE id=?", (match["scenario_id"],)).fetchone()
            if not owner or owner[0] != leaf:
                raise CatalogError("项目关联必须属于本次更新的叶子")
        old_matches = [json.loads(row[0]) for row in con.execute(
            "SELECT m.data FROM oss_match m JOIN oss_scenario s ON s.id=m.scenario_id WHERE m.repository_id=? AND s.leaf=? ORDER BY m.scenario_id", (key, leaf))]
        fingerprint = content_digest({**card, "matches": []})
        same = old and content_digest({**json.loads(old[0]), "matches": []}) == fingerprint and canonical(old_matches) == canonical(sorted(card["matches"], key=lambda m: m["scenario_id"]))
        outcome = "created" if old is None else "unchanged" if same else "updated"
        con.execute("""INSERT INTO oss_project(repository_id,full_name,data,content_digest,checked_at) VALUES (?,?,?,?,?)
            ON CONFLICT(repository_id) DO UPDATE SET full_name=excluded.full_name,data=excluded.data,
            content_digest=excluded.content_digest,checked_at=excluded.checked_at""",
                    (key, card["full_name"], canonical(card), fingerprint, card["checked_at"]))
        con.execute("INSERT OR IGNORE INTO oss_leaf_project VALUES (?,?)", (leaf, key))
        # Replace only this pilot's associations. Other leaves can share the same
        # global repository record without losing their own matches.
        con.execute("DELETE FROM oss_match WHERE repository_id=? AND scenario_id IN (SELECT id FROM oss_scenario WHERE leaf=?)", (key, leaf))
        for match in card["matches"]:
            con.execute("INSERT INTO oss_match VALUES (?,?,?)", (match["scenario_id"], key, canonical(match)))
        return outcome

    def previous(self, full_name, leaf=None):
        with self.connect() as con:
            row = con.execute("SELECT repository_id,data FROM oss_project WHERE full_name=?", (full_name,)).fetchone()
            if not row:
                return None
            card = json.loads(row["data"])
            card["matches"] = [json.loads(m[0]) for m in con.execute(
                "SELECT m.data FROM oss_match m JOIN oss_scenario s ON s.id=m.scenario_id WHERE m.repository_id=? AND (? IS NULL OR s.leaf=?) ORDER BY m.scenario_id", (row["repository_id"], leaf, leaf))]
            return card

    def catalog(self, leaf="", q="", scenario="", license_status="", favorites=False,
                limit=None, offset=0, sort="name", overview=False):
        if len(q) > 200:
            raise CatalogError("搜索词过长")
        if license_status not in {"", "open_source", "source_available", "pending"}:
            raise CatalogError("许可证筛选无效")
        if (limit is not None and (type(limit) is not int or not 1 <= limit <= 100)) or type(offset) is not int or offset < 0:
            raise CatalogError("分页参数无效")
        if sort not in {"name", "recent", "recommended"}:
            raise CatalogError("排序参数无效")
        index = _CatalogIndex.get(self)
        with self.connect() as con:
            favorite_ids = {row[0] for row in con.execute("SELECT repository_id FROM oss_project WHERE favorite=1")}
            latest = con.execute("SELECT data FROM oss_run WHERE (?='' OR leaf=?) ORDER BY rowid DESC LIMIT 1", (leaf, leaf)).fetchone()
        scenarios = [dict(item) for item in index.scenarios if not leaf or item["leaf"] == leaf]
        allowed = {item["id"] for item in scenarios}
        needle = q.casefold()
        scenario_hits = {item["id"] for item in scenarios if needle and needle in index.scenario_text[item["id"]]}
        # Filtering, counts and sorting use the in-memory index; full cards are
        # read only for the returned page.
        selected = []
        for entry in index.entries:
            matched = [sid for sid in entry.matches if sid in allowed]
            if (leaf and leaf not in entry.leaves and not matched) or (not leaf and not entry.leaves and not matched) or (scenario and scenario not in matched):
                continue
            if license_status and entry.license != license_status:
                continue
            if favorites and entry.repository_id not in favorite_ids:
                continue
            if needle and needle not in entry.text and not any(needle in entry.matches[sid] or sid in scenario_hits for sid in matched):
                continue
            selected.append((entry, matched))
        scenario_leaf = {item["id"]: item["leaf"] for item in scenarios}
        scenario_counts = {}
        leaf_counts = {}
        for entry, matched in selected:
            for sid in matched:
                scenario_counts[sid] = scenario_counts.get(sid, 0) + 1
            for slug in set(entry.leaves) | {scenario_leaf[sid] for sid in matched}:
                leaf_counts[slug] = leaf_counts.get(slug, 0) + 1
        for item in scenarios:
            item["project_count"] = scenario_counts.get(item["id"], 0)
        total = len(selected)
        stats = {"projects": total, "scenarios": len(scenarios), "leaves": len(leaf_counts),
                 "favorites": sum(entry.repository_id in favorite_ids for entry, _ in selected)}
        if sort == "recent":
            selected.sort(key=lambda pair: (pair[0].checked_at, pair[0].full_name.casefold(), pair[0].repository_id), reverse=True)
        elif sort == "recommended":
            # Name hits first when searching, then active repositories by the
            # star count recorded at collection time. Stable for equal keys.
            selected.sort(key=lambda pair: (not (needle and needle in pair[0].title), pair[0].archived, -pair[0].stars))
        page = [] if overview else selected[offset:offset + limit if limit is not None else None]
        projects = self._cards(page, allowed, favorite_ids)
        if overview:
            # The landing page needs coverage counts and the pilot scenarios only.
            scenarios = [item for item in scenarios if item["leaf"] == PILOT_LEAF]
        elif not leaf and limit is not None:
            # A paged listing without a type filter returns only scenarios the
            # page can show; full reads (exports) keep every scenario.
            shown = {match["scenario_id"] for card in projects for match in card["matches"]} | {scenario}
            scenarios = [item for item in scenarios if item["id"] in shown]
        return {"leaf": leaf, "scenarios": scenarios, "projects": projects,
                "stats": stats,
                "pagination": {"total": total, "offset": offset, "limit": limit,
                               "has_more": not overview and offset + len(projects) < total},
                "discovery": {"total": 0, "counts": {}, "items": []} if overview else self._discovery(leaf),
                "latest_run": json.loads(latest[0]) if latest else None, "pilot_leaf": PILOT_LEAF,
                "supported_leaves": [{"slug": slug, "name": name, "mode": "curated" if slug == PILOT_LEAF else "automatic",
                                      "project_count": leaf_counts.get(slug, 0)}
                                     for slug, name in {PILOT_LEAF: "个人知识管理应用", **available_leaves()}.items()
                                     if not overview or slug in leaf_counts]}

    def _cards(self, page, allowed, favorite_ids):
        if not page:
            return []
        ids = [entry.repository_id for entry, _ in page]
        cards = {}
        matches = {}
        with self.connect() as con:
            for start in range(0, len(ids), 500):
                chunk = ids[start:start + 500]
                marks = ",".join("?" * len(chunk))
                for row in con.execute(f"SELECT repository_id,data FROM oss_project WHERE repository_id IN ({marks})", chunk):
                    cards[row[0]] = json.loads(row[1])
                for row in con.execute(f"SELECT repository_id,scenario_id,data FROM oss_match WHERE repository_id IN ({marks}) ORDER BY rowid", chunk):
                    if row[1] in allowed:
                        matches.setdefault(row[0], []).append(json.loads(row[2]))
        projects = []
        for entry, _ in page:
            card = cards.get(entry.repository_id)
            if card is None:
                continue
            card["favorite"] = entry.repository_id in favorite_ids
            card["leaves"] = list(entry.leaves)
            card["stars"] = entry.stars if entry.stars >= 0 else None
            card["matches"] = matches.get(entry.repository_id, [])
            projects.append(card)
        return projects

    def _discovery(self, leaf):
        # Candidate rows carry saved source material; never load it for a listing.
        with self.connect() as con:
            counts = dict(con.execute("SELECT status,COUNT(*) FROM oss_candidate WHERE (?='' OR leaf=?) GROUP BY status", (leaf, leaf)))
            items = [] if not leaf else [
                {"repository_id": row[0], "leaf": row[1], "full_name": row[2], "github_url": row[3], "status": row[4], "reason": row[5]}
                for row in con.execute("""SELECT repository_id,leaf,json_extract(data,'$.meta.full_name'),
                    json_extract(data,'$.meta.html_url'),status,reason FROM oss_candidate WHERE leaf=? ORDER BY repository_id""", (leaf,))]
        return {"total": sum(counts.values()),
                "counts": {state: counts.get(state, 0) for state in ("pending", "accepted", "partial", "rejected", "needs_evidence", "failed")},
                "items": items}

    def project(self, repo_id):
        """One card with all its type memberships and scenario associations."""
        index = _CatalogIndex.get(self)
        entry = next((item for item in index.entries if item.repository_id == repo_id), None)
        if entry is None:
            raise CatalogError("项目不存在", 404)
        with self.connect() as con:
            favorite_ids = {row[0] for row in con.execute("SELECT repository_id FROM oss_project WHERE favorite=1 AND repository_id=?", (repo_id,))}
        scenario_ids = set(entry.matches)
        cards = self._cards([(entry, list(entry.matches))], scenario_ids, favorite_ids)
        if not cards:
            raise CatalogError("项目不存在", 404)
        names = {PILOT_LEAF: "个人知识管理应用", **available_leaves()}
        scenarios = [dict(item) for item in index.scenarios if item["id"] in scenario_ids]
        for item in scenarios:
            item["leaf_name"] = names.get(item["leaf"], item["leaf"])
        slugs = list(dict.fromkeys([*entry.leaves, *(item["leaf"] for item in scenarios)]))
        return {"project": cards[0], "scenarios": scenarios,
                "leaves": [{"slug": slug, "name": names.get(slug, slug)} for slug in slugs]}

    def favorite(self, repo_id, value):
        if not isinstance(value, bool):
            raise CatalogError("favorite 必须是布尔值")
        def write():
            with self.connect() as con:
                return con.execute("UPDATE oss_project SET favorite=? WHERE repository_id=?", (int(value), repo_id)).rowcount
        if not _CatalogIndex.absorb_own_write(self, write):
            raise CatalogError("项目不存在", 404)
        return {"repository_id": repo_id, "favorite": value}

    def _lock(self):
        stream = self.path.with_suffix(".refresh.lock").open("a")
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            stream.close()
            raise CatalogError("已有更新正在运行，请等待完成", 409) from None
        return stream

    def run(self, run_id):
        with self.connect() as con:
            row = con.execute("SELECT data FROM oss_run WHERE id=?", (run_id,)).fetchone()
        if not row:
            raise CatalogError("更新记录不存在", 404)
        result = json.loads(row[0])
        if result["status"] == "running":
            try:
                lock = self._lock()
            except CatalogError:
                return result
            try:
                result.update(status="interrupted", finished_at=now())
                self._save_run(result)
            finally:
                lock.close()
        return result

    def _save_run(self, run):
        with self.connect() as con:
            con.execute("INSERT INTO oss_run VALUES (?,?,?,?) ON CONFLICT(id) DO UPDATE SET status=excluded.status,data=excluded.data",
                        (run["id"], run["leaf"], run["status"], canonical(run)))

    def refresh(self, client=None, background=False, leaf=PILOT_LEAF, recheck=False):
        validate_leaf(leaf)
        lock = self._lock()
        run = {"id": "oss_" + uuid.uuid4().hex, "leaf": leaf, "status": "running", "started_at": now(),
               "created": 0, "updated": 0, "unchanged": 0, "failed": 0, "processed": 0, "errors": []}
        try:
            # Holding the process lock proves no previous run is still alive.
            # Retire crash leftovers before publishing the new running record.
            with self.connect() as con:
                for row in con.execute("SELECT data FROM oss_run WHERE status='running'").fetchall():
                    previous_run = json.loads(row[0])
                    previous_run.update(status="interrupted", finished_at=now())
                    con.execute("UPDATE oss_run SET status='interrupted',data=? WHERE id=?",
                                (canonical(previous_run), previous_run["id"]))
            self._save_run(run)
        except BaseException:
            lock.close()
            raise

        def execute():
            try:
                if leaf != PILOT_LEAF:
                    from oss_workflow import discover_open_leaf
                    discover_open_leaf(self, leaf, run, github=client)
                    return run
                plan = manifest()
                with self.connect() as con:
                    self._scenarios(con, plan["scenarios"])
                run["total"] = len(plan["projects"])
                github = client or GitHub()
                for candidate in plan["projects"]:
                    try:
                        card = github.collect(candidate, self.previous(candidate["repo"], PILOT_LEAF))
                        with self.connect() as con:
                            outcome = self._upsert(con, card)
                        run[outcome] += 1
                    except Exception as error:
                        run["failed"] += 1
                        run["errors"].append({"repo": candidate["repo"], "error": str(error) if isinstance(error, CatalogError)
                                              else "项目更新失败，保留上次成功资料"})
                    run["processed"] += 1
                    self._save_run(run)
                run["status"] = "completed" if not run["failed"] else "partial" if run["failed"] < run["total"] else "failed"
            except ServiceUnavailable:
                run["status"] = "paused_model"
            except Exception:
                run["status"] = "failed"
                run["errors"].append({"error": "更新中断，已保存资料保留"})
            finally:
                run["finished_at"] = now()
                self._save_run(run)
                lock.close()
            return run

        if background:
            threading.Thread(target=execute, name=run["id"], daemon=True).start()
            return dict(run)
        return execute()

    def export(self, path):
        data = self.catalog(leaf=PILOT_LEAF)
        projects = [{k: v for k, v in card.items() if k != "favorite"} for card in data["projects"]]
        atomic_json(path, {"schema": "atlas.oss-catalog.v1", "exported_at": now(),
                           "scenarios": manifest()["scenarios"], "projects": projects})



_READY = set()


def _file_key(path):
    try:
        return str(Path(path).resolve()), os.stat(path).st_ino
    except OSError:
        return None


class _Entry:
    __slots__ = ("repository_id", "full_name", "checked_at", "license", "leaves", "matches", "text",
                 "title", "archived", "stars")

    def __init__(self, card, leaves, matches, stars):
        self.repository_id = card["repository_id"]
        self.full_name = card["full_name"]
        self.checked_at = card["checked_at"]
        self.license = card["license"]["status"]
        self.leaves = tuple(leaves)
        self.matches = matches
        self.title = (card["name"] + " " + card["full_name"]).casefold()
        self.archived = bool(card.get("archived"))
        self.stars = stars if isinstance(stars, int) else -1
        self.text = " ".join([card["name"], card["full_name"], card["positioning"], card["summary"], card["scope"],
                              *card["languages"], card["license"].get("spdx") or "",
                              *(f["text"] for f in card["features"])]).casefold()


class _CatalogIndex:
    """Lightweight searchable view of the catalog, rebuilt when the file changes.

    PRAGMA data_version on a dedicated connection reports commits made by any
    other connection, including batch workers. Large catalogs take seconds to
    index, so only while a batch job is active the view refreshes at most every
    30s; otherwise every committed change is visible on the next read.
    """

    _lock = threading.Lock()
    _items = {}

    def __init__(self, store):
        self.key = _file_key(store.path)
        self.watch = sqlite3.connect(store.path, timeout=10, check_same_thread=False)
        self.version = None
        self.built_at = 0.0
        self.duration = 0.0

    @classmethod
    def get(cls, store):
        key = _file_key(store.path)
        with cls._lock:
            index = cls._items.get(key[0] if key else None)
            if index is None or index.key != key:
                if index is not None:
                    index.watch.close()
                index = cls._items[key[0]] = cls(store)
            version = index.watch.execute("PRAGMA data_version").fetchone()[0]
            stale = version != index.version
            throttled = (index.duration > 1 and time.monotonic() - index.built_at < 30
                         and index.watch.execute("SELECT 1 FROM oss_batch_job WHERE status IN ('running','retry_wait') LIMIT 1").fetchone())
            if stale and not (index.version is not None and throttled):
                index.build(store, version)
            return index

    @classmethod
    def absorb_own_write(cls, store, write):
        """Run a write that cannot change indexed fields without forcing a rebuild."""
        key = _file_key(store.path)
        with cls._lock:
            index = cls._items.get(key[0] if key else None)
            before = index.watch.execute("PRAGMA data_version").fetchone()[0] if index else None
            result = write()
            if index is not None and index.version == before:
                index.version = index.watch.execute("PRAGMA data_version").fetchone()[0]
            return result

    def build(self, store, version):
        started = time.monotonic()
        with store.connect() as con:
            con.execute("BEGIN")
            self.scenarios = [{**json.loads(row["data"]), "leaf": row["leaf"]} for row in con.execute(
                "SELECT leaf,data FROM oss_scenario ORDER BY position,id")]
            matches = {}
            for rid, sid, data in con.execute("SELECT repository_id,scenario_id,data FROM oss_match ORDER BY rowid"):
                match = json.loads(data)
                matches.setdefault(rid, {})[sid] = " ".join([match.get("reason", ""), *match.get("conditions", [])]).casefold()
            leaves = {}
            for slug, rid in con.execute("SELECT leaf,repository_id FROM oss_leaf_project"):
                leaves.setdefault(rid, []).append(slug)
            # Star counts come from the search metadata saved with candidates.
            stars = dict(con.execute("""SELECT repository_id,MAX(json_extract(data,'$.meta.stargazers_count'))
                FROM oss_candidate GROUP BY repository_id"""))
            self.entries = [_Entry(json.loads(row[1]), leaves.get(row[0], []), matches.get(row[0], {}), stars.get(row[0]))
                            for row in con.execute("SELECT repository_id,data FROM oss_project ORDER BY full_name")]
        self.scenario_text = {s["id"]: (s["name"] + " " + s["description"]).casefold() for s in self.scenarios}
        self.version = version
        self.built_at = time.monotonic()
        self.duration = self.built_at - started


def dispatch(method, path, query, body=None):
    params = {key: values[-1] for key, values in parse_qs(query).items()}
    store = CatalogStore()
    if method == "GET" and path == "/api/oss/catalog":
        try:
            limit = int(params["limit"]) if "limit" in params else None
            offset = int(params.get("offset", "0"))
        except ValueError:
            raise CatalogError("分页参数无效") from None
        return store.catalog(leaf=params.get("leaf", ""), q=params.get("q", ""), scenario=params.get("scenario", ""),
                             license_status=params.get("license", ""), favorites=params.get("favorites") == "1",
                             limit=limit, offset=offset, sort=params.get("sort", "name"), overview=params.get("view") == "overview"), 200
    if path.startswith("/api/oss/batches"):
        from oss_batch import dispatch_batch
        return dispatch_batch(store, method, path, body)
    match = re.fullmatch(r"/api/oss/projects/(\d{1,12})", path)
    if method == "GET" and match:
        return store.project(int(match[1])), 200
    if method == "GET" and re.fullmatch(r"/api/oss/runs/oss_[0-9a-f]{32}", path):
        return store.run(path.rsplit("/", 1)[1]), 200
    if method == "POST":
        if not isinstance(body, dict):
            raise CatalogError("请求必须是 JSON 对象")
        if path == "/api/oss/refresh":
            if set(body) - {"leaf"}:
                raise CatalogError("更新参数无效")
            return store.refresh(background=True, leaf=body.get("leaf", PILOT_LEAF)), 202
        match = re.fullmatch(r"/api/oss/projects/(\d+)/favorite", path)
        if match and set(body) == {"favorite"}:
            return store.favorite(int(match[1]), body["favorite"]), 200
    raise CatalogError("接口不存在", 404)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["refresh", "inspect", "export", "discover"])
    parser.add_argument("--db")
    parser.add_argument("--query", default="topic:pkm archived:false")
    parser.add_argument("--output")
    args = parser.parse_args()
    if args.action == "discover":
        result = GitHub().discover(args.query)
        if args.output:
            atomic_json(args.output, result)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        raise SystemExit(0)
    store = CatalogStore(args.db)
    if args.action == "refresh":
        result = store.refresh()
        print(json.dumps(result, ensure_ascii=False, indent=2))
        raise SystemExit(0 if result["status"] == "completed" else 1)
    elif args.action == "export":
        output = args.output or DATA / "pilot.snapshot.json"
        store.export(output)
        print(output)
    else:
        data = store.catalog(PILOT_LEAF)
        print(json.dumps({"projects": len(data["projects"]), "scenarios": data["scenarios"], "latest_run": data["latest_run"]}, ensure_ascii=False, indent=2))
