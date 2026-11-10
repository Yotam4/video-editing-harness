#!/usr/bin/env python3
"""Validate the recipe registry and observable routing scenarios."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from classify_content import classify

ROOT = Path(__file__).resolve().parents[1]


def validate(registry: dict, root: Path) -> bool:
    patterns = registry["patterns"]
    ids = [p["id"] for p in patterns]
    assert len(ids) == len(set(ids)), "Duplicate type IDs"
    for p in patterns:
        for key, axis in [("formats", "format"), ("possible_purposes", "purpose"), ("suggested_audience_stages", "audience_stage")]:
            assert set(p[key]) <= set(registry["axes"][axis]), f"Unknown {axis} in {p['id']}"
        assert p["cta_policy"] == "optional", f"Forced CTA in {p['id']}"
        for skill in p["skills"]:
            assert (root / "skills" / skill / "SKILL.md").is_file(), f"Missing skill {skill} in {p['id']}"
    try:
        import jsonschema
    except ImportError:
        print("warning: jsonschema is unavailable; structural/integrity checks ran, JSON Schema validation did not", file=sys.stderr)
        return False
    else:
        schema = json.loads((root / "registry" / "content-types.schema.json").read_text())
        try:
            jsonschema.Draft202012Validator.check_schema(schema)
            jsonschema.validate(registry, schema)
        except (jsonschema.SchemaError, jsonschema.ValidationError) as exc:
            raise ValueError(f"JSON Schema validation failed: {exc.message}") from exc
        return True


def smoke(registry: dict) -> list[str]:
    scenarios = []
    result = classify("A carousel of three springs for the weekend", registry)
    assert result["status"] == "matched" and result["selected_type"] == "route-collection"
    assert result["axes"]["audience_stage"] == "unknown", "A content recipe must not assign funnel readiness"
    scenarios.append("known place collection routes without assigning a funnel stage")

    result = classify("A carousel or a reel showing an app demo", registry)
    assert result["status"] == "needs_choice" and result["selected_type"] is None
    scenarios.append("mixed media formats request a choice instead of silently selecting a deliverable")

    result = classify("An interactive location-aware live audio scavenger experience", registry)
    assert result["status"] == "unclassified" and result["new_type_candidate"]["status"] == "needs_review"
    assert result["new_type_candidate"]["automatically_registered"] is False
    scenarios.append("unfamiliar structure becomes a review candidate, not an automatically installed skill")

    result = classify("A funny moment with friends as a reel", registry, purpose="entertainment", stage="none", cta="none")
    assert result["selected_type"] == "humor-observation" and result["axes"]["cta"] == "none"
    assert result["axes"]["audience_stage"] == "not_applicable"
    scenarios.append("entertainment preserves an explicit no-funnel, no-CTA choice")

    result = classify("A commercial app demo", registry, format_hint="carousel")
    assert all("carousel" in c["allowed_formats"] for c in result["candidates"])
    assert result["axes"]["format"] == "carousel", "commercial intent is not a format"
    scenarios.append("an explicit carousel format excludes video-only production recipes")

    result = classify("An app demo", registry, format_hint="reel", stage="bofu")
    assert result["selected_type"] == "app-screen-demo" and result["axes"]["format"] == "short_video"
    assert result["axes"]["placement"] == "reels" and result["axes"]["audience_stage"] == "action"
    scenarios.append("Reel and BOFU aliases populate independent format/placement/stage axes")

    result = classify("We want people to understand our forum. We have real screenshots, but no current screen recording. What should we make?", registry)
    assert result["selected_type"] != "app-screen-demo"
    assert any(x["phrase"] == "screen recording" for x in result["excluded_signals"])
    scenarios.append("an explicitly missing recording is not treated as evidence for a screen demo")

    result = classify("Make the highlight orange", registry, revision=True, existing_type="feature-walkthrough", format_hint="carousel")
    assert result["selected_type"] == "feature-walkthrough" and result["classification_basis"] == "existing_record"
    assert result["new_type_candidate"]["automatically_registered"] is False
    result = classify("Make it orange", registry, revision=True)
    assert result["status"] == "needs_choice" and result["selected_type"] is None
    scenarios.append("a small approved revision inherits its existing recipe, or requests its record rather than inventing a new type")
    return scenarios


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=ROOT / "registry" / "content-types.json")
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    try:
        registry = json.loads(args.registry.read_text())
        schema_validated = validate(registry, ROOT)
        scenarios = smoke(registry) if args.smoke else []
        print(json.dumps({"valid": True, "json_schema_validation": "passed" if schema_validated else "not_run_missing_dependency", "recipes": len(registry["patterns"]), "smoke_scenarios": scenarios}, indent=2))
    except (AssertionError, OSError, ValueError, KeyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
