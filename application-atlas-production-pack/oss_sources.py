"""Read bounded text documentation from a discovered repository, never source code."""
import json
from datetime import datetime, timezone
from pathlib import PurePosixPath
import re
from urllib.parse import quote, unquote, urlparse

from atlas_runtime import atomic_json
from oss_catalog import CatalogError, ServiceUnavailable, canonical, decode_file, digest, now, plain_text, repository_metadata, source_file

MAX_DOCUMENTS = 2


def allowed_document(path):
    lower = path.casefold()
    if any(part.startswith(".") for part in PurePosixPath(path).parts):
        return False
    if re.search(r"(?:^|/)(?:tests?|scripts?|src|client|contrib|node_modules|vendor|superpowers|plans?|proposals?|specs?|fastlane|resources|plugins)(?:/|$)", lower):
        return False
    if re.search(r"contribut|changelog|code.of.conduct|code.review|style.*(?:guide|practice)|privacy|symbolicat|licen[cs]e|third.party|security|/adr/|dependenc|pull.request|template", lower):
        return False
    if re.search(r"readme[-_.](?!en(?:\.|$)|zh(?:[-_.]|$)|cn(?:\.|$))[a-z]{2}(?:[-_.]|$)", lower):
        return False
    return True


def document_paths(tree, readme, repository):
    paths = {item["path"] for item in tree.get("tree", []) if item.get("type") == "blob"
             and re.search(r"\.(md|rst|txt)$", item.get("path", ""), re.I)}
    linked = set()
    for link in re.findall(r"\]\(([^\s)#]+)", decode_file(readme)):
        parsed = urlparse(link)
        if parsed.scheme:
            prefix = f"https://github.com/{repository}/blob/"
            if not link.startswith(prefix):
                continue
            parts = parsed.path.split("/", 5)
            link = parts[5] if len(parts) > 5 else ""
        else:
            link = str(PurePosixPath(readme["path"]).parent / parsed.path)
        linked.add(unquote(link).removeprefix("./"))

    def score(path):
        lower = path.casefold()
        if path == readme["path"] or not allowed_document(path):
            return -1
        value = 8 if path in linked else 0
        value += 6 if re.search(r"feature|autofill|getting.started|user.guide|usage|manual|sharing|quickstart|overview", lower) else 0
        value += 3 if value and lower.startswith(("docs/", "doc/", "documentation/")) else 0
        value += 2 if PurePosixPath(lower).name.startswith("readme") else 0
        return value

    return sorted((p for p in paths if score(p) > 0), key=lambda p: (-score(p), p.count("/"), p))[:MAX_DOCUMENTS]


def archive_evidence(root, files):
    """Keep successfully read immutable text even when a sibling request fails."""
    for file in files:
        if not file or not file.get("git_url"):
            continue
        try:
            body = decode_file(file)
        except (CatalogError, UnicodeError):
            continue
        key = digest(canonical({"url": file["git_url"], "sha256": digest(body)}))
        path = root / "evidence" / (key + ".json")
        if not path.exists():
            atomic_json(path, {"file": {k: file[k] for k in ("git_url", "html_url", "path", "sha", "encoding", "content", "size") if k in file},
                               "sha256": digest(body), "retrieved_at": now()})


