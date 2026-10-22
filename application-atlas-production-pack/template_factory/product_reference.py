"""ProductReference v1 validation, scope selection, and deterministic rendering."""
from __future__ import annotations

import hashlib
import json
import re
from typing import Any

SCHEMA = "atlas.product-reference.v1"
ROOT_KEYS = {
    "schema", "product_shape", "roles", "objects", "actions", "surfaces",
    "journeys", "rules", "assertions", "scope_options", "basis", "gaps",
}
COLLECTIONS = (
    "roles", "objects", "actions", "surfaces", "journeys", "rules",
    "assertions", "scope_options", "basis", "gaps",
)
KINDS = {"web", "desktop", "cli", "api", "library", "other"}
BASIS_KINDS = {"requirement", "upstream_observation", "design_inference", "unknown"}
ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9_-]*$")


def _fail(path: str, message: str) -> None:
    raise ValueError(f"{path}: {message}")


def _keys(value: Any, required: set[str], path: str) -> None:
    if not isinstance(value, dict):
        _fail(path, "must be an object")
    missing = required - value.keys()
    extra = value.keys() - required
    if missing:
        _fail(path, f"missing keys: {', '.join(sorted(missing))}")
    if extra:
        _fail(path, f"unsupported keys: {', '.join(sorted(extra))}")


def _text(value: Any, path: str) -> None:
    if not isinstance(value, str) or not value.strip():
        _fail(path, "must be a nonblank string")


def _id(value: Any, path: str) -> None:
    _text(value, path)
    if not ID_PATTERN.fullmatch(value):
        _fail(path, "must use lowercase letters, digits, underscores, or hyphens")


def _text_list(value: Any, path: str, *, nonempty: bool = False) -> None:
    if not isinstance(value, list):
        _fail(path, "must be a list")
    if nonempty and not value:
        _fail(path, "must not be empty")
    for index, item in enumerate(value):
        _text(item, f"{path}[{index}]")


def _id_list(value: Any, path: str, *, nonempty: bool = False) -> None:
    if not isinstance(value, list):
        _fail(path, "must be a list")
    if nonempty and not value:
        _fail(path, "must not be empty")
    for index, item in enumerate(value):
        _id(item, f"{path}[{index}]")
    if len(value) != len(set(value)):
        _fail(path, "must not contain duplicate IDs")


def _acyclic(graph: dict[str, list[str]], path: str) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            _fail(path, f"dependency cycle includes {node}")
        if node in visited:
            return
        visiting.add(node)
        for child in graph[node]:
            visit(child)
        visiting.remove(node)
        visited.add(node)

    for node in graph:
        visit(node)


def validate_reference(spec: dict[str, Any], *, source_ids: set[str] | None = None) -> dict[str, Any]:
    """Validate a complete ProductReference v1 and return it unchanged.

    Malformed JSON-like Python values are normalized to ValueError, keeping the
    caller's contract stable even when a nested value has the wrong type.
    """
    try:
        return _validate_reference(spec, source_ids=source_ids)
    except ValueError:
        raise
    except (TypeError, KeyError, AttributeError) as error:
        raise ValueError(f"malformed ProductReference: {error}") from error


