"""Fetch pinned public GitHub sources as data; never run repository hooks."""

from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
import re
import tarfile
import urllib.request
from urllib.parse import urlsplit

from .artifacts import IGNORED, MAX_FILES, MAX_TOTAL, relative
from .store import FactoryError


def source_storage_root(store_root):
    """Return the stable logical ``sources`` entry after validating any alias.

    A linked entry is deliberately returned by its original path so snapshots
    continue to record the same local_root string after storage is moved. Its
    target must already exist; a broken link must never fall back to a local
    directory with the same name.
    """
    entry = Path(store_root) / "sources"
    if entry.is_symlink():
        try:
            target = entry.resolve(strict=True)
        except OSError as error:
            raise FactoryError(
                "source storage alias is unavailable", "source_storage_unavailable", 503
            ) from error
        if not target.is_dir():
            raise FactoryError(
                "source storage alias target is not a directory",
                "source_storage_unavailable",
                503,
            )
    elif entry.exists() and not entry.is_dir():
        raise FactoryError(
            "source storage entry is not a directory", "source_storage_unavailable", 503
        )
    return entry


class FixedRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise FactoryError("unexpected source redirect", "source_download_failed", 502)


def github_repo(value):
    if not isinstance(value, str):
        raise FactoryError("source must be a public GitHub repository URL")
    parsed = urlsplit(value)
    if (
        parsed.scheme != "https"
        or parsed.netloc != "github.com"
        or parsed.query
        or parsed.fragment
    ):
        raise FactoryError("source must be https://github.com/owner/repository")
    match = re.fullmatch(
        r"/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?:\.git)?/?", parsed.path
    )
    if not match or match[1] in {".", ".."} or match[2] in {".", ".."}:
        raise FactoryError("invalid GitHub repository URL")
    return match[1] + "/" + match[2]


def request_bytes(url, limit=2_000_000, *, timeout=45):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Atlas-Template-Factory/1",
            "Accept": "application/vnd.github+json",
        },
    )
    try:
        with urllib.request.build_opener(FixedRedirect()).open(
            request, timeout=timeout
        ) as response:
            body = response.read(limit + 1)
    except FactoryError:
        raise
    except OSError as error:
        raise FactoryError(
            f"public source request failed: {type(error).__name__}; retry or select another source",
            "source_download_failed",
            502,
        ) from error
    if len(body) > limit:
        raise FactoryError("source response exceeds download limit")
    return body


def resolve_commit(repository, commit=None, fetch=request_bytes):
    """Resolve once, then persist the returned SHA before downloading data."""
    repo = github_repo(repository)
    if commit is not None and (
        not isinstance(commit, str) or not re.fullmatch(r"[a-f0-9]{40}", commit)
    ):
        raise FactoryError("source commit must be a full lowercase SHA")
    resolved = json.loads(fetch(f"https://api.github.com/repos/{repo}/commits/{commit or 'HEAD'}"))
    sha = resolved.get("sha")
    if not isinstance(sha, str) or not re.fullmatch(r"[a-f0-9]{40}", sha) or (commit and sha != commit):
        raise FactoryError("source did not resolve to the requested immutable commit")
    return sha


def fetch_source(repository, destination, fetch=request_bytes, *, commit=None):
    repo = github_repo(repository)
    metadata = json.loads(fetch(f"https://api.github.com/repos/{repo}"))
    sha = resolve_commit(repository, commit, fetch)
    license_info = metadata.get("license") or {}
    license_id = license_info.get("spdx_id")
    if not license_id or license_id in {"NOASSERTION", "NONE"}:
        raise FactoryError(
            "source license is missing or unclear; choose another source or review it",
            "license_review_required",
            409,
        )
    data = fetch(f"https://codeload.github.com/{repo}/tar.gz/{sha}", 64 * 1024 * 1024)
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=False)
    skipped, total, count, notices = [], 0, 0, {}
    with tarfile.open(fileobj=io.BytesIO(data), mode="r|gz") as archive:
        top = None
        for entry_count, member in enumerate(archive):
            if entry_count >= MAX_FILES * 2:
                raise FactoryError("source archive contains too many entries")
            parts = member.name.split("/")
            if top is None:
                top = parts[0]
            if parts[0] != top or parts[0] in {"", ".", ".."}:
                raise FactoryError("invalid source archive root")
            rel = "/".join(parts[1:]).rstrip("/")
            if not rel:
                continue
            if (
                member.issym()
                or member.islnk()
                or not (member.isfile() or member.isdir())
            ):
                raise FactoryError(
                    "source contains links or special files; manual conversion required"
                )
            if (
                any(p in {"..", ".", ""} for p in rel.split("/"))
                or rel.startswith("/")
                or "\\" in rel
            ):
                raise FactoryError("unsafe source archive path")
            if member.isdir():
                continue
            total += member.size
            count += 1
            if total > MAX_TOTAL or count > MAX_FILES:
                raise FactoryError("source archive exceeds extraction limits")
            if any(p in IGNORED for p in rel.split("/")):
                skipped.append(rel)
                continue
            try:
                relative(rel)
            except FactoryError:
                skipped.append(rel)
                continue
            target = destination / rel
            if target.exists():
                raise FactoryError("duplicate source archive entry")
            target.parent.mkdir(parents=True, exist_ok=True)
            stream = archive.extractfile(member)
            if stream is None:
                raise FactoryError("source archive entry is unreadable")
            content = stream.read()
            target.write_bytes(content)
            if target.name.lower().startswith(("license", "copying", "notice")):
                notices[rel] = hashlib.sha256(content).hexdigest()
    if not notices:
        raise FactoryError(
            "license metadata has no corresponding notice in the source archive",
            "license_review_required",
            409,
        )
    return {
        "repository": "https://github.com/" + repo,
        "repository_id": metadata.get("id"),
        "default_branch": metadata.get("default_branch"),
        "commit": sha,
        "license": license_id,
        "notice_hashes": notices,
        "archive_sha256": hashlib.sha256(data).hexdigest(),
        "excluded_paths": skipped,
    }
