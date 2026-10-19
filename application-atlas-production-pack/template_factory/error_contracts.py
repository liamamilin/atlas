"""Host-owned, explicitly scoped negative-branch contracts (not runtime evidence)."""
from .store import FactoryError

BOOKMARK_PRODUCT = "product-c42848f63251507bd9d911a5"
BOOKMARK_SCENARIO = "scn_7756e0007f6a463a97316f3f49c15248"
ERROR_SCHEMA = "atlas.bookmark-error-contract.v1"


def bookmark_bound(snapshot):
    return (snapshot.get("v1", {}).get("product_id") == BOOKMARK_PRODUCT
            and snapshot.get("scenario", {}).get("id") == BOOKMARK_SCENARIO)


def required_branches():
    rows = []

    def add(transport, operation, field, value_kind, code, case, features):
        rows.append({
            "id": ".".join((transport, operation, field, value_kind)),
            "transport": transport, "operation": operation, "field": field,
            "value_kind": value_kind, "status": 400, "code": code,
            "write_effect": "none", "acceptance_ids": [case],
            "feature_ids": features, "implementation": "acceptance/p0_organize.py",
            "response": "form-error and submitted values retained" if transport == "html" else "error.code/message/field",
        })

    for transport in ("html", "json"):
        for operation in ("category_create", "category_rename"):
            kinds = ("omitted", "empty", "whitespace", "overlong_121") + (("null",) if transport == "json" else ())
            for kind in kinds:
                add(transport, operation, "name", kind, "invalid_name", "A04", ["F03"])
        for operation in ("bookmark_save", "bookmark_move"):
            # JSON APIs consume category NAMES. HTML move consumes category IDs.
            field = "category_id" if transport == "html" and operation == "bookmark_move" else "category"
            kinds = (("omitted", "empty", "unknown_id") if field == "category_id"
                     else ("empty", "whitespace", "overlong_121"))
            if operation == "bookmark_move" and transport == "json":
                kinds += ("omitted", "null")
            for kind in kinds:
                add(transport, operation, field, kind, "invalid_category", "A12", ["F04", "F10"])
    return rows


def validate_error_contract(spec, file_plan=None, *, required=False):
    coverage = spec.get("contract_coverage") or {}
    contract = coverage.get("error_contract")
    if contract is None and not required:
        return

    def fail(message):
        raise FactoryError(message, "error_contract_invalid", 409)

    expected = required_branches()
    if not isinstance(contract, dict) or set(contract) != {"schema", "branches"} or contract.get("schema") != ERROR_SCHEMA:
        fail("bound negative error contract is missing or unsupported")
    rows = contract.get("branches")
    if not isinstance(rows, list) or rows != expected:
        fail("negative branches are missing, duplicated, reordered or use a mixed error code/field/transport")
    features = {r["id"]: r for r in spec.get("features", [])}
    cases = {r["id"]: r for r in spec.get("acceptance", [])}
    for branch in rows:
        for aid in branch["acceptance_ids"]:
            case = cases.get(aid, {})
            if case.get("phase") != "P0" or case.get("implementation") != branch["implementation"]:
                fail("negative branch lacks its original P0 acceptance implementation")
            if not set(branch["feature_ids"]) <= set(case.get("features", [])):
                fail("negative branch points to an unrelated acceptance feature")
        for fid in branch["feature_ids"]:
            if not set(branch["acceptance_ids"]) <= set(features.get(fid, {}).get("acceptance", [])):
                fail("negative branch lacks the bidirectional feature/case reference")
    for row in coverage.get("features", []):
        refs = [b["id"] for b in rows if row.get("feature_id") in b["feature_ids"]]
        if row.get("error_branch_ids", []) != refs:
            fail("coverage feature is missing or mixing its negative-branch references")
    if file_plan is not None:
        for row in file_plan:
            refs = [b["id"] for b in rows if row.get("path") == b["implementation"]]
            if row.get("error_branch_ids", []) != refs:
                fail("file plan lacks its explicit negative-branch references")
        if not any(r.get("path") == "acceptance/p0_organize.py" for r in file_plan):
            fail("negative-branch program is absent from the file plan")