def _validate_reference(spec: dict[str, Any], *, source_ids: set[str] | None) -> dict[str, Any]:
    _keys(spec, ROOT_KEYS, "reference")
    if spec["schema"] != SCHEMA:
        _fail("schema", f"must equal {SCHEMA}")
    shape = spec["product_shape"]
    _keys(shape, {"name", "audience", "value", "delivery_profile", "boundary", "excluded"}, "product_shape")
    for key in ("name", "audience", "value", "delivery_profile", "boundary"):
        _text(shape[key], f"product_shape.{key}")
    _text_list(shape["excluded"], "product_shape.excluded")

    row_keys = {
        "roles": {"id", "name", "goal", "data_scope"},
        "objects": {"id", "name", "fields", "states", "relations"},
        "actions": {"id", "name", "role_ids", "object_ids", "surface_ids", "rule_ids", "preconditions", "effects", "failures", "basis_ids", "depends_on", "transitions"},
        "surfaces": {"id", "name", "kind", "purpose", "role_ids", "action_ids", "sections", "navigation", "states", "query"},
        "journeys": {"id", "name", "goal", "role_ids", "steps", "completion", "recovery"},
        "rules": {"id", "statement", "object_ids", "basis_ids"},
        "assertions": {"id", "given", "when", "then", "negative", "action_ids", "rule_ids", "journey_ids"},
        "scope_options": {"id", "name", "journey_ids", "extra_action_ids", "depends_on", "rationale"},
        "basis": {"id", "kind", "statement", "source_ids", "depends_on"},
        "gaps": {"id", "statement", "core", "action_ids", "resolution"},
    }
    by: dict[str, dict[str, dict[str, Any]]] = {}
    id_paths: dict[str, str] = {}
    for collection in COLLECTIONS:
        rows = spec[collection]
        if not isinstance(rows, list):
            _fail(collection, "must be a list")
        if collection in {"roles", "objects", "actions", "surfaces", "journeys", "assertions"} and not rows:
            _fail(collection, "must not be empty")
        by[collection] = {}
        for index, row in enumerate(rows):
            path = f"{collection}[{index}]"
            _keys(row, row_keys[collection], path)
            _id(row["id"], f"{path}.id")
            if row["id"] in id_paths:
                _fail(f"{path}.id", f"duplicate ID also used by {id_paths[row['id']]}")
            id_paths[row["id"]] = path
            by[collection][row["id"]] = row

    def refs(row: dict[str, Any], key: str, target: str, path: str, *, nonempty: bool = False) -> None:
        _id_list(row[key], f"{path}.{key}", nonempty=nonempty)
        for ref in row[key]:
            if ref not in by[target]:
                _fail(f"{path}.{key}", f"unknown {target} ID {ref}")

    def texts(row: dict[str, Any], keys: tuple[str, ...], path: str) -> None:
        for key in keys:
            _text(row[key], f"{path}.{key}")

    for row in spec["roles"]:
        path = f"roles.{row['id']}"
        texts(row, ("name", "goal", "data_scope"), path)

    for row in spec["objects"]:
        path = f"objects.{row['id']}"
        _text(row["name"], path + ".name")
        _text_list(row["states"], path + ".states")
        if not isinstance(row["fields"], list) or not isinstance(row["relations"], list):
            _fail(path, "fields and relations must be lists")
        for index, field in enumerate(row["fields"]):
            field_path = f"{path}.fields[{index}]"
            _keys(field, {"name", "meaning"}, field_path)
            texts(field, ("name", "meaning"), field_path)
        for index, relation in enumerate(row["relations"]):
            relation_path = f"{path}.relations[{index}]"
            _keys(relation, {"object_id", "meaning"}, relation_path)
            _id(relation["object_id"], relation_path + ".object_id")
            _text(relation["meaning"], relation_path + ".meaning")

    for row in spec["actions"]:
        path = f"actions.{row['id']}"
        _text(row["name"], path + ".name")
        for key, target in (("role_ids", "roles"), ("object_ids", "objects"), ("surface_ids", "surfaces"), ("rule_ids", "rules"), ("basis_ids", "basis"), ("depends_on", "actions")):
            refs(row, key, target, path, nonempty=key in {"role_ids", "object_ids", "surface_ids", "basis_ids"})
        _text_list(row["preconditions"], path + ".preconditions", nonempty=True)
        _text_list(row["effects"], path + ".effects", nonempty=True)
        if not isinstance(row["failures"], list) or not row["failures"]:
            _fail(path + ".failures", "must be a nonempty list")
        for index, failure in enumerate(row["failures"]):
            failure_path = f"{path}.failures[{index}]"
            _keys(failure, {"condition", "response", "recovery"}, failure_path)
            texts(failure, ("condition", "response", "recovery"), failure_path)
        if not isinstance(row["transitions"], list):
            _fail(path + ".transitions", "must be a list")
        for index, transition in enumerate(row["transitions"]):
            transition_path = f"{path}.transitions[{index}]"
            _keys(transition, {"object_id", "from_states", "to_state"}, transition_path)
            _id(transition["object_id"], transition_path + ".object_id")
            _text_list(transition["from_states"], transition_path + ".from_states")
            _text(transition["to_state"], transition_path + ".to_state")

    for row in spec["surfaces"]:
        path = f"surfaces.{row['id']}"
        texts(row, ("name", "purpose"), path)
        if not isinstance(row["kind"], str) or row["kind"] not in KINDS:
            _fail(path + ".kind", "unsupported surface kind")
        for key, target in (("role_ids", "roles"), ("action_ids", "actions"), ("navigation", "surfaces")):
            refs(row, key, target, path, nonempty=key != "navigation")
        _text_list(row["sections"], path + ".sections")
        _keys(row["states"], {"loading", "empty", "no_results", "error", "forbidden"}, path + ".states")
        for key, value in row["states"].items():
            _text(value, f"{path}.states.{key}")
        _keys(row["query"], {"search", "filter", "sort", "pagination", "bulk", "export"}, path + ".query")
        for key, value in row["query"].items():
            _text(value, f"{path}.query.{key}")

    for row in spec["journeys"]:
        path = f"journeys.{row['id']}"
        texts(row, ("name", "goal", "completion", "recovery"), path)
        refs(row, "role_ids", "roles", path, nonempty=True)
        if not isinstance(row["steps"], list) or not row["steps"]:
            _fail(path + ".steps", "must be a nonempty list")
        for index, step in enumerate(row["steps"]):
            step_path = f"{path}.steps[{index}]"
            _keys(step, {"surface_id", "action_id", "role_id", "success"}, step_path)
            for key in ("surface_id", "action_id", "role_id"):
                _id(step[key], f"{step_path}.{key}")
            _text(step["success"], step_path + ".success")
            for key, target in (("surface_id", "surfaces"), ("action_id", "actions"), ("role_id", "roles")):
                if step[key] not in by[target]:
                    _fail(f"{step_path}.{key}", f"unknown {target} ID {step[key]}")
            action = by["actions"][step["action_id"]]
            surface = by["surfaces"][step["surface_id"]]
            if (step["surface_id"] not in action["surface_ids"] or step["role_id"] not in action["role_ids"]
                    or step["role_id"] not in surface["role_ids"] or step["role_id"] not in row["role_ids"]):
                _fail(step_path, "action, surface, journey, and role are incompatible")

    for row in spec["rules"]:
        path = f"rules.{row['id']}"
        _text(row["statement"], path + ".statement")
        refs(row, "object_ids", "objects", path)
        refs(row, "basis_ids", "basis", path)

    for row in spec["assertions"]:
        path = f"assertions.{row['id']}"
        texts(row, ("given", "when", "then", "negative"), path)
        refs(row, "action_ids", "actions", path, nonempty=True)
        refs(row, "rule_ids", "rules", path)
        refs(row, "journey_ids", "journeys", path)

    for row in spec["scope_options"]:
        path = f"scope_options.{row['id']}"
        texts(row, ("name", "rationale"), path)
        refs(row, "journey_ids", "journeys", path)
        refs(row, "extra_action_ids", "actions", path)
        refs(row, "depends_on", "scope_options", path)
        if not row["journey_ids"] and not row["extra_action_ids"]:
            _fail(path, "must select a journey or extra action")

    for row in spec["basis"]:
        path = f"basis.{row['id']}"
        _text(row["statement"], path + ".statement")
        refs(row, "depends_on", "basis", path)
        _id_list(row["source_ids"], path + ".source_ids")
        if not isinstance(row["kind"], str) or row["kind"] not in BASIS_KINDS:
            _fail(path + ".kind", "unsupported basis kind")
        if source_ids is not None:
            unknown = set(row["source_ids"]) - source_ids
            if unknown:
                _fail(path + ".source_ids", f"untrusted source IDs: {', '.join(sorted(unknown))}")
        if row["kind"] == "upstream_observation":
            if not row["source_ids"]:
                _fail(path, "upstream observations require trusted source IDs")
            if source_ids is None:
                _fail(path, "source_ids must be supplied for upstream observations")
        if row["kind"] == "design_inference":
            dependencies = [by["basis"].get(dep) for dep in row["depends_on"]]
            if not dependencies or all(dep["kind"] == "unknown" for dep in dependencies):
                _fail(path, "design inference requires a known basis dependency")

    for row in spec["gaps"]:
        path = f"gaps.{row['id']}"
        texts(row, ("statement", "resolution"), path)
        refs(row, "action_ids", "actions", path)
        if not isinstance(row["core"], bool):
            _fail(path + ".core", "must be boolean")
        if row["core"]:
            _fail(path, "unknown core gap blocks a reviewable reference")

    for obj in spec["objects"]:
        for relation in obj["relations"]:
            if relation["object_id"] not in by["objects"]:
                _fail(f"objects.{obj['id']}.relations", f"unknown object ID {relation['object_id']}")
    for action in spec["actions"]:
        path = f"actions.{action['id']}"
        if not any(action["id"] in assertion["action_ids"] for assertion in spec["assertions"]):
            _fail(path, "every action must be asserted")
        for transition in action["transitions"]:
            obj = by["objects"].get(transition["object_id"])
            if obj is None or transition["object_id"] not in action["object_ids"]:
                _fail(path + ".transitions", "transition object must be a referenced action object")
            states = set(obj["states"])
            if transition["to_state"] not in states or any(state not in states for state in transition["from_states"]):
                _fail(path + ".transitions", "transition claims a state not declared by its object")
        for surface_id in action["surface_ids"]:
            surface = by["surfaces"][surface_id]
            if action["id"] not in surface["action_ids"]:
                _fail(path + ".surface_ids", f"missing symmetric link from surface {surface_id}")
            if not set(action["role_ids"]).intersection(surface["role_ids"]):
                _fail(path, f"no action role can use surface {surface_id}")
    for surface in spec["surfaces"]:
        for action_id in surface["action_ids"]:
            if surface["id"] not in by["actions"][action_id]["surface_ids"]:
                _fail(f"surfaces.{surface['id']}.action_ids", f"missing symmetric link from action {action_id}")
    for assertion in spec["assertions"]:
        for rule_id in assertion["rule_ids"]:
            if not any(rule_id in by["actions"][action_id]["rule_ids"] for action_id in assertion["action_ids"]):
                _fail(f"assertions.{assertion['id']}.rule_ids", f"rule {rule_id} is not used by its asserted actions")
    for rule in spec["rules"]:
        if not any(rule["id"] in assertion["rule_ids"] for assertion in spec["assertions"]):
            _fail(f"rules.{rule['id']}", "every rule must be referenced by an assertion")

    _acyclic({row["id"]: row["depends_on"] for row in spec["actions"]}, "actions.depends_on")
    _acyclic({row["id"]: row["depends_on"] for row in spec["scope_options"]}, "scope_options.depends_on")
    _acyclic({row["id"]: row["depends_on"] for row in spec["basis"]}, "basis.depends_on")
    return spec


