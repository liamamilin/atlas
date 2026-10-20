"""Lossless, deterministic reading materials for the narrowly scoped frozen review."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Iterable

SCHEMA = "atlas.frozen-review-materials.v1"
CONFIG_SCHEMA = "atlas.frozen-review-readonly-config.v1"
READ_LINE_LIMIT = 2000
SEGMENT_TARGET_BYTES = 1600

PROMPT_APPEND = """

Frozen-review reading materials:
- Read review-materials/INDEX.md first. The registered files there are lossless UTF-8 presentations of long strings from the original input.json, leaf.md, or frozen source/; they are not summaries.
- Read every indexed review diff and text through its end. When an entry lists offset segments, read every part and use the offsets to reconstruct the exact physical line; segment boundaries are display-only. Continue paged reads until the file ends.
- If identical original text has multiple origins, one byte-verified derived copy is sufficient; the manifest preserves every origin. All original source/ remains available and must be checked against its presentation.
- Preserve the original eight review dimensions, assertions, repair scope, existing unknowns, and suggestions. No outside historical review conclusions are added. Do not assume a pass; mark uncertain when evidence is insufficient.
- Final `files` references may name only existing frozen files in input.source_inventory. review-materials/, its manifest, leaf.md, and input.json are reading context, not frozen files or new case facts.
""".strip()


def _sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _canonical(value) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _pointer(parts: Iterable[object]) -> str:
    return "".join("/" + str(p).replace("~", "~0").replace("/", "~1") for p in parts)


def _walk(value, parts=()):
    if isinstance(value, dict):
        for key in sorted(value):
            yield from _walk(value[key], (*parts, key))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from _walk(item, (*parts, index))
    elif isinstance(value, str):
        yield parts, value


def _line_stats(raw: bytes):
    lines = raw.splitlines(keepends=True)
    if not lines and raw:
        lines = [raw]
    lengths = [len(line.rstrip(b"\r\n")) for line in lines]
    return {"line_count": len(lines), "max_physical_line_bytes": max(lengths, default=0)}


def _utf8_chunks(raw: bytes, target: int):
    start = 0
    while start < len(raw):
        end = min(len(raw), start + target)
        while end > start:
            try:
                raw[start:end].decode("utf-8", errors="strict")
                break
            except UnicodeDecodeError:
                end -= 1
        if end == start:
            raise ValueError("could not find a UTF-8 segment boundary")
        yield start, end, raw[start:end]
        start = end


def _target_paths(parts):
    parts = list(parts)
    for marker in ("program_diffs", "files"):
        if marker in parts:
            i = parts.index(marker)
            if i + 1 < len(parts) and isinstance(parts[i + 1], str):
                return [parts[i + 1]]
    if "architecture_markdown" in parts:
        return ["ARCHITECTURE.md"]
    return []


def _extension(parts):
    if "program_diffs" in parts or "unified_diff" in parts:
        return ".diff"
    if "architecture_markdown" in parts or "leaf" in parts:
        return ".md"
    return ".txt"


def _load_json(raw: bytes, label: str):
    try:
        return json.loads(raw.decode("utf-8", errors="strict"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{label} must be valid UTF-8 JSON") from exc


def build_materials(input_bytes: bytes, leaf_bytes: bytes, source_dir: Path) -> dict:
    """Return exact derived reading files and their source/hash/index manifest.

    The supplied originals are read only. Extracted JSON string values are emitted
    byte-for-byte after UTF-8 decoding; duplicate values share one display file
    while retaining every pointer in `origins`.
    """
    if not isinstance(input_bytes, bytes) or not isinstance(leaf_bytes, bytes):
        raise TypeError("input_bytes and leaf_bytes must be bytes")
    source_dir = Path(source_dir)
    if source_dir.is_symlink() or not source_dir.is_dir():
        raise ValueError("source_dir must be a regular directory")
    input_doc = _load_json(input_bytes, "input.json")
    leaf_bytes.decode("utf-8", errors="strict")
    source_files = []
    for path in sorted(source_dir.rglob("*")):
        if path.is_symlink():
            raise ValueError("source tree contains a symlink")
        if not path.is_file():
            continue
        raw = path.read_bytes()
        rel = path.relative_to(source_dir).as_posix()
        source_files.append({"path": rel, "sha256": _sha(raw), "bytes": len(raw), **_line_stats(raw)})
    source_tree_digest = _tree_digest({row["path"]: source_dir.joinpath(*row["path"].split("/")).read_bytes() for row in source_files})

    extracted = []
    scan = {"line_limit_bytes": READ_LINE_LIMIT, "input_json": _line_stats(input_bytes),
            "leaf_md": _line_stats(leaf_bytes), "source_files": source_files,
            "long_json_strings": [], "long_physical_lines": []}

    def scan_raw_lines(raw: bytes, relative_path: str, *, encoded_json: bool):
        offset = 0
        for line_number, line in enumerate(raw.splitlines(keepends=True), 1):
            visible = line.rstrip(b"\r\n")
            if len(visible) > READ_LINE_LIMIT:
                scan["long_physical_lines"].append({"origin": {"relative_path": relative_path,
                    "line": line_number, "byte_offset": offset, "byte_length": len(line),
                    "json_encoded_line": encoded_json}, "bytes": len(visible)})
            offset += len(line)

    scan_raw_lines(input_bytes, "input.json", encoded_json=True)
    scan_raw_lines(leaf_bytes, "leaf.md", encoded_json=False)
    for row in source_files:
        raw = source_dir.joinpath(*row["path"].split("/")).read_bytes()
        scan_raw_lines(raw, "source/" + row["path"], encoded_json=row["path"].lower().endswith(".json"))

    def add_text(raw: bytes, origin: dict, label_parts=(), *, force=False):
        if len(raw) <= READ_LINE_LIMIT and not force:
            return
        raw.decode("utf-8", errors="strict")
        origin = {**origin, "raw_sha256": _sha(raw)}
        stats = _line_stats(raw)
        extracted.append({"raw": raw, "origin": origin, "target_paths": _target_paths(label_parts),
                          "extension": _extension(label_parts), "stats": stats})
        if stats["max_physical_line_bytes"] > READ_LINE_LIMIT:
            scan["long_physical_lines"].append({"origin": origin, **stats})

    for parts, value in _walk(input_doc):
        raw = value.encode("utf-8")
        required_diff = "program_diffs" in parts
        if len(raw) > READ_LINE_LIMIT or required_diff:
            origin = {"relative_path": "input.json", "json_pointer": _pointer(parts)}
            if len(raw) > READ_LINE_LIMIT:
                scan["long_json_strings"].append({"origin": origin, "bytes": len(raw), **_line_stats(raw)})
            add_text(raw, origin, parts, force=required_diff)
    # leaf.md is deliberately independently included even when identical to input.leaf.content.
    add_text(leaf_bytes, {"relative_path": "leaf.md", "json_pointer": None}, ("leaf",))

    # JSON source files may contain readable semantic text in minified/escaped fields.
    for row in source_files:
        rel = row["path"]
        raw_file = source_dir.joinpath(*rel.split("/")).read_bytes()
        try:
            parsed = _load_json(raw_file, "source/" + rel) if rel.lower().endswith(".json") else None
        except ValueError:
            parsed = None
        if parsed is not None:
            for parts, value in _walk(parsed):
                encoded = value.encode("utf-8")
                required_diff = "program_diffs" in parts
                if len(encoded) > READ_LINE_LIMIT or required_diff:
                    origin = {"relative_path": "source/" + rel, "json_pointer": _pointer(parts)}
                    if len(encoded) > READ_LINE_LIMIT:
                        scan["long_json_strings"].append({"origin": origin, "bytes": len(encoded), **_line_stats(encoded)})
                    add_text(encoded, origin, parts, force=required_diff)
        elif row["max_physical_line_bytes"] > READ_LINE_LIMIT:
            # Keep an exact raw line display for non-JSON files only. JSON long
            # lines are presented via their decoded string pointers above.
            offset = 0
            for line_number, line in enumerate(raw_file.splitlines(keepends=True), 1):
                content = line.rstrip(b"\r\n")
                if len(content) > READ_LINE_LIMIT:
                    origin = {"relative_path": "source/" + rel, "line": line_number,
                              "byte_offset": offset, "byte_length": len(line)}
                    add_text(line, origin, (rel,))
                offset += len(line)

    # Dedupe only byte-identical strings, retaining every original source pointer.
    groups = {}
    for item in extracted:
        groups.setdefault(item["raw"], []).append(item)
    ordered = sorted(groups.items(), key=lambda pair: (pair[1][0]["origin"]["relative_path"],
                                                       pair[1][0]["origin"].get("json_pointer") or "",
                                                       _sha(pair[0])))
    files: dict[str, bytes] = {}
    manifest_entries = []
    segment_entries = []
    for number, (raw, items) in enumerate(ordered, 1):
        path = f"text/{number:04d}{items[0]['extension']}"
        files[path] = raw
        origins = [item["origin"] for item in items]
        stats = _line_stats(raw)
        manifest_entries.append({"path": path, "sha256": _sha(raw), "bytes": len(raw),
                                 **stats, "origins": origins,
                                 "target_paths": sorted({p for item in items for p in item["target_paths"]})})
        # Present every truly overlong physical line as explicit exact byte slices.
        offset = 0
        for line_number, line in enumerate(raw.splitlines(keepends=True), 1):
            visible = line.rstrip(b"\r\n")
            if len(visible) > READ_LINE_LIMIT:
                pieces = []
                for piece_number, (start, end, part) in enumerate(_utf8_chunks(visible, SEGMENT_TARGET_BYTES), 1):
                    piece_path = f"segments/{number:04d}-line-{line_number:04d}-part-{piece_number:04d}.txt"
                    files[piece_path] = part
                    pieces.append({"path": piece_path, "start_byte": offset + start,
                                   "end_byte": offset + end, "sha256": _sha(part), "bytes": len(part)})
                segment_entries.append({"display_only": True, "original_path": path,
                                        "line_number": line_number, "line_start_byte": offset,
                                        "line_end_byte": offset + len(line), "parts": pieces,
                                        "roundtrip_sha256": _sha(visible), "newline_bytes": line[len(visible):].hex()})
            offset += len(line)

    index_lines = ["# Frozen review reading index", "",
                   "Derived texts below preserve exact UTF-8 source bytes; this index contains no review summary.",
                   "Read each listed item to EOF. Segment parts are display-only and reconstruct by byte offsets.", ""]
    for row in manifest_entries:
        index_lines.append(f"- `{row['path']}` — {row['bytes']} bytes, {row['line_count']} physical lines, max line {row['max_physical_line_bytes']} bytes; origins: "
                           + "; ".join(f"`{o['relative_path']}`{o.get('json_pointer') or ''}" for o in row["origins"]))
        segments = [s for s in segment_entries if s["original_path"] == row["path"]]
        for segment in segments:
            index_lines.append("  - Long line " + str(segment["line_number"]) + ": " + ", ".join("`" + p["path"] + "`" for p in segment["parts"]) + " (exact byte offsets in manifest)")
    index_bytes = ("\n".join(index_lines).rstrip() + "\n").encode("utf-8")
    files["INDEX.md"] = index_bytes
    manifest = {
        "schema": SCHEMA,
        "source_identity": {"input.json": {"sha256": _sha(input_bytes), "bytes": len(input_bytes)},
                            "leaf.md": {"sha256": _sha(leaf_bytes), "bytes": len(leaf_bytes)},
                            "source_tree_digest": source_tree_digest, "source_files": source_files},
        "scan": scan,
        "entries": manifest_entries,
        "segments": segment_entries,
        "allowed_paths": sorted({"INDEX.md", "manifest.json", *files.keys()}),
        "file_hashes": {path: _sha(raw) for path, raw in sorted(files.items())},
        "tree_digest_algorithm": "sha256(sorted(relative_path + NUL + sha256(file_bytes) + LF))",
    }
    manifest_raw = json.dumps(manifest, ensure_ascii=False, indent=2).encode("utf-8") + b"\n"
    files["manifest.json"] = manifest_raw
    return {"files": files, "manifest": manifest, "manifest_digest": _sha(manifest_raw),
            "tree_digest": _tree_digest(files), "source_tree_digest": source_tree_digest,
            "source_identities": manifest["source_identity"], "scan": scan}


def _tree_digest(files: dict[str, bytes]) -> str:
    h = hashlib.sha256()
    for path, raw in sorted(files.items()):
        h.update(path.encode("utf-8"))
        h.update(b"\0")
        h.update(_sha(raw).encode("ascii"))
        h.update(b"\n")
    return h.hexdigest()


def append_review_prompt(original_prompt: str):
    if not isinstance(original_prompt, str):
        raise TypeError("original_prompt must be str")
    appended = "\n\n" + PROMPT_APPEND
    result = original_prompt + appended
    return result, {"old_prompt_sha256": _sha(original_prompt.encode("utf-8")),
                    "append_text": appended, "append_sha256": _sha(appended.encode("utf-8")),
                    "new_prompt_sha256": _sha(result.encode("utf-8"))}


def _base_config(directory: Path):
    directory = Path(directory).resolve()
    relative = ["input.json", "leaf.md", "source", "source/**"]
    reads = relative + [str(directory / item) for item in relative]
    rules = [{"action": "*", "resource": "*", "effect": "deny"}]
    rules.extend({"action": "read", "resource": item, "effect": "allow"} for item in reads)
    agent_name = "atlas-factory-" + _sha(str(directory).encode())[:12]
    return {"$schema": "https://opencode.ai/config.json", "permissions": rules,
            "agents": {agent_name: {"mode": "primary", "description": "Atlas read-only factory proposal agent", "permissions": rules}},
            "policies": [{"action": action, "resource": resource, "effect": "deny"} for action, resource in
                         [("tool.use", "shell:*"), ("tool.use", "execute:*"), ("plugin.use", "*"),
                          ("mcp.use", "*"), ("skill.use", "*")]]}


def _manifest_paths(manifest: dict):
    if not isinstance(manifest, dict) or manifest.get("schema") != SCHEMA:
        raise ValueError("unknown frozen-review material manifest")
    paths = manifest.get("allowed_paths")
    if not isinstance(paths, list) or not paths or len(paths) != len(set(paths)):
        raise ValueError("manifest allowed_paths must be a unique path list")
    normalized = []
    for value in paths:
        if (not isinstance(value, str) or value.startswith("/") or "\\" in value
                or any(part in {"", ".", ".."} for part in value.split("/"))):
            raise ValueError("manifest contains an unsafe derived path")
        normalized.append("review-materials/" + value)
    all_paths = set(normalized)
    all_paths.add("review-materials")
    for path in normalized:
        parent = Path(path).parent
        while parent.as_posix() != "review-materials":
            all_paths.add(parent.as_posix())
            parent = parent.parent
    return sorted(all_paths)


def registered_read_resources(attempt_dir: Path, *, expected_manifest_digest: str | None = None,
                              expected_tree_digest: str | None = None):
    """Verify the persisted derived tree and return exact relative/absolute ACL reads.

    The attempt path is trusted from the worker's resolved task directory. All
    names below it come from the strict manifest schema and are checked against
    the actual regular-file inventory before any path is returned.
    """
    attempt_dir = Path(attempt_dir).resolve()
    root = attempt_dir / "review-materials"
    if root.is_symlink() or not root.is_dir():
        raise ValueError("review-materials is missing or not a regular directory")
    manifest_path = root / "manifest.json"
    if manifest_path.is_symlink() or not manifest_path.is_file():
        raise ValueError("review-materials manifest is missing or unsafe")
    manifest_raw = manifest_path.read_bytes()
    if expected_manifest_digest is not None and _sha(manifest_raw) != expected_manifest_digest:
        raise ValueError("review-materials manifest digest differs from the binding")
    manifest = _load_json(manifest_raw, "review-materials/manifest.json")
    # Validate the schema and every path before using the inventory. This also
    # rejects traversal, backslashes, and malformed duplicate path lists.
    _manifest_paths(manifest)
    paths = manifest.get("allowed_paths") if isinstance(manifest, dict) else None
    hashes = manifest.get("file_hashes") if isinstance(manifest, dict) else None
    if (not isinstance(paths, list) or not isinstance(hashes, dict)
            or set(hashes) != set(paths) - {"manifest.json"}
            or "manifest.json" not in paths or len(paths) != len(set(paths))):
        raise ValueError("review-materials path/hash inventory is invalid")
    expected = set(paths)
    actual = set()
    material_bytes = {}
    for path in root.rglob("*"):
        if path.is_symlink():
            raise ValueError("review-materials contains a symlink")
        if path.is_file():
            rel = path.relative_to(root).as_posix()
            actual.add(rel)
            material_bytes[rel] = path.read_bytes()
    if actual != expected:
        raise ValueError("review-materials contains missing or unregistered files")
    for rel, expected_hash in hashes.items():
        if _sha(material_bytes[rel]) != expected_hash:
            raise ValueError("review-materials file hash differs from manifest: " + rel)
    tree = _tree_digest(material_bytes)
    if expected_tree_digest is not None and tree != expected_tree_digest:
        raise ValueError("review-materials tree digest differs from the binding")
    # Every directory needed to traverse nested paths is an explicit read; no wildcard is granted.
    relative = {"review-materials"}
    for rel in paths:
        parts = Path("review-materials") / rel
        relative.add(parts.as_posix())
        parent = parts.parent
        while parent.as_posix() != "review-materials":
            relative.add(parent.as_posix())
            parent = parent.parent
    relative = sorted(relative)
    return {"relative": relative,
            "absolute": [str((attempt_dir / path).resolve()) for path in relative],
            "manifest_digest": _sha(manifest_raw), "tree_digest": tree,
            "manifest": manifest}


def extend_readonly_config(original_config: dict, original_attempt_dir: Path,
                           effective_attempt_dir: Path, manifest: dict):
    """Verify archived base ACL, then add exact derived reads and return identity."""
    if original_config != _base_config(Path(original_attempt_dir)):
        raise ValueError("original cognitive-review config is not the exact deny-by-default read-only config")
    effective_attempt_dir = Path(effective_attempt_dir).resolve()
    config = _base_config(effective_attempt_dir)
    relatives = _manifest_paths(manifest)
    extra = [*relatives, *(str((effective_attempt_dir / rel).resolve()) for rel in relatives)]
    additional_rules = [{"action": "read", "resource": path, "effect": "allow"} for path in extra]
    config["permissions"].extend(additional_rules)
    agent = next(iter(config["agents"].values()))
    agent["permissions"] = config["permissions"]
    identity = {"schema": CONFIG_SCHEMA, "default_permission": "deny",
                "relative_read_resources": ["input.json", "leaf.md", "source", "source/**", *relatives],
                "absolute_material_reads": ["{attempt}/" + path for path in relatives],
                "agent": {"name": "atlas-factory-{attempt_sha256_12}", "mode": "primary",
                          "description": "Atlas read-only factory proposal agent"},
                "policies": config["policies"], "materials_manifest_digest": _sha(_canonical(manifest)),
                "config_digest": _sha(_canonical(_normalized_config(config, effective_attempt_dir)))}
    return config, identity


def validate_readonly_config(config: dict, effective_attempt_dir: Path, manifest: dict,
                             expected_identity: dict | None = None):
    """Reject any ACL/path expansion beyond the manifest-derived read-only set."""
    # Build the exact expected form using the same manifest-bound read set.
    directory = Path(effective_attempt_dir).resolve()
    expected = _base_config(directory)
    relatives = _manifest_paths(manifest)
    extra = [*relatives, *(str((directory / rel).resolve()) for rel in relatives)]
    rules = [{"action": "read", "resource": value, "effect": "allow"} for value in extra]
    expected["permissions"].extend(rules)
    next(iter(expected["agents"].values()))["permissions"] = expected["permissions"]
    if config != expected:
        raise ValueError("effective config differs from exact manifest-scoped read-only ACL")
    identity = {"schema": CONFIG_SCHEMA, "default_permission": "deny",
                "relative_read_resources": ["input.json", "leaf.md", "source", "source/**", *relatives],
                "absolute_material_reads": ["{attempt}/" + path for path in relatives],
                "agent": {"name": "atlas-factory-{attempt_sha256_12}", "mode": "primary",
                          "description": "Atlas read-only factory proposal agent"},
                "policies": config["policies"], "materials_manifest_digest": _sha(_canonical(manifest)),
                "config_digest": _sha(_canonical(_normalized_config(config, directory)))}
    if expected_identity is not None and identity != expected_identity:
        raise ValueError("effective read-only config identity differs from its binding")
    return identity


def _normalized_config(config: dict, attempt_dir: Path):
    """Canonicalize only attempt-specific absolute paths and derived agent key.

    Callers validate the complete concrete config against the exact expected ACL
    before using this digest, so normalization cannot forgive policy changes.
    """
    directory = Path(attempt_dir).resolve()
    normalized = json.loads(json.dumps(config))
    permissions = normalized.get("permissions", [])
    for rule in permissions:
        resource = rule.get("resource") if isinstance(rule, dict) else None
        if isinstance(resource, str) and resource.startswith(str(directory) + "/"):
            rule["resource"] = "{attempt}/" + resource[len(str(directory) + "/"):]
    agents = normalized.get("agents", {})
    if len(agents) == 1:
        name, value = next(iter(agents.items()))
        expected_name = "atlas-factory-" + _sha(str(directory).encode())[:12]
        if name != expected_name:
            raise ValueError("derived agent name differs from the resolved attempt directory")
        agent_permissions = value.get("permissions", []) if isinstance(value, dict) else []
        for rule in agent_permissions:
            resource = rule.get("resource") if isinstance(rule, dict) else None
            if isinstance(resource, str) and resource.startswith(str(directory) + "/"):
                rule["resource"] = "{attempt}/" + resource[len(str(directory) + "/"):]
        normalized["agents"] = {"atlas-factory-{attempt_sha256_12}": value}
    return normalized
