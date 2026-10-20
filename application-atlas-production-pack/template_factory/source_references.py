"""Pure validation for feature-to-source references in authored specifications."""

from __future__ import annotations

import json

from .store import FactoryError, digest


def _source_ids(available_sources):
    if not isinstance(available_sources, (list, tuple)):
        return [], ["available_sources must be a list"]
    ids = []
    errors = []
    for index, row in enumerate(available_sources):
        value = row.get("id") if isinstance(row, dict) else row
        if not isinstance(value, str) or not value:
            errors.append(f"available_sources[{index}] must have a non-empty string id")
            continue
        ids.append(value)
    if len(set(ids)) != len(ids):
        errors.append("available source IDs must be unique")
    return sorted(set(ids)), errors


def feature_source_reference_report(spec, available_sources, *, binding=None):
    """Return complete source-reference validation data without mutating input.

    `available_sources` is the exact scenario-eligible source inventory, not the
    broader case evidence collection. Malformed rows are reported alongside
    every feature that can be inspected.
    """
    available, errors = _source_ids(available_sources)
    features = spec.get("features") if isinstance(spec, dict) else None
    if not isinstance(spec, dict):
        errors.append("spec must be an object")
    if not isinstance(features, list):
        errors.append("spec.features must be a list")
        features = []
    feature_rows = []
    seen_features = set()
    for index, feature in enumerate(features):
        row_errors = []
        if not isinstance(feature, dict):
            feature_rows.append({"index": index, "feature_id": None, "source_ids": None,
                                 "missing_source_ids": [], "errors": ["feature must be an object"]})
            errors.append(f"features[{index}] must be an object")
            continue
        feature_id = feature.get("id")
        if not isinstance(feature_id, str) or not feature_id:
            row_errors.append("feature id must be a non-empty string")
        elif feature_id in seen_features:
            row_errors.append("feature IDs must be unique")
        else:
            seen_features.add(feature_id)
        refs = feature.get("sources")
        if not isinstance(refs, list) or not all(isinstance(item, str) for item in refs):
            row_errors.append("sources must be a list of strings")
            refs = []
        elif len(set(refs)) != len(refs):
            row_errors.append("source IDs must be unique")
        missing = sorted(set(refs) - set(available))
        if missing:
            row_errors.append("source IDs are not available in the bound scenario")
        feature_rows.append({
            "index": index,
            "feature_id": feature_id if isinstance(feature_id, str) else None,
            "source_ids": list(refs),
            "missing_source_ids": missing,
            "errors": row_errors,
        })
        if row_errors:
            errors.extend(f"features[{index}] ({feature_id!r}): {item}" for item in row_errors)
    report = {
        "schema": "atlas.feature-source-reference-report.v1",
        "valid": not errors,
        "spec_digest": digest(spec),
        "available_source_ids": available,
        "binding": binding,
        "binding_digest": digest(binding) if binding is not None else None,
        "features": feature_rows,
        "errors": errors,
    }
    report["report_digest"] = digest({key: value for key, value in report.items() if key != "report_digest"})
    return report


def validate_feature_source_references(spec, available_sources, *, binding=None):
    """Validate source references and return the complete successful report."""
    report = feature_source_reference_report(spec, available_sources, binding=binding)
    if not report["valid"]:
        raise FactoryError(
            "invalid blueprint references: feature sources; report="
            + json.dumps(report, ensure_ascii=False, sort_keys=True),
            "invalid_feature_sources",
            409,
        )
    return report
