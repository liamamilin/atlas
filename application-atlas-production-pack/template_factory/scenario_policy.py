"""Host-owned, identity-bound scenario guidance for cognition production."""

import json
from copy import deepcopy
from pathlib import Path

BOOKMARK_SCENARIO_ID = "scn_7756e0007f6a463a97316f3f49c15248"
BOOKMARK_PRODUCT_ID = "product-c42848f63251507bd9d911a5"

BOOKMARK_POLICY = {
    "schema": "atlas.scenario-policy.bookmarks.v1",
    "revision": "CP-1",
    "scenario_id": BOOKMARK_SCENARIO_ID,
    "product_id": BOOKMARK_PRODUCT_ID,
    "category_contract": {
        "management": {
            "acceptance_id": "A04",
            "operations": ["category_create", "category_rename"],
            "input_field": "name",
            "existing_category_identity_field": "category_id",
            "html_invalid_values": ["omitted", "empty", "whitespace_only", "121_characters"],
            "json_invalid_values": ["omitted", "empty", "whitespace_only", "121_characters", "null"],
            "invalid_result": {"status": 400, "code": "invalid_name"},
            "html_failure": "Show form-error, retain submitted values, and make no writes.",
            "json_failure": "Return invalid_name and make no writes.",
        },
        "bookmark_save": {
            "acceptance_id": "A12",
            "json_field": "category",
            "html_field": "category",
            "field_semantics": "Category NAME, never category ID.",
            "omitted_or_null_json": "Use the default category.",
            "html_null": "HTML forms have no native null value.",
            "invalid_values": ["empty", "whitespace_only", "121_characters"],
            "invalid_result": {"status": 400, "code": "invalid_category"},
            "html_failure": "Show form-error, retain submitted values, and make no writes.",
            "valid_new_name": "Automatically create and use the named category.",
        },
        "bookmark_move": {
            "acceptance_id": "A12",
            "json_field": "category",
            "json_semantics": "Category NAME, never category ID.",
            "invalid_json_values": ["omitted", "JSON null", "empty", "whitespace_only", "121_characters"],
            "html_field": "category_id",
            "html_semantics": "Resolve the submitted ID to an existing category name.",
            "invalid_html_values": ["omitted", "empty", "unknown_id"],
            "invalid_result": {"status": 400, "code": "invalid_category"},
            "html_failure": "Show form-error, retain submitted values, and make no writes.",
            "valid_new_json_name": "Automatically create and use the named category.",
            "never_create_from_html_id": True,
        },
        "unknown_get_filter": "Return an empty result; do not treat an unknown category filter as an error.",
    },
    "search_contract": (
        "Search is a case-insensitive substring over title, hostname, and description, "
        "with optional category filtering applied together. Search does not match tags "
        "or raw URL substrings."
    ),
    "url_policy": {
        "schemes": ["http", "https"],
        "absolute": True,
        "nonempty_valid_hostname": True,
        "single_label_hosts": True,
        "dns_required": False,
        "preserve_original_text": True,
        "p0_fetch": False,
    },
    "authorized_assertion_adaptation": (
        "A02 may replace only its single-label-hostname rejection example with a positive "
        "example; missing scheme, unsupported scheme, empty hostname, and invalid hostname "
        "must remain rejected without writing."
    ),
    "adaptation": (
        "The source IndexedDB/Dexie and SPA are source facts. Adapt persistence and "
        "rendering to the declared target profile; do not turn source facts into target "
        "requirements. Preserve the exact A04 category-management and A12 bookmark "
        "save/move contracts above, plus the title/hostname/description search contract."
    ),
}


def policy_for(scenario, product_id=None):
    """Return policy only for the exact host-owned scenario/product binding."""
    if not isinstance(scenario, dict):
        return None
    if scenario.get("id") != BOOKMARK_SCENARIO_ID:
        return None
    if product_id != BOOKMARK_PRODUCT_ID:
        return None
    return deepcopy(BOOKMARK_POLICY)


def policy_prompt(policy):
    """Render a bound policy for a production/review source document."""
    if not isinstance(policy, dict):
        return ""
    return "Host-owned policy for this exact scenario/product identity:\n" + "\n".join(
        f"- {key}: {value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, sort_keys=True)}"
        for key, value in policy.items()
        if key not in {"schema", "scenario_id", "product_id"}
    )


def write_architecture_review_material(directory, case_design, policy):
    """Persist case choices and their bound policy for architecture review."""
    if not isinstance(policy, dict):
        return []
    directory = Path(directory)
    files = {
        "CASE_DESIGN.json": case_design,
        "CASE_ADAPTATION_POLICY.json": policy,
    }
    for name, value in files.items():
        (directory / name).write_text(
            json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    return list(files)