def select_scope(spec: dict[str, Any], scope_id: str, *, source_ids: set[str] | None = None) -> dict[str, Any]:
    """Select a minimal coherent slice; keep the full reference unchanged."""
    validate_reference(spec, source_ids=source_ids)
    scopes = {row["id"]: row for row in spec["scope_options"]}
    if scope_id not in scopes:
        raise ValueError(f"unknown scope option ID {scope_id}")
    selected_scopes: set[str] = set()

    def add_scope(selected_id: str) -> None:
        if selected_id in selected_scopes:
            return
        selected_scopes.add(selected_id)
        for dependency in scopes[selected_id]["depends_on"]:
            add_scope(dependency)

    add_scope(scope_id)
    journeys = {row["id"]: row for row in spec["journeys"]}
    actions = {row["id"]: row for row in spec["actions"]}
    rules = {row["id"]: row for row in spec["rules"]}
    basis = {row["id"]: row for row in spec["basis"]}
    journey_ids = {jid for sid in selected_scopes for jid in scopes[sid]["journey_ids"]}
    action_ids = {aid for sid in selected_scopes for aid in scopes[sid]["extra_action_ids"]}
    for journey_id in journey_ids:
        action_ids.update(step["action_id"] for step in journeys[journey_id]["steps"])

    def add_action_dependencies(action_id: str) -> None:
        for dependency in actions[action_id]["depends_on"]:
            if dependency not in action_ids:
                action_ids.add(dependency)
                add_action_dependencies(dependency)

    for action_id in list(action_ids):
        add_action_dependencies(action_id)
    role_ids = {role_id for journey_id in journey_ids for role_id in journeys[journey_id]["role_ids"]}
    object_ids = {object_id for action_id in action_ids for object_id in actions[action_id]["object_ids"]}
    for action_id in action_ids:
        role_ids.update(actions[action_id]["role_ids"])
    objects = {row["id"]: row for row in spec["objects"]}
    while True:
        related = {relation["object_id"] for object_id in object_ids for relation in objects[object_id]["relations"]}
        new_related = related - object_ids
        if not new_related:
            break
        object_ids.update(new_related)
    surface_ids = {sid for action_id in action_ids for sid in actions[action_id]["surface_ids"]}
    rule_ids = {rid for action_id in action_ids for rid in actions[action_id]["rule_ids"]}
    assertion_ids = set()
    for assertion in spec["assertions"]:
        if (set(assertion["action_ids"]).issubset(action_ids)
                and set(assertion["journey_ids"]).issubset(journey_ids)):
            assertion_ids.add(assertion["id"])
            rule_ids.update(assertion["rule_ids"])
    selected_assertions = [row for row in spec["assertions"] if row["id"] in assertion_ids]
    for action_id in action_ids:
        if not any(action_id in row["action_ids"] for row in selected_assertions):
            raise ValueError(
                f"scope {scope_id} is incomplete: selected action {action_id} has no "
                "assertion independent of deferred actions; add a separate assertion"
            )
    for rule_id in rule_ids:
        if not any(rule_id in row["rule_ids"] for row in selected_assertions):
            raise ValueError(
                f"scope {scope_id} is incomplete: selected rule {rule_id} has no "
                "selected assertion; add an assertion covering this rule"
            )
    for journey_id in journey_ids:
        if not any(journey_id in row["journey_ids"] for row in selected_assertions):
            raise ValueError(
                f"scope {scope_id} is incomplete: selected journey {journey_id} has no "
                "selected assertion; add an assertion covering this journey"
            )
    object_ids.update(object_id for rule_id in rule_ids for object_id in rules[rule_id]["object_ids"])
    while True:
        related = {relation["object_id"] for object_id in object_ids for relation in objects[object_id]["relations"]}
        new_related = related - object_ids
        if not new_related:
            break
        object_ids.update(new_related)
    basis_ids = {bid for action_id in action_ids for bid in actions[action_id]["basis_ids"]}
    basis_ids.update(bid for rule_id in rule_ids for bid in rules[rule_id]["basis_ids"])
    pending = list(basis_ids)
    while pending:
        for dependency in basis[pending.pop()]["depends_on"]:
            if dependency not in basis_ids:
                basis_ids.add(dependency)
                pending.append(dependency)
    deferred_action_ids = [row["id"] for row in spec["actions"] if row["id"] not in action_ids]
    digest_input = json.dumps(spec, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return {
        "scope_id": scope_id,
        "journey_ids": sorted(journey_ids),
        "action_ids": sorted(action_ids),
        "role_ids": sorted(role_ids),
        "object_ids": sorted(object_ids),
        "rule_ids": sorted(rule_ids),
        "assertion_ids": sorted(assertion_ids),
        "surface_ids": sorted(surface_ids),
        "basis_ids": sorted(basis_ids),
        "deferred_action_ids": deferred_action_ids,
        "reference_digest": hashlib.sha256(digest_input.encode("utf-8")).hexdigest(),
        "reference": spec,
    }


def render_reference(spec: dict[str, Any], *, source_ids: set[str] | None = None) -> dict[str, str]:
    """Return canonical JSON and readable Markdown with stable local anchors."""
    validate_reference(spec, source_ids=source_ids)
    canonical = json.dumps(spec, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    lines = [
        f"# {spec['product_shape']['name']}", "", f"Schema: `{SCHEMA}`", "",
        "## Product shape", "",
        f"- 受众 / Audience: {spec['product_shape']['audience']}",
        f"- 价值 / Value: {spec['product_shape']['value']}",
        f"- 交付形态 / Delivery profile: {spec['product_shape']['delivery_profile']}",
        f"- 边界 / Boundary: {spec['product_shape']['boundary']}",
        "- 排除项 / Excluded: " + ("；".join(spec["product_shape"]["excluded"]) or "None specified"), "",
    ]
    sections = (
        ("roles", "Roles"), ("objects", "Objects"), ("actions", "Actions"),
        ("surfaces", "Surfaces"), ("journeys", "Journeys"), ("rules", "Rules"),
        ("assertions", "Assertions"), ("scope_options", "Scope options"),
        ("basis", "Basis"), ("gaps", "Gaps"),
    )

    labels = {
        "goal": "目标 / Goal", "data_scope": "数据范围 / Data scope",
        "fields": "字段 / Fields", "states": "状态 / States", "relations": "关系 / Relations",
        "meaning": "含义 / Meaning", "role_ids": "角色 / Roles", "object_ids": "对象 / Objects",
        "surface_ids": "入口 / Surfaces", "rule_ids": "规则 / Rules", "preconditions": "前置条件 / Preconditions",
        "effects": "效果 / Effects", "failures": "失败与恢复 / Failures and recovery",
        "condition": "条件 / Condition", "response": "反馈 / Response", "recovery": "恢复 / Recovery",
        "basis_ids": "依据 / Basis", "depends_on": "依赖 / Dependencies", "transitions": "状态转换 / Transitions",
        "from_states": "起始状态 / From", "to_state": "目标状态 / To", "kind": "形态 / Kind",
        "purpose": "用途 / Purpose", "action_ids": "操作 / Actions", "sections": "区块 / Sections",
        "navigation": "导航 / Navigation", "loading": "加载 / Loading", "empty": "空数据 / Empty",
        "no_results": "无结果 / No results", "error": "错误 / Error", "forbidden": "无权限 / Forbidden",
        "query": "查询行为 / Query behavior", "search": "搜索 / Search", "filter": "筛选 / Filter",
        "sort": "排序 / Sort", "pagination": "分页 / Pagination", "bulk": "批量 / Bulk",
        "export": "导出 / Export", "steps": "步骤 / Steps", "success": "成功结果 / Success",
        "completion": "完成条件 / Completion", "statement": "说明 / Statement", "given": "给定 / Given",
        "when": "当 / When", "then": "则 / Then", "negative": "负向检查 / Negative check",
        "journey_ids": "旅程 / Journeys", "extra_action_ids": "额外操作 / Extra actions",
        "rationale": "理由 / Rationale", "source_ids": "来源 / Sources", "core": "核心缺口 / Core gap",
    }

    def linked(value: Any, key: str = "") -> str:
        if isinstance(value, str) and (key.endswith("_id") or key.endswith("_ids")):
            return f"[{value}](#{value})"
        return value if isinstance(value, str) else str(value)

    def append_value(lines_out: list[str], key: str, value: Any, indent: int = 0) -> None:
        prefix = "  " * indent + "- "
        label = labels.get(key, key.replace("_", " ").capitalize())
        if isinstance(value, dict):
            lines_out.append(f"{prefix}{label}:")
            for child_key, child_value in value.items():
                append_value(lines_out, child_key, child_value, indent + 1)
        elif isinstance(value, list):
            lines_out.append(f"{prefix}{label}:")
            for index, item in enumerate(value, 1):
                if isinstance(item, dict):
                    lines_out.append("  " * (indent + 1) + f"{index}. ")
                    for child_key, child_value in item.items():
                        append_value(lines_out, child_key, child_value, indent + 2)
                else:
                    lines_out.append("  " * (indent + 1) + f"- {linked(item, key)}")
        else:
            lines_out.append(f"{prefix}{label}: {linked(value, key)}")

    for collection, title in sections:
        lines.extend((f"## {title}", ""))
        for row in spec[collection]:
            label = row.get("name") or row.get("statement") or row.get("goal") or row["id"]
            lines.extend((f"### {row['id']}", f"**{label}**", ""))
            for key, value in row.items():
                if key == "id" or (key == "name" and collection in {"roles", "objects", "actions", "surfaces", "journeys", "scope_options"}):
                    continue
                append_value(lines, key, value)
            lines.append("")
    return {
        "PRODUCT_REFERENCE.md": "\n".join(lines).rstrip() + "\n",
        "PRODUCT_REFERENCE.json": canonical,
    }