def collect_sources(github, meta, root, run, allow_partial=False, *, include_documents=True, search_verified_at=None):
    recent_search = False
    try:
        age = (datetime.now(timezone.utc) - datetime.fromisoformat(search_verified_at)).total_seconds()
        cached_key = digest(canonical({"id": meta["id"], "pushed_at": meta["pushed_at"], "branch": meta["default_branch"]}))
        cached_path = root / "sources" / (cached_key + ".json")
        cached_public = json.loads(cached_path.read_text()) if cached_path.exists() else {}
        cache_only = (not include_documents and cached_public.get("readme") and not cached_public.get("warnings")
                      and len(plain_text(decode_file(cached_public["readme"]))) >= 400)
        recent_search = (-300 <= age <= 86400 and meta.get("private") is False and not meta.get("disabled")
                         and meta.get("visibility") != "private"
                         and meta.get("url") == "https://api.github.com/repos/" + meta["full_name"]
                         and meta.get("html_url") == "https://github.com/" + meta["full_name"] and cache_only)
    except (TypeError, ValueError, KeyError):
        pass
    if recent_search:
        # This branch uses previously archived public files only. Fresh file or
        # supplementary-document fetches always recheck current visibility.
        current = dict(meta)
        identity_verified_at = search_verified_at
        run["search_identity_reuses"] = run.get("search_identity_reuses", 0) + 1
    else:
        current = github.get("/repositories/" + str(meta["id"]))
        identity_verified_at = now()
        run["repository_checks"] = run.get("repository_checks", 0) + 1
    if current.get("id") != meta["id"] or current.get("private") or current.get("visibility") == "private" or current.get("disabled"):
        raise CatalogError("仓库身份已变化或不再公开，停止采集并保留历史资料", 422)
    meta.clear()
    meta.update(repository_metadata(current))
    key = digest(canonical({"id": meta["id"], "pushed_at": meta["pushed_at"], "branch": meta["default_branch"]}))
    path = root / "sources" / (key + ".json")
    cached = path.exists()
    if cached:
        resources = json.loads(path.read_text())
        run["source_cache_hits"] += 1
    else:
        run["source_fetches"] += 1
        warnings = []
        try:
            readme = github.get("/repos/" + meta["full_name"] + "/readme")
        except ServiceUnavailable:
            raise
        except CatalogError as error:
            if not allow_partial:
                raise
            readme = None
            warnings.append("README：" + str(error))
        try:
            license_file = github.get("/repos/" + meta["full_name"] + "/license")
        except ServiceUnavailable:
            archive_evidence(root, [readme])
            raise
        except CatalogError as error:
            if "不存在" not in str(error) and not allow_partial:
                raise
            license_file = None
            if "不存在" not in str(error):
                warnings.append("LICENSE：" + str(error))
        resources = {"readme": readme, "license": license_file, "retrieved_at": now(), "warnings": warnings}
        if not warnings:
            atomic_json(path, resources)
    # A GitHub file endpoint can return an empty file, symlink, or encoding:none.
    # That is missing text evidence, not a reason to discard a public project.
    resources = {**resources, "warnings": list(resources.get("warnings", []))}
    if allow_partial:
        for kind in ("readme", "license"):
            if resources.get(kind):
                try:
                    decode_file(resources[kind])
                except (CatalogError, UnicodeError):
                    resources[kind] = None
                    resources["warnings"].append(kind.upper() + " 未返回可读文本；先依据其余官方资料收录")
    # First-round collection reads README and LICENSE first. A short/missing
    # README still gets the existing supplementary-document fallback. Never
    # cache deferred documentation as an empty completed lookup.
    readme_sufficient = resources.get("readme") and len(plain_text(decode_file(resources["readme"]))) >= 400
    if not include_documents and readme_sufficient:
        if resources.get("warnings"):
            archive_evidence(root, [resources.get("readme"), resources.get("license")])
        return {**resources, "documents": [], "supplemental_documents_deferred": True,
                "identity_verified_at": identity_verified_at}, cached
    docs_path = root / "documentation" / (key + ".json")
    if docs_path.exists():
        docs = json.loads(docs_path.read_text())
        docs["documents"] = [d for d in docs["documents"] if allowed_document(d["file"]["path"])]
        run["document_cache_hits"] += len(docs["documents"])
    else:
        docs = {"documents": [], "warnings": []}
        try:
            tree = github.get("/repos/" + meta["full_name"] + "/git/trees/" + quote(meta.get("default_branch") or "HEAD", safe="") + "?recursive=1")
            paths = document_paths(tree, resources["readme"] or {"path": "README.md", "encoding": "base64", "content": "Cg=="}, meta["full_name"])
            if tree.get("truncated"):
                docs["warnings"].append("官方文档目录结果被 GitHub 截断")
            for selected in paths:
                file = github.get("/repos/" + meta["full_name"] + "/contents/" + quote(selected, safe="/") + "?ref=" + quote(meta["default_branch"], safe=""))
                decode_file(file)
                docs["documents"].append({"file": file, "retrieved_at": now()})
                run["document_fetches"] += 1
            atomic_json(docs_path, docs)
        except ServiceUnavailable:
            archive_evidence(root, [resources.get("readme"), resources.get("license"), *[d["file"] for d in docs["documents"]]])
            raise
        except CatalogError as error:
            docs["warnings"].append(str(error))
            # A failed document lookup is retried later, never cached as absence.
    if resources.get("warnings") or docs.get("warnings"):
        archive_evidence(root, [resources.get("readme"), resources.get("license"), *[d["file"] for d in docs["documents"]]])
    return {**resources, **docs, "warnings": resources.get("warnings", []) + docs.get("warnings", []),
            "identity_verified_at": identity_verified_at}, cached


def documents(resources, repository):
    result = []
    items = ([{"file": resources["readme"], "retrieved_at": resources["retrieved_at"]}] if resources.get("readme") else [])
    items += [d for d in resources.get("documents", []) if allowed_document(d["file"]["path"])]
    for index, item in enumerate(items):
        raw = decode_file(item["file"])
        is_readme = item["file"] is resources.get("readme")
        source = source_file(repository, "readme" if is_readme else "documentation", item["file"], raw)
        source["retrieved_at"] = item["retrieved_at"]
        result.append({"source_id": "readme" if is_readme else f"doc-{index}", "text": plain_text(raw)[:24000 if is_readme else 10000], "source": source})
    return result
