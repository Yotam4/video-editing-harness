#!/usr/bin/env python3
"""Transparent recipe assistance. Lexical scores are not semantic confidence."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "registry" / "content-types.json"
FORMAT_ALIASES = {"reel": "short_video", "video": "short_video", "static": "single_image", "story": "story_sequence"}
STAGE_ALIASES = {"tofu": "discovery", "mofu": "evaluation", "bofu": "action", "none": "not_applicable"}
FORMAT_PHRASES = {
    "carousel": ["carousel", "carousels", "קרוסלה", "קרוסלת"],
    "short_video": ["reel", "reels", "short video", "video", "ריל", "רילס", "סרטון", "וידאו"],
    "single_image": ["single image", "static image", "static post", "תמונה בודדת", "פוסט תמונה"],
    "story_sequence": ["instagram story", "instagram stories", "story sequence", "סטורי", "סטוריז"],
}


def normalize(value: str) -> str:
    text = unicodedata.normalize("NFKC", value).casefold()
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", text)).strip()


def has_phrase(text: str, phrase: str) -> bool:
    return re.search(r"(?<!\w)" + re.escape(normalize(phrase)) + r"(?!\w)", text) is not None


def signal_present(text: str, phrase: str) -> tuple[bool, bool]:
    """Return positive and simply negated occurrences, without semantic claims."""
    positive = False
    negative = False
    for match in re.finditer(r"(?<!\w)" + re.escape(normalize(phrase)) + r"(?!\w)", text):
        prefix = text[:match.start()]
        # Avoid turning 'no current screen recording' into available recording
        # evidence. Limited lexical scope, explicitly not a full language parser.
        negated = re.search(r"(?:^|\s)(?:no|not|without|אין|בלי|ללא|לא)(?:\s+\w+){0,3}\s+$", prefix)
        qualified_not = re.search(r"(?:not only|not just)(?:\s+\w+){0,2}\s+$", prefix)
        if negated and not qualified_not:
            negative = True
        else:
            positive = True
    return positive, negative


def classify(brief: str, registry: dict, *, format_hint: str | None = None,
             placement: str | None = None, stage: str = "unknown",
             purpose: str | None = None, cta: str | None = None,
             campaign: str = "undecided", asset_mode: str = "undecided",
             known_inputs: list[str] | None = None, revision: bool = False,
             existing_type: str | None = None) -> dict:
    text = normalize(brief)
    known_inputs = set(known_inputs or [])
    # Only remove simple explicit exclusions for format detection. This is not
    # a general natural-language negation parser; explicit flags are stronger.
    format_text = re.sub(r"\bnot (?:a )?(?:reel|carousel|video)\b", " ", text)
    format_text = re.sub(r"לא (?:ריל|קרוסלה|סרטון)", " ", format_text)
    mentions = sorted(f for f, phrases in FORMAT_PHRASES.items()
                      if any(has_phrase(format_text, p) for p in phrases))
    if format_hint:
        selected_format = FORMAT_ALIASES.get(format_hint, format_hint)
    else:
        selected_format = mentions[0] if len(mentions) == 1 else None
    if format_hint == "reel" and placement is None:
        placement = "reels"
    stage = STAGE_ALIASES.get(stage, stage)
    candidates = []
    excluded_signals = []
    pattern_ids = {p["id"] for p in registry["patterns"]}
    if existing_type and existing_type not in pattern_ids:
        raise ValueError(f"unknown existing type: {existing_type}")
    for pattern in registry["patterns"]:
        if selected_format and selected_format not in pattern["formats"]:
            continue
        evidence = []
        score = 0
        for group in pattern["match_signals"]:
            signals = [(p, signal_present(text, p)) for p in group["phrases"]]
            hits = [p for p, (positive, _) in signals if positive]
            for phrase, (_, negative) in signals:
                if negative:
                    excluded_signals.append({"type_id": pattern["id"], "phrase": phrase,
                                             "reason": "simple_explicit_negation_or_absence"})
            if hits:
                # Synonyms in one group count once, preventing verbosity from
                # creating a higher score simply by repeating equivalent terms.
                score += group["weight"]
                evidence.append({"phrases": hits, "weight": group["weight"]})
        if purpose and purpose in pattern["possible_purposes"] and score:
            score += 1
            evidence.append({"purpose_hint": purpose, "weight": 1})
        inherit = revision and pattern["id"] == existing_type
        if score or inherit:
            candidates.append({"type_id": pattern["id"], "name": pattern["name"],
                               "lexical_score": score if not revision else 0,
                               "evidence": evidence if not revision else [{"existing_type": existing_type}],
                               "allowed_formats": pattern["formats"],
                               "possible_purposes": pattern["possible_purposes"],
                               "suggested_stages_only": pattern["suggested_audience_stages"],
                               "inputs_to_confirm": [x for x in pattern["required_inputs"] if x not in known_inputs],
                               "proof_requirements": pattern["proof_requirements"],
                               "skills": pattern["skills"],
                               "quality_checks": pattern["quality_checks"]})
    candidates.sort(key=lambda c: (-c["lexical_score"], c["type_id"]))
    top_score = candidates[0]["lexical_score"] if candidates else 0
    close_match = len(candidates) > 1 and candidates[1]["lexical_score"] >= top_score - 1
    format_conflict = not format_hint and len(mentions) > 1
    if top_score < 4:
        status = "unclassified"
    elif format_conflict or close_match:
        status = "needs_choice"
    else:
        status = "matched"
    if revision:
        candidates = [c for c in candidates if c["type_id"] == existing_type]
        status = "matched" if len(candidates) == 1 else "needs_choice"
    chosen = candidates[0] if status == "matched" else None
    questions = []
    if revision and not chosen:
        questions.append("Read the existing content record and supply its recipe/format; do not reclassify a short approved revision from the change request alone.")
    if format_conflict:
        questions.append("The brief names multiple formats: choose one deliverable or plan separate variants.")
    if status == "unclassified":
        questions.append("What is the viewer meant to receive, and what structure or example should this resemble?")
    elif status == "needs_choice" and not revision:
        questions.append("Choose the main content recipe; the runner-up may be a supporting treatment or a separate variant.")
    if not purpose and not revision:
        questions.append("What is the intended outcome: enjoyment, connection, useful knowledge, understanding, or a specific action?")
    if not selected_format and not revision:
        questions.append("Which production format should we use, or should brainstorming compare formats first?")
    if chosen and len(chosen["allowed_formats"]) > 1 and not selected_format:
        questions.append("The selected recipe supports several formats; recipe selection does not settle the production format.")
    candidate_review = status == "unclassified" and not revision
    proposed_format = (chosen["allowed_formats"][0] if chosen and len(chosen["allowed_formats"]) == 1 else None)
    return {
        "mode": "transparent_keyword_assistance_not_semantic_ai",
        "classification_basis": "existing_record" if revision and chosen else "existing_record_needed" if revision else "lexical_assistance",
        "revision_mode": revision,
        "status": status,
        "selected_type": chosen["type_id"] if chosen else None,
        "axes": {"format": selected_format, "placement": placement or "undecided",
                 "audience_stage": stage, "purpose": purpose,
                 "cta": cta, "campaign": campaign, "asset_mode": asset_mode},
        "format_proposal_only": proposed_format if not selected_format else None,
        "format_mentions": mentions,
        "excluded_signals": excluded_signals,
        "candidates": candidates[:3],
        "questions": questions,
        "new_type_candidate": {"status": "needs_review" if candidate_review else "not_suggested",
                               "reason": "Missing context and a genuinely new pattern are both possible; compare existing recipes before registering anything." if candidate_review else "Use or compare existing recipes before proposing a new one.",
                               "automatically_registered": False},
        "record_path_template": "docs/content/<format>/<type-id-or-candidate>/<slug>/",
        "limitations": ["Scores describe matched phrases, not probability, audience readiness or expected performance.",
                        "Stage is supplied explicitly; recipe suggestions never establish the viewer's funnel position.",
                        "Required assets, facts and permissions are not inferred from prompt words.",
                        "Absence of a CTA is valid; a blank CTA remains an undecided editorial choice.",
                        "This helper does not create records, skills, media, schedules or publications."],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("brief", nargs="?", help="Brief text; omit to read standard input")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--format", dest="format_hint")
    parser.add_argument("--placement")
    parser.add_argument("--stage", default="unknown")
    parser.add_argument("--purpose")
    cta_group = parser.add_mutually_exclusive_group()
    cta_group.add_argument("--cta")
    cta_group.add_argument("--no-cta", action="store_true")
    parser.add_argument("--campaign", default="undecided")
    parser.add_argument("--asset-mode", default="undecided")
    parser.add_argument("--known-input", action="append", default=[], help="Exact required-input key already verified; repeat as needed")
    parser.add_argument("--revision", action="store_true", help="Preserve the existing content recipe for a small approved revision")
    parser.add_argument("--existing-type", help="Existing recipe ID from the content record; use with --revision")
    args = parser.parse_args()
    try:
        registry = json.loads(args.registry.read_text(encoding="utf-8"))
        brief = args.brief if args.brief is not None else sys.stdin.read()
        if not brief.strip():
            parser.error("brief must not be empty")
        if args.existing_type and not args.revision:
            parser.error("--existing-type requires --revision")
        checks = {"format": (FORMAT_ALIASES.get(args.format_hint, args.format_hint), "format"),
                  "placement": (args.placement, "placement"),
                  "stage": (STAGE_ALIASES.get(args.stage, args.stage), "audience_stage"),
                  "purpose": (args.purpose, "purpose"), "cta": (args.cta, "cta"),
                  "campaign": (args.campaign, "campaign"), "asset-mode": (args.asset_mode, "asset_mode")}
        for flag, (value, axis) in checks.items():
            if value is not None and value not in registry["axes"][axis]:
                parser.error(f"invalid --{flag}: {value}; use one of {registry['axes'][axis]}")
        result = classify(brief, registry, format_hint=args.format_hint, placement=args.placement,
                          stage=args.stage, purpose=args.purpose, cta="none" if args.no_cta else args.cta,
                          campaign=args.campaign, asset_mode=args.asset_mode, known_inputs=args.known_input,
                          revision=args.revision, existing_type=args.existing_type)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
